# Informe de revisión y aceptación · Laboratorios SDR v2.0

**Fecha:** 15 de octubre de 2026 · **Alcance:** reconstrucción del manual SDR de cinco prácticas en dos laboratorios de solo recepción, con guía del instructor, respaldo offline verificado y publicación.

> **Quién revisó.** Claude Opus 5.5 hizo la ingeniería, la verificación y las revisiones, por encargo del responsable del repositorio. Los «equipos», «adversarios» y «jueces» de este informe son pasadas de revisión separadas, cada una con su propio criterio, que hizo ese mismo agente. No son personas independientes. Todos los hallazgos son reales y están en el texto o en el código; ninguno es ilustrativo.

## 1. Veredictos

| Veredicto | Resultado |
|---|---|
| **Aceptación documental** | **93,5 / 100: no alcanza el umbral de 95.** Se cumplen las diez condiciones obligatorias (sección 7). Los 6,5 puntos que faltan corresponden sobre todo a procedimientos documentados pero no ejecutados (Ubuntu 24.04, banco físico). Más edición no puede ganarlos honestamente. |
| **Validación de hardware en campo** | **Pendiente.** No se operó el HackRF One, la antena del kit ni el SIGLENT. La prueba en seco de la guía del instructor lo resuelve. |
| **Respaldo offline ADS-B** | **Verificado en software**: SDRangel 7.27.2 (Windows), verificador propio y pyModeS 3.6.0. |
| **Publicación** | Se publicó primero en la rama `sdr-labs-v2`, sin fusionar en `main`, porque no se alcanzó el umbral de aceptación documental. El 15-10-2026, el responsable del repositorio ordenó fusionarla en `main` sabiendo que la puntuación era de 93,5/100 y que la validación en campo seguía pendiente. |

## 2. Evidencia por tipo

| Tipo | Qué incluye |
|---|---|
| **Hechos de las fuentes** | Manual v1.2 del repositorio (`laboratorio_sdr_3.tex`, `main.tex`); fotografía del kit, tomada el 15-10-2026 |
| **Documentación del fabricante o del proyecto** | Documentación de HackRF One (−5 dBm máx., 3,0–3,3 V/50 mA de alimentación de antena, 2–20 MSa/s, ADC de 8 bits); hoja de datos SSA3000X Plus DS0703P E04B; manuales de usuario SSA3000X Plus UM0703P-E01A y SSA3000X UM0703X-E02A; readme de los plugins de SDRangel; packages.ubuntu.com (noble); Snap Store |
| **Pruebas de software ejecutadas** | Compilación LaTeX; SDRangel 7.27.2 para Windows controlado por su API REST (FileInput + ADS-B Demodulator + BFM; valores por defecto leídos de la instancia); `adsb_iq.py`; pyModeS 3.6.0; lectura de los metadatos del `.deb` 7.27.2 de 24.04 |
| **Medidas con instrumentos** | Ninguna |
| **Validación por reproducción offline** | Grabación de dump1090 en SDRangel 7.27.2: 23 847 tramas registradas en 20 s de bucle, 143 distintas, todas con paridad válida |
| **Pendiente de hardware** | Todo lo que necesita HackRF, antena, SIGLENT o Ubuntu (tabla 9 de la guía del instructor) |

## 3. Fase cero · línea base

**Repositorio.** `marcoteran/python-vigilancia-labs` (público), rama `main` en `a301089`, sincronizada con `origin/main`. Había un directorio sin seguimiento, `_historic/`, de notebooks; no se tocó. Fuera del repositorio, la carpeta hermana `../lab_SDR_surveillance_LaTeX/` contiene borradores más antiguos (la copia `main(1).tex` que se entregó corresponde a esa versión); la fuente de referencia fue la del repositorio, más reciente.

**Auditoría de las fuentes (v1.2, cinco prácticas):**

| Contenido v1.2 | Decisión | Destino en v2.0 |
|---|---|---|
| Niveles de evidencia (7 niveles), nota CPR, separación RF/externo | MANTENER | Parte común §0.1.2 y Lab. 02 |
| P1 SDRangel FM | MEJORAR | Lab. 01 completo |
| P1 AM a 1050 kHz | RETIRAR del flujo | Fuera de alcance (la antena del kit no sirve en onda media) |
| P2/P3 transmisión FM conducida, GNU Radio, `grc/` | RETIRAR | Prohibido por la puerta de seguridad; queda en el historial de Git |
| P4 Wi-Fi/OFDM/BLE | RETIRAR | Fuera de alcance |
| P5 ADS-B/Mode S | MEJORAR | Lab. 02 completo |
| Aviso Zadig «Downgrade WCID» | MANTENER y mejorar | Lab. 01 bloque B (más la comprobación del USB ID 1D50 6089) |
| `\MAInsertVisual` con marcadores de posición | RETIRAR | Todas las figuras son TikZ verificadas o la fotografía real |
| Snap con `sudo snap connect ... audio-record` | REVISAR | Solo `raw-usb` (audio-record no hace falta para recibir) |

