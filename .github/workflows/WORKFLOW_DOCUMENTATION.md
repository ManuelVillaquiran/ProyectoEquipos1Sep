# Documentación del Workflow de GitHub Actions

## ¿Qué es un Workflow?
Un workflow es un proceso automatizado configurable que ejecuta uno o más trabajos (jobs). Se define mediante un archivo YAML en la carpeta `.github/workflows` y se activa mediante eventos como `push` o `pull_request`.

## Explicación del archivo YAML (`ci-pipeline.yml`)

- **`on: [push, pull_request]`**: Define los disparadores. El flujo se ejecuta automáticamente al subir cambios o abrir un pull request hacia la rama `main` o `master`.
- **`runs-on: ubuntu-latest`**: Asigna un servidor virtual con sistema operativo Ubuntu para ejecutar las tareas.
- **`actions/checkout@v4`**: Copia el código fuente del repositorio al runner.
- **`actions/setup-python@v5`**: Configura la versión especificada de Python (3.14).
- **`pip install -r ...`**: Instala todas las dependencias listadas en el proyecto.
- **`python manage.py migrate`**: Aplica las migraciones requeridas para la base de datos en el entorno de pruebas.
- **`python manage.py test`**: Ejecuta la suite de pruebas unitarias de Django.

## Retos Enfrentados y Soluciones
- **Estructura de carpetas**: El archivo `manage.py` y `requirements.txt` se encuentran dentro de la subcarpeta `proyectoEquipos`, por lo que se ajustaron las rutas en las instrucciones `cd` y `pip install`.