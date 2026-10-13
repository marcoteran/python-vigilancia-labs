# Auditoría pedagógica y técnica · 13 de octubre de 2026

Para mantenedores. Resume qué se encontró en los dos notebooks, el manual SDR, el README y el verificador; qué se cambió; qué se comprobó y qué queda sin comprobar. Las correcciones están implementadas en el repositorio; este documento no las sustituye.

## 1. Línea base

Estado inicial: rama `main` en `1e89ed0`, sin cambios de contenido pendientes. Las modificaciones locales previas eran solo salidas reejecutadas, marcas de tiempo y metadatos de kernel de una sesión de Jupyter; se restauraron los metadatos de `HEAD`. `lab_SDR_surveillance_LaTeX/` estaba sin seguimiento.

| Medida | NB01 antes | NB01 después | NB02 antes | NB02 después |
|---|---:|---:|---:|---:|
| Celdas | 43 | 62 | 77 | 94 |
| Ejercicios | 8 | 9 | 12 | 12 |
| Imágenes Markdown incrustadas | 2 | 2 | 2 | 2 |
| Gráficos generados | 1 | 2 | 7 | 8 |
| Palabras de texto para el alumno | 939 | 3477 | 3104 | 6354 |
| Plantilla, soluciones y salidas de ejercicios | PASS | PASS | PASS | PASS |

**Hallazgo en la línea base.** `.\.venv\Scripts\python.exe scripts\verificar.py --in-process` **fallaba** en Windows: Q01 no coincidía porque `soluciones.json` se leía con cp1252 y `Ω`/`í` se corrompían. Con `PYTHONUTF8=1` la línea base pasaba con las cifras históricas. Se corrigió el script, no el entorno.

## 2. Problemas principales y correcciones

### Laboratorio 01 · lectura como principiante absoluto (pasada 1)

El notebook era claro pero muy compacto: 939 palabras para todo Python. Faltaban conceptos que el Laboratorio 02 usa sin explicar, y varias secciones presentaban sintaxis sin decir qué hace cada línea.

- Se añadió en cada sección el ciclo **qué es → por qué → cómo se escribe → predice → lee el resultado → modifica**.
- Celdas nuevas: reasignación, `x = x + 1` y notación científica; tabla de formatos de f-string; porciones `[:2]` e índice `-1`; tabla de operadores de comparación; funciones con varios parámetros, valores por defecto, argumentos con nombre y docstring; `return` frente a `print`.
- El ciclo `for` pasó de la ampliación a la ruta principal (§6), con barrido de parámetros y comprensión de lista.
- §7 añade `np.linspace`, `np.arange`, `np.log10` y comparaciones sobre arrays (umbral) con un ejemplo ejecutable.
- §8 añade una lectura línea a línea del gráfico de barras y un gráfico de curvas con `ax.plot`, `label`, `legend` y `ax.set(...)`, el patrón de todos los gráficos del Laboratorio 02.
- La tabla de errores añade cómo leer un *traceback*, `ZeroDivisionError` y el caso «sin error pero el resultado no cuadra».
- Nuevo cierre **«Lo que ya sabes y cómo lo usarás en el Laboratorio 02»**: tabla de correspondencias, lista de comprobación y ejercicio **R01** (ida y vuelta de un pulso a 60 km: 400.0 µs), que anticipa $R=c\Delta t/2$.

**Valoración:** la ruta ya no requiere ninguna construcción sin enseñar. El texto creció 3.7 veces; las nuevas explicaciones son tablas y listas breves junto al código. Esa longitud adicional ya no cabe en una hora con explicación presencial; la guía del instructor lo declara.

### Laboratorio 02 · lectura con solo el Laboratorio 01 (pasada 2)

**Mapa de prerrequisitos.** Construcciones del Laboratorio 02 y dónde se enseñan ahora:

| Construcción | Dónde |
|---|---|
| Notación científica, f-strings con formato, `print` con comas | NB01 §2, §4 |
| Funciones, valores por defecto, argumentos con nombre, docstrings | NB01 §5 |
| `for`, comprensión de lista, desempaquetado `a, b = ...` | NB01 §6, §8; NB02 §4 |
| Arrays, `np.linspace`, `np.arange`, `np.log10`, comparaciones sobre arrays | NB01 §7 |
| `fig, ax = plt.subplots`, `ax.plot`, `ax.set`, leyendas | NB01 §8 |
| Diccionarios, `zip`, `np.isclose` (celda de preparación) | NB02, nota tras la celda inicial |
| FFT, `a *= 2`, subgráficos `ax[0]` | NB02 §3, recuadro «Python nuevo» |
| Números complejos, *broadcasting* `[:, None]`, `axis=0`, `np.maximum`, `deg2rad` | NB02 §5, recuadro y celda de demostración |
| `try` / `except` | NB02 §5 |
| `np.asarray`, `**0.25`, `axhline`, `semilogx` | NB02 §6 |
| `np.where`, `.astype`, indexación con arrays, `step`, `int(texto, base)` | NB02 §8 |
| Semillas aleatorias, `&` y `~` sobre `bool`, `meshgrid`, `hypot`, `contour` | Cápsulas B y D |

