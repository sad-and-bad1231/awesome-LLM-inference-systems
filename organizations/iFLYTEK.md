# iFLYTEK / Spark

First-party **domestic heterogeneous inference infrastructure and edge/cloud model deployment** signals. This page separates publicly documented model/runtime compatibility from claims about an undisclosed proprietary optimization.

[← Organizations](README.md)

## Verified execution-facing sources

| Source | Relevance | Boundary |
|---|---|---|
| [Spark AI computing platform (AICC)](https://spark-aicc.iflytek.com/aicc-portal/) | Provides online/batch model deployment, managed heterogeneous accelerator resources (Ascend, Cambricon, Hygon, NVIDIA in vendor docs) and a model-inference service layer. | **Product/platform architecture**, not published kernel schedule, benchmark harness or actual equal-budget end-to-end comparisons. |
| [iFLYTEK Open Source](https://github.com/iFLYTEK) · [Astron projects](https://opensource.iflytek.com/) | Public enterprise agent/workflow ecosystem and operating-platform integration. | **Agent application infrastructure** and orchestration should not be called token-level inference-engine optimization. |
| [Spark X2.6 portal](https://www.xfyun.cn/) (Nov 2026 catalog) | First-party model offering and domestic hardware execution demands; streaming audio/long context and on-device lines are distinct workloads. | Model family claims are **not** proof of new open-serving kernel or deployed serving throughput on a specified GPU/NPU. |
| [Earlier serving-service projects](https://iflytek.github.io/) | Historical published inference-service framework and MLOps infrastructure overview. | Historic source may be **general AI serving**, not specifically modern vLLM-compatible autoregressive decode. |

## Research reading angle

Useful for **heterogeneous resource management**, API model serving, cloud–edge execution and multimodal real-time workloads. Claims about proprietary kernel performance or cross-chip portability require version-pinned public artifacts and workload details before promotion.

**Status:** first-party platform/service disclosures; limited publicly inspectable modern inference-engine internals.
