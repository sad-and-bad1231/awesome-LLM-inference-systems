"""Deterministic guide-based reading lanes, themes, and priorities."""

from __future__ import annotations

from datetime import date, datetime, timedelta
import re
from typing import Any
from urllib.parse import urlparse


CURATION_VERSION = "guide-2026-v6"
SCOPES = ("core", "adjacent", "archive")
PRIORITIES = ("foundation", "frontier", "supporting")

# 记录 topics 中带此标记时，强制 scope=core / priority=foundation。
# 用于人工策展的经典根节点：它们用词与现代论文不同，关键词启发式会误判为 archive。
FOUNDATION_PIN_TOPIC = "foundation-pinned"

# 记录 topics 中带此标记时，强制 scope=archive / priority=supporting。
# 用于人工策展：pre-2026 的非奠基论文统一退出公开主线，保留事实但移入 archive。
ARCHIVE_PIN_TOPIC = "archive-pinned"

# 记录 topics 中带此标记时，强制 scope=core，priority 仍按常规规则判定（前沿工作=frontier）。
# 用于人工策展的高价值前沿工作：它们的标题/渠道不含主题关键词（例如 "long context caching"、
# "tensor program"、"online LLM inference"），关键词启发式会误判为 archive 而从主线消失。
CORE_PIN_TOPIC = "core-pinned"

# 华为全栈专题里属于「公司技术栈背景」而非「稳定推理主线」的分组：显式踢出主线，
# 保留事实但归入 adjacent（在公开视图里只作为探索观察出现）。
HUAWEI_FULL_STACK_ADJACENT_GROUPS = {
    "training-frameworks",
    "cloud-platform",
    "cpu-heterogeneous",
}

THEME_ORDER = (
    "attention-kernel",
    "kv-cache",
    "prefill-decode-transfer",
    "speculative-decoding",
    "moe",
    "compiler-dsl",
    "runtime-scheduling",
    # 展示用兜底主线：人工钉选的经典根节点（架构/训练/量化等）不命中上面任何关键词
    # 主线；若不兜底，它们会从所有分区里消失。它从不参与关键词命中，只在渲染时由
    # reading.display_themes 补位。
    "foundation",
)

THEME_TERMS = {
    "foundation": (),
    "attention-kernel": (
        "flashattention", "flash attention", "attention kernel", "pagedattention",
        "long-sequence attention", "io-aware attention",
    ),
    "kv-cache": (
        "kv cache", "kvcache", "prefix cache", "paged kv", "kv compression",
        "kv offload", "cache eviction",
    ),
    "prefill-decode-transfer": (
        "prefill", "decode", "disaggregated serving", "disaggregated inference",
        "kv transfer", "nixl", "rdma", "p/d",
    ),
    "speculative-decoding": (
        "speculative decoding", "draft verify", "draft/verify", "speculation",
        "medusa", "tree drafting",
    ),
    "moe": (
        "mixture-of-experts", "mixture of experts", "moe", "expert routing",
        "expert parallel", "expert cache", "all-to-all",
    ),
    "compiler-dsl": (
        "triton", "cuda", "rocm", "wave compiler", "compiler", "dsl",
        "kernel fusion", "fused kernel", "parallelkittens", "tensor program",
    ),
    "runtime-scheduling": (
        "llm serving", "inference serving", "inference runtime", "inference engine",
        "continuous batching", "scheduler", "scheduling", "goodput", "autoscaling",
        "serverless inference", "vllm", "sglang", "tensorrt-llm",
    ),
}

FOUNDATION_TERMS = (
    "orca", "pagedattention", "flashattention:", "flashattention-1", "flashattention-2",
    "flashattention-3", "flexgen", "distserve", "sarathi", "splitwise",
    "continuous batching", "deepspeed-fastgen", "sarathi-serve", "llumnix", "p/d-serve",
    "deepspeed inference", "s-lora", "sglang", "memserve:", "hydragen:", "medusa:",
    "prompt cache:", "flashinfer", "vllm v1", "torch.compile", "flexattention",
    "tutel", "deepspeed-moe", "megablocks:",
)

PERIPHERAL_TERMS = (
    "training communication", "training-only", "vector database", "trusted execution",
    "fully homomorphic", "membership inference", "side-channel", "timing attack",
    "security attack", "privacy-preserving", "point cloud", "3d gaussian",
    "image classification", "object detection", "generic database",
)

EXPLORATION_TERMS = (
    "agent", "agentic", "rag", "multimodal", "diffusion", "video generation",
    "speech generation", "comic", "edge", "mobile", "tool calling", "reasoning",
    "reliability", "workload", "coding",
)

MODEL_TERMS = (
    "llm", "language model", "foundation model", "transformer", "generative model",
    "attention", "kv cache", "kvcache", "moe", "mixture-of-experts", "vllm",
    "sglang", "tensorrt-llm", "vision-language", "multimodal", "diffusion",
    "comic generation",
)