Otras correcciones en NB02:

- Portada con objetivos de aprendizaje y un mapa de las nueve secciones con la habilidad de Python de cada una.
- Cada sección principal empieza con **«El problema»** y, cuando faltaba, una intuición física antes de la ecuación.
- Interpretación tras cada cálculo o gráfico central (antes, la mayoría de los gráficos no tenía ninguna) y un experimento concreto con predicción.
- La misión indica qué sección repasar en cada hoja y propone un método de trabajo.
- Las respuestas de «Concluye con evidencia» quedan en un bloque desplegable, para intentarlas antes de verlas.
- Enlace explícito al laboratorio SDR como siguiente paso.

### Exactitud de radar y vigilancia (pasada 3, instructor)

| Hallazgo | Corrección |
|---|---|
| La figura PPM usaba «0 = pulso en la primera mitad», lo contrario de Mode S/ADS-B, sin declararlo | Código y texto siguen la convención Mode S (1 = primera mitad); se explica la fusión de pulsos 0→1 |
| Friis sin definición de variables; presupuesto con números sueltos (`50 + 3 + 8 - 2`) | Tabla de símbolos y unidades; variables con nombre (`pt_dbm`, `gt_dbi`…) con la misma salida |
| `D` designaba a la vez la directividad y el diámetro de la parábola | Diámetro renombrado a $d_{ap}$; las salidas de la cápsula C lo dicen en palabras |
| R⁻² frente a R⁻⁴ solo se mencionaba en texto | Nuevo gráfico normalizado en escala logarítmica (−20 y −40 dB por década) y su interpretación |
| Ecuación radar sin tabla de variables | Tabla con significado y valor del ejemplo; derivación del alcance límite |
| PSR/SSR/ADS-B/MLAT solo en tabla | Distinción cooperativo/no cooperativo y dependiente; por qué se divide por 2; la tabla original se conserva |
| Factor de arreglo sin ecuación | Ecuación con fasores, primer nulo en $\sin\theta=2/N$ y nivel de lóbulos laterales (~−13 dB) |

Sin cambios, por ser correctos: valores numéricos de todos los ejercicios, retardos de Q09 declarados como datos del ejercicio, FFT unilateral, horizonte y Fresnel, Γ/VSWR, SQNR, latencia y disponibilidad. Las salidas esperadas de los 12 ejercicios Q no cambiaron.

### Claridad de los ejercicios

Los 20 ejercicios originales ya mostraban la salida esperada exacta y eran inequívocos. Se añadieron referencias a la sección que repasar (Q01–Q12) y R01. No se encontraron soluciones completas en los notebooks del alumno: los 21 ejercicios conservan `None` y las celdas de ejercicio de NB01 no guardan salidas.

### Manual SDR

| Hallazgo | Corrección |
|---|---|
| Carpeta con 13 borradores `.tex`, 27 figuras (~56 MB) no usadas por la edición activa, `.py` generados y artefactos de compilación | Movidos a `_hist/` (local, fuera de Git); nada se borró. Flowgraphs de referencia en `grc/` |
| La advertencia del equipo hablaba del límite de entrada del HackRF en un contexto de TX donde el instrumento expuesto es el analizador | Advertencia reescrita: proteger la entrada del SIGLENT (consultar su manual) y la del HackRF en RX (−5 dBm según su documentación) |
| Reglas de TX dispersas | Nuevo **protocolo de transmisión conducida** de seis pasos, enlazado desde las prácticas 2 y 3; parada antes de cambiar conexiones también en la práctica 3 |
| Práctica Wi-Fi sin límites de privacidad | Solo recepción; tramas de gestión; sin descifrado ni asociación; sin ejemplos TX de `gr-ieee802-11`; PCAP como datos sensibles; MAC ajenas enmascaradas |
| Falta un marco común de evidencia | Tabla de siete niveles: energía → demodulación → sincronización → trama válida → información decodificada → derivada → externa |
| Posición ADS-B y máximo alcance presentados como datos directos | Nota CPR (tramas par/impar o posición de referencia) y clasificación como información derivada |
| «1.050 MHz» ambiguo en tipografía española; portadora AM sobre la componente DC | Aclarado como 1050 kHz; nota con sintonía desplazada y offset |
| «Fuentes técnicas verificadas» sin una verificación documentada | Renombrado a «de referencia»; recuadro de estado de validación al inicio |
| Título duplicado, sin índice, recuadro de portada vacío, numeración doble («5.4. 3D.»), desborde de 55 pt | Portada con pregunta guía y modalidad RF; índice; secciones sin numeración automática; recuadros alineados con el estilo del paquete; cero desbordes |

Se conservó el alcance de las cinco prácticas. No se eliminó contenido técnico.

### README y verificador

