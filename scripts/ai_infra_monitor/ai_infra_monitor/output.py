from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from .identity import canonical_url, normalize_title
from .models import Candidate


def _escape(value: str) -> str:
    return " ".join(value.replace("|", "/").split())


def append_candidates(path: Path, candidates: list[Candidate]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(
            "# AI Infra Candidate Pool\n\n"
            "| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |\n"
            "|---|---|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    text = path.read_text(encoding="utf-8")
    existing_urls = {
        canonical_url(url)
        for url in re.findall(r"\((https?://[^)]+)\)", text)
    }
    existing_titles = {
        normalize_title(cells[4])
        for line in text.splitlines()
        if line.startswith("|")
        for cells in [[cell.strip() for cell in line.strip().strip("|").split("|")]]
        if len(cells) == 8 and cells[4] != "Title"
    }
    rows = []
    for item in candidates:
        if (
            canonical_url(item.url) in existing_urls
            or normalize_title(item.title) in existing_titles
        ):
            continue
        status = "needs verification" if item.tier == "A" else "candidate"
        rows.append(
            "| {date} | {tier} | {kind} | {source} | {title} | {topics} | "
            "[primary]({url}) | {status} |".format(
                date=_escape(item.discovered),
                tier=_escape(item.tier),
                kind=_escape(item.kind),
                source=_escape(item.source_name or item.source_id),
                title=_escape(item.title),
                topics=_escape(", ".join(item.topics)),
                url=item.url.replace(")", "%29"),
                status=status,
            )
        )
        existing_urls.add(canonical_url(item.url))
        existing_titles.add(normalize_title(item.title))
    if rows:
        with path.open("a", encoding="utf-8", newline="\n") as stream:
            if text and not text.endswith("\n"):
                stream.write("\n")
            stream.write("\n".join(rows) + "\n")
    return len(rows)


def write_weekly_report(run_manifest: dict, path: Path) -> None:
    candidates = [
        Candidate.from_dict(item) for item in run_manifest.get("candidates", [])
    ]
    tiers = Counter(item.tier for item in candidates)
    topics = Counter(topic for item in candidates for topic in item.topics)
    lines = [
        f"# AI Infra Weekly Report: {run_manifest['run_id']}",
        "",
        f"- Candidates: {len(candidates)}",
        f"- Source errors: {len(run_manifest.get('errors', []))}",
        f"- Tiers: {', '.join(f'{key}={value}' for key, value in sorted(tiers.items())) or 'none'}",
        "",
        "## Topics",
        "",
    ]
    lines.extend(
        f"- {topic}: {count}" for topic, count in topics.most_common()
    )
    if not topics:
        lines.append("- No matching candidates.")
    lines.extend(["", "## Candidates", ""])
    lines.extend(
        f"- [{item.title}]({item.url}) ({item.tier}, {item.source_name})"
        for item in candidates
    )
    if not candidates:
        lines.append("- None.")
    if run_manifest.get("errors"):
        lines.extend(["", "## Source Errors", ""])
        lines.extend(
            f"- {error['source_name']}: {error['error']}"
            for error in run_manifest["errors"]
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
