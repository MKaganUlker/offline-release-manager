"""
Local version registry.

Responsible only for presence checks.
No mutation logic here.
"""

from release_store.paths import get_version_path


def is_version_installed(version: str) -> bool:
    """
    Check whether a specific version exists locally.

    Args:
        version (str): version identifier

    Returns:
        bool: True if installed
    """
    return get_version_path(version).exists()
