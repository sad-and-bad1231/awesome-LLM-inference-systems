# Research labs & open-source communities

An opinionated, **small starting map** of people and codebases worth following for LLM inference systems. Projects and university labs are listed separately: a runtime is not a university laboratory, and a collaboration is not company ownership.

[← Home](../README.md) · [Companies](../organizations/README.md)

## Open-source systems

| Project | Why follow | Source |
|---|---|---|
| **vLLM** | Continuous batching, paged KV memory and production LLM execution. | [Repository](https://github.com/vllm-project/vllm) |
| **SGLang** | Structured generation, RadixAttention, serving runtime and multi-node performance. | [Repository](https://github.com/sgl-project/sglang) |
| **xLLM** | High-performance serving across accelerator backends; part of the OpenAtom ecosystem. | [Repository](https://github.com/xLLM-AI/xllm) |
| **LMDeploy** | Open inference engine and optimized runtime in the OpenMMLab/InternLM ecosystem. | [Repository](https://github.com/InternLM/lmdeploy) |
| **Mooncake** | Distributed KV-cache store and transfer engine for disaggregated serving. | [Repository](https://github.com/kvcache-ai/Mooncake) |
| **LMCache** | Multi-tier and distributed KV reuse for LLM serving. | [Repository](https://github.com/LMCache/LMCache) |
| **FlashInfer** | Serving-oriented attention, sampling, and kernel primitives. | [Repository](https://github.com/flashinfer-ai/flashinfer) |
| **FlashAttention** | IO-aware exact attention kernels; historical and ongoing performance reference. | [Repository](https://github.com/Dao-AILab/flash-attention) |
| **MLC-LLM** | Compilation and runtime for portable LLM deployment. | [Repository](https://github.com/mlc-ai/mlc-llm) |
| **Ray Serve** | Application-serving framework for scalable online inference. | [Repository](https://github.com/ray-project/ray) |
| **vLLM Ascend** | Community-maintained Ascend hardware plugin; do not attribute solely to one company. | [Repository](https://github.com/vllm-project/vllm-ascend) |

## Academic research groups

| Group | Why follow | Official source |
|---|---|---|
| **UC Berkeley Sky Computing Lab** | Cloud and distributed inference; vLLM/LoRA serving lineage and systems research. | [Lab / projects](https://sky.cs.berkeley.edu/projects/) |
| **LMSYS** | Open serving systems, SGLang, evaluation and deployment engineering. | [Lab / projects](https://lmsys.org/) |
| **Stanford Hazy Research** | FlashAttention lineage, model/serving execution and IO-aware algorithm–systems thinking. | [Lab / projects](https://hazyresearch.stanford.edu/) |
| **MIT HAN Lab** | LLM quantization, efficient kernels and inference model–systems co-design. | [Lab / projects](https://hanlab.mit.edu/) |
| **Tsinghua PACMAN Group** | Parallel architecture, ML systems and performance optimization. | [Lab / projects](https://pacman.cs.tsinghua.edu.cn/) |
| **Shanghai Jiao Tong University IPADS** | Operating systems, systems infrastructure, distributed and ML systems. | [Lab / projects](https://ipads.se.sjtu.edu.cn/) |
| **ETH Zurich SPCL** | Scalable high-performance computing, communication and GPU performance. | [Lab / projects](https://spcl.inf.ethz.ch/) |
| **UW SyFI Lab** | GPU/accelerator execution, FlashInfer and production-oriented multimodal inference systems. | [Lab / publications](https://syfi.cs.washington.edu/publications/) |

## Latest group-originated inference signals (checked 2026-10-25)

This is a **discovery map**, not another canonical paper list or an institutional ranking. **TOPIC** means the *paper itself* has a primary row in [the eight selective categories](../topics/README.md); **FOUNDATION** means the paper is intentionally on the [homepage](../README.md#foundational-and-influential-papers); **REVIEW** means a publisher/author group lists a relevant source but the selective-catalog evidence gate has not been passed; **ENGINEERING** means an upstream software change or project, not necessarily a new peer-reviewed paper. A missing topic row **does not automatically justify admission**.

| Group / primary research source | Recent representative work | Repository crosswalk and what to check |
|---|---|---|
| [Berkeley Sky](https://sky.cs.berkeley.edu/publications/) | **Agentix** (NSDI'26); **SkyWalker** (EuroSys'26); **HERALD**, **K-Search** (2026); **MORI**, **Foundry**, **FreeToken**, **CommBench** (2026 papers) | **TOPIC** Agentix / SkyWalker / HERALD / K-Search. **REVIEW** MORI (agent tool-window state offload), Foundry (CUDA Graph cold start), FreeToken (edge-native MoE), CommBench (communication-kernel benchmark). [Projects](https://sky.cs.berkeley.edu/projects/) |
| [MIT HAN Lab](https://hanlab.mit.edu/publications) | **Fast-dLLM**, **Fast-dLLM v2**, **StreamingVLM**, **DuoAttention**, **Quest**, **LServe**, **QServe**; **Quant VideoGen / VLASH** (2026 adjacent video/VLA) | **TOPIC** Fast-dLLM, Quest, LServe, AWQ and SmoothQuant. **FOUNDATION** QServe (already covered on homepage; do not duplicate). **REVIEW** DuoAttention and Fast-dLLM v2. Video generation/VLA work is adjacent unless a distinct Serving execution mechanism is proved. |
| [LMSYS / SGLang](https://www.lmsys.org/) | **DFlash + Spec V2** (Jun'26); **Elastic EP**, **TorchTPU**, **Trainium Plugin** (Oct'26) | **TOPIC** DFlash; **FOUNDATION** SGLang (NeurIPS 2024); later engine/backend releases are **ENGINEERING**, not new papers by default. [Current serving comparison](https://www.lmsys.org/blog/2026-10-24-dsv41-deepinfer/) |
| [Stanford Hazy](https://hazyresearch.stanford.edu/blog) | **ThunderKittens 2.0** (Feb'26), **Next-Concept Modeling** (Oct'26), FlashAttention family / FA4 coauthor lineage | **TOPIC** ThunderKittens original and FlashAttention-4; **FOUNDATION** FlashAttention 1–3. ThunderKittens 2.0 is an **ENGINEERING update**, while NCM is a model/generation paradigm; neither automatically becomes a new Serving paper. |
| [UW SyFI](https://syfi.cs.washington.edu/publications/) | **DynaFlow**, **FlashInfer-Bench**, **Sparse Self-Speculative Decoding** (MLSys'26); **VoxServe**, **MURMUR**, **M***, **VibeServe** (2026) | First three **TOPIC**; speech, ASR, modular multimodal and agent-designed Serving candidates **REVIEW**, rather than automatic multimodal quota filling. |
| [Tsinghua PACMAN / Jidong Zhai](https://pacman.cs.tsinghua.edu.cn/~zjd/publication/) | **Taming Dynamic Diffusion LLM Inference** (ICS'26); **RoMeo** (PPoPP'26); **FlashFuser** (HPCA'26); **Lethe** (AAAI'26); **FlowPrefill** (2026 preprint) | Virtual static execution **TOPIC**. **REVIEW** RoMeo and FlashFuser for quantized kernels and cross-SM fusion; Lethe and FlowPrefill need strong modern serving baselines. Multiple papers have different coauthor institutions; the faculty publication list establishes participation, not exclusive authorship. |
| [SJTU IPADS](https://ipads.sjtu.edu.cn/pub/publication) | **SolidAttention** (FAST'26); **Simple Is Better**, **Sereno** (OSDI'26); **CHIME** (ISCA'26); **Taming Dynamism on GPUs** (SOSP'26); **RS-Infer** (ATC'26) | SolidAttention/Simple Is Better/Sereno **TOPIC**. **REVIEW** CHIME (PIM-specific hardware), cross-SM fusion (general GPU mechanism), and secure on-device RS-Infer. Vendor/prototype hardware cannot be relabeled commodity GPU/NPU benchmarks. |
| [ETH Zurich SPCL](https://spcl.inf.ethz.ch/Publications/) | **Performance Foundations of Parallel & Distributed Reasoning Language Models** (2026 preprint), in-network collective principles, performance models | **RESEARCH REFERENCE**: strong analytical/HPC source; currently no clear mandatory new LLM-online-Serving system to admit. Training/collectives/hardware studies require a concrete Serving link. |

**Screening priorities:** MORI, Foundry, DuoAttention, Fast-dLLM v2, RoMeo, FlashFuser, CHIME, and SyFI's new multimodal serving systems. Prefer complete papers, runnable patches and fair real-device benchmarking; group prestige is not a substitute.

**Boundary.** This is a discovery map, not an institutional ranking, provenance database or literature quality label. Credit individual papers and maintainers at the source; additions need a concrete connection to inference systems.
