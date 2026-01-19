"""
Centralized filesystem paths.

All components rely on this module to avoid
hardcoded or duplicated paths.
"""

from pathlib import Path

BASE_DIR = Path.home() / ".offline_release_manager"
VERSIONS_DIR = BASE_DIR / "versions"


def ensure_directories() -> None:
    """
    Create required base directories if missing.
    """
    VERSIONS_DIR.mkdir(parents=True, exist_ok=True)


def get_version_path(version: str) -> Path:
    """
    Returns filesystem path for a specific version.

    Args:
        version (str): version identifier

    Returns:
        Path: version directory
    """
    return VERSIONS_DIR / version