**Inventario de hardware a partir de la fotografía:** tabla 3 del manual. Etiqueta legible: «LoRa Antenna Kit · 109990225 · SEEED STUDIO · BH1906130003 · 09/24/19». Un distribuidor lista ese SKU con terminación RP-SMA macho y sin frecuencia.

**Línea base de software (verificada el 15-10-2026):** SDRangel v7.27.2 (19-08-2026); herramientas HackRF v2026.01.3; Ubuntu 24.04 `hackrf` 2023.01.1-9build1; snap `sdrangel` 7.27.2; el `.deb` de 24.04 depende de `libuhd4.10.0`, que no existe en noble.

## 4. Iteración 1 · auditoría académica, de RF y pedagógica

| ID | Severidad | Hallazgo | Resolución |
|---|---|---|---|
| I1-01 | CRÍTICO | El manual v1.2 incluía transmisión (P2, P3), fuera del alcance de solo recepción | Retirada; puerta de seguridad «solo recepción» en §0.3 |
| I1-02 | ALTO | Antena del kit no calificada para FM ni 1090 MHz; posible RP-SMA (sin contacto central en el HackRF) | Tabla de decisión PASS/CONDICIONAL/BLOQUEADO, figura de conectores, paso de identificación, criterios de calificación en la guía |
| I1-03 | ALTO | El SIGLENT tiene entrada tipo N; no hay adaptador confirmado | Bloque E y bloque J condicionados; recomendación de compra |
| I1-04 | ALTO | No existía un respaldo ADS-B real («procedimiento conceptual») | Grabación dump1090 convertida, verificada y empaquetada (bloque K) |
| I1-05 | ALTO | `.deb` de SDRangel 7.27.2 para 24.04 no instalable en noble (`libuhd4.10.0`) | Ruta snap; explicación en el manual |
| I1-06 | MEDIO | El instalador de SDRangel para Windows no incluye `hackrf_info` | radioconda como preparación previa; comprobación alternativa en SDRangel |
| I1-07 | MEDIO | El demodulador BFM trae 50 µs de de-énfasis por defecto (verificado); en América es 75 µs | Paso W13 explícito y fila de diagnóstico |
| I1-08 | MEDIO | La frecuencia de 100,9 MHz no se puede asumir en otros lugares | Etiquetada como ejemplo; barrido de banda obligatorio |
| I1-09 | MEDIO | La demodulación sobre el pico DC degrada la señal | Sintonía con desplazamiento (+300 kHz / Δf −300 kHz), figura 8 |
| I1-10 | MEDIO | Faltaban cuestionarios, rúbrica y tiempos realistas | Cuatro cuestionarios (8 + 12 por laboratorio), rúbrica, presupuestos de 210 y 225 min |

**Puerta 1:** procedimientos defendibles, arquitectura solo de recepción, antena tratada explícitamente, requisitos completos. **Superada.**

## 5. Iteración 2 · reconstrucción técnica

Se escribió desde cero. `main.tex` y `guia_instructor.tex` comparten `preambulo_comun.tex`. Los capítulos están en `contenido/`, con un banco único de preguntas que imprime las respuestas solo en la guía. Hay 11 diagramas TikZ en `figuras/`, recuadros de paso con siete partes y de orden de terminal con cinco, y hojas de registro.

Comprobaciones de la puerta 2: compilación en tres pasadas; **todas las páginas** de ambos PDF se renderizaron a imagen y se revisaron. La revisión visual encontró y corrigió:

- título de portada desbordado;
- etiquetas superpuestas en seis figuras;
- desalineación de etiquetas en los recuadros de paso (por `\color` al inicio de una celda `p{}`);
- comillas rectas activas por `babel` en castellano;
- títulos de tabla repetidos sin «continuación»;
- 14 avisos de 461 pt por `\caption` en `longtable` con `\LTright` rígido, causa aislada con un documento mínimo.

Resultado final: **0 errores, 0 desbordes, 0 referencias indefinidas, 0 glifos ausentes**. **Superada.**

## 6. Iteración 3 · revisión adversarial

Seis pasadas, una por perfil. Severidades según el encargo.

