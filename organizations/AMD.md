# AMD

**ROCm inference execution**, with emphasis on reusable GPU kernels and their connection to serving engines.

[← Organizations](../README.md#organizations)

| Project | Role | Official source |
|---|---|---|
| **ROCm / HIP** | Open accelerator software stack and GPU programming interface. | [ROCm](https://github.com/ROCm/ROCm) |
| **AITER** | Optimized Attention/MLA, MoE, GEMM and normalization kernels integrated with LLM serving frameworks. | [GitHub](https://github.com/ROCm/aiter) |
| **Composable Kernel** | AMD GPU kernel composition primitives, including GEMM and attention building blocks. | [GitHub](https://github.com/ROCm/composable_kernel) |
| **hipBLASLt** | Tunable matrix-multiplication backend for efficient inference computation. | [GitHub](https://github.com/ROCm/hipBLASLt) |
| **vLLM ROCm work** | ROCm-compatible LLM execution and framework integration; upstream and downstream ownership should be distinguished. | [ROCm fork](https://github.com/ROCm/vllm) |

**Boundary.** The focus is AMD-maintained tooling rather than papers by unaffiliated researchers benchmarking AMD GPUs. Reported operator speedups are vendor claims, not independently verified here.
