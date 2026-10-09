<p align="center"><img src="assets/banner.svg" alt="Python × Vigilancia · IQV01 · Marco Terán" width="100%"></p>

<p align="center">
  <a href="https://colab.research.google.com/github/marcoteran/python-vigilancia-labs/blob/main/notebooks/01_python_desde_cero.ipynb">Abrir laboratorio 01</a> ·
  <a href="https://colab.research.google.com/github/marcoteran/python-vigilancia-labs/blob/main/notebooks/02_calculos_vigilancia.ipynb">Abrir laboratorio 02</a> ·
  <a href="instructor/guia_instructor.md">Guía del instructor</a>
</p>

# Del primer `print` al eco radar

> **Material completo disponible en este repositorio público.** Abre los laboratorios en Colab o descarga cada notebook para Jupyter. [Estado y validación](docs/estado_entrega.md).

Dos notebooks en español para aprender a convertir una pregunta en un cálculo reproducible. Empieza sin experiencia de programación; termina explorando un haz de antena, calculando un enlace y explicando qué demuestra cada resultado de una cadena de vigilancia.

**Observa → predice → ejecuta → completa → interpreta.** Cada ejercicio muestra el resultado esperado. Los gráficos salen de las mismas fórmulas que estás aprendiendo; dos ilustraciones ayudan a entender los mecanismos. Los controles permiten cambiar un parámetro y ver qué ocurre.

## Abre tu laboratorio

