# Python Project Template

This is a template for a Python project. It includes a basic structure for organizing your code, tests, and documentation.

## Get Started

### Prerequisites

- Python 3.12 or higher
- uv

### Installation

1. Clone the repository:

   ```bash
    git clone git@github.com:23people-io/python-project-template.git
    cd python-project-template
   ```

2. Create an uv environment and activate it:

   ```bash
    uv venv
    source .venv/bin/activate
    uv sync
   ```

3. Install pre-commit hooks:

   ```bash
    pre-commit install
   ```

Alternatively, you can run all commands from step 2 to step 3 with a single command:

```bash
./setup.sh
```

1. Create a `.env` file in the root directory of the project:

```bash
PORT=8000
```

## Usage

To run the main application, use the following command:

```bash
uv run --env-file .env python run.py main.py
```

Or alternatively, you can run the application with a single command:

```bash
./run.sh
```

## Testing

To run the tests, use the following command:

```bash
uv run pytest --capture=no
```

Or alternatively, you can run the tests with a single command:

```bash
./test.sh
```

## Linting

To lint the code, use the following command:

```bash
uv run pre-commit run --all-files
```

Or alternatively, you can run the linter with a single command:

```bash
./lint.sh
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
