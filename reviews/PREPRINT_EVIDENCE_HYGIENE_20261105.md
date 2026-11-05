# 2026-11-05 preprint identity and evidence-hygiene pass

**Baseline:** `main` at `31009fea`, 852 canonical papers / 8 systems mechanisms / 44 engineering directions. This pass changes **11 existing rows across three topic pages**; **zero new admissions/removals** and zero author-reported speedups independently reproduced.

## What was screened — and what was not

Mechanical scan of the eight canonical topic pages returned **199 rows** with catalogue year **2026** and whose venue column contained `arXiv` or `preprint` (including some papers also claiming venue acceptance). This is an **editorial risk queue**, not proof that all 199 are unpublished, weak, independently reviewed, or even individually examined. We then prioritized short or underspecified descriptions whose mechanism, measurement unit, model/hardware scope, or bibliographic identity could be corrected from author/publisher-facing abstract and accessible published descriptions.

The **11 source-scrutinized rows below** are explicitly scoped corrections, not a 199-paper independent primary-paper deep audit. Text descriptions contain authors' metrics under their evaluation conditions; no local experiment or code reproduction took place.

## Exact changes and source receipts

| Paper / primary source | Corrected claim or mechanism | Evidence boundary |
|---|---|---|
| [Nuska — Stage-Aware Communication Scheduling for Disaggregated LLM Serving](https://arxiv.org/abs/2603.17456) | **G0 identity correction:** the catalogue's older title, `Multi-stage Flow Scheduling for LLM Serving`, was superseded by **arXiv v2 (2026-09-19)**. The actual `Nuska` system prioritizes multistage KV Retrieval/Collective/P2D flows via Defer-and-Promote / RMLQ as an LLF approximation. | Author-reported **1.2–2.4× TTFT SLO attainment** in **8-server/32-GPU** testbed plus simulations; not 2.4× lower token latency. |
| [SmartGen](https://arxiv.org/abs/2607.28150) | Profile-based essential KV push, local+remote on-demand read, eventually full speculative KV transfer; restricts **initial** P/D handoff bytes. | Author **up to 4.3× faster Time-to-second-token**, not a universal TTFT/E2E Goodput improvement; network-constrained deployment. |
| [AFD limitations](https://arxiv.org/abs/2602.09721) | Communication-aware Roofline analysis of MoE Attention–FFN separation versus EP shows ordinary scale-out bandwidth dead-zone; Superpod and coarser experts can alter the conclusion. | **Analytical characterization**, not claim that AFD universally outperforms EP on deployed hardware. |
| [HMA-Serve](https://arxiv.org/abs/2606.29986) | Cross-vendor GDDR prefill / HBM decode, per-phase quantization, layerwise KV transport and lazy dequantization. | Author **up to 3.2× Goodput and 4.8× Goodput/$**, in **four Qwen3 sizes (4–32B)** with Tenstorrent×4/A100 hardware and sampled traces; not generic homogeneous-GPU speedup or verified Ascend behavior. |
| [PDD](https://arxiv.org/abs/2609.13161) | Prefill→RelayDecode→MainDecode cross-datacenter handoff overlaps WAN KV transfer with Relay Decode; decode-side radix cache and handoff orchestration. | Author **Benefit–Cost Ratio up to +37.5%** for tested H100/H200 and cross-DC deployment vs selected same-DC baseline, not TPS uplift. |
| [Kairos / load-aware deflection](https://arxiv.org/abs/2607.02043) | Decode-side chunked prefill deflection with estimated TTFT and in-flight TBT-SLO guard. | **2P2D A100** finding: prefill compute is 2–23% of measured P95 TTFT. This observation is not itself the intervention speedup. |
| [ASAP](https://arxiv.org/abs/2606.22541) | Async attention DP and expert EP with Superhub, length-aware batching, dual-batch interleaving, triple-stream overlap and layer-oblivious MoE Super Kernel on **CloudMatrix384**. | Author **+90% SLO-compliant Prefill instance throughput** on DeepSeek-V3.2 vs synchronous baselines with 5s TTFT SLO; not total multi-stage Serving throughput. |
| [TP/PP/Hybrid characterization](https://arxiv.org/abs/2610.05305) | Compute–communication–bubble model explains phase-dependent Parallelism tradeoff; no dynamic policy invented. | **8×A100 NVLink**, Qwen2.5-14B/32B, FP16, fixed ISL/OSL; TTFT/ITL and operator breakdown only. |
| [CacheWise](https://arxiv.org/abs/2606.16824) | Coding-Agent trace informed prefix-aware scheduling + predicted tool metadata KV reuse/eviction in vLLM. | Author **2–2.6× fewer evictions, up to 3.5× session completion improvement**; whole session metric, not kernel TPOT. |
| [VeriCache](https://arxiv.org/abs/2605.17613) | Compressed-KV Draft + full-KV host/remote transfer overlapped with verification: exact output through Full-KV Verify. | Author **up to 4× throughput vs Full-KV** in tested environments; still requires full KV stored/transferred outside HBM, not a free lossless compressor. |
| [SAC sparse KV CXL](https://arxiv.org/abs/2606.19746) | SGLang/HiSparse with DeepSeek-V3.2 sparse indexer fetches per-layer top-k KV from CXL pool rather than full RDMA prefix transfer. | Author **2.1× throughput, up to 9.7× TTFT and 1.8× TBT decreases** vs selected RDMA baselines; depends on CXL/Sparse Attention and network topology. |

## Structural consistency and provenance rules

- 11 rows remain in their original primary mechanism homes; counts remain **852 / 8 / 44**.
- A preprint title is not an immutable identity: use latest arXiv title/version, preserving the arXiv ID. This pass fixed Nuska v1→v2.
- Distinguish **TTFT**, **Time-to-second-token**, **TBT/TPOT**, **SLO-attainment**, **Goodput**, **Goodput/$** and **Session Completion Time**. A measured improvement in one is not a bound on any other.
- Full paper methodology and author artifacts are not automatically validated by checking title/abstract. A source-level KEEP is not experimental reproduction. Claim wording now describes its original source rather than inventing an independent hardware result.

## Further P1 queue

1. Among the remaining **2026-preprint venue-labelled records** review important terse or scope-sensitive studies: `KVEraser`, `Joint Encoding of KV-Cache Blocks`, `ReMP`, `Geometry-Aware Online Scheduling`, `CacheFlow`, `SmoothAgent`, `Sangam`, `ShuntServe`, `WANSpec`, `LLMServingSim 2.0`; prioritize claims that could be mistaken for real Serving or for exact model preservation.
2. Continue deduplicating **publication aliases** across arXiv / proceedings / DOI and ensure latest paper title. The current offline linter detects identical first-source IDs but cannot prove semantic non-duplication.
3. Audit model and hardware setup, strongest existing baseline, code revision, and actual output oracle for **high-return reproducible systems** (especially Ascend, multi-card communication and agent KV policy) before a larger admission campaign.
4. Record per-row primary source, exact metric, critical limitation, code/artifact, and (if attempted) a distinct **reproduction receipt**. Treat unattributed marketing/blog speedups as HOLD.

**Do not equate the 199 mechanical selection with 199 full-text audited papers.** This document is a traceable targeted evidence correction.
