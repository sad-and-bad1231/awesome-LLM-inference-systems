# AI Infra Monitor Workflow

This repository has three working documents:

- `paper-list.md`: verified papers only.
- `industrial-llm-inference-systems.md`: verified industrial systems, projects, official reports and engineering material.
- `ai-infra-candidates.md`: discovery queue and review backlog.

The default workflow is conservative: discover broadly, confirm in small batches, and write only verified items to the main documents.

## Source Strategy

- Daily sources: arXiv queries, stable enterprise RSS feeds and core project releases.
- Weekly sources: top-conference indexes, OpenReview/DBLP pages and enterprise HTML indexes.
- Main-document promotion still requires primary-source verification; source discovery alone is not evidence.
- New papers in `paper-list.md` must be inserted into the existing topic category; do not create date-based append sections.

## Paper Priority

`paper-list.md` is a cumulative high-quality index, not a short reading list. Do not remove existing entries only because they are lower priority.

- P0: CCF A systems/architecture/network/database/security conferences or widely recognized ML venues, with a clear LLM inference systems contribution.
- P0: ICLR, ICML, NeurIPS, MLSys and similar high-signal ML systems papers from 2025 or 2026 that directly affect inference execution, runtime, state, compression, kernels, evaluation, or industrial serving.
- P1: strong 2025 papers and 2026 new papers from arXiv, ARR, OpenReview, official company research pages, or top-company technical reports when the mechanism is concrete and inference-relevant.
- P2: useful background, adjacent infrastructure, training-cluster, vector-database, privacy, or hardware papers. Keep them if already present, but do not prioritize them over P0/P1.

## Commands

Run from `D:\ResearchWork`:

```powershell
python scripts/ai_infra_monitor/monitor.py init
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py discover --mode weekly
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers A B C
python scripts/ai_infra_monitor/monitor.py report --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py finalize --run-id <run-id>
```

## Daily Increment

Goal: collect signals, not rewrite the index.

1. Run `init`.
2. Run `discover --mode daily`.
3. Add useful P0/P1/P2 candidates to `ai-infra-candidates.md`, marking likely P0/P1 in the status note when obvious.
4. Do not update `paper-list.md` or `industrial-llm-inference-systems.md` unless the change is a trivial correction.
5. Run `validate`.
6. Run `finalize --run-id <run-id>`.

Daily automation runs Sunday through Friday at 22:00 Beijing time. The daily cap is 8 candidates.

## Weekly Confirmation

Goal: add verified high-quality papers and keep the queue clean.

1. Run `init`.
2. Run `discover --mode weekly`.
3. Review the candidate pool and new manifest together.
4. Promote every verified P0/P1 paper found in the reviewed batch.
5. Keep P2 items in the candidate pool unless they are already verified and clearly useful to the index.
6. Drop obvious duplicates, off-topic records and weak sources from the candidate pool.
7. Write a weekly report if there are meaningful status changes.
8. Run `validate`.
9. Run `finalize --run-id <run-id>`.

Weekly automation runs Saturday at 22:00 Beijing time. The weekly cap is 24 candidates.

## Quality Gate

Before a main-document edit, confirm:

- Primary source is available: official proceedings, paper PDF, official docs, official repository, or company technical post.
- Title and venue/status are copied from the source, not guessed.
- Main author organizations come from the paper or official page. If absent, write `作者公开稿未列单位`.
- The summary is one sentence and describes the mechanism, not marketing claims.
- The item fits one of the current AI infra themes: runtime, long context/state, compression/cost, kernels/compiler, disaggregation/network, MoE, agent/RAG, multimodal serving, hardware/edge, reliability/evaluation.
- The item is not already covered in either main document.

If any point is uncertain, keep the item in `ai-infra-candidates.md`.

## Change Size

- Daily: candidate-pool updates only by default.
- Weekly: promote verified P0/P1 papers from the reviewed batch; keep lower-confidence items queued.
- Main documents: prefer append-only additions and clear status corrections.
- `paper-list.md`: keep category sections stable and add rows under the best matching category.
- Deletions: only duplicate, off-topic, broken-source, or superseded entries.

## Automation Boundaries

- Automations may create local Git commits.
- Automations must never push.
- Automations must not modify `long-cot-kv-retention-literature.md`.
- Runtime state, run manifests, reports and temporary files are local unless intentionally promoted.

## Recovery

- Network errors stay in the run manifest. Re-run discovery later; do not delete state to hide the error.
- If validation fails, fix the reported rows and rerun `validate`.
- If a run should not be committed, use `finalize --run-id <run-id> --no-commit`.
