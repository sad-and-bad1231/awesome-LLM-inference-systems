# Curation policy

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
