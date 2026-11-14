# Papers by systems mechanism

**Current canonical index (2026-11-14): 938 source-curated papers · 8 mechanisms · 44 engineering directions.** Each entry has one primary home; **source admission is not independent reproduction or exhaustive G0–G5 certification**. PR #80 contributes 77 source-curated entries from the shared 852-paper baseline (852 → 929); the separate DCore admission adds one distinct entry, giving a reconciled total of **930**. DCore is absent from PR #80's topic branch.

**Inventory history:** [October 31 close (851)](../reviews/OCTOBER_2026_FOLLOWUP_SWEEP_20261031.md) → [November 2 intake (854)](../reviews/NOVEMBER_2026_ARXIV_FIRST_PASS_20261102.md) → [November 5 adjacent-scope cleanup (852)](../reviews/ADJACENT_FULL_SCOPE_REVIEW_20261105.md) → [November 9 intake (862)](../reviews/NOVEMBER_2026_SYSTEMS_SWEEP_20261109.md) → [Nov 9 expanded pass (879)](../reviews/NOVEMBER_2026_EXPANDED_SWEEP_20261109.md) → [Nov 9 third pass + Nov 10 preprint recalibration (898)](../reviews/NOVEMBER_2026_THIRD_PASS_20261109.md) → [Nov 10 frontier + backlog re-audit (929)](../reviews/ARXIV_FRONTIER_BACKLOG_REAUDIT_20261110.md). Original sources of the two removed video-only works remain in the scope review and [Frontier context](../frontiers/README.md). Older snapshots are not live totals; see [review index](../reviews/README.md).

**November 11 addition:** [Baidu/DCore controlled speculative-decoding study](benchmarking-analysis.md#performance--efficiency-studies-27) admitted as one author-reported, publicly reproducible-artifact *preprint* after [G0–G5 case review](../reviews/BAIDU_MECHANISM_CODE_AUDIT_20261111.md) (**852 → 853**). No GPU test was performed here.

**November 14 decoding-only intake:** [eight source-reviewed additions and explicit WATCHs](../reviews/NOVEMBER_2026_DECODING_SWEEP_20261114.md) extend Decoding 91 → 99 and the corpus 930 → 938. Earlier numbers are historical.

Each paper has **one primary mechanism home**. Hardware, Agent, multimodal, long-context and reasoning are evaluation contexts—not additional top-level bins. [Frontiers](../frontiers/README.md) is a reading cross-index and never a second canonical paper list.

[← Home](../README.md) · [Research labs](../communities/README.md) · [Strict G0–G5 review](../STRICT_REVIEW.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Sub-groups | Scope |
|---|---:|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 123 | 6 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 179 | 6 | Reuse, eviction, compression, offloading and distributed KV state. |
| [Decoding Acceleration](decoding-acceleration.md) | 99 | 5 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 52 | 6 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 88 | 4 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 158 | 6 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 143 | 5 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 96 | 6 | Validated models, traces, benchmarks and production diagnosis |
| **Total** | **938** | **44** | |

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

- **Read:** follow the closest *engineering bottleneck* into a sub-group; prioritize a clearly stated mechanism, actual model/hardware/workload and real versus simulated execution.
- **Evaluate:** treat every reported performance/accuracy figure as **author-reported** unless an explicit reproduction receipt says otherwise. Distinguish kernel-only results from end-to-end serving, quality-changing work from exact execution, and trace replay from production measurement.
- **Contribute:** check title/arXiv-ID/DOI aliases across all eight pages, verify the publisher identity, and submit a small source-backed change with a G0–G5 receipt. HOLD candidates stay in dated `reviews/` notes, not canonical tables.

**History and provenance:** [Archived topic-index chronology](../reviews/archive/TOPIC_INDEX_HISTORY_20261030.md) preserves the prior 2026 admission accounting, including provisional intake and later removal waves. Recent per-candidate sources: [Oct 30 arXiv/labs](../reviews/ARXIV_LAB_SWEEP_20261030.md), [Oct 8–21 backfill](../reviews/ARXIV_OCT08_21_INTATTENTION_20261029.md), [Oct 22–29](../reviews/WEEKLY_ARXIV_MAINLINE_20261029.md). Historical totals are not current catalog counts.
