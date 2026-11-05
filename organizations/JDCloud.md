# JD.com / JD Cloud

JD.com operates a model-service platform **and publishes an inspectable clustered inference serving layer**. The engineering record is stronger than the former service-only description; neither the open code nor JoyMaaS APIs alone establish the configuration of every JD production deployment.

[← Organizations](README.md)

## First-party service evidence

| Source | Executed or externally visible contract | What cannot be concluded |
|---|---|---|
| **[xLLM Service](https://github.com/xLLM-AI/xllm-service)** · [JD source namespace](https://github.com/jd-opensource/xllm-service) | Open C++ service layer built around the xLLM engine: multi-replica deployment, separate service/controller vs engine execution, error detection, re-dispatch/recovery and resource orchestration. | Public repository credits **JD.com**; inspect branch and submodules before concluding a specific vLLM-style scheduler, commercial usage, throughput or Ascend model parity. |
| [JoyMaaS](https://joymaas.jdcloud.com/) · [model registry](https://joymaas.jdcloud.com/models) | Enterprise model-service gateway with a normalized API, authentication, rate limiting, routing, load balancing, fallback and usage/cost controls; serves JD-built models alongside third-party models. | A **published service/API surface**. Request-routing policy, internal P/D topology, kernel code and measured fleet utilization are **not publicly disclosed here**. |
| [JD JoyAI-VL-Interaction / LiveTTS](https://joymaas.jdcloud.com/models) | First-party multimodal interaction and streaming speech endpoints illustrate different execution and latency contracts in the same model gateway. | Endpoint inventory is not evidence of shared model architecture or internally optimized decode kernels. |
| [JD Cloud platform](https://www.jdcloud.com/) | Heterogeneous compute, GPU and enterprise model deployment product family; relevant infrastructure discovery source. | Broad vendor capability claims are not a benchmark or inspectable inference-engine mechanism. |

## Research reading angle

**MaaS at enterprise scale** brings service-level questions: dynamic provider/model routing, isolation, token-based usage and billing, fallback/error semantics, concurrency SLO, security and heterogeneous deployment. The **xLLM Service source now provides real controller/service implementation evidence**. However, an end-to-end speedup claim still needs commit-pinned engine+service configurations, a correctness oracle, workload traces and strong benchmark baselines.

**Status:** first-party **[OPEN CODE + SERVICE-CONTRACT]**; JD company attribution is stated by the xLLM Service repository, but submodule ownership and production adoption still require separate evidence. Do not claim private scheduling implementation from marketing text or recruitment descriptions.
