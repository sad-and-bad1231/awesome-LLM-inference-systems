# AI Infra Dual-Store Knowledge Base Design

## Goal

Keep academic papers and industry/infrastructure solutions as separate, directly readable collections while making identity, evidence, triage, and rendering machine-verifiable.

## Architecture

- `data/papers.jsonl` is the fact source for academic papers.
- `data/industry.jsonl` is the fact source for company solutions, open-source systems, and engineering material.
- `data/candidates.jsonl` is staging for newly discovered records before promotion.
- `paper-list.md`, `industrial-llm-inference-systems.md`, and `ai-infra-candidates.md` are generated views.
- `ai-infra-system-abstractions.md` remains a compact navigation index and never becomes the primary reading list.

Each main record keeps the existing technical fields and adds `canonical_id`, `aliases`, `status_history`, and `evidence`. Canonical identity is resolved from DOI/OpenReview/arXiv identifiers first, known title aliases second, and normalized title last. Evidence fields separate venue status and source type from subjective triage and priority.

## Data Flow

```text
discover -> candidates.jsonl -> triage -> queue papers/industry -> render -> validate -> finalize
```

Queue promotion marks the staging record as promoted and writes a typed record to the matching main store. Cross-store canonical conflicts are validation errors unless the staging record is already promoted or dropped.

## Scope

The active discovery line prioritizes serving runtime, P/D disaggregation, KV state, kernel/compiler, scheduling, MoE serving, and serving benchmarks. Existing peripheral records are retained for auditability, but new peripheral candidates are downranked unless they contain direct inference-serving evidence.

`long-cot-kv-retention-literature.md` is retired as a standalone side list; any useful entries already present in the main stores remain governed by the new schema.

## Verification

Tests cover canonical alias merging, store splitting, promotion routing, cross-store conflicts, generated-view separation, and peripheral triage. Full CLI validation must pass after migration and rendering.
