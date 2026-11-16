# Brick Creation Creator

An AI-ready Python foundation for building the Brick Creation Creator.

## Quick start

```powershell
poetry install --with dev
poetry run pre-commit install
./scripts/verify.ps1
```

Use the repository guidance in [AGENTS.md](AGENTS.md) for human and AI-assisted changes. The
project’s quality checks are intentionally runnable locally and in CI.

## Layout

- `src/brick_creation_creator/` — application package
- `tests/` — behavioural and regression tests
- `docs/decisions/` — concise architectural decision records
- `.codex/skills/` — repository-local reusable AI workflow
