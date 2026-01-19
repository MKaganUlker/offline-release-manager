import subprocess
import shutil
from runtime.logger import get_logger
from runtime.bootstrap import bootstrap
from runtime.release_index import load_index
from runtime.installer import install
from runtime.paths import CACHE

log = get_logger("launcher")


def pick_release(releases):
    """
    Pick exactly one release to run.

    Rules:
    1) If exactly one release is marked as recommended → use it
    2) Otherwise → use highest semantic version
    """

    recommended = [r for r in releases if r.get("recommended") is True]
    if len(recommended) == 1:
        return recommended[0]

    def version_key(r):
        return tuple(map(int, r["version"].split(".")))

    return sorted(releases, key=version_key, reverse=True)[0]


def clean_cache_except(version: str):
    """
    Remove cached versions other than the selected one.
    Prevents stale execution.
    """
    if not CACHE.exists():
        return

    for d in CACHE.iterdir():
        if d.is_dir() and d.name != version:
            shutil.rmtree(d)


def launch():
    log.info("Launcher started")

    # Import release bundle into user space
    bootstrap()

    index = load_index()
    release = pick_release(index["releases"])
    version = release["version"]

    log.info(f"Selected version: {version}")

    # Prevent stale cache reuse
    clean_cache_except(version)

    app_dir = install(version)

    log.info(f"Executing app.exe from {app_dir}")
    subprocess.Popen(str(app_dir / "app.exe"), shell=True)


if __name__ == "__main__":
    launch()
