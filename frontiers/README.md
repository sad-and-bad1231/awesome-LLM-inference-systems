# Emerging inference research frontiers

**A short reading map, not a second paper database.** The [eight mechanism categories](../topics/README.md) remain the canonical bibliography. Frontiers connect reusable systems mechanisms to new workloads; the links below are pointers, not duplicate canonical admissions.

[← Home](../README.md) · [Papers by mechanism](../topics/README.md) · [Curation policy](../CURATION.md)

## Six papers to start with

Read **one anchor per frontier**, not the entire archive. These represent distinct systems questions rather than a popularity ranking.

| Frontier | Start here | Core systems question |
|---|---|---|
| **Agent-native serving** | [AgentSysBench — *From LLM Inference to Agentic Workloads*](https://arxiv.org/abs/2608.15127) (2026 **preprint**) | What is the real critical path when a session includes LLM calls, tools, sandboxes, retrieval and persistent state? |
| **Omni-modal serving** | [vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models](https://arxiv.org/abs/2602.02204) (2026 **technical report**) | How should a runtime place, connect and schedule heterogeneous modality stages? |
| **World models / interactive video** | [FAST-AR: Fast Autoregressive Video Diffusion and World Models](https://proceedings.mlr.press/v306/samuel26a.html) (ICML 2026) | Can temporal KV compression and sparse attention bound memory and latency during long rollouts? |
| **Embodied / VLA inference** | [Characterizing Vision-Language-Action Models across XPUs](https://proceedings.mlr.press/v306/zhou26e.html) (ICML 2026) | How do VLM backbone and action expert create different real-time hardware bottlenecks on robots? |
| **Agentic kernel engineering** | [KernelBench: Can LLMs Write Efficient GPU Kernels?](https://proceedings.mlr.press/v267/ouyang25a.html) (ICML 2025) | How should automated kernel generation be measured for correctness **and** execution speed? |
| **Non-AR / diffusion inference** | [BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ac8ec9b4d94c03f0af8c4fe3d5fad4fd-Abstract-Conference.html) (ICLR 2026) | Which intermediate features can be reused across denoising steps without harming quality? |

## Go deeper only when the bottleneck interests you

### Agent-native serving
- [FlashAgents](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9a6f6e0d6781d1cb8689192408946d73-Abstract-Conference.html) (MLSys 2026, **existing canonical**): overlap upstream Agent tokens with downstream incremental prefill instead of treating calls as isolated requests.
- *Missing research question:* session-aware scheduling and non-LLM compute costs versus single-request TTFT/TPOT.

### Omni-modal serving
- [Cornserve](https://arxiv.org/abs/2512.14098) (2025 **preprint**, **existing canonical**): stage DAG, modality-aware disaggregation and distributed runtime.
- *Missing research question:* full-duplex audio/video backpressure, cross-stage data movement, heterogeneous SLOs.

### Interactive world models
- [Rolling Forcing](https://proceedings.iclr.cc/paper_files/paper/2026/hash/935151cc6cb5d8b6816133b75233775a-Abstract-Conference.html) (ICLR 2026): rolling-window joint denoising and attention-sink state, with measured single-GPU real-time streaming.
- [WorldPlay](https://proceedings.mlr.press/v306/sun26az.html) (ICML 2026): history-frame context reconstruction to retain geometric consistency in real-time controllable generation.
- *Caution:* these mix model/algorithm design with execution mechanisms; they are **adjacent foundation-model inference** papers, not evidence that current LLM serving stacks already support interactive world models.

### Embodied / VLA
- The ICML 2026 XPU characterization above is the **single starting paper** in this wave. Do not pad the category with robotics benchmarks lacking inference-time hardware evidence.
- *Missing research question:* bounded action latency, edge placement, persistent visual state and vision-to-action pipeline scheduling.

### Agentic kernels
- [KernelBand](https://proceedings.mlr.press/v306/ran26b.html) (ICML 2026): hardware-aware bandit search, profile-based pruning and runtime-behavior clustering.
- [AccelOpt](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0f8426558905746fc38da5e335700aec-Abstract-Conference.html) (MLSys 2026, **existing canonical**): closed-loop Trainium NKI optimization with measured feedback.
- *Evaluation guardrail:* [KernelBench-Verified](https://arxiv.org/abs/2607.16241) (2026 **preprint**, **methodology watch; not canonically admitted here**) flags benchmark exploitation, hidden-test correctness and baseline-timing biases. Kernel microbenchmarks must not be presented as LLM end-to-end speedups.

### Diffusion / non-autoregressive inference
- [Fast-dLLM](https://nvlabs.github.io/Fast-dLLM/) (ICLR 2026, **existing canonical**): approximate KV retention and parallel token commit in diffusion language models.
- [Sangam](https://arxiv.org/abs/2607.04206) (2026 **preprint**, **existing canonical**): dLLM-specific token-budget scheduling on a serving stack.
- *Distinction:* discrete diffusion **language** decoding and continuous latent video **DiT** denoising have different state and compute patterns; neither should silently be treated as ordinary AR token serving.

## Admission boundary

1. **Foundation first:** start with one high-leverage mechanism or measurement anchor per frontier; add follow-ons only when they expose a distinct bottleneck or execution abstraction.
2. **Keep one canonical home:** [topic pages](../topics/README.md) contain the full admissions. This page is a lightweight cross-index with no separate counts.
3. **Prefer credible execution evidence:** distinguish real accelerator / end-to-end experiments from quality-only model comparisons, synthetic extrapolations and hardware simulations. Cite official proceedings when available; label preprints explicitly.
4. **Adjacent scope is narrow:** real-time world models, video diffusion and VLA enter only when their *inference-time* memory, scheduling, computation or serving mechanism is both reusable and measured. Not a general computer-vision or robotics paper list.
5. **Bound the reading load:** six entry papers first; optional follow-ups are a menu, not a reading assignment.

This is a **selective 2026-10-12 seed**, not a claim of exhaustive coverage or independently reproduced results.
