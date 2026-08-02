"""Tests for Git LFS template structure and files.

This file and its associated tests flow down via a SYNC action from the jebel-quant/rhiza repository
(https://github.com/jebel-quant/rhiza).

Verifies that LFS-related files and configurations are present.
"""

import pytest


@pytest.fixture
def lfs_makefile(root):
    """Fixture that returns the path to lfs.mk if it exists, else skips."""
    path = root / ".rhiza" / "make.d" / "lfs.mk"
    if not path.exists():
        pytest.skip("lfs.mk not found, skipping LFS tests")
    return path


class TestLFSTemplateStructure:
    """Tests for LFS template file structure."""

    def test_lfs_makefile_exists(self, lfs_makefile):
        """LFS makefile should exist in make.d directory."""
        assert lfs_makefile.exists()

    def test_lfs_makefile_has_targets(self, lfs_makefile):
        """LFS makefile should define all expected targets."""
        content = lfs_makefile.read_text()

        required_targets = [
            "lfs-install:",
            "lfs-pull:",
            "lfs-track:",
            "lfs-status:",
        ]

        for target in required_targets:
            assert target in content, f"Target {target} not found in lfs.mk"

    def test_lfs_makefile_has_phony_declarations(self, lfs_makefile):
        """LFS makefile should declare targets as phony."""
        content = lfs_makefile.read_text()

        assert ".PHONY:" in content
        assert "lfs-install" in content
        assert "lfs-pull" in content
        assert "lfs-track" in content
        assert "lfs-status" in content

    def test_lfs_makefile_has_help_comments(self, lfs_makefile):
        """LFS makefile should have help comments for targets."""
        content = lfs_makefile.read_text()

        # Check for ##@ section header
        assert "##@ Git LFS" in content

        # Check for target descriptions
        assert "##" in content

    def test_lfs_makefile_cross_platform_support(self, lfs_makefile):
        """LFS makefile should support multiple platforms."""
        content = lfs_makefile.read_text()

        # Check for OS detection
        assert "uname -s" in content
        assert "Darwin" in content
        assert "Linux" in content

        # Check for architecture detection (macOS)
        assert "uname -m" in content
        assert "arm64" in content
        assert "amd64" in content

    def test_lfs_makefile_error_handling(self, lfs_makefile):
        """LFS makefile should include error handling."""
        content = lfs_makefile.read_text()

        # Check for error messages
        assert "ERROR" in content
        assert "exit 1" in content

    def test_lfs_makefile_uses_color_variables(self, lfs_makefile):
        """LFS makefile should use standard color variables."""
        content = lfs_makefile.read_text()

        # Check for color variable usage
        assert "BLUE" in content
        assert "RED" in content
        assert "RESET" in content
