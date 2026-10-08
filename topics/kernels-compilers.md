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

## Legacy Serving cohort — re-admitted (1)

Reclassified by **primary systems mechanism**, not legacy “Serving” keywords. Bibliographic links have been updated where a stronger individual source was found; other links preserve the original proceedings record.

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2025 | [POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference](https://doi.org/10.1145/3676641.3715996) | ASPLOS 2025 | 在共享 SM 中重叠计算密集 Prefill 与访存密集 Decode Attention。 |

## Newly admitted · Wave 2 (8)

Publisher/conference identity and the distinct inference mechanism were reviewed. Very early compiler papers are included as *foundational execution primitives*; work with cross-model training applicability is explicitly described.

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2018 | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://www.usenix.org/conference/osdi18/presentation/chen) | OSDI 2018 | 端到端张量编译、算子调度与自动调优；作为现代 LLM Kernel Compiler 的体系结构前驱。 |
| 2020 | [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://www.usenix.org/conference/osdi20/presentation/zheng) | OSDI 2020 | 以搜索空间和 Cost Model 代替人工模板调参，实现跨硬件张量程序自动生成。 |
| 2023 | [TensorIR: An Abstraction for Automatic Tensorized Program Optimization](https://doi.org/10.1145/3575693.3576933) | ASPLOS 2023 | 张量化计算块和数据变换的结构化 IR，支撑 Tensor Core 自动映射。 |
| 2024 | [Ladder: Enabling Efficient Low-Precision Deep Learning Computing through Hardware-aware Tensor Transformation](https://www.usenix.org/conference/osdi24/presentation/wang-lei) | OSDI 2024 | 数据布局变换与硬件原生低精度张量指令协同，避免低位宽执行的转换开销。 |
| 2025 | [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b286c344d38e10d2466c0514b78e2f36-Abstract-Conference.html) | ICLR 2025 | INT8 Attention Quantization 与 GPU Kernel 优化协同，保持高效推理所需数值精度。 |
| 2025 | [SageAttention2: Efficient Attention with Thorough Outlier Smoothing and Per-thread INT4 Quantization](https://proceedings.mlr.press/v267/zhang25ae.html) | ICML 2025 | 结合 Outlier Smoothing 与 per-thread INT4 算子，更深入地利用 GPU 低精度执行。 |
| 2025 | [SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs](https://doi.org/10.1145/3689031.3717481) | EuroSys 2025 | 以 SpMM 和新稀疏格式利用推理 GEMM 的低级稀疏性，减少存储和计算开销。 |
| 2025 | [ThunderKittens: Simple, Fast, and Adorable Kernels](https://proceedings.iclr.cc/paper_files/paper/2025/file/05dc08730e32441edff52b0fa6caab5f-Paper-Conference.pdf) | ICLR 2025 | 面向 GPU Tile/布局的数据抽象与原生执行流水，用于高性能 Attention Kernel。 |

