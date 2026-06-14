from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .identity import normalize_title


@dataclass(frozen=True)
class ValidationError:
    path: Path
    line: int
    message: str


def _common_errors(path: Path) -> list[ValidationError]:
    if not path.exists():
        return [ValidationError(path, 0, "file does not exist")]
    errors = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r"\[[^\]]+\]\(\s*\)", line):
            errors.append(ValidationError(path, number, "empty markdown link"))
        if line.rstrip() != line:
            errors.append(ValidationError(path, number, "trailing whitespace"))
        if line.startswith(("<<<<<<<", "=======", ">>>>>>>")):
            errors.append(ValidationError(path, number, "merge conflict marker"))
    return errors


def _table_rows(path: Path, expected_cells: int) -> list[tuple[int, list[str]]]:
    rows = []
    if not path.exists():
        return rows
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if len(cells) == expected_cells:
            rows.append((number, cells))
    return rows


def _duplicates(
    path: Path, rows: list[tuple[int, list[str]]], column: int, header: str, label: str
) -> list[ValidationError]:
    seen: dict[str, int] = {}
    errors = []
    for number, cells in rows:
        title = cells[column]
        if title == header:
            continue
        normalized = normalize_title(re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title))
        if not normalized:
            continue
        if normalized in seen:
            errors.append(
                ValidationError(
                    path,
                    number,
                    f"duplicate {label}: first seen on line {seen[normalized]}",
                )
            )
        else:
            seen[normalized] = number
    return errors


def validate_workspace(
    paper_path: Path, industry_path: Path, candidate_path: Path
) -> list[ValidationError]:
    errors = []
    for path in (paper_path, industry_path, candidate_path):
        errors.extend(_common_errors(path))

    paper_rows = _table_rows(paper_path, 4)
    industry_rows = _table_rows(industry_path, 6)
    candidate_rows = _table_rows(candidate_path, 8)
    errors.extend(_duplicates(paper_path, paper_rows, 0, "题目", "paper title"))
    errors.extend(
        _duplicates(industry_path, industry_rows, 1, "方案/论文", "industry solution")
    )
    errors.extend(_duplicates(candidate_path, candidate_rows, 4, "Title", "candidate"))
    return errors
