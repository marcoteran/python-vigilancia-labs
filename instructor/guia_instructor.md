# Guía del instructor · IQV01

**Marco Terán · dos laboratorios, un cambio de escala:** aprender a expresar una cuenta en Python y después elegir un modelo de vigilancia.

Los alumnos reciben exclusivamente los dos notebooks de `notebooks/`. Este documento contiene tiempos, conducción de clase, respuestas y criterios de avance. No proyectes las soluciones antes del intento. Los gráficos numéricos se calculan con Python. Las dos ilustraciones de documento/memoria y enlace/eco se generaron con IA y están integradas en los notebooks; sus prompts y estado figuran en `prompts/ilustraciones.md`.

## Laboratorio 01 · una hora con tus explicaciones

| Minutos | Sección | Tu intervención | Evidencia del alumno |
|---|---|---|---|
| 0–6 | Habla con el notebook | Abre Colab, guarda copia, ejecuta print. Usa la ilustración para señalar texto/código/resultado y memoria del kernel. | Cambia un aeropuerto y obtiene salida |
| 6–17 | Calculadora y E01 | Escribe una fórmula verbal antes del código. Explica nombre, valor, unidad, `=` y decimal. | E01: 1.5 h |
| 17–27 | Tipos, lista, decisión y E02 | Contrasta texto/número y `=`/`==`. Marca índice cero e indentación. | E02: 10 min; explica condición |
| 27–35 | Función y E03 | Distingue definir y llamar. Haz dos llamadas con entradas distintas. | E03: 0.75 h |
| 35–46 | Librerías, gráfico y E04 | Importar frente a instalar. Lista frente a array. Lee ejes y unidad. | E04: 45 min; cambia una barra |
| 46–57 | Misión M01–M04 | Da un intento individual; pide comparar fórmula, resultado y unidad por parejas. | 120 min, 2 h, 30 min, True |
| 57–60 | Cierre | Reinicia y ejecuta; pregunta por orden y memoria. | Explica una cuenta sin leer el código |

**Revisión de octubre de 2026.** El notebook añadió contenido para que un principiante absoluto pueda llegar al Laboratorio 02 sin construcciones sin explicar: reasignación y notación científica (§2), formatos de f-string, porciones de listas (§4), funciones con valores por defecto y argumentos con nombre (§5), el ciclo `for` y la comprensión de lista (§6, antes solo en la ampliación), `np.linspace`, `np.arange`, `np.log10` y comparaciones sobre arrays (§7), un gráfico de curvas con leyenda (§8) y el puente final con la lista de comprobación y el ejercicio **R01** (ida y vuelta de un pulso: 400.0 µs). La tabla anterior es la propuesta original para el núcleo y **no se ha medido con esta versión**: con explicación presencial, la ruta completa necesita más de una hora. Asigna §6–§8 y el puente como preparación previa, o amplía la sesión.

La sección pandas es ampliación, fuera de la hora central. No enseñes clases, entornos virtuales, instalación ni Git durante este bloque. Si el grupo se atrasa, conserva la misión y muestra una sola modificación del gráfico. No conviertas la explicación de librerías en un catálogo.

### Guion mínimo

- «Antes de ejecutar, ¿qué crees que se imprimirá?»
- «¿Qué representa este número y cuál es su unidad?»
- «¿Cambiaste una fórmula o solo su presentación?»
- «Si reinicio, ¿qué valor deja de existir?»

`None` evita errores mientras el ejercicio está pendiente. Las condiciones de guardia están proporcionadas: el alumno completa la expresión, no tiene que inventar ese mecanismo. En la misión debe resolver las preguntas en orden porque M02–M04 usan M01.

**Criterio de avance:** completa al menos tres de E01–E04, las cuatro partes de la misión y R01; puede explicar una división con unidades, llamar una función e identificar por qué un resultado antiguo no prueba que su código actual funciona. Corrige los fallos antes del laboratorio 02; no uses la rapidez como criterio.

