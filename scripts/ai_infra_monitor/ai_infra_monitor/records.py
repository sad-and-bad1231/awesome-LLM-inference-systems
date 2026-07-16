from __future__ import annotations

import errno
import hashlib
import json
import re
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .identity import normalize_title, record_identity
from .models import Candidate
from .triage import triage_candidate


ABSTRACTIONS = (
    "Memory Topology & Virtualization",
    "Disaggregated Interconnects",
    "State Compression & Signal Coding",
    "Execution Compilation & Kernel Fusion",
    "Program-Aware Scheduling",
    "SRE/Fault-Tolerance/Sparing",
)

PAPER_CATEGORIES = (
    "Runtime、调度与服务架构",
    "分离式推理、通信与 KV 传输",
    "长上下文、KV 状态与外部记忆",
    "KV Cache 压缩、量化与淘汰",
    "推测解码、Test-time Scaling 与生成加速",
    "算子、编译与硬件加速",
    "MoE、Adapter、多租户与模型服务",
    "Agent、RAG、多模态与应用级 Serving",
    "Workload、评测、可靠性与方法论",
    "AI 集群、向量数据库、安全与周边基础设施",
)

GENERATED_NOTICE = "<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->"
ABSTRACTION_DESCRIPTIONS = {
    "Memory Topology & Virtualization": "KV cache、long-context state、offload、prefix/RAG cache、CXL/分层内存。",
    "Disaggregated Interconnects": "P/D 分离、KV transfer、RDMA/NIXL/UCCL、collective 和跨节点路由。",
    "State Compression & Signal Coding": "低比特 KV、MLA latent、稀疏/量化/编码压缩与质量-成本权衡。",
    "Execution Compilation & Kernel Fusion": "Triton/CUDA/HIP kernel、attention/GEMM/MoE 算子、编译和硬件后端。",
    "Program-Aware Scheduling": "agent graph、structured generation、多阶段工作流和程序感知调度。",
    "SRE/Fault-Tolerance/Sparing": "trace/benchmark、SLO、故障恢复、漂移、数值稳定性和生产降级。",
}
ABSTRACTION_REPRESENTATIVE_LIMIT = 12

KNOWN_CANONICALS = {
    "prism unleashing gpu sharing cost efficient multi llm serving": (
        "paper:osdi-2026-prism",
        "Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning",
    ),
    "chimera cost efficient multi llm serving via gpu memory ballooning": (
        "paper:osdi-2026-prism",
        "Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning",
    ),
    "contextra hierarchical context caching long context language model serving": (
        "paper:osdi-2026-strata",
        "Strata",
    ),
    "llmfabric unifying decentralized hpc clusters heterogeneous llm serving": (
        "paper:osdi-2026-opentela",
        "OpenTela",
    ),
}


def _evidence(record: dict[str, Any]) -> dict[str, str]:
    channel = str(record.get("venue_or_channel", "")).lower()
    if "arxiv" in channel:
        source_type = "arxiv"
        venue_status = "preprint"
    elif any(token in channel for token in ("poster", "workshop")):
        source_type = "conference_program"
        venue_status = "poster_or_workshop"
    elif any(
        token in channel
        for token in (
            "osdi",
            "sosp",
            "icml",
            "iclr",
            "mlsys",
            "usenix",
            "nsdi",
            "asplos",
            "eurosys",
            "euro-par",
            "europar",
            "icpe",
            "socc",
            "cloud",
            "icdcs",
            "hpca",
            "hpdc",
            "cgo",
            "ppopp",
            "pldi",
            "micro",
            "sigcomm",
            "sigmetrics",
            "ipdps",
            "ics",
            "acsos",
        )
    ):
        source_type = "conference_program"
        venue_status = "formal_conference"
    elif record.get("record_type") in {"industry", "project"}:
        source_type = "project_or_engineering_material"
        venue_status = "industrial_material"
    else:
        source_type = "legacy_markdown"
        venue_status = "unclassified"
    return {
        "venue_status": venue_status,
        "source_type": source_type,
        "verification_level": (
            "official_source"
            if record.get("source_ids") and record.get("source_tier") != "legacy"
            else "legacy_import"
        ),
        "verified_at": "",
    }


def _canonical_fields(record: dict[str, Any]) -> dict[str, Any]:
    title = str(record.get("title", "")).strip()
    title_key = normalize_title(title)
    canonical_id, canonical_title = KNOWN_CANONICALS.get(
        title_key,
        (record_identity(title, str(record.get("primary_url", "")), list(record.get("source_ids", []))), title),
    )
    aliases = [alias for alias in record.get("aliases", []) if alias and alias != canonical_title]
    if title != canonical_title and title not in aliases:
        aliases.append(title)
    record["title"] = canonical_title
    record["canonical_id"] = canonical_id
    record.setdefault("id", _stable_id(str(record.get("record_type", "record")), canonical_title, str(record.get("primary_url", ""))))
    record["aliases"] = sorted(set(aliases))
    history = list(record.get("status_history", []))
    current = {
        "status": record.get("status", ""),
        "venue_or_channel": record.get("venue_or_channel", ""),
        "source_tier": record.get("source_tier", ""),
    }
    if current not in history:
        history.append(current)
    record["status_history"] = history
    existing_evidence = dict(record.get("evidence", {}))
    computed_evidence = _evidence(record)
    for key in ("source_type", "venue_status"):
        if existing_evidence.get(key) in {None, "", "legacy_markdown", "unclassified"}:
            existing_evidence[key] = computed_evidence[key]
    if record.get("source_ids") and record.get("source_tier") != "legacy":
        existing_evidence["verification_level"] = computed_evidence["verification_level"]
    record["evidence"] = existing_evidence
    return record


def normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    """Fill the current schema while preserving imported facts."""
    normalized = dict(record)
    normalized.setdefault("aliases", [])
    normalized.setdefault("status_history", [])
    normalized.setdefault("evidence", {})
    normalized.setdefault("source_ids", [])
    normalized.setdefault("artifact_url", "")
    normalized.setdefault("display_category", "")
    normalized.setdefault("topics", [])
    normalized.setdefault("discovered", "")
    return _canonical_fields(normalized)


@dataclass(frozen=True)
class RecordValidationError:
    path: Path
    line: int
    message: str


def _slug(value: str) -> str:
    normalized = normalize_title(value)
    slug = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    return slug[:72] or "record"


def _stable_id(record_type: str, title: str, url: str = "") -> str:
    digest = hashlib.sha1(f"{record_type}\n{normalize_title(title)}\n{url}".encode("utf-8")).hexdigest()[:10]
    return f"{record_type}-{_slug(title)}-{digest}"


def _escape(value: object) -> str:
    return " ".join(str(value or "").replace("|", "/").split())


def _markdown_link_url(value: str) -> str:
    match = re.search(r"\]\((https?://[^)]+)\)", value)
    return match.group(1) if match else ""


def _strip_markdown_link(value: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value).strip()


def _year_from_text(value: str) -> str:
    match = re.search(r"(20\d{2})", value or "")
    return match.group(1) if match else ""


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _base_tags(text: str) -> dict[str, list[str]]:
    lowered = text.lower()
    tags = {
        "phase": [],
        "hardware": [],
        "optimization_layer": [],
        "workload": [],
        "framework_binding": [],
        "metrics": [],
    }
    for phase in ("prefill", "decode", "training", "serving", "routing"):
        if phase in lowered:
            tags["phase"].append(phase)
    for hardware in ("cuda", "gpu", "npu", "tpu", "rocm", "amd", "hopper", "blackwell", "cxl", "rdma"):
        if hardware in lowered:
            tags["hardware"].append(hardware)
    for layer in ("kv-cache", "quantization", "kernel", "compiler", "scheduler", "routing", "memory", "compression", "moe"):
        needle = layer.replace("-", " ")
        if layer in lowered or needle in lowered:
            tags["optimization_layer"].append(layer)
    for workload in ("long-context", "long-cot", "agent", "rag", "multimodal", "video", "moe", "edge"):
        needle = workload.replace("-", " ")
        if workload in lowered or needle in lowered:
            tags["workload"].append(workload)
    for binding in ("vllm", "sglang", "tensorrt-llm", "kserve", "llm-d", "lmcache", "kubernetes", "docker"):
        if binding in lowered:
            tags["framework_binding"].append(binding)
    for metric in ("ttft", "tpot", "goodput", "latency", "throughput", "slo", "stall", "reproducibility"):
        if metric in lowered:
            tags["metrics"].append(metric)
    return {key: sorted(set(values)) for key, values in tags.items()}


def _abstraction_from_text(text: str, category: str = "") -> str:
    lowered = f"{text} {category}".lower()
    if any(term in lowered for term in ("disaggreg", "rdma", "cxl", "nixl", "collective", "all-to-all", "interconnect")):
        return "Disaggregated Interconnects"
    if any(term in lowered for term in ("quant", "compression", "low-bit", "fp4", "fp8", "int4", "latent", "coding")):
        return "State Compression & Signal Coding"
    if any(term in lowered for term in ("kernel", "compiler", "triton", "cuda", "rocm", "operator", "fusion", "hardware", "accelerator")):
        return "Execution Compilation & Kernel Fusion"
    if any(term in lowered for term in ("fault", "reliab", "checkpoint", "restore", "sre", "drift", "benchmark", "trace", "security", "spot")):
        return "SRE/Fault-Tolerance/Sparing"
    if any(term in lowered for term in ("kv", "cache", "memory", "long context", "state", "pagedattention", "vattention")):
        return "Memory Topology & Virtualization"
    return "Program-Aware Scheduling"


