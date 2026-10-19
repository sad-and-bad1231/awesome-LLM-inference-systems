# Curation policy

## Strict second-pass handoff (2026-10-18)

**Use [STRICT_REVIEW.md](STRICT_REVIEW.md) before the next curation batch.** The provisional broad intake has been screened by identity/target, **not** accepted after an independent methods or reproduction audit. Original historical pool: **1,003 distinct records**, **762 with directional decisions**, **241 still evidence-pending**. Historical pre-audit inventory: **678 canonical Markdown rows**. After the merged #45–#48 strict review, category cleanup and targeted capture, the catalog evolved from **669** after the #45–#50 curation sequence to **796** after 127 October 19 additions, then to a proposed **745** after 17 R0 removals, 34 additional R1 editorial removals, and six canonical re-homes. Both inventory counts use a **different denominator** from the original 1,003 JSONL candidates; not every current row has passed full G0–G5 review. Audit G0–G5, preserve author-claimed-vs-measured-vs-simulated boundaries, and remove weak or mis-scoped entries. A **first-pass taxonomy and screening sweep (2026-10-18)** then regrouped every category into **69 industry-grounded sub-groups** and tagged **176 rows** with an explicit inline caveat, removing no rows; because venue prestige is not an admission criterion here, borderline entries are kept and marked rather than deleted. Those 69 sub-groups were subsequently consolidated into **43 engineer-facing research directions**, moving five sparse-attention papers into MoE & Sparse Execution and one Tree-of-Thought scheduling paper into Runtime, without changing 669 canonical identities. Current proposed category counts: Kernels 80, KV 157, Decoding 81, Quantization 37, MoE 74, Runtime 129, Distributed 128, Benchmarking 59. The track structure is a reading map, **not** an admission or G0–G5 verdict. PR-level review and reviewer approval remain mandatory. **October 19 mainline review makes a concrete editorial decision on all 127 new entries (76 remain), but full-text G3 strong-baseline parity and G4 artifact/independent performance reproduction remain unresolved where not directly evidenced**. 

## Goal

Maintain an approachable, **selectively edited Awesome bibliography**, not a paper database, monitoring platform, knowledge graph, ranking site or per-paper note repository. `README.md` is the editorial entrance; each topic or organization Markdown page is a directly maintained, human-reviewed list. No machine-generated parallel catalog. Updates should remain small and attributable to primary sources.

## Admission gate

A paper or survey is accepted when all baseline requirements are satisfied:

1. **Systems relevance:** targets a concrete LLM inference/serving bottleneck (runtime scheduling, memory/KV, P/D transfer, kernel/compiler, distributed systems, parallelism, speculation, production operations), or is a genuinely foundational prerequisite.
2. **Substantive contribution:** proposes an identifiable and reusable system mechanism or architecture, not merely a renamed heuristic, new prompt/task, or marginal parameter tuning.
3. **Evidence:** credible real hardware, end-to-end workloads, published evaluation or production deployment; baseline and trade-offs should be intelligible. Older landmark papers can be admitted for historic influence after their concrete contribution is verified.
4. **Reliable identity:** title, year, venue, and official primary source checked; unverified entries must not appear in the published list.
5. **Research credibility:** author expertise, institutions, open-source adoption, and selective systems venues are positive supporting signals. **Institutional prestige alone is neither sufficient nor necessary.**

## Default exclusion

- Training-only or model-quality-only studies with no inference execution/system contribution.
- Pure simulation/proof/algorithm papers lacking convincing systems evidence, except historically foundational techniques.
- Derivative variants without an important new abstraction, measurable systems advantage, or materially different deployment context.
- General vector DB, security, generic cloud, and hardware papers not tightly connected to LLM inference.
- Duplicates, unpublished claims with unclear provenance, and venue/affiliation metadata that cannot be verified.

## Review workflow

1. Search the candidate in the original JSONL, but do not trust `verified_legacy` or `core` as final admission evidence.
2. Verify using conference proceedings, publisher, official paper PDF, or author's artifact/project page.
3. Judge **problem → mechanism → end-to-end value / limitations**. Favor precision over coverage.
4. Add one Markdown table row under the correct year with primary link, venue, concise institutions, and mechanism.
5. When uncertain, omit from public list and revisit in a later batch. Use GitHub issues/PRs for discussions; do not create a second shadow database.

## Rebuild provenance

Started 2026-10-08 from the user-supplied `papers.jsonl` (1,003 entries). First pass is selective identity-and-abstract-level screening, **not a complete reading of all papers or verification of each experimental claim**. The original 19-paper seed contained 18 entries from the upload and the missing FlashAttention paper. This follow-up adds 11 further historical/engineering papers and 6 complementary surveys. The initial 19-paper reset was merged into `main` in PR #7. Earlier data and automation can still be recovered from Git history. Later curation waves are independently checked and committed via reviewable changes; the original import and past scripts remain recoverable from Git history.

## Change discipline

No crawler, JSONL store, generated views, CI publication pipeline, deep research-note hierarchy, badges with hardcoded counts, or mandatory per-paper reading documents. Add complexity only when a concrete presentation need cannot be solved with Markdown.

## Survey-specific gate

Require a distinct systems lens (Serving architecture, hardware/compilers, KV cache, scheduling or distributed inference), credible primary source, meaningful taxonomy/synthesis and an honest coverage boundary. Prefer peer-reviewed surveys; strong lab-authored preprints must be clearly labeled. Reject near-duplicate overviews and survey titles without substantial system content.

## Historical prerequisites

Only a small set of pre-LLM papers belongs here, when its mechanism directly grounds modern inference (Transformer, blockwise verification, MQA). Label background architectures/algorithms separately from evaluated modern serving systems.

## Topic and organization pages

A **topic page** is a deliberately bounded, reproducible bibliography: one problem family, primary publication links, explicit year/venue, and a short *distinct mechanism* for each paper. Do not re-list established anchor entries from the home page to inflate coverage; link back instead. Paper counts are descriptive, never targets that override admission quality. When only an official conference program is available, label that weaker link provenance.

An **organization page** is a *small map of publicly documented work owned or clearly led by that organization*: model architecture with inference consequences, first-party software and technical reports, and public serving interfaces. Label the evidence type; never present an API feature as proof of an undisclosed implementation. **Do not catalog multi-institution collaborations merely because an organization coauthored a paper; place those in the topic bibliography instead.** Ownership of an open-source ecosystem component should be described precisely, without erasing external contributors. Prefer official repositories, publisher pages, and organization documentation. Verify version compatibility; do not exhaustively enumerate checkpoints, marketing releases, benchmarks or company news.

These are reader-facing Markdown pages, not a second structured database. Resist new pipelines and automatic admission.

## Eight mutually focused research classes (2026-10-08)

New primary paper admissions use **one** of: Kernels & Compilers; KV Cache & Context Memory; Decoding Acceleration; Quantization & Compression; MoE & Sparse Execution; Runtime & Scheduling; Distributed & Disaggregated Serving; Benchmarking & Systems Analysis. The classification follows the **decisive reusable mechanism** and its system boundary. Long-context, Agentic, Reasoning, Multimodal, GPU/NPU, model family and organization are workload/hardware contexts, **not top-level paper buckets**.

A publication may have multiple mechanisms, but each paper has only **one canonical full entry**. A short cross-reference to the home page's historical foundations is allowed. The legacy 50-entry Serving cohort was reviewed in the October 2026 migration: 49 assigned a canonical mechanism class, 1 (SkyServe) held out on LLM-specific scope grounds; the prior list is available from Git history. Reclassification does not independently reproduce measured results. The original user-provided JSONL and third-party awesome lists are discovery aids, not proof of admission. Publisher or formal conference pages determine publication status. For new entries, prefer a short technical mechanism rather than unverified benchmark speedup numbers.

## Emerging frontiers: selective adjacent-inference exception (2026-10-12)

The eight canonical classes remain classified by **decisive systems mechanism**. The [frontier reading map](frontiers/README.md) is a cross-index, never a second paper database or quota. Start with one foundation/measurement anchor per field and admit only exceptional follow-ons; venue rank, novelty language and large-scale paper discovery alone do not qualify.

