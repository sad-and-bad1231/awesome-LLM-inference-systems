# AI Infra Candidate Pool

This is the working queue. Daily automation should add candidates here first.
Main documents should change only after a small manual or weekly confirmation pass.

Status values:

- `new`: not reviewed.
- `keep`: worth tracking, but not ready for the main documents.
- `promote`: verified and ready for a small main-document update.
- `drop`: off-topic, duplicate, weak source, or too speculative.

## Current Keep Rationale（2026-06-27）

The queue is intentionally small after the weekly-quality pass. These entries are still worth watching, but the current public source does not yet justify moving them into the main index.

| Title | Keep reason | Next check |
|---|---|---|
| Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications | Enterprise multi-agent deployment is relevant, but the systems mechanism is still too application/framework-level for the main LLM inference index. | Re-check for a concrete runtime, scheduling, or state-management artifact. |
| Variable-Width Transformers | Potential inference efficiency implications, but it is primarily a model-architecture direction until systems evaluation is clearer. | Re-check for serving/runtime benchmarks or adoption by an inference engine. |
| CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference | KV compression is on-topic, but the arXiv page currently carries an admin note about text overlap, so promotion should wait. | Re-check arXiv status or an independent venue/source before promotion. |

| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |
|---|---|---|---|---|---|---|---|
| 2026-06-18 | A | paper | arXiv AI infrastructure query | Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications | compression-cost, agent-rag | [primary](https://arxiv.org/abs/2606.18502v1) | keep |
| 2026-06-18 | A | paper | arXiv AI infrastructure query | Variable-Width Transformers | runtime-serving, state-kv, agent-rag | [primary](https://arxiv.org/abs/2606.18246v1) | keep |
| 2026-06-24 | A | paper | arXiv AI infrastructure query | CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference | state-kv, compression-cost, kernel-compiler, agent-rag | [primary](https://arxiv.org/abs/2606.24467v1) | keep |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving | runtime-serving, state-kv, network-disaggregation | [primary](https://arxiv.org/abs/2607.01617v1) | new (likely P1) |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal | runtime-serving, kernel-compiler, moe | [primary](https://arxiv.org/abs/2607.00501v1) | new (likely P1) |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference | kernel-compiler, reliability-evaluation | [primary](https://arxiv.org/abs/2606.31903v1) | new |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding | runtime-serving, hardware-edge | [primary](https://arxiv.org/abs/2606.31315v1) | new |
