# Laboratorios SDR · recepción FM y ADS-B/Mode S

Dos laboratorios universitarios **de solo recepción** con **HackRF One**, **SDRangel 7.27.2** y un analizador **SIGLENT SSA3032X Plus**. Son el complemento con hardware de los notebooks de Python de este repositorio.

Edición 3.0 · 16-10-2026 · versión aprobada para uso en clase · autor: Marco Teran

| Documento | Para quién | Contenido |
|---|---|---|
| **[Manual del laboratorio](laboratorio_sdr_surveillance.pdf)** (23 p.) | Estudiante, junto al equipo | Qué hacer, en qué orden y qué debe ver, organizado en etapas |
| **[Anexo A · Fundamentos](anexo_a_fundamentos_sdr.pdf)** (17 p.) | Estudiante, antes y después | Teoría, aclaraciones, seguridad, diagnóstico de fallos, grabación de referencia, glosario y referencias |
| **[Anexo B · Evaluación y registro](anexo_b_evaluacion_sdr.pdf)** (21 p.) | Estudiante, impreso | Cuestionarios diagnóstico y final, 20 hojas de registro, ejercicios, entregables y criterios de evaluación |
| **[Guía del instructor](guia_instructor_sdr.pdf)** (18 p.) | Instructor | Preparación del banco, ensayo previo, conducción de la sesión, claves y respuestas de referencia |

| # | Sistema | Laboratorio | Duración |
|---|---|---|---|
| 01 | Windows 10/11 | *De las ondas de radio al sonido:* recepción FM, SDR y análisis de espectro, en siete etapas | 210 min |
| 02 | Ubuntu 24.04 LTS | *Del pulso de 1090 MHz a la aeronave en el mapa:* recepción y decodificación ADS-B/Mode S, en diez etapas | 225 min |

**Banco:** HackRF One, antena ANT500 (FM), antena de 1090 MHz con base magnética, filtro pasivo de 1090 MHz, cable de extensión SMA, adaptadores SMA, adaptador N -- SMA, SIGLENT SSA3032X Plus y atenuador SMA de 20 dB. La lista con enlaces de compra está en el [README principal](../README.md#implementos-y-dónde-comprarlos).

## Cómo está pensado

- **El manual es corto y solo dice qué hacer.** Cada etapa empieza con una transición que explica de dónde viene el estudiante y qué va a conseguir, y termina con un punto de control. Los pasos tienen siempre la misma forma: dónde, valor, por qué, qué se ve, cómo se verifica y qué hacer si falla.
- **La teoría vive en el Anexo A** y el manual remite a ella con referencias numeradas (enlaces entre los PDF).
- **La evaluación vive en el Anexo B**, un cuaderno imprimible; el manual indica en qué paso completar cada hoja. Las respuestas solo están en la guía del instructor, que usa el mismo banco de preguntas.
- **Hilo conductor:** la escalera de evidencia (energía, demodulación, sincronización, trama válida, información, información derivada, información externa).
- **Momento clave del Laboratorio 02:** la grabación de referencia se reproduce primero con la posición del aula y la aeronave aparece en un lugar imposible. Así el estudiante descubre por sí mismo cómo falla la decodificación CPR con una referencia lejana.

## Grabación de referencia del Laboratorio 02

`datos_adsb/modes1_dump1090_2MSps_1090MHz.sdriq` (1,4 MB): grabación real de 1090 MHz del proyecto [dump1090](https://github.com/antirez/dump1090) (BSD-3, licencia incluida), convertida al formato `.sdriq` de SDRangel con `herramientas/adsb_iq.py`.

| Comprobación | Resultado |
|---|---|
| Verificador del repositorio (`adsb_iq.py verificar`) | 430 preámbulos candidatos, 242 tramas con paridad válida (DF0/4/5/11/17/20/21), 1 aeronave: ICAO 4D2023, «AMC421» |
| pyModeS 3.6.0 | 242/242 tramas coinciden campo a campo; 52 posiciones comunes con diferencia ≤ 5×10⁻⁶° |
| SDRangel 7.27.2 (Windows), FileInput + ADS-B Demodulator | Cabecera aceptada; 143 tramas distintas, todas válidas; posición 36,98–37,10 °N, 13,79–13,85 °E con la referencia en 37,0 N 14,0 E |
| Limitaciones | Tiempo comprimido (silencios eliminados), bucle, una sola aeronave: tasas y alcance sin significado físico |

`datos_adsb/verificacion_modes1.json` y `datos_adsb/sdrangel_7.27.2_tramas_unicas.csv` contienen la evidencia; `SHA256SUMS` permite comprobar la integridad.

## Contenido de la carpeta

```text
lab_SDR_surveillance_LaTeX/
├── laboratorio_sdr_surveillance.pdf   # manual del laboratorio
├── anexo_a_fundamentos_sdr.pdf        # anexo A: fundamentos y referencia técnica
├── anexo_b_evaluacion_sdr.pdf         # anexo B: evaluación y registro
├── guia_instructor_sdr.pdf            # guía del instructor (con claves; no distribuir)
├── main.tex, anexo_a.tex, anexo_b.tex, guia_instructor.tex   # maestros
├── preambulo_comun.tex                # estilos, recuadros, hojas, referencias entre documentos
├── marco-academic.sty                 # sistema visual MARCO ACADEMIC
├── contenido/
│   ├── m00_inicio.tex, m01_lab_fm.tex, m02_lab_adsb.tex   # manual
│   ├── a_fundamentos.tex              # anexo A
│   ├── b_evaluacion.tex               # anexo B
│   ├── cuestionarios.tex              # banco único de preguntas (anexo B y guía)
│   └── guia_instructor_cuerpo.tex     # guía
├── figuras/                           # diagramas TikZ
├── datos_adsb/                        # grabación de referencia, licencia, sumas y evidencia
├── herramientas/adsb_iq.py            # conversor u8 -> .sdriq y verificador Mode S (numpy)
├── INFORME_REVISION.md                # historial de revisión y verificación
└── compile-xelatex.bat, compile-lualatex.bat, Makefile, latexmkrc
```

`build/` (archivos intermedios) y `_hist/` (borradores locales) están excluidos de Git.

## Compilar

Requisitos: MiKTeX o TeX Live recientes con XeLaTeX y los paquetes de `marco-academic.sty` (`libertinus`, `plex-sans`, `sourcecodepro`, `tcolorbox`, `listings`, `babel-spanish`, `siunitx`, `cleveref`, `koma-script`) más `pgf/tikz`, `longtable`, `multirow` y `xr-hyper` (incluido en `hyperref`).

Los cuatro documentos se citan entre sí, así que se compilan juntos en **tres rondas**:

- **Windows (PowerShell), desde esta carpeta:** `.\compile-xelatex.bat`
- **Linux/macOS:** `make`

Verificado el 16-10-2026 con MiKTeX 25.12 (XeTeX 4.16) en Windows 11: los cuatro documentos con **0 errores, 0 cajas desbordadas, 0 referencias indefinidas y 0 glifos ausentes**; todas las páginas revisadas visualmente. LuaLaTeX también compila el manual.

**Comprobar la grabación:** `make verificar`, o `python3 herramientas/adsb_iq.py verificar datos_adsb/modes1_dump1090_2MSps_1090MHz.sdriq` (requiere `numpy`).

### Notas técnicas de LaTeX

- No se usa `\DocumentMetadata` a propósito: en instalaciones MiKTeX desincronizadas activa el etiquetado experimental `latex-lab/tagpdf`.
- `babel` en castellano convierte `<`, `>` y `"` en caracteres activos: los diagramas cargan la biblioteca TikZ `babel`, y no se usan comillas rectas dentro de `\texttt`.
- `\LTright` es elástico (`0pt plus 1fill`): con un valor rígido, cada `\caption` de `longtable` desborda exactamente el ancho de línea.
- Las hojas del Anexo B usan `tabular`, no `longtable`: un formulario no debe partirse entre páginas.
- Los `.bat` deben conservar finales de línea CRLF y texto ASCII: con LF, `cmd.exe` interpreta mal los comentarios.
