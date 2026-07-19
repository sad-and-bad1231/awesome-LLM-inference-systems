"""Shared, compact presentation helpers for research and engineering views."""

from __future__ import annotations

from collections import defaultdict
from html import unescape
import re
from typing import Any

from .curation import THEME_ORDER, curation_for, project_key_for_record


THEME_LABELS = {
    "attention-kernel": "Attention / Kernel",
    "kv-cache": "KV Cache",
    "prefill-decode-transfer": "Prefill–Decode 与传输",
    "speculative-decoding": "Speculative Decoding",
    "moe": "MoE",
    "compiler-dsl": "Compiler / DSL",
    "runtime-scheduling": "Runtime / Scheduling",
}


def _is_release(record: dict[str, Any]) -> bool:
    title = str(record.get("title", "")).lower().strip()
    url = str(record.get("primary_url", "")).lower()
    channel = str(record.get("venue_or_channel", "")).lower()
    return "/releases/" in url or " releases" in channel or bool(re.fullmatch(r"(?:release\s+)?v?\d[\w.\-]*", title))


def _plain_text(value: str) -> str:
    text = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", value, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[`*_#>]", " ", text)
    return re.sub(r"\s+", " ", unescape(text)).strip()


def _truncate(value: str, max_chars: int) -> str:
    if max_chars <= 0:
        return ""
    if len(value) <= max_chars:
        return value
    return value[: max(0, max_chars - 1)].rstrip() + "…"


def display_summary(record: dict[str, Any], max_chars: int = 240) -> str:
    """Return compact display text without mutating the source record."""
    presentation = record.get("presentation") if isinstance(record.get("presentation"), dict) else {}
    raw = str(presentation.get("blurb") or record.get("summary") or "No summary provided.")
    themes = curation_for(record).get("themes", [])
    if not presentation.get("blurb") and _is_release(record) and (len(raw) > 2000 or "<" in raw):
        labels = [THEME_LABELS[theme] for theme in themes if theme in THEME_LABELS]
        neutral = "官方发布记录"
        if labels:
            neutral += "，涉及：" + "、".join(labels)
        return _truncate(neutral + "。", max_chars)
    return _truncate(_plain_text(raw), max_chars)


def project_key_for(record: dict[str, Any]) -> str:
    return project_key_for_record(record)


def _date_key(record: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(record.get("evidence", {}).get("verified_at") or record.get("discovered") or ""),
        str(record.get("year", "")),
        str(record.get("title", "")),
    )


def _is_prerelease(record: dict[str, Any]) -> bool:
    value = " ".join([str(record.get("title", "")), str(record.get("primary_url", ""))]).lower()
    return bool(re.search(r"(?:rc|alpha|beta|preview)\d*(?:$|[./\-\s])", value))


def _anchor_sort_key(record: dict[str, Any]) -> tuple[int, int, str, str]:
    presentation = record.get("presentation") if isinstance(record.get("presentation"), dict) else {}
    priority = {"foundation": 0, "frontier": 1, "supporting": 2}.get(
        curation_for(record).get("priority"), 3
    )
    return (
        0 if presentation.get("featured") is True else 1,
        priority,
        str(record.get("year", "")),
        str(record.get("title", "")),
    )


def aggregate_industry_records(
    records: list[dict[str, Any]], *, milestone_limit: int = 3
) -> list[dict[str, Any]]:
    """Collapse release-heavy industry facts into deterministic project entries."""
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[project_key_for(record)].append(record)

    projects = []
    for key, rows in grouped.items():
        non_releases = [record for record in rows if not _is_release(record)]
        if non_releases:
            anchor = sorted(non_releases, key=_anchor_sort_key)[0]
        else:
            stable = [record for record in rows if not _is_prerelease(record)]
            anchor = max(stable or rows, key=_date_key)

        candidates = [
            record for record in rows
            if record is not anchor
            and curation_for(record).get("scope") == "core"
            and curation_for(record).get("priority") in {"foundation", "frontier"}
            and curation_for(record).get("themes")
        ]
        candidates.sort(key=lambda record: str(record.get("title", "")))
        candidates.sort(key=_date_key, reverse=True)
        candidates.sort(
            key=lambda record: {"foundation": 0, "frontier": 1}.get(
                curation_for(record).get("priority"), 2
            )
        )
        milestones = []
        seen_themes = set()
        for record in candidates:
            primary_theme = curation_for(record).get("themes", [""])[0]
            if primary_theme in seen_themes:
                continue
            seen_themes.add(primary_theme)
            milestones.append(record)
            if len(milestones) >= max(milestone_limit, 0):
                break

        themes = [
            theme for theme in THEME_ORDER
            if any(theme in curation_for(record).get("themes", []) for record in rows)
        ]
        scopes = {curation_for(record).get("scope", "archive") for record in rows}
        group_scope = "core" if "core" in scopes else "adjacent" if "adjacent" in scopes else "archive"
        projects.append({
            "project_key": key,
            "anchor": anchor,
            "milestones": milestones,
            "themes": themes,
            "scope": group_scope,
        })
    projects.sort(key=lambda project: _anchor_sort_key(project["anchor"]))
    return projects
