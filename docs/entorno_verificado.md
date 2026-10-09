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