Errores que debes provocar y reparar: variable con mayúscula distinta, texto que se concatena, `^` confundido con potencia, falta de dos puntos y lista dividida por un número. Hazlo en una celda temporal que luego se elimina, para que el archivo entregado ejecute completo.

## Laboratorio 02 · tres horas guiadas

| Minutos | Ruta | Objetivo de tu explicación |
|---|---|---|
| 0–10 | Apertura y unidades | Reusar funciones y escribir SI antes de calcular |
| 10–30 | Alimentación | Medida bajo carga, energía útil y límites de autonomía |
| 30–50 | Señales y ruido | Tiempo/frecuencia, duty, pico/media y sensibilidad |
| 50–70 | Propagación | Friis unidireccional, margen, horizonte y Fresnel |
| 70–95 | Antena y controles | Leer patrón polar, nulos y lóbulos; predecir N y dirección |
| 95–115 | Ecuación radar y controles | Usa enlace/eco antes de R⁻⁴, factores lineales y ganancia doble |
| 115–135 | Observación, digitalización y red | Origen de posición, retardo, aliasing, integridad y latencia |
| 135–173 | Misión Q01–Q12 | Completar en parejas, cotejar salida y justificar modelo |
| 173–180 | Conclusión | Del cálculo favorable a la evidencia por capas |

Las cápsulas «Explora más» se encuentran antes de la misión para mantener el cierre consolidado al final del notebook. En la ruta de tres horas presenta una cápsula relacionada con la dificultad del grupo y asigna las otras como lectura/práctica. Cubrir cada ampliación con explicación presencial requiere otra sesión. **La cobertura del material no implica que todo se pueda enseñar a principiantes en tres horas.**

### Dinámica de los controles

1. Predicción escrita de una frase.
2. Cambio de un solo parámetro y ejecución.
3. Descripción de lo observado con ejes y unidades.
4. Explicación física y límite del modelo.

Antena: 8 → 32 elementos estrecha el haz porque aumenta la apertura con separación fija λ/2. El haz posterior es correcto para elementos isotrópicos sin reflector. La normalización impide deducir ganancia absoluta. Cambiar fases orienta la respuesta, no crea energía.

Radar: duplicar R resta 12.041 dB; duplicar Pt suma 3.010 dB y multiplica el límite por 1.1892. Subir G en 3 dB suma 6 dB al eco. El umbral −110 dBm es dado, no especificación de equipo. σ=10 m² es un valor del ejemplo, no una caracterización de una aeronave específica.

Si el frontend no dibuja controles, usa `dibujar_antena(8, 20)` y `dibujar_radar(100, 30, 10)`. El gráfico estático queda guardado en el notebook. No hay instalación obligatoria ni acceso a sensores.

### Puntos técnicos que no debes omitir

- Cable: longitud completa, corriente constante y resistividad supuesta. Batería: Ah no equivale a Wh; el modelo simplifica descarga y eficiencia.
- FFT: amplitud unilateral de un seno coherente; no espectro de potencia calibrado. RMS del seno, no fórmula universal para cualquier forma.
- Sensibilidad: −174 dBm/Hz corresponde aproximadamente a 290 K. No duplicar NF ni pérdidas ya contabilizadas.
- Propagación: espacio libre y campo lejano; frecuencia y ganancia fija. Horizonte usa refracción estándar, no entorno real. El 60% de Fresnel es condición del ejercicio.
- VSWR: 50/75 Ω resistivos; adaptación perfecta implica Γ=0, VSWR=1 y retorno infinito ideal. La carga extrema exige tratamiento de límites.
- ADC: banda base, filtro previo y seno a escala completa para SQNR. Un ADC de 10 bits no garantiza exactitud de 10 bits.
- SSR: las marcas temporales y retardos de Q09 son datos definidos del ejercicio; no son un decodificador normativo.
- TDoA: cΔt es diferencia de camino, no error de posición. Una pareja no localiza de forma única.
- Red: latencia sin overhead ni retransmisión. Dos rutas pueden compartir alimentación, reloj o red: «independientes» requiere evidencia.
- Diagnóstico: separar síntoma, falla e hipótesis causal. Una detección no garantiza mensaje válido; un mensaje no garantiza track válido.
- PPM: desde octubre de 2026 la figura de §8 sigue la convención de Mode S/ADS-B (1 = pulso en la primera mitad del bit). La versión anterior usaba la convención inversa sin declararla.
- Enlace frente a eco: §6 incluye un gráfico normalizado R⁻² frente a R⁻⁴ en escala logarítmica (−20 dB y −40 dB por década). Úsalo antes de los controles del radar para fijar la diferencia.
- Recuadros «Python nuevo»: explican justo a tiempo FFT, números complejos, *broadcasting*, `try`/`except`, `np.where`, `np.meshgrid` y conversiones grados/radianes. Q06 necesita `np.deg2rad`.