- README rediseñado como página de entrada: ruta de aprendizaje con Mermaid, lanzamiento en Colab, los tres laboratorios con requisitos y relaciones, galería con interpretación honesta, sección SDR con advertencias, instalación en PowerShell sin activar el entorno, metodología, qué valida y qué no el verificador, estructura real y recursos para instructores. Sin insignias de estado, cifras de popularidad ni pruebas no realizadas.
- `verificar.py`: lectura/escritura UTF-8 explícita y comprobación numérica de R01.

## 3. Resultados de las pruebas

| Comprobación | Resultado |
|---|---|
| `.\.venv\Scripts\python.exe scripts\verificar.py --in-process` (Windows, Python 3.14.6, sin `PYTHONUTF8`) | **PASS**: estructura, imágenes incrustadas, plantillas, soluciones, salida exacta de 21 ejercicios, invariantes físicos, controles y alternativas |
| Ausencia de soluciones en los notebooks del alumno | **PASS**: 21/21 ejercicios con `None` |
| Anclas, rutas relativas e imágenes de README, README SDR, guía y CONTRIBUTING | **PASS** (comprobación automática con reglas de anclas de GitHub) |
| Compilación SDR, XeLaTeX ×3 (MiKTeX 25.12) | **PASS**: 0 errores, 0 cajas desbordadas, 0 referencias indefinidas, 0 glifos ausentes; 41 páginas |
| Compilación SDR, LuaLaTeX | **PASS** (una pasada) |
| `compile-xelatex.bat` | **PASS** |
| Revisión visual | Portada, índice, tabla de evidencia, protocolo de TX y gráficos nuevos inspeccionados |

## 4. Limitaciones que siguen abiertas

- **No probado:** el modo por defecto del verificador (kernels en procesos separados) en Windows; Colab; los widgets en un navegador; el renderizado de Mermaid y de los avisos `[!WARNING]` en GitHub; cualquier procedimiento SDR con HackRF One, SIGLENT, SDRangel, GNU Radio o Ubuntu.
- **Sin validación con estudiantes:** la claridad se evaluó por lectura simulada, no con alumnos reales. Los tiempos de la guía del instructor no se han medido con la versión actual.
- **Longitud:** NB01 casi cuadruplica su texto. Si el grupo lo encuentra largo, las secciones §6–§8 y el puente admiten trabajo previo a la clase.
- **Enlaces de Colab:** apuntan a `main` en GitHub; mostrarán esta versión solo después de publicar los cambios.
- **Manual SDR:** los niveles máximos de entrada del SIGLENT y de potencia de salida del HackRF deben confirmarse en los manuales de los equipos de cada banco; el texto remite a ellos en lugar de fijar cifras.
- `docs/cobertura.md` mantiene su numeración de secciones, que no cambió; no se reescribió.

## 5. Trazabilidad

| ID | Problema | Archivo | Corrección |
|---|---|---|---|
| T01 | El verificador fallaba en Windows (cp1252) | `scripts/verificar.py` | Lectura/escritura UTF-8 explícita |
| T02 | NB01 no enseñaba lo que NB02 usa | `notebooks/01_…` | §2, §4–§8 ampliadas; ciclo `for` en la ruta principal |
| T03 | Sin puente NB01→NB02 | `notebooks/01_…` | Tabla, lista de comprobación, R01 y solución |
| T04 | Sintaxis sin explicar en NB02 | `notebooks/02_…` | Recuadros «Python nuevo» y demostración de *broadcasting* |
| T05 | Gráficos sin interpretación | `notebooks/02_…` | «Interpreta» y «Experimenta» tras cada cálculo central |
| T06 | Convención PPM invertida | `notebooks/02_…` | Convención Mode S declarada e implementada |
| T07 | Variables de Friis sin definir | `notebooks/02_…` | Tabla de símbolos y presupuesto con variables con nombre |
| T08 | R⁻² frente a R⁻⁴ sin visualización | `notebooks/02_…` | Nuevo gráfico logarítmico (`assets/lab02_fig04.png`) |
| T09 | Símbolo `D` ambiguo | `notebooks/02_…` | $d_{ap}$ para el diámetro |
| T10 | Respuestas de cierre visibles | `notebooks/02_…` | Bloque desplegable |
| T11 | Carpeta SDR desordenada | `lab_SDR_surveillance_LaTeX/` | `_hist/` local, `grc/`, `build/` ignorado |
| T12 | Advertencia de TX imprecisa | `laboratorio_sdr_3.tex` | Protección de ambas entradas y protocolo enlazado |
| T13 | Sin límites de privacidad Wi-Fi | `laboratorio_sdr_3.tex` | Advertencia y requisito en entregables |
| T14 | Niveles de evidencia implícitos | `laboratorio_sdr_3.tex` | Tabla de siete niveles; notas CPR y estadísticas |
| T15 | Defectos de maquetación del PDF | `main.tex` | Portada, índice, numeración, recuadros, cero desbordes |
| T16 | README no integraba el SDR | `README.md` | Rediseño completo con rutas y enlaces verificados |
| T17 | Guía sin cambios ni nota SDR | `instructor/guia_instructor.md` | Revisión NB01, notas NB02 y sección SDR |
| T18 | Banner con «dos laboratorios» | `assets/banner.svg` | «01 → 02 → SDR» |
