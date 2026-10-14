# Estado de la entrega · 9 de octubre de 2026

## Lo encontrado

La carpeta de Drive contenía dos notebooks, guía docente, README y un ZIP completo. El paquete incluía encabezados y ocho gráficos generados mediante código; los cuatro prompts de ilustraciones estaban sin ejecutar. El repositorio esperado `marcoteran/python-vigilancia-labs` devolvía 404.

## Trabajo completado

- Generadas e integradas las ilustraciones 01-A (documento/memoria) y 02-A (enlace/eco).
- Revisados los textos, flechas y mecanismos. La primera ilustración incluye un `print` para que su salida sea reproducible.
- Prompts ejecutados conservados con resolución real y estado de cada propuesta. Se mantiene la distinción entre ilustración conceptual y cálculo preciso.
- Encabezados e ilustraciones incrustados en los archivos, con formato de URI de datos compatible con los ejemplos de Colab; no dependen de una carpeta vecina.
- Corregidos el formato de las instrucciones iniciales y las referencias de sección de cobertura.
- README, guía docente, documentación y paquete actualizados.
- Plantillas y soluciones ejecutadas en kernels nuevos en memoria: las 20 actividades y las comprobaciones numéricas pasan. Los notebooks del alumno conservan sus respuestas pendientes.
- Repositorio público creado en [marcoteran/python-vigilancia-labs](https://github.com/marcoteran/python-vigilancia-labs), con el proyecto completo en la rama `main`.
- Enlaces de ejecución en Colab y descarga directa actualizados para usar los notebooks públicos de GitHub.

## Pendiente

**Colab:** prueba de ejecución y controles en el frontend de Google. La validación local y la exportación HTML no prueban una sesión remota de Colab ni una clase con alumnos.

**Resolución visual:** las dos ilustraciones generadas tienen 1672 × 941 px, aproximadamente 16:9. No son 4K. El fondo se percibe blanco y presenta variaciones mínimas de generación; no se certifica uniformidad pixel a pixel en #FFFFFF.

Las propuestas 01-B y 02-B quedan pendientes y están identificadas como tales.

## Mantenimiento

El proyecto conserva `prompts/claude_code_publicar.md`, los scripts, los requisitos y el workflow de GitHub. Las modificaciones futuras deben mantener los ejercicios sin resolver en el material del alumno y conservar la evidencia de validación. No se añade una licencia de reutilización sin decisión del autor.

## Revisión del 13 de octubre de 2026

Notebooks revisados para principiantes absolutos, laboratorio SDR integrado en `lab_SDR_surveillance_LaTeX/` con PDF compilado, README rediseñado y verificador corregido para Windows. Detalle, resultados de pruebas y limitaciones: [auditoría pedagógica](pedagogical_audit.md). Publicada en `main` (commit `0fe9657`).

## Revisión del 14 de octubre de 2026

Presentación `slides/python_lab_slides.pdf` publicada y enlazada desde el README; notebooks alineados con ella; salidas de los controles limpias; verificador con comprobación de enlaces. Detalle en la sección 6 de la [auditoría pedagógica](pedagogical_audit.md).
