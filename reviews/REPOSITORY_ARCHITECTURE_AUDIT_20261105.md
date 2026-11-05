# Repository architecture and editorial audit — 2026-11-05

**Baseline:** main at [6d4ff42](https://github.com/sad-and-bad1231/awesome-LLM-inference-systems/commit/6d4ff42f04f42feefc8b75fe0719ff9d6c819627). **Scope:** all 88 Markdown blobs in the non-truncated 94-object repository tree: 3 root, 10 topics, 50 organizations (including index), 1 communities, 2 frontiers and 22 reviews (including 4 archived notes). Reviewed file-level structure, heading/navigation, stated evidence boundaries, source/link presentation and category inventories. This is **not** a full re-reading of 854 primary papers, a link-availability crawl, or an independent reproduction of authors' numerical results.

## 1. Architecture verdict

**Keep the current layers:** foundational lineage on the homepage; **one canonical bibliography** in eight mechanism-specific topic pages; first-party organization pages; an execution-boundary open-source map and research-source crosswalk; seven non-canonical Frontier research questions; curation rules and dated review evidence. A paper should have one full canonical row. Model providers, academic affiliation, hardware target, agent workflow and Frontier topics are **cross-indexes**, not excuses to duplicate the bibliography.

The design is defensible, but navigation and source depth are less mature than the paper count suggests. The most important distinction is between **source-verified identity/claim attribution** and **independently measured performance**.

### Mechanical inventory checks

| Layer | Checked inventory | Audit result |
|---|---:|---|
| Foundations | 30 chronological milestones (2017–2026) | Count agrees with homepage; separate historical/reference reading path |
| Canonical bibliography | 854 rows / 8 classes / 44 directions | All eight paper rows and subgroup counts add up; no identical first-source URL across canonical rows detected |
| Company profiles | 19 China + 30 United States = 49 | All indexed standalone profiles present |
| Open-source execution projects | 76 entries: 24 engine, 11 orchestration, 9 KV/transfer, 23 kernel/compiler, 9 multimodal/backend | Five group totals add up |
| Named research-source additions | 12 November nodes + 10 November 5 nodes | **22 addendum nodes, not 22 distinct formally constituted labs** |
| Active research frontiers | 7 | Research cross-index only; no additional canonical paper rows |
| Reviews/archives | 22 files | Dated snapshots and HOLD/REMOVE dispositions preserved; archives are not live counts |

**Corpus composition (mechanical field scan):** 617 of the 854 topic rows have year **2026** (about 72%); 240 venue fields contain arXiv / preprint wording; and 323 distinct mechanism cells have fewer than 85 plain-text characters after stripping Markdown formatting. The last threshold is only a **navigation-density flag**, not a quality score: concise Chinese descriptions may be technically useful. However, a short mechanism description should not be mistaken for a complete hardware/workload/baseline/equivalence receipt. Prioritize source and evidence review on high-impact recent preprints, cross-domain exceptions and difficult replication claims instead of imposing a fixed page-length rule.

Exact first-source URL deduplication is a **syntactic screen**; DOI/arXiv/publisher aliases and semantically duplicated papers still require source-level checking.

## 2. Why these foundations?

The 30 are a selective **mechanism lineage**, not a ranking or a contemporary best-paper list. The roles are: Transformer and decoding prerequisites; iteration-level scheduling and selective batching (Orca); I/O-aware attention (FlashAttention family); KV memory virtualization and request reuse (PagedAttention, vAttention, Mooncake); speculative acceptance and verification (Blockwise, Speculative Decoding, Medusa, SpecInfer); goodput/SLO and phase separation (Sarathi-Serve, DistServe, Splitwise); production-scale orchestration, kernel engines and heterogeneous resources (Llumnix, FlashInfer, NanoFlow, Strata, Prism). Earlier papers explain the invariant, not an up-to-date benchmark.

**Risk:** a static thirty-paper table can be misread as the full history; 2026 representation is selective and the choice is editorial. Keep this as a starter map and route later innovations to the eight technical categories. Do not grow the foundation list merely to reward a famous institution or increase the count.

## 3. Eight mechanism classes: role and identified weaknesses

| Mechanism / rows | Why it is separate | Main editorial risk or next verification |
|---|---|---|
| Kernels & Compilers / **115**, six tracks | Changes executed operators, layout, lowering, code generation, fusion and data-movement efficiency | Hardware- or simulation-specific kernel claims can be misread as end-to-end gains; verify compiler/runtime integration and correctness; 18 rows contain KEEP_ADJACENT |
| KV Cache & Context Memory / **166**, six | KV residency, reuse, eviction, selection, transfer and virtual/physical page management | Largest category; compressive algorithms, cache policy and actual reusable Serving state must stay distinct. Verify workload traces and accuracy |
| Decoding Acceleration / **85**, five | Changes token proposal, tree/parallel verification, acceptance or non-autoregressive generation | New-model diffusion results are not same-model speculative wins; quality- and model-change tags must remain conspicuous |
| Quantization & Compression / **46**, six | Representation/precision choices and executable low-bit computation | Smaller count is not automatically a gap. Verify W/A/KV formats, actual device support, dequantization cost and quality at equal budgets |
| MoE & Sparse Execution / **75**, four | Expert routing, placement, offload and conditional computation | Sparse Attention and MoE are related by conditional work, but not identical; kernel-only sparse methods can overlap with Kernels or KV |
| Runtime & Scheduling / **151**, six | Batching, routing policy, priorities, preemption, fairness, request SLO, autoscaling decisions | P/D allocation and scheduling overlap with distributed substrate; distinguish *policy* from *physical data path* |
| Distributed & Disaggregated Serving / **134**, five | Parallelism, interconnect/KV transfer, phase/component separation, fleet and heterogeneous execution | Separate communication microbenchmarks from end-to-end Goodput; phase-splitting papers may also have scheduler policies |
| Benchmarking & Systems Analysis / **82**, six | Workloads, measurement, profiling, correctness, modeling and independent diagnosis | A benchmark of an adjacent task is not evidence for an optimization. Keep trace provenance, real/simulated and evaluation parity explicit |

Across these eight files, **83 row descriptions contain the label KEEP_ADJACENT** (literal text count, not 83 independently adjudicated decisions). This is a targeted scope-review queue, **not** evidence that 83 papers are invalid. Check each exceptional inclusion for the exact relevance to executable inference and whether the implementation/result is actually on the claimed serving path.

The topic index now records tie-break rules for KV vs quantization; kernels vs MoE; runtime vs distributed; decoding vs runtime; and benchmarks vs optimization.

## 4. Organizations: why this roster and how much detail?

**Selection unit = first-party evidence of inference execution**, not enterprise valuation or model API size. Four justified types exist: (a) model architectures with concrete compute/KV/expert implications, (b) engine/kernel/compiler/communication owners, (c) documented production Serving engineering, and (d) hardware/backend vendors with inspectable execution software. Industry labs and co-owned communities are credited explicitly; an API alone is not proof of hidden kernels or scheduling.

**Source-rich starting points:** DeepSeek, Google, Qwen/Alibaba, Tencent, Meta, Moonshot/Kimi and NVIDIA connect models to multiple execution components. **Mechanism-oriented operator evidence:** Meituan/LongCat, Ant Group, ByteDance, Huawei/Ascend, AMD, Cloudflare, Together AI and others offer specific pieces of deployment/runtime/communication, often with caveats. **Narrower public evidence:** for instance BentoML, Cambricon, Intel, Predibase, Groq and Asari AI have much shorter pages and/or fewer directly linkable sources. A short page may reflect a genuinely narrower public footprint; do **not** fabricate missing implementation details to equalize profile length.

**Structural debt:** the organization directory is a 49-profile China/US window rather than a global roster. Its long date-stamped update sections overshadow the current index. Model-version crosswalks and production claims age faster than source-code mechanism descriptions; renew identity checks rather than making a static vendor model registry.

**International watch, not immediate admission:** Mistral, for example, has first-party model/inference documentation but the older mistral-inference repository is archived; a credible execution-specific contribution should be established before adding an organization page. Other regions and vendor-neutral compiler/inference maintainers deserve source-led discovery instead of geographic quota filling.

## 5. Labs and open-source communities: why these sources?

**Open-source grouping is by executable boundary, not GitHub stars or nationality:**
1. Engines (vLLM, SGLang, TensorRT-LLM, DeepInfer, RTP-LLM, LightLLM, llama.cpp and hardware-specific runtimes) explain the token-step pipeline.
2. Cluster orchestration/routing projects explain fleet-level resource allocation rather than attention kernels.
3. KV/transport projects explain ownership, copies, cache and communication.
4. Kernels/DSLs/compilers explain device scheduling, verification and optimization.
5. Multimodal/backends explain streaming or alternate-accelerator execution contracts.

**Research sources are worth following when they repeatedly originate identifiable mechanisms or maintain artifacts**, not because the institution is famous. Distinct examples: Berkeley Sky (serving/distribution), Stanford Hazy/MAST (execution and agentic correctness), MIT Han (quantization/kernels), UW SyFI (serving engine/agent optimization), Tsinghua PACMAN and MADSys (compiler/runtime and heterogeneous MoE), CMU InfiniAI (program IR and serving), SJTU IPADS (systems source discovery), ETH SPCL (collectives and HPC context). The October and November addenda also contain **industrial engineering teams, maintainers and coauthored collaborations**: do not label all of them universities or independent labs.

**Main weakness:** research groups, industry research teams and OSS maintainers are intermixed in one long document. The 76-code-project section is navigable; the lab section is chronological rather than an enduring, evidence-tiered research-group directory. Next pass should distinguish recurring lab owner, collaboration, open-source maintainer, and discovery-only source without duplicating papers.

## 6. Why seven active Frontier questions?

These are not taxonomy bins. The qualifying test is **a changed execution contract or optimization lifecycle, an unresolved systems decision, and specific source evidence allowing a meaningful experiment**.

| Frontier | Specific reason it remains a research question |
|---|---|
| Agent-native serving | Tool/LLM alternation changes session continuity, cache survival and tail-latency objective |
| Real-time omni-modal serving | Continuous audio/video event timing, interruption, synchronization and jitter impose a new live-session contract |
| Diffusion/non-AR language serving | Blockwise updates and state/quality constraints differ materially from autoregressive token stepping |
| Interactive world-model inference | Action-to-frame loops need sustained FPS and long-horizon state/latency controls |
| Embodied / VLA loops | Perception–action deadlines and heterogeneous edge resource constraints affect executable deployment |
| Agentic kernel engineering | Correctness-verified, budget-matched kernel search challenges fixed hand-crafted optimization workflows |
| Autonomous inference-engine evolution (RSI-adjacent) | Persistent whole-stack experiment loops must prove workload transfer and evaluator robustness; **engine improvement does not prove recursive optimizer/model self-improvement** |

**Do not promote** standard KV tiering, hybrid attention, ordinary multi-node scaling or routine deployment just because they appear in new papers. Those already have canonical engineering homes. Revisit the seven periodically against baseline engines, artifacts and negative evidence; allow demotion.

### Specific source-level follow-up example

The 2026-11 source [RTP-LLM: Building an Evolvable and Reliable LLM Inference Engine at Alibaba Scale](https://arxiv.org/abs/2611.00967) presents production-engine evolution and failure containment, whereas the already-canonical [May 2026 RTP-LLM report](https://arxiv.org/abs/2605.29639) focuses on performance mechanisms, cache/phase separation and model loading. **Do not automatically admit two rows because the arXiv IDs differ**; first examine overlap, independent contribution, publication identity, implementation continuity and the G0–G5 value of a second row. This is a **review candidate**, not a newly accepted paper.

## 7. Confirmed small documentation fixes in this audit branch

- Corrected a stale homepage claim of **851 current** topic entries to **854**.
- Condensed duplicated admission chronology in homepage and topic directory; retained dated evidence links.
- Added an explicit selection rationale for the 30 foundations and cross-category placement rules.
- Fixed the organization index link to a removed community research-heading anchor; synchronized November 5 timestamp.
- Clarified company inclusion/evidence scope and the distinction between executable projects, source nodes and independent research labs.
- Synchronized the community index timestamp with its November 5 additions.

**Not changed:** canonical paper rows, inclusion decisions, company profiles, 76 open-source rows, research-source rows, Frontier membership, archival audit receipts, or author performance figures.

## 8. Next worklist (proposed, not executed)

| Priority | Task | Acceptance criteria |
|---|---|---|
| **P0** | Lightweight *local* Markdown consistency check | Count 854 rows/44 directions/30 foundations/49 companies/76 code entries; detect missing relative paths and heading anchors; no generated bibliography, crawler or publication pipeline |
| **P0** | Scope-audit the 83 KEEP_ADJACENT-labeled rows | For each, record exact adjacent status, real vs simulated hardware, changed model/semantics, published source and KEEP/HOLD/REMOVE decision; no wholesale deletion by label |
| **P1** | Evidence-depth pass for low-source company pages | Strengthen with first-party code, design reports or explicit service-only boundaries; do not equalize page lengths artificially |
| **P1** | Make research-source navigation durable | Separate true labs, collaborations, industry researchers and OSS maintainers in the existing map or one lightweight subpage; preserve source attribution and avoid duplicate papers |
| **P1** | Revisit group boundaries | Examine MoE/sparse attention, KV compression vs quantization, scheduler policy vs distributed fabric on difficult examples; document stable tie-break decisions |
| **P1** | Evidence-depth pass on 2026/preprint and terse mechanism rows | Focus on strong recent works, source identity, real hardware, closest baseline, correctness/model changes and code; short text alone is not grounds for rejection |
| **P2** | International organization discovery | Add only teams with inspectable inference-specific engineering; classify archived software, API documentation and production claims distinctly |
| **P2** | Reduce landing-page chronology | Move old organization release/update matrices to dated reviews when safe; keep a current source map, not a rolling release blog on the landing page |
| **P2** | Frontier reevaluation and experimental handoff | Require a new executable workload contract and 1–2 decisive measurable tests per active Frontier; cross-reference the canonical mechanism, not another paper list |

**Definition of done for the next round:** a reader can find the right mechanism, the strongest primary sources and the relevant execution/evidence caveat in two navigation steps, without confusing a reviewed paper, an OSS project, a lab affiliation, a model release or an unverified vendor performance claim.
