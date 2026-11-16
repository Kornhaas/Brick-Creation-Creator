# AI Development Guide

## Project contract

Brick Creation Creator is a Python 3.13 project managed with Poetry. Keep production code in
`src/brick_creation_creator/` and tests in `tests/`. Prefer small, typed, independently testable
modules. Do not invent product behaviour when a requirement is ambiguous; document the decision or
ask the user.

## Working agreement

1. Read the relevant code, tests, and this file before editing.
2. State the intended outcome and the assumptions that materially affect behaviour.
3. Make the smallest cohesive change. Preserve unrelated user changes.
4. Add or update tests for behaviour changes and run `./scripts/verify.ps1` before handoff.
5. Report changed files, verification performed, and any remaining risk.

## Roles

Use these roles as perspectives, not bureaucracy. One agent may cover several roles on small work.

| Role | Owns | Must check |
| --- | --- | --- |
| Product steward | intent, acceptance criteria, user-facing copy | scope and ambiguous decisions |
| Python implementer | design and code changes | typing, errors, compatibility |
| Test engineer | executable acceptance evidence | normal, boundary, and failure paths |
| Reviewer | maintainability and regressions | API contracts, simplicity, documentation |
| Security/privacy reviewer | trust boundaries and sensitive data | validation, secrets, permissions, dependencies |
| Release steward | integration and delivery readiness | verification, versioning, migration notes |

For changes that cross a trust boundary, handle credentials, add dependencies, change persistence,
or expose a network/API surface, explicitly apply the security/privacy reviewer perspective. Do not
perform external releases, publish packages, or change credentials without explicit user approval.

## Definition of done

- Requested behaviour and acceptance criteria are satisfied.
- New or changed logic has focused tests.
- `ruff format --check .`, `ruff check .`, `mypy src`, and `pytest` pass (or a failure is explained).
- Documentation and public types are updated when the contract changes.
- No secrets, personal data, generated build artifacts, or unrelated edits are committed.

## Decision records

Add a short record under `docs/decisions/` for a durable architectural choice, a new external
dependency, or a security-relevant tradeoff. Use `docs/decisions/0000-template.md` as the format.
