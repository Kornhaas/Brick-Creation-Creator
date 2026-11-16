---
name: brick-creation-development
description: Implement, test, review, or plan changes in Brick Creation Creator using its Python quality gates and role-based workflow.
---

# Brick Creation Creator Development

Use this skill for repository work on Brick Creation Creator. Read `AGENTS.md` first; it is the
source of truth for scope, roles, and the definition of done.

Keep code under `src/brick_creation_creator` and tests under `tests`. For a behaviour change,
first identify acceptance criteria, then implement a small typed change and focused tests. Run
`./scripts/verify.ps1` before handoff.

Apply the security/privacy reviewer perspective for trust boundaries, secrets, dependencies,
persistence, and network/API work. Record durable architecture, dependency, or security choices
with `docs/decisions/0000-template.md`. Never publish, deploy, or alter external credentials
without explicit authorization.
