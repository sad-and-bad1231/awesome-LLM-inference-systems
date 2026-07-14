from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
from typing import Any

from .records import ABSTRACTIONS, load_records


GENERATED_NOTICE = "<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->"
PUBLIC_CATEGORIES = {
    "Program-Aware Scheduling": "Runtime & Serving",
    "Disaggregated Interconnects": "P/D Disaggregation & KV Transfer",
    "Memory Topology & Virtualization": "KV State & Memory",
    "State Compression & Signal Coding": "KV Compression & Low-Bit State",
    "Execution Compilation & Kernel Fusion": "Kernel & Compiler",
    "SRE/Fault-Tolerance/Sparing": "Reliability & Benchmarks",
}
EXCLUDED_STATUSES = {"new", "keep", "drop", "promote", "queued"}
DIRECT_SERVING_TERMS = (
    "inference",
    "serving",
    "kv cache",
    "kv-cache",
    "prefill",
    "decode",
    "vllm",
    "sglang",
    "tensorrt-llm",
    "llm runtime",
    "llm engine",
    "speculative decoding",
    "attention kernel",
    "moe inference",
)


def _escape(value: object) -> str:
    return " ".join(str(value or "").replace("|", "/").split())


def _url(record: dict[str, Any]) -> str:
    return str(record.get("primary_url") or record.get("artifact_url") or "")


def _evidence_label(record: dict[str, Any]) -> str:
    label = {
        "formal_conference": "Formal Conference",
        "poster_or_workshop": "Poster / Workshop",
        "preprint": "Preprint",
        "industrial_material": "Industrial Material",
    }.get(record.get("evidence", {}).get("venue_status"), "Unclassified")
    if record.get("evidence", {}).get("verification_level") == "legacy_import":
        return f"{label} · Legacy Import"
    return label


def _tags(record: dict[str, Any]) -> str:
    tags = record.get("technical_tags", {})
    values = []
    for key in ("phase", "hardware", "optimization_layer", "workload", "framework_binding", "metrics"):
        for value in tags.get(key, [])[:2]:
            values.append(value)
    return " ".join(f"`{value}`" for value in values[:6])


def _sort_key(record: dict[str, Any]) -> tuple[int, int, int, str]:
    evidence_rank = {
        "formal_conference": 0,
        "industrial_material": 1,
        "poster_or_workshop": 2,
        "preprint": 3,
        "unclassified": 4,
    }
    try:
        year = -int(record.get("year") or 0)
    except (TypeError, ValueError):
        year = 0
    return (
        evidence_rank.get(record.get("evidence", {}).get("venue_status"), 4),
        0 if record.get("source_tier") == "A" else 1,
        year,
        str(record.get("title", "")),
    )


def _public_records(path: Path, types: set[str]) -> list[dict[str, Any]]:
    return sorted(
        [
            record
            for record in load_records(path)
            if record.get("record_type") in types
            and record.get("status") not in EXCLUDED_STATUSES
            and _is_serving_mainline(record)
        ],
        key=_sort_key,
    )


def _is_serving_mainline(record: dict[str, Any]) -> bool:
    text = " ".join(
        [
            str(record.get("title", "")),
            str(record.get("summary", "")),
            " ".join(str(value) for values in record.get("technical_tags", {}).values() for value in values),
        ]
    ).lower()
    if any(term in text for term in DIRECT_SERVING_TERMS):
        return True
    bindings = record.get("technical_tags", {}).get("framework_binding", [])
    return bool(bindings)


