# PR #80 pre-merge editorial audit — November 10, 2026

**Target:** [PR #80](https://github.com/sad-and-bad1231/awesome-LLM-inference-systems/pull/80), branch `curation/november-2026-systems-sweep-1109` based on `main@6bcdd81`; 852 → 897 canonical rows, 8 technical categories, 44 tracks, 45 net additions. **Status: DRAFT / NO MERGE APPROVAL.** Source-level review and CI are **not a substitute** for independent GPU/NPU replication or a second scientific reviewer.

## 1. Audit scope, controls and primary evidence

- Reviewed the actual PR changed-file patch (25 changed files at audit start), canonical row titles/source IDs, README/topic/review reconciliation and official GitHub Action. Spot-checked representative high-impact primary arXiv abstracts/full HTML, plus [Anthropic Fable/Mythos 5.2](https://www.anthropic.com/claude-fable-and-mythos-5-2), [Google TPU 8tx/8i Max / TPU Sync](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/), [LMSYS HiCache](https://www.lmsys.org/blog/2026-11-02-hicache-distributed-serving) and [Buoyant Kinference](https://vllm.ai/blog/2026-11-04-introducing-kinference). Google XLA Serving Engine official announcement was independently verified against its [official November archive](https://opensource.googleblog.com/2026/11) and [GitHub source](https://github.com/openxla/xla-serving).
- Re-checked [Warpline](https://arxiv.org/html/2611.04331v1), [StrataFlux](https://arxiv.org/abs/2611.08363), [Penelope](https://arxiv.org/abs/2611.00391), [LoopDuet](https://arxiv.org/abs/2611.07211), [Bevy](https://arxiv.org/abs/2611.04794), [Basin](https://arxiv.org/abs/2611.02543), [UniExit](https://arxiv.org/abs/2611.09159), [ELDR v3](https://arxiv.org/abs/2607.00466), [flash-comm](https://arxiv.org/abs/2611.06634), [SpecPilot](https://arxiv.org/abs/2611.02501), [FlashOffloading](https://arxiv.org/abs/2611.07542), [MORTIS](https://arxiv.org/abs/2611.08638) and [KVGuard](https://arxiv.org/abs/2611.06138), among other source identities. A spot-check is **not** a complete full-method re-review of all 46.
- No author code, GPU timing or NPU kernels were executed. Numerical claims in topical rows remain **author-reported**. A paper may present both real measured systems and simulation, but the specific metric's origin must remain explicit.

## 2. Corrections implemented on the branch

| Finding | Severity | Resolution |
|---|---|---|
| Six canonical Markdown titles embellished/modified the original paper title with a system nickname or subtitle: **Penelope, StrataFlux, The GPU Needs an Operating System, LoopDuet, Basin, Bevy** | **P1 / G0 identity and searchability** | Corrected paper link labels to **exact first-party arXiv titles**. Kept Penelope/LoopDuet/Basin/Bevy project names in the mechanism text, not the formal citation title. **No paper-count change** |
| **Warpline** paper abstract states **35** kernels, while its method Table 1 analyzes **38 total** | **P2 / G3 denominator** | Clarified that 35 are open-source kernels **plus three closed-source library kernels**. Agent comparison uses **10 SOL-ExecBench** cases, separate from the tracing-overhead population; do not merge their denominators. Updated topic row and third-pass source ledger |
| **MobiInfer (arXiv:2611.08496)**: arXiv ID indicates November 2026, but primary abstract and HTML `v1` submission history both state **“11 Aug 2026”** | **P1 / source metadata conflict — OPEN** | Demoted the paper from the canonical row to **HOLD_G0_DATE_CONFLICT** on Nov 10; the previously unverified “Nov 5 preprint” date had already been removed; no assertion of first-publication day/month. This is a source-metadata discrepancy, not demonstrated evidence that the paper's model, source identity or experiment is fabricated. Request an author/arXiv source clarification before clearing date/venue gate |
| Mixed hardware, simulator and approximate-quality claims | **G3 spot review** | Existing scoped caveats remain: **Basin** H200 arrival-time prototype versus predictor-driven simulation, **StrataFlux** three distinct evaluation configurations, **flash-comm** reduction microbenchmark versus E2E TPOT, **UniExit** 1B edge Early Exit versus large-model Serving. No new unaudited speedups introduced |
| **ELDR** already has one canonical home, while its Nov 6 v3 abstract has updated results and ACM SIGOPS ATC venue | **G0 version** | Retained exactly one row. [2026 ACM SIGOPS ATC official schedule](https://atc.sigops.org/2026/schedule.html) independently lists ELDR; [arXiv author-final v3](https://arxiv.org/abs/2607.00466) cites ACM DOI `10.1145/3828523.3857077`. Published/proceedings citation can be updated after publisher landing page verification |

## 3. Remaining pre-merge issues

1. **P1: Reviewability / batch size.** A single PR now adds **45 papers** across eight topics and organization/Frontier files; [STRICT_REVIEW](../STRICT_REVIEW.md) recommends about **10–20 full-method entries per review batch**, and [CURATION](../CURATION.md) requests small reviewable PR diffs. Do not merge on structural CI alone. Either split the admitted rows into independently reviewable batches or obtain per-category review signoff with explicit named reviewer and audit scope.
2. **P1: MobiInfer source-date conflict.** The paper's **arXiv ID/year/title/authors** resolve, but the source's submission day/month does not; keep the source in the HOLD audit, **not canonical**, until clarified. Do not use this entry as an example of *newly submitted November 2026* work.
3. **P1: G4 artifact and code traceability.** Most receipts do not pin author artifact **commit/release**, runtime dependency pair and the exact workload manifest. This corpus is correctly described as *source-curated*, not fully reproducible; independent high-value reproducibility should be done on a smaller candidate subset rather than marking all 46 green.
4. **P2: Editorial density.** Very long single-line canonical rows duplicate full evaluation details in three audit ledgers; shortening paper-row prose into mechanism + 1 strong metric + failure/quality boundary would improve navigability **after** scientific review, while retaining full receipts.
5. **P2: Historic provenance.** The 42 historical rapid program-index admissions and NovaServe/Select-N identity conflict predate this PR and remain open. Do not advertise them as resolved by this intake.

## 4. Freeze criteria

- **Structural CI:** GitHub Actions `catalog-integrity` must complete **success on the latest HEAD**, not merely a prior commit; locally or in CI, run `python3 -m unittest discover -s tests -p 'test_*.py'` and `python3 scripts/check_catalog.py`.
- **Source:** spot audit all *new* final titles/venues, particularly revised publisher/DOI cases; disputed dates and artifacts must carry flags, not invented verification. No duplicate first-source identity across topics.
- **Review:** obtain explicit approval for batch size/source claims; keep PR **Draft until reviewed**. The current total is **897** after one documented G0 removal; further evidentiary HOLD/REMOVE requires another explicit count adjustment.

**Verdict:** **STRUCTURAL_PASS_PENDING_FINAL_HEAD_CI; SCIENTIFIC_REVIEW_INCOMPLETE / DRAFT**. The already implemented corrections are appropriate; this document is **not** a merge approval.


## November 10 second review: full new-source G0 metadata / selective G3 and G4

**Additional source work:** compared **all 46 newly admitted arXiv paper titles and date metadata**, plus the revised [ELDR author-final](https://arxiv.org/abs/2607.00466), against their first-party arXiv abstract/metadata pages, rather than sampling only famous titles. **No unmatched paper title/ID was found among the original 46; one was subsequently demoted due to a first-submission metadata conflict**. This does **not** mean all 46 full evaluation appendices were inspected, nor that experiment claims are replicated. The unresolved MobiInfer anomaly remains specifically marked and should not be counted as a verified November first-submission date.

### Further corrections made

| Source | Original row defect | Correct evidence and change |
|---|---|---|
| [Inside the Trap, 2611.08902](https://arxiv.org/abs/2611.08902) | Incorrect **Nov 5** first-submission date | arXiv records **Nov 6, 2026**; corrected category row |
| [SpecCTMC, 2611.08362](https://arxiv.org/abs/2611.08362) | Incorrect **Nov 6** first-submission date | arXiv records **Nov 5, 2026**; corrected category row |
| [UMLoad, 2611.04253](https://arxiv.org/abs/2611.04253) | Listed **Nov 4** as initial preprint date | Submitted **Nov 3, 2026 (v1)** and revised **Nov 4 (v2)**; corrected category row and switched the detailed evaluation link to **v2** |
| [MobiInfer, 2611.08496](https://arxiv.org/abs/2611.08496) | arXiv ID encodes a November intake while the source page and its v1 submission history say **11 Aug 2026** | **UNRESOLVED SOURCE_CONFLICT:** preserve year/title/authors, keep November-first-submission date **unverified** and remove the record from the canonical Runtime topic on Nov 10. Do not silently infer source typo or assert an author correction |
| [ELDR 2607.00466v3](https://arxiv.org/abs/2607.00466) | Earlier preprint claims in old row | Author-final revision **Nov 6**, originally submitted **Jul 1**. Existing canonical row refreshed; the manuscript's accepted ACM SIGOPS ATC 2026 claim is backed by the public conference schedule; one paper, one home |

**Historical timing detail:** [Penelope](https://arxiv.org/abs/2611.00391), [Megakernel Study](https://arxiv.org/abs/2611.00495), [Weights That Stay](https://arxiv.org/abs/2611.00506) and [Ripple](https://arxiv.org/abs/2611.01067) were **first submitted October 30–31**, but surfaced in the November arXiv issue/index. Their topic rows already retain the date distinction; **do not count them as November first submissions**.

### Verified G4 author artifacts — pinned browse snapshot, no execution

These sources supply a useful beginning for **source audit**, but a browseable repository alone does not establish that author performance tables are reproducible.

| Paper | Official artifact/commit seen during audit | Evidence limit |
|---|---|---|
| [ForgeKernel](https://arxiv.org/abs/2611.04998) | [OpenBMB/ForgeKernel @ `6664d608`](https://github.com/OpenBMB/ForgeKernel/tree/6664d6080c37803605d6c6bc25f87656423ff114): `src/`, `skills/`, `kernels/`, `tests/`, `hw_kb/` | Original agent/kernel repository resolved and source paths visible; **no model, test-suite, hardware probe, NPU run or match of leaderboard outputs** attempted |
| [ServerBench](https://arxiv.org/abs/2611.06841) | [Infini-AI-Lab/Server-Bench @ `b80a3fb2`](https://github.com/Infini-AI-Lab/Server-Bench/tree/b80a3fb21ff9037bedbde78536a5b918f100c6cc): `serving_tasks/`, `serverbench/`, `agentx-harness/`, `experiments/` | Source and harness present, no executed frozen submission, reference replay or held-out verification |
| [SpecCTMC](https://arxiv.org/abs/2611.08362) | [kasakh/specctmc @ `c2cff633`](https://github.com/kasakh/specctmc/tree/c2cff63396b0446dbfefbc0b062461dd23ee2d77): `src/`, `tests/`, `examples/`, `environment.yml` | Official arXiv-linked repo supports CPU synthetic tests and user-supplied models; **no tests run**. README explicitly says code repo lacks checkpoints, paper results and experiment logs |

**Important quality boundary:** source G0 was checked across the original 46 submissions; **45 are currently canonical, while MobiInfer is HOLD due to the source-date conflict**, while G3/G4 checks remain **selective** and uneven; source-level author claims can still be wrong. Passing `catalog-integrity` is evidence about repository structure only. **Do not convert this status into a merge approval**.


### Nov 10 hard-gate follow-up (supersedes earlier provisional row treatment)

**Disposition: MobiInfer → HOLD_G0_DATE_CONFLICT, Runtime -1, canonical 898 → 897.** Its authors, ID and runtime work remain discoverable from [arXiv](https://arxiv.org/abs/2611.08496) and the dated [third-pass source receipt](NOVEMBER_2026_THIRD_PASS_20261109.md). The conflicting first-submission provenance should be clarified with arXiv/author rather than guessed. This is an editorial source-admission decision, not a claim that the experiments are false. The draft PR now contains **45 net new papers**, not 46. **No merge approval**.
