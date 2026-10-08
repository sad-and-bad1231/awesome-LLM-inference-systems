# Papers by systems mechanism

Eight research categories. Each accepted paper has **one primary home** based on its decisive reusable mechanism, not by author, application, hardware platform or conference.

[← Home](../README.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Scope |
|---|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 25 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 35 | Reuse, eviction, compression, offloading and distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 15 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 15 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 17 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 38 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 38 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 17 | Validated models, traces, benchmarks and production diagnosis |

## Admission summary (2026-10-08)

| Decision | Count |
|---|---:|
| First eight-category admission wave | 21 |
| Former 50-entry Serving cohort: reclassified and admitted | 49 |
| New second-wave papers admitted by primary-source screening | 50 |
| Broad literature sweep: source-screened additional papers | 80 |
| **Canonical topic entries** | **200** |
| Legacy paper held out: general-purpose AI model serving | 1 |

The [Serving migration record](serving-systems.md) explains the holdout and bibliographic corrections. Existing 30 [foundational papers](../README.md#foundational-and-influential-papers) remain a separate editorial reading path on the homepage, rather than being duplicated as full rows in topic pages. The six selected surveys also remain unchanged.

**Quality boundary.** Publisher/proceedings identity and proposed mechanisms have been cross-checked; independent reproduction of speedups is not claimed. Workshop articles are labeled as such. No automatic bulk import from the historical JSONL or upstream paper lists; per-paper experimental validity is an ongoing editorial review responsibility.


## Broad-source screening note (October 2026)

A broad candidate discovery pass examined the original uploaded list, historical repository candidate pool, MLSys 2025–2026 proceedings, and selected USENIX/ACM/ICML/ICLR/NeurIPS records. **80 additional paper entries** were selected on publicly traceable publication identity, an identifiable inference-relevant system mechanism, and abstract/paper-reported technical or experimental evidence. The 200 total is the cumulative eight-topic total, **not** a claim that 200–300 new papers passed admission. Many candidate records were excluded or deferred when publication details or actual systems evidence were insufficient.

The evidence tier is publication/abstract and technical-description screening, **not** full-paper methodological audit or experimental reproduction. Some shortlisted work is a directly relevant compiler/edge execution primitive rather than a dedicated online LLM serving system; this boundary is made explicit in its one-sentence entry. Continue resolving publication-title/link discrepancies in later editorial passes rather than inflating the list by adding source-unverified conference titles.