def _anchor(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def _entry(record: dict[str, Any], industry: bool = False) -> str:
    url = _url(record)
    title = f"[{_escape(record['title'])}]({url})" if url else _escape(record["title"])
    if industry:
        prefix = f"`{_escape(record.get('orgs') or 'Project')}` · `{_escape(record.get('year'))}` · `{_evidence_label(record)}`"
    else:
        prefix = f"`{_escape(record.get('venue_or_channel'))}` · `{_evidence_label(record)}`"
    return f"- **{title}**<br>\n  {prefix} · {_tags(record)}<br>\n  {_escape(record.get('summary'))}"


def _group(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped = {abstraction: [] for abstraction in ABSTRACTIONS}
    for record in records:
        grouped.setdefault(record.get("system_abstraction_primary", "Program-Aware Scheduling"), []).append(record)
    return grouped


def _render_collection(
    title: str,
    subtitle: str,
    records: list[dict[str, Any]],
    industry: bool,
) -> str:
    grouped = _group(records)
    lines = [f"# {title}", "", GENERATED_NOTICE, "", subtitle, "", "## Categories", ""]
    lines.extend(f"- [{PUBLIC_CATEGORIES[abstraction]}](#{_anchor(PUBLIC_CATEGORIES[abstraction])})" for abstraction in ABSTRACTIONS)
    lines.extend(["", "## Resource List", ""])
    for abstraction in ABSTRACTIONS:
        category = PUBLIC_CATEGORIES[abstraction]
        lines.extend([f"### {category}", ""])
        rows = grouped.get(abstraction, [])
        if not rows:
            lines.append("_No verified records yet._")
        else:
            lines.extend(_entry(record, industry=industry) for record in rows)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_root(papers: list[dict[str, Any]], industry: list[dict[str, Any]]) -> str:
    paper_counts = Counter(_evidence_label(record) for record in papers)
    industry_counts = Counter(_evidence_label(record) for record in industry)
    lines = [
        "# Awesome AI Inference Systems",
        "",
        GENERATED_NOTICE,
        "",
        "A curated, evidence-aware collection of LLM inference serving papers and industrial systems.",
        "",
        "This repository focuses on the serving mainline: runtime, P/D disaggregation, KV state, kernels, compilers, scheduling, reliability, and production infrastructure.",
        "",
        "## Contents",
        "",
        "- [Academic Papers](papers/README.md)",
        "- [Industry & Open-Source Systems](industry/README.md)",
        "- [Contribution Guide](CONTRIBUTING.md)",
        "",
        "## Coverage",
        "",
        "| Collection | Records | Evidence breakdown |",
        "|---|---:|---|",
        f"| Academic papers | {len(papers)} | {_escape(', '.join(f'{key}: {value}' for key, value in sorted(paper_counts.items())))} |",
        f"| Industry / open-source systems | {len(industry)} | {_escape(', '.join(f'{key}: {value}' for key, value in sorted(industry_counts.items())))} |",
        "",
        "## Taxonomy",
        "",
    ]
    lines.extend(f"- **{PUBLIC_CATEGORIES[abstraction]}**: system-level techniques and evidence for the serving stack." for abstraction in ABSTRACTIONS)
    lines.extend(["", "## Featured Papers", ""])
    for record in papers[:12]:
        lines.append(_entry(record))
    lines.extend(["", "## Featured Industry Systems", ""])
    for record in industry[:12]:
        lines.append(_entry(record, industry=True))
    lines.extend([
        "",
        "## Evidence Policy",
        "",
        "Venue status and source type are factual metadata. Technical tags summarize the system surface. Internal triage priority is not a publication-quality ranking and is not shown here.",
        "",
        "## Contributing",
        "",
        "Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.",
        "",
    ])
    return "\n".join(lines).rstrip() + "\n"


def render_public_repository(papers_path: Path, industry_path: Path, output_root: Path) -> None:
    papers = _public_records(papers_path, {"paper"})
    industry = _public_records(industry_path, {"industry", "project"})
    (output_root / "papers").mkdir(parents=True, exist_ok=True)
    (output_root / "industry").mkdir(parents=True, exist_ok=True)
    (output_root / "README.md").write_text(_render_root(papers, industry), encoding="utf-8", newline="\n")
    (output_root / "papers" / "README.md").write_text(
        _render_collection(
            "AI Inference Papers",
            "Full academic paper collection. Evidence labels distinguish formal conference publications, posters/workshops, and preprints.",
            papers,
            industry=False,
        ),
        encoding="utf-8",
        newline="\n",
    )
    (output_root / "industry" / "README.md").write_text(
        _render_collection(
            "Industry & Open-Source Inference Systems",
            "Full collection of production systems, open-source runtimes, infrastructure projects, and engineering material.",
            industry,
            industry=True,
        ),
        encoding="utf-8",
        newline="\n",
    )
