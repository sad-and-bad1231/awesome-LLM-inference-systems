# Ant Group

Inference-relevant work from **Ant Group and its credited collaborators**. Ant also develops foundation models, but this page prioritizes executable low-level performance mechanisms over model marketing.

[← Organizations](README.md)

## First-party / jointly maintained inference mechanisms

| Source | Technical contribution | Provenance and performance boundary |
|---|---|---|
| [Humming: Fast, Flexible Kernels for Quantized Inference](https://vllm.ai/blog/2026-10-21-humming) · [code](https://github.com/vllm-project/humming) (Oct 2026) | Unified typed quantization layout + on-demand JIT kernels for dense GEMM and MoE GEMM; selects tile/pipeline execution for weight/activation precisions and hardware shapes. | **Joint Ant Group × vLLM Community** project, not exclusively Ant-owned vLLM. Integrated in the **CUDA** lane from vLLM 0.29.0; no automatic Ascend 910B2 support. |
| [Humming performance methodology](https://vllm.ai/blog/2026-10-21-humming) | Compares quantized kernel families and includes an end-to-end Qwen/DeepSeek deployment example. | The report's DeepSeek-V4.1 Flash W4A8 vs Marlin W4A16 comparison **changes activation precision**, so is not a precision-identical algorithm A/B; all numbers are author-reported. |
| [Ant model research portfolio](https://www.antgroup.com/technology/new-tech-Technology-Antfocuses-Tabcomnent-detail/20241028001) | Ling/Ring/Ming model families and sparse/MoE/long-reasoning execution demands. | Model ownership and training results are separate from an inspectable online serving algorithm; do not assign community projects to the model team without source attribution. |

## Why it matters

Humming is a concrete **format × kernel × backend** systems abstraction. Useful topics: datatype-parameterized kernel generation, JIT compilation overhead vs shape diversity, low-bit communication, dense-vs-MoE execution and whether microkernel gains survive actual batching, EP and Goodput constraints.

**Status:** shipped open-source kernel library + team-authored performance report; no independently reproduced results. Compare against tuned strong alternatives at matched precision, hardware and input shapes.
