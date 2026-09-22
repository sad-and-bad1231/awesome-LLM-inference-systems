# Evidence-first foundation implementation plan

**Goal:** Bound every public reading surface, make core evidence completeness machine-checkable, and add a compact audit path before expanding sources.

**Architecture:** Keep JSONL as the unlimited fact layer. Add deterministic selectors only at publication time, add conservative legacy evidence states during normalization, and expose compact aggregate diagnostics through `monitor.py audit`. Internal lists and archives remain complete.

**Tech stack:** Python standard library, unittest, JSONL, generated Markdown.

## Task 1: Deterministic public selectors

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/reading.py`
- Test: `tests/ai_infra_monitor/test_reading.py`

1. Add failing tests for per-theme limits, priority ordering, multi-theme single placement, and repeatable ordering.
2. Run the focused test and confirm it fails because the selector is absent.
3. Implement the smallest shared selector returning bounded theme groups.
4. Run the focused tests, then the complete reading test module.

## Task 2: Wire public budgets into every public surface

**Files:**
- Modify: `ai-infra-sources.yaml`
- Modify: `scripts/ai_infra_monitor/monitor.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/publication.py`
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/reading.py`
- Test: `tests/ai_infra_monitor/test_publication.py`
- Test: `tests/ai_infra_monitor/test_monitor_cli.py`

1. Add failing publication tests for 8 papers/theme, 5 projects/theme, 15 exploration entries/track, and 8 rows/company topic.
2. Confirm failures reflect currently unbounded rendering.
3. Add config defaults and pass them only into public rendering.
4. Apply the shared selector after industry project aggregation; bound company topics deterministically.
5. Update public copy so bounded views are not described as complete collections.
6. Run focused publication and CLI tests.

## Task 3: Core evidence-state contract and conservative migration

**Files:**
- Modify: `scripts/ai_infra_monitor/ai_infra_monitor/records.py`
- Test: `tests/ai_infra_monitor/test_records.py`

1. Add failing tests requiring valid evidence states on core records and accepting explicit legacy/not-checked states.
2. Add failing normalization tests that map existing organizations/artifacts to `legacy_present`/`legacy_linked` and gaps to `not_checked` without inventing verification.
3. Implement enums, date/source validation, and conservative normalization.
4. Run focused record tests.
5. Run `monitor.py curate` to migrate derived curation metadata while preserving raw summaries and user facts.

## Task 4: Compact audit command

**Files:**
- Create: `scripts/ai_infra_monitor/ai_infra_monitor/audit.py`
- Modify: `scripts/ai_infra_monitor/monitor.py`
- Test: `tests/ai_infra_monitor/test_audit.py`
- Test: `tests/ai_infra_monitor/test_monitor_cli.py`

1. Add failing tests for compact counts: scopes, latest dates, core evidence states, duplicate identities/titles, long summaries, themes, company topics, and public budget projections.
2. Add a failing CLI test for `monitor.py audit` and JSON output.
3. Implement aggregate-only audit functions and CLI wiring; never emit full summaries.
4. Run focused tests and inspect output size.

## Task 5: First reliability repair batch

**Files:**
- Modify: `data/papers.jsonl`
- Modify: `data/industry.jsonl`
- Add or modify: `reports/metadata-audit-2026-08-10.md` only if the repository already tracks equivalent audit reports

1. Use the audit output to enumerate public-visible and foundation/frontier core records lacking checked metadata.
2. Verify only those records against official paper pages, official repositories, conference pages, or author/project pages.
3. Record explicit `verified`, `partial`, or `not_found` states, check date, and source URLs; do not infer affiliations from email domains or third-party summaries.
4. Keep unresolved records explicit as `not_checked`; do not broaden the search to new venues or companies.
5. Re-run record validation and audit, and report the before/after gap count.

## Task 6: Rebuild and full verification

**Files:**
- Regenerate only through monitor commands: public READMEs, internal lists, archives, and derived curation metadata.

1. Run the complete unit test suite.
2. Run `monitor.py render`, `publish`, `validate`, and `audit`.
3. Snapshot status, run render/publish a second time, and verify no additional diff.
4. Check public per-section budgets, absence of release HTML, unique industry projects, and unchanged raw summary text aside from pre-existing user changes.
5. Review the full git diff for scope and commit the completed foundation as a focused commit.