def _values(record: dict[str, Any], include_summary: bool = False) -> list[str]:
    values = [str(record.get("title", "")), str(record.get("venue_or_channel", ""))]
    if include_summary:
        values.append(str(record.get("summary", "")))
    tags = record.get("technical_tags", {})
    if isinstance(tags, dict):
        for tag_values in tags.values():
            values.extend(str(value) for value in (tag_values if isinstance(tag_values, list) else [tag_values]))
    return values


def _structured_text(record: dict[str, Any]) -> str:
    return " ".join(_values(record)).lower()


def _contains(text: str, terms: tuple[str, ...]) -> bool:
    return any(re.search(rf"(?<!\w){re.escape(term)}(?!\w)", text) for term in terms)


def _year(record: dict[str, Any]) -> int:
    match = re.search(r"20\d{2}", str(record.get("year", "")))
    return int(match.group(0)) if match else 0


def _record_date(record: dict[str, Any]) -> date:
    candidates = [
        record.get("evidence", {}).get("verified_at"),
        record.get("discovered"),
    ]
    for candidate in candidates:
        if not candidate:
            continue
        try:
            return datetime.fromisoformat(str(candidate).replace("Z", "+00:00")).date()
        except ValueError:
            pass
    year = _year(record)
    return date(year, 12, 31) if year else date.min


def _themes_for_text(text: str) -> list[str]:
    return [theme for theme in THEME_ORDER if _contains(text, THEME_TERMS[theme])]


def _themes(record: dict[str, Any]) -> list[str]:
    return _themes_for_text(_structured_text(record))


def _has_system_evidence(record: dict[str, Any]) -> bool:
    evidence = record.get("evidence", {})
    return bool(
        evidence.get("venue_status") in {"formal_conference", "industrial_material"}
        or evidence.get("source_type") == "project_or_engineering_material"
        or record.get("artifact_url")
        or record.get("triage", {}).get("physical_eval", {}).get("has_physical_signal")
    )


def _is_release(record: dict[str, Any]) -> bool:
    title = str(record.get("title", "")).lower().strip()
    url = str(record.get("primary_url", "")).lower()
    channel = str(record.get("venue_or_channel", "")).lower()
    return "/releases/" in url or " releases" in channel or bool(re.fullmatch(r"(?:release\s+)?v?\d[\w.\-]*", title))


