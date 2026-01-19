"""
Release installation logic.

Assumptions:
- Release ZIPs are provided externally
- Installation is explicit and controlled
- Installed versions are immutable
"""

import zipfile
from pathlib import Path
from utils.logging import get_logger
from release_store.paths import get_version_path, ensure_directories

logger = get_logger(__name__)

# Directory where release ZIPs are placed manually
RELEASES_DIR = Path("releases")


def install_version(version: str) -> None:
    """
    Install a version from a ZIP archive.

    Args:
        version (str): version identifier
    """
    ensure_directories()

    zip_path = RELEASES_DIR / f"app_{version}.zip"
    if not zip_path.exists():
        raise RuntimeError(f"Release package not found: {zip_path}")

    target_dir = get_version_path(version)
    if target_dir.exists():
        raise RuntimeError(f"Version already installed: {version}")

    logger.info(f"Installing version {version}")

    target_dir.mkdir(parents=True)

    with zipfile.ZipFile(zip_path, "r") as archive:
        archive.extractall(target_dir)

    logger.info(f"Version {version} installed successfully")
