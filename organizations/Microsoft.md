# Microsoft

Microsoft's main **LLM inference software and systems engineering**; a small subset of wider Azure/Microsoft Research work.

[← Organizations](../README.md#organizations)

## Systems and technical work

| Work | Inference relevance | Primary source |
|---|---|---|
| **DeepSpeed Inference** | Transformer inference optimization, GPU parallelism and kernel-level acceleration; DeepSpeed itself also targets training. | [GitHub](https://github.com/microsoft/DeepSpeed) |
| **DeepSpeed-MII / FastGen** | Deployable generative inference with continuous batching, blocked KV caches and SplitFuse techniques. | [Official project](https://www.microsoft.com/en-us/research/project/deepspeed/deepspeed-mii/) · [GitHub](https://github.com/deepspeedai/DeepSpeed-MII) |
| **Splitwise** (ISCA 2024) | Split Prefill and Decode phases across suitable resource pools; joint latency and cost considerations. | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) |
| **vAttention** (ASPLOS 2025) | GPU virtual-memory approach to dynamic KV allocation without paged attention kernels. | [Publisher](https://doi.org/10.1145/3669940.3707256) |

## Libraries and models

| Project | Role | Official source |
|---|---|---|
| **ONNX Runtime** | Cross-platform inference engine and execution-provider infrastructure. | [GitHub](https://github.com/microsoft/onnxruntime) |
| **BitNet / bitnet.cpp** | Low-bit LLM architectures and CPU-oriented reference inference software. | [GitHub](https://github.com/microsoft/BitNet) |

**Boundary.** The projects above concern local execution or inference architecture; they are not a complete map of Azure's commercial services or Microsoft model releases.
