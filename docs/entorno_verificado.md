# Entorno de verificación

Python 3.12.14 · Linux · ejecución local en kernels IPython en memoria.

| Paquete | Versión instalada |
|---|---|
| numpy | 2.5.3 |
| matplotlib | 3.11.2 |
| pandas | 2.3.3 |
| ipywidgets | 8.1.9 |
| nbformat | 5.11.1 |
| nbclient | 0.11.0 |
| ipykernel | 7.4.0 |

Revisión del 9 de octubre de 2026. El entorno gestionado impide abrir sockets; se usó `python scripts/verificar.py --in-process`. Cada ejecución crea y reinicia su kernel en memoria para evitar depender del estado anterior. La opción normal utiliza nbclient con kernels de Jupyter en procesos independientes.

Se probaron plantillas sin respuestas, versiones resueltas, salidas exactas de las 20 actividades, límites de controles, cambios de valores de los widgets mediante Python y sus modelos físicos. Se comprobó también que las cuatro imágenes Markdown incrustadas coinciden exactamente con los PNG del paquete, y que la exportación HTML contiene esas imágenes y los ocho gráficos numéricos sin referencias attachment: pendientes. No se probó arrastrar controles en un navegador ni una sesión remota de Colab. El workflow `.github/workflows/verificar.yml` vuelve a ejecutar las comprobaciones con kernels de Jupyter en GitHub Actions; el resultado de cada ejecución se consulta en la pestaña Actions del repositorio.

## Revisión del 13 de octubre de 2026 · Windows

Python 3.14.6 · Windows 11 Enterprise · `.\.venv\Scripts\python.exe scripts\verificar.py --in-process`.

| Paquete | Versión instalada |
|---|---|
| numpy | 2.5.4 |
| matplotlib | 3.11.2 |
| pandas | 2.3.3 |
| ipywidgets | 8.1.9 |
| nbformat | 5.11.1 |
| nbclient | 0.11.0 |
| ipykernel | 7.4.0 |

Antes de esta revisión, el comando fallaba en Windows aunque los notebooks estaban bien: `verificar.py` leía `instructor/soluciones.json` con la codificación por defecto del sistema (cp1252), y las soluciones con `Ω` o `í` dejaban de coincidir con la salida esperada. Ahora lee y escribe en UTF-8 de forma explícita. No se probó el modo por defecto, con kernels en procesos separados, en este equipo.

Manual SDR: MiKTeX 25.12 (XeTeX 4.16), tres pasadas de XeLaTeX sin errores, sin cajas desbordadas, sin referencias indefinidas y sin glifos ausentes; 41 páginas. LuaLaTeX también compila el documento. No se ensayaron procedimientos con HackRF One ni con el SIGLENT SSA3032X Plus.

## Revisión del 14 de octubre de 2026 · Windows

Python 3.14.6 · Windows 11 Enterprise · mismas versiones de paquetes que el 13 de octubre (numpy 2.5.4, matplotlib 3.11.2, pandas 2.3.3, ipywidgets 8.1.9, nbformat 5.11.1, nbclient 0.11.0, ipykernel 7.4.0).

Se probaron los dos modos: `.\.venv\Scripts\python.exe scripts\verificar.py` (kernels de Jupyter en procesos separados, el mismo modo que GitHub Actions) y `--in-process`. Ambos pasan. Los notebooks publicados se generaron con el modo por defecto, que conserva el orden real de textos y figuras. No se probó Colab ni la interacción con widgets en un navegador.

## Revisión del 15 de octubre de 2026 · laboratorios SDR (edición 2.0)

Windows 11 Enterprise 25H2 · MiKTeX 25.12 (XeTeX 4.16) · Python 3.14.6 con numpy 2.5.4.

- **LaTeX:** manual del estudiante (59 páginas) y guía del instructor (22 páginas), tres pasadas de XeLaTeX cada uno: 0 errores, 0 cajas desbordadas, 0 referencias indefinidas, 0 glifos ausentes. LuaLaTeX compila el manual. Todas las páginas se renderizaron a imagen y se revisaron visualmente.
- **SDRangel 7.27.2 para Windows** (`sdrangel-7.27.2-win64.exe`, SHA-256 `96e4d6c8…dabf74dc2`), desempaquetado en una carpeta temporal y controlado por su API REST: FileInput aceptó la grabación `.sdriq`; el ADS-B Demodulator decodificó la aeronave 4D2023/AMC421 y registró 143 tramas distintas con paridad válida. La configuración que SDRangel creó en el perfil de usuario se eliminó después.
- **Decodificadores independientes:** `herramientas/adsb_iq.py` (242 tramas válidas) y pyModeS 3.6.0 (coincidencia 242/242).
- **No probado:** HackRF One real, antena del kit, SIGLENT SSA3032X Plus, cualquier paso en Ubuntu 24.04 (no había Ubuntu ni WSL disponibles).

## Revisión del 16 de octubre de 2026 · laboratorios SDR (edición 3.0)

Windows 11 Enterprise 25H2 · MiKTeX 25.12 (XeTeX 4.16).

- **LaTeX:** cuatro documentos enlazados con `xr-hyper`, tres rondas de XeLaTeX: manual (23 páginas), Anexo A (17), Anexo B (21) y guía del instructor (18). Cada uno con 0 errores, 0 cajas desbordadas, 0 referencias indefinidas y 0 glifos ausentes, sin «??» en ningún PDF. LuaLaTeX compila el manual. Todas las páginas se renderizaron a imagen y se revisaron visualmente.
- **Sin cambios respecto de la edición 2.0:** la grabación de referencia, sus sumas SHA-256 y la evidencia de SDRangel 7.27.2, `adsb_iq.py` y pyModeS.
- **No probado en esta sesión:** HackRF One, antenas, SIGLENT SSA3032X Plus y Ubuntu 24.04. La guía del instructor los cubre con el ensayo previo de cada curso.
