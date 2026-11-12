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

## Current inference communication and runtime artifacts (source checked 2026-11-04)

| Source | Executed mechanism | Boundary |
|---|---|---|
| [ATOM](https://github.com/ROCm/ATOM) | AMD's AITER-based model inference runtime, including piecewise compile, P/D separation, TP/DP/EP and two-batch compute/communication overlap. | **AMD ROCm stack**; feature compatibility and metrics must use a pinned Instinct GPU and release. |
| [MORI](https://github.com/ROCm/mori) | Composable MORI-EP expert dispatch, MORI-IO P/D KV RDMA transfer, MORI-SHMEM and collective communication/IR integration. | Distinguish transfer/collective microbenchmarks from end-to-end Goodput, and RDMA vs fallback transport. |

**November 6 first-party inference planning signal:** [ROCm InferaSim](https://rocm.blogs.amd.com/software-tools-optimization/inferasim/README.html) ([preprint](https://arxiv.org/abs/2611.04032)) uses measured MI355X kernel/engine anchors, transfer laws and Discrete-event Simulation to project Model/Batch/P-D/Precision/SLO choices. AMD reports **11 anchors, 9.1 GPU-hours** versus **226 measured configurations, 204 GPU-hours**. **Predicted throughput is not an observed deployment throughput**; validation error, hardware topology and version scope matter. Indexed once under [Benchmarking/Simulation](../topics/benchmarking-analysis.md).

**Source status:** two public AMD-owned runtime/transport repositories. These are not NVIDIA NIXL/DeepEP drop-in equivalents on any accelerator without validation.
