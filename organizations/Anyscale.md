# Anyscale / Ray Serve

A cloud operator and major contributor to the open **Ray Serve** ecosystem. The inference value is **multi-replica control-plane and engine orchestration**, rather than inventing vLLM/SGLang kernel implementations.

[← Organizations](README.md)

## First-party and community code

| Artifact | Executed mechanism | Attribution and limits |
|---|---|---|
| [Ray Serve LLM](https://github.com/ray-project/ray/blob/master/doc/source/serve/llm/index.md) | Multi-node/multi-model serving, autoscaling, load balancing, TP/PP/EP, P/D disaggregation, prefix-aware routing, multi-LoRA serving and engine-agnostic vLLM/SGLang adapters. | **Ray open-source project**, not wholly Anyscale-owned code; supports distributed serving above engines. Backend version and compatibility must be pinned. |
| [Anyscale AI Infra Cookbook](https://github.com/anyscale/ai-infra-cookbook) | Runnable online-service examples: multi-node SGLang TP×PP, vLLM wide-EP gang restart, model-load acceleration and multiple deployment patterns. | Example recipes and author benchmarks, not published claims of universal fleet performance. |
| [Ray Serve LLM benchmarks](https://github.com/ray-project/ray/blob/master/doc/source/serve/llm/benchmarks.md) | Differentiates orchestration overhead, router policy, replica startup and real TTFT/TPOT measurements. | Benchmark snapshots vary by software/hardware; do not compare deployment patterns without equal SLO and load. |

## Engineering focus

The reusable problem is **composing proven model engines into resilient services**: routing, cache affinity, admission, resource packing, scale-out and failure recovery. A GPU kernel speedup does not establish multi-tenant SLO or goodput at the Ray routing layer.

**Status:** runnable open source and vendor-maintained examples; performance not independently reproduced in this bibliography.