For the emerging World Model / Interactive Video / VLA boundary, admit an **explicitly labeled adjacent foundation-model inference** work only when it exposes a reusable inference-time bottleneck or mechanism (e.g. long-lived state, temporal cache, streaming execution, heterogeneous VLM/action pipelines) **and** reports credible measured real-device execution or end-to-end inference. Training-only improvements, video-quality-only innovations, generic robotics datasets, and unmeasured speedup projections remain excluded. The foundational KernelBench general-ML evaluation paper is a **narrow landmark exception**, not permission to add generic DNN benchmarks or GPU optimization papers without clear relevance to future inference-kernel engineering.

For agent-generated kernels, require real compiled/executed kernels and distinguish benchmark speedups from actual inference serving speedups; consider hidden-distribution correctness, baseline flags and resource overhead. Preprints remain preprints. Treat all performance gains as *author reported*, not reproduced. Each paper retains one canonical mechanism home.

## Bibliographic quality control (2026-10-08)

For every new row: verify the **final published title and venue** rather than assuming an arXiv title persisted into formal proceedings; use a publication-specific URL where possible (publisher, USENIX session, PMLR, NeurIPS/ICLR/MLSys conference page). The source note must distinguish arXiv versions, workshops, corporate reports and peer-reviewed papers. Mark papers with unresolved links/identity for later editorial work rather than upgrading their status. Canonical full rows must not duplicate between topic pages, migrated cohorts or the historical Foundation showcase.

## Expansion and limits (October 2026)

Large corpus discovery is not bulk admission. A historical source's `core`, `verified_legacy`, or `official_source` label is only a retrieval signal. Each public topic row needs a named technical mechanism and a publisher/conference source with evidence of implementation or technically meaningful measurement. Screening of publication abstracts is weaker than reading the evaluation section or reproducing the results, and should never be described as equivalent. Generic DNN, training-only and venue-title-only candidates remain outside the main eight topics. No quota overrides these rules.

## 2026 conference expansion discipline

For the 2026 large-volume request, **2026 must describe the accepted formal conference publication**, not merely a paper's preprint date. Verify a paper-specific proceedings page, DOI or publisher-endorsed conference schedule, not a scraped bibliography entry. Require concrete LLM inference relevance and distinctive evaluated system mechanisms. Record numerical shortfalls honestly rather than importing training papers, generic GPU benchmark papers or incomplete program-title-only entries to satisfy a fixed quota. The 2026 conference-only tranche adds 53 entries. The target of 300 *additional* entries remains unmet and should not be confused with the cumulative library count.


## Distributed-inference curation wave (2026-10-09)

Added 33 screened papers within the existing mechanism pages, with particular attention to DP/EP scheduling metadata, asynchronous synchronization, collectives, topology-aware state movement, MoE attention/FFN disaggregation and skeptical design-space studies. Formal publication and preprint/technical-report status are distinguished in each row. The previous 53-item formal-2026-conference tranche has **not** been retroactively expanded using preprints. This wave checks paper identity and the authors' stated mechanism/evidence, **not** full reproducibility or exhaustive 2026 completeness.


## 2025–2026 landmark systems sweep (2026-10-11)

**48 newly admitted, nonduplicate papers** (26 published in 2025; 22 in 2026) were reviewed from selected primary conference sessions/proceedings and paper-specific publication records: SOSP, SIGCOMM, FAST, USENIX ATC and ASPLOS, including cross-checks against existing eight mechanism classes. Admission required an identifiable inference-time bottleneck, a novel execution/system mechanism, and paper-reported implementation plus evaluation; top-venue labels alone did not qualify. Each paper has exactly one canonical entry and a publication-year venue citation. Do not confuse source/abstract screening with replication or guarantee that all notable research has been discovered; continuously audit newly released venue records and exclude unresolved titles.

The MLSys 2025 cross-check additionally admits LeanAttention, MEADOW and relational LLM-query scheduling, and the ASPLOS 2025 cross-check adds FlashGen and Neuralink. SOSP 2026 had accepted-paper announcements by 2026-10-11 but acceptance alone is not an archival proceedings citation; pending papers were not bulk-admitted without publication-qualified sources.

The final 2026 PACMMOD/PVLDB publication check adds AlignedServe, RetroInfer, OrbitFlow and SPDP. CoKV was examined but withheld because the inspected evidence emphasizes compression quality rather than an isolated, validated online serving-system improvement. General ANN papers remain outside scope.


## Legacy corpus evidence-gated reconciliation (2026-10-11)

The separately supplied 1,003-record JSONL is **not** an authority for venue, year, status, evaluation or acceptance. We screened candidate records, compared normalized titles with existing canonical rows, and admitted **52 missing papers** only where a verifiable primary paper identity and a distinct inference-specific systems mechanism with reported implementation/evaluation were found. In particular, some legacy "official_source" descriptions only prove that a title appeared on a program or poster page; those are **not** sufficient evidence of a valid serving system. Poster/preprint/Industry Track distinctions and corrected publication years are recorded in individual entries. Existing duplicates and historical foundations are not re-added. Unverified, training-only, generic vector database, quality-only and venue-title-only candidates are held out; do not relax the gate to hit a paper target. This is source/abstract/technical-artifact screening, not an exhaustive full-paper experiment audit or independent replication. The 1,003-entry source-by-source disposition report is maintained as a separately delivered user artifact, **not** a parallel repository database.


The historic follow-up adds 9 originally missing older LLM serving mechanisms including the formally published KDD 2025 BurstGPT paper (listed as 2024 preprint in the original source). Punica, EAGLE/EAGLE-2, Parrot and VTC were already in the canonical categories and not duplicated. Oaken was corrected to its final ISCA 2025 DOI (10.1145/3695053.3731019). All selected admissions still require paper-reported implementation and evaluation; no exception was made for historically famous papers.


Five additional original-file candidates with concrete inference system evidence (TileLang, Medha, BitMoD, Cornserve and a multimodal serving trace/architecture study) passed the same admission gate. Possible preprint-only scheduling papers with unclear independent experimental boundaries remain withheld, even if conference submissions or later programs mention the title.


## Re-review correction: missing evidence is not rejection (2026-10-11)

Following a user challenge to the prior 1,003-record historical audit, we independently searched primary venues, author articles, and runnable artifacts for previously withheld entries. **39 additionally verified papers** were admitted without relaxing systems relevance, reusable mechanism, or credible implementation/evaluation requirements. In particular, earlier automated keyword screening incorrectly treated 'training-free' Diffusion LLM inference as training-only, and some authors' workshop/symposium/poster titles had been labeled as main-conference papers in the imported data. Canonical entries correct preprint versus proceedings identity; open implementation alone is not a substitute for measured evidence. The old holdout category 'unverified' MUST NOT be interpreted as an academic negative decision, and the original 1,003 papers have **not** all received full-text experiment audits. Admission uses primary source and author-reported systems evidence, not independent benchmark reproduction. See separately delivered per-source revision ledger for what was actually checked and what remains pending.

Further admissions include seven arXiv 2026 systems preprints with author-reported real-hardware or end-to-end inference evaluation. HiFA4's paper explicitly projects, rather than actually measures, its on-NPU kernel speed improvement; it remains held out. VarRate's evaluated compression accuracy and prefill overhead alone do not establish the full-serving runtime gain. Neither case warrants waiving the existing systems-evidence gate.

The independently located IEEE proceedings and institutional record establish that Tropical is DAC **2025**, despite an incorrectly labeled 2026 legacy entry; the historical source year is never an authority. The vLLM-Omni, Tarragon, ConServe and SPIN system reports were admitted on distinctive implementations and end-to-end/real-workload evidence, with arXiv status preserved.

The extended cache-system check admits Tutti, HYPIC and KEEP because paper primary records and public author artifacts document real Serving mechanisms and measured end-to-end latency/throughput or task accuracy. The domain of KEEP is embodied planning, but its main mechanism is inference-time KV recomputation and loading, rather than model quality alone.

The further evidence check corrects the original source's mistaken title of the empirical TOSEM LLM inference engine bug paper; it admits published fault characterization, not as an optimization, but as Benchmarking & Systems Analysis. Formal ICLR Tactic, vLLM-based SVF scheduling, and arXiv implementations with real measured runtime enter with correct provenance. All category indices were regenerated from actual per-topic row counts to fix an earlier string-concatenation error in index count updates.

RouteBalance and Models Take Notes passed source/evidence admission with explicit deployment scope caveats. The original STARC ASPLOS 2026 paper provides a functional GPU–PIM simulation artifact but no measured physical PIM speedup; although it is a legitimate peer-reviewed architecture paper, this particular serving-systems bibliography does not upgrade those simulated speedups into deployment evidence. BAT targets generative recommendation workflows rather than the curated general LLM serving boundaries. Titles cannot be admitted by venue rank alone.


