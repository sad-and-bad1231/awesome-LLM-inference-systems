# Together AI

Together AI's **open-model inference infrastructure and research on continuous engine optimization**. The company supplies hosted inference, but its hosted third-party model catalog is not a list of Together-owned architectures.

[← Organizations](README.md) · [← Frontiers](../frontiers/README.md)

## First-party inference-system signals

| Work | Mechanism relevant to inference systems | Evidence type and boundary |
|---|---|---|
| **[From Megakernels to Together Compiler](https://www.together.ai/blog/road-to-together-compiler)** (Nov 16, 2026) | Author ablation: CUDA Graphs + PDL recover **98%** of monolithic megakernel performance on their Llama1B test; CUDA Graphs + PDL with agent-guided multi-kernel rewrites can outperform the hand-written megakernel. Production experience was narrowly limited to one 1B model, BF16, B=1, one customer; **maintenance/shape adaptability are the decisive constraints**. | [First-party engineering report](https://www.together.ai/blog/road-to-together-compiler); vendor-specific Llama1B H100/B200 findings, **not proof that monolithic kernels are always slower** and not a CANN measurement. |
| **[Together Compiler (TKCC)](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference)** (2026-11-04) | Persistent, hot-reloadable engine; parallel code-editing agents; tiered low-/high-fidelity engine evaluation; measured cost model for TP/EP/DCP. Optimizes changing model × hardware × traffic regimes. | **First-party technical report/engineering deployment claim**, not a peer-reviewed or independently reproduced result. Reported **252× is experiment throughput**, not inference TPS; **up to 2.6× TPS** is a separate selected configuration-dependent comparison. |
| **[Polymorphic Inference](https://www.together.ai/blog/polymorphic-inference)** (2026-11-04) | Production-oriented continuous adaptation of inference implementations to traffic shapes; describes deployment of TKCC on selected serverless endpoints and future routing/speculation work. | Deployment statements are attributed to Together AI. The phrase **“RSI” is the company's characterization**, not proof the optimizer agent recursively improves its own capabilities. Planned features are **not yet shipped evidence**. |
| **[Open-weight inference platform](https://www.together.ai/blog/the-production-platform-for-open-weight-ai-inference)** (2026-07-23) | Canary, blue-green/rolling updates, real-traffic A/B/shadow tests and inference deployment rollback. | Production service capabilities, not documentation of private runtime internals nor proof of a specific kernel speedup. |
| **[ThunderAgent](https://proceedings.mlr.press/v306/kang26j.html)** (ICML 2026; collaborative research) | Agent-program-aware scheduling and inference resource optimization are relevant to the group's research. | **Paper collaboration**, not inferred exclusive ownership of community vLLM/SGLang components; canonical bibliography belongs to its primary mechanism category. |

## TKCC: continual compilation and the bitter lessons

| Technical question | First-party observation |
|---|---|
| How can agents run more experiments? | Engine startup example: 467 s → 9 s with persistent hot reload; 252× experiment throughput against restart-per-trial optimization, a separate comparison from serving TPS. |
| How can fast feedback remain representative? | Few-layer screening plus more complete execution; real MoE routing and sparse-attention distributions affect kernel choices. A measured cost model narrows parallel configurations before code search. |
| Does expert scaffolding help? | On MiniMax-M3 layer 3 (B200, TP4, B=1), the ensemble's speedup falls from 5.85× to 4.75× with a knowledge base; naive ensemble 6.20× vs expert-strategy ensemble 4.92×. These are scoped ablations, not a general rejection of domain knowledge. |
| How should agents coordinate? | Frequent messages: 7.72× vs 6.20× infrequent and 4.82× no communication in the reported ablation; structured research tracking consumed up to 43% of tool calls in a trial. Simple Markdown notes and a message board reduced coordination overhead. |

Required reading: [paper §4.2–4.4, Appendix C.1–C.3](https://arxiv.org/html/2611.14681v1) · [engineering evolution (Nov 16)](https://www.together.ai/blog/road-to-together-compiler). Results are author-reported. Even after the speedup, Appendix C.3 reports agents waiting for evaluation gates for 52.7–57.0% of time in three evaluated configurations; evaluation latency remains an optimization target. The full TKCC implementation has not been verified as publicly available.

## Critical reading

The contribution to study is **experiment-loop engineering** (hot-swappable persistent execution, data-dependent fidelity tiers, configuration search under workload drift), not marketing language about an autonomous general RSI system. To establish recursive *optimizer* improvement, evaluate a **fixed optimizer** against an **experience-updated optimizer** on held-out workloads with matched LLM tokens, accelerator-hours, correctness and serving SLOs. Faster experiment iterations alone are not proof of stronger optimization intelligence.

**Source status (2026-11-27):** first-party blog/technical material; no local benchmark replication is claimed. Read alongside [autonomous engine evolution](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi).
