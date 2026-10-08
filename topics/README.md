# Papers by systems mechanism

Eight research categories. Each accepted paper has **one primary home** based on its decisive reusable mechanism, not by author, application, hardware platform or conference.

[← Home](../README.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Scope |
|---|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 11 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 18 | Reuse, eviction, compression, offloading and distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 10 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 13 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 11 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 22 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 27 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 8 | Validated models, traces, benchmarks and production diagnosis |

## Admission summary (2026-10-08)

| Decision | Count |
|---|---:|
| First eight-category admission wave | 21 |
| Former 50-entry Serving cohort: reclassified and admitted | 49 |
| New second-wave papers admitted by primary-source screening | 50 |
| **Canonical topic entries** | **120** |
| Legacy paper held out: general-purpose AI model serving | 1 |

The [Serving migration record](serving-systems.md) explains the holdout and bibliographic corrections. Existing 30 [foundational papers](../README.md#foundational-and-influential-papers) remain a separate editorial reading path on the homepage, rather than being duplicated as full rows in topic pages. The six selected surveys also remain unchanged.

**Quality boundary.** Publisher/proceedings identity and proposed mechanisms have been cross-checked; independent reproduction of speedups is not claimed. Workshop articles are labeled as such. No automatic bulk import from the historical JSONL or upstream paper lists; per-paper experimental validity is an ongoing editorial review responsibility.