## Laboratorio SDR · complemento con hardware

El manual [`lab_SDR_surveillance_LaTeX/laboratorio_sdr_surveillance.pdf`](../lab_SDR_surveillance_LaTeX/laboratorio_sdr_surveillance.pdf) propone cinco prácticas con HackRF One, SDRangel, GNU Radio y un analizador SIGLENT SSA3032X Plus. No es requisito de los notebooks; los notebooks tampoco bastan como preparación para el banco: el alumno necesita además instalar software en Windows y Ubuntu, manejar hardware RF y conocer las reglas de transmisión conducida.

Antes de asignarlo: ensaya cada práctica con tu banco y las versiones de software instaladas, confirma el atenuador y los niveles máximos de entrada del analizador, y verifica la normativa local de radiofrecuencia. La revisión de este repositorio compiló el PDF y revisó el texto; **no** probó los procedimientos con hardware.

### Preguntas de las cápsulas: respuestas de referencia

| Pregunta | Respuesta breve |
|---|---|
| ¿Fusible intacto prueba alimentación correcta? | No: falta medir bajo carga y respecto a la referencia adecuada. |
| ¿Dónde ubicar el LNA? | Evitar pérdidas previas; respetar saturación, interferencia y diseño del receptor. |
| ¿Por qué una copia puede cancelar? | La fase relativa determina superposición de campos; las potencias no se suman siempre sin término cruzado. |
| ¿Cómo distinguir SINR de SNR? | SINR incluye interferencia además de ruido, sumados en potencia lineal. |
| ¿7 Hz a 10 Hz conserva la señal? | No: las muestras también admiten alias de −3 Hz; el original no se recupera sin información adicional. |
| ¿La curva TDoA es una trayectoria del avión? | No: es el conjunto de posiciones compatibles con una diferencia de llegada. |
| ¿Un dato recibido hace 1 ms puede tener 2 s de edad? | Sí: el timestamp de observación y el de recepción son distintos. |
| ¿Fusionar es promediar PSR y ADS-B? | No: requiere asociación, tiempo, procedencia, incertidumbre y calidad. |

### Evaluación y soluciones

Cada Q permite cotejar el valor, pero pide además una frase de interpretación. Una cifra correcta copiada no demuestra elección de modelo. Acepta expresiones equivalentes y redondeos compatibles con la tolerancia; no exijas que los nombres de pasos intermedios coincidan.

Respuestas completas: [Laboratorio 01](soluciones_01.md), [Laboratorio 02](soluciones_02.md). El script `scripts/verificar.py` ejecuta tanto plantillas como versiones resueltas en sesiones limpias. Las soluciones son públicas en la carpeta instructor; no hay embargo de respuestas.

## Qué está verificado

Las cuentas, invariantes físicos, salidas de cada ejercicio y figuras se comprueban por ejecución local. El informe de `docs/verificacion.json` declara el modo de ejecución. Los controles están escritos con ipywidgets y tienen alternativa por llamada de función. Una prueba local no verifica el frontend de Colab ni equivale a una prueba con alumnos. Antes de impartir, abre cada enlace en Colab y ensaya los controles desde la cuenta que usarás en clase.
