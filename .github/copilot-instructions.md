# Repository AI Instructions

Follow `AGENTS.md` as the authoritative development contract. Work in the smallest reviewable
increments, preserve user-owned changes, and avoid assuming product rules not evidenced by a
request or test.

Python lives in `src/brick_creation_creator`; tests live in `tests`. Use Python 3.13 features only
when they improve clarity, retain strict typing, and use `poetry run` for project tools. Before
proposing a completed change, run `./scripts/verify.ps1` and report its outcome.

Flag security, privacy, external-dependency, persistence, network/API, and release implications
explicitly. Never add secrets, publish a package, deploy, or mutate third-party systems without
the user's direct approval.
