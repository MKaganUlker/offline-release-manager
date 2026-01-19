"""
Integrity verification logic.

Ensures installed artifacts are not corrupted.
"""

import hashlib
from pathlib import Path
from utils.logging import get_logger
from release_store.paths import get_version_path

logger = get_logger(__name__)


def calculate_sha256(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()


def verify_version(version: str) -> None:
    """
    Verify integrity of a given version.

    Raises RuntimeError if verification fails.
    """
    version_dir = get_version_path(version)

    checksum_file = version_dir / "checksum.sha256"
    exe_file = version_dir / "app.exe"

    if not checksum_file.exists():
        raise RuntimeError("Checksum file missing")

    if not exe_file.exists():
        raise RuntimeError("Executable missing")

    expected = checksum_file.read_text().strip()
    actual = calculate_sha256(exe_file)

    if expected != actual:
        raise RuntimeError("Checksum mismatch")

    logger.info("Integrity verification passed")
