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
3. Add useful candidates to `ai-infra-candidates.md`.
4. Do not update `paper-list.md` or `industrial-llm-inference-systems.md` unless the change is a trivial correction.
5. Run `validate`.
6. Run `finalize --run-id <run-id>`.

Daily automation runs Sunday through Friday at 22:00 Beijing time. The daily cap is 8 candidates.

## Weekly Confirmation

Goal: make a small number of high-confidence changes.

1. Run `init`.
2. Run `discover --mode weekly`.
3. Review the candidate pool and new manifest together.
4. Promote at most 5 items unless the user explicitly asks for a larger sweep.
5. Drop obvious duplicates, off-topic records and weak sources from the candidate pool.
6. Write a weekly report if there are meaningful status changes.
7. Run `validate`.
8. Run `finalize --run-id <run-id>`.

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
- Weekly: up to 5 promotions or removals by default.
- Main documents: prefer append-only additions and clear status corrections.
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
