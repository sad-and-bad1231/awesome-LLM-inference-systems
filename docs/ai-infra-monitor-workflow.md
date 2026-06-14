# AI Infra Monitor Workflow

## Commands

Run from `D:\ResearchWork`:

```powershell
python scripts/ai_infra_monitor/monitor.py init
python scripts/ai_infra_monitor/monitor.py discover --mode daily
python scripts/ai_infra_monitor/monitor.py discover --mode weekly
python scripts/ai_infra_monitor/monitor.py status
python scripts/ai_infra_monitor/monitor.py queue --run-id <run-id> --tiers B C
python scripts/ai_infra_monitor/monitor.py report --run-id <run-id>
python scripts/ai_infra_monitor/monitor.py validate
python scripts/ai_infra_monitor/monitor.py finalize --run-id <run-id>
```

## Daily Run

1. Execute `discover --mode daily`.
2. Read only the generated `runs/<run-id>/candidates.json`.
3. Verify new A-level candidates from their primary URLs.
4. Add qualifying papers or projects to the main documents.
5. Route B/C and unresolved A-level candidates to `ai-infra-candidates.md`.
6. Execute `validate`.
7. Execute `finalize --run-id <run-id>`.

Daily runs do not rescan conference indexes. The default cap is 24 candidates.
The active Codex automation runs Sunday through Friday at 22:00 Beijing time.

## Weekly Run

1. Execute `discover --mode weekly`.
2. Check conference programs for new acceptance lists and status changes.
3. Reconcile preprints with formal publication status.
4. Verify major release notes and enterprise engineering announcements.
5. Update both main documents and the candidate pool.
6. Execute `report --run-id <run-id>`.
7. Execute `validate`.
8. Execute `finalize --run-id <run-id>`.

Weekly runs scan all configured sources and cap semantic review at 80 candidates.
The active Codex automation runs Saturday at 22:00 Beijing time.

## Automation Boundaries

- `AI Infra Daily Increment` handles incremental discovery and review.
- `AI Infra Weekly Deep Scan` handles conference/status reconciliation and the weekly report.
- Both automations run in the local `D:\ResearchWork` workspace with high reasoning effort.
- Both automations may create local Git commits but must never push.
- Runtime state, run manifests and temporary files remain ignored by Git.

## Promotion Rules

- A-level evidence may enter a main document after title, venue/status, organization and mechanism are verified.
- Official repositories and releases enter the industrial document, not the paper list, unless an accompanying paper exists.
- B/C-level records remain in the candidate pool.
- Uncertain author affiliation is written as `作者公开稿未列单位` or the relevant official-directory wording.
- A formal proceedings record replaces an arXiv-only venue field.
- Existing summaries are not regenerated when only a release version changes.

## Recovery

- Network errors are listed in the run manifest. Re-run discovery later; do not delete state.
- If validation fails, fix the reported rows and rerun `validate`. Do not finalize.
- If a run was semantically reviewed but should not be committed, use `finalize --run-id <run-id> --no-commit`.
- Runtime state and manifests are local and ignored by Git.
- The monitor contains no push command.
