from __future__ import annotations

import subprocess
from pathlib import Path


def _git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        capture_output=True,
        check=check,
    )


def is_repository(root: Path) -> bool:
    return _git(root, "rev-parse", "--is-inside-work-tree", check=False).returncode == 0


def commit_research_updates(root: Path, message: str, paths: list[Path]) -> str:
    relative = [str(path.relative_to(root)) for path in paths if path.exists()]
    if not relative:
        return ""
    _git(root, "add", "--", *relative)
    staged = _git(root, "diff", "--cached", "--quiet", check=False)
    if staged.returncode == 0:
        return ""
    result = _git(root, "commit", "-m", message)
    return result.stdout.strip()
