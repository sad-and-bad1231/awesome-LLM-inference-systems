"""Deterministic reading-scope and editorial-priority classification.

This layer is intentionally separate from triage. Triage decides whether a
discovery should enter the processing queue; curation decides where a human
should spend reading attention.
"""

from __future__ import annotations

import re
from typing import Any


CURATION_VERSION = "guide-2026-v5"
SCOPES = ("core", "adjacent", "archive")
PRIORITIES = ("foundation", "frontier", "supporting")

MAINLINE_TERMS = (
    "attention",
    "kv cache",
    "kvcache",
    "prefill",
    "decode",
    "speculative decoding",
    "draft verify",
    "moe",
    "mixture-of-experts",
    "expert routing",
    "expert parallel",
    "kernel",
    "triton",
    "cuda",
    "rocm",
    "wave compiler",
    "dsl",
    "compiler",
    "llm serving",
    "llm inference",
    "serving",
    "inference",
    "inference engine",
    "inference runtime",
    "vllm",
    "sglang",
    "tensorrt-llm",
    "continuous batching",
    "scheduler",
    "scheduling",
    "disaggregated serving",
    "kv transfer",
)

FOUNDATION_TERMS = (
    "orca",
    "pagedattention",
    "flashattention:",
    "flashattention-1",
    "flashattention-2",
    "flashattention-3",
    "flexgen",
    "distserve",
    "sarathi",
    "splitwise",
    "continuous batching",
    "deepspeed-fastgen",
    "sarathi-serve",
    "llumnix",
    "p/d-serve",
    "deepspeed inference",
    "s-lora",
    "sglang",
    "memserve:",
    "hydragen:",
    "medusa:",
    "prompt cache:",
    "flashinfer",
    "vllm v1",
    "torch.compile",
    "flexattention",
    "tutel",
    "deepspeed-moe",
    "megablocks:",
)

PERIPHERAL_TERMS = (
    "training communication",
    "training-only",
    "vector database",
    "trusted execution",
    "fully homomorphic",
    "membership inference",
    "side-channel",
    "timing attack",
    "security attack",
    "privacy-preserving",
    "point cloud",
    "3d gaussian",
    "image classification",
    "object detection",
    "generic database",
)


def _text(record: dict[str, Any]) -> str:
    values = [
        str(record.get("title", "")),
        str(record.get("summary", "")),
        str(record.get("venue_or_channel", "")),
    ]
    tags = record.get("technical_tags", {})
    if isinstance(tags, dict):
        values.extend(
            str(value)
            for values_for_tag in tags.values()
            for value in (values_for_tag if isinstance(values_for_tag, list) else [values_for_tag])
        )
    return " ".join(values).lower()


def _contains(text: str, terms: tuple[str, ...]) -> bool:
    return any(re.search(rf"(?<!\w){re.escape(term)}(?!\w)", text) for term in terms)


def _year(record: dict[str, Any]) -> int:
    match = re.search(r"20\d{2}", str(record.get("year", "")))
    return int(match.group(0)) if match else 0


def classify_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return a stable, explainable reading scope and priority for a record."""
    text = _text(record)
    tags = record.get("technical_tags", {})
    structured_text = " ".join(
        [
            str(record.get("title", "")),
            str(record.get("venue_or_channel", "")),
            " ".join(
                str(value)
                for values_for_tag in tags.values()
                for value in (values_for_tag if isinstance(values_for_tag, list) else [values_for_tag])
            ),
        ]
    ).lower()
    model_signal = _contains(
        text,
        (
            "llm",
            "language model",
            "transformer",
            "generative model",
            "attention",
            "kv cache",
            "moe",
            "mixture-of-experts",
            "vllm",
            "sglang",
            "tensorrt-llm",
        ),
    )
    explicit_guide_kernel = _contains(
        structured_text,
        ("flashattention", "pagedattention", "parallelkittens", "wave compiler", "attention kernel"),
    )
    mainline = _contains(structured_text, MAINLINE_TERMS) and (model_signal or explicit_guide_kernel)
    peripheral = _contains(text, PERIPHERAL_TERMS)
    physical = bool(record.get("triage", {}).get("physical_eval", {}).get("has_physical_signal"))
    has_artifact = bool(record.get("artifact_url"))
    formal = record.get("evidence", {}).get("venue_status") == "formal_conference"
    high_triage = record.get("triage", {}).get("priority") == "high"
    source_tier = str(record.get("source_tier", ""))

    if not mainline:
        scope = "archive"
        reasons = ["no guide-defined kernel or LLM serving mainline signal"]
    elif peripheral and not any(
        term in text for term in ("llm inference", "llm serving", "kv cache", "inference kernel", "serving runtime")
    ):
        scope = "adjacent"
        reasons = ["related infrastructure is not directly on the serving execution path"]
    else:
        scope = "core"
        reasons = ["matches guide-defined kernel/serving mainline"]

    foundation_text = " ".join(
        [str(record.get("title", "")), str(record.get("venue_or_channel", ""))]
    ).lower()
    if _contains(foundation_text, FOUNDATION_TERMS):
        priority = "foundation"
        reasons.append("foundational serving or kernel abstraction")
    elif (
        scope == "core"
        and _year(record) >= 2025
        and (high_triage or formal or has_artifact or physical or source_tier == "A")
    ):
        priority = "frontier"
        reasons.append("recent mainline work with system or artifact evidence")
    else:
        priority = "supporting"
        reasons.append("useful supporting evidence or incomplete system evidence")

    return {
        "version": CURATION_VERSION,
        "scope": scope,
        "priority": priority,
        "reasons": reasons,
    }


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
        scope_rank.get(curation.get("scope"), 3),
        priority_rank.get(curation.get("priority"), 3),
        evidence_rank.get(record.get("evidence", {}).get("venue_status"), 4),
        year,
        str(record.get("title", "")),
    )


def is_public_mainline(record: dict[str, Any]) -> bool:
    return curation_for(record).get("scope") == "core"
