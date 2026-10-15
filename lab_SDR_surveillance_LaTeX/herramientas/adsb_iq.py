"""Prepara y verifica la grabación I/Q de 1090 MHz del plan offline del Laboratorio 02.

Dos órdenes:

  convertir  I/Q de 8 bits sin signo (formato rtl_sdr/dump1090) -> .sdriq de SDRangel
  verificar  demodula un .sdriq o .bin, comprueba la paridad Mode S y resume el contenido

Solo usa numpy y la biblioteca estándar. El demodulador es deliberadamente simple
(sin corrección de errores): lo que informa como válido ha superado la paridad
sin ninguna modificación de bits. Su objetivo es demostrar que la grabación
contiene tramas reales, no competir con SDRangel ni con dump1090.

Ejemplos (desde lab_SDR_surveillance_LaTeX/):
  python herramientas/adsb_iq.py convertir modes1.bin datos_adsb/modes1_2MSps_1090MHz.sdriq
  python herramientas/adsb_iq.py verificar datos_adsb/modes1_2MSps_1090MHz.sdriq --json informe.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
import zlib
from collections import Counter, defaultdict
from math import floor
from pathlib import Path

import numpy as np

# --------------------------------------------------------------------------
# Formato .sdriq (sdrbase/dsp/filerecordinterface.h de SDRangel):
# cabecera empaquetada de 32 bytes, little endian, CRC-32 de los primeros 28.
#   uint32 sampleRate | uint64 centerFrequency | uint64 startTimeStamp (ms)
#   uint32 sampleSize (16 o 24) | uint32 filler = 0 | uint32 crc32
# Con sampleSize = 16 las muestras son pares I,Q int16 intercalados.
# --------------------------------------------------------------------------
HEADER = struct.Struct('<IQQII')


def write_sdriq(path: Path, iq_int16: np.ndarray, rate: int, freq: int, t0_ms: int) -> None:
    head = HEADER.pack(rate, freq, t0_ms, 16, 0)
    crc = zlib.crc32(head) & 0xFFFFFFFF   # CRC-32 estándar, igual que boost::crc_32_type
    with open(path, 'wb') as f:
        f.write(head + struct.pack('<I', crc))
        f.write(iq_int16.astype('<i2').tobytes())


def read_sdriq(path: Path):
    raw = path.read_bytes()
    rate, freq, t0, size, filler = HEADER.unpack_from(raw, 0)
    crc_file = struct.unpack_from('<I', raw, 28)[0]
    crc_ok = (zlib.crc32(raw[:28]) & 0xFFFFFFFF) == crc_file
    if size != 16:
        raise SystemExit(f'Solo se admiten .sdriq de 16 bits; el archivo declara {size}.')
    iq = np.frombuffer(raw, dtype='<i2', offset=32).astype(np.float32)
    meta = dict(sample_rate=rate, center_frequency=freq, start_timestamp_ms=t0,
                sample_size=size, filler=filler, header_crc_ok=crc_ok)
    return iq[0::2] + 1j * iq[1::2], meta


def read_u8(path: Path):
    raw = np.frombuffer(path.read_bytes(), dtype=np.uint8).astype(np.float32) - 127.5
    return raw[0::2] + 1j * raw[1::2]


# --------------------------------------------------------------------------
# Paridad Mode S: polinomio generador de 25 bits 0x1FFF409 (Anexo 10, Vol. IV).
# El resto de 24 bits se compara con lo que cada formato superpone a la paridad.
# --------------------------------------------------------------------------
GEN = 0x1FFF409


def crc_remainder(bits: list[int]) -> int:
    """Resto de dividir el mensaje completo (datos + 24 bits de paridad) por GEN."""
    reg = int(''.join(map(str, bits)), 2)
    n = len(bits)
    for i in range(n - 1, 23, -1):
        if reg >> i & 1:
            reg ^= GEN << (i - 24)
    return reg & 0xFFFFFF


def bits_to_int(bits, a, b):
    """Campo entre los bits a..b (numeración 1-based e inclusiva, como en el estándar)."""
    return int(''.join(map(str, bits[a - 1:b])), 2)


CHARSET = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ##### ###############0123456789######'


def decode_ac13(bits13: int):
    """Altitud de 13 bits (DF0/4/16/20) solo cuando M=0 y Q=1 (incrementos de 25 ft)."""
    m = bits13 >> 6 & 1
    q = bits13 >> 4 & 1
    if m == 0 and q == 1:
        n = (bits13 >> 7) << 5 | ((bits13 >> 5) & 1) << 4 | (bits13 & 0xF)
        return n * 25 - 1000
    return None


def decode_ac12(bits12: int):
    """Altitud de 12 bits de la posición en vuelo (TC 9-18) con Q=1."""
    if bits12 >> 4 & 1:
        n = (bits12 >> 5) << 4 | (bits12 & 0xF)
        return n * 25 - 1000
    return None


# --------------------------------------------------------------------------
# CPR global con un par par/impar (DO-260B §A.1.7)
# --------------------------------------------------------------------------
NZ = 15


def nl(lat: float) -> int:
    if abs(lat) == 87.0:
        return 2
    if abs(lat) > 87.0:
        return 1
    from math import acos, cos, pi
    a = 1 - cos(pi / (2 * NZ))
    b = cos(pi / 180 * abs(lat)) ** 2
    return int(floor(2 * pi / acos(1 - a / b)))


def cpr_global(even, odd, latest_is_odd: bool):
    """even/odd = (lat_cpr, lon_cpr) en [0, 2^17). Devuelve (lat, lon) o None."""
    s = 131072.0
    lat_e, lon_e = even[0] / s, even[1] / s
    lat_o, lon_o = odd[0] / s, odd[1] / s
    d_e, d_o = 360.0 / 60, 360.0 / 59
    j = floor(59 * lat_e - 60 * lat_o + 0.5)
    rlat_e = d_e * (j % 60 + lat_e)
    rlat_o = d_o * (j % 59 + lat_o)
    if rlat_e >= 270:
        rlat_e -= 360
    if rlat_o >= 270:
        rlat_o -= 360
    if nl(rlat_e) != nl(rlat_o):
        return None   # par incompatible: las dos tramas caen en zonas de latitud distintas
    lat = rlat_o if latest_is_odd else rlat_e
    n = max(nl(lat) - (1 if latest_is_odd else 0), 1)
    m = floor(lon_e * (nl(lat) - 1) - lon_o * nl(lat) + 0.5)
    lon = 360.0 / n * (m % n + (lon_o if latest_is_odd else lon_e))
    if lon >= 180:
        lon -= 360
    return round(lat, 5), round(lon, 5)


# --------------------------------------------------------------------------
# Demodulación PPM a 2 MSa/s: un chip de 0,5 µs = una muestra.
# Preámbulo de 8 µs: pulsos en 0; 1,0; 3,5 y 4,5 µs -> muestras 0, 2, 7 y 9.
# Datos desde 8 µs (muestra 16): bit = 1 si el pulso está en la primera mitad.
# --------------------------------------------------------------------------
def demodulate(iq: np.ndarray, rate: int):
    if rate != 2_000_000:
        raise SystemExit('Este verificador sencillo exige 2 MSa/s (un chip por muestra).')
    m = np.abs(iq)
    found = []
    n = len(m) - (16 + 224)
    j = 0
    while j < n:
        p = m[j:j + 16]
        if not (p[0] > p[1] and p[1] < p[2] and p[2] > p[3] and p[3] < p[0] and p[4] < p[0]
                and p[5] < p[0] and p[6] < p[0] and p[7] > p[8] and p[8] < p[9] and p[9] > p[6]):
            j += 1
            continue
        high = (p[0] + p[2] + p[7] + p[9]) / 6.0
        if p[4] >= high or p[5] >= high or any(p[k] >= high for k in range(11, 15)):
            j += 1
            continue
        d = m[j + 16:j + 16 + 224]
        bits = [1 if d[2 * i] > d[2 * i + 1] else 0 for i in range(112)]
        df = bits_to_int(bits, 1, 5)
        nbits = 112 if df >= 16 else 56
        found.append((j, bits[:nbits], float(high)))
        j += 16 + 2 * nbits   # no buscar otro preámbulo dentro de esta trama
    return found


def classify(candidates):
    """Aplica la regla de paridad propia de cada DF y decodifica campos básicos."""
    # Paso 1: formatos con paridad pura (PI con II=0) o II/SI pequeño.
    confirmed = set()
    frames = []
    for pos, bits, level in candidates:
        df = bits_to_int(bits, 1, 5)
        rem = crc_remainder(bits)
        rec = dict(sample=pos, t_us=pos / 2.0, df=df, hex=f'{int("".join(map(str, bits)), 2):0{len(bits)//4}X}',
                   remainder=f'{rem:06X}', level=round(level, 2))
        if df in (17, 18) and rem == 0:
            rec['valid'] = 'PI=0'
            rec['icao'] = f'{bits_to_int(bits, 9, 32):06X}'
            confirmed.add(rec['icao'])
        elif df == 11 and rem < 80:
            rec['valid'] = f'II/SI={rem}'
            rec['icao'] = f'{bits_to_int(bits, 9, 32):06X}'
            confirmed.add(rec['icao'])
        frames.append((rec, bits))
    # Paso 2: formatos con dirección/paridad (AP): el resto ES la dirección ICAO.
    for rec, bits in frames:
        if 'valid' in rec:
            continue
        if rec['df'] in (0, 4, 5, 16, 20, 21) and rec['remainder'] in confirmed:
            rec['valid'] = 'AP=ICAO confirmada'
            rec['icao'] = rec['remainder']
    return frames


def decode_fields(frames):
    aircraft = defaultdict(lambda: dict(frames=0, df=Counter(), tc=Counter()))
    cpr = defaultdict(dict)
    for rec, bits in frames:
        if 'valid' not in rec:
            continue
        a = aircraft[rec['icao']]
        a['frames'] += 1
        a['df'][rec['df']] += 1
        df = rec['df']
        if df in (0, 4, 16, 20):
            alt = decode_ac13(bits_to_int(bits, 20, 32))
            if alt is not None:
                a['altitude_ft'] = alt
                rec['altitude_ft'] = alt
        if df not in (17, 18):
            continue
        tc = bits_to_int(bits, 33, 37)
        rec['tc'] = tc
        a['tc'][tc] += 1
        if 1 <= tc <= 4:
            cs = ''.join(CHARSET[bits_to_int(bits, 41 + 6 * k, 46 + 6 * k)] for k in range(8))
            a['callsign'] = rec['callsign'] = cs.replace('#', '').strip()
        elif 9 <= tc <= 18:
            alt = decode_ac12(bits_to_int(bits, 41, 52))
            if alt is not None:
                a['altitude_ft'] = rec['altitude_ft'] = alt
            odd = bits[53]
            latlon = (bits_to_int(bits, 55, 71), bits_to_int(bits, 72, 88))
            cpr[rec['icao']]['odd' if odd else 'even'] = (latlon, rec['t_us'])
            rec['cpr'] = dict(format='impar' if odd else 'par', lat_cpr=latlon[0], lon_cpr=latlon[1])
            pair = cpr[rec['icao']]
            if 'even' in pair and 'odd' in pair and abs(pair['even'][1] - pair['odd'][1]) < 10e6:
                pos = cpr_global(pair['even'][0], pair['odd'][0], latest_is_odd=bool(odd))
                if pos:
                    a['position'] = rec['position'] = pos
        elif tc == 19:
            st = bits_to_int(bits, 38, 40)
            if st in (1, 2):
                s_ew, v_ew = bits[45], bits_to_int(bits, 47, 56) - 1
                s_ns, v_ns = bits[56], bits_to_int(bits, 58, 67) - 1
                if v_ew >= 0 and v_ns >= 0:
                    from math import atan2, degrees, hypot
                    vx = -v_ew if s_ew else v_ew
                    vy = -v_ns if s_ns else v_ns
                    a['ground_speed_kt'] = rec['ground_speed_kt'] = round(hypot(vx, vy))
                    a['track_deg'] = rec['track_deg'] = round(degrees(atan2(vx, vy)) % 360, 1)
    # Un par par/impar de tramas separadas en el tiempo real puede caer en zonas de
    # latitud distintas y dar una posición falsa aunque ambas tramas sean válidas.
    # Se marca toda posición a más de 100 km (~0,9°) de la mediana de su aeronave.
    for icao, a in aircraft.items():
        pts = [rec for rec, _ in frames if rec.get('icao') == icao and 'position' in rec]
        if not pts:
            continue
        lat0 = float(np.median([r['position'][0] for r in pts]))
        lon0 = float(np.median([r['position'][1] for r in pts]))
        a['positions'] = len(pts)
        a['suspect_positions'] = 0
        for r in pts:
            if abs(r['position'][0] - lat0) > 0.9 or abs(r['position'][1] - lon0) > 0.9:
                r['position_suspect'] = True
                a['suspect_positions'] += 1
    return aircraft


def cmd_convertir(args):
    src, dst = Path(args.entrada), Path(args.salida)
    u8 = np.frombuffer(src.read_bytes(), dtype=np.uint8)
    if len(u8) % 2:
        raise SystemExit('Número impar de bytes: el archivo no es I/Q intercalado.')
    # 8 bits sin signo con desplazamiento 127,5 -> int16 centrado (factor 256).
    iq16 = np.round((u8.astype(np.float32) - 127.5) * 256.0).astype(np.int16)
    dst.parent.mkdir(parents=True, exist_ok=True)
    write_sdriq(dst, iq16, args.fs, args.fc, args.t0)
    print(f'{dst}  {dst.stat().st_size} bytes  SHA-256 {hashlib.sha256(dst.read_bytes()).hexdigest()}')


def cmd_verificar(args):
    path = Path(args.archivo)
    if path.suffix.lower() == '.sdriq':
        iq, meta = read_sdriq(path)
    else:
        iq = read_u8(path)
        meta = dict(sample_rate=args.fs, center_frequency=args.fc, formato='u8 sin cabecera')
    rate = meta['sample_rate']
    frames = classify(demodulate(iq, rate))
    aircraft = decode_fields(frames)
    valid = [r for r, _ in frames if 'valid' in r]
    report = dict(
        archivo=path.name,
        sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        bytes=path.stat().st_size,
        cabecera=meta,
        muestras_complejas=int(len(iq)),
        duracion_ms=round(len(iq) / rate * 1e3, 3),
        candidatos_preambulo=len(frames),
        tramas_validas=len(valid),
        tramas_por_df=dict(sorted(Counter(r['df'] for r in valid).items())),
        tramas_por_regla=dict(Counter(r['valid'] for r in valid)),
        aeronaves={k: dict(v, df=dict(v['df']), tc=dict(v['tc'])) for k, v in sorted(aircraft.items())},
        tramas=[r for r, _ in frames],
    )
    if not meta.get('header_crc_ok', True):
        print('ATENCIÓN: el CRC de la cabecera .sdriq no coincide; SDRangel rechazará el archivo.')
    print(f"{report['archivo']}: {report['duracion_ms']} ms, {report['candidatos_preambulo']} preámbulos candidatos, "
          f"{report['tramas_validas']} tramas válidas, {len(aircraft)} direcciones ICAO")
    print('Tramas válidas por DF:', report['tramas_por_df'])
    for r in valid:
        extra = ' '.join(f'{k}={r[k]}' for k in ('tc', 'callsign', 'altitude_ft', 'ground_speed_kt', 'track_deg', 'position') if k in r)
        if r.get('position_suspect'):
            extra += '  <- POSICIÓN SOSPECHOSA (par CPR incoherente)'
        print(f"  t={r['t_us']:>9.1f} µs  DF{r['df']:<2} {r['icao']}  {r['hex']}  [{r['valid']}] {extra}")
    for icao, a in report['aeronaves'].items():
        print(f"Aeronave {icao}: {a['frames']} tramas, callsign={a.get('callsign', '-')}, "
              f"posiciones={a.get('positions', 0)} (sospechosas={a.get('suspect_positions', 0)})")
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=1, ensure_ascii=False), encoding='utf-8')
    return 0 if valid else 1


def main(argv=None):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')   # la consola de Windows usa cp1252 por defecto
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='orden', required=True)
    c = sub.add_parser('convertir', help='I/Q u8 (rtl_sdr) -> .sdriq de 16 bits')
    c.add_argument('entrada')
    c.add_argument('salida')
    c.add_argument('--fs', type=int, default=2_000_000, help='tasa de muestreo en S/s (2000000)')
    c.add_argument('--fc', type=int, default=1_090_000_000, help='frecuencia central en Hz (1090000000)')
    c.add_argument('--t0', type=int, default=0, help='marca de tiempo inicial, ms Unix (0)')
    c.set_defaults(func=cmd_convertir)
    v = sub.add_parser('verificar', help='demodula y comprueba la paridad Mode S')
    v.add_argument('archivo')
    v.add_argument('--fs', type=int, default=2_000_000)
    v.add_argument('--fc', type=int, default=1_090_000_000)
    v.add_argument('--json', help='escribe el informe completo en este archivo')
    v.set_defaults(func=cmd_verificar)
    args = p.parse_args(argv)
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
