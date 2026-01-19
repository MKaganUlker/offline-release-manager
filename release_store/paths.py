"""
Centralized path handling.
"""

from pathlib import Path

BASE_DIR = Path.home() / ".offline_release_manager"
VERSIONS_DIR = BASE_DIR / "versions"


def get_version_path(version: str) -> Path:
    return VERSIONS_DIR / version
