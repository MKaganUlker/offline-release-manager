from pathlib import Path

# Launcher directory (portable)
LAUNCHER_ROOT = Path(__file__).resolve().parent.parent

# DEV-provided bundle (read-only)
BUNDLE_ROOT = LAUNCHER_ROOT / "release_bundle"
BUNDLE_INDEX = BUNDLE_ROOT / "releases.json"
BUNDLE_PACKAGES = BUNDLE_ROOT / "packages"

# Runtime-managed user space
BASE = Path.home() / ".offline_release"
CACHE = BASE / "cache"
LOGS = BASE / "logs"
DATA = BASE / "data"

for p in (CACHE, LOGS, DATA):
    p.mkdir(parents=True, exist_ok=True)
