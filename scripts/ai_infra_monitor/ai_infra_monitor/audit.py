"""Compact aggregate diagnostics for the research fact stores."""

from __future__ import annotations

from collections import Counter
from datetime import date
from typing import Any

from .curation import THEME_ORDER, curation_for, is_public_mainline, select_exploration
from .identity import normalize_title
from .reading import (
    INDUSTRY_TOPICS,
    aggregate_industry_records,
    public_source_records,
    select_industry_topic,
    select_public_mainline,
)


def _record_date(record: dict[str, Any]) -> str:
    for value in (
        record.get("evidence", {}).get("verified_at"),
        record.get("discovered"),
        f"{record.get('year')}-12-31" if str(record.get("year", "")).isdigit() else "",
    ):
        if value:
            try:
                return date.fromisoformat(str(value)[:10]).isoformat()
            except ValueError:
                continue
    return ""


def _duplicate_count(values: list[str]) -> int:
    counts = Counter(value for value in values if value)
    return sum(count - 1 for count in counts.values() if count > 1)


def _store_audit(records: list[dict[str, Any]]) -> dict[str, Any]:
    scopes = Counter(curation_for(record).get("scope", "unknown") for record in records)
    core = [record for record in records if curation_for(record).get("scope") == "core"]
    themes = Counter(
        theme
        for record in core
        for theme in curation_for(record).get("themes", [])
        if theme in THEME_ORDER
    )
    return {
        "records": len(records),
        "scopes": dict(sorted(scopes.items())),
        "latest_date": max((_record_date(record) for record in records), default=""),
        "duplicate_canonical_ids": _duplicate_count(
            [str(record.get("canonical_id", "")) for record in records]
        ),
        "duplicate_titles": _duplicate_count(
            [normalize_title(str(record.get("title", ""))) for record in records]
        ),
        "long_summaries": sum(len(str(record.get("summary", ""))) > 5000 for record in records),
        "core_affiliation_status": dict(
            sorted(
                Counter(
                    str(record.get("evidence", {}).get("affiliation_status") or "missing")
                    for record in core
                ).items()
            )
        ),
        "core_artifact_status": dict(
            sorted(
                Counter(
                    str(record.get("evidence", {}).get("artifact_status") or "missing")
                    for record in core
                ).items()
            )
        ),
        "themes": {theme: themes.get(theme, 0) for theme in THEME_ORDER},
    }


def build_audit(
    papers: list[dict[str, Any]],
    industry: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    *,
    paper_limit_per_theme: int = 8,
    industry_limit_per_theme: int = 5,
    exploration_limit_per_track: int = 15,
    company_topic_limit: int = 8,
) -> dict[str, Any]:
    paper_source = public_source_records(papers, {"paper"})
    industry_source = public_source_records(industry, {"industry", "project"})
    paper_mainline = [record for record in paper_source if is_public_mainline(record)]
    project_groups = aggregate_industry_records(industry_source)
    project_mainline = []
    for group in project_groups:
        if group["scope"] != "core":
            continue
        display = dict(group["anchor"])
        display["_reading_themes"] = list(group["themes"])
        project_mainline.append(display)
    topic_counts = {
        str(topic["key"]): len(
            select_industry_topic(
                industry_source, str(topic["key"]), limit=company_topic_limit
            )
        )
        for topic in INDUSTRY_TOPICS
    }
    industry_exploration_source = select_exploration(
        industry_source,
        limit=max(exploration_limit_per_track * 5, exploration_limit_per_track),
    )
    industry_exploration_projects = aggregate_industry_records(industry_exploration_source)
    return {
        "stores": {
            "papers": _store_audit(papers),
            "industry": _store_audit(industry),
            "candidates": _store_audit(candidates),
        },
        "public_projection": {
            # papers 视图开启 foundation 兜底车道（与 reading.display_themes 一致），
            # 否则不命中关键词的奠基类论文会从投影计数里漏掉。
            "papers": len(
                select_public_mainline(
                    paper_mainline,
                    limit_per_theme=paper_limit_per_theme,
                    allow_foundation=True,
                )
            ),
            "industry_projects": len(
                select_public_mainline(
                    project_mainline, limit_per_theme=industry_limit_per_theme
                )
            ),
            "paper_exploration": len(
                select_exploration(
                    paper_source, limit=exploration_limit_per_track
                )
            ),
            "industry_exploration": min(
                len(industry_exploration_projects), max(exploration_limit_per_track, 0)
            ),
            "company_topics": topic_counts,
        },
    }
