# Asari AI

A narrowly scoped research signal: **agent-led optimization of a complete, existing inference stack**, rather than a hosted-model catalog or a generic AI coding announcement.

[← Organizations](README.md) · [← Frontiers](../frontiers/README.md)

## Public inference work

| Source | Mechanism | Evidence and limits |
|---|---|---|
| **[Speeding up end-to-end inference with self-improving agents](https://asari.ai/blog/inference-optimization)** (2026-07-28) | Multiple agents diagnose and change vLLM kernels, scheduling, load balancing and configuration; profiling + hierarchical micro/E2E evaluations + token-distribution checks; experiment lessons transfer between model optimization tasks. | Author reports **up to 16%** gains across selected concurrency settings for **DeepSeek V4 Pro / GLM 5.2**, **8×B200**, **vLLM 0.23**. These are first-party findings, **not independently reproduced**, and should not be compared directly to SEIS mini-SGLang or Together Compiler results. |
| **Experiment memory and verification** | Stores reusable optimization insights, including avoidance of distributed deadlock and improved experimental workflows; matches token-probability distributions on a prompt corpus. | A few documented transfer examples are evidence of **workflow adaptation**, not a controlled demonstration of open-ended recursive improvements to the underlying foundation model. |

## Research questions

The interesting systems boundary is whether hardware/trace evidence **causally improves** agent search quality relative to a generic coding agent, and whether learning persists on unseen models, traffic shapes and hardware **under equal compute budgets**. Correctness should cover output behavior, distributional drift, adverse concurrency cases and hidden workloads. A single isolated speedup or agent-memory demonstration is not self-sustaining RSI.

**Status:** a first-party engineering/research blog with reported real-GPU experiments, not a released general-purpose framework or peer-reviewed publication. Its vLLM 0.23 experiments cannot be automatically projected onto other engine versions or Ascend.
