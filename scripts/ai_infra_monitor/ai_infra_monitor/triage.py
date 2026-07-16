from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from .models import Candidate


PHYSICAL_TERMS = (
    "kernel",
    "triton",
    "cuda",
    "hip",
    "rocm",
    "gpu",
    "npu",
    "tpu",
    "hopper",
    "blackwell",
    "mi300",
    "mi350",
    "rdma",
    "cxl",
    "vllm",
    "sglang",
    "tensorrt-llm",
    "kubernetes",
    "docker",
)

ALGORITHMIC_ONLY_TERMS = (
    "simulation",
    "simulated",
    "synthesized dataset",
    "synthetic dataset",
    "mathematical proof",
    "theorem",
    "convergence proof",
)

FRAMEWORK_BINDINGS = (
    "vllm",
    "sglang",
    "tensorrt-llm",
    "tensorRT-LLM".lower(),
    "kserve",
    "llm-d",
    "lmcache",
    "kubernetes",
    "docker",
)

CORE_SERVING_TOPICS = {
    "runtime-serving",
    "state-kv",
    "compression-cost",
    "kernel-compiler",
    "network-disaggregation",
    "moe",
    "reliability-evaluation",
}
PERIPHERAL_TERMS = (
    "training communication",
    "vector database",
    "trusted execution",
    "fully homomorphic",
    "pim",
    "wafer-scale",
    "quantum error correction",
    "quantum decoder",
    "membership inference",
    "side-channel",
    "timing attack",
    "security attack",
)
SERVING_TERMS = (
    "llm serving",
    "llms serving",
    "llm inference",
    "llms inference",
    "inference serving",
    "prefill",
    "speculative decoding",
    "decode stage",
    "token decoding",
    "kv cache",
    "vllm",
    "sglang",
    "tensorrt-llm",
)
SYSTEM_OPERATION_TERMS = (
    "serving",
    "llm inference",
    "llms inference",
    "model inference",
    "foundation model inference",
    "large model inference",
    "distributed inference",
    "moe inference",
    "expert offloading",
    "inference on",
    "rag system",
    "rag serving",
    "retrieval-augmented generation system",
    "inference optimization",
    "inference optimizations",
    "efficient inference",
    "inference engine",
    "inference system",
    "prefill",
    "kv cache",
    "kvcache",
    "lora",
    "prefix cache",
    "context cache",
    "speculative decoding",
    "memory-efficient decoding",
    "decoding optimization",
    "runtime",
    "rag system",
    "retrieval-augmented generation system",
)
MODEL_SYSTEM_TERMS = (
    "llm",
    "llms",
    "mllm",
    "large language model",
    "large language models",
    "foundation model",
    "foundation models",
    "large model",
    "large models",
    "language model",
    "language models",
    "vision-language model",
    "vision-language models",
    "transformer",
    "moe",
    "mixture-of-experts",
    "mixture of experts",
    "attention",
    "rag",
    "retrieval-augmented generation",
    "kv cache",
    "kvcache",
)
DIRECT_SYSTEM_TITLE_TERMS = (
    "serving",
    "inference",
    "prefill",
    "speculative decoding",
    "decode stage",
    "token decoding",
    "kv cache",
    "kvcache",
    "prefix cache",
    "context cache",
    "scheduler",
    "scheduling",
    "disaggregated",
    "rdma",
    "nixl",
    "all-to-all",
    "expert parallel",
    "kernel",
    "triton",
    "cuda",
    "rocm",
    "gpu",
    "runtime",
    "rag system",
    "retrieval-augmented generation system",
)

REPO_STRUCTURE_TERMS = (
    "csrc",
    "kernel",
    "kernels",
    "setup.py",
    "pyproject.toml",
    "triton",
    "cuda",
    "hip",
    "c++",
    "cpp",
)

SYSTEM_LANGUAGES = {"C++", "C", "Cuda", "CMake", "Roff", "Objective-C", "Rust"}
ROOT_SIGNAL_PATHS = {"csrc", "kernel", "kernels", "setup.py", "pyproject.toml"}


