# Together AI

Together AI's **open-model inference infrastructure and research on continuous engine optimization**. The company supplies hosted inference, but its hosted third-party model catalog is not a list of Together-owned architectures.

[← Organizations](README.md) · [← Frontiers](../frontiers/README.md)

## First-party inference-system signals

| Work | Mechanism relevant to inference systems | Evidence type and boundary |
|---|---|---|
| **[From Megakernels to Together Compiler](https://www.together.ai/blog/road-to-together-compiler)** (Nov 16, 2026) | Author ablation: CUDA Graphs + PDL recoup **98%** of the benefits of a monolithic megakernel on their Llama1B test; CUDA Graphs + PDL with agent-guided multi-kernel rewrites can outperform the hand-written megakernel. Production experience was narrowly limited to one 1B model, BF16, B=1, one customer; **maintenance/shape adaptability are the decisive constraints**. | [First-party engineering report](https://www.together.ai/blog/road-to-together-compiler); vendor-specific Llama1B H100/B200 findings, **not proof that monolithic kernels are always slower** and not a CANN measurement. |
| **[Together Compiler (TKCC)](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference)** (2026-11-04) | Persistent, hot-reloadable engine; parallel code-editing agents; tiered low-/high-fidelity engine evaluation; measured cost model for TP/EP/DCP. Optimizes changing model × hardware × traffic regimes. | **First-party technical report/engineering deployment claim**, not a peer-reviewed or independently reproduced result. Reported **252× is experiment throughput**, not inference TPS; **up to 2.6× TPS** is a separate selected configuration-dependent comparison. |
| **[Polymorphic Inference](https://www.together.ai/blog/polymorphic-inference)** (2026-11-04) | Production-oriented continuous adaptation of inference implementations to traffic shapes; describes deployment of TKCC on selected serverless endpoints and future routing/speculation work. | Deployment statements are attributed to Together AI. The phrase **“RSI” is the company's characterization**, not proof the optimizer agent recursively improves its own capabilities. Planned features are **not yet shipped evidence**. |
| **[Open-weight inference platform](https://www.together.ai/blog/the-production-platform-for-open-weight-ai-inference)** (2026-07-23) | Canary, blue-green/rolling updates, real-traffic A/B/shadow tests and inference deployment rollback. | Production service capabilities, not documentation of private runtime internals nor proof of a specific kernel speedup. |
| **[ThunderAgent](https://proceedings.mlr.press/v306/kang26j.html)** (ICML 2026; collaborative research) | Agent-program-aware scheduling and inference resource optimization are relevant to the group's research. | **Paper collaboration**, not inferred exclusive ownership of community vLLM/SGLang components; canonical bibliography belongs to its primary mechanism category. |

## Critical reading

The contribution to study is **experiment-loop engineering** (hot-swappable persistent execution, data-dependent fidelity tiers, configuration search under workload drift), not marketing language about an autonomous general RSI system. To establish recursive *optimizer* improvement, evaluate a **fixed optimizer** against an **experience-updated optimizer** on held-out workloads with matched LLM tokens, accelerator-hours, correctness and serving SLOs. Faster experiment iterations alone are not proof of stronger optimization intelligence.

**Source status (2026-11-04):** first-party blog/technical material; no local benchmark replication is claimed. Read alongside [autonomous engine evolution](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi).
