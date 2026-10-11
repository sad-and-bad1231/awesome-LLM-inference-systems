# Papers by systems mechanism

Eight research categories. Each accepted paper has **one primary home** based on its decisive reusable mechanism, not by author, application, hardware platform or conference.

[← Home](../README.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Scope |
|---|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 50 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 77 | Reuse, eviction, compression, offloading and distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 20 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 24 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 36 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 70 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 80 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 29 | Validated models, traces, benchmarks and production diagnosis |

## Admission summary (2026-10-08)

| Decision | Count |
|---|---:|
| First eight-category admission wave | 21 |
| Former 50-entry Serving cohort: reclassified and admitted | 49 |
| New second-wave papers admitted by primary-source screening | 50 |
| Broad literature sweep: source-screened additional papers | 80 |
| 2026 top-conference additions (strict-source tranche) | 53 |
| Distributed-inference literature expansion (2026-10-09) | 33 |
| 2025–2026 landmark systems sweep (2026-10-11) | 48 |
| Legacy JSONL reconciliation (2026-10-11) | 52 |
| **Canonical topic entries** | **386** |
| Legacy paper held out: general-purpose AI model serving | 1 |

The [Serving migration record](serving-systems.md) explains the holdout and bibliographic corrections. Existing 30 [foundational papers](../README.md#foundational-and-influential-papers) remain a separate editorial reading path on the homepage, rather than being duplicated as full rows in topic pages. The homepage has seven selected surveys, including one new distributed-collectives survey.

**Quality boundary.** Publisher/proceedings identity and proposed mechanisms have been cross-checked; independent reproduction of speedups is not claimed. Workshop articles are labeled as such. No automatic bulk import from the historical JSONL or upstream paper lists; per-paper experimental validity is an ongoing editorial review responsibility.


## Broad-source screening note (October 2026)

A broad candidate discovery pass examined the original uploaded list, historical repository candidate pool, MLSys 2025–2026 proceedings, and selected USENIX/ACM/ICML/ICLR/NeurIPS records. **80 additional paper entries** were selected on publicly traceable publication identity, an identifiable inference-relevant system mechanism, and abstract/paper-reported technical or experimental evidence. The 200 total is the cumulative eight-topic total, **not** a claim that 200–300 new papers passed admission. Many candidate records were excluded or deferred when publication details or actual systems evidence were insufficient.

The evidence tier is publication/abstract and technical-description screening, **not** full-paper methodological audit or experimental reproduction. Some shortlisted work is a directly relevant compiler/edge execution primitive rather than a dedicated online LLM serving system; this boundary is made explicit in its one-sentence entry. Continue resolving publication-title/link discrepancies in later editorial passes rather than inflating the list by adding source-unverified conference titles.


## 2026 conference-only audit (2026-10-08)

This tranche adds **53 papers published in 2026**, with one official conference proceedings/publisher/venue page per entry, or the paper-specific DOI. Covered venues: MLSys, OSDI, EuroSys, ASPLOS, ISCA, HPCA, ICML, and ICLR. Excluded were duplicates, arXiv-only submissions, training-only papers, publication-program titles without substantiated mechanisms, and general DNN work lacking inference relevance. The 2026 NeurIPS conference does not take place until December and its official proceedings are not yet equivalent to an issued 2026 archival paper volume.

**Important:** The user requested **300 new 2026 top-conference papers**. This vetted tranche adds **53**, not 300; its contribution does not discharge the numerical target. The 253 figure is the *cumulative* eight-topic total (previously 200). No paper is added solely to meet a quota; source and system-mechanism standards remain in force.

This pass checked publication identity and mechanism from publisher/venue material. Evaluation details are summarized from authors' papers and abstracts; no independent hardware replication or complete methodological audit is implied.


## Distributed-inference literature update (2026-10-09)

Added **33 canonical entries** (2024–2026), including **24 papers from 2026**, into existing mechanism pages. Priorities: 2026 disaggregated inference, Attention-DP/Expert-EP synchronization, collective communication, multi-node KV transfer, expert placement, and AFD counter-evidence. Conference entries link to publisher proceedings; arXiv-only papers explicitly say **preprint** or **technical report**. Mechanisms were screened against primary abstracts/technical descriptions, **not** reproduced benchmarks, and this is **not** claimed exhaustive 2026 coverage. The earlier 53-paper 2026 formal-conference tranche remains a separate cohort.


## 2025–2026 landmark inference-systems sweep (2026-10-11)

This reviewed wave adds **48** distinct primary papers (**26 from 2025; 22 from 2026**), placing every entry in its existing primary mechanism home. Sources were checked against official SOSP 2025, SIGCOMM 2026, FAST 2026, USENIX ATC 2025, ASPLOS 2025/2026, MLSys 2025, PACMMOD 2026 and PVLDB 2026 publication/session records, with ACM DOI/USENIX paper-specific links preferred. The one SIGCOMM program-only link is explicitly flagged as such in its venue cell. The wave emphasizes durable implementation mechanisms: workload-specific execution engines, P/D multiplexing, MoE expert communication, KV network/storage paths, low-precision compiler primitives, and production traces. Training-only, general GPU/network studies without LLM inference evidence, and uncertain paper identities were not imported. These descriptions rely on primary abstracts and official technical records; they do **not** represent independent replication or an exhaustive claim about every 2025–2026 publication.


## Historical 1,003-record JSONL reconciliation (2026-10-11)

The supplied legacy JSONL contains **1,003 candidate records**; it is a discovery dataset, not primary publication evidence. An exact normalized-title comparison against the pre-wave eight-topic bibliography found 206 direct overlaps; fuzzy/alternate-title, homepage and survey matches are handled conservatively separately. A strict primary-source and systems-evidence check admitted **52 additional papers** (**8 published in 2024; 27 in 2025; 17 in 2026**), placed in their existing mechanism categories. Important legacy errors corrected at admission: **MagicDec is ICLR 2025**, **Shortcut-connected Expert Parallelism is ICML 2025**, **HotPrefix and DepCache are PACMMOD 2025**, **LMCache's verified paper is arXiv 2025 rather than a verified MLSys 2026 publication**, and HACK's SIGCOMM appearance is a poster rather than an assumed full paper. Publisher or official conference identity and paper abstracts/author implementation claims were corroborated for admitted entries; no independent benchmark reproduction is implied. Entries without enough evidence remain outside the library. The one-row-per-source audit is delivered separately, not committed as a redundant catalog.


The historic-backfill pass also admitted early serving work (DéjàVu, CachedAttention, Andes, QLM, Hydragen, MemServe, Infinite-LLM, PowerInfer-2) and formally published **KDD 2025 BurstGPT**. Punica, EAGLE/EAGLE-2, Parrot and VTC fairness were found already present and were not re-added. The legacy BurstGPT record was dated to its 2024 preprint, while the canonical paper is cited at its final 2025 ACM proceedings venue.


An additional high-signal sweep admitted TileLang (source-evidenced kernel compiler/implementation), Medha (long-context pipeline and distributed KV), BitMoD (HPCA 2025 bit-serial engine), Cornserve (preprint evaluation and open implementation) and a measured multimodal production-trace study. These entries are labeled according to verified archival or preprint status, not the legacy dataset's venue string.