def _github_project_key(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return ""
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return ""
    return f"github:{parts[0].lower()}/{parts[1].removesuffix('.git').lower()}"


def project_key_for_record(record: dict[str, Any]) -> str:
    for field in ("primary_url", "artifact_url"):
        key = _github_project_key(str(record.get(field, "")))
        if key:
            return key
    for source_id in record.get("source_ids", []):
        source = str(source_id).lower()
        if source.endswith("-releases"):
            return f"source:{source[:-len('-releases')]}"
    identity = record.get("canonical_id") or record.get("id") or record.get("title") or "unknown"
    return f"canonical:{identity}"


def classify_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return stable reading metadata without using free-form summaries as signals."""
    text = _structured_text(record)
    title_channel = " ".join(
        [str(record.get("title", "")), str(record.get("venue_or_channel", ""))]
    ).lower()
    direct_themes = _themes_for_text(title_channel)
    all_themes = _themes(record)
    themes = direct_themes + [theme for theme in all_themes if theme not in direct_themes]
    bindings = record.get("technical_tags", {}).get("framework_binding", [])
    if isinstance(bindings, str):
        bindings = [bindings]
    binding_text = " ".join(str(value) for value in bindings).lower()
    model_signal = _contains(f"{title_channel} {binding_text}", MODEL_TERMS)
    strong_binding = _contains(binding_text, ("vllm", "sglang", "tensorrt-llm", "kserve", "llm-d", "lmcache"))
    structured_core_signal = bool(themes) and strong_binding
    explicit_kernel = bool(themes) and _contains(
        text, ("flashattention", "pagedattention", "attention kernel", "wave compiler", "parallelkittens")
    )
    inherently_model_specific = any(
        theme in {"kv-cache", "prefill-decode-transfer", "speculative-decoding"}
        for theme in direct_themes
    )
    peripheral = _contains(text, PERIPHERAL_TERMS)
    evidence = _has_system_evidence(record)
    exploration = model_signal and _contains(text, EXPLORATION_TERMS) and evidence

    release_has_explicit_mechanism = any(
        _contains(title_channel, THEME_TERMS[theme]) for theme in themes
    )

    # 人工钉选：把明确策展的经典根节点固定进主线，不依赖关键词启发式。
    # 标记写在记录的 topics 里（topic "foundation-pinned"），便于后续增删。
    record_topics = [str(topic) for topic in (record.get("topics") or [])]
    pinned = FOUNDATION_PIN_TOPIC in record_topics
    archive_pinned = ARCHIVE_PIN_TOPIC in record_topics
    core_pinned = CORE_PIN_TOPIC in record_topics

    superseded_by = str(record.get("evidence", {}).get("superseded_by") or "").strip()
    presentation_meta = record.get("presentation", {})
    huawei_full_stack_adjacent = (
        isinstance(presentation_meta, dict)
        and presentation_meta.get("topic") == "huawei-ascend-ai-systems"
        and presentation_meta.get("topic_group") in HUAWEI_FULL_STACK_ADJACENT_GROUPS
    )

    if pinned:
        scope = "core"
        reasons = ["manually curated foundation root node (pinned in topics)"]
    elif archive_pinned:
        scope = "archive"
        reasons = ["manually archived pre-2026 non-foundation record (pinned in topics)"]
        themes = []
    elif core_pinned:
        scope = "core"
        reasons = ["manually curated core mainline record (pinned in topics)"]
    elif superseded_by:
        scope = "archive"
        reasons = [f"superseded by verified record {superseded_by}"]
        themes = []
    elif huawei_full_stack_adjacent:
        scope = "adjacent"
        reasons = ["explicit company-stack context outside the stable inference mainline"]
        themes = []
    elif themes and (direct_themes or structured_core_signal) and (
        model_signal or explicit_kernel or inherently_model_specific
    ) and not peripheral and (
        not _is_release(record) or release_has_explicit_mechanism
    ):
        scope = "core"
        reasons = ["matches a guide-defined inference execution theme"]
    elif exploration and not peripheral:
        scope = "adjacent"
        reasons = ["evidenced inference-system exploration outside the stable mainline"]
        themes = []
    else:
        scope = "archive"
        reasons = ["no direct guide theme or evidenced exploration signal"]
        themes = []

    foundation_text = title_channel
    formal = record.get("evidence", {}).get("venue_status") == "formal_conference"
    physical = bool(record.get("triage", {}).get("physical_eval", {}).get("has_physical_signal"))
    high_triage = record.get("triage", {}).get("priority") == "high"
    if pinned:
        priority = "foundation"
        reasons.append("kept as long-term foundation reading set")
    elif archive_pinned:
        priority = "supporting"
        reasons.append("excluded from the pre-2026 foundation mainline")
    elif scope == "core" and _contains(foundation_text, FOUNDATION_TERMS):
        priority = "foundation"
        reasons.append("foundational serving or kernel abstraction")
    elif scope == "core" and _year(record) >= 2025 and (
        high_triage or formal or record.get("artifact_url") or physical or str(record.get("source_tier", "")) == "A"
    ):
        priority = "frontier"
        reasons.append("recent mainline work with system or artifact evidence")
    else:
        priority = "supporting"
        reasons.append("supporting or exploratory evidence")

    result = {
        "version": CURATION_VERSION,
        "scope": scope,
        "priority": priority,
        "themes": themes,
        "reasons": reasons,
    }
    if record.get("record_type") in {"industry", "project"}:
        result["project_key"] = project_key_for_record(record)
    return result


def curation_for(record: dict[str, Any]) -> dict[str, Any]:
    value = record.get("curation")
    if isinstance(value, dict) and value.get("version") == CURATION_VERSION:
        return value
    return classify_record(record)


def curation_sort_key(record: dict[str, Any]) -> tuple[int, int, int, int, str]:
    curation = curation_for(record)
    scope_rank = {"core": 0, "adjacent": 1, "archive": 2}
    priority_rank = {"foundation": 0, "frontier": 1, "supporting": 2}
    evidence_rank = {
        "formal_conference": 0, "industrial_material": 1, "poster_or_workshop": 2,
        "preprint": 3, "unclassified": 4,
    }
    return (
        scope_rank.get(curation.get("scope"), 3),
        priority_rank.get(curation.get("priority"), 3),
        evidence_rank.get(record.get("evidence", {}).get("venue_status"), 4),
        -_year(record),
        str(record.get("title", "")),
    )


def select_exploration(
    records: list[dict[str, Any]], *, window_days: int = 180, limit: int = 20
) -> list[dict[str, Any]]:
    """Select a reproducible rolling set relative to the newest stored evidence date."""
    if not records or limit <= 0:
        return []
    as_of = max((_record_date(record) for record in records), default=date.min)
    threshold = date.min if as_of == date.min else as_of - timedelta(days=max(window_days, 0))
    eligible = [
        record for record in records
        if curation_for(record).get("scope") == "adjacent" and _record_date(record) >= threshold
    ]
    eligible.sort(key=lambda record: (-_record_date(record).toordinal(), str(record.get("title", ""))))
    return eligible[:limit]


def is_public_mainline(record: dict[str, Any]) -> bool:
    return curation_for(record).get("scope") == "core"
