import json
from runtime.paths import DATA

def load_index():
    index = DATA / "releases.json"
    if not index.exists():
        raise RuntimeError("No releases available")
    return json.loads(index.read_text(encoding="utf-8"))
