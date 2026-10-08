# Kernels & Compilers

Efficient execution of model operators: attention, GEMM, tiling, fusion, hardware-aware mapping and compilation.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Compute kernels; technical contribution changes the GPU/NPU execution path, not only the model architecture.

**Foundational context.** See also: [FlashAttention (2022), FlashAttention-2 (2024), FlashAttention-3 (2024), FlashInfer (2025)](../README.md#foundational-and-influential-papers).

## Newly admitted · October 2026 (2)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [FlashDecoding++: Faster Large Language Model Inference with Asynchronization, Flat GEMM Optimization, and Heuristics](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5321b1dabcd2be188d796c21b733e8c7-Abstract-Conference.html) | MLSys 2024 | 解码 Softmax 的异步化、Flat GEMM 专项优化与形状感知 Dataflow；跨 NVIDIA/AMD 的 Operator + Engine 评测。 |
| 2026 | [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ae8b0b5838ba510daff1198474e7b984-Abstract-Conference.html) | MLSys 2026 | 针对 Blackwell 的算力与非矩阵单元不对称扩展，重构异步 MMA、Softmax 流水及 CuTe-DSL 实现。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.
