# Papers by systems mechanism

Eight research categories. Each accepted paper has **one primary home** based on its decisive reusable mechanism, not by author, application, hardware platform or conference.

[← Home](../README.md) · [Curation policy](../CURATION.md)

| Mechanism | Canonical entries | Scope |
|---|---:|---|
| [Kernels & Compilers](kernels-compilers.md) | 50 | Attention kernels, GEMM, compilers and hardware mappings |
| [KV Cache & Context Memory](kv-cache-memory.md) | 97 | Reuse, eviction, compression, offloading and distributed KV state |
| [Decoding Acceleration](decoding-acceleration.md) | 30 | Speculative, blockwise and parallel generation |
| [Quantization & Compression](quantization-compression.md) | 27 | Low-bit representation with executable system gains |
| [MoE & Sparse Execution](moe-sparse-execution.md) | 44 | Expert movement, conditional computation and sparse attention |
| [Runtime & Scheduling](runtime-scheduling.md) | 81 | Batching, routing, SLO, fairness and request-level control |
| [Distributed & Disaggregated Serving](distributed-serving.md) | 95 | Parallelism, multi-node orchestration, memory/compute disaggregation |
| [Benchmarking & Systems Analysis](benchmarking-analysis.md) | 32 | Validated models, traces, benchmarks and production diagnosis |

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
| Strict re-verification of legacy holdouts (2026-10-11) | 39 |
| Follow-up legacy primary-source verification (2026-10-11) | 9 |
| Agentic cache, quantization & speculation verification (2026-10-11) | 7 |
| Further verifiable KV, MoE and inter-regional systems (2026-10-11) | 6 |
| Verified LoRA disaggregation systems (2026-10-11) | 2 |
| Legacy primary paper identity & evaluation review (2026-10-11) | 3 |
| Additional verified execution mechanisms (2026-10-11) | 4 |
| **Canonical topic entries** | **456** |
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


## Strict re-verification of historical holdouts (2026-10-11)

Re-opened the historical per-record reconciliation and independently searched archival publisher pages, official code/artifact sites and author preprints. **39 formerly withheld works** met the same admission gate (4 dated 2025; 35 dated 2026; venue status verified independently), with distinct execution mechanisms and author-reported actual runtime/accuracy or GPU validation. No conference-poster promotion is allowed: **Kascade and Cascade are cited as arXiv 2025 preprints**, not as MLSys 2026 main-conference papers. Training-free dLLM acceleration is inference work, not training-only research. Strict decoding output-distribution equivalence is **not claimed** for FLy or approximate diffusion methods; they are evaluated as quality/latency trade-offs. **The remaining historical corpus is NOT certified complete or rejected:** entries without individual primary-source and experiment review remain pending verification. Cross-title aliases, surveys and existing bibliography rows must be reconciled separately; candidate count is not a quality score.


Further evidence-backed admissions: SiFAR and near-speed-of-light GPU collectives (real multi-GPU LLM inference), Sangam (runnable H100 dLLM Serving), SMetric (production Agent traces), PagedWeight (GPU memory/quality/throughput), D-cut (batched speculation), ViBE (GPU-variability-aware EP placement). **HiFA4 is held out** because the speedup is projected without measured on-NPU Kernel timing. **VarRate is held out** pending convincing end-to-end online inference runtime evidence beyond compression accuracy and prefill overhead. Both are evidence-boundary decisions, not claims of scientific invalidity.


Additional official-record checks admit vLLM-Omni (stage-graph and executable serving), Tarragon (worker-level fault containment), ConServe (conversation-level single KV move), SPIN (vLLM sparse-attention/hierarchical KV) and **Tropical**. The legacy corpus incorrectly dated Tropical 2026: its actual formal publication is **DAC 2025**, DOI 10.1109/DAC63849.2025.11132617. Exact citation year takes precedence over uploaded records.


Tutti, HYPIC and KEEP were separately source-confirmed through the original arXiv descriptions plus authors' public implementations: Tutti integrates GPU-initiated SSD KV transport with a vLLM connector, HYPIC implements segment-composable recurrent state and Attention boundary repair, and KEEP implements grouped persistent planning KV with cross-layer recomputation. All three report real inference TTFT/throughput or task-quality tradeoffs; they are arXiv **preprints** and are not mislabeled as formal conference acceptances.


Further primary-source admissions: SLOs-Serve (multi-SLO token budgeting), SVF geometry-aware scheduling (vLLM implementation), the TOSEM 2026 929-bug empirical study, ICLR 2026 Tactic, LycheeDecode, MiniPIC, and HERALD. Each has implementation-based system evidence, rigorous measured systems analysis, or end-to-end hardware evaluation described in its primary source. TOSEM's empirical bug taxonomy is a systems study, not a claim to have optimized inference. Authors' published speedups are not independently reproduced.


