# Papers by systems mechanism

**Final October 31 follow-up (2026-10-31): 851 unique canonical paper rows · 8 mechanisms · 44 engineering directions.** [Second-pass arXiv/EMNLP and industrial evidence audit](../reviews/OCTOBER_2026_FOLLOWUP_SWEEP_20261031.md) admits **16** source-reviewed nonduplicates after the prior **835** monthly snapshot, with each item separately pushed. This does **not** certify independent code execution, benchmarking, quality-equivalence or 100% October submission coverage. The earlier 835 figure is a dated checkpoint, not a second count.

**Historical first October monthly close (2026-10-31): 835 distinct source-curated papers · 8 mechanisms · 44 engineering directions.** The [October complete month-close audit](../reviews/OCTOBER_2026_MONTHLY_SWEEP_20261031.md) adds **14** nonduplicate paper rows to the latest **821** source baseline (not the historical 813 checkpoint). Each paper received its own push, and industrial releases/research-lab blogs are indexed separately. **G0–G5 source screening does not equal independent G3/G4 replication**. The earlier October 30 tally is a dated snapshot, not current.

**Historical checkpoint (2026-10-30): 821 canonical topic papers / 44 engineering tracks.** This was the baseline before the Oct 31 monthly close; no independent full-corpus reproducibility audit has been performed.

Each paper has **one primary mechanism home**. Hardware, Agent, multimodal, long-context and reasoning are evaluation contexts—not additional top-level bins. [Frontiers](../frontiers/README.md) is a reading cross-index and never a second canonical paper list.

[← Home](../README.md) · [Research labs](../communities/README.md) · [Strict G0–G5 review](../STRICT_REVIEW.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Sub-groups | Scope |
|---|---:|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 115 | 6 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 165 | 6 | Reuse, eviction, compression, offloading and distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 85 | 5 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 46 | 6 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 75 | 4 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 151 | 6 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 134 | 5 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 80 | 6 | Validated models, traces, benchmarks and production diagnosis |
| **Total** | **851** | **44** | |

## How to use this index

- **Read:** follow the closest *engineering bottleneck* into a sub-group; prioritize a clearly stated mechanism, actual model/hardware/workload and real versus simulated execution.
- **Evaluate:** treat every reported performance/accuracy figure as **author-reported** unless an explicit reproduction receipt says otherwise. Distinguish kernel-only results from end-to-end serving, quality-changing work from exact execution, and trace replay from production measurement.
- **Contribute:** check title/arXiv-ID/DOI aliases across all eight pages, verify the publisher identity, and submit a small source-backed change with a G0–G5 receipt. HOLD candidates stay in dated `reviews/` notes, not canonical tables.

**History and provenance:** [Archived topic-index chronology](../reviews/archive/TOPIC_INDEX_HISTORY_20261030.md) preserves the prior 2026 admission accounting, including provisional intake and later removal waves. Recent per-candidate sources: [Oct 30 arXiv/labs](../reviews/ARXIV_LAB_SWEEP_20261030.md), [Oct 8–21 backfill](../reviews/ARXIV_OCT08_21_INTATTENTION_20261029.md), [Oct 22–29](../reviews/WEEKLY_ARXIV_MAINLINE_20261029.md). Historical totals are not current catalog counts.