## Additional source-verification wave (2026-10-11)

Nine disaggregated serving, elastically scheduled and KV-memory systems (semi-PD, HydraInfer, TraCT, TokenScale, RTP-LLM, TokenDance, KernelFlume, SAC and Festina) were admitted following paper-specific source lookup and evaluation/implementation screening. All arXiv-only papers are labeled **preprint/technical report** rather than being upgraded from the historical dataset's status. TraCT's public paper and thesis report partially different workloads and benchmark improvements; the canonical entry states only the shared mechanism and measured evidence rather than an inflated single speedup. The previous per-paper pending queue continues separately; no total-corpus completion is claimed.


## Agentic KV and runtime re-verification (2026-10-11)

Pythia, TokenCake, AdaptCache, SwiftCache, CacheWise, SAW-INT4 and JetSpec were individually checked against original publication pages, project code and author reports. TokenCake's early 2025 arXiv record and 2026 revision are not treated as a formally published 2027 conference volume; its primary venue remains arXiv until proceedings exist. JetFlow in the legacy data was revised/renamed JetSpec in current arXiv and project pages; the same arXiv identifier prevents duplicate imports. SAW-INT4 is admitted for real SGLang/PagedAttention co-design, not because model quality alone is sufficient. The older pending categories are not reclassified as scientific rejects.


Six further source-verified admissions (MaverIQ, EVICPRESS, WANSpec, VeriCache, Joint KV Encoding and CoX-MoE) were checked against publisher DOI, primary arXiv pages, release artifacts and real system benchmark summaries. MaverIQ's formal SC 2025 status was confirmed rather than imported from its legacy title alone; other preprints remain labeled as such. These meet the same inference-specific mechanism and implementation/evaluation gate, without any claim of independent result reproduction.


## Source-verified LoRA systems (2026-10-11)

Admitted InfiniLoRA and LoRAServe only after inspecting author primary abstracts reporting actual disaggregated serving mechanisms and GPU/production-trace SLO comparisons. Their preprint status remains explicit. Screening does not imply independent reproduction. Other historical candidates remain pending rather than rejected for absent metadata.


## Further verified source & identity reconciliation (2026-10-11)

Three more independent items were admitted on formal publisher or author-origin primary sources and paper-reported implementation/evaluation: TetriInfer (arXiv 2024 phase disaggregation), AlayaDB (formal SIGMOD 2025 DOI, inference-optimized KV/attention query system), and a preprint on rigorous LLM serving benchmark methodology with speculative decoding case study. RAGBoost has a strong paper-identity overlap with already-catalogued MLSys 2026 ContextPilot and is withheld for alias reconciliation rather than counted twice. Simulated SPAD hardware claims were not misrepresented as physical serving evaluations. Current review is still incomplete for the other historical records.


## Four system-execution source verifications (2026-10-11)

CacheFlow, ReMP, NPUMoE and SCORPIO report inference-native mechanisms, executable system implementations, and GPU/NPU serving evaluations in primary arXiv sources, justifying distinct admissions. Their published performance is author-reported rather than reproduced; preprint status remains explicit. Pending other records still need individual review, not keyword rejection.


## Six further per-source checked inferences (2026-10-11)

DeepSpeed-FastGen, LeMix, AIRS, CXL-SpecKV, ITME and VeriAttn have verified paper identities plus reusable inference execution, runtime or memory mechanisms, and described physical serving/system evaluations or publicly inspectable artifacts. Conference proceedings are distinguished from arXiv sources. Benchmark speedups remain attributed to papers, not independent replication; missing historical source URLs are not rejected by default.


## Six strictly source-verified kernel, KV and decoding systems (2026-10-11)

HILOS, SmallKV, Mirage, AttenIO, SpecMemo and Mirror-SD passed primary-paper identity, distinct systems mechanism and reported measured inference/accelerator evaluation. HILOS provides full synthesis and real-hardware deployment artifacts; Mirage has an open µGraph superoptimizer. SpecMemo/Mirror-SD are preserved as arXiv preprints rather than assigned unverifiable conference claims. AttenIO/SmallKV have verified formal publisher proceedings. This is selective admission, not a blanket inclusion of all technique papers, and does not imply independent reproduction.


## Three further verifiable compiler/hardware runtime works (2026-10-11)

KPerfIR (OSDI 2025), NeuronMM (Trainium matmul system preprint) and BaseRT (Metal-native inference engine preprint) have verified primary sources, distinguishable execution architectures and hardware measurements/code; broad generic GPU performance tools only qualify when they clearly affect the inference kernel toolchain. Speedup and overhead are author-reported and not independently reproduced.


## MoE primary-source verification (2026-10-11)

BrownoutServe's formally published IEEE TC 2026 method and open code demonstrate runtime burst/SLO handling, while CrossPool's 2026 preprint shows weight/KV GPU pool separation with measured long-context service latency; admitted under separate MoE Execution and Distributed Serving homes respectively. No model-quality-only or generic training paper imported, and neither author-provided result is an independent replication.


## First strict 50-record batch (2026-10-11)

The earliest 50 records marked pending in the user's immediately prior 1,003-entry ledger were source-checked individually. Five inference papers and one distinct long-context serving survey met the existing entry gates; five were prior canonical papers/aliases; 32 were excluded on documented subject/systems evidence or mechanism grounds; seven hardware/caching papers remain `pending_evaluation_verification` because full paper physical/simulated-hardware attribution, baseline fairness or complete deployment evidence is unresolved. Entries missing a URL in the original JSONL were actively searched, never rejected solely due to missing metadata. The formal HPCA 2026 final title and open artifact were confirmed for VectorLiteRAG, and the previous legacy title was not reused in publication citations. Official publishers are preferred over the old preprint names; preprints and surveys are clearly identified. Evaluations are attributed to the authors; this is individual primary-source/abstract and evaluation-material screening, not independent speedup reproduction or a completed full-methodology reading of all 50 papers. See the separately delivered batch ledger for full per-record reasons.

## Strict top-systems source review (2026-10-18)

From the historical 1,003-record JSONL ledger, independently checked formal venue identity, source-stated mechanisms and measured inference execution for six previously absent high-signal systems: Linear Layouts (ASPLOS 2026), LiquidGEMM (SC 2025), LIA (ISCA 2025), Chameleon (MICRO 2025), FastTTS (ASPLOS 2026) and Diff-MoE (SC 2025). One canonical entry per paper; official proceedings DOI in each row. The imported LIA title was incorrect: its actual published mechanism is AMX-enabled CPU–GPU collaboration with CXL, **not** layer bypass / speculative decoding. TokenWeave (MLSys 2026) was already present and is not double counted; the imported TokenBlend identity is not automatically treated as a separate paper.

**Evidence limits:** conference acceptance is not a quality proxy; each addition has a concrete system bottleneck and author-reported GPU/CPU execution or serving measurement. Source/abstract/method-level inspection is **not** full experimental reanalysis, benchmark replication, or a finding that all remaining historical entries have been audited. Public author artifacts are confirmed for LIA, FastTTS and the upstream Triton compiler underlying Linear Layouts; availability of official standalone reproduction code for LiquidGEMM, Chameleon or Diff-MoE was not established in this review. The original pending pool remains open to strict per-paper evidence review; do not infer rejection of unexamined entries.

## Rapid source-qualified intake for subsequent deep review (2026-10-18)

Following the strict six-paper PR #31 foundation, an additional **10 source- and mechanism-screened papers** were classified directly into the existing canonical topic tables. This implements a two-pass editorial policy requested by the maintainer: fast primary-publication/technical-mechanism screening now, later rigorous full-method/evaluation audit with removals where warranted. The first pass is **not** proof of experimental merit, methodological fairness, or reproduction, and does not imply the remaining historical backlog was screened. The canonical library is now **502** topic entries. No parallel metadata catalog or automated admission pipeline is added.

- **Kernels & Compilers:** KernelFoundry (ICML 2026, executed agent-generated kernels), Triton-Sanitizer (ASPLOS 2026, runtime memory diagnostics of real kernels) and the diffusion-LLM Prism work *Taming Dynamic Diffusion LLM Inference through Virtual Static Execution* (ICS 2026, compiler-stable physical-bucket execution).
- **Distributed & Disaggregated Serving:** Symbiosis (SoCC 2025, adapter/base-model split execution), Cortex (NSDI 2026, agent cross-region semantic data caching; explicitly **not** a KV-cache paper), StreamDiffusionV2 (MLSys 2026, adjacent interactive-video serving, real H100 measurements).
- **Runtime & Scheduling:** TetriServe (ASPLOS 2026, adjacent DiT serving, author-provided multi-GPU artifact) and *Optimal Scheduling Algorithms for LLM Inference: Theory and Practice* (full **Proc. ACM Meas. Anal. Comput. Syst. 2025** paper, later SIGMETRICS 2026 presentation—not a 2026 full conference paper).
- **Benchmarking & Systems Analysis:** TritonGym (ICML 2026, real compiled/executed Triton kernel agent evaluation) and XProf (MLSys 2026, production OpenXLA profiler). KernelFoundry/TritonGym are kernel-generation tools/benchmarks, not end-to-end LLM Serving speedup claims; XProf and Triton-Sanitizer are broadly applicable tooling exceptions, and video/DiT entries are adjacent inference.

**Explicit metadata corrections / no duplicate admissions:** Imported `RagInfer` is the formally published **TeleRAG (MLSys 2026)** and already has a canonical Runtime entry; imported `TokenBlend` has not been promoted while its relationship to the existing TokenWeave is unresolved. **PF-LLM (ASPLOS 2026 Best Paper) is excluded** despite the award: its LLM generates prefetch hints for general CPU workloads and its key evaluation uses SPEC/ChampSim rather than optimizing an LLM inference path. MixNet (SIGCOMM 2025) targets MoE **training**, not inference. SIGMETRICS 2026 proceedings contain extended abstracts which must not be mistaken for full papers. Generic multi-tenant GPU scheduling and simulated-only architecture claims remain for later evidence review.

**Audit to follow:** Reopen these 10 in a later pass for baseline fairness, production versus simulator split, hardware dependencies, working artifact and explanatory value. Remove entries with incremental mechanisms, weak real-world evidence or no lasting inference-system importance even though official publication identity is established. The published count is provisional, not a quota or a mark of independent reproduction.

## High-priority historical source sweep — 50 reviewed records (2026-10-18)

Individually screened the **50 priority-3 records** from the earlier 1,003-entry candidate ledger. The review outcomes: **6 new source-qualified, provisional canonical admissions**, **4 already-catalogued titles/aliases**, **9 excluded as outside LLM inference-system scope**, and **31 held pending stronger source/experimental/identity verification**. These counts sum to 50, and the admitted items lift the eight-topic total from 502 to **508** on this stacked branch. Do not conflate source/abstract evaluation review with method-level reproduction.

New: Coruscant (MICRO 2025, executed GPU sparse kernel; end-to-end artifact unfinished), MX+ (MICRO 2025, GPU microscaling inference execution), Characterizing Mobile SoC (SOSP 2025, real mobile GPU/NPU profiling/co-execution), PROMPTS (MLSys 2026 Industry Track, production profiling-driven LLM sharding proposals), Agentic Operator Generation for ML ASICs/TritorX (MLSys 2026, real MTIA correctness/coverage rather than serving-speed claims), and Understanding Inference Scaling (ISCA 2026 Industry Track, actual GPU-cluster profiling).

Already catalogued: **StriaTrace** (OSDI 2026), **Tetris** (ISCA 2026), **FlashInfer-Bench** (MLSys 2026), and **FarSkip-Collective** (MLSys 2026; already canonical under MoE). Historical entry #399 mislabeled FlashInfer-Bench as “LLMInfer-Bench”; it was **not readmitted**. The prior entry #457's plural “FarSkip-Collectives” is corrected to formal singular “FarSkip-Collective”. Historical #362 “H2-LLM” omitted “Low-Batch” from the official ISCA 2025 title; public DSE artifact alone does not demonstrate physical deployment. Historical #713 *Kelle* was mislabeled MICRO 2026, but is formally **MICRO 2025**; its new-hardware efficiency gains must not be represented as physical production measurements. Historical #412 *TokenBlend* has unresolved independent paper identity relative to existing TokenWeave: do not conflate or double count them without an independently verified primary source.

Evidence boundary: the 31 pending items include simulated PIM/CIM/systolic architectures, MICRO 2026 program entries, MLSys virtual-poster-only references and 2026 ISCA entries whose measured physical system gains were not established in this screening. The nine out-of-scope items are generic CPU prefetching, RTL PPA prediction, training-first FP8 MoE, agent semantic storage rather than execution, agent security, safety testing, LLM development/training cluster telemetry, RL training and federated-model attribution. “Pending evidence” does not mean technically bad. The complete source-indexed 50-row disposition is delivered as a separate artifact, not committed as a second internal database. Eight-topic schema, one canonical entry per paper and no crawler/automation remain unchanged.

## Priority follow-up: previously unresolved hardware/serving evidence (2026-10-18)

Six more entries were admitted provisionally after source-specific checks, raising the stacked branch's canonical count from **508 to 514**. Three are from the earlier 31 high-priority evidence holdouts: ConServe (ISCA 2026, contiguity-preserving virtual KV allocator implemented using CUDA VMM), DynoPipe (ISCA 2026, dynamically shifting edge/cloud pipeline boundaries), and XtraMAC (ISCA 2026, source-released FPGA MAC RTL plus real Alveo U55C measurements). Another three came from the previously unreviewed medium-priority pool: LILo (HPCA 2026, real Xeon IAA/AMX execution and public replication artifact), *Multiplexed Heterogeneous LLM Serving via Stage-Aligned Parallelism* / ParaFlex (SoCC 2025), and throttLL’eM (HPCA 2025, serving-aware GPU energy/SLO control).

**Evaluation distinctions:** XtraMAC's FPGA logic measurements and open RTL do not validate modeled full-LLM speedups on hypothetical larger FPGA arrays. LILo requires Intel IAA and large CPU memory/storage resources, unlike ordinary GPU inference. ParaFlex's small physical experiments do not independently verify its larger simulated deployment results. DynoPipe's real-edge-vs-simulation experimental split has not yet received a full-method audit. Other unsettled architecture papers remain pending rather than rejected: publication at ISCA/MICRO/ASPLOS does not imply physical manufactured silicon or transferable serving-speed benefits. The new rows are primary-source/evidence screened, **not independently reproduced**.

The source-indexed follow-up ledger is kept as a separate review artifact, not as a second structured database in the public repository. No script, crawler, benchmark claim, or automatic admission process is introduced. One canonical home per paper remains mandatory.

## Second venue/evidence-driven historical sweep (2026-10-18)

Twelve individually verified titles from the previously pending 1,003-record ledger have one newly proposed canonical entry each; the stacked branch moves **514 → 526** topic entries. Formal venue/year and primary publication links were checked alongside a distinctive inference execution mechanism or a narrow, explicitly labeled GPU/compiler tooling dependency. This is a fast admission pending later methodological/audit pruning, **not** independent reproduction.

- **KV & Context:** SwiftKV (*EMNLP 2025*, source had erroneous 2026 label; implementation and vLLM E2E), MatKV (*ICDE 2026*, physical GPU/SSD RAG materialization), SpecCache (*ACL 2026*, approximate deep-feature guided RAG KV reuse), UniCache (*POMACS 2026* full journal article; SIGMETRICS 2026 presentation, vLLM control-plane **trace simulator** with a limited GPU demo). The last paper's simulated cache-hit/latency benefits must not be labeled independently measured production goodput.
- **MoE:** SERE (*ICLR 2026*, vLLM/CUDA expert re-routing that intentionally changes selected expert execution and has quality tradeoffs); LayerScope (*ICS 2026*, ordinary CPU/GPU memory-offloaded MoE activation prediction + cross-layer prefetch and async I/O).
- **Runtime:** LithOS (*SOSP 2025*, LLM-containing GPU co-location experiments; general-purpose Rust GPU OS/TPC kernel atomization), dLLM-Serve (*ICS 2026*, measured diffusion LLM serving on NVIDIA RTX 4090/L40S), HEXGEN-FLOW (*ICDE 2026*, task-level scheduling for agentic Text-to-SQL on heterogeneous GPU systems). LithOS is a foundational GPU-scheduler adjacency, not a claim of LLM-specialized kernel or Serving algorithms.
- **Kernel/compiler tooling:** QiMeng-Xpiler (*OSDI 2025*, multi-ISA transcompilation with real target runtimes and an author-run evaluation artifact); KernelCraft (*ICML 2026*, agent-generated hardware-specific low-level kernels with **AMD NPU hardware plus PLENA simulator / Coral RTL**, not uniformly native silicon). KernelCraft's standalone reproduction code was labeled forthcoming in inspected materials; do not assert an available end-to-end benchmark harness.
- **GPU execution state:** GCR / *GPU Checkpoint/Restore Made Fast and Lightweight* (*FAST 2026*, Distinguished Artifact and open vLLM evaluation; generic GPU checkpoint with shadow execution, not an inference-specific KV mechanism). Classified in Distributed & Disaggregated Serving as a narrow state-mobility prerequisite, rather than misleadingly describing it as a disaggregated LLM service deployment.

**Alias reconciliation:** original #986 THETA is already catalogued by its final ICML 2026 title *Threshold-Based Exclusive Batching for LLM Inference*. Original #451 CRAFT uses an older arXiv title; the actual MLSys 2026 paper *CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving* already appears once under MoE. Neither source is counted twice. The original #835 SwiftKV was mistakenly labeled EMNLP 2026; ACL Anthology proves its formal publication is **EMNLP 2025**. Source #920 Pittacus may refer to renamed SageServe and remains pending complete full-publication identity verification; program-only 2026 SIGMETRICS abstracts are not automatically full papers.

**Limitations:** Source identities, mechanisms and paper-stated experimental settings were checked; the 12 additions have not received an independent full-baseline audit, nor do author artifacts guarantee easy reproduction on Ascend/Huawei NPUs. Public topic pages still constitute the sole canonical catalog; the detailed source-index decision ledger remains a separate deliverable outside this repository.

## Historical serving-core follow-up: nine source-verified admissions (2026-10-18)

Nine previously pending records from the user-supplied 1,003-paper JSONL received formal publication identity and mechanism/author-reported experiment checks, then one canonical Markdown row each. The stacked topic library moves **526 → 535**. These are fast, provisional admissions requiring a later experimental-methods pruning pass, not independent performance replications. The original 480 unreviewed-primary-source pool falls to **471**, while older pending evidence/identity items are unchanged.

**Runtime & Scheduling (5):** TurboTransformers (PPoPP 2021) is a **historical Transformer/BERT-era** online GPU serving prerequisite with smart batching, a DP batch scheduler, and a published Tencent implementation, **not** a modern autoregressive LLM-serving claim. MemSpec was mislabeled *PLDI 2026* in the import: its actual full-paper venue is **LCTES 2026** (PLDI co-located); its edge speculative-draft residency/scheduling is tested on Jetson Orin Nano. Omnia's formal HPDC 2026 full title is *Omnia: Efficient RAG Serving through Speculative Scheduling* (adds “Efficient”). STAR (HPDC 2026) uses output-length prediction and decode-phase rescheduling to control latency/goodput under long decode imbalance. PKAS (HPDC 2026) is *Predictive KVCache-Aware Scheduling for Faster LLM and Transformer Inferences* and avoids future KV exhaustion/preemption by predicted admission; not merely a cache-eviction heuristic.

**KV Cache & Context Memory (1):** *From Prefix Cache to Fusion RAG Cache* (Proc. ACM Manag. Data, SIGMOD 2026) adds cross-chunk context at materialization time and selective online KV recomputation; quality-vs-latency tradeoffs remain part of the mechanism and must be checked together.

**Distributed & Disaggregated Serving (2):** PhoenixOS (SOSP 2025) contributes OS-level *concurrent* GPU checkpoint/restore using speculative access tracking with runtime validation; it has an author CUDA artifact and Llama2 checkpoint experiments. Although it shares the generic GPU C/R problem space with GCR (FAST 2026), the central mechanisms differ (validated speculation versus low-overhead CPU shadow execution/data path); neither is falsely labeled as an independent LLM-specific disaggregated serving system. MixServe (ICDCS 2026) selects mixed TP/EP and overlaps intra-node AllReduce with inter-node All-to-All for MoE inference, with paper-reported physical multi-GPU execution.

**Kernels & Compilers (1):** FlashServe (ICDCS 2026) is formally titled *FlashServe: Adaptive Kernel Provision for Quantized LLM Serving*, **not** the import's “Dynamic GEMM Kernel Provision”; batch-sensitive quantized kernels are selected with switching-cost models and overlapped asynchronous switching. Its original authors' benchmarks are not replicated and artifact identity should not be inferred from unrelated same-name GitHub repositories.

**Withheld candidates reviewed but not promoted:** Insum (ASPLOS 2026) is a credible general-purpose sparse GPU compiler yet its evaluated workloads do not clearly pass this collection's narrow LLM-inference-specific gate; WISP (SIGMETRICS 2026) has documented analytic/numerical distributed speculative-serving results, but the extent of measured physical edge/server evaluation is not established here. Program/accepted-title-only 2026 listings and generic serverless-inference systems likewise do not automatically meet this admission boundary. Missing evidence does not mean poor research quality.

All rows were checked against existing topic titles/links before insertion. One primary mechanism category per paper. The source-index evidence decisions are kept as separate private/user-delivered artifacts, not a machine-generated secondary catalog committed into the public repository.

## Rapid evidence-qualified historical sweep — seven additions (2026-10-18)