def _record(
    *,
    record_type: str,
    title: str,
    venue_or_channel: str,
    year: str,
    orgs: str,
    summary: str,
    source_tier: str,
    primary_url: str,
    artifact_url: str = "",
    source_ids: list[str] | None = None,
    status: str = "verified_legacy",
    display_category: str = "",
    topics: list[str] | None = None,
    triage: dict[str, object] | None = None,
    discovered: str = "",
) -> dict[str, Any]:
    text = " ".join((title, venue_or_channel, orgs, summary, display_category, " ".join(topics or [])))
    record = {
        "id": _stable_id(record_type, title, primary_url),
        "record_type": record_type,
        "title": _strip_markdown_link(title),
        "venue_or_channel": venue_or_channel,
        "year": year,
        "orgs": orgs,
        "summary": summary,
        "source_tier": source_tier,
        "primary_url": primary_url,
        "artifact_url": artifact_url,
        "source_ids": source_ids or [],
        "status": status,
        "system_abstraction_primary": _abstraction_from_text(text, display_category),
        "system_abstraction_secondary": [],
        "technical_tags": _base_tags(text),
        "triage": triage
        or {
            "verdict": "keep",
            "priority": "normal",
            "reasons": ["migrated from verified markdown"],
            "repo_signals": {},
            "physical_eval": {},
            "llm_review": {"status": "not_configured"},
        },
        "display_category": display_category,
        "topics": topics or [],
        "discovered": discovered,
    }
    return normalize_record(record)


def load_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def write_records(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(record, ensure_ascii=False, sort_keys=True) for record in records)
    payload = text + ("\n" if text else "")
    for attempt in range(5):
        try:
            path.write_text(payload, encoding="utf-8", newline="\n")
            return
        except OSError as exc:
            # Windows security scanners can briefly hold a freshly appended JSONL file.
            if exc.errno not in {errno.EINVAL, errno.EACCES, errno.EBUSY} or attempt == 4:
                raise
            time.sleep(0.2 * (attempt + 1))


def _merge_record_evidence(existing: dict[str, Any], incoming: dict[str, Any]) -> bool:
    before = json.dumps(existing, ensure_ascii=False, sort_keys=True)
    for field in ("primary_url", "artifact_url"):
        if incoming.get(field) and not existing.get(field):
            existing[field] = incoming[field]
    if existing.get("source_tier") == "legacy" and incoming.get("source_tier") != "legacy":
        existing["source_tier"] = incoming["source_tier"]
    for source_id in incoming.get("source_ids", []):
        if source_id and source_id not in existing.setdefault("source_ids", []):
            existing["source_ids"].append(source_id)
    incoming_summary = str(incoming.get("summary", ""))
    existing_summary = str(existing.get("summary", ""))
    if incoming_summary and (
        not existing_summary
        or existing_summary.startswith("migrated from")
        or len(incoming_summary) > len(existing_summary)
    ):
        existing["summary"] = incoming_summary
    for topic in incoming.get("topics", []):
        if topic and topic not in existing.setdefault("topics", []):
            existing["topics"].append(topic)
    existing_tags = existing.setdefault("technical_tags", {})
    for key, values in incoming.get("technical_tags", {}).items():
        current = existing_tags.setdefault(key, [])
        for value in values:
            if value and value not in current:
                current.append(value)
        current.sort()
    if incoming.get("status") in {"queued", "promote"} and incoming.get("triage"):
        existing["triage"] = incoming["triage"]
    normalized = normalize_record(existing)
    existing.clear()
    existing.update(normalized)
    after = json.dumps(existing, ensure_ascii=False, sort_keys=True)
    return before != after


def append_records(path: Path, records: list[dict[str, Any]]) -> int:
    existing = load_records(path)
    lookup: dict[tuple[str, str], int] = {}
    for index, record in enumerate(existing):
        lookup[(str(record.get("canonical_id", "")), "canonical")] = index
        lookup[(normalize_title(record.get("title", "")), "title")] = index
    seen_ids = {record.get("id") for record in existing}
    appended = []
    changed_existing = False
    for record in records:
        record = normalize_record(record)
        title_key = normalize_title(record.get("title", ""))
        canonical_id = record.get("canonical_id")
        existing_index = lookup.get((str(canonical_id), "canonical"))
        if existing_index is None:
            existing_index = lookup.get((title_key, "title"))
        if existing_index is not None:
            changed_existing = _merge_record_evidence(existing[existing_index], record) or changed_existing
            continue
        if not title_key or record.get("id") in seen_ids:
            continue
        appended.append(record)
        seen_ids.add(record.get("id"))
        lookup[(str(canonical_id), "canonical")] = len(existing) + len(appended) - 1
        lookup[(title_key, "title")] = len(existing) + len(appended) - 1
    if changed_existing:
        write_records(path, existing + appended)
    elif appended:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as stream:
            for record in appended:
                stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    return len(appended)


def compact_candidate_records(path: Path) -> int:
    """Keep only actionable candidates active while preserving rejected evidence."""
    records = load_records(path)
    changed = 0
    for record in records:
        if record.get("record_type") != "candidate" or record.get("status") in {"drop", "promote"}:
            continue
        triage = record.get("triage", {})
        actionable = (
            triage.get("verdict") == "keep"
            and triage.get("priority") in {"high", "normal"}
        )
        if not actionable:
            record["status"] = "drop"
            normalize_record(record)
            changed += 1
    if changed:
        write_records(path, records)
    return changed


