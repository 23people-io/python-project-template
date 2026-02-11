#!/usr/bin/env bash

set -e

if [[ -z "$1" ]]; then
  uv run --env-file .env python src/run.py src/main.py
elif [[ "$1" = "lint" ]]; then
  uv run ruff check
  uv run ty check
elif [[ "$1" = "tests" ]]; then
  uv run pytest --capture=no
elif [[ "$1" = "setup" ]]; then
  uv sync
  source .venv/bin/activate
  pre-commit install
else
  echo "Unknown command: $1"
  echo ""
  echo "Usage:"
  echo "  ./run.sh         # Run application"
  echo "  ./run.sh lint    # Run linters"
  echo "  ./run.sh tests   # Run tests"
  echo "  ./run.sh setup   # Run setup"
  exit 1
fi
