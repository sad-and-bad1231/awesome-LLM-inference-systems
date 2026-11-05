# Cambricon / MLU

[← Organizations](README.md)

A domestic accelerator ecosystem with a public **PyTorch backend integration**; do not confuse that with a fully open modern online LLM serving engine.

| Source | System engineering | Boundary |
|---|---|---|
| [torch_mlu](https://github.com/Cambricon/torch_mlu) | MLU PyTorch extension, backend registration and dependence on CNToolkit/CNNL/CNCL/BANGC OPS. | Repository's visible default/release branch documentation includes older PyTorch/CNToolkit pairs; **not proof of current vLLM model support or CANN compatibility**. |
| [Mooncake multi-backend transport](https://github.com/kvcache-ai/Mooncake) | Community KV transport/store releases list Cambricon support among many hardware targets. | **Third-party community interoperability**, not a Cambricon-owned Mooncake implementation or independently verified performance. |

**Research fit:** operator lowering, backend ABI, tensor layouts, distributed collectives and device-specific correctness; verify exact model, hardware SKU and toolchain before throughput claims.
