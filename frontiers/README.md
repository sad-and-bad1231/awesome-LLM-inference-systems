# Emerging inference research frontiers

[← Home](../README.md) · [Technical Topics](../topics/README.md)

Frontiers track new execution contracts and system-optimization lifecycles that cannot be adequately described by a single established topic. They are not another bibliography. Concrete papers and implementations retain their primary homes in the technical topics.

## The frontier test

A direction belongs here when it changes the unit of execution, workload contract or optimization lifecycle; has a traceable technical mechanism with evidence appropriate to its maturity; and exposes a falsifiable unresolved systems problem. Novelty alone is insufficient. Demote established mechanisms when their own technical topic can explain the research question.

## Agent-native inference systems

The unit of execution becomes a long-lived agent program rather than an isolated request. Session state, tool execution, cache residency, dependency scheduling and harness–engine coordination share an end-to-end critical path.

- [ThunderAgent](https://proceedings.mlr.press/v306/kang26j.html) · [code](https://github.com/ThunderAgent-org/ThunderAgent): program-aware scheduling.
- [MORTIS](https://arxiv.org/abs/2611.08638): typed agent dataflow and cache residency; [Evolving Infra](https://arxiv.org/abs/2611.12304): P/D and KV placement for agent traffic.
- **Open question:** how should the harness and runtime jointly own persistent state, tool waits and resources? Evaluate session completion, GPU idle time, cache reuse and interference under equivalent task quality.

Mechanism homes: [Runtime](../topics/runtime-scheduling.md), [KV](../topics/kv-cache-memory.md), [Distributed Serving](../topics/distributed-serving.md).

## Autonomous inference optimization & RSI

### Autonomous inference-engine evolution: separate engine evolution from RSI

Whole-engine optimization changes kernels, execution policy and configuration together through repeated measurement. Distinguish an improving engine artifact, an optimizer that acquires transferable search competence, and recursive self-improvement of that optimizer; the first does not establish the latter two.

| Representative work | Contribution / boundary |
|---|---|
| [SEIS](https://arxiv.org/abs/2610.04646) · [code/history](https://github.com/nehzux/SEIS) | Fixed coding agent inherits engine code and experiment reports; the result concerns mini-SGLang on a particular model/workload. |
| [Together Compiler](https://arxiv.org/abs/2611.14681) · [engineering report](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference) | Persistent hot-swappable runtime and mixed-fidelity evaluation; experiment throughput is not inference TPS. |
| [ERNIE Evolve](https://ernie.baidu.com/research/posts/ernie-evolve/) · [Baidu profile](../organizations/Baidu.md) | Director/Selector/Executor, independent evaluation and reusable experiment history; first-party results, not independent reproduction. |
| [VibeServe](https://arxiv.org/abs/2605.06068) · [code](https://github.com/uw-syfi/vibe-serve) | Nested design and implementation search for specialized inference stacks. |
| [InferenceBench](https://arxiv.org/abs/2607.20468) · [benchmark](https://inferencebench.ai/) | Fixed-budget optimization; compare against conventional tuning and strong baselines. |
| [RSIBench-Infra](https://arxiv.org/abs/2611.24395) · [EngineAgent](https://arxiv.org/abs/2611.14356) | Infrastructure task evaluation and cross-layer model enablement, not proof of recursive agent self-improvement. |

**Open question:** does inherited experience improve future optimization under equal search budgets, rather than merely improving a code checkpoint? Compare fresh agents, artifact inheritance, strategy memory and conventional search on held-out workloads with correctness, end-to-end goodput and accelerator-hour accounting.

Kernel-specific agents have graduated to [Kernels & Compilers](../topics/kernels-compilers.md#kernel-agents-goal-only-vs-kda-vs-compiler-agent-co-design).

## Beyond autoregressive inference

[Diffusion-language-model serving: dLLM-Serve](https://doi.org/10.1145/3797905.3800532). Token/block-parallel updates create different step dependencies, memory lifetimes and scheduling constraints from AR decoding.

**Open question:** how should admission, batching and memory allocation adapt to the new iteration structure under comparable output quality?

Mechanism homes: [Decoding](../topics/decoding-acceleration.md), [Runtime](../topics/runtime-scheduling.md).

## Real-time multimodal & interactive inference

| Direction | Representative source | New contract |
|---|---|---|
| Omni-modal serving | [vLLM-Omni report](https://arxiv.org/abs/2610.09307) · [runtime](https://docs.vllm.ai/projects/vllm-omni/en/latest/) | Duplex streaming, asynchronous stages, inter-stage transfer and backpressure. |
| Interactive world models | [StreamDiffusionV2](https://mlsys.org/virtual/2026/oral/3750) | Continuous action-conditioned frame generation; latency, FPS, jitter and persistent state. |
| Embodied / VLA inference | [Characterizing VLA Models across XPUs](https://proceedings.mlr.press/v306/zhou26e.html) | Perception-to-action deadlines, heterogeneous stage placement and power limits. |

**Open questions:** quantify event-to-output latency, sustained throughput, deadline misses, state drift and quality under real interactive workloads. Do not treat model demos or adjacent video-generation algorithms as verified serving-system improvements.

## Watching, not yet promoting

- [Reasoning/test-time-compute control](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ae8d4084f418bb51575c2ca6c658a05b-Abstract-Conference.html): joint quality, token budget and multi-tenant serving SLOs.
- [RL rollout / online-serving convergence](https://www.usenix.org/conference/osdi26/presentation/wu-tianyuan) · [llm-d time-slicing](https://llm-d.ai/blog/rl-post-training-co-operative-time-slicing): sharing resources while protecting live user-serving SLOs.

## Update rule

Keep this page selective; retain source anchors, new systems contracts and decisive research questions. Track individual PRs and mechanism improvements in their technical topics. Historical evidence is available in [October scan](2026-10-frontier-scan.md), [review receipts](../reviews/README.md) and the [pre-reorganization frontier snapshot](https://github.com/sad-and-bad1231/awesome-LLM-inference-systems/blob/21dbb9c17bc402ccd84b791d2804020d9794e3ed/frontiers/README.md).
