# Emerging inference research frontiers

**Six selective bets on *new inference execution problems*, not six more ways to subdivide LLM serving.** Updated **2026-11-03** (six frontiers; agent-kernel comparator refresh). The [eight practical topic areas](../topics/README.md) and their **44 engineering tracks** remain the one canonical bibliography. This page only connects *new workload contracts* to original research and shipping infrastructure; it admits **zero** additional paper rows.

[← Home](../README.md) · [Papers by mechanism](../topics/README.md) · [Historical October 2026 signals](2026-10-frontier-scan.md)

## The frontier test

A direction earns a place here when **all three** hold:

1. **New execution contract:** the workload challenges the request → prefill → autoregressive decode loop (or substantially changes how its kernels are built). Merely improving an existing KV policy, sparse attention algorithm, or GPU backend does not qualify.
2. **Two kinds of evidence:** a traceable systems paper **and** a public implementation/credible industry serving signal, where possible. Distinguish deployed code, research prototype, preprint and hardware simulation.
3. **An unsettled systems question:** there is a meaningful unresolved scheduling, memory, correctness, communication, throughput or latency question, and a way to test it with real workloads.

**Not frontiers by themselves:** KV caching/offloading/sharing, sparse/hybrid/MLA attention, ordinary MoE/parallelism, P/D disaggregation, quantization, heterogeneous CUDA/ROCm/Ascend porting, and generic semantic response caching. These are **important active engineering tracks** in the topic pages, not new fields. Particularly, *response reuse* is not equivalent to exact *KV reuse*.

## Six active frontiers — one anchor each

| Frontier | Start here | New systems contract / unresolved decision |
|---|---|---|
| **Agent-native inference** | [ThunderAgent](https://proceedings.mlr.press/v306/kang26j.html) (ICML 2026; [code](https://github.com/ThunderAgent-org/ThunderAgent)) | Schedule the **entire agent program**, not isolated token requests. Who owns the long-lived session state, tool sandbox, KV residency and end-to-end critical path? |
| **Real-time omni-modal serving** | [vLLM-Omni Technical Report](https://arxiv.org/abs/2610.09307) (2026 **technical report**; [runtime](https://docs.vllm.ai/projects/vllm-omni/en/latest/)) | Serve asynchronous audio/video/text/action stages with **duplex streaming, backpressure, stage placement and inter-stage transfers**, not one text generation loop. |
| **Diffusion-language-model serving** | [dLLM-Serve](https://doi.org/10.1145/3797905.3800532) (ICS 2026) | Token/step/block-parallel decoding changes compute and memory demand. How should an **iteration-aware, block-aware** scheduler admit, batch and allocate memory versus an AR baseline? |
| **Interactive world-model inference** | [StreamDiffusionV2](https://mlsys.org/virtual/2026/oral/3750) (MLSys 2026; [vLLM-Omni world-model path](https://github.com/vllm-project/vllm-omni)) | An interactive, continuous environment consumes actions and emits frames over many steps. Bound **action-to-first-frame, sustained FPS, jitter, memory growth and state drift** together. |
| **Embodied / VLA action-loop inference** | [Characterizing VLA Models across XPUs](https://proceedings.mlr.press/v306/zhou26e.html) (ICML 2026) | The vision backbone and action expert have dissimilar hardware bottlenecks; meet a **hard perception-to-action deadline** on power-limited heterogeneous edge hardware. |
| **Agentic kernel engineering** | [JustGoal](https://arxiv.org/abs/2610.36434) (2026 preprint; [released kernels](https://github.com/OpenBMB/JustGoal)); compare [KDA](https://nvlabs.github.io/kda/blog/2026-09-27-kda-for-kda/), [CAKE](https://arxiv.org/abs/2608.12629), [KernelBand](https://proceedings.mlr.press/v306/ran26b.html) | When does **goal-only** optimization beat domain-specific agents, and when do compiler IR, model-agnostic diagnostics, reusable search memory or a stronger verification harness justify their cost? Judge **same foundation model, operator shapes, budget, correctness and real serving** rather than cherry-picked per-kernel wins. |

### Agent-native serving: program, state, and feedback across the engine boundary (2026 audit)

The [source-audited gap review](../reviews/AGENT_NATIVE_SERVING_GAP_AUDIT_20261103.md) screens 47 named studies, adds **14 previously missing canonical systems papers** to the eight regular classes, and cross-links eight first-party implementation signals plus six labs/source groups. These are **older 2025–2026 works uncovered in November**, not new November publications or independently reproduced speedups. Agent-native serving and **agentic kernel generation** are separate frontiers: in the first, the application *runs* agents; in the second, agents *write kernels*.

| Cross-layer question | Technical anchors already indexed once | What changes in the execution contract |
|---|---|---|
| **Program-aware scheduling and JCT** | [ThunderAgent](https://proceedings.mlr.press/v306/kang26j.html) (ICML 2026), [Agentix](https://www.usenix.org/conference/nsdi26/presentation/luo) (NSDI 2026), [Murakkab](https://www.usenix.org/conference/osdi26/presentation/chaudhry) (OSDI 2026), [SAGA](https://arxiv.org/abs/2605.00528), [TOPAS](https://arxiv.org/abs/2608.25523) | Entire tool/LLM DAG and session critical path replace a set of unrelated requests; agent JCT/success and token throughput can conflict |
| **State ownership, lifetime and reuse** | [EfficientAgent](https://arxiv.org/abs/2609.33762) (host-tier working sets), [RoleKV](https://aclanthology.org/2026.emnlp-main.1982/) (whole-KV residency), [AgentKV](https://aclanthology.org/2026.emnlp-main.2514/) (phase-aware **approximate** pruning), [CacheScout](https://arxiv.org/abs/2608.14624) (online transition learning), [Ask the Tool](https://arxiv.org/abs/2609.18849) (in-flight tool-progress signals) | KV must survive tool wait and branching with bounded HBM budget and correct tenant isolation; distinguish exact residency, approximate cache pruning, and speculative prefetch |
| **Tool ↔ engine contract** | [Sutradhara](https://arxiv.org/abs/2601.12967), [Helium](https://arxiv.org/abs/2603.16104), [HEAR](https://arxiv.org/abs/2610.06597), [Parrot](https://www.usenix.org/conference/osdi24/presentation/lin-chaofan) | Safe optional session identifiers, precedence/deadline/tool-progress hints; engine remains authority on KV ownership, scheduling and cleanup |
| **Agent workload characterization** | [TraceLab](https://arxiv.org/abs/2606.30560), [real-NPU tool re-arrival measurement](https://arxiv.org/abs/2609.34663), [AgentSysBench](https://arxiv.org/abs/2608.15127), [production task→workflow→GPU study](https://arxiv.org/abs/2609.34432), [UltraQuant](https://aclanthology.org/2026.emnlp-industry.161/) | Performance attribution crosses LLM decoding, CPU sandbox, network/tool calls and session completion; hardware gains must preserve task quality and application semantics |

**First-party adoption is implementation/version-specific:** [vLLM × AgentX](https://vllm.ai/blog/2026-09-08-vllm-agentx) characterizes session-centric code-agent traces and describes proposed future API hints; [NVIDIA Dynamo session-aware discussion](https://pytorch.org/blog/session-aware-agentic-inference-with-nvidia-dynamo/) includes a mix of shipping paths and research proposals; [SGLang Session-aware Radix Cache docs](https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/session_radix_cache.mdx) document an implementation with soft cache references, while [Programmable KV proposal](https://github.com/sgl-project/sglang/issues/27574) is **not all shipped**. Labs and vendor projects remain source references in [communities](../communities/README.md) and [organizations](../organizations/README.md), not duplicate paper counts.

**Boundary for research:** A working agent program may expose `session_id`, dependency/phase, tool progress and expiry hints; it need not expose private prompts or tool outputs. Derive GPU work-shape/TTFT/TPOT/cache/offload **and** P95 session Job Completion Time, verified success/GPU-hour and energy per successful task. Compare trace replay with closed-loop execution; fixed replay cannot establish changed future agent arrival/retry patterns. The earliest Ascend experiment should instrument current vLLM-Ascend API for metadata availability before adding a new scheduling contract.

### Kernel agents: goal-only vs. KDA vs. compiler-agent co-design

**This is one frontier, not three new categories.** The decisive research question is the *marginal value of agent-specific engineering under controlled compute/model budgets*.

| Approach | First-party source / implementation | Mechanism | Valid comparison boundary |
|---|---|---|---|
| **Goal-only (JustGoal)** | [arXiv:2610.36434](https://arxiv.org/abs/2610.36434) · [released B200 kernels](https://github.com/OpenBMB/JustGoal) | General coding agent receives goals and constraints but constructs its own optimizer/evaluator; no prebuilt domain-specific harness | On B200, reported wins versus open-source kernel libraries on 8/10 operators; in a **same-model, single-shape** Fable 5.1 comparison, KDA-0.5 reaches 0.95× of JustGoal. This is not a claim that JustGoal wins across full-shape operator workloads. |
| **KDA / Kernel Design Agents** | [NVIDIA KDA case study](https://nvlabs.github.io/kda/blog/2026-09-27-kda-for-kda/) · [source](https://github.com/NVlabs/kda/tree/260927-kda-for-kda) | Specialized tool/harness, persistent knowledge and correctness feedback; can pair with several Kernel DSLs including CAKE | Reported 2.96× vs FlashKDA on **B300** Kimi Delta Attention; not directly comparable with B200 JustGoal or to full vLLM throughput. KDA reports verifier-overfit candidates it explicitly rejected. |
| **CAKE (NVIDIA/CMU)** | [arXiv:2608.12629](https://arxiv.org/abs/2608.12629) | Co-design of Agent + typed schedule IR + compiler diagnostics and reusable verifier | Author reports B200 Flash-KMeans and Kimi Delta Attention kernel / serving validation; token budgets, task coverage and availability of the core compiler differ from JustGoal. |
| **CANNBot-CAKE (Ascend; distinct project)** | [arXiv:2610.31034](https://arxiv.org/abs/2610.31034) | CANN-specific multi-DSL generation/evolution with curated knowledge | Reports CANN-Bench hidden correctness on **Ascend 950PR**; not NVIDIA CAKE, not verified on 910B2 and not online vLLM Goodput. |

**Name/identity check:** `ForgeKernel` (user-observed name) has **not** been tied to a uniquely verifiable official paper or code identity in this review. Do not silently equate it with JustGoal or the distinct [Kernel Forge](https://arxiv.org/abs/2607.24762) paper. Keep that project as an unresolved discovery lead until its original URL is checked. Canonical paper entries remain in the existing Kernels & Compilers category, never duplicated here.

**New benchmark obligation:** add same-model and same-token-budget A/B, hidden distribution and output-equivalence tests, **single shape vs full operator**, compilation/search cost, and engine-level throughput/latency with composed winners. [FastKernels](https://fastkernels.github.io/) highlights that individually faster kernels can fail or regress after composition. A leaderboard score alone is not validated production inference speedup.

The anchors are a **starter reading path, not new canonical admission**. An ICML paper with a kernel benchmark is not evidence of vLLM end-to-end Goodput; a video model demo is not proof of multi-session production serving.

## What remains open (researcher-facing)

| If you work on... | First engineering question | Minimal defensible experiment |
|---|---|---|
| Agent-native inference | What state survives LLM → tool → LLM and who pays for eviction/rebuild? | Multi-turn agent trace; session completion time/P95, cached tokens, GPU idle, tool startup, GPU memory, and interference at equal quality |
| Omni-modal serving | Which stage stalls the live session when frame/audio arrivals become bursty? | Stage-by-stage timeline; P95 event-to-first-output, interruption latency, jitter, backpressure, dropped/late chunks and E2E quality |
| dLLM | Does AR batch/KV scheduling remain optimal when one request emits/updates whole token blocks? | Equal model/quality constraints; memory curve per step, batch efficiency, latency, throughput and output quality against native dLLM runtime |
| Interactive worlds | When must old latent/attention state be refreshed to prevent visual drift? | Long interactive action trace; sustained FPS, action latency P95, memory, consistency/drift checks and controlled action changes |
| VLA execution | Can the compute-bound backbone overlap with the memory-bound action expert within deadline? | Hardware-traced stage latency, missed deadline rate, energy/action and action quality on embedded devices |
| Agentic kernels | Does the generated code remain correct and fast outside public test tensors? | Hidden distributions + precision parity, multi-shape benchmarks, real profiler evidence, compilation cost and downstream serving impact |

**World-model state-management follow-on (October 2026):** [WorldPager](https://arxiv.org/abs/2610.35529) explores pose-predictable KV-prefetch into NVMe-backed memory for long interactive sessions on a consumer GPU. It is an **adjacent real-hardware experiment**, with int4 quality limitations, and already has its one canonical entry under KV Cache & Context Memory; it is not a seventh frontier or a claim about text LLM KV reuse.

## Watching, not yet promoting

- **Reasoning/test-time-compute control.** [Plan and Budget](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ae8d4084f418bb51575c2ca6c658a05b-Abstract-Conference.html) (ICLR 2026) demonstrates adaptive reasoning budgets, but it is primarily a **model-level quality–compute algorithm**. Promote when a real inference runtime jointly optimizes correctness/quality, token budgets, SLO and co-tenant requests across workloads; avoid mistaking fewer tokens for a proven serving-system breakthrough.
- **RL rollout / online-serving infrastructure convergence.** [Weave](https://www.usenix.org/conference/osdi26/presentation/wu-tianyuan) (OSDI 2026) and [llm-d time-slicing](https://llm-d.ai/blog/rl-post-training-co-operative-time-slicing) provide serious systems evidence for **RL rollout–training job co-scheduling**, not proof of simultaneously protecting **live user-serving SLOs**. Keep as an inference/training crossover watch until that boundary is evaluated.
- **Kernel-agent benchmark trust.** [KernelBench-Verified](https://arxiv.org/abs/2607.16241) (2026 **preprint**) is a high-priority *evaluation check* under agentic kernels, **not** a seventh frontier. Reward hacking, baseline precision and hidden input tests are admission criteria.

## Where the previously named "frontiers" went

| Removed frontier heading | Its proper home |
|---|---|
| **KV as a distributed object** | [KV Cache & Context Memory](../topics/kv-cache-memory.md) → Distributed KV Sharing & Transfer / Offloading & Tiered Storage |
| **Sparse & hybrid attention at production scale** | [Kernels & Compilers](../topics/kernels-compilers.md), [MoE & Sparse Execution](../topics/moe-sparse-execution.md), and existing KV tracks |
| **Vendor/edge heterogeneity as a standalone frontier** | [Distributed & Disaggregated Serving](../topics/distributed-serving.md), [Runtime & Scheduling](../topics/runtime-scheduling.md); edge **VLA control loops** remain distinct |
| **Semantic caching as a new KV frontier** | A separate *response-quality/freshness* concern; not an exact Attention KV system nor independently frontier-worthy without a new execution contract |

## Update rule

**Maintain only 5–7 active frontiers.** To promote an item, document its *new workload/contract*, a primary systems paper, a usable public stack or real hardware receipt, strong existing baselines, and a testable unresolved bottleneck. To demote: if vLLM/SGLang/Omni/Dynamo/llm-d ship it as routine infrastructure and newer papers simply improve its policy or kernel, put it back in its existing engineering track. Do **not** add categories or papers here automatically.

*Research judgement updated 2026-11-03. All acceleration numbers remain author-reported; no independent reproduction is implied. The [historical scan](2026-10-frontier-scan.md) is an archived signal log, not the current active frontier list.*
