# Huawei

Ascend's publicly available accelerator programming and inference ecosystem. Community-maintained integrations are labeled as such, rather than described as exclusively Huawei-owned.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Ascend C / CANN** | Ascend device programming and operator toolchain; fundamental kernel/runtime substrate. | [Official source](https://www.hiascend.com/en/software/cann) |
| **MindIE** | Huawei Ascend inference service/deployment software; vendor documentation is the authority for availability and compatibility. | [Official source](https://www.hiascend.com/en/software/mindie) |
| **Ascend ModelZoo** | Ascend-supported model examples and engineering references, some including inference paths. | [Official source](https://github.com/Ascend/ModelZoo-PyTorch) |
| **vLLM Ascend** | Community-maintained hardware plugin for the vLLM ecosystem; collaboration, **not** a Huawei-exclusive project. | [Official source](https://github.com/vllm-project/vllm-ascend) |
| **TileLang Ascend backend** (external ecosystem) | TileAI's public kernel compiler added **Ascend 950** support in Sept 2026, exposing GEMM/Attention examples; **not a Huawei-owned repository**, nor a demonstrated Ascend 910B2/CANN 9.1.0 deployment. Included as an important NPU programming direction. | [Maintainer's repository](https://github.com/tile-ai/tilelang) · [DeepSeek TileKernels hardware requirements](https://github.com/deepseek-ai/TileKernels) |

**Scope:** a brief technical map of publicly documented results and first-party components; not an exhaustive release history, ownership claim for independent runtimes, or independently reproduced benchmark.
