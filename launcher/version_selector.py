"""
Version selection logic based on manifest and machine ID.
"""

import json
from pathlib import Path
from utils.logging import get_logger

logger = get_logger(__name__)

MANIFEST_PATH = Path("manifest/example_manifest.json")


def select_version(machine_id: str) -> str:
    if not MANIFEST_PATH.exists():
        raise RuntimeError("Manifest file not found")

    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        manifest = json.load(f)

    machines = manifest.get("machines", {})
    default_version = manifest.get("default_version")

    if machine_id in machines:
        logger.info("Machine-specific version rule applied")
        return machines[machine_id]

    if default_version:
        logger.info("Default version rule applied")
        return default_version

    raise RuntimeError(f"No version rule found for machine {machine_id}")
