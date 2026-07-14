from __future__ import annotations

import re
import json
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
)
SERVING_TERMS = (
    "llm serving",
    "llm inference",
    "inference serving",
    "prefill",
    "decode",
    "kv cache",
    "vllm",
    "sglang",
    "tensorrt-llm",
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
    return any(term.lower() in text for term in terms)


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
    text = " ".join(
        (
            candidate.title,
            candidate.summary,
            " ".join(candidate.topics),
            candidate.source_name,
            candidate.url,
        )
    ).lower()
    reasons: list[str] = []
    priority = "normal"
    verdict = "keep"

    has_physical_signal = _contains_any(text, PHYSICAL_TERMS)
    algorithmic_only = _contains_any(text, ALGORITHMIC_ONLY_TERMS) and not has_physical_signal
    if algorithmic_only:
        verdict = "downrank"
        priority = "low"
        reasons.append("algorithmic-only text without hardware/runtime/kernel signal")

    if core_only:
        has_core_topic = bool(set(candidate.topics) & CORE_SERVING_TOPICS)
        has_serving_signal = _contains_any(text, SERVING_TERMS)
        peripheral_only = _contains_any(text, PERIPHERAL_TERMS) and not has_serving_signal
        if peripheral_only or (not has_core_topic and not has_serving_signal):
            priority = "low"
            if verdict == "keep":
                verdict = "downrank"
            reasons.append("outside serving mainline without direct inference-serving signal")

    bindings = [term for term in FRAMEWORK_BINDINGS if term in text]
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
