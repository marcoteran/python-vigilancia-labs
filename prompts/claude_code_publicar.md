# Publicar el proyecto completo con Claude Code

El usuario ha autorizado publicar **un repositorio nuevo y público** en su cuenta. No es una autorización para sobrescribir otro proyecto. Este prompt permite reproducir la publicación desde una máquina con GitHub CLI disponible.

La entrega del 9 de octubre de 2026 ya está publicada en `marcoteran/python-vigilancia-labs`, rama `main`. El siguiente prompt conserva el procedimiento de publicación inicial; para actualizar esta entrega, clona el repositorio existente y realiza un push normal con las modificaciones verificadas.

```text
Trabaja dentro de la carpeta python-vigilancia-labs (o aviation-python-labs si conserva el nombre del paquete). El contenido ya es el entregable final: dos notebooks para alumnos, guía y soluciones del instructor, gráficos exactos, prompts de ilustraciones y README. Publica el proyecto como repositorio nuevo PÚBLICO `python-vigilancia-labs` en la cuenta autenticada del autor.

1. Lee README.md, instructor/guia_instructor.md y docs/verificacion.json. Identifica la cuenta con `gh api user --jq .login`; debe ser la cuenta del usuario. No imprimas tokens ni inspecciones almacenes de credenciales.
2. Verifica que `<cuenta>/python-vigilancia-labs` no existe. Si existe y no pertenece a esta publicación, no sobreescribas ni fuerces pushes: informa el conflicto. Si está vacío y el usuario lo acaba de crear para este proyecto, úsalo.
3. Ejecuta `python -m pip install -r requirements-dev.txt` y `python scripts/verificar.py`. Revisa el informe, los encabezados y las imágenes. Nunca completes los None en los notebooks del alumno. Si el entorno impide sockets, usa `--in-process` y conserva esa limitación en el informe. No declares Colab probado por una prueba local.
4. Ajusta todos los enlaces README a la cuenta real y rama main. Comprueba que cada notebook indicado existe. No inventes estrellas, forks, testimonios, resultados pedagógicos ni pruebas de frontend.
5. Inicializa git si hace falta. Crea main, agrega solo los archivos del proyecto y realiza un commit descriptivo. No incluyas los archivos originales de clase, zip, rutas locales, tokens, resultados resueltos dentro de notebooks ni metadatos privados de Drive.
6. Crea y publica mediante `gh repo create <cuenta>/python-vigilancia-labs --public --source=. --remote=origin --push --description "Dos laboratorios en español: Python desde cero y cálculos de vigilancia aeronáutica, con antenas y radar interactivos."`. Si origin ya apunta a este repo, usa push normal sin --force. No cambies otros remotos.
7. Verifica con `gh api repos/<cuenta>/python-vigilancia-labs` que private=false y default_branch=main. Lee README y los dos archivos ipynb desde el remoto y compara sus SHA-256 con los archivos locales. Comprueba que las URLs públicas raw devuelven 200. Abre los dos enlaces Colab si tienes acceso de navegador autorizado; si no, declara que solo la estructura del enlace está verificada.
8. Entrega URL del repositorio, dos enlaces para Colab, dos descargas directas y resumen de pruebas. Conserva los prompts y el estado real de cada ilustración: 01-A y 02-A están generadas e integradas; 01-B y 02-B son propuestas pendientes. No añadas licencia de reutilización sin decisión del autor.
```
