# Technical Topics

[← Home](../README.md) · [Frontiers](../frontiers/README.md) · [Organizations](../organizations/README.md) · [Communities](../communities/README.md)

Eight technical topics connect principles, upstream implementations, engineering developments, industry practice and research literature. Each publication has one primary home; cross-links are encouraged.

The research inventory contains **977 source-curated papers across 44 engineering directions**, plus 30 historical foundations and 4 topic-specific surveys relocated from the homepage. Counts of older review batches are historical.

| Mechanism | Canonical entries | Sub-groups | Scope |
|---|---:|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 137 | 6 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 186 | 6 | Reuse, eviction, compression, offloading and distributed KV state. |
| [Decoding Acceleration](decoding-acceleration.md) | 100 | 5 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 53 | 6 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 91 | 4 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 164 | 6 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 146 | 5 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 100 | 6 | Validated models, traces, benchmarks and production diagnosis |
| **Total** | **977** | **44** | |

## Classification boundaries

The **primary engineering mechanism** determines the one canonical home; workload labels (Agent, multimodal, reasoning, long-context), accelerator vendor, venue, and application domain are cross-cutting attributes rather than extra categories. For borderline studies, use the main technical contribution, not keyword frequency:

| Boundary | Choose the first when… | Choose the second when… |
|---|---|---|
| **KV Cache** vs **Quantization** | The principal problem is cache residency, reuse, eviction, tiering or transfer, even if compression is used. | The principal result is a low-bit representation, error control or executable quantization scheme, including KV precision. |
| **Kernels & Compilers** vs **MoE & Sparse Execution** | The novelty lies in operator implementation, tiling, code generation or launch/fusion. | The novelty lies in conditional computation, expert placement, sparse execution policy or expert communication. |
| **Runtime & Scheduling** vs **Distributed Serving** | The system decides request ordering, batching, routing, fairness or SLO policy. | The system changes the physical execution layout, parallelism, transport, disaggregation or fleet lifecycle. |
| **Decoding Acceleration** vs **Runtime & Scheduling** | The work changes draft generation, verification, acceptance or non-autoregressive decoding. | The work schedules existing decoding methods dynamically among requests and resources. |
| **Benchmarking & Analysis** vs **optimization categories** | The primary contribution is a workload, measurement method, correctness oracle, analytical model or diagnosis. | The primary contribution is an optimization mechanism evaluated using those tools. |

Hybrid systems may span multiple rows; keep **one full paper entry** under the dominant mechanism and refer to it in prose elsewhere when useful. Do not duplicate bibliography rows to make a category look fuller.

## How to use this index

Start with the bottleneck and execution model, then follow upstream code and representative literature. Treat benchmark results as author-reported unless reproduced explicitly. Submit changes under the [curation policy](../CURATION.md) and [review rules](../STRICT_REVIEW.md).

[Review receipts and historical inventory](../reviews/README.md).
