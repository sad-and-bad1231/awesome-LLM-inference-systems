# Review receipts and evidence status

[← Home](../README.md) · [Current canonical topics](../topics/README.md) · [G0–G5 rules](../STRICT_REVIEW.md) · [Curation policy](../CURATION.md)

**Current state — 2026-11-12 (Baidu closeout + Alibaba surface audit; one strict paper admission in the prior pass):** **853** canonical topic entries across **8 mechanisms / 44 directions**. Dated receipts are **historical decisions**, not extra papers or a parallel bibliography. A source-audited KEEP is **not** a reproduced GPU/NPU performance result. The [eight topic tables](../topics/README.md) are the only live inventory.

## Read these first: latest evidence and quality corrections

| Receipt | What it establishes | What it does **not** establish |
|---|---|---|
| [November 12 Alibaba main-work coverage audit](ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md) | Maps Qwen4 preview / Qwen-AgentWorld, RTP-LLM and BladeLLM, Tair/FlashKV, 2026 serving papers, AgentScope/Qwen-Agent/GUI-Owl/AgentCore, ROLL/RollArt/ROCK, MNN and T-Head/Agentic Cloud | Organization-level surface map only; no new canonical admission or independent reproduction; **853 papers unchanged** |
| [November 11 Baidu native-execution source closeout](BAIDU_NATIVE_EXECUTION_CLOSEOUT_20261111.md) | Frozen SHA comparison across FastDeploy router/scheduler/KV handoff, vLLM V1 KV Connector, SGLang RadixCache/P-D queues; project exit decision | Not a feature-parity, vLLM-Ascend backend, or GPU/NPU performance test; **853 papers unchanged** |
| [November 11 Baidu mechanism/code deep audit](BAIDU_MECHANISM_CODE_AUDIT_20261111.md) | First-principles HCA/MLA/MoE/ECHO cost boundaries, native FastDeploy router/scheduler/KV code pointers, ERNIE Evolve negative experiments and DCore reproducibility receipt | Not a kernel/serving reproduction, and not a claim of Baidu invention of every adopted model mechanism |
| [November 11 Baidu/Paddle primary-source audit](BAIDU_PRIMARY_SOURCE_AUDIT_20261111.md) | Rebuilds ERNIE research-to-inference lineage, FastDeploy/FlashMask, 5.5 architecture and ERNIE Evolve frontier source; records strict KEEP_ORG vs HOLD_TOPIC boundaries | No new canonical paper, independent GPU/NPU benchmark, Looped Transformer attribution or verified RSI |
| [November 6 G0/G3–G5 primary-source review](G5_G4_PRIMARY_SOURCE_REVIEW_20261106.md) | Eleven previously flagged value/evidence cases; Formulaic, ReadKV and TokenSim metric/negative-result corrections; RAGBoost→ContextPilot alias, DefensiveKV ≠ CriticalKV | Neither independent execution nor resolution of NovaServe/Select-N |
| [November 5 preprint identity/metrics](PREPRINT_EVIDENCE_HYGIENE_20261105.md) | Eleven selected source corrections, including Nuska's updated arXiv title and TTFT/SLO distinction | An audit or quality certification of every 2026 preprint |
| [November 5 full adjacent-scope triage](ADJACENT_FULL_SCOPE_REVIEW_20261105.md) | Individual **75-row** editorial screening, after the [earlier eight-case review](ADJACENT_SCOPE_REVIEW_20261105.md); documented two video-only removals and topic migrations | 75 independently re-opened or benchmark-reproduced publications; the initial G5/G4 concerns are superseded where November 6 followed up |
| [November 5 repository architecture audit](REPOSITORY_ARCHITECTURE_AUDIT_20261105.md) | Collection sizes, index rules, classification boundaries and organization/lab coverage | Full per-paper method verification or exhaustive worldwide coverage |

## Outstanding gates — do not silently mark GREEN

- **NovaServe vs Select-N:** `HOLD_IDENTITY`. Conflicting first-party ICS 2026 records; no accepted canonical entry until final publisher camera-ready and version relationship are reconciled. See [November 6 review](G5_G4_PRIMARY_SOURCE_REVIEW_20261106.md).
- **Historical fast admissions:** `STRICT_REVIEW.md` records **42 legacy `admitted_fast_provisional_program_index` cases** from an external ledger. A complete 42-title machine-readable manifest is not established in the current repo; **do not infer that all 42 have been reverified**. The URL form alone (USENIX `/presentation/`, conference poster, etc.) is not a sound proxy for paper availability.
- **Scope policy:** adjacent video, VLA, GPU-OS, rollout and new-model work must satisfy a **reusable inference execution mechanism** test. The [November 6 review](G5_G4_PRIMARY_SOURCE_REVIEW_20261106.md) explicitly notes remaining symmetry questions around retained versus removed cross-modal papers. Do not batch-prune by modality.
- **Reproducibility:** even a verified venue, author repository and experimental table do not mean that matched model/version/hardware/correctness and SLO performance were independently reproduced. `AUTHOR_REPORTED`, `TRACE_SIM`, `PERF_SIM`, `MODEL_CHANGED` and `KEEP_ADJACENT` are not success badges.

## Historical intake and organization sources

| Evidence family | Dated records |
|---|---|
| **Monthly paper intake** | [October close](OCTOBER_2026_MONTHLY_SWEEP_20261031.md) · [October follow-up](OCTOBER_2026_FOLLOWUP_SWEEP_20261031.md) · [November first-pass arXiv intake](NOVEMBER_2026_ARXIV_FIRST_PASS_20261102.md) |
| **Research labs and companies** | [October lab origin](LAB_ORIGIN_REVIEW_20261025.md) · [November 4 industrial sweep](ORG_INFRA_SWEEP_20261104.md) · [November 4 lab/OSS audit](ORG_LAB_OSS_SWEEP_20261104.md) · [November 5 lab/OSS follow-up](ORG_LAB_OSS_SWEEP_20261105.md) |
| **Kernel and system scans** | [Top conference / systems candidates](THREE_ROUNDS_SYSTEMS_20261026.md) · [Kernel frontier](ARXIV_KERNEL_FRONTIER_20261029.md) · [October 30 arXiv/labs](ARXIV_LAB_SWEEP_20261030.md) · [Production kernels](ATC2026_PRODUCTION_KERNEL_SWEEP_20261026.md) |
| **Legacy decisions and corrections** | [HOLD resolutions](HOLD_RESOLUTION_20261025.md) · [Taxonomy/lab hygiene](TAXONOMY_LAB_HYGIENE_20261030.md) · [Archived numerical/curation history](archive/CURATION_HISTORY_20261030.md) · [Archived status snapshots](archive/STATUS_SNAPSHOTS_20261030.md) |

## Contributing without creating another source of truth

Read the current [topic row](../topics/README.md) → fetch the paper's **publisher/author full text and artifact** → apply [G0–G5](../STRICT_REVIEW.md) to exact mechanism, workloads, hardware, Baseline, quality and correctness → record any HOLD/KEEP/REMOVE in a dated receipt → update **only one canonical topic row** and the appropriate visible counts. The [offline catalogue checker](../scripts/check_catalog.py) validates internal links and accounting, **not the scientific validity of claims**.

**Change discipline:** prefer small source-backed PRs; preserve author-reported negative results and the exact unit of every speedup; don't auto-admit papers from this directory or close a HOLD because a link returns HTTP 200.
