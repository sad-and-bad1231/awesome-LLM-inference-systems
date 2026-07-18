from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
from typing import Any
from urllib.parse import quote

from .curation import curation_for, curation_sort_key, is_public_mainline
from .records import ABSTRACTIONS, load_records


GENERATED_NOTICE = "<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->"
PUBLIC_REPOSITORY_URL = "https://github.com/sad-and-bad1231/awesome-LLM-inference-systems"
PUBLIC_CATEGORIES = {
    "Program-Aware Scheduling": "Runtime & Serving",
    "Disaggregated Interconnects": "P/D Disaggregation & KV Transfer",
    "Memory Topology & Virtualization": "KV State & Memory",
    "State Compression & Signal Coding": "KV Compression & Low-Bit State",
    "Execution Compilation & Kernel Fusion": "Kernel & Compiler",
    "SRE/Fault-Tolerance/Sparing": "Reliability & Benchmarks",
}
PUBLIC_CATEGORY_DESCRIPTIONS = {
    "KV State & Memory": "KV blocks, prefix state, offload, external memory, and memory-aware serving.",
    "P/D Disaggregation & KV Transfer": "Prefill/decode separation, KV transfer, routing, and distributed transport.",
    "KV Compression & Low-Bit State": "KV quantization, latent state, sparsity, and quality-cost tradeoffs.",
    "Kernel & Compiler": "CUDA, Triton, HIP, attention, GEMM, MoE kernels, and compiler backends.",
    "Runtime & Serving": "Runtime scheduling, agent graphs, structured generation, and SLO-aware dispatch.",
    "Reliability & Benchmarks": "SLOs, drift, recovery, reproducibility, benchmarks, and graceful degradation.",
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
METRIC_DESCRIPTIONS = (
    ("TTFT under Drift", "首 token 延迟在网络抖动、Spot 切换和基础设施漂移下的恶化边界。"),
    ("Generation Stall Rate", "由验证失败、专家拥塞或 tool-call 挂起造成的生成中断率。"),
    ("Numerical Reproducibility", "混合精度、量化和大规模部署中的数值稳定性与可复现性。"),
)
READING_PATHS = (
    ("Reduce first-token latency", "P/D disaggregation, KV transfer, prefix reuse", "papers/README.md#p-d-disaggregation-kv-transfer"),
    ("Fit longer context", "KV state, offload, compression, and memory tiers", "papers/README.md#kv-state-memory"),
    ("Raise decode goodput", "Kernels, compilation, MoE execution, and batching", "papers/README.md#kernel-compiler"),
    ("Operate in production", "Runtime policy, SLOs, recovery, and ecosystem bindings", "industry/README.md#runtime-serving"),
    ("Deploy beyond CUDA", "AMD, TPU, NPU, Apple, and heterogeneous serving stacks", "industry/README.md#hardware-ecosystem"),
)
EVIDENCE_LADDER = (
    ("Formal venue", "Conference or journal identity confirmed; publication status is shown as metadata."),
    ("Artifact / ecosystem", "A code, runtime, hardware, deployment, or production entry point is linked when available."),
    ("Physical evaluation", "Real hardware or end-to-end serving evidence is preferred over algorithm-only simulation."),
    ("Legacy import", "Imported during migration and retained for coverage; not an implicit quality ranking."),
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


def _format_label(record: dict[str, Any]) -> str:
    if record.get("record_type") == "project":
        return "Open-source project"
    if record.get("record_type") == "industry":
        return "Industry / engineering material"
    source_type = record.get("evidence", {}).get("source_type")
    return {
        "conference_program": "Academic paper",
        "journal_or_conference": "Academic paper",
        "preprint": "Preprint",
    }.get(source_type, "Research record")


def _presentation(record: dict[str, Any]) -> dict[str, Any]:
    value = record.get("presentation")
    return value if isinstance(value, dict) else {}


def _tags(record: dict[str, Any]) -> str:
    tags = record.get("technical_tags", {})
    values = []
    for key in ("phase", "hardware", "optimization_layer", "workload", "framework_binding", "metrics"):
        raw_values = tags.get(key, [])
        if isinstance(raw_values, str):
            raw_values = [raw_values]
        for value in raw_values[:2]:
            if value and value not in values:
                values.append(value)
    return " ".join(f"`{_escape(value)}`" for value in values[:8])


def _sort_key(record: dict[str, Any]) -> tuple[int, int, int, int, str]:
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
    curation = curation_for(record)
    return (
        0 if curation.get("scope") == "core" else 1,
        {"foundation": 0, "frontier": 1, "supporting": 2}.get(curation.get("priority"), 3),
        evidence_rank.get(record.get("evidence", {}).get("venue_status"), 4),
        year,
        str(record.get("title", "")),
    )


def _featured_sort_key(record: dict[str, Any]) -> tuple[int, int, int, int, str]:
    presentation = _presentation(record)
    try:
        order = int(presentation.get("order", 10000))
    except (TypeError, ValueError):
        order = 10000
    base = _sort_key(record)
    return (0 if presentation.get("featured") is True else 1, order, *base)


def _public_records(path: Path, types: set[str]) -> list[dict[str, Any]]:
    return sorted(
        [
            record
            for record in load_records(path)
            if record.get("record_type") in types
            and record.get("status") not in EXCLUDED_STATUSES
            and is_public_mainline(record)
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


def _featured_records(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    explicit = sorted(
        [record for record in records if _presentation(record).get("featured") is True],
        key=_featured_sort_key,
    )
    selected = explicit[:limit]
    selected_ids = {record.get("canonical_id") or record.get("id") for record in selected}
    for record in sorted(records, key=_sort_key):
        identity = record.get("canonical_id") or record.get("id")
        if identity not in selected_ids:
            selected.append(record)
            selected_ids.add(identity)
        if len(selected) >= limit:
            break
    return selected[:limit]


def _archive_records(path: Path, types: set[str]) -> list[dict[str, Any]]:
    return sorted(
        [
            record
            for record in load_records(path)
            if record.get("record_type") in types
            and record.get("status") not in EXCLUDED_STATUSES
            and not is_public_mainline(record)
        ],
        key=curation_sort_key,
    )


def _anchor(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def _summary(record: dict[str, Any]) -> str:
    return _escape(_presentation(record).get("blurb") or record.get("summary") or "No summary provided.")


def _entry(record: dict[str, Any], industry: bool = False, featured: bool = False) -> str:
    url = _url(record)
    title_text = _escape(record.get("title"))
    title = f"[{title_text}]({url})" if url else title_text
    headline = f"**Featured:** **{title}**" if featured else f"**{title}**"
    meta = []
    if industry:
        meta.extend([_escape(record.get("orgs") or "Project"), _escape(record.get("year")), _format_label(record)])
    else:
        meta.extend([_escape(record.get("venue_or_channel")), _escape(record.get("year")), _format_label(record)])
    meta.append(_evidence_label(record))
    lines = [f"- {headline}", f"  {' · '.join(f'`{item}`' for item in meta if item)}"]
    tags = _tags(record)
    if tags:
        lines.append(f"  Tags: {tags}")
    artifact_url = str(record.get("artifact_url") or "")
    if artifact_url and artifact_url != url:
        lines.append(f"  Artifact: [source]({artifact_url})")
    lines.append(f"  {_summary(record)}")
    return "\n".join(lines)


def _group(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped = {abstraction: [] for abstraction in ABSTRACTIONS}
    for record in records:
        grouped.setdefault(record.get("system_abstraction_primary", "Program-Aware Scheduling"), []).append(record)
    return grouped


def _category_counts(papers: list[dict[str, Any]], industry: list[dict[str, Any]]) -> dict[str, int]:
    counts = Counter()
    for record in [*papers, *industry]:
        category = PUBLIC_CATEGORIES.get(record.get("system_abstraction_primary"))
        if category:
            counts[category] += 1
    return counts


def _badge(label: str, value: object, color: str, link: str = "") -> str:
    image = f"https://img.shields.io/badge/{quote(label)}-{quote(str(value))}-{color}"
    badge = f"![{label}]({image})"
    return f"[{badge}]({link})" if link else badge


def _last_updated(records: list[dict[str, Any]]) -> str:
    values = []
    for record in records:
        values.append(str(record.get("evidence", {}).get("verified_at") or ""))
        values.append(str(record.get("year") or ""))
    return max((value for value in values if value), default="unknown")[:10]


def _render_badges(papers: list[dict[str, Any]], industry: list[dict[str, Any]]) -> str:
    formal = sum(record.get("evidence", {}).get("venue_status") == "formal_conference" for record in papers)
    all_records = [*papers, *industry]
    workflow = f"{PUBLIC_REPOSITORY_URL}/actions/workflows/validate-and-render.yml"
    return " ".join(
        [
            _badge("Academic Papers", len(papers), "168de2", "papers/README.md"),
            _badge("Industry Systems", len(industry), "0a8f6a", "industry/README.md"),
            _badge("Formal Venues", formal, "7b61ff", "papers/README.md#evidence-and-selection"),
            _badge("Last Updated", _last_updated(all_records), "555555"),
            _badge("CI", "workflow", "brightgreen", workflow),
        ]
    )


def _render_collection(
    title: str,
    subtitle: str,
    records: list[dict[str, Any]],
    industry: bool,
    image: str,
) -> str:
    grouped = _group(records)
    counts = Counter(PUBLIC_CATEGORIES.get(record.get("system_abstraction_primary"), "Unclassified") for record in records)
    featured_ids = {record.get("canonical_id") or record.get("id") for record in _featured_records(records, 12)}
    primary_status = "industrial_material" if industry else "formal_conference"
    primary_count = sum(record.get("evidence", {}).get("venue_status") == primary_status for record in records)
    artifact_count = sum(bool(record.get("artifact_url")) for record in records)
    tagged_count = sum(any(values for values in record.get("technical_tags", {}).values()) for record in records)
    primary_label = "Industrial material" if industry else "Formal venue"
    lines = [
        f"# {title}",
        "",
        GENERATED_NOTICE,
        "",
        "[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · "
        f"[{('Industry systems' if not industry else 'Academic papers')}](../{('industry' if not industry else 'papers')}/README.md)",
        "",
        subtitle,
        "",
        f"![AI inference system map]({image})",
        "",
        "> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. Adjacent and archived material is kept in the [archive](../archive/README.md).",
        "",
        "## At a Glance",
        "",
        f"| Records | {primary_label} | With artifact | Tagged records |",
        "|---:|---:|---:|---:|",
        f"| {len(records)} | {primary_count} | {artifact_count} | {tagged_count} |",
        "",
        "## Collection Navigation",
        "",
    ]
    lines.extend(
        f"- [{PUBLIC_CATEGORIES[abstraction]}](#{_anchor(PUBLIC_CATEGORIES[abstraction])}) ({counts.get(PUBLIC_CATEGORIES[abstraction], 0)})"
        for abstraction in ABSTRACTIONS
    )
    lines.extend(
        [
            "",
            "## Evidence and Selection",
            "",
            "Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.",
            "",
            "| Field | Reading rule |",
            "|---|---|",
            "| Venue / channel | What kind of source it is, not a quality score. |",
            "| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |",
            "| Artifact | A linked implementation, documentation page, or deployment entry point. |",
            "| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |",
            "| Scope | Only `core` records are shown here; adjacent/archive material is in the archive page. |",
            "| Featured | A small editorial starting set; all core records remain below. |",
            "",
            "## Resource List",
            "",
        ]
    )
    for abstraction in ABSTRACTIONS:
        category = PUBLIC_CATEGORIES[abstraction]
        rows = grouped.get(abstraction, [])
        featured = [record for record in rows if (record.get("canonical_id") or record.get("id")) in featured_ids]
        remaining = [record for record in rows if (record.get("canonical_id") or record.get("id")) not in featured_ids]
        lines.extend([f"### {category} ({len(rows)})", "", PUBLIC_CATEGORY_DESCRIPTIONS[category], ""])
        if not rows:
            lines.append("_No verified records yet._")
        else:
            if featured:
                lines.extend(["#### Featured", ""])
                lines.extend(_entry(record, industry=industry, featured=True) for record in featured)
            if remaining:
                lines.extend(["#### Full Resource List", ""])
                lines.extend(_entry(record, industry=industry) for record in remaining)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _render_archive(
    papers: list[dict[str, Any]], industry: list[dict[str, Any]]
) -> str:
    lines = [
        "# AI Infra Adjacent and Archive",
        "",
        GENERATED_NOTICE,
        "",
        "本页集中存放偏离 serving 主线或暂不适合作为优先阅读入口的记录。事实、来源和摘要仍然保留；当 workload 或系统证据变强时，可重新进入主线。",
        "",
        "[Home](../README.md) · [Academic papers](../papers/README.md) · [Industry systems](../industry/README.md)",
        "",
        "## Reading Rule",
        "",
        "`adjacent` 表示与 AI Infra 有关但不直接改变 LLM serving 执行路径；`archive` 表示没有 guide.md 定义的 kernel/serving 主线信号。归档不是事实否定，也不是永久删除。",
        "",
        "| Scope | Papers | Industry / Projects |",
        "|---|---:|---:|",
        f"| adjacent | {sum(curation_for(record).get('scope') == 'adjacent' for record in papers)} | {sum(curation_for(record).get('scope') == 'adjacent' for record in industry)} |",
        f"| archive | {sum(curation_for(record).get('scope') == 'archive' for record in papers)} | {sum(curation_for(record).get('scope') == 'archive' for record in industry)} |",
    ]
    for label, records, is_industry in (
        ("Academic Papers", papers, False),
        ("Industry and Projects", industry, True),
    ):
        lines.extend([
            "",
            f"## {label}",
            "",
            "| Scope | Priority | Year | Title | Channel / Organization | Reason |",
            "|---|---|---:|---|---|---|",
        ])
        if not records:
            lines.append("| - | - | - | No archived records | - | - |")
            continue
        for record in records:
            curation = curation_for(record)
            target = _url(record)
            title = f"[{_escape(record.get('title'))}]({target})" if target else _escape(record.get("title"))
            channel = record.get("orgs") if is_industry else record.get("venue_or_channel")
            reason = "; ".join(curation.get("reasons", []))
            lines.append(
                f"| {_escape(curation.get('scope'))} | {_escape(curation.get('priority'))} | {_escape(record.get('year'))} | {title} | {_escape(channel)} | {_escape(reason)} |"
            )
    return "\n".join(lines).rstrip() + "\n"


def _render_root(papers: list[dict[str, Any]], industry: list[dict[str, Any]]) -> str:
    paper_counts = Counter(_evidence_label(record) for record in papers)
    industry_counts = Counter(_evidence_label(record) for record in industry)
    category_counts = _category_counts(papers, industry)
    featured_papers = _featured_records(papers, 8)
    featured_industry = _featured_records(industry, 6)
    formal_papers = sum(record.get("evidence", {}).get("venue_status") == "formal_conference" for record in papers)
    lines = [
        "# Awesome AI Inference Systems",
        "",
        GENERATED_NOTICE,
        "",
        _render_badges(papers, industry),
        "",
        "![AI inference systems serving stack](figs/ai-inference-systems-cover.png)",
        "",
        "> **A serving-first research entrance.** Follow the request path from admission to output, then inspect where state lives, how it moves, how kernels execute, and how production systems recover.",
        "",
        "A curated, evidence-aware collection of LLM inference serving papers, industrial systems, and open-source AI infrastructure.",
        "",
        "## Overview",
        "",
        "This repository maps the serving mainline from request state to production operations: memory, transport, execution, runtime scheduling, and reliability. The public reading path follows guide.md and keeps peripheral records in the archive.",
        "",
        "We prioritize work with system-level mechanisms, real hardware or production evidence, and clear connections to serving ecosystems such as vLLM, SGLang, TensorRT-LLM, Kubernetes, and LMCache.",
        "",
        "Out of scope by default: training-only methods, algorithm-only simulations without serving evidence, generic vector databases, and peripheral hardware work without an inference-system connection.",
        "",
        "| In scope | Usually excluded unless they directly affect serving |",
        "|---|---|",
        "| LLM serving, KV state, P/D transport, kernels, runtimes, scheduling, SRE, and production infrastructure | Training-only optimization, pure model quality work, generic databases, and hardware papers without an inference path |",
        "",
        "## Start Here",
        "",
        "| Research entry point | What you get |",
        "|---|---|",
        "| [Paper map](figs/ai-inference-system-map.png) | The six system abstractions and the serving lifecycle in one figure. |",
        "| [Academic papers](papers/README.md) | Formal venues, preprints, legacy imports, and evidence labels kept separate. |",
        "| [Industry systems](industry/README.md) | Core runtimes, operators, hardware stacks, transfer layers, and production material. |",
        "| [Adjacent / archive](archive/README.md) | Peripheral or lower-priority records retained for audit without occupying the main reading path. |",
        "| [Machine facts](data/papers.jsonl) | The JSONL records used to regenerate every public view. |",
        "",
        "## Contents",
        "",
        "| Start here | Purpose |",
        "|---|---|",
        "| [Academic Papers](papers/README.md) | Conference, poster, workshop, preprint, and legacy-import paper records. |",
        "| [Industry & Open-Source Systems](industry/README.md) | Core runtimes, operators, hardware stacks, transfer layers, and production material. |",
        "| [Adjacent / Archive](archive/README.md) | Related but non-mainline records, preserved with reasons and links. |",
        "| [System Abstraction Overview](ai-infra-system-abstractions.md) | Cross-collection taxonomy and full system map. |",
        "| [Contribution Guide](CONTRIBUTING.md) | JSONL facts, evidence policy, and generated-view workflow. |",
        "",
        "## Coverage",
        "",
        "| Papers | Industry systems | Formal paper venues | System abstractions |",
        "|---:|---:|---:|---:|",
        f"| {len(papers)} | {len(industry)} | {formal_papers} | {len(ABSTRACTIONS)} |",
        "",
        "| Collection | Records | Evidence breakdown |",
        "|---|---:|---|",
        f"| Academic papers | {len(papers)} | {_escape(', '.join(f'{key}: {value}' for key, value in sorted(paper_counts.items())))} |",
        f"| Industry / open-source systems | {len(industry)} | {_escape(', '.join(f'{key}: {value}' for key, value in sorted(industry_counts.items())))} |",
        "",
        "## Reading Paths",
        "",
        "| Research question | Follow this path |",
        "|---|---|",
    ]
    for question, path, link in READING_PATHS:
        lines.append(f"| **{question}** | {path} ([open](%s)) |" % link)
    lines.extend(
        [
        "",
        "## Taxonomy",
        "",
        "| System abstraction | Records | What it covers | Entry points |",
        "|---|---:|---|---|",
    ]
    )
    for abstraction in ABSTRACTIONS:
        category = PUBLIC_CATEGORIES[abstraction]
        anchor = _anchor(category)
        lines.append(
            f"| **{category}** | {category_counts.get(category, 0)} | {_escape(PUBLIC_CATEGORY_DESCRIPTIONS[category])} | [Papers](papers/README.md#{anchor}) · [Industry](industry/README.md#{anchor}) |"
        )
    lines.extend(
        [
            "",
            "## System Map",
            "",
            "![AI inference system abstractions](figs/ai-inference-system-map.png)",
            "",
            "## Featured Papers",
            "",
        ]
    )
    lines.extend(_entry(record) for record in featured_papers)
    lines.extend(["", "## Featured Industry Systems", ""])
    lines.extend(_entry(record, industry=True) for record in featured_industry)
    lines.extend(
        [
            "",
            "## Evaluation Lens",
            "",
            "The collection tracks system behavior beyond isolated token throughput:",
            "",
            "| Metric | What to look for |",
            "|---|---|",
        ]
    )
    lines.extend(f"| **{name}** | {description} |" for name, description in METRIC_DESCRIPTIONS)
    lines.extend(
        [
            "",
            "## Evidence Policy",
            "",
            "Venue status and source type are factual metadata. Technical tags summarize the system surface. Legacy imports are marked explicitly. Internal triage priority is a discovery signal, not a publication-quality ranking.",
            "",
            "### Evidence Ladder",
            "",
            "| Evidence layer | How it is used |",
            "|---|---|",
        ]
    )
    lines.extend(f"| **{name}** | {description} |" for name, description in EVIDENCE_LADDER)
    lines.extend(
        [
            "",
            "## Contributing",
            "",
            "Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Add facts to JSONL and regenerate the Markdown views; do not edit generated tables directly.",
            "",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def render_public_repository(papers_path: Path, industry_path: Path, output_root: Path) -> None:
    papers = _public_records(papers_path, {"paper"})
    industry = _public_records(industry_path, {"industry", "project"})
    archived_papers = _archive_records(papers_path, {"paper"})
    archived_industry = _archive_records(industry_path, {"industry", "project"})
    (output_root / "papers").mkdir(parents=True, exist_ok=True)
    (output_root / "industry").mkdir(parents=True, exist_ok=True)
    (output_root / "archive").mkdir(parents=True, exist_ok=True)
    (output_root / "README.md").write_text(_render_root(papers, industry), encoding="utf-8", newline="\n")
    (output_root / "papers" / "README.md").write_text(
        _render_collection(
            "AI Inference Papers",
            "A complete academic paper collection organized by serving-system abstraction. Formal venues, posters/workshops, preprints, and legacy imports are labeled separately.",
            papers,
            industry=False,
            image="../figs/ai-inference-system-map.png",
        ),
        encoding="utf-8",
        newline="\n",
    )
    (output_root / "industry" / "README.md").write_text(
        _render_collection(
            "Industry & Open-Source Inference Systems",
            "A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.",
            industry,
            industry=True,
            image="../figs/ai-inference-system-map.png",
        ),
        encoding="utf-8",
        newline="\n",
    )
    (output_root / "archive" / "README.md").write_text(
        _render_archive(archived_papers, archived_industry),
        encoding="utf-8",
        newline="\n",
    )