def candidate_to_record(candidate: Candidate, record_type: str = "candidate", status: str = "new") -> dict[str, Any]:
    triage = candidate.triage or triage_candidate(candidate).to_dict()
    summary = candidate.summary
    if not summary:
        summary = f"{candidate.source_name or candidate.source_id} 官方页面条目；发现源未提供摘要，需进一步核对正文。"
    return _record(
        record_type=record_type,
        title=candidate.title,
        venue_or_channel=candidate.venue or candidate.source_name or candidate.source_id,
        year=_year_from_text(candidate.published or candidate.discovered),
        orgs="",
        summary=summary,
        source_tier=candidate.tier,
        primary_url=candidate.url,
        source_ids=[candidate.source_id] if candidate.source_id else [],
        status=status,
        topics=list(candidate.topics),
        triage=triage,
        discovered=candidate.discovered,
    )


def promote_candidates(
    paper_path: Path, industry_path: Path, candidates: list[Candidate]
) -> dict[str, int]:
    paper_records = [candidate_to_record(item, "paper", "queued") for item in candidates if item.kind == "paper"]
    industry_records = [
        candidate_to_record(item, item.kind if item.kind in {"project", "industry"} else "industry", "queued")
        for item in candidates
        if item.kind in {"project", "industry"}
    ]
    return {
        "papers": append_records(paper_path, paper_records),
        "industry": append_records(industry_path, industry_records),
    }


def migrate_markdown_to_jsonl(
    paper_path: Path, industry_path: Path, candidate_path: Path, db_path: Path
) -> int:
    records: list[dict[str, Any]] = []
    current_category = ""
    for line in paper_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            name = line[3:].strip()
            current_category = name if name in PAPER_CATEGORIES else ""
            continue
        if not current_category or not line.startswith("| ") or line.startswith("|---") or line.startswith("| 题目"):
            continue
        cells = _cells(line)
        if len(cells) != 4:
            continue
        records.append(
            _record(
                record_type="paper",
                title=cells[0],
                venue_or_channel=cells[1],
                year=_year_from_text(cells[1]),
                orgs=cells[2],
                summary=cells[3],
                source_tier="legacy",
                primary_url=_markdown_link_url(cells[0]),
                status="verified_legacy",
                display_category=current_category,
            )
        )

    for line in industry_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or line.startswith("|---") or line.startswith("| 企业/组织"):
            continue
        cells = _cells(line)
        if len(cells) != 6:
            continue
        records.append(
            _record(
                record_type="industry",
                title=cells[1],
                venue_or_channel=cells[3],
                year=_year_from_text(cells[2]),
                orgs=cells[0],
                summary=cells[4],
                source_tier="legacy",
                primary_url=_markdown_link_url(cells[5]),
                artifact_url=_markdown_link_url(cells[5]),
                status="verified" if _markdown_link_url(cells[5]) else "verified_legacy",
                display_category=cells[3],
            )
        )

    for line in candidate_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = _cells(line)
        if len(cells) != 8:
            continue
        url = _markdown_link_url(cells[6])
        topics = [topic.strip() for topic in cells[5].split(",") if topic.strip()]
        candidate = Candidate(
            title=cells[4],
            url=url,
            source_id=cells[3],
            source_name=cells[3],
            tier=cells[1],
            kind=cells[2],
            discovered=cells[0],
            topics=tuple(topics),
        )
        records.append(
            _record(
                record_type="candidate",
                title=cells[4],
                venue_or_channel=cells[3],
                year=_year_from_text(cells[0]),
                orgs="",
                summary="",
                source_tier=cells[1],
                primary_url=url,
                source_ids=[cells[3]],
                status=cells[7],
                display_category="Candidate Pool",
                topics=topics,
                discovered=cells[0],
                triage=triage_candidate(candidate).to_dict(),
            )
        )

    records = _merge_candidate_conflicts(records)
    write_records(db_path, records)
    return len(records)


