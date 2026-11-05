# Moore Threads

MUSA accelerator software and hardware-backend engineering for LLM inference. It belongs to the industrial inference map as a **device/porting and kernel-stack vendor**, not a foundation-model owner.

[← Organizations](README.md)

## Public software stack

| Code / source | Systems contribution | Boundary |
|---|---|---|
| [vllm-musa](https://github.com/MooreThreads/vllm-musa) | MUSA-oriented vLLM fork covering backend adaptation, model execution and serving paths. | **Fork/port**, not the upstream vLLM default or proof every recent model feature works at parity; check branch, MUSA SDK and device version. |
| [musa-aiter](https://github.com/MooreThreads/musa-aiter) | GPU kernel/tooling interoperability targeted at MUSA hardware and AI inference primitives. | Public repository is evidence of active backend engineering, **not** a validated performance-equivalent ROCm AITER or CUDA deployment. |
| [MATE](https://github.com/MooreThreads/mate) | MUSA AI Tensor Engine implementation in the vendor's public organization. | Read executable sources and support matrix before attributing novel algorithmic mechanisms or end-to-end gains. |
| [Official GitHub organization](https://github.com/MooreThreads) | Central version and ownership index for MUSA compilers, backend libraries and model-runtime integrations. | Source identity does not certify production deployment or reproducibility on unrelated accelerator families. |

## Research reading angle

Track **backend API compatibility, operator lowering, quantization/memory layouts, dynamic scheduling, and kernel-to-engine composition**. Compare full output correctness and TTFT/TPOT/goodput on exact device/driver versions, not CUDA numbers extrapolated to MUSA.

**Status:** first-party software artifacts; no local performance replication.
