# Mejorar los laboratorios

Describe el problema con una referencia de sección, un ejemplo reproducible y el resultado esperado. Para correcciones físicas aporta una fuente primaria. Para cambios de enseñanza explica qué dificultad del principiante resuelve la propuesta.

Mantén los dos notebooks independientes de servicios externos: sin secretos, sensores, rutas absolutas de tu máquina ni datasets privados. Conserva los `None` del alumno y actualiza las soluciones por separado. Cada fórmula debe declarar unidades e hipótesis; cada gráfico debe nombrar sus ejes.

Ejecuta `python scripts/verificar.py` después de una modificación de código o respuestas. Revisa visualmente los gráficos y los encabezados. Si cambias widgets, prueba también la alternativa por llamada de función. No marques una prueba de Colab como aprobada si solo hiciste ejecución local.

Los archivos de clase originales no forman parte de este repositorio. No agregues datos de aeronaves, credenciales ni información de personas a los ejercicios sintéticos.