| Laboratorio | Qué construirás | Ejecutar | Descargar |
|---|---|---|---|
| **01 · Tu primer vuelo con Python** | Variables, tipos, listas, decisiones, funciones y un gráfico de entrenamiento | [Abrir en Colab](https://colab.research.google.com/github/marcoteran/python-vigilancia-labs/blob/main/notebooks/01_python_desde_cero.ipynb) | [Notebook .ipynb](https://raw.githubusercontent.com/marcoteran/python-vigilancia-labs/main/notebooks/01_python_desde_cero.ipynb) |
| **02 · De la señal a la vigilancia** | Potencia, señales, propagación, antenas, radar, digitalización y red | [Abrir en Colab](https://colab.research.google.com/github/marcoteran/python-vigilancia-labs/blob/main/notebooks/02_calculos_vigilancia.ipynb) | [Notebook .ipynb](https://raw.githubusercontent.com/marcoteran/python-vigilancia-labs/main/notebooks/02_calculos_vigilancia.ipynb) |

En Colab: **Archivo → Guardar una copia en Drive**. Ejecuta de arriba hacia abajo. Sustituye `None` en los ejercicios y compara tu salida con la referencia. Conserva las unidades. Para reproducir la entrega, reinicia la sesión y ejecuta todo.

No necesitas sensores, archivos de datos, claves ni montar Drive. Google Colab puede requerir una cuenta para ejecutar y guardar. También puedes descargar ambos notebooks y abrirlos con Jupyter.

## Dos ideas para empezar bien

<p align="center"><img src="assets/ilustraciones/01_documento_memoria.png" alt="Ejecutar código crea una variable en la memoria; reiniciar vacía la memoria y conserva el documento y sus resultados guardados" width="900"></p>

**Documento y memoria.** El notebook guarda lo que escribiste y las salidas que conservaste. La sesión mantiene las variables mientras ejecutas. Reiniciar y ejecutar todo permite comprobar que tu resultado se puede repetir.

<p align="center"><img src="assets/ilustraciones/02_enlace_eco.png" alt="Un enlace transmite del avión al receptor; un radar recibe un eco después de la ida y la vuelta" width="900"></p>

**Un recorrido, o ida y vuelta.** El enlace y el eco recorren caminos distintos. Esta diferencia ayuda a elegir el modelo antes de escribir una fórmula.

## Así se ve un cálculo que puedes explorar

<p align="center"><img src="assets/lab02_fig02.png" alt="Factor de arreglo de antena: patrón polar y corte frontal, calculados para 16 elementos separados media longitud de onda" width="900"></p>

**Un haz con significado.** Observa lóbulos, nulos y dirección. Aumenta el número de elementos y explica por qué se estrecha el haz. El modelo usa elementos isotrópicos y conserva el haz posterior: no disfraza un factor de arreglo como una medición de antena real.

<p align="center"><img src="assets/lab02_fig03.png" alt="Curva de potencia del eco radar frente a distancia, con umbral dado y límite del modelo" width="800"></p>

**El viaje de ida y vuelta.** La ecuación radar muestra por qué duplicar distancia reduce el eco 12.04 dB. Cambia potencia, ganancia y sección radar; compara una variable a la vez. El límite mostrado pertenece al modelo didáctico.

Si los widgets no aparecen, los gráficos guardados siguen visibles y puedes cambiar argumentos de las funciones proporcionadas. Los ejercicios numéricos no dependen de los controles.

## Una ruta completa, con material distinto para cada rol

- **Alumnos:** dos notebooks, explicaciones breves, ejemplos y ejercicios. El 01 termina con cuatro preguntas conectadas; el 02, con un diagnóstico consolidado de doce cálculos y una interpretación por capas.
- **Instructor:** [guía de clase](instructor/guia_instructor.md), tiempos, preguntas, errores frecuentes, criterios de avance y [soluciones](instructor/soluciones_02.md). Las soluciones son públicas y están separadas de los notebooks del alumno.
- **Diseño visual:** dos ilustraciones generadas con IA e incrustadas dentro de los notebooks; [prompts y estado de cada figura](prompts/ilustraciones.md). El patrón de antena, la curva radar y los demás gráficos numéricos se calculan con Python.
- **Trazabilidad:** [cobertura del curso](docs/cobertura.md), [modelos y fuentes](docs/referencias.md) e [informe de verificación](docs/verificacion.json).

El primer laboratorio se diseñó para una hora con explicación del instructor. El segundo tiene una ruta guiada de tres horas y cápsulas de ampliación dentro del mismo notebook. Las ampliaciones requieren trabajo adicional; la guía ayuda a elegirlas sin perder la misión final.

## Herramientas, con un propósito claro

| Herramienta | Para qué la usamos |
|---|---|
| Python / `math` | Expresar fórmulas y calcular con números individuales |
| NumPy | Arrays, conversiones, señales, FFT y modelos numéricos |
| Matplotlib | Gráficos con ejes y unidades, patrón polar y ecuación radar |
| pandas | Primera tabla de registros en la ampliación del laboratorio 01 |
| ipywidgets | Controles opcionales de antena y radar |

Para usar Jupyter localmente con Python 3.10 o superior:

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyterlab
```

## Estructura del proyecto

| Carpeta | Contenido |
|---|---|
| `notebooks/` | Los dos laboratorios para alumnos, con figuras guardadas |
| `instructor/` | Guía, soluciones y datos de comprobación |
| `assets/` | Encabezados, gráficos calculados e ilustraciones de mecanismos |
| `prompts/` | Prompts de ilustraciones y publicación |
| `docs/` | Cobertura, referencias y evidencia de verificación |
| `scripts/` | Verificación reproducible |

## Comprobar y contribuir

```bash
python -m pip install -r requirements-dev.txt
python scripts/verificar.py
```

El verificador ejecuta las plantillas y las soluciones en sesiones limpias, coteja **todas** las salidas de ejercicios y comprueba propiedades físicas: R⁻⁴, crecimiento con potencia, dirección y nulos de antena, y aliasing. Guarda salidas estáticas en los notebooks del alumno sin completar sus respuestas. En entornos que impiden abrir sockets puede usarse `--in-process`; el informe declara qué modo se utilizó. No equivale a validar el frontend de Colab ni a una prueba pedagógica con alumnos.

Para proponer una mejora, abre un issue con sección, fórmula, comportamiento esperado y evidencia. Las PR deben mantener unidades, hipótesis explícitas, ejecución completa y separación entre material de alumno e instructor. Evita agregar dependencias si no aportan una capacidad que el alumno necesita.

## Autoría y uso

Diseñado para el curso **Introducción teórica de vigilancia · IQV01**, de **Marco Terán**, a partir de los materiales de clase aportados por el instructor. Los cálculos son modelos didácticos con datos sintéticos; no constituyen especificaciones de equipos ni procedimientos operacionales. Las referencias primarias se enlazan en `docs/referencias.md`.

El repositorio es público para lectura y descarga. No se añade una licencia de reutilización sin que el autor la elija; la visibilidad pública no sustituye esa autorización.
