"""
Version selection logic.

Selects exactly one version based on:
- Machine identifier
- Manifest rules
"""

import json
from pathlib import Path
from utils.logging import get_logger

logger = get_logger(__name__)

MANIFEST_PATH = Path("manifest/example_manifest.json")


def select_version(machine_id: str) -> str:
    """
    Determine which version should run on this machine.

    Args:
        machine_id (str): unique machine identifier

    Returns:
        str: selected version
    """
    if not MANIFEST_PATH.exists():
        raise RuntimeError("Manifest file not found")

    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        manifest = json.load(f)

    machine_map = manifest.get("machines", {})
    default_version = manifest.get("default_version")

    if machine_id in machine_map:
        logger.info("Machine-specific rule applied")
        return machine_map[machine_id]

    if default_version:
        logger.info("Default rule applied")
        return default_version

    raise RuntimeError("No version rule applicable")
