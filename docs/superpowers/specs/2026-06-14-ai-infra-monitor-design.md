# AI Infra Monitor Design

## Objective

Maintain `paper-list.md` and `industrial-llm-inference-systems.md` as a long-lived, auditable AI infrastructure knowledge base with minimal repeated browsing and token use.

The monitor runs:

- Daily incremental scan at 22:00 Asia/Shanghai, Sunday through Friday.
- Weekly deep scan at 22:00 Asia/Shanghai on Saturday.
- Every successful run creates a local Git commit and never pushes.

## Evidence Policy

Sources are classified before semantic processing:

- **A**: official proceedings/programs, arXiv/OpenReview papers, official documentation, official repositories and releases. Verified A-level items may update the main documents automatically.
- **B**: official engineering blogs, product announcements and engineering retrospectives. These enter `ai-infra-candidates.md` until promoted.
- **C**: media, financing news, roadmap reporting and unverified aggregators. These are trend signals only.

Conference status overrides preprint status. DOI or arXiv ID is the primary identity; normalized title and canonical URL are fallbacks. Author affiliations are never inferred from names.

## Architecture

The deterministic Python monitor performs cheap, repeatable work:

1. Fetch configured Atom/RSS, HTML index, OpenReview API and GitHub release sources.
2. Use ETag/Last-Modified state and stable identities to avoid repeated processing.
3. Filter by the query matrix and cap each run's candidate count.
4. Persist unresolved candidates and generate a compact JSON run manifest.
5. Validate Markdown structure, duplicates, links and conflict markers.
6. Finalize state and create a scoped local Git commit only after validation.

The scheduled Codex job performs semantic work:

1. Run discovery.
2. Read only the new run manifest rather than rescanning the web.
3. Verify A-level candidates against primary sources.
4. Add qualified records to the two main documents.
5. Add B/C or unresolved records to the candidate pool.
6. Run validation and finalize the run.

## Files

- `ai-infra-sources.yaml`: JSON-compatible YAML containing sources, query groups, limits and target files.
- `ai-infra-state.json`: ignored local cursor, HTTP cache metadata, pending records and run history.
- `ai-infra-state.example.json`: tracked empty-state schema.
- `ai-infra-candidates.md`: review queue for B/C and unresolved A-level items.
- `scripts/ai_infra_monitor/monitor.py`: CLI entry point.
- `scripts/ai_infra_monitor/ai_infra_monitor/`: focused discovery, parsing, storage, validation and Git modules.
- `tests/ai_infra_monitor/`: stdlib `unittest` coverage and fixtures.
- `reports/weekly/`: tracked weekly summaries.
- `docs/ai-infra-monitor-workflow.md`: operating procedure and recovery rules.

## Run Contract

`discover --mode daily|weekly` creates `runs/<run-id>/candidates.json` and prints a machine-readable summary. The manifest contains only pending, previously unseen candidates.

The semantic worker may edit only:

- `paper-list.md`
- `industrial-llm-inference-systems.md`
- `ai-infra-candidates.md`
- `reports/weekly/<date>.md` during weekly mode

`validate` must pass before `finalize`. `finalize` marks the run processed, stages only approved knowledge-base files, and commits when there is a meaningful diff.

## Token-Efficiency Rules

- Daily scan processes at most 24 candidates; weekly scan at most 80.
- Daily mode scans fast feeds and releases only.
- Weekly mode additionally scans conference programs and broader queries.
- Previously seen identities are not sent back to the semantic worker.
- Candidate manifests contain title, source, tier, URL, date and matched topics only.
- The worker opens a source only when the manifest item is new or its status changed.
- No summary is regenerated for an unchanged record.

## Failure Handling

- Network failures are recorded per source and do not abort unrelated sources.
- A failed validation leaves the run pending and creates no commit.
- A source returning malformed content is quarantined in the run report.
- A record with uncertain venue, affiliation or title remains in the candidate pool.
- Git commits are local; no remote operation exists in the monitor.

## Success Criteria

- Offline tests pass with no third-party Python dependency.
- A fixture discovery run generates candidates and preserves deduplication across a second run.
- Markdown validation detects malformed rows, duplicate records and empty links.
- Finalization creates no commit when nothing changed.
- Two Codex cron automations exist with the agreed schedules and local workspace.
