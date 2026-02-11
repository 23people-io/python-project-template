# Python Project Template

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=23people-io_python-project-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=23people-io_python-project-template)

Esta plantilla es un ejemplo de la estructura básica de un proyecto en Python.

Forma parte de la presentación de ["Introducción a Python"]([LICENSE](https://www.canva.com/design/DAHA1PesQ2o/EUIVCJNTx7DmD0sqrdzqVA/view?utm_content=DAHA1PesQ2o&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h1e9507b8c7)) realizada en 23people para desarrolladores con experiencia en otros lenguajes.

El repositorio incluye un ejemplo con fastapi en la carpeta src y una carpeta con ejemplos de código en python de la presentación.

El proyecto incluye:

- Un administrador de paquetes: [uv](https://docs.astral.sh/uv/)
- Linter y Formatter: [ruff](https://docs.astral.sh/ruff/)
- Chequeador de Tipos: [ty](https://docs.astral.sh/ty/)
- Verifica que los mensajes de commit cumplan con ["Conventional Commits"](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13).
- Se integra con Sonar a través del archivo [.sonarcloud.properties](.sonarcloud.properties).
- Github workflow para chequear el código
- Incluye plugins sugeridos para el trabajo con VsCode

## Comenzar

### Pre-requisitos

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

No es necesario que instales python previamente. UV instala la versión de python requerida por el proyecto.

### Instalación

1. Clonar repositorio:

   ```bash
    git clone git@github.com:23people-io/python-project-template.git
    cd python-project-template
   ```

2. Actualizar python, dependencias y configurar el virtual environment:

   ```bash
    uv sync
   ```

3. Instalar los hooks de pre-commit y chequear el código con ruff, ty, correr los tests, limitar el tamaño de archivos,  ["conventional commits"](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13):

   ```bash
    source .venv/bin/activate
    pre-commit install
   ```

Alternativamente puedes ejecutar todos los comandos del paso 2 y 3 ejecutando el script:

```bash
   ./run.sh setup
```

## Configuración

1. Crar un archivo `.env` file en la raíz del proyecto y agregar lo siguiente:

```bash
   PORT=8000
```

## Uso

Para correr la aplicación principal ejecuta el siguiente comando:

```bash
   uv run --env-file .env python src/run.py src/main.py
```

Alternativamente ejecuta:

```bash
   ./run.sh
```

## Testing

Para correr los tests ejecuta:

```bash
   uv run pytest --capture=no
```

Alternativamente:

```bash
   ./run.sh tests
```

## Linter y Tipos

Para chequear prácticas de código y type hints:

```bash
    uv run ruff check
    uv run ty check
```

O alternativamente:

```bash
   ./run.sh lint
```

## Chequear todo: linter, format, tipos y tests

Para chequear todo con un sólo comando:

```bash
   uv run pre-commit run --all-files
```

## Conventional Commits

Los mensajes de commit deben comenzar por los siguientes prefijos:

| Prefijo  | Descripcion                                      |
| -----    | -----------                                      |
| feat     | Nueva funcionalidad.                             |
| fix      | Un bug fix.                                      |
| docs     | Modificaciones sólo Documentación.               |
| style    | Cambios de formato, espacios, punto y comas.     |
| refactor | Refactorización.                                 |
| perf     | Cambio en el código para mejorar la performance. |
| test     | Agregar tests o corregir alguno existente.       |
| build    | Cambios que afectan sólo al build.               |
| chore    | Otros no clasificados.                           |


Ejemplos:

```bash
    git commit -m "feat: delete user by id"
    git commit -m "fix: prevent crash when input is empty"
    git commit -m "docs: update README with installation steps"
    git commit -m "style: fix indentation in user service"
    git commit -m "refactor: simplify validation logic"
    git commit -m "perf: optimize database query for users"
    git commit -m "test: add unit tests for login flow"
    git commit -m "build: update webpack configuration"
    git commit -m "chore: update dependencies"
```

Es posible utilzar scopes entre paréntesis para que el mensaje sea más claro y acotado.

Ejemplos:

```bash
    git commit -m "feat(api): enable password reset endpoint"
    git commit -m "fix(payment): correct currency conversion bug"
    git commit -m "docs(api): add usage examples"
    git commit -m "style(css): reorder class declarations"
    git commit -m "refactor(auth): extract token generation logic"
    git commit -m "perf(api): reduce response time for search endpoint"
    git commit -m "test(auth): improve coverage for token service"
    git commit -m "build(ci): configure GitHub Actions pipeline"

```

## Nuevo proyecto

Si deseas partir un nuevo proyecto en python:

```bash
uv init mi-proyecto
cd mi-proyecto
uv add --dev ruff ty pytest
```

Si deseas agregar chequeo de "Conventional Commits"

```bash
uv add pre-commit
source .venv/bin/activate
pre-commit install
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
