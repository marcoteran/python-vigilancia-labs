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
