# Laboratorios SDR · recepción FM y ADS-B/Mode S

Dos laboratorios universitarios **de solo recepción** con **HackRF One**, **SDRangel 7.27.2** y un analizador **SIGLENT SSA3032X Plus**. Son el complemento con hardware de los notebooks de Python de este repositorio.

**[Manual del estudiante (PDF)](laboratorio_sdr_surveillance.pdf)** · **[Guía del instructor (PDF)](guia_instructor_sdr.pdf)** · versión 2.0 · 15-10-2026 · autor: Marco Teran

| # | Sistema | Laboratorio | Duración | Resultado |
|---|---|---|---|---|
| 01 | Windows 10/11 | *De las ondas de radio al sonido:* recepción FM, SDR y análisis de espectro | 210 min | Audio FM recuperado; espectro y cascada; medidas con marcador en el SIGLENT; comparación de instrumentos |
| 02 | Ubuntu 24.04 LTS | *Del pulso de 1090 MHz a la aeronave en el mapa:* recepción y decodificación ADS-B/Mode S | 225 min | Tramas con paridad válida, tabla de aeronaves, mapa, estadísticas; respaldo offline verificado |

**Implementos:** la lista completa (lo que ya está en el banco, los adaptadores imprescindibles y las mejoras recomendadas), con enlaces de compra comprobados, está en el [README principal](../README.md#implementos-y-dónde-comprarlos).

## Antes de asignarlos

- **Solo recepción.** Ninguna actividad transmite. La edición anterior (cinco prácticas, con transmisión FM conducida, GNU Radio y Wi-Fi/BLE) quedó retirada; sigue disponible en el historial de Git.
- **Antena no calificada.** El banco solo dispone del kit «LoRa Antenna Kit» (Seeed 109990225), sin especificación para 88–108 MHz ni para 1090 MHz y posiblemente con conector RP-SMA. La guía del instructor explica cómo calificarla en el lugar real.
- **Adaptador N.** El SIGLENT tiene entrada tipo N; sin un adaptador N–SMA (o N–RP-SMA), las actividades con el analizador quedan bloqueadas.
- **Estado de validación.** Documentación revisada y compilada; respaldo ADS-B verificado en software (abajo). **No se ha ejecutado ningún paso con el HackRF real, la antena del kit ni el SIGLENT.** La prueba en seco de la guía del instructor es obligatoria.

## Respaldo offline del Laboratorio 02

`datos_adsb/modes1_dump1090_2MSps_1090MHz.sdriq` (1,4 MB): grabación real de 1090 MHz del proyecto [dump1090](https://github.com/antirez/dump1090) (BSD-3, licencia incluida), convertida al formato `.sdriq` de SDRangel con `herramientas/adsb_iq.py`.

| Comprobación | Resultado (15-10-2026) |
|---|---|
| Verificador del repositorio (`adsb_iq.py verificar`) | 430 preámbulos candidatos, 242 tramas con paridad válida (DF0/4/5/11/17/20/21), 1 aeronave: ICAO 4D2023, «AMC421» |
| pyModeS 3.6.0 (decodificador independiente) | 242/242 tramas coinciden campo a campo; 52 posiciones comunes con diferencia ≤ 5×10⁻⁶° |
| SDRangel 7.27.2 Windows, FileInput + ADS-B Demodulator (vía su API REST) | Cabecera aceptada (2 MS/s, 1090 MHz, 16 bits); 143 tramas distintas registradas, todas con paridad válida; aeronave 4d2023/AMC421 con posición 36,98–37,10 °N, 13,79–13,85 °E **solo** con la posición del receptor fijada cerca de 37,0 N 14,0 E |
| Limitaciones | Tiempo comprimido (silencios eliminados, inferido), bucle, una sola aeronave; las tasas y el alcance no tienen significado físico |

`datos_adsb/verificacion_modes1.json` y `datos_adsb/sdrangel_7.27.2_tramas_unicas.csv` contienen la evidencia completa. `SHA256SUMS` permite comprobar la integridad.

## Contenido de la carpeta

```text
lab_SDR_surveillance_LaTeX/
├── laboratorio_sdr_surveillance.pdf   # manual del estudiante (entregable)
├── guia_instructor_sdr.pdf            # guía del instructor, con claves (no distribuir antes de evaluar)
├── main.tex                           # maestro del manual: portada y orden de capítulos
├── guia_instructor.tex                # maestro de la guía del instructor
├── preambulo_comun.tex                # paquetes, recuadros de paso/orden, macros de cuestionario
├── marco-academic.sty                 # sistema visual MARCO ACADEMIC
├── contenido/                         # 00 común, 01 Windows FM, 02 Ubuntu ADS-B, 03 anexos,
│                                      # cuestionarios (fuente única) y cuerpo de la guía
├── figuras/                           # diagramas TikZ y fotografía del kit de antenas
├── datos_adsb/                        # grabación de respaldo, licencia, sumas y evidencia
├── herramientas/adsb_iq.py            # conversor u8 -> .sdriq y verificador Mode S (numpy)
├── INFORME_REVISION.md                # iteraciones, hallazgos, puntuación y estado de validación
├── compile-xelatex.bat, compile-lualatex.bat, Makefile, latexmkrc
```

`build/` (archivos intermedios) y `_hist/` (borradores locales) están excluidos de Git.

## Compilar

Requisitos: MiKTeX o TeX Live recientes con XeLaTeX y los paquetes de `marco-academic.sty` (`libertinus`, `plex-sans`, `sourcecodepro`, `tcolorbox`, `listings`, `babel-spanish`, `siunitx`, `cleveref`, `koma-script`) más `pgf/tikz`, `longtable` y `multirow`.

**Windows (PowerShell), desde esta carpeta:** `.\compile-xelatex.bat` genera los dos PDF.

**Linux/macOS:** `make` (o `make manual`, `make guia`). Manualmente, tres pasadas por documento:

```bash
mkdir -p build
for i in 1 2 3; do xelatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=laboratorio_sdr_surveillance main.tex; done
for i in 1 2 3; do xelatex -interaction=nonstopmode -halt-on-error -output-directory=build -jobname=guia_instructor_sdr guia_instructor.tex; done
cp build/laboratorio_sdr_surveillance.pdf build/guia_instructor_sdr.pdf .
```

Verificado el 15-10-2026 con MiKTeX 25.12 (XeTeX 4.16) en Windows 11: manual de 59 páginas y guía de 22, tres pasadas cada uno, **0 errores, 0 cajas desbordadas, 0 referencias indefinidas, 0 glifos ausentes**. Quedan avisos *underfull* en columnas estrechas de tablas, sin efecto visible. LuaLaTeX también compila el manual.

**Comprobar el respaldo:** `make verificar`, o `python3 herramientas/adsb_iq.py verificar datos_adsb/modes1_dump1090_2MSps_1090MHz.sdriq` (requiere `numpy`).

### Notas técnicas de LaTeX

- `main.tex` no usa `\DocumentMetadata` a propósito: en instalaciones MiKTeX desincronizadas activa el etiquetado experimental `latex-lab/tagpdf`.
- `babel` en castellano convierte `<`, `>` y `"` en caracteres activos: los diagramas cargan la biblioteca TikZ `babel`, y no se usan comillas rectas dentro de `\texttt`.
- `\LTright` es elástico (`0pt plus 1fill`): con un valor rígido, cada `\caption` de `longtable` desborda exactamente el ancho de línea.
