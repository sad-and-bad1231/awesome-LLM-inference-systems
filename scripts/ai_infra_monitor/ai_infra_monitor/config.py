"""Tiny config loader extracted from the deleted discovery module.

Only contains the YAML→dict load_config helper that monitor.py and several
other top-level imports depend on. Kept separate so monitor.py can import
it without dragging in the heavy discovery/fetch/parsers/triage chain.
"""

from __future__ import annotations

import json
from pathlib import Path


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))