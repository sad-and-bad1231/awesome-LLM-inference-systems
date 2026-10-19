# Emerging inference research frontiers

**Six selective bets on *new inference execution problems*, not six more ways to subdivide LLM serving.** As of **2026-10-19**. The [eight practical topic areas](../topics/README.md) and their **43 engineering tracks** remain the one canonical bibliography. This page only connects *new workload contracts* to original research and shipping infrastructure; it admits **zero** additional paper rows.

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
| **Agentic kernel engineering** | [KernelBand](https://proceedings.mlr.press/v306/ran26b.html) (ICML 2026; [code](https://github.com/TongmingLAIC/KernelBand)) | Search and *verify* kernels across shapes and devices; separate **semantic correctness, fair timing, memory footprint** and engine-level value from benchmark score. |

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

*Research judgement as of 2026-10-19. All acceleration numbers remain author-reported; no independent reproduction is implied. The [historical scan](2026-10-frontier-scan.md) is an archived signal log, not the current active frontier list.*
