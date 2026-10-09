# Modelos y referencias primarias

Las fórmulas del laboratorio se adaptan a datos sintéticos explícitos. Los materiales de IQV01 aportados por Marco Terán determinan el alcance temático; no se publican los archivos fuente de clase.

| Tema | Referencia |
|---|---|
| Python: valores, tipos, control y funciones | [Tutorial oficial de Python](https://docs.python.org/3/tutorial/) |
| Arrays y operaciones | [NumPy: fundamentos para principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html) |
| Figuras y ejes | [Matplotlib: guía rápida](https://matplotlib.org/stable/users/explain/quick_start.html) |
| Tablas | [pandas: primeros pasos](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) |
| Controles interactivos | [ipywidgets: Using Interact](https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html) |
| Abrir notebooks de GitHub en Colab | [googlecolab/open_in_colab](https://github.com/googlecolab/open_in_colab) |
| Radar, ecuación y propagación | [MIT Lincoln Laboratory: Introduction to Radar Systems](https://www.ll.mit.edu/outreach/web-based-course-radar-introduction-radar-systems) |
| Ecuación radar y parámetros | [MathWorks: Radar Equation](https://www.mathworks.com/help/radar/ug/radar-equation.html) |
| Factor de arreglo y elementos isotrópicos | [MathWorks: Element and Array Radiation Patterns](https://www.mathworks.com/help/phased/ug/element-and-array-radiation-patterns-and-responses.html) |
| Arreglo lineal uniforme | [MathWorks: phased.ULA](https://www.mathworks.com/help/phased/ref/phased.ula-system-object.html) |

## Convenciones verificables

- c = 3.00e8 m/s, aproximación de clase.
- Ganancias y pérdidas: lineales dentro de Friis/radar; en dB dentro de presupuestos logarítmicos.
- Factor de arreglo: promedio de campos de N elementos isotrópicos, separación λ/2, fase de dirección dada por seno del ángulo desde broadside. La potencia normalizada es el módulo al cuadrado; corte con piso −40 dB.
- FFT: amplitud unilateral para un seno con muestreo coherente; no duplicar DC ni Nyquist.
- Radar: monostático, RCS fija, umbral dado, sin clutter ni modelo estadístico de detección.
- Retardos de SSR de Q09: datos definidos con marcas temporales del ejercicio; no valores universales de cualquier protocolo.
- Capacidad y disponibilidad: límites o estimaciones bajo hipótesis declaradas, no garantías de servicio.

No se solicita consultar normas cerradas ni documentación de fabricante para completar los ejercicios. Los números del ejercicio no se usan como especificación normativa.