def _merge_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: dict[str, dict[str, Any]] = {}
    for raw in records:
        record = normalize_record(raw)
        key = record["canonical_id"]
        if key not in merged:
            merged[key] = record
            continue
        current = merged[key]
        current["aliases"] = sorted(set(current.get("aliases", [])) | set(record.get("aliases", [])))
        current["source_ids"] = sorted(set(current.get("source_ids", [])) | set(record.get("source_ids", [])))
        current["status_history"] = current.get("status_history", []) + [
            item for item in record.get("status_history", []) if item not in current.get("status_history", [])
        ]
        if not current.get("primary_url") and record.get("primary_url"):
            current["primary_url"] = record["primary_url"]
        current_channel = str(current.get("venue_or_channel", "")).lower()
        record_channel = str(record.get("venue_or_channel", "")).lower()
        current_formal = any(token in current_channel for token in ("osdi", "sosp", "icml", "iclr", "mlsys", "usenix", "nsdi", "asplos", "eurosys"))
        record_formal = any(token in record_channel for token in ("osdi", "sosp", "icml", "iclr", "mlsys", "usenix", "nsdi", "asplos", "eurosys"))
        if record_formal and not current_formal:
            for field in ("venue_or_channel", "year", "orgs", "summary", "display_category"):
                if record.get(field):
                    current[field] = record[field]
        if current.get("source_tier") == "legacy" and record.get("source_tier") != "legacy":
            current["source_tier"] = record["source_tier"]
        current["triage"]["reasons"] = sorted(
            set(current.get("triage", {}).get("reasons", []))
            | set(record.get("triage", {}).get("reasons", []))
            | {"merged records sharing canonical identity"}
        )
        if not current.get("presentation") and record.get("presentation"):
            current["presentation"] = record["presentation"]
    return list(merged.values())


def migrate_jsonl_to_split_stores(
    source_path: Path, paper_path: Path, industry_path: Path, candidate_path: Path
) -> dict[str, int]:
    records = _merge_records(load_records(source_path))
    papers = [record for record in records if record.get("record_type") == "paper"]
    industry = [record for record in records if record.get("record_type") in {"industry", "project"}]
    candidates = [record for record in records if record.get("record_type") == "candidate"]
    write_records(paper_path, papers)
    write_records(industry_path, industry)
    write_records(candidate_path, candidates)
    return {"papers": len(papers), "industry": len(industry), "candidates": len(candidates)}


def _merge_candidate_conflicts(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    verified_by_title: dict[str, dict[str, Any]] = {}
    for record in records:
        title_key = normalize_title(record.get("title", ""))
        if record.get("record_type") != "candidate" and record.get("status") not in {"new", "keep", "drop", "promote"}:
            verified_by_title[title_key] = record

    merged: list[dict[str, Any]] = []
    for record in records:
        title_key = normalize_title(record.get("title", ""))
        verified = verified_by_title.get(title_key)
        if record.get("record_type") == "candidate" and verified is not None:
            if record.get("primary_url") and not verified.get("primary_url"):
                verified["primary_url"] = record["primary_url"]
            for source_id in record.get("source_ids", []):
                if source_id and source_id not in verified["source_ids"]:
                    verified["source_ids"].append(source_id)
            verified["triage"]["reasons"] = sorted(
                set(verified["triage"].get("reasons", []))
                | {"merged duplicate promoted candidate during migration"}
            )
            continue
        merged.append(record)
    return merged


def validate_record_store(path: Path) -> list[RecordValidationError]:
    errors: list[RecordValidationError] = []
    if not path.exists():
        return [RecordValidationError(path, 0, "record store does not exist")]
    seen_titles: dict[str, int] = {}
    seen_canonicals: dict[str, int] = {}
    seen_verified: dict[str, int] = {}
    required = {
        "id",
        "record_type",
        "title",
        "venue_or_channel",
        "year",
        "orgs",
        "summary",
        "source_tier",
        "primary_url",
        "artifact_url",
        "source_ids",
        "status",
        "system_abstraction_primary",
        "system_abstraction_secondary",
        "technical_tags",
        "triage",
        "canonical_id",
        "aliases",
        "status_history",
        "evidence",
    }
    tag_keys = {"phase", "hardware", "optimization_layer", "workload", "framework_binding", "metrics"}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            errors.append(RecordValidationError(path, number, f"invalid json: {error}"))
            continue
        missing = sorted(required - set(record))
        if missing:
            errors.append(RecordValidationError(path, number, "missing fields: " + ", ".join(missing)))
        title_key = normalize_title(record.get("title", ""))
        if title_key:
            if title_key in seen_titles:
                errors.append(RecordValidationError(path, number, f"duplicate title: first seen on line {seen_titles[title_key]}"))
            else:
                seen_titles[title_key] = number
        if record.get("record_type") not in {"paper", "project", "industry", "candidate"}:
            errors.append(RecordValidationError(path, number, "invalid record_type"))
        if not record.get("canonical_id"):
            errors.append(RecordValidationError(path, number, "missing canonical_id"))
        elif record["canonical_id"] in seen_canonicals:
            errors.append(RecordValidationError(path, number, f"duplicate canonical_id: first seen on line {seen_canonicals[record['canonical_id']]}"))
        else:
            seen_canonicals[record["canonical_id"]] = number
        if not isinstance(record.get("aliases"), list) or not isinstance(record.get("status_history"), list):
            errors.append(RecordValidationError(path, number, "invalid identity history fields"))
        if not isinstance(record.get("evidence"), dict):
            errors.append(RecordValidationError(path, number, "invalid evidence"))
        presentation = record.get("presentation")
        if presentation is not None:
            if not isinstance(presentation, dict):
                errors.append(RecordValidationError(path, number, "invalid presentation metadata"))
            else:
                if "featured" in presentation and not isinstance(presentation["featured"], bool):
                    errors.append(RecordValidationError(path, number, "presentation.featured must be boolean"))
                if "order" in presentation and (
                    isinstance(presentation["order"], bool)
                    or not isinstance(presentation["order"], int)
                    or presentation["order"] < 0
                ):
                    errors.append(RecordValidationError(path, number, "presentation.order must be a non-negative integer"))
                if "blurb" in presentation and not isinstance(presentation["blurb"], str):
                    errors.append(RecordValidationError(path, number, "presentation.blurb must be a string"))
        if record.get("system_abstraction_primary") not in ABSTRACTIONS:
            errors.append(RecordValidationError(path, number, "invalid system_abstraction_primary"))
        tags = record.get("technical_tags", {})
        if set(tags) != tag_keys or not all(isinstance(tags.get(key), list) for key in tag_keys):
            errors.append(RecordValidationError(path, number, "invalid technical_tags"))
        triage = record.get("triage", {})
        if not isinstance(triage, dict) or not {"verdict", "priority", "reasons", "repo_signals", "physical_eval"}.issubset(triage):
            errors.append(RecordValidationError(path, number, "invalid triage"))
        status = str(record.get("status", ""))
        if status != "verified_legacy" and not record.get("primary_url"):
            errors.append(RecordValidationError(path, number, "missing primary_url"))
        if record.get("record_type") != "candidate" and status not in {"new", "keep", "drop", "promote"}:
            seen_verified[title_key] = number
        elif title_key in seen_verified:
            errors.append(RecordValidationError(path, number, f"candidate conflicts with verified record on line {seen_verified[title_key]}"))
    return errors


def validate_record_stores(
    paper_path: Path, industry_path: Path, candidate_path: Path
) -> list[RecordValidationError]:
    errors: list[RecordValidationError] = []
    stores = {
        paper_path: {"paper"},
        industry_path: {"industry", "project"},
        candidate_path: {"candidate"},
    }
    main_canonicals: dict[str, Path] = {}
    for path, allowed_types in stores.items():
        errors.extend(validate_record_store(path))
        for number, record in enumerate(load_records(path), 1):
            if record.get("record_type") not in allowed_types:
                errors.append(RecordValidationError(path, number, "record_type does not match store"))
            if (
                path != candidate_path
                and record.get("canonical_id")
                and record.get("status") not in {"new", "keep", "drop", "promote", "queued"}
            ):
                main_canonicals[record["canonical_id"]] = path
    for number, record in enumerate(load_records(candidate_path), 1):
        if record.get("canonical_id") in main_canonicals and record.get("status") not in {"drop", "promote"}:
            errors.append(RecordValidationError(candidate_path, number, "candidate conflicts with main store canonical_id"))
    return errors


def _render_link(record: dict[str, Any]) -> str:
    url = record.get("primary_url") or record.get("artifact_url") or ""
    return f"[primary]({url})" if url else ""


def _paper_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("record_type") == "paper" and record.get("status") not in {"new", "keep", "drop", "promote"}
    ]


