# Predibase

A first-party example of **many-adapter inference**—a different serving problem from simply running one large model quickly. The public mechanism is in **LoRAX**.

[← Organizations](README.md)

## Public runtime

| Artifact | Mechanism | Boundary |
|---|---|---|
| [LoRAX — LoRA eXchange](https://github.com/predibase/lorax) | Dynamic adapter loading, GPU↔CPU adapter prefetch/eviction, **heterogeneous continuous batching** for requests targeting different adapters, shared base weights, TP, paged attention and streaming. | Open-source server **forked from Hugging Face TGI**, using concepts/kernels from the wider community including Punica; not wholly original lower-level GPU kernels. |
| [Deployment and observability](https://github.com/predibase/lorax) | Prometheus/OpenTelemetry and Kubernetes packaging, per-request adapter selection and multi-tenant serving. | Repository features and published marketing figures are not independently validated across thousands of simultaneous active adapters. |

## Research reading angle

The systems problem is **adapter residency and batching interference**: which adapters stay in GPU memory; what to prefetch; whether mixed batches retain kernel efficiency; and how tenant/model-isolation affects request fairness. Evaluate cache miss, adapter-load time, TTFT/TPOT tail, throughput at fixed model/adapter count and batch/concurrency.

**Status:** directly inspectable inference runtime. No invented 2026 model generation or exclusive ownership of third-party kernels.
