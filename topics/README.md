# Papers by systems mechanism

**Current inventory (2026-10-30): 821 unique canonical topic papers · 8 mechanism classes · 44 engineering tracks.** These are **source-curated reading selections**, not 813 independently reproduced experiments or a guarantee of complete G3/G4 baseline scrutiny.

Each paper has **one primary mechanism home**. Hardware, Agent, multimodal, long-context and reasoning are evaluation contexts—not additional top-level bins. [Frontiers](../frontiers/README.md) is a reading cross-index and never a second canonical paper list.

[← Home](../README.md) · [Research labs](../communities/README.md) · [Strict G0–G5 review](../STRICT_REVIEW.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Sub-groups | Scope |
|---|---:|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 114 | 6 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 160 | 6 | Reuse, eviction, compression, offloading and distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 79 | 5 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 43 | 6 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 72 | 4 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 144 | 6 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 133 | 5 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 76 | 6 | Validated models, traces, benchmarks and production diagnosis |
| **Total** | **821** | **44** | |

## How to use this index

- **Read:** follow the closest *engineering bottleneck* into a sub-group; prioritize a clearly stated mechanism, actual model/hardware/workload and real versus simulated execution.
- **Evaluate:** treat every reported performance/accuracy figure as **author-reported** unless an explicit reproduction receipt says otherwise. Distinguish kernel-only results from end-to-end serving, quality-changing work from exact execution, and trace replay from production measurement.
- **Contribute:** check title/arXiv-ID/DOI aliases across all eight pages, verify the publisher identity, and submit a small source-backed change with a G0–G5 receipt. HOLD candidates stay in dated `reviews/` notes, not canonical tables.

**History and provenance:** [Archived topic-index chronology](../reviews/archive/TOPIC_INDEX_HISTORY_20261030.md) preserves the prior 2026 admission accounting, including provisional intake and later removal waves. Recent per-candidate sources: [Oct 30 arXiv/labs](../reviews/ARXIV_LAB_SWEEP_20261030.md), [Oct 8–21 backfill](../reviews/ARXIV_OCT08_21_INTATTENTION_20261029.md), [Oct 22–29](../reviews/WEEKLY_ARXIV_MAINLINE_20261029.md). Historical totals are not current catalog counts.
