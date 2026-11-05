# Fireworks AI

A production-oriented inference infrastructure provider with **first-party disclosures of a disaggregated execution stack**. Hosting other teams' foundation models does not establish ownership of those model architectures.

[← Organizations](README.md)

## Publicly described inference architecture

| First-party source | Executed systems concept | Evidence boundary |
|---|---|---|
| **[Disaggregated Inference Engine](https://fireworks.ai/platform/disaggregated-inference-engine)** | Separate prefill/decode capacity, disaggregated KV cache, prompt-aware routing, multi-node expert parallelism, custom precision and kernel optimizations. | Official **product architecture description**, without complete published source/experiment harness; advertised speedups are not independently verified or portable across models. |
| **[Fireworks inference](https://fireworks.ai/inference)** | End-to-end engine co-design spanning memory layout, model-specific kernels, speculative decoding, long-context cache/routing and serving modes. | Do not infer that every advertised feature runs identically for every listed hosted model. |
| **[Sovereign inference](https://fireworks.ai/product/sovereign)** | Describes FireOptimizer configuration selection, pinned CUDA/NCCL/kernel rollout, canary verification and rollback under managed deployments. | Vendor-disclosed operating practices; an **84,000-configuration search space** is not a published autonomous-RSI algorithm or independently observed optimization gain. |

## Engineering question

How should model-specific kernel/precision choices, cache placement and distributed scheduling be **jointly optimized** under traffic shifts while guaranteeing latency and semantic quality? This is a **whole-inference-stack** problem; distinguish documented product behavior from published execution traces, source code or peer-reviewed systems results.

**Status:** company first-party docs, limited public implementation details; no local reproduction. Models by DeepSeek, Qwen, Meta and others remain attributed to their creators.
