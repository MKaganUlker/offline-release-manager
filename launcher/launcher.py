"""
Launcher entry point.

This is the ONLY file users execute.
"""

import sys
import subprocess
from launcher.machine_id import get_machine_id
from launcher.version_selector import select_version
from launcher.verifier import verify_version
from release_store.registry import is_version_installed
from release_store.install import install_version
from release_store.paths import get_version_path
from utils.logging import get_logger

logger = get_logger(__name__)


def launch():
    logger.info("Launcher started")

    machine_id = get_machine_id()
    logger.info(f"Machine ID: {machine_id}")

    version = select_version(machine_id)
    logger.info(f"Target version: {version}")

    if not is_version_installed(version):
        logger.warning("Version not installed locally")
        install_version(version)

    verify_version(version)

    exe_path = get_version_path(version) / "app.exe"
    logger.info(f"Launching {exe_path}")

    subprocess.Popen([str(exe_path)], shell=False)


if __name__ == "__main__":
    try:
        launch()
    except Exception:
        logger.exception("Launcher execution failed")
        sys.exit(1)