| ID | Adversario | Sev. | Hallazgo | Corrección |
|---|---|---|---|---|
| A-01 | Principiante | MEDIO | En el barrido de banda, el pico DC central parece una emisora | Aviso en W10 |
| A-02 | Principiante | BAJO | No se explicaba cómo introducir un desplazamiento negativo | Rueda del ratón o flechas sobre cada dígito |
| B-01 | Instrumentación RF | **ALTO** | El HackRF no tiene preselección: cerca de un SSR (1030 MHz), el pico recibido puede acercarse a −5 dBm (orden de magnitud: unos 90 dBm de PIRE de pico menos unos 93 dB de pérdida a 1 km). Riesgo real en un emplazamiento aeroportuario | Nueva regla en §0.3; RF amp prohibido cerca de SSR/DME; elemento en la lista del instructor |
| B-02 | Instrumentación RF | **ALTO** | La clave del experimento 4 decía que solo el SDR recupera audio, pero el SSA3000X Plus tiene la tecla `Demod` (AM/FM por auriculares) | Clave corregida; extensión opcional `Demod` en el bloque E |
| B-03 | Instrumentación RF | MEDIO | Los rótulos de teclas y el tiempo mínimo de barrido procedían del manual de la serie no Plus | Verificados con UM0703P-E01A: mismas teclas; 900 µs de barrido mínimo |
| B-04 | Instrumentación RF | MEDIO | Pregunta sobre la RBW ambigua (dos opciones defendibles para señales anchas) | Reescrita en términos del piso de ruido sin señal |
| C-01 | Sistemas | MEDIO | Un snap confinado puede no leer archivos fuera del directorio personal | Paso U13 y guía: copiar los datos a `~/` |
| C-02 | Sistemas | MEDIO | El rótulo de la casilla de actualización automática de posición no estaba verificado | Tomado del `.ui` de SDRangel: «Auto-update position», activada por defecto |
| C-03 | Sistemas | MEDIO | SDRangel sobrescribe `My Position` con la ubicación del sistema (medido: la ubicación del equipo de prueba, en Bogotá; coordenadas omitidas a propósito) y puede usar geolocalización por IP | Aviso de privacidad; capturas sin coordenadas |
| D-01 | Protocolo | **ALTO** | Con la referencia del aula, SDRangel situó la aeronave de la grabación en Colombia (6,57 N, −75,95 W); la decodificación CPR local elige la zona equivocada sin aviso | Paso U14 obligatorio (37,0 N 14,0 E); figura 13 con los valores medidos; pregunta 7 del cuestionario final |
| D-02 | Protocolo | MEDIO | Las respuestas Mode S también responden a ACAS, no solo a SSR | Texto corregido |
| D-03 | Protocolo | MEDIO | Faltaban los TC de posición 20–22 (GNSS) y 5–8 (superficie) | Tabla de campos ampliada |
| D-04 | Protocolo | MEDIO | La grabación tiene el tiempo comprimido (`--snip`, inferido: −4250 ft en 178 ms) | Limitaciones declaradas; el verificador marca 4 posiciones sospechosas |
| E-01 | Editor | MEDIO | Cuadros repetidos sin continuación; desbordes; figuras superpuestas | Corregido (sección 5) |
| E-02 | Editor | BAJO | Referencias con URL partidas en columnas estrechas | Lista con fuente, URL y uso |
| F-01 | Instructor | ALTO | Riesgo de sesión fallida sin tráfico ADS-B | Regla del minuto 85, respaldo en cada puesto, criterios de calificación por lugar y hora |
| F-02 | Instructor | MEDIO | Un solo SIGLENT para varios grupos | Rotación de los bloques E y J en la guía |
| F-03 | Instructor | MEDIO | Sin respaldo FM | Grabación con File Sink durante la prueba en seco (canal presente en 7.27.2; procedimiento no ejecutado) |

**Puerta 3:** cero CRÍTICOS abiertos; cero ALTOS abiertos en el flujo documentado; supuestos de hardware calificados; respaldo con evidencia real; sin evidencia fabricada. **Superada.**

## 7. Panel de jueces

| Juez | Máx. | Nota | Deducciones |
|---|---:|---:|---|
| 1 · Corrección científica y de RF | 20 | 19 | Pérdidas de cable y riesgo SSR expresados como órdenes de magnitud a partir de valores típicos |
| 2 · Pedagogía y claridad para principiantes | 20 | 19 | La interfaz de SDRangel se describe sin capturas reales (decisión deliberada: no hay hardware para obtenerlas sin falsearlas); el manual es extenso (59 páginas) |
| 3 · Reproducibilidad práctica | 20 | 17 | Ubuntu 24.04 sin ejecutar; flujo con HackRF real sin ejecutar; respaldo FM con File Sink sin ejecutar. La compilación, el conjunto de datos y la reproducción en Windows sí se ejecutaron |
| 4 · Seguridad del instrumental y validez ADS-B | 15 | 14,5 | Estimación de riesgo SSR basada en potencias típicas, no medidas |
| 5 · Documentación, gráficos y evaluación | 25 | 24 | Visual 9/10 (figuras esquemáticas, algunas tablas densas); evaluación 5/5; diagnóstico y usabilidad para el instructor 5/5; referencias y evidencia reproducible 5/5 |
| **Total** | **100** | **93,5** | |