def _candidate_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("record_type") == "candidate" or record.get("status") in {"new", "keep", "promote", "drop"}
    ]


def _industry_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("record_type") in {"industry", "project"} and record.get("status") not in {"new", "keep", "drop", "promote"}
    ]


def _record_year(record: dict[str, Any]) -> int:
    try:
        return int(record.get("year") or 0)
    except (TypeError, ValueError):
        return 0


def _representative_sort_key(record: dict[str, Any]) -> tuple[int, int, int, str]:
    type_rank = {"paper": 0, "industry": 1, "project": 1, "candidate": 2}
    tier_rank = {"A": 0, "B": 1, "C": 2, "legacy": 1}
    status = str(record.get("status", ""))
    verified_rank = 0 if status not in {"new", "keep", "drop", "promote"} else 1
    return (
        verified_rank,
        type_rank.get(str(record.get("record_type", "")), 3),
        tier_rank.get(str(record.get("source_tier", "")), 3) * 10000 - _record_year(record),
        str(record.get("title", "")),
    )


def _compact_tags(record: dict[str, Any]) -> str:
    tags = record.get("technical_tags", {})
    selected = []
    for key in ("phase", "hardware", "optimization_layer", "workload", "framework_binding", "metrics"):
        values = tags.get(key, [])
        if values:
            selected.append(f"{key}:{','.join(values[:3])}")
    return " ".join(f"[{value}]" for value in selected[:4])


