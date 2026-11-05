# Groq

First-party **LPU-based, compiler-scheduled inference hardware** and its deployment stack; relevant as a distinct architectural path from GPU-centric vLLM/SGLang backends.

[← Organizations](README.md)

## Public hardware and execution concepts

| Source | Inference systems relevance | Evidence boundary |
|---|---|---|
| **[Groq LPU overview](https://groq.com/blog/the-groq-lpu-explained)** (2025) | On-chip SRAM emphasis, deterministic/static compiler-coordinated execution and synchronized multi-chip dataflow for low-latency autoregressive serving. | First-party **architecture explanation**, not an independently reproduced GPU-vs-LPU energy, throughput or cost comparison. |
| **[Groq platform](https://groq.com/platform)** | Cloud/dedicated infrastructure and inference service layers; publishes rack-scale LPU capacity and deployment offerings. | **Current products vs future platform roadmap** must be separated. Vendor headline token rates and power claims are configuration-dependent, not general SLO-correct serving results. |

## Systems comparison boundary

Groq's explicitly scheduled memory/communication architecture changes the cost model for **memory residency, pipeline partitioning and token latency**. It should be compared with GPUs/TPUs/Cerebras under matched checkpoint, precision, context, concurrency, hardware count, quality constraints and cost. Do not infer its internal scheduler/runtime implementation from the API interface.

**Status:** vendor hardware/product documentation, not new canonical inference papers. No local measurements claimed.
