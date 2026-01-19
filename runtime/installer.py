import zipfile
from runtime.paths import CACHE, DATA
from runtime.verifier import sha256


def install(version: str):
    target = CACHE / version
    if target.exists():
        return target

    zip_path = DATA / "packages" / f"app_{version}.zip"
    if not zip_path.exists():
        raise RuntimeError("Package missing")

    target.mkdir()

    with zipfile.ZipFile(zip_path) as z:
        z.extractall(target)

    exe = target / "app.exe"
    expected = (target / "checksum.sha256").read_text().strip()

    if sha256(exe) != expected:
        raise RuntimeError("Integrity verification failed")

    return target
