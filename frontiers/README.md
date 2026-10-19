# Emerging inference research frontiers

**A short reading map, not a second paper database.** The [eight mechanism categories](../topics/README.md) remain the canonical bibliography. Frontiers connect reusable systems mechanisms to new workloads; the links below are pointers, not duplicate canonical admissions.

[← Home](../README.md) · [Papers by mechanism](../topics/README.md) · [Curation policy](../CURATION.md) · [Frontier scan, October 2026](2026-10-frontier-scan.md)

## What the industry is shipping right now (2026-10 refresh)

Read the first-party signals before the papers — they say what the frontier *is*.

- **vLLM's own roadmap** names the coming quarter's work directly: [vLLM Roadmap Q4 2026](https://github.com/vllm-project/vllm/issues/61024).
- **KV became a distributed, first-class object.** [llm-d v0.5 — Sustaining Performance at Scale](https://llm-d.ai/blog/llm-d-v0.5-sustaining-performance-at-scale) runs a three-tier GPU → CPU → **filesystem** KV hierarchy on top of [vLLM's KV offloading connector](https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html), so replicas *hydrate* instead of re-prefilling; [Peer-to-Peer KV Cache Sharing](https://llm-d.ai/blog/p2p-kv-cache-sharing-llm-d) turns one instance's eviction into another's prefix hit; [NVIDIA Dynamo's Flash Indexer](https://docs.dynamo.nvidia.com/dynamo/v1.4.0/digest/flash-indexer) treats KV location as the routing substrate.
- **Scheduling policy is now the product surface.** [llm-d's Token-Aware Routing](https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing) and [Predicted-Latency Based Scheduling](https://llm-d.ai/blog/predicted-latency-based-scheduling-for-llms) shift the control variable from queue depth to predicted TTFT/TPOT; [BLIS](https://llm-d.ai/blog/blis-evolving-llm-d-at-simulation-speed) evolves the whole policy offline in simulation before shipping it.
- **Rollout fleets and serving fleets are the same hardware.** [llm-d's RL time-slicing](https://llm-d.ai/blog/rl-post-training-co-operative-time-slicing) reports ~40% more post-training experiments on identical GPUs by co-tenanting rollout with online serving.
- **Heterogeneity is normal, not exceptional.** [llm-d across three GPU vendors](https://llm-d.ai/blog/heterogeneous-inference-3-vendor-sovereign-cluster), [vision-heavy Kimi-VL with heterogeneous E/PD](https://llm-d.ai/blog/scaling-vision-heavy-kimi-vl-with-heterogeneous-epd), [GLM-5.1-FP8 wide-EP on 64 MI300X](https://rocm.blogs.amd.com/software-tools-optimization/di-glm-wideep/README.html), [MoE inference with Dynamo on Google Cloud A4X](https://cloud.google.com/blog/products/compute/scaling-moe-inference-with-nvidia-dynamo-on-google-cloud-a4x), [MoE performance leaps on Blackwell](https://developer.nvidia.com/blog/delivering-massive-performance-leaps-for-mixture-of-experts-inference-on-nvidia-blackwell/).

Three cross-cutting shifts are visible across independent first-party sources:

1. **The unit of optimisation moved from the request to the session.** Cache-aware *and* session-aware routing ship together; prefix reuse is the default path and the open problems are eviction, freshness and fairness.
2. **The memory hierarchy, not FLOPS, is the binding constraint.** Tiered KV, P2P KV sharing, semantic caches and 4-bit KV offload are one idea: decouple cache capacity from HBM.
3. **The fleet is heterogeneous and co-tenanted.** Mixed vendors, mixed E/PD roles, RL rollouts sharing GPUs with online serving — SLO protection under co-tenancy is the new scheduling problem.

## Nine anchors, one per frontier

Read **one anchor per frontier**, not the entire archive. These represent distinct systems questions rather than a popularity ranking.

| Frontier | Start here | Core systems question |
|---|---|---|
| **Agent-native serving** | [AgentSysBench — *From LLM Inference to Agentic Workloads*](https://arxiv.org/abs/2608.15127) (2026 **preprint**) | What is the real critical path when a session includes LLM calls, tools, sandboxes, retrieval and persistent state? |
| **Omni-modal serving** | [vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models](https://arxiv.org/abs/2602.02204) (2026 **technical report**) | How should a runtime place, connect and schedule heterogeneous modality stages? |
| **World models / interactive video** | [FAST-AR: Fast Autoregressive Video Diffusion and World Models](https://proceedings.mlr.press/v306/samuel26a.html) (ICML 2026) | Can temporal KV compression and sparse attention bound memory and latency during long rollouts? |
| **Embodied / VLA inference** | [Characterizing Vision-Language-Action Models across XPUs](https://proceedings.mlr.press/v306/zhou26e.html) (ICML 2026) | How do VLM backbone and action expert create different real-time hardware bottlenecks on robots? |
| **Agentic kernel engineering** | [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://proceedings.mlr.press/v267/ouyang25a.html) (ICML 2025) | How should automated kernel generation be measured for correctness **and** execution speed? |
| **Non-AR / diffusion inference** | [BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html) (ICLR 2026) | Which intermediate features can be reused across denoising steps without harming quality? |
| **RL rollout × serving co-tenancy** | [Weave: Efficient Co-Scheduling for Disaggregated RL Post-Training](https://www.usenix.org/conference/osdi26/presentation/wu-tianyuan) (OSDI 2026) | Who yields compute, KV and bandwidth when rollout and online serving share one fleet? |
| **KV as a distributed object** | [llm-d v0.5 — Sustaining Performance at Scale](https://llm-d.ai/blog/llm-d-v0.5-sustaining-performance-at-scale) (2026 engineering blog) | What is the right index, placement and freshness policy when KV lives across GPU, CPU, disk and peers? |
| **Sparse & hybrid attention at production scale** | [Native Hybrid Attention for Efficient Sequence Modeling](https://aclanthology.org/2026.acl-long.176/) (ACL 2026) | Which attention layers can be linear/sparse without breaking long-context serving, and what does that do to the KV hierarchy? |

## Go deeper only when the bottleneck interests you

### Agent-native serving
- [FlashAgents](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9a6f6e0d6781d1cb8689192408946d73-Abstract-Conference.html) (MLSys 2026, **existing canonical**): overlap upstream Agent tokens with downstream incremental prefill instead of treating calls as isolated requests.
- [SMetric — Balanced Session-centric Scheduling](https://arxiv.org/abs/2607.08565) (2026 **preprint**): the scheduling unit becomes the session, not the request.
- [Helios: Exposing Context Lifecycles for Memory-Efficient Agentic LLM Serving](https://dl.acm.org/doi/10.1145/3816891.3834846) (ICPP 2026 workshop): context has a lifecycle (open → grow → idle → dead); serving systems that cannot see it over-provision KV.
- [NVIDIA Dynamo — Full-Stack Optimizations for Agentic Inference](https://docs.dynamo.nvidia.com/dynamo/dev/digest/agentic-inference) and [llm-d — Serving GLM-5.2 for Agentic Workloads](https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d): the two big control planes describe their agentic paths.
- *Missing research question:* session-aware scheduling and non-LLM compute costs versus single-request TTFT/TPOT.

### Omni-modal serving
- [Cornserve](https://arxiv.org/abs/2512.14098) (2025 **preprint**, **existing canonical**): stage DAG, modality-aware disaggregation and distributed runtime.
- [llm-d — Serving Multimodal at Scale](https://llm-d.ai/blog/serving-multimodal-at-scale-in-llm-d): production framing of the same problem.
- *Missing research question:* full-duplex audio/video backpressure, cross-stage data movement, heterogeneous SLOs.

### Interactive world models
- [Rolling Forcing](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) (ICLR 2026): rolling-window joint denoising and attention-sink state, with measured single-GPU real-time streaming.
- [WorldPlay](https://proceedings.mlr.press/v306/sun26az.html) (ICML 2026): history-frame context reconstruction to retain geometric consistency in real-time controllable generation.
- [StreamDiffusionV2](https://mlsys.org/virtual/2026/oral/3750) (MLSys 2026 oral): a streaming *system* for dynamic and interactive video generation, not just a model.
- [LongLive: Real-time Interactive Long Video Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/91a1610c6ed9e02d33f826b46f472b92-Abstract-Conference.html) (ICLR 2026): long-horizon real-time interactivity.
- [MoWorld: A Flash World Model](https://www.semanticscholar.org/paper/MoWorld%3A-A-Flash-World-Model-Moxin-Ji/5b2d839de22b93c8609f5103d01daeca6001eda0): MoE applied to world modelling — sparsity meets rollout.
- [FLEX-WAM: Flexible Block-Causal World–Action Models](https://arxiv.org/abs/2610.05483) (2026 **preprint**): world–action coupling for long-horizon imagination.
- ["The Cost of Dreaming" survey](https://ieeexplore.ieee.org/document/11663588) (2026): computational constraints across generative and latent world models — the best single map of this frontier's systems limits.
- *Caution:* these mix model/algorithm design with execution mechanisms; they are **adjacent foundation-model inference** papers, not evidence that current LLM serving stacks already support interactive world models.

### Embodied / VLA
- The ICML 2026 XPU characterization above is the **single starting paper** in this wave. Do not pad the category with robotics benchmarks lacking inference-time hardware evidence.
- [A Scalable VLA Edge Processor with Token Filtering and Hybrid Processing-Near-Memory for 6.7-ms Perception-to-Action Latency](https://ieeexplore.ieee.org/document/11577377) (2026): the silicon end of the same question.
- *Missing research question:* bounded action latency, edge placement, persistent visual state and vision-to-action pipeline scheduling.

### Agentic kernels
- [KernelBand](https://proceedings.mlr.press/v306/ran26b.html) (ICML 2026): hardware-aware bandit search, profile-based pruning and runtime-behavior clustering.
- [AccelOpt](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0f8426558905746fc38da5e335700aec-Abstract-Conference.html) (MLSys 2026, **existing canonical**): closed-loop Trainium NKI optimization with measured feedback.
- [AlphaCu: Transformation-Driven Synthesis for LLM-Based GPU Kernel Generation](https://dl.acm.org/doi/10.1145/3832783.3837433) (2026) and [Towards Automated Kernel Generation in the Era of LLMs](https://www.ijcai.org/proceedings/2026/895) (IJCAI 2026): synthesis frameworks and a field survey.
- *Evaluation guardrail:* [KernelBench-Verified](https://arxiv.org/abs/2607.16241) (2026 **preprint**, **methodology watch; not canonically admitted here**) flags benchmark exploitation, hidden-test correctness and baseline-timing biases. Kernel microbenchmarks must not be presented as LLM end-to-end speedups.

### Diffusion / non-autoregressive inference
- [Fast-dLLM](https://nvlabs.github.io/Fast-dLLM/) (ICLR 2026, **existing canonical**): approximate KV retention and parallel token commit in diffusion language models.
- [Sangam](https://arxiv.org/abs/2607.04206) (2026 **preprint**, **existing canonical**): dLLM-specific token-budget scheduling on a serving stack.
- [dLLM-Serve: Bridging the Memory Gap in Diffusion Language Model Serving](https://dl.acm.org/doi/full/10.1145/3797905.3800532) (ICS 2026): the first *serving-system* treatment — diffusion decoding changes the memory curve, and AR-tuned KV managers mis-predict it.
- [DiffusionGemma: The Developer Guide](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/) (Google, 2026): a major vendor shipping a dLLM with developer-facing inference guidance.
- *Distinction:* discrete diffusion **language** decoding and continuous latent video **DiT** denoising have different state and compute patterns; neither should silently be treated as ordinary AR token serving.

### RL rollout × serving co-tenancy (new)
- [ROSE: Rollout On Serving GPUs via Cooperative Elasticity for Agentic RL](https://preprints.kavlimeetings.org/2026/05/07/all/nano/caltech/261830/) (2026): elasticity across the serving/rollout boundary.
- [llm-d — RL Post-Training: Co-Operative Time-Slicing](https://llm-d.ai/blog/rl-post-training-co-operative-time-slicing) and [Run 40% more post-training experiments on the same GPUs](https://llm-d.ai/blog/increase-researcher-velocity-rl-llm-d-time-slicing): production time-slicing results.
- *Why it matters:* preemption, KV residency and SLO protection under co-tenancy are unresolved — and every lab that serves *and* trains hits them daily.

### KV as a distributed object (new)
- [llm-d — Native KV Cache Offloading to Any Filesystem](https://llm-d.ai/blog/native-kv-cache-offloading-to-any-file-system-with-llm-d) and [vLLM KV Offloading Connector](https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html): the interface layer.
- **Semantic caching is arriving as a serving tier:** [SmartCache](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fb74b63d225f846e6032bf3e3ab0f4ec-Abstract-Conference.html) (NeurIPS 2025) and [CacheSense: Freshness-Aware Semantic Caching with Selective Invalidation](https://ieeexplore.ieee.org/document/11621808) (2026). The open question is *invalidation*, not hit rate — a stale semantic hit is worse than a miss.
- *Missing research question:* correctness under approximate/semantic KV reuse, and cache coherence across tenants.

### Sparse & hybrid attention at production scale (new)
- [MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference](https://arxiv.org/abs/2605.07363) (2026 **preprint**).
- [NVIDIA TensorRT-LLM — Temporal Correlation Meets Sparse Attention: Guess-Verify-Refine Top-K for Blackwell](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog21_Temporal_Correlation_Meets_Sparse_Attention.html): a vendor shipping learned/temporal sparsity in its production stack.
- [DeepSeek-V3.2 DSA / lightning indexer](https://github.com/deepseek-ai) is the production anchor for learned sparse attention; [AMD's 64M-token context with 4-bit KV offloading](https://devcommunity.amd.com/t/llm-inference-at-scale-on-amd-instinct-multi-node-moe-64m-token-context-and-4-bit-kv-offloading/939) shows the memory side.
- *Missing research question:* how hybrid/sparse attention changes the KV cache hierarchy — sparse attention makes *some* KV cheap and makes eviction policy harder, not easier.

### Watch list (too early to anchor)
- **Test-time-scaling serving:** [ThinkBooster](https://aclanthology.org/2026.acl-demo.70/) (ACL 2026 demo), [FastTTS](https://dlnext.acm.org/doi/10.1145/3779212.3790161) (ASPLOS 2026) — reasoning budgets as a first-class scheduling dimension.
- **Observability:** [llm-d — End-to-End and Fine-Grained Tracing](https://llm-d.ai/blog/end-to-end-and-fine-grained-tracing-in-llm-d), [Opik: durable LLM observability at scale](https://ieeexplore.ieee.org/document/11502391) — session-level tracing is becoming table stakes.
- **On-device:** [MLPerf Mobile v6.0 — new GenAI benchmarks for on-device LLMs](https://mlcommons.org/2026/06/mlperf-mobile-v6/) — measurement finally catching up with on-device deployment.

## Admission boundary

1. **Foundation first:** start with one high-leverage mechanism or measurement anchor per frontier; add follow-ons only when they expose a distinct bottleneck or execution abstraction.
2. **Keep one canonical home:** [topic pages](../topics/README.md) contain the full admissions. This page is a lightweight cross-index with no separate counts.
3. **Prefer credible execution evidence:** distinguish real accelerator / end-to-end experiments from quality-only model comparisons, synthetic extrapolations and hardware simulations. Cite official proceedings when available; label preprints explicitly.
4. **Adjacent scope is narrow:** real-time world models, video diffusion and VLA enter only when their *inference-time* memory, scheduling, computation or serving mechanism is both reusable and measured. Not a general computer-vision or robotics paper list.
5. **Bound the reading load:** nine entry papers first; optional follow-ups are a menu, not a reading assignment.

This is a **selective seed refreshed 2026-10-18 from first-party industry signals**, not a claim of exhaustive coverage or independently reproduced results. For the dated, lighter-weight scan of signals that have *not* been admitted here, see [Frontier scan — October 2026](2026-10-frontier-scan.md).