La puntuación preliminar, antes de la última pasada de mejora, era de unos 93. La pasada verificó los rótulos con el manual del Plus y el rótulo de SDRangel, y corrigió el error de `Demod`, que también se había pasado por alto. No se ajustó ninguna nota para alcanzar el umbral.

**Condiciones obligatorias:**

1. Sin críticos abiertos ✔.
2. Sin altos abiertos en el flujo documentado ✔.
3. Compila ✔.
4. PDF inspeccionado visualmente ✔.
5. Sin figuras ni referencias rotas ✔.
6. Órdenes verificadas o marcadas como pendientes de plataforma ✔.
7. Seguridad documentada ✔.
8. Antena resuelta de forma condicional ✔.
9. Respaldo con evidencia real ✔.
10. Sin afirmaciones engañosas de éxito con hardware ✔.

**Qué falta para llegar a 95:** ejecutar en una instalación limpia de Ubuntu 24.04 los pasos U1–U16 (snap, `raw-usb`, udev, FileInput) y la prueba en seco del Laboratorio 01 con el HackRF y la antena del banco. Son tareas físicas, no de redacción.

## 8. Compilación y revisión visual

- MiKTeX 25.12 / XeTeX 4.16, Windows 11 25H2.
- `laboratorio_sdr_surveillance.pdf`: 59 páginas. `guia_instructor_sdr.pdf`: 22 páginas.
- Tres pasadas cada uno: 0 errores, 0 cajas desbordadas, 0 referencias indefinidas, 0 glifos ausentes; quedan avisos *underfull* en columnas estrechas de tablas, sin efecto visible.
- LuaLaTeX compila el manual (58 páginas).
- `compile-xelatex.bat` se ejecutó y genera los dos PDF.
- Revisión visual: las 59 + 22 páginas, renderizadas a 55 ppp en hojas de contacto de 6 páginas, y las páginas con problemas a 100–110 ppp.

## 9. Respaldo offline: cifras exactas

- Origen: `antirez/dump1090`, `testfiles/modes1.bin`, SHA-256 `3a33e160…5fb3094`, licencia BSD-3, añadido al repositorio el 05-01-2013.
- `.sdriq`: 1 427 504 bytes, SHA-256 `d201250f…74ee5f25d`. Cabecera de 32 bytes: 2 000 000 S/s, 1 090 000 000 Hz, 16 bits, CRC-32 válido.
- Verificador: 430 preámbulos candidatos, 242 tramas válidas (PI = 0: 132; II/SI: 68; AP con ICAO confirmada: 42); ICAO 4D2023, «AMC421»; 60 posiciones, 4 de ellas sospechosas.
- pyModeS 3.6.0: 242/242 coincidencias. Su decodificador con estado rechaza las posiciones con el tiempo del archivo (implican más de 1500 kt) y las acepta con el tiempo escalado ×2000; 52 posiciones comunes, diferencia máxima de 5×10⁻⁶°.
- SDRangel 7.27.2: 143 tramas distintas (126 comunes con el verificador; 17 DF17 adicionales; el verificador halló 1 DF21 que SDRangel no registró); correlación de 5,7 a 62,7 dB (mediana 23,4 dB).
- Prueba de SDRangel: se desempaquetó en una carpeta temporal, sin instalar. Para fijar la referencia, se desactivó el *plugin* de posición de Qt solo en esa copia. La configuración creada (`HKCU\Software\f4exb`, `%LOCALAPPDATA%\f4exb`) se eliminó; no existía antes.

## 10. Limitaciones restantes y acciones del instructor

1. Prueba en seco completa (sección I.11 de la guía), en el aula y a la hora de la clase.
2. Identificar el conector de la antena B y del cable C; confirmar o comprar los adaptadores N–SMA y RP-SMA–SMA.
3. Ejecutar la instalación en Ubuntu 24.04 (snap, `raw-usb`, udev) y abrir la grabación desde `~/`.
4. Calificar la antena B en FM y en 1090 MHz en dos días distintos.
5. Comprobar en el SIGLENT el firmware, la opción AMK, `Demod` y el tiempo de barrido mínimo real en span cero.
6. Valorar la distancia a radares secundarios y DME del lugar de clase.
7. Grabar el respaldo FM con File Sink.
8. Decidir si se publica la fotografía del kit (incluida en el manual; muestra solo equipo y etiquetas de producto).
