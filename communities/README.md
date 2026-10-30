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

## Research labs and source-linked systems signals

This is a **navigation crosswalk, not a second paper bibliography or institutional ranking**. A paper appears in an [existing canonical topic](../topics/README.md) only once, regardless of how many labs collaborated. A **BLOG/ENGINEERING** signal is not automatically a peer-reviewed paper, and **REVIEW/HOLD** is not admission.

| Research group | Inference-system focus | Representative verified source and its status |
|---|---|---|
| [UC Berkeley Sky](https://sky.cs.berkeley.edu/publications/) | Cloud inference, edge MoE and distributed serving | [CommBench](https://arxiv.org/abs/2608.04450) and [FreeToken](https://arxiv.org/abs/2608.16157) — **TOPIC**, already indexed; collaboration does not imply exclusive lab ownership |
| [LMSYS / SGLang](https://lmsys.org/) | Runtime, speculative decoding, serving infrastructure | [SGLang project](https://github.com/sgl-project/sglang) — **ENGINEERING**; separately cite published papers where applicable |
| [Stanford Hazy](https://hazyresearch.stanford.edu/) | IO-aware attention and generation mechanisms | [NCM](https://arxiv.org/abs/2610.14162) — **TOPIC / ADJACENT**; different trained model/tokenizer, not an existing-LLM kernel speedup |
| [MIT HAN Lab](https://hanlab.mit.edu/) | Quantization, efficient kernels, edge/video/robot inference | [Quant VideoGen](https://proceedings.mlr.press/v306/xi26f.html) — **TOPIC / ICML 2026 / ADJACENT**; [VLASH](https://arxiv.org/abs/2512.01031) — **TOPIC / VLA-ADJACENT**, lab-listed IROS |
| [Tsinghua PACMAN](https://pacman.cs.tsinghua.edu.cn/) | AI compilers, GPU/NPU mapping, parallel runtime | [Group publication source](https://pacman.cs.tsinghua.edu.cn/~zjd/publication/) — **DISCOVERY**; verify final venue and exact hardware per paper |
| [SJTU IPADS](https://ipads.sjtu.edu.cn/pub/publication) | OS, storage, distributed inference and reproducible evaluation | [Group publications](https://ipads.sjtu.edu.cn/pub/publication) — **DISCOVERY**; CHIME remains **REVIEW** pending hardware-scope clarity |
| [ETH Zurich SPCL](https://spcl.inf.ethz.ch/Publications/) | HPC collectives, communication and performance modeling | [Official publications](https://spcl.inf.ethz.ch/Publications/) — **DISCOVERY/REFERENCE**, not automatic LLM Serving admission |
| [UW SyFI](https://syfi.cs.washington.edu/publications/) | FlashInfer, agentic serving and multimodal execution | [VibeSys](https://syfi.cs.washington.edu/blog/2026-10-08-qwen35-mi300a/) and [ServingStudio](https://syfi.cs.washington.edu/blog/2026-09-24-introducing-servingstudio/) — **BLOG/ENGINEERING**, no invented formal paper identity |
| [CMU InfiniAI](https://www.infini-ai-lab.cmu.edu/publications.html) | Program IR and agent-driven distributed multimodal inference | [FlashRT](https://arxiv.org/abs/2607.18171) — **TOPIC / PREPRINT**; distinct from FlashRT-PAI. [STAPLE](https://arxiv.org/abs/2610.12599) remains **HOLD** for system/architecture attribution |

**Status vocabulary:** **TOPIC** = indexed paper in one of eight topic tables; **FOUNDATION** = intentionally on the homepage; **ENGINEERING/BLOG** = software or first-party technical post; **DISCOVERY/REFERENCE** = useful source, no automatic admission; **REVIEW/HOLD** = insufficient source/evaluation/fit. Sub-labels such as *ADJACENT* or *PREPRINT* state scope and publication status, not reproduction.

Previous dated per-lab work lists and their explanations: [archived Oct 25/30 signals](../reviews/archive/LAB_SIGNALS_20261030.md). The [Oct 30 G0–G5 review](../reviews/ARXIV_LAB_SWEEP_20261030.md) owns individual KEEP/HOLD decisions. Update the canonical **paper row**, not a second paper inventory here.