def render_markdown_views(
    paper_db_path: Path,
    industry_db_path: Path,
    candidate_db_path: Path,
    paper_path: Path,
    industry_path: Path,
    candidate_path: Path,
    abstractions_path: Path,
) -> None:
    paper_records = _paper_records(load_records(paper_db_path))
    industry_records = _industry_records(load_records(industry_db_path))
    candidate_records = _candidate_records(load_records(candidate_db_path))
    records = paper_records + industry_records + candidate_records

    category_counts = Counter(record.get("display_category") or _category_for_record(record) for record in paper_records)
    paper_lines = [
        "# Paper List（按类别整理；会议栏为最新发表/审稿状态）",
        "",
        GENERATED_NOTICE,
        "",
        "核验口径：结构化事实源为 `data/papers.jsonl`；本文件由脚本生成，请勿直接编辑。",
        "",
        "## 当前覆盖概览",
        "",
        "| 类别 | 条目数 | 主用途 |",
        "|---|---:|---|",
    ]
    scopes = {
        "Runtime、调度与服务架构": "serving runtime、SLO、batching、autoscaling、serverless、模型路由",
        "分离式推理、通信与 KV 传输": "prefill/decode 分离、KV transfer、collective、CXL/RDMA、多实例编排",
        "长上下文、KV 状态与外部记忆": "长上下文 serving、KV offload、prefix/RAG cache、分层存储与召回",
        "KV Cache 压缩、量化与淘汰": "KV 量化、token/head/layer 保留、稀疏选择、压缩-质量权衡",
        "推测解码、Test-time Scaling 与生成加速": "speculative decoding、并行解码、tree drafting、reasoning 生成加速",
        "算子、编译与硬件加速": "attention/GEMM/MoE kernel、编译器、端侧/NPU/GPU/wafer-scale 加速",
        "MoE、Adapter、多租户与模型服务": "expert routing、adapter serving、多租户 batching、MoE 通信与缓存",
        "Agent、RAG、多模态与应用级 Serving": "agent workflow、RAG pipeline、多模态 stage graph、程序级调度",
        "Workload、评测、可靠性与方法论": "trace、benchmark、fault tolerance、profiling、数值稳定性和理论分析",
        "AI 集群、向量数据库、安全与周边基础设施": "GPU 集群、向量数据库、TEE/FHE、侧信道、spot/geo routing",
    }
    for category in PAPER_CATEGORIES:
        paper_lines.append(f"| {category} | {category_counts.get(category, 0)} | {scopes[category]} |")
    evidence_counts = Counter(record.get("evidence", {}).get("venue_status", "unclassified") for record in paper_records)
    paper_lines.extend([
        "",
        "## Evidence Layers",
        "",
        "事实层与评价层分开：venue status/source type 来自来源材料；triage priority/verdict 只表示筛选意见，不等同于发表等级。",
        "",
        "| Venue Status | Count |",
        "|---|---:|",
    ])
    for venue_status, count in sorted(evidence_counts.items()):
        paper_lines.append(f"| {_escape(venue_status)} | {count} |")
    for category in PAPER_CATEGORIES:
        rows = [record for record in paper_records if (record.get("display_category") or _category_for_record(record)) == category]
        paper_lines.extend(["", f"## {category}", "", "| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |", "|---|---|---|---|"])
        for record in rows:
            paper_lines.append(
                f"| {_escape(record['title'])} | {_escape(record['venue_or_channel'])} | {_escape(record['orgs'])} | {_escape(record['summary'])} |"
            )
    paper_path.write_text("\n".join(paper_lines) + "\n", encoding="utf-8", newline="\n")

    industry_lines = [
        "# 工业界 LLM 推理系统方案追踪",
        "",
        GENERATED_NOTICE,
        "",
        "更新时间：由 `data/industry.jsonl` 生成。",
        "",
        "## 观察框架",
        "",
        "- TTFT under Drift：基础设施漂移、广域网抖动、Spot 节点切换时的首 token 延迟恶化边界。",
        "- Generation Stall Rate：推测解码验证失败、MoE all-to-all 热点或 tool-call 挂起造成的生成中断率。",
        "- Numerical Reproducibility：低精度混合量化、scale search 和异构执行导致的数值不稳定与非确定性。",
        "",
        "## 企业方案清单",
        "",
        "| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |",
        "|---|---|---:|---|---|---|",
    ]
    for record in industry_records:
        industry_lines.append(
            f"| {_escape(record['orgs'])} | {_escape(record['title'])} | {_escape(record['year'])} | {_escape(record['venue_or_channel'])} | {_escape(record['summary'])} | {_render_link(record)} |"
        )
    industry_path.write_text("\n".join(industry_lines) + "\n", encoding="utf-8", newline="\n")

    active_candidates = [
        record for record in candidate_records
        if record.get("status") not in {"drop", "promote"}
    ]
    archived_candidates = [
        record for record in candidate_records
        if record.get("status") in {"drop", "promote"}
    ]
    candidate_lines = [
        "# AI Infra Candidate Pool",
        "",
        GENERATED_NOTICE,
        "",
        f"Active candidates: {len(active_candidates)}. Archived audit items: {len(archived_candidates)}.",
        "",
        "## Active Candidates",
        "",
        "| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for record in active_candidates:
        source = ", ".join(record.get("source_ids", [])) or record.get("venue_or_channel", "")
        topics = ", ".join(record.get("topics", []))
        candidate_lines.append(
            f"| {_escape(record.get('discovered') or record.get('year') or '')} | {_escape(record['source_tier'])} | {_escape(record['record_type'])} | {_escape(source)} | {_escape(record['title'])} | {_escape(topics)} | {_render_link(record)} | {_escape(record['status'])} |"
        )
    if archived_candidates:
        candidate_lines.extend(["", "<details>", "<summary>Archived audit items</summary>", "", "| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |", "|---|---|---|---|---|---|---|---|"])
        for record in archived_candidates:
            source = ", ".join(record.get("source_ids", [])) or record.get("venue_or_channel", "")
            topics = ", ".join(record.get("topics", []))
            candidate_lines.append(
                f"| {_escape(record.get('discovered') or record.get('year') or '')} | {_escape(record['source_tier'])} | {_escape(record['record_type'])} | {_escape(source)} | {_escape(record['title'])} | {_escape(topics)} | {_render_link(record)} | {_escape(record['status'])} |"
            )
        candidate_lines.extend(["", "</details>"])
    candidate_path.write_text("\n".join(candidate_lines) + "\n", encoding="utf-8", newline="\n")

    by_abstraction: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_abstraction[record.get("system_abstraction_primary", "Program-Aware Scheduling")].append(record)
    abstraction_lines = [
        "# AI Infra System Abstractions",
        "",
        GENERATED_NOTICE,
        "",
        "主视图只保留结构、统计和代表条目；公开全量入口见 `papers/README.md` 和 `industry/README.md`，机器事实源见 JSONL。",
        "",
        "## Reading Entry Points",
        "",
        "| Need | File |",
        "|---|---|",
        "| 按系统抽象快速定位方向 | `ai-infra-system-abstractions.md` |",
        "| 查 verified 学术论文全量明细 | `papers/README.md` |",
        "| 查工业界/开源系统全量明细 | `industry/README.md` |",
        "| 查待处理候选 | `ai-infra-candidates.md` |",
        "| 机器可读论文事实源 | `data/papers.jsonl` |",
        "| 机器可读工业事实源 | `data/industry.jsonl` |",
        "| 候选 staging | `data/candidates.jsonl` |",
        "",
        "## Coverage",
        "",
        "| System Abstraction | Total | Papers | Industry/Projects | Candidates | Scope |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for abstraction in ABSTRACTIONS:
        rows = by_abstraction.get(abstraction, [])
        paper_count = sum(record.get("record_type") == "paper" for record in rows)
        industry_count = sum(record.get("record_type") in {"industry", "project"} for record in rows)
        candidate_count = sum(record.get("record_type") == "candidate" for record in rows)
        abstraction_lines.append(
            f"| {abstraction} | {len(rows)} | {paper_count} | {industry_count} | {candidate_count} | {ABSTRACTION_DESCRIPTIONS[abstraction]} |"
        )
    abstraction_lines.extend([
        "",
        "## SRE Metrics To Track",
        "",
        "| Metric | Meaning |",
        "|---|---|",
        "| TTFT under Drift | 基础设施漂移、广域网抖动、Spot 节点切换时的首 token 延迟恶化边界。 |",
        "| Generation Stall Rate | 推测解码验证失败、MoE all-to-all 热点或 tool-call 挂起造成的生成中断率。 |",
        "| Numerical Reproducibility | 低精度混合量化、scale search 和异构执行导致的数值不稳定与非确定性。 |",
        "",
        "## Representative Items",
        "",
    ])
    for abstraction in ABSTRACTIONS:
        rows = sorted(by_abstraction.get(abstraction, []), key=_representative_sort_key)
        abstraction_lines.extend([
            f"### {abstraction}",
            "",
            f"_Showing up to {ABSTRACTION_REPRESENTATIVE_LIMIT} representative records; full detail stays in generated compatibility views and JSONL._",
            "",
            "| Title | Type | Year/Channel | Why it matters | Tags |",
            "|---|---|---|---|---|",
        ])
        for record in rows[:ABSTRACTION_REPRESENTATIVE_LIMIT]:
            abstraction_lines.append(
                f"| {_escape(record['title'])} | {_escape(record['record_type'])} | {_escape(record.get('year') or record['venue_or_channel'])} | {_escape(record['summary'])} | {_escape(_compact_tags(record))} |"
            )
        abstraction_lines.append("")
    abstractions_path.write_text("\n".join(abstraction_lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def _category_for_record(record: dict[str, Any]) -> str:
    abstraction = record.get("system_abstraction_primary")
    if abstraction == "Disaggregated Interconnects":
        return "分离式推理、通信与 KV 传输"
    if abstraction == "Memory Topology & Virtualization":
        return "长上下文、KV 状态与外部记忆"
    if abstraction == "State Compression & Signal Coding":
        return "KV Cache 压缩、量化与淘汰"
    if abstraction == "Execution Compilation & Kernel Fusion":
        return "算子、编译与硬件加速"
    if abstraction == "SRE/Fault-Tolerance/Sparing":
        return "Workload、评测、可靠性与方法论"
    return "Runtime、调度与服务架构"
