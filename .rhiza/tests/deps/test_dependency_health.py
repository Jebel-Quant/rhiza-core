"""Dependency health tests — validate pyproject.toml content."""

import tomllib


def test_pyproject_has_requires_python(root):
    """Verify that pyproject.toml declares requires-python in [project]."""
    pyproject_path = root / "pyproject.toml"
    assert pyproject_path.exists(), "pyproject.toml not found"

    with pyproject_path.open("rb") as f:
        pyproject = tomllib.load(f)

    assert "project" in pyproject, "[project] section missing from pyproject.toml"
    assert "requires-python" in pyproject["project"], "requires-python missing from [project] section"

    requires_python = pyproject["project"]["requires-python"]
    assert isinstance(requires_python, str), "requires-python must be a string"
    assert requires_python.strip(), "requires-python cannot be empty"
