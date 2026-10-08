# Serving Systems — migration record

The first 50-paper Serving cohort has been **retired as an independent paper list** to avoid maintaining parallel entries. It was reviewed against the eight-category ontology; the accepted work has one full entry on its corresponding topic page.

| Decision | Count |
|---|---:|
| Reclassified into one of eight canonical categories | 49 |
| Held outside the core LLM-specific bibliography | 1 |

## Held for scope review

- **[SkyServe: Serving AI Models across Regions and Clouds with Spot Instances](https://2025.eurosys.org/accepted-papers.html) (EuroSys 2025)** — strong general-purpose cross-cloud AI model serving, but the published mechanism is not specific to autoregressive LLM inference. Excluded from the eight LLM inference categories; this is a **scope decision, not a claim that the work is low-quality**.

## Source corrections

- **ExeGPT / SpotServe**: former ASPLOS general program links were replaced by individual author arXiv records, while venue labels are retained as previously catalogued. Publisher-specific landing-page URLs should be substituted when independently confirmed.
- **CacheBlend / DeltaZip**: replaced EuroSys conference-list URLs with paper-specific ACM DOIs.
- **Pensieve**: links to the EuroSys technical program rather than a generic accepted-papers page; individual publisher URL remains a follow-up bibliographic task.
- **Simple Is Better**: replaced generic OSDI technical sessions page with the author-specific USENIX landing page.

Older catalog rows remain recoverable in Git history. **Reclassification is not experimental reproduction**; reported mechanisms are from publication abstracts and technical descriptions, not independently measured speedups.
