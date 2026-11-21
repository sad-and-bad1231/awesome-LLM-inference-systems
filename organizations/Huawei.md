# Huawei

Ascend's publicly available accelerator programming and inference ecosystem. Community-maintained integrations are labeled as such, rather than described as exclusively Huawei-owned.

[← Organizations](README.md) · [← Home](../README.md)

## Vendor model family (separate from Ascend execution stack)

Huawei Cloud's [Pangu official product portfolio](https://www.huaweicloud.com/product/pangu) lists **five foundation-model classes**: **Pangu LLM**, **vision**, **multimodal**, **prediction**, and **weather**. The latter non-text categories are not automatically LLM autoregressive serving research. This is a company product-family taxonomy, not five verified downloadable checkpoints or evidence that CANN/MindIE/vLLM Ascend all share one codebase.

**Attribution boundary:** Huawei Pangu models, Huawei CANN/MindIE software, community [vLLM-Ascend](https://github.com/vllm-project/vllm-ascend), and independently owned [TileLang](https://github.com/tile-ai/tilelang) are four different provenance units. Model support requires a precise checkpoint, package and device version.

## November 10, 2026 — community vLLM-Ascend release boundary

[**vLLM-Ascend v0.32.0rc1**](https://docs.vllm.ai/projects/ascend/zh-cn/v0.32.0rc/user_guide/release_notes.html) is a **release candidate**, aligned with upstream **vLLM 0.32.0**, with documented inference integrations for **MiniMax-M3.1-Flash, Qwen3.8-Flash-Next, DeepSeek-V4.1-Flash and GLM-5.3-Flash** across explicitly listed A2/A3/950DT variants. Improvements include KV Pool, disaggregated P/D, PCP/DCP, MTP/DSpark and specific attention/kernel paths—not interchangeable model/hardware support. The pinned release image requires **CANN 9.2.1**, **torch 2.10.0 / torch-npu 2.10.0.post7** and Python 3.12. [Official installation matrix](https://docs.vllm.ai/projects/ascend/zh-cn/v0.32.0rc/getting_started/installation.html) · [community release notes](https://github.com/vllm-project/vllm-ascend/releases).

**Version & provenance discipline:** [v0.30.0 (Oct 26)](https://docs.vllm.ai/projects/ascend/en/v0.30.0/user_guide/release_notes.html) is an earlier **stable** release, while **v0.32.0rc1 is not stable**. These listed support/feature announcements do **not** establish that a user's frozen vLLM 0.23 / Ascend 910B2 / CANN 9.1.0 environment can run any new model or mechanism by a simple version substitution. The plugin is an upstream open-source **community** project with multiple contributors, not solely Huawei-owned kernel source.

## Selected first-party architecture and execution sources

| Public work | Inference relevance | Primary source |
|---|---|---|
| **[TorchNPU](https://github.com/Ascend/pytorch)** | PyTorch/Ascend backend plugin with operator dispatch, PrivateUse1 integration, memory management and distributed device execution. **GitHub is an official mirror** of the GitCode upstream. | Match torch, torch-npu, driver and CANN release versions before using with a vLLM Ascend plugin. |
| **Ascend C / CANN** | Ascend device programming and operator toolchain; fundamental kernel/runtime substrate. | [Official source](https://www.hiascend.com/en/software/cann) |
| **MindIE** | Huawei Ascend inference service/deployment software; vendor documentation is the authority for availability and compatibility. | [Official source](https://www.hiascend.com/en/software/mindie) |
| **Ascend ModelZoo** | Ascend-supported model examples and engineering references, some including inference paths. | [Official source](https://github.com/Ascend/ModelZoo-PyTorch) |
| **vLLM Ascend** | Community-maintained hardware plugin for the vLLM ecosystem; collaboration, **not** a Huawei-exclusive project. | [Official source](https://github.com/vllm-project/vllm-ascend) |
| **TileLang Ascend backend** (external ecosystem) | TileAI's public kernel compiler added **Ascend 950** support in Sept 2026, exposing GEMM/Attention examples; **not a Huawei-owned repository**, nor a demonstrated Ascend 910B2/CANN 9.1.0 deployment. Included as an important NPU programming direction. | [Maintainer's repository](https://github.com/tile-ai/tilelang) · [DeepSeek TileKernels hardware requirements](https://github.com/deepseek-ai/TileKernels) |
