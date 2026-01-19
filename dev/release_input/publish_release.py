import json
import hashlib
import zipfile
import shutil
from pathlib import Path
import re

INPUT = Path("dev/release_input")
BUNDLE = Path("release_bundle")
PACKAGES = BUNDLE / "packages"
INDEX = BUNDLE / "releases.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def load_release():
    cfg = json.loads((INPUT / "release.json").read_text(encoding="utf-8"))
    if not re.fullmatch(r"\d+\.\d+\.\d+", cfg["version"]):
        raise RuntimeError("Version must be X.Y.Z")
    return cfg


def publish():
    PACKAGES.mkdir(parents=True, exist_ok=True)

    exe = INPUT / "app.exe"
    if not exe.exists():
        raise RuntimeError("app.exe missing")

    release = load_release()
    version = release["version"]

    zip_path = PACKAGES / f"app_{version}.zip"
    if zip_path.exists():
        raise RuntimeError(f"Version {version} already exists")

    checksum = sha256(exe)

    tmp = INPUT / "_tmp"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()

    shutil.copy(exe, tmp / "app.exe")
    (tmp / "checksum.sha256").write_text(checksum, encoding="utf-8")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(tmp / "app.exe", "app.exe")
        z.write(tmp / "checksum.sha256", "checksum.sha256")

    shutil.rmtree(tmp)

    index = {"releases": []}
    if INDEX.exists():
        index = json.loads(INDEX.read_text(encoding="utf-8"))

    index["releases"] = [
        r for r in index["releases"] if r["version"] != version
    ]
    index["releases"].insert(0, release)

    INDEX.write_text(json.dumps(index, indent=2), encoding="utf-8")

    print(f"Published version {version}")
    print(f"Bundle ready in: {BUNDLE.resolve()}")


if __name__ == "__main__":
    publish()
