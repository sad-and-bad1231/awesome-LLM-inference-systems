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

**Boundary.** This is a discovery map, not an institutional ranking, provenance database or literature quality label. Credit individual papers and maintainers at the source; additions need a concrete connection to inference systems.
