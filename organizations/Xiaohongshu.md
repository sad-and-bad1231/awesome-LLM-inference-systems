# Xiaohongshu / Rednote AI Infrastructure

The public [RAI Studio](https://github.com/redai-studio) organization identifies itself as Xiaohongshu's AI Infra team. Its work spans model serving, caching, training–rollout coordination and heterogeneous accelerator deployment; **model ownership is not a prerequisite for systems relevance**.

[← Organizations](README.md)

## First-party software and research

| Source | Mechanism | Evidence boundary |
|---|---|---|
| [HYPIC](https://github.com/redai-studio/HYPIC) · [paper](https://arxiv.org/abs/2607.01299) (2026 preprint) | **Position-independent segment caching** for hybrid linear/full-attention models: cache transition operators for recurrent state composition; recompute a seam window for full attention; parallelize cold segments. Implemented on **SGLang v0.5.14** with benchmark/replay examples. | Authors report TTFT/QPS improvements on selected hybrid models and workloads; cached state composition is **approximate where recomputation is bounded** and requires a quality oracle. The HYPIC fork is not automatically upstream SGLang support. |
| [Relax](https://github.com/redai-studio/Relax) (released software) | Asynchronous multimodal post-training stack using Ray Serve, SGLang rollout workers and a streaming transfer queue; separates training and inference resources. | **RL rollout** infrastructure, **not** evidence of production online serving Goodput or a new inference kernel. |
| [RAI Studio infrastructure map](https://github.com/redai-studio) (first-party team statement) | **Red Token Hub** model-serving layer describes model onboarding, request routing, KV reuse, reliability and scaling; other layers include model-production and accelerator-management infrastructure. | A public organizational architecture statement, **not** an open codebase or separately benchmarked routing implementation. |
| [PIPO research implementation](https://github.com/redai-studio/PIPO) | Architectural experiment in latent multi-token prediction, relevant to future generation/decode workloads. | Model/architecture research; no production serving advantage inferred. |

## Research reading angle

**Hybrid-state ownership** is the distinctive signal: exact prefix KV reuse cannot be transplanted to linear-attention recurrent state unchanged. Inspect HYPIC's state transition algebra, prefix position handling, seam recompute accuracy and distributed scatter. For Relax, study the training–rollout handoff and resource scheduler rather than attributing online service performance.

**Status:** primary organization, open-source code and author preprint; no local benchmark replication. Attribution must remain to the listed RAI team, not an assumed company-wide production system.
