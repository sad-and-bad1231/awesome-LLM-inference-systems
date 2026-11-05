# Inferact

[← Organizations](README.md) · [← Open-source systems](../communities/README.md)

**vLLM-core-maintainer-founded inference engineering company**; public work to follow is its open-source cross-hardware collaboration, not undocumented proprietary runtime internals.

| Public work | System contribution | Boundary |
|---|---|---|
| [vLLM TorchTPU launch](https://vllm.ai/blog/2026-10-20-vllm-torchtpu) · [source](https://github.com/vllm-project/vllm-torchtpu) | Joint **Inferact + Google** native PyTorch TPU backend, Pallas kernels, quantized GEMM/MoE, shared vLLM scheduler and KV manager. | The repository is under the **vLLM project**, not an Inferact-exclusive fork. TPU v7x tested; other TPU generations experimental as documented. |
| [Google–Inferact partnership](https://inferact.ai/news/google-tpu-partnership) (Sep 2026) | Public model-onboarding, hardware CI and contribution TPU access roadmap. | Announced roadmap/benchmark intentions are not independently reproduced production performance. |
| [Inferact platform](https://inferact.ai/) | Production inference service built around open vLLM expertise. | Proprietary service internals cannot be inferred from the commercial platform overview. |

**Research fit:** hardware-backend boundary, upstream contribution model, correctness/benchmark CI for new model families; compare pinned vLLM TorchTPU against the relevant TPU JAX stack, not against unrelated Ascend kernels. No local reproduction.