@dataclass(frozen=True)
class TriageResult:
    verdict: str = "keep"
    priority: str = "normal"
    reasons: tuple[str, ...] = field(default_factory=tuple)
    repo_signals: dict[str, object] = field(default_factory=dict)
    physical_eval: dict[str, object] = field(default_factory=dict)
    llm_review: dict[str, object] = field(
        default_factory=lambda: {
            "status": "not_configured",
            "prompt_template": (
                "You are a strict AI infrastructure expert. Answer only: "
                "hardware, baseline, physical goodput/latency improvement, "
                "or REJECT if the text is only theoretical."
            ),
        }
    )

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data["reasons"] = list(self.reasons)
        return data


def _contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(
        re.search(rf"(?<!\w){re.escape(term.lower())}(?!\w)", text) is not None
        for term in terms
    )


def _github_repo_from_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.lower() != "github.com":
        return ""
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return ""
    return "/".join(parts[:2])


def _github_json(url: str, timeout_seconds: int) -> object:
    request = Request(url, headers={"User-Agent": "ai-infra-monitor/1.0"})
    with urlopen(request, timeout=timeout_seconds) as response:
        return json.loads(response.read().decode("utf-8"))


def inspect_github_repository(repo: str, timeout_seconds: int = 6) -> dict[str, object]:
    signals: dict[str, object] = {"repository": repo}
    try:
        languages = _github_json(
            f"https://api.github.com/repos/{repo}/languages", timeout_seconds
        )
        contents = _github_json(
            f"https://api.github.com/repos/{repo}/contents", timeout_seconds
        )
    except (OSError, HTTPError, URLError, TimeoutError, json.JSONDecodeError) as error:
        signals["unavailable"] = f"{type(error).__name__}: {error}"
        return signals
    if isinstance(languages, dict):
        signals["languages"] = languages
        signals["has_system_language"] = any(
            language in SYSTEM_LANGUAGES or language.lower() in {"cuda", "triton"}
            for language, bytes_count in languages.items()
            if int(bytes_count or 0) > 0
        )
    if isinstance(contents, list):
        names = {str(item.get("name", "")).lower() for item in contents if isinstance(item, dict)}
        signals["root_paths"] = sorted(names & ROOT_SIGNAL_PATHS)
        signals["has_build_or_kernel_path"] = bool(names & ROOT_SIGNAL_PATHS)
    return signals


