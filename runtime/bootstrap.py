"""
Bootstrap logic.

Imports DEV-provided release bundle into
runtime-managed user space automatically.
"""

import shutil
from runtime.paths import (
    BUNDLE_ROOT, BUNDLE_INDEX, BUNDLE_PACKAGES,
    DATA
)

DATA_INDEX = DATA / "releases.json"
DATA_PACKAGES = DATA / "packages"


def bootstrap():
    if not BUNDLE_ROOT.exists():
        raise RuntimeError("Release bundle missing")

    DATA_PACKAGES.mkdir(parents=True, exist_ok=True)

    # Copy index if not present
    if not DATA_INDEX.exists():
        shutil.copy(BUNDLE_INDEX, DATA_INDEX)

    # Copy packages (read-only import)
    for pkg in BUNDLE_PACKAGES.glob("*.zip"):
        target = DATA_PACKAGES / pkg.name
        if not target.exists():
            shutil.copy(pkg, target)
