# Meituan / LongCat

**Model–system co-design with an inspectable inference-engine artifact**, not just a model/API vendor. LongCat is a Meituan-developed family; SGLang remains community-owned.

[← Organizations](README.md) · [← Frontiers](../frontiers/README.md)

## First-party engineering evidence

| Artifact / publication | Reusable inference mechanism | What the evidence does **not** establish |
|---|---|---|
| [SGLang-FluentLLM](https://github.com/meituan-longcat/SGLang-FluentLLM) (open code) | Meituan's SGLang-derived engine customizations: fused target/verify/draft CUDA graph, overlap-aware speculative decoding (Eagle/MTP/PLD), layer-wise KV transfer and Decode Radix Tree Cache to reduce P/D traffic. | Fork-specific implementation, **not** automatically merged upstream; GPU CUDA graph path cannot be assumed to run on Ascend. |
| [LongCat-2.0 inference code and deployment](https://tech.meituan.com/2026/07/12/LongCat-2.0-Open-source.html) (2026-07-12) | LSA sparse attention with index reuse, MLA indexer/prolog overlap, KVP-partitioned cache, Super Kernel, weight prefetch, P/D disaggregation and asynchronous EP load balancing on domestic accelerators. | Engineering report + released model/inference artifacts. Vendor performance claims are not independent replication or proof of one universal hardware configuration. |
| [LongCat-2.5](https://tech.meituan.com/2026/11/02/Meituan-LongCat-2.5.html) (2026-11-02) | Reports W4A4 MoE inference with INT4 matrix multiplication, pre-dispatch quantization, compute/communication overlap, and training–prefill–decode numerical consistency for long-context rollout. | The **86% single-card SFT improvement** described in the report is *training* throughput, not online serving speedup; W4A4 equivalence requires per-task quality checks. |
| [LongCat-2.0 model release](https://tech.meituan.com/2026/06/30/LongCat2.0.html) | 1.6T-total sparse MoE with dynamically varying active parameters; 1M-context and long-agent requests create challenging variable-workload serving demand. | Model capability and published scale figures must not be conflated with achieved SLO-correct Goodput. |

## What to learn

- **Across kernel/runtime:** multi-step speculation + graph capture, communication overlap, KV cache representation and sparse-indexer lifetime.
- **Across accelerator/runtime:** P/D and EP mapping on domestic hardware, constrained memory bandwidth, and how training/rollout numerical paths affect correctness.
- **Validation contract:** check exact LongCat checkpoint, fork commit, device/CANN, output oracle and TTFT/TPOT/goodput. An Nvidia CUDA optimization and a domestic-card implementation are **different paths**.

**Evidence status:** official open code + first-party engineering reports; no independent reproduction in this catalogue. Model papers belong once in canonical topic categories after G0–G5 review, not duplicated here.