RouteBalance is admitted on actual heterogenous 28-GPU cluster measurements of joint model selection and instance load balancing, including router-baseline isolation and source release. Models Take Notes at Prefill is admitted for editable/position-portable cache composition, public implementation and an online vLLM system evaluation; enormous reported P90 TTFT improvements apply to specific recomputation baselines and must not be generalized across all workloads. The economic proposal Can I Buy Your KV Cache? is held out as a general-serving architecture admission, as its token-level/compute microbenchmark and monetary model are insufficient proof of a deployed cross-party cache-delivery system.


## Follow-up primary-source verification: disaggregation and elastic serving (2026-10-11)

Nine additional source-checked high-impact systems are admitted (2025: 4; 2026: 5). Details are placed in the existing Distributed Serving, KV/Memory and Runtime/Scheduling classes: semi-PD, HydraInfer, TraCT, TokenScale, RTP-LLM, TokenDance, KernelFlume, SAC and Festina. Each has an original paper source and author-reported real GPU/prototype or production-trace Serving results. KernelFlume's real A6000/H100 measurements are intentionally distinguished from its larger simulated scenarios. The original 1,003-record holdouts **remain pending except specifically rechecked records**; they are not wholesale rejected.


## Agentic cache, quantization and speculation verification (2026-10-11)

Seven more historical source entries were individually checked and admitted: Pythia (live SGLang/A100 implementation and real traces); TokenCake (arXiv 2025 preprint updated in 2026, with vLLM source and agent workload experiments); AdaptCache (explicitly **SOSP BigMem 2025 Workshop**, not main SOSP); SwiftCache (cross-model NVLink KV reuse); CacheWise (vLLM coding-agent traces); SAW-INT4 (SGLang fused Paged KV INT4/quality/throughput evaluation); and JetSpec (originally JetFlow in this uploaded corpus, now a 2026 preprint with original arXiv ID 2606.18394, GPU and vLLM benchmarks). These are all substantive systems mechanisms with author-reported deployed or hardware-level evaluation. Publication labels never silently inherit future conference claims from code READMEs.


## Further verified cache, MoE and scheduling mechanisms (2026-10-11)

Six additional original-corpus records independently passed the same admission gate: formal **SC 2025 MaverIQ**, arXiv **2025 EVICPRESS**, and arXiv **2026** WANSpec, VeriCache, Joint Encoding of KV Cache Blocks, and CoX-MoE. Every paper has a distinct serving-specific implementation or architectural mechanism and authors' reported actual code or cluster/GPU/cloud deployment evaluation. WANSpec combines measured real-cloud deployment with simulated extrapolation; no simulator output is represented as physical hardware measurement. VeriCache's output-equivalence claim is attributed to the original experimental protocol. The prior pending queue remains unfinished.


## Evidence-gated LoRA verification (2026-10-11)

Two previously unverified historical entries were source-checked and admitted: InfiniLoRA (independent LoRA-server execution, GPU-initiated transfers, system-level SLO tests) and LoRAServe (rank-aware cross-GPU adapter routing with production-trace TTFT and throughput evaluation). Both remain correctly identified as arXiv preprints, not proven archival conference papers. Other unverified candidate identities remain pending.


## Legacy source checks (2026-10-11)

TetriInfer was located under its full preprint title with working disaggregated serving evaluation. AlayaDB has a verified SIGMOD 2025 DOI and industrial plus inference benchmark reports, and thus belongs in KV Memory despite its vector database name. `On Evaluating Performance...` provides a serving-specific baseline/workload/metric audit and speculative decoding case study. `RAGBoost` was cross-checked and **not** added as an independent duplicate: the closely matching MLSys 2026 `ContextPilot` by the same authors is already present; publication version identity requires further reconciliation. SPAD remained withheld under the physical-serving gate because its new chips and clusters are modeled/simulated rather than actually measured. Other historical pending candidates remain to be individually audited.


## Additional source-reviewed execution systems (2026-10-11)

Four long-pending works admitted from original arXiv abstracts with concrete claimed implementations and measured real devices/serving: CacheFlow (3D parallel KV restoration), ReMP (state-preserving TP/PP reconfiguration), NPUMoE (Apple ANE MoE execution), and SCORPIO (heterogeneous-SLO admission and batching). All remain **preprints** unless publisher evidence changes. Paper-reported gains are not independently replicated; the remaining legacy queue is not characterized as rejected merely for lacking metadata.
