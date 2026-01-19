"""
Integrity verification logic for installed versions.
"""

import hashlib
from pathlib import Path
from release_store.paths import get_version_path
from utils.logging import get_logger

logger = get_logger(__name__)


def calculate_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def verify_version(version: str) -> None:
    version_path = get_version_path(version)

    checksum_file = version_path / "checksum.sha256"
    if not checksum_file.exists():
        raise RuntimeError("Checksum file missing")

    expected = checksum_file.read_text().strip()

    exe = version_path / "app.exe"
    actual = calculate_sha256(exe)

    if actual != expected:
        raise RuntimeError("Integrity check failed")

    logger.info("Integrity verified successfully")
