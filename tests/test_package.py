"""Smoke tests for the package boundary."""

import brick_creation_creator


def test_package_imports() -> None:
    """The public package remains importable."""
    assert brick_creation_creator.__doc__ is not None
