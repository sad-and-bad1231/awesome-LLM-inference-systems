# Anyscale / Ray Serve

A cloud operator and major contributor to the open **Ray Serve** ecosystem. The inference value is **multi-replica control-plane and engine orchestration**, rather than inventing vLLM/SGLang kernel implementations.

[← Organizations](README.md)

## First-party and community code

| Artifact | Executed mechanism | Attribution and limits |
|---|---|---|
| [Ray Serve LLM](https://github.com/ray-project/ray/blob/master/doc/source/serve/llm/index.md) | Multi-node/multi-model serving, autoscaling, load balancing, TP/PP/EP, P/D disaggregation, prefix-aware routing, multi-LoRA serving and engine-agnostic vLLM/SGLang adapters. | **Ray open-source project**, not wholly Anyscale-owned code; supports distributed serving above engines. Backend version and compatibility must be pinned. |
| [Anyscale AI Infra Cookbook](https://github.com/anyscale/ai-infra-cookbook) | Runnable online-service examples: multi-node SGLang TP×PP, vLLM wide-EP gang restart, model-load acceleration and multiple deployment patterns. | Example recipes and author benchmarks, not published claims of universal fleet performance. |
| [Ray Serve LLM benchmarks](https://github.com/ray-project/ray/blob/master/doc/source/serve/llm/benchmarks.md) | Differentiates orchestration overhead, router policy, replica startup and real TTFT/TPOT measurements. | Benchmark snapshots vary by software/hardware; do not compare deployment patterns without equal SLO and load. |

## Inspectable execution architecture (Ray Serve LLM)

The [Ray Serve LLM architecture](https://docs.ray.io/en/latest/serve/llm/architecture/overview.html) separates **OpenAI ingress / model routing**, **replica routing**, and an **LLMServer** deployment running an engine such as vLLM or SGLang. A Ray Serve deployment/replica is a cluster control-plane unit; an engine's token scheduler, KV block manager and CUDA/NPU kernels remain separate responsibilities.

| Execution boundary | Source and specific decision to learn | Evidence caution |
|---|---|---|
| [Request routing](https://docs.ray.io/en/latest/serve/llm/architecture/routing-policies.html) | Distinguish `model_id`→deployment from per-deployment replica selection; default Power-of-Two Choices versus prefix-aware KV locality and queue/load constraints | Prefix affinity does not prove reused KV hits; version and engine/backend affect available policies |
| [P/D disaggregation](https://docs.ray.io/en/latest/serve/llm/architecture/serving-patterns/prefill-decode.html) | Separate Prefill/Decode engine replicas and lifecycle, independent scaling and KV handoff | Transfer overhead, load mix, connector and engine versions determine gains |
| [Data-parallel attention](https://docs.ray.io/en/latest/serve/llm/architecture/serving-patterns/data-parallel.html) | Coordinate Attention replicas with expert-parallel execution; rank synchronization is not the same as independent stateless replicas | Compare GPU/NPU topology, EP communication and synchronized Rank stalls |
| [Engine interfaces](https://docs.ray.io/en/latest/serve/llm/architecture/overview.html) | `LLMEngine` protocol and deployment builders decouple topology/routing from underlying inference engine | Framework interface alone does not guarantee feature parity across vLLM/SGLang |

**Suggested read:** trace ingress → replica router → `LLMServer` → engine scheduler → KV/Prefill/Decode events, then profile TTFT/TPOT/Goodput alongside request-route cache hit rate, queue depth, replica scaling and transfer time at fixed model/precision and version.

## Engineering focus

The reusable problem is **composing proven model engines into resilient services**: routing, cache affinity, admission, resource packing, scale-out and failure recovery. A GPU kernel speedup does not establish multi-tenant SLO or goodput at the Ray routing layer.

**Status:** runnable open source and vendor-maintained examples; performance not independently reproduced in this bibliography.
