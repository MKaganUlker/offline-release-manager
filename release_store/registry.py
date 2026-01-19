"""
Local version registry logic.
"""

from release_store.paths import get_version_path


def is_version_installed(version: str) -> bool:
    return get_version_path(version).exists()
