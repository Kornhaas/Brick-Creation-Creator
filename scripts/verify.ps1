[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"

poetry run ruff format --check .
poetry run ruff check .
poetry run mypy src
poetry run pytest