Seven **previously unresolved** source-index records (#138, #232, #322, #384, #459, #475, #476) were compared against publisher records, confirmed as new canonical identities and given one mechanism-home each. This is a rapid **primary-publication / mechanism / author-reported evaluation** intake, not a reproduction or a comprehensive full-methodology audit. The stacked branch now has **542** topic entries (previously 535).

- **KV:** KV Cache Transform Coding / KVTC (ICLR 2026) performs transform + quantization + entropy coding for stored KV; its large storage compression ratios are **not** directly measured inference goodput gains. PM-KVQ (ICLR 2026) uses progressive bitwidth reduction, sensitivity-aware per-block allocation and interpolation-based long-CoT calibration, with public code and performance/quality comparisons.
- **Decoding:** CDLM (MLSys 2026) jointly trains for fewer diffusion refinement steps and blockwise causal KV cache compatibility. Its speedup requires model training/fine-tuning, unlike drop-in inference runtime changes.
- **MoE:** Libra (ICLR 2026) forecasts expert load and overlaps routing overhead, evaluated on a real 8×H200 deployment with an author artifact.
- **Historical kernel library:** LightSeq (NAACL **2021 Industry Track**) was evaluated on machine translation / early transformer inference. It is a distinct historical kernel/runtime foundation, not a current autoregressive LLM serving benchmark.
- **Adjacent multimodal inference:** DiffServe (MLSys 2025) optimizes query-aware cascades for text-to-image, while ScaleFusion (MLSys 2025) pipelines distributed spatial-temporal attention for long video diffusion on physical 32×A100. Neither is attributed text LLM deployment results.

**Existing canonical paper identities (no duplicate rows):** Original #47 BEAM (MLSys 2026), #55 SchedFlow → DynaFlow (MLSys 2026 publisher name), #56 EcoServe (OSDI 2026), #127 RDMA Point-to-Point → fabric-lib (MLSys 2026 publisher name), and #230 RefreshKV (ACL 2025). These imported records already had previous final dispositions in the user's JSONL; this sweep merely revalidated the alias links and did not inflate processed counts.

**Scope hold:** SkyServe (EuroSys 2025) has real published systems research and deployment results but is general AI cross-cloud spot-instance placement. Its prior **scope-excluded** status is preserved as the technical mechanism is not specialized for LLM inference; an excellent paper is not automatically a fit for this particular bibliography. Hardware-simulation-only and generalized ASIC cost-prediction papers remain held for future evidence review.

Topic Markdown tables stay the one canonical public catalog. Separate dated disposition tracking remains outside the repository. All claims are from published/author evidence, not independently repeated.

## 98-entry historical review wave: verified admissions vs scope screens (2026-10-18)

The user requested **at least 50 distinct papers examined in one wave**. This wave produces **98 individually source-indexed, non-overlapping decisions** in a separate, downloadable record-level ledger rather than an internal parallel repository catalog:

- **13 fast provisional admissions**: six KV/context papers (TRIM-KV / *Cache What Lasts*, ReST-KV, ChanMix, ForesightKV, ProphetKV, and *CriticalKV*), six speculative/diffusion decoding papers (PARD, FlashDLM, ES-dLLM, AdaBlock-dLLM, *Learning To Draft*, *Not-a-Bandit*), and one MoE execution paper (*Opportunistic Expert Activation*). Each identity and mechanism was checked against its final **ICLR or ICML 2026** formal publisher record, with code/evaluation assertions kept as authors' claims. Their canonical rows increase the stacked bibliography from **542 to 555**.
- **55 explicit topic-mechanism exclusions**, each with an individual reason in the decision ledger. This is **scope triage from title/research target plus selective publisher cross-checks**, *not* a claim of 55 independently audited full papers or that their research is bad. Major exclusion classes: training-only LLM distributed systems, generic DL training and federated learning, ANN/vector database engines (Milvus, SPFresh, CAGRA, LEANN), security/unlearning/side channels, and unrelated model/infrastructure work. Training-first titles with real 256×H100 results (e.g. FreeScale) remain legitimately good systems research but are not evidence of LLM inference execution.
- **30 technical/evidence holds**; these underwent first-pass problem/mechanism/evidence-gap review and remain **unresolved**. This includes REPA/LongSight GPU-PIM/CEM, MCBP/DFVG/M2XFP/ORCHES, wafer-scale WSC-LLM and H²-LLM, in-flash AiF/Lincoln, provisional diffusion-LLM/model work and preprints. Publication at ISCA/ASPLOS/MICRO alone does not establish measured physical silicon or serving throughput; do not convert these 30 into final rejects.
- **Formal title correction**: imported 'Optimizing KV Cache Eviction from an Output Perturbation Perspective' is the **ICML 2026 CriticalKV** paper. Its official PMLR 306 URL is in the row.

**Evidence-level boundary:** The 13 admission records have formal primary publisher pages checked; no results independently reproduced. The 55 exclusions are completed editorial **scope** decisions only, and the 30 holds are incomplete evidence decisions. Thus 98 *records were explicitly handled*, but only 68 had a final directional disposition (13+55). Do not claim 98 independent full-text primary-source evaluations. See the separate 98-line JSONL receipts and full 1,003-record ledger outside this repository for exact source_index, reason and audit depth.

Methods/quality flags for later pruning: ForesightKV and CriticalKV primarily demonstrate accuracy/cache-reconstruction effects, not necessarily live-serving goodput; PARD uses trained draft adaptation; FlashDLM's guided auxiliary AR model must be included in runtime cost; OEA re-routing is **not** perfectly output preserving and may trade off model quality. Priority for a second pass: real-device/paper Artifact, fair throughput/TTFT/TPOT metrics, accuracy constraints, version-pinned reference builds and research value beyond adjacent algorithm baselines.

No JSONL, scraper, auto-approval workflow or shadow metadata source is committed into the eight-topic repository. One canonical home per paper remains mandatory.

## Large 200-record historical triage and source-checked intake (2026-10-18)

This wave handles **200 distinct original source_index records** in the maintainer's separate historical 1,003-entry audit ledger, including:
- **22 primary-publisher-screened provisional canonical admissions**: checked exact archival identity, source-described mechanism and author-reported execution/evaluation, then placed in one of seven existing topic pages. Includes PipeThreader (OSDI 2025), ApproxMLIR, Dataflow Is All You Need, ExecuTorch, sparse activation and db-SP (MLSys 2026); EpiCache, LRAgent, DHSA, SOLO, PuzzleMoE, SALE, STAR-KV, Sketch&Walk, SANTA and Token Sparse Attention (ICML 2026); QIGen (CGO 2026), STOF and Quantix (PPoPP 2026), TurboInfer, ShadowNPU and TimelyLLM (MobiSys 2026).
- **1 verified already-canonical alias**: old `Search Your NVFP4 Scales!` is the formal MLSys 2026 paper *Search Your Block Floating Point Scales!*; no duplicate row.
- **50 editorial scope exclusions**, individually source-indexed. These are *title/research-target or abstract-level scope decisions*, not an assertion that all 50 had full-text experimental review or that their research lacks merit. They chiefly cover training-only infrastructure, generic agents/optimizer SDKs, generic cloud/Kubernetes and non-LLM inference, security and survey/position/economics.
- **127 first-pass evidence holds**, individually indexed with subject-appropriate reasons (physical accelerator verification; unresolved preprint venue/artifact; real-SLO/goodput versus simulator; novelty/quality and full-paper details). They remain unresolved, not reclassified as excluded. They received a **title/metadata/technical-target pass**, not 127 primary paper full-text audits.

Therefore 200 distinct records have documented reviews, **73 have final directional dispositions** and 127 do not. Historical estimate of unresolved candidate records drops **433 → 360** (22 admitted + 1 alias + 50 scope exclusions). The canonical bibliography on this stacked PR branch grows **555 → 577**; `main` is not updated by this branch. Full record-level audit and 1,003-row ledger are delivered as separate user artifacts rather than committed as a second source of truth.

### Mandatory methodology boundaries
- Runtime-relevant real-device execution: LRAgent has source-reported KV-sharing TTFT/throughput, STAR-KV uses Triton and reports generation throughput, Quantix benchmarks L40, ShadowNPU uses Qualcomm Hexagon mobile NPU, TurboInfer uses actual phones, TimelyLLM uses physical-I/O-constrained agent workloads, and PipeThreader uses actual GPU kernels. **None of these reported results were independently reproduced here.**
- *ExecuTorch* and *ApproxMLIR* are consciously labeled reusable ML deployment/compiler tooling rather than LLM-specific P/D-serving optimizers. *db-SP* is for DiT-based visual generation, not text LLM. *Dataflow Is All You Need* runs on SambaNova's proprietary RDU, so its 16-chip comparative costs and roofline claims should not be generalized to GPUs/Ascend without reproducing them.
- Sparse methods SAL(E), Sketch&Walk, SANTA, Token Sparse Attention and DHSA can measure attention-kernel speed separately from full forward-pass speed. Ablation must include sparse-mask discovery, quality loss and memory overhead. MoE sparse activation and PuzzleMoE explicitly trade sparsity/weight size against accuracy.
- Original publisher identities, titles and venue years were checked before admission. General TPU-training CATWILD, optimizer research and LLM codegen are scoped out without being judged bad systems science. The former import's `Search Your NVFP4 Scales!` is explicitly a previously catalogued alias.
- Fast admission never waives a later independent methodology audit (fair baselines, kernel-level vs serving-level claims, hardware provenance, official code version and actual personal reading value). Remove weak entries after that audit, even if they passed venue/source screening.

## Second pass on ten previously held papers (2026-10-18)

Revisited **ten records selected out of the preceding 127 technical/evidence holds** with authoritative publisher and mechanism evidence: **seven new provisional admissions and three explicit editorial scope exclusions**. These are **not ten additional distinct source_index records** beyond the prior 200-record audit, so cumulative distinct records screened remains **200**, with final outcomes **73 → 83**, unresolved prior pool **360 → 350**, and still-technical-hold records in that wave **127 → 117**. The stacked canonical topic inventory grows **577 → 584**. Details and source-index dispositions are in the external private review ledger, not a repo-local JSON database.

- **Runtime (+3):** *AgenticCache* (MLSys 2026) avoids repeated embodied-agent LLM planning requests by caching plan transitions plus asynchronous refresh; its reduced latency was measured largely in simulation, and it is **not** LLM KV caching. *Faro* and *Bless* (both EuroSys 2025) are explicitly labeled **general ML inference Autoscaling** and **general GPU Quota/Bubble Scheduling**, respectively. They are narrow but substantial foundational systems exceptions; they do not claim optimized long-context text LLM serving measurements.
- **Benchmark (+1):** *Scaling Up, Speeding Up* (ICLR 2026) benchmarks speculative decoding under Best-of-N/multiple reasoning traces with consistent experimental controls. It does **not** propose a new Serving Runtime. Formal paper status was checked; OpenReview may present a browser challenge.
- **MoE (+1):** *Dynamo-MoE* (HPDC 2026) dynamically manages Expert imbalance through load-aware parallelization and on-demand placement; author code is advertised. Hardware scaling and strong baseline fairness remain for later full-paper verification.
- **KV (+1):** *Scaling Attention Beyond GPUs for LLM Inference* (HPDC 2026) combines recent dense GPU Attention with salient CPU-resident sparse Attention, fusing via LogSumExp to address host/device bandwidth costs on commodity systems.
- **Decoding (+1):** *HeteroSpec* (ACL 2026) adjusts speculative candidate verification budgets to entropy/heterogeneity, with the paper reporting exact-distribution acceleration; it still requires independent runtime/SLO replication.

**Three scoped-out papers after source inspection:** *RAT+* (ICML 2026) primarily changes/pretrains model architecture for sparse inference; *SALAAD* (ICML 2026) induces sparse/low-rank structures via ADMM during training; and *StreamBox* (USENIX ATC 2024) is an excellent but generic DNN serverless GPU Sandbox, without an identifiable LLM-specific KV/Decode/serving optimization that justifies another adjacent runtime entry. These scope exclusions **are not statements of weak paper quality**.

All above performance findings are author-reported. The six previously untouched PRs and this PR remain stacked and unmerged. Later independent review must separate empirical physical devices, simulators, author-provided artifacts, and actual end-to-end TTFT/TPOT/Goodput.

## ACL/COLM 2026 formal-evidence second pass (2026-10-18)

Rechecked **six previously held source records from the same 200-record review wave**; **five** now admitted provisionally and **one** editorially excluded. **Do not add six to the unique historical records screened**. The first 200 remain the same 200; final decisions **83 → 89**, evidence holds **117 → 111**, historical unresolved candidate count **350 → 344**, and canonical topic inventory **584 → 589** on the latest stacked branch.

- **VecInfer** (ACL 2026): smooth/Hadamard transform addresses KV vector-quantization outliers with a **fused CUDA dequantization compute kernel**; original paper reports true 196K-context Llama GPU inference latency, but was not independently replicated.
- **ContrastKV** (ACL 2026): contrastive semantic/structure fusion for query-agnostic KV eviction; paper reports decoder latency and multi-query answer fidelity. No independently verified vLLM deployment.
- **ASPIRE** (COLM 2026): unified mixed batched self-speculation, per-request asynchronous draft-verify scheduler, intra-draft layer refresh. **COLM official accepted paper list** verifies identity and [authors' public executable research artifact](https://github.com/Amir-zsh/ASPIRE) logs per-step runtimes, generated-token hashes, and resolved benchmark configurations. Official arXiv version is linked in its canonical row; test results are author reported.
- **UniSpec** (ACL 2026): hardware-calibrated n-gram/tree speculative decoding, public code/benchmarks according to archival abstract; output-distribution/quality invariance must be independently checked.
- **TokenTiming** (ACL 2026): dynamic token-sequence alignment allows Draft/Target models with different tokenizers, without retraining; the Tokenization/DTW latency overhead needs profiling.
- **Excluded from the narrow runtime catalog:** **PDTrim** (ACL 2026), a genuine model *block-pruning/distillation* method tuned to Prefill/Decode disaggregation. It changes model structure rather than exposing a reusable dispatch, KV materialization, memory management or serving runtime mechanism. Exclusion is about library boundaries, not academic merit.

Each original source_index, final URL, mechanism boundary and verdict is separately documented in the 6-record evidence receipt and 1,003-row ledger; these are **not committed to the public topic bibliography as competing structured catalogs**. Scope checks from publisher abstracts do not replace full-paper inspection or physical-hardware reproduction.

## Archival-identity sweep: 202 distinct historical records (2026-10-18)

After PR #41, we **reconciled all 1,003 candidate statuses across legacy overlays**. Previous summaries described 344 unresolved by omitting **seven `withheld_after_source_review` records**; under the explicit conservative rule that those still need a final disposition, the true pre-wave count is **351**. This sweep screened **202 distinct original source_index records**, made **24 publisher-checked provisional canonical admissions**, **6 source/target-specific scope exclusions** and **172 metadata/technical-target reviews that remain pending**. Final directional decisions rise **652 → 682**; unresolved count falls **351 → 321**. The canonical topic library grows **589 → 613** on this stacked branch (not main).

### 24 publisher-qualified titles
- **Decoding and adjacent image/VLM generation (+9):** Dovetail, QSpec (both **EMNLP 2025**, historical EMNLP 2026 venue labels corrected), LongSpec, SSSD, HCSpec, Jakiro, Focus-dLLM, DREAM-S (ACL 2026), and Multi-Scale Local Speculative Decoding for Image Generation (CVPR 2026). Entries distinguish exact/output-preserving Draft/Verify and trained Draft/visual-adjacent methods; no 2026 ACL result is misattributed to text-only runtime where it uses VLM/image generation.
- **KV Cache and multimodal memory (+6):** HeteroCache, HybridKV, HERMES, AdapShot (ACL 2026); ElastKV/KV Cache Reuse for Elastic LLM Inference and Dual-Blade NVMe Offload (ICDCS 2026). Cache retrieval/placement and physical I/O are distinguished from quality-only cache retention; HERMES is explicitly streaming video, not text-only.
- **Runtime (+3):** FLARE (ACL 2026, resource-aware heterogeneous model routing); PEACE (IPDPS 2026, mixed-length Prefill preemption and public replay/ablation code); Quicktopia (CCGrid 2026, measured iteration-level GPU DVFS).
- **Distributed/edge (+4):** EdgeFlow KV Migration, EdgeTP hetero edge tensor parallelism, and ShadowLLM hot standby (ICDCS 2026), plus Euro-Par 2026 Layer-Wise CPU–GPU Scheduling for models exceeding consumer GPU memory.
- **MoE (+1):** *Efficient MoE Inference on Single Consumer-grade GPU with Dynamic Expert Caching* (IPDPS 2026); historical title omitted 'Consumer-grade'.
- **Benchmarking (+1):** *The Pitfalls of KV Cache Compression* (ACL 2026) demonstrates benchmark-specific instruction-following degradation and unsafe semantic changes under popular KV compression policies. This is a critical counterexample/quality audit, not a new efficiency algorithm.

**Evidence standards:** Each of the 24 admissions was checked against a definitive publisher/Anthology/IEEE/Springer/CVF publication page or primary author-linked reproduction source, and source-described mechanisms and evaluation classes were identified; **none** were independently rebuilt or benchmarked. PEACE's experiment source is https://github.com/Zeyu-ZEYU/PEACE, ShadowLLM authors report Jetson/phone testbed, HERMES authors publish https://github.com/haowei-freesky/HERMES. Results from adjacent VLM/image generation must not be presented as improvements to autoregressive text LLM Serving.

**Six explicit exclusions:** secure encrypted PowerSoftmax; EcoTune (officially **EMNLP 2025**, optimization of sampling hyperparameters rather than system execution); repetition-penalty numerical anomaly; BridgeLoRA (officially edge **Fine-Tuning**, not the historical erroneous 'Inference'); T-TAMER (general synthetic/vision/NLP model-cascade theoretical approximation rather than LLM serving implementation); generic serverless GPU inference workflows without an identifiable LLM-specific mechanism. These are **scope decisions**, not a judgment of scientific merit.

**172 remaining holds:** covered by title/imported-venue/technical-goal analysis only. Formal primary papers, physical accelerator provenance, full-paper methodology and Artifact were **not** checked for each one; their original uncertainty is retained in the exported 202-source-index JSONL. The updated full 1,003-entry private ledger includes `current_disposition_20261018` for every record and reconciles the old seven held records. We do not commit that ledger or another metadata corpus into this one-canonical-row-per-paper Markdown repository.

Further editing may *remove* provisional entries after fair workload/metrics, end-to-end physical-device benchmarks, implementation effort and reading merit have been independently assessed.

## Second evidence upgrade on four previously held records (2026-10-18)

The *same 202 distinct source-index records* from the immediately preceding historical sweep received a focused full-publication/real-hardware recheck. Four held records were upgraded; this does **not** enlarge the number of unique source records screened. On the stacked branch: **28 publisher/mechanism/experiment screened provisional admissions**, **6 explicit scope exclusions**, **168 metadata/technical-target holds** = **202**; 34 final directional decisions. Historical strictly unresolved **351 → 317**, correcting the previous temporary 321 tally. Canonical entries move **613 → 617**. All published speedups are author-reported, not independently reproduced.

- **#940 Understanding and Improving Communication Performance in Multi-node LLM Inference** (*CAIS 2026*, doi:10.1145/3786335.3813165): real multi-node HPC Slingshot/InfiniBand GPU evaluation and Llama 3.1 405B TP Decode, NVSHMEM NVRAR small-message hierarchical AllReduce with paper-described vLLM/YALIS integration and author-code availability. This is primarily a **real-model distributed serving/collective** optimization rather than abstract collective simulation.
- **#924 Beyond Throughput: Performance and Energy Insights of LLM Inference Across AI Accelerators** (*IPDPS 2026*, doi:10.1109/IPDPS65963.2026.00083): author artifact at https://github.com/SPEAR-UIC/IPDPS26-LLM-Energy provides runnable vLLM single/multi-GPU and MoE parallel evaluation plus power-measurement scripts across Nvidia, AMD and Intel GPU infrastructures. Cerebras and SambaNova benchmark components use vendor-specific inference-server client templates, not fully portable local implementations.
- **#973 PTStore (Prefix Tensor Store)** (*Euro-Par **2026***, authors' https://arxiv.org/abs/2607.22648 and official Springer proceedings): decentralized prefix KV cache replication/placement inspired by CDN consistency and hotspots, supporting long-question-answering LLM workloads; large reported throughput uplift remains an author claim pending an independent network and strong-prefix-baseline audit.
- **#974 Performance Characterization and Optimization of LLM Inference on Tenstorrent AI Accelerators** (*Euro-Par **2026***, https://doi.org/10.1007/978-3-032-35251-4_32): real Tenstorrent Wormhole/Tensix decode profiling and the **Chip-Pipe** pipeline scheduling alternative to TP, physical throughput with four models. **Date distinction:** Euro-Par meeting August 2026; the corresponding Springer LNCS 16782 title is formally listed in book metadata as published **2027**. Canonical table uses meeting year 2026 with imprint noted, not a fabricated 2026 publisher date.

**High-priority evidence conflict retained as pending #933:** *Latency-SLO-Aware Memory Offloading for Large Language Model Inference* (ICS 2026, https://doi.org/10.1145/3797905.3807874): the Michigan Tech official university proceedings archive describes a system **NovaServe** optimizing *weight offload ratio plus attention placement* and reports **2.3x**, whereas an authors' university lab page on the related manuscript describes **Select-N** optimizing per-layer *offloading interval* and reports **1.85x**. The title and overlapping authors obscure materially different technical/measured claims; without a publisher camera-ready PDF that resolves the conflict, do not admit either misleading version or claim equal paper identity. This is not a judgment about method quality.

The complete 202-record revised decision file and 1,003-row updated ledger are separate user artifacts outside this public canonical Markdown bibliography. Run full experiment/quality audits later and remove weak provisional papers; do not add second JSONL source-of-truth or automatically publish new candidates.

## Final three additional historical evidence upgrades (2026-10-18)

Within the **same 202 unique historical records screened earlier in this PR**, three *previously held* entries received official IEEE/ACM publisher-source and real-hardware evidence checks; they must **not be counted as three more distinct records**. Two classified as Distributed Serving, one Runtime; the canonical stacked library now contains **620 entries**. Final per-record tally in the 202-record wave: **31 provisional primary-source admissions**, **6 scope exclusions**, **165 metadata/technical-target holds**; **37 final directional decisions**, with **314/1,003** historical records unresolved under the conservative denominator that includes seven older `withheld_after_source_review` entries. Updated 202-row and 1,003-row receipts remain external user artifacts only, not part of the Markdown bibliography.

- **#900 MIDAS** ([ICASSP 2026](https://doi.org/10.1109/ICASSP55912.2026.11461518)): NVLink-based cross-GPU borrowing of otherwise idle GPU memory for KV, with revocation/reallocation during bursty coscheduled tenants. **Measured on an 8×A100 GPU cluster**; no automatic claim that cross-GPU network occupancy and reliability are free.
- **#913 LLM-PILOT** ([CCGrid 2026](https://doi.org/10.1109/CCGRID68966.2026.00023), [author-hosted paper](https://discos.sogang.ac.kr/file/2026/intl_conf/CCGRID_2026_J_Kim.pdf)): calibrated analytical planning for public-cloud VM type and hybrid KV/Attention Offload selection under latency/throughput SLOs; **actual AWS experiment**, separate measured cases from modeled configuration sweep.
- **#936 PPPR / Phase-aware Peak Power Reduction for Minimizing the Capital Expense of LLM Inference** ([ICS 2026](https://doi.org/10.1145/3797905.3815788)): uses the phase-specific Prefill power spike vs Decode low steady power to coordinate server **supercapacitors** and rack **UPS batteries** for datacenter power capacity. The source distinguishes **measured hardware peak-power reduction** from **trace-simulated CapEx/lifetime projections**; these should not be conflated with direct serving goodput improvements.

The following remain pending, with a concrete reason: #933 **NovaServe vs Select-N** same-title DOI discrepancy, #930 VoLLM verified IPDPS proceedings but insufficient inspectable baseline/full hardware detail, other physical/simulated hardware research. The publisher identity and real-system evidence in this wave remain author claims, not independent reproduction. Final acceptance still depends on later quality pruning and explanation value.

## Complete first-pass screening of all previously unresolved history (2026-10-18)

The maintainers requested **broad first-pass intake before deep paper-by-paper vetting**. Every one of the prior **314** historically nonfinal `source_index` records from the original 1,003-entry user-provided JSONL was screened **exactly once in this pass**. The full evidence receipts are delivered separately rather than committed as a second machine-generated metadata database.

| Scope outcome | Unique source records | Evidence threshold |
|---|---:|---|
| Fast, **provisional** canonical topic admission | **58** | Official archival paper page or official accepted-program/DBLP index; name + plausible inference execution mechanism, **no** independent artifact or physical-GPU performance reproduction |
| Editorial scope exclusion | **15** | Unambiguously generic DNN kernel/storage infrastructure, training/data creation, privacy/security, survey/perspective, or output-hyperparameter tuning; title/goal screen **not full-paper scientific ranking** |
| Screened but still **evidence pending** | **241** | Title, venue/imported identity and likely bottleneck classified; insufficient full paper, official publication or implementation/benchmark evidence to make a final directional decision |
| Total unique screened this pass | **314** | Exhaustive by distinct source_index, not exhaustive full-paper audits |

**Historical accounting:** Of 1,003 source records, **762** now have a directional admission/exclusion/alias decision; **241 remain unresolved for in-depth verification**. Every previously outstanding record nevertheless has an explicit first-pass category, rationale and next-evidence requirement in the external receipts. **Screening coverage is 314/314; final resolution is not 314/314.** Do not say that the 241 have been 'admitted', 'rejected', or 'independently verified'.

This stacked proposal expands the canonical Markdown bibliography **620 → 678** using one canonical topic per source-qualified provisional entry: 1 Kernel/compiler, 4 Quantization, 15 KV Memory, 14 Decoding, 5 MoE, 10 Runtime, 3 Distributed Serving and 6 Benchmarking. Topic headings/index and global unique-title/URL checks must pass before merging; `main` remains at its prior state unless the maintainer merges stacked PRs in order.

**Important distinction:** A PMLR/ACL Anthology/ICLR/CVF paper page is stronger identity evidence than an official conference **program**, and a DBLP proceedings *listing* is weaker evidence than actually inspecting the corresponding publisher full paper. Entries with only program/index evidence have an explicit note `快速准入（会议节目／索引）`. Even directly archived papers receive only `source/mechanism screen`, not a claim of stable, reproducible Serving Goodput/TTFT/TPOT or safe lossless execution. In the later method-level pass, remove any paper whose actual experimental value is weak or whose inference mechanism is marginal; do not invent device speedups.

A few consciously deferred examples: historical #933 NovaServe/Select-N disputed paper identity and conflicting reported results; #215 RAGBoost requires a confirmed archival MLSys identity despite an author preprint and code; #288 DefensiveKV has an ICLR source and open code but its direct paper/experiment identity was not populated in the import; novel GPU-PIM/NAND/chiplet/wafer-scale systems remain pending fabricated-versus-simulated hardware evidence. The nonadmitted records are not all scientifically low quality.

The repo remains **Markdown-only as its canonical reading library**, no crawler/automatic eligibility decision pipeline or separate JSONL catalogue has been committed. The downloadables contain (a) complete 314-row first-pass decision file, (b) complete reconciled 1,003-row status ledger, and (c) audit-ready report including all 241 outstanding evidence gaps.
