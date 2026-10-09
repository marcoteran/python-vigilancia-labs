# Prompts de ilustraciones · estado de la entrega

Las figuras **01-A y 02-A se generaron con IA y están integradas**. Los prompts ejecutados, la revisión y las dimensiones reales están en [generacion_ejecutada.md](generacion_ejecutada.md). **01-B y 02-B permanecen como propuestas pendientes.** Los otros PNG son gráficos numéricos calculados con Python; los encabezados se componen con código. El patrón de antena, la curva radar, FFT y TDoA se mantienen como gráficos calculados: no sustituirlos por ilustraciones generativas que puedan falsear escalas o ecuaciones.

## Lenguaje visual común

Figura única, fondo blanco puro #FFFFFF, formato 16:9, 3840 × 2160 px. Geometría de apariencia vectorial, líneas de peso medio, tipografía legible en proyección y amplio espacio negativo. Paleta: Deep Navy #0F2747, Midnight Ink #111827, Refined Blue #2563EB, Soft Sky Blue #60A5FA, Warm Amber #F59E0B, Slate Gray #475569 y Cool Gray #D1D5DB. Rojo solo para error grave; no usar verde dominante. Etiquetas visibles en español. Sin título de póster, sin párrafos, sin paneles de dashboard, sin degradados, sin sombras, sin texturas, sin marca de agua. Las fórmulas exactas se añaden en el notebook, no mediante generación.

## 01-A · Documento y memoria · después de «Habla con el notebook»

```text
Create a single standalone explanatory mechanism figure for an introductory Python notebook, in a pure white 16:9 canvas, 3840×2160. Use the editorial visual language and restricted palette specified below. Show a notebook page with three clearly distinct cell types: a Spanish text line, one code line `tiempo_h = 90 / 60`, and its output `1.5`. Beside it, show a small memory container holding `tiempo_h: 1.5`. Connect the code cell to the memory container with an arrow labeled `Ejecutar`. A separate restart arrow empties the memory container; the page and its saved output remain visible. Exact visible labels: `Texto`, `Código`, `Resultado guardado`, `Memoria de la sesión`, `Reiniciar`. The teaching point is that the saved document and the live session memory are different. Do not depict restarting as erasing the notebook file. No screenshots of real interfaces, no long explanation, no decorative laptop or poster title. Pure white #FFFFFF; navy #0F2747, blue #2563EB, sky blue #60A5FA, amber #F59E0B, slate #475569, gray #D1D5DB. Medium-weight vector-like lines, generous whitespace, large crisp Spanish labels. No dominant green, gradients, shadows, or watermark.
```

## 01-B · Herramientas · apertura de «Caja de herramientas»

```text
Create one standalone figure showing four compact Python tool stations connected to a small aviation training log, on pure white #FFFFFF, 16:9, 3840×2160. Stations have precise short Spanish labels: `math · un número`, `NumPy · varios números`, `Matplotlib · un gráfico`, `pandas · una tabla`. Use a square-root symbol, a row of three numeric tokens, a tiny axis with three bars, and a three-row table respectively. The training log has only `20, 35, 25 min`. Clearly show that these are reusable tools imported into Python, not four programming languages. No package-installation UI, no aircraft photograph, no conceptual formula pretending to be a computed result. Restricted palette navy #0F2747, blue #2563EB, sky blue #60A5FA, amber #F59E0B, slate #475569 and gray #D1D5DB. Crisp vector-like geometry, high contrast, medium lines, balanced whitespace, large Spanish labels. No poster heading, paragraphs, gradients, shadows, dashboard, dominant green, or watermark.
```

## 02-A · Enlace y eco · antes de la ecuación radar

```text
Create one conceptual comparison figure with two horizontally aligned mechanisms on pure white #FFFFFF, 16:9, 3840×2160. Top mechanism: an aircraft transmitter sends one blue arrow to a ground receiver, labeled `Enlace · un recorrido`. Bottom mechanism: a ground radar sends a blue arrow to an aircraft; an amber arrow returns to the same radar, labeled `Eco · ida y vuelta`. Give the target a subtle scattering glyph, not a second active transmitter. Exact short labels: `Transmisión`, `Recepción`, `Dispersión`, `Distancia R`. Both outgoing and return radar paths refer to the same R. This is a mechanism illustration, not a scaled engineering drawing; include no gain curves, no fabricated numerical axes, no equations, no claims of operational coverage. Use navy #0F2747, blue #2563EB, sky blue #60A5FA, amber #F59E0B, slate #475569 and gray #D1D5DB, medium-weight lines, precise arrowheads and generous whitespace. No poster title, paragraphs, gradients, shadows, dashboard, dominant green, photorealism or watermark.
```

## 02-B · Tiempo, origen y calidad · cierre

```text
Create a single conceptual mechanism figure for a university air-surveillance notebook. Pure white #FFFFFF, 16:9, 3840×2160. Show three different incoming observation tokens converging into a small association gate and then one track token. Each incoming token carries three tiny tags with exact Spanish labels `Tiempo`, `Origen`, `Calidad`. One stale token is held aside with an amber clock glyph; do not depict it as automatically false. Use short labels `Observaciones`, `Asociación`, `Track`, `Dato antiguo`. Depict association through time, not arithmetic averaging and not a guaranteed truth machine. No real geographic map, identities, ICAO addresses, system screenshots, numerical specification, formulas, dashboard panels or long paragraphs. Editorial vector-like style; navy #0F2747, blue #2563EB, sky blue #60A5FA, amber #F59E0B, slate #475569 and gray #D1D5DB. Medium-weight lines, projection-safe typography, intentional whitespace. No gradients, shadows, dominant green, poster title or watermark.
```

## Cómo incorporar una nueva ilustración

Guarda la imagen en `assets/ilustraciones/`, conserva el prompt y revisa etiquetas/mecanismo. Inserta el PNG como una URI de datos en una celda Markdown; así se conserva dentro del notebook y no depende de una carpeta vecina ni de enlaces attachment:. Añade texto alternativo. No requiere generar ninguna ilustración para ejecutar los laboratorios actuales.
