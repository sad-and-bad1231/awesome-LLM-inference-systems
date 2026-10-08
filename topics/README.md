# Papers by systems mechanism

Eight stable research categories. Papers have **one primary technical home**, chosen by the novel reusable mechanism—not by author, hardware brand, year, application or trending workload. Multi-layer contributions may be cross-linked, but full paper rows are not duplicated.

[← Home](../README.md) · [Curation policy](../CURATION.md)

| Mechanism | First verified additions | Scope |
|---|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 2 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 3 | Reuse, eviction, compression, offloading, distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 3 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 5 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 3 | Expert movement, conditional computation, sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 1 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 1 | Parallelism, multi-node orchestration and phase placement |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 3 | Validated models, traces and production diagnosis |

## Migration discipline

**October 2026 initial wave: 21 new papers**, individually matched to publisher/conference pages and their mechanism/evaluation summaries. These are **additions**, not a re-labeling of the older 80-entry public collection.

The existing [Serving Systems first cohort](serving-systems.md) (50 papers, 2024–2026) is retained as a **legacy selection pending re-audit**. We will move entries into one of the eight categories only after checking paper title, actual publication, primary mechanism and end-to-end engineering evidence; a prior `verified_legacy`/`core` field does not grant automatic admission. Historic [Foundations](../README.md#foundational-and-influential-papers) remain featured on the homepage; links to them are cross-references, not second full records.

**No quota.** A class with only one newly admitted paper is intentional, not a sign that its field lacks important works. The emphasis is on publication provenance, mechanism novelty, evaluative rigor and relevance to real inference.
