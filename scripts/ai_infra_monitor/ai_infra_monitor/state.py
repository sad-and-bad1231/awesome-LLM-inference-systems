from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path


def default_state() -> dict:
    return {"version": 1, "sources": {}, "records": {}, "runs": []}


def load_state(path: Path) -> dict:
    if not path.exists():
        return default_state()
    data = json.loads(path.read_text(encoding="utf-8"))
    base = default_state()
    base.update(data)
    return base


def save_state(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
        os.replace(temporary_name, path)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)
