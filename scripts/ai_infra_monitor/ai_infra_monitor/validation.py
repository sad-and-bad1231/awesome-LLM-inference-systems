from __future__ import annotations

import re
import struct
from dataclasses import dataclass
from pathlib import Path

from .identity import normalize_title
from .publication import GENERATED_NOTICE
from .records import validate_record_stores


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


def _public_view_errors(
    public_root: Path,
    paper_db_path: Path | None,
    industry_db_path: Path | None,
) -> list[ValidationError]:
    errors: list[ValidationError] = []
    required_views = (
        public_root / "README.md",
        public_root / "papers" / "README.md",
        public_root / "industry" / "README.md",
        public_root / "archive" / "README.md",
    )
    for path in required_views:
        errors.extend(_common_errors(path))
        if path.exists() and GENERATED_NOTICE not in path.read_text(encoding="utf-8"):
            errors.append(ValidationError(path, 1, "missing generated-view notice"))

    required_assets = (
        public_root / "figs" / "ai-inference-systems-cover.png",
        public_root / "figs" / "ai-inference-system-map.png",
    )
    for path in required_assets:
        if not path.exists():
            errors.append(ValidationError(path, 0, "required public image does not exist"))
            continue
        header = path.read_bytes()
        if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(ValidationError(path, 0, "public image is not a valid PNG"))
            continue
        width, height = struct.unpack(">II", header[16:24])
        if width < 640 or height < 200:
            errors.append(ValidationError(path, 0, "public image dimensions are too small"))

    markdown_link_pattern = re.compile(r"!?(?:\[([^\]]*)\])\(([^)]+)\)")
    for path in required_views:
        if not path.exists():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for alt_text, raw_target in markdown_link_pattern.findall(line):
                if raw_target.startswith(("figs/", "../figs/")) and not alt_text.strip():
                    errors.append(ValidationError(path, number, "local public image is missing alt text"))
                target = raw_target
                target = target.split("#", 1)[0].strip()
                if not target or re.match(r"(?:https?|mailto):", target):
                    continue
                target_path = (path.parent / target).resolve()
                if not target_path.exists():
                    errors.append(ValidationError(path, number, f"broken local link: {target}"))

    root = public_root / "README.md"
    if root.exists():
        text = root.read_text(encoding="utf-8")
        for section in ("## Overview", "## Start Here", "## Contents", "## Coverage", "## Reading Paths", "## Taxonomy", "## System Map", "## Evaluation Lens", "## Evidence Policy"):
            if section not in text:
                errors.append(ValidationError(root, 1, f"missing public README section: {section}"))
        if paper_db_path and industry_db_path:
            from .publication import _public_records

            papers = _public_records(paper_db_path, {"paper"})
            industry = _public_records(industry_db_path, {"industry", "project"})
            expected = {
                "Academic papers": len(papers),
                "Industry / open-source systems": len(industry),
            }
            for label, count in expected.items():
                if not re.search(rf"\| {re.escape(label)} \| {count} \|", text):
                    errors.append(ValidationError(root, 1, f"public coverage count mismatch: {label}"))
    for path in (public_root / "papers" / "README.md", public_root / "industry" / "README.md"):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for section in ("## At a Glance", "## Collection Navigation", "## Evidence and Selection", "## Resource List"):
            if section not in text:
                errors.append(ValidationError(path, 1, f"missing public collection section: {section}"))
    archive_path = public_root / "archive" / "README.md"
    if archive_path.exists():
        archive_text = archive_path.read_text(encoding="utf-8")
        for section in ("## Reading Rule", "## Academic Papers", "## Industry and Projects"):
            if section not in archive_text:
                errors.append(ValidationError(archive_path, 1, f"missing archive section: {section}"))
    return errors


def validate_workspace(
    paper_path: Path,
    industry_path: Path,
    candidate_path: Path,
    paper_db_path: Path | None = None,
    industry_db_path: Path | None = None,
    candidate_db_path: Path | None = None,
    public_root: Path | None = None,
) -> list[ValidationError]:
    errors = []
    if paper_db_path and industry_db_path and candidate_db_path:
        errors.extend(
            ValidationError(error.path, error.line, error.message)
            for error in validate_record_stores(paper_db_path, industry_db_path, candidate_db_path)
        )
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
    if public_root is not None:
        errors.extend(_public_view_errors(public_root, paper_db_path, industry_db_path))
    return errors
