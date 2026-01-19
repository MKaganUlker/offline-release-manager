"""
Main entry point for Offline Release Manager launcher.

Responsibilities:
- Identify machine
- Load manifest
- Select target version
- Verify integrity
- Launch application
"""

from launcher.machine_id import get_machine_id
from launcher.version_selector import select_version
from launcher.verifier import verify_version
from release_store.registry import is_version_installed
from release_store.install import install_version
from release_store.paths import get_version_path
from utils.logging import get_logger
import subprocess
import sys

logger = get_logger(__name__)


def launch():
    logger.info("Launcher started")

    machine_id = get_machine_id()
    logger.info(f"Machine ID: {machine_id}")

    target_version = select_version(machine_id)
    logger.info(f"Selected version: {target_version}")

    if not is_version_installed(target_version):
        logger.warning(f"Version {target_version} not installed, installing")
        install_version(target_version)

    verify_version(target_version)

    exe_path = get_version_path(target_version) / "app.exe"
    if not exe_path.exists():
        raise RuntimeError(f"Executable not found: {exe_path}")

    logger.info(f"Launching application: {exe_path}")
    subprocess.Popen([str(exe_path)], shell=False)


if __name__ == "__main__":
    try:
        launch()
    except Exception as exc:
        logger.exception("Launcher failed")
        sys.exit(1)