def triage_candidate(
    candidate: Candidate,
    inspect_repo: bool = False,
    repo_timeout_seconds: int = 6,
    core_only: bool = False,
) -> TriageResult:
    evidence_text = " ".join(
        (
            candidate.title,
            candidate.summary,
            candidate.source_name,
            candidate.url,
        )
    ).lower()
    topic_text = " ".join(candidate.topics).lower()
    text = f"{evidence_text} {topic_text}".strip()
    reasons: list[str] = []
    priority = "normal"
    verdict = "keep"

    has_physical_signal = _contains_any(evidence_text, PHYSICAL_TERMS)
    algorithmic_only = _contains_any(evidence_text, ALGORITHMIC_ONLY_TERMS) and not has_physical_signal
    bindings = [term for term in FRAMEWORK_BINDINGS if _contains_any(evidence_text, (term,))]
    if algorithmic_only:
        verdict = "downrank"
        priority = "low"
        reasons.append("algorithmic-only text without hardware/runtime/kernel signal")

    if core_only:
        has_serving_signal = _contains_any(evidence_text, SERVING_TERMS)
        model_system_signal = _contains_any(evidence_text, MODEL_SYSTEM_TERMS)
        model_serving_signal = _contains_any(
            evidence_text,
            (
                "llm",
                "llms",
                "mllm",
                "large language model",
                "large language models",
                "foundation model",
                "foundation models",
                "large model",
                "large models",
                "language model",
                "language models",
                "transformer",
                "mixture-of-experts",
                "mixture of experts",
                "moe",
                "rag",
                "retrieval-augmented generation",
                "kv cache",
                "kvcache",
                "lora",
            ),
        )
        core_topics = set(candidate.topics) & CORE_SERVING_TOPICS
        strong_core_topics = core_topics - {"kernel-compiler", "reliability-evaluation"}
        has_core_topic = bool(
            strong_core_topics
            and model_serving_signal
            and _contains_any(
                evidence_text,
                SYSTEM_OPERATION_TERMS,
            )
        )
        kernel_system_signal = (
            "kernel-compiler" in core_topics
            and model_serving_signal
            and _contains_any(
                evidence_text,
                SYSTEM_OPERATION_TERMS,
            )
            and _contains_any(evidence_text, ("cuda", "triton", "rocm", "gpu", "kernel", "compiler"))
        )
        training_only = "training" in evidence_text and not has_serving_signal
        title_system_signal = _contains_any(
            candidate.title.lower(), DIRECT_SYSTEM_TITLE_TERMS
        )
        peripheral_only = _contains_any(evidence_text, PERIPHERAL_TERMS) and (
            not has_serving_signal or not model_system_signal
        )
        if (
            peripheral_only
            or training_only
            or (not title_system_signal and not bindings)
            or (not has_core_topic and not kernel_system_signal and not has_serving_signal)
        ):
            priority = "low"
            if verdict == "keep":
                verdict = "downrank"
            reasons.append("outside serving mainline without direct inference-serving signal")

    if bindings:
        priority = "high"
        verdict = "keep"
        reasons.append("ecosystem binding: " + ", ".join(sorted(set(bindings))))

    repo = _github_repo_from_url(candidate.url)
    repo_signals: dict[str, object] = {}
    if repo:
        repo_signals["repository"] = repo
        repo_signals["structure_hints"] = [
            term for term in REPO_STRUCTURE_TERMS if re.search(rf"(^|[/\s_-]){re.escape(term)}($|[/\s_-])", text)
        ]
        if inspect_repo:
            repo_signals.update(inspect_github_repository(repo, repo_timeout_seconds))
            if repo_signals.get("has_system_language"):
                priority = "high"
                reasons.append("GitHub languages include systems implementation")
            if repo_signals.get("has_build_or_kernel_path"):
                priority = "high"
                reasons.append("GitHub root contains build/kernel path")
            if repo_signals.get("unavailable"):
                reasons.append("GitHub repository metadata unavailable")
        if repo_signals["structure_hints"]:
            priority = "high"
            reasons.append("repository structure suggests systems implementation")
        else:
            repo_signals["structure_hints"] = []

    physical_eval = {
        "has_physical_signal": has_physical_signal,
        "has_framework_binding": bool(bindings),
    }
    if not reasons:
        reasons.append("matched configured AI infra topic")
    return TriageResult(
        verdict=verdict,
        priority=priority,
        reasons=tuple(dict.fromkeys(reasons)),
        repo_signals=repo_signals,
        physical_eval=physical_eval,
    )


def triage_candidates(
    candidates: list[Candidate],
    inspect_repo: bool = False,
    repo_timeout_seconds: int = 6,
    core_only: bool = False,
    max_workers: int = 1,
) -> list[TriageResult]:
    """Triage candidates concurrently while preserving input order."""
    if len(candidates) <= 1 or max_workers <= 1:
        return [
            triage_candidate(
                candidate,
                inspect_repo=inspect_repo,
                repo_timeout_seconds=repo_timeout_seconds,
                core_only=core_only,
            )
            for candidate in candidates
        ]

    with ThreadPoolExecutor(max_workers=min(max_workers, len(candidates))) as pool:
        futures = [
            pool.submit(
                triage_candidate,
                candidate,
                inspect_repo=inspect_repo,
                repo_timeout_seconds=repo_timeout_seconds,
                core_only=core_only,
            )
            for candidate in candidates
        ]
        return [future.result() for future in futures]
