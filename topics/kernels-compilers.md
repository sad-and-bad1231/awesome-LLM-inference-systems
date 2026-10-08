# Kernels & Compilers

Efficient execution of model operators: attention, GEMM, tiling, fusion, hardware-aware mapping and compilation.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Compute kernels; technical contribution changes the GPU/NPU execution path, not only the model architecture.

**Foundational context.** See also: [FlashAttention (2022), FlashAttention-2 (2024), FlashAttention-3 (2024), FlashInfer (2025)](../README.md#foundational-and-influential-papers).

## Papers (31)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2018 | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://www.usenix.org/conference/osdi18/presentation/chen) | OSDI 2018 | 端到端张量编译、算子调度与自动调优；作为现代 LLM Kernel Compiler 的体系结构前驱。 |
| 2020 | [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://www.usenix.org/conference/osdi20/presentation/zheng) | OSDI 2020 | 以搜索空间和 Cost Model 代替人工模板调参，实现跨硬件张量程序自动生成。 |
| 2023 | [TensorIR: An Abstraction for Automatic Tensorized Program Optimization](https://doi.org/10.1145/3575693.3576933) | ASPLOS 2023 | 张量化计算块和数据变换的结构化 IR，支撑 Tensor Core 自动映射。 |
| 2024 | [FlashDecoding++: Faster Large Language Model Inference with Asynchronization, Flat GEMM Optimization, and Heuristics](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5321b1dabcd2be188d796c21b733e8c7-Abstract-Conference.html) | MLSys 2024 | 解码 Softmax 的异步化、Flat GEMM 专项优化与形状感知 Dataflow；跨 NVIDIA/AMD 的 Operator + Engine 评测。 |
| 2024 | [Ladder: Enabling Efficient Low-Precision Deep Learning Computing through Hardware-aware Tensor Transformation](https://www.usenix.org/conference/osdi24/presentation/wang-lei) | OSDI 2024 | 数据布局变换与硬件原生低精度张量指令协同，避免低位宽执行的转换开销。 |
| 2025 | [FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/96894468eb44631a32d7ebd56f9892c7-Abstract-Conference.html) | MLSys 2025 | 联合设计 Radix Tree Prefix Share Attention Kernel 与树划分 Runtime。 |
| 2025 | [FlexAttention: A Programming Model for Generating Fused Attention Variants](https://proceedings.mlsys.org/paper_files/paper/2025/hash/61a9278dfef5f871b5e472389f8d6fa1-Abstract-Conference.html) | MLSys 2025 | 以 PyTorch 组合式表达实现并编译融合 Attention 变体。 |
| 2025 | [MAS-ATTENTION: MEMORY-AWARE STREAM PROCESSING FOR ATTENTION ACCELERATION ON RESOURCE-CONSTRAINED EDGE DEVICES](https://proceedings.mlsys.org/paper_files/paper/2025/hash/d3cf1559a8795eb1ed2b3ad52409ac7d-Abstract-Conference.html) | MLSys 2025 | 协调边缘加速器的向量与矩阵执行流水，以多级 Tiling 和缓存覆盖减少片上空间开销；含真实 NPU 验证。 |
| 2025 | [POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference](https://doi.org/10.1145/3676641.3715996) | ASPLOS 2025 | 在共享 SM 中重叠计算密集 Prefill 与访存密集 Decode Attention。 |
| 2025 | [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b286c344d38e10d2466c0514b78e2f36-Abstract-Conference.html) | ICLR 2025 | INT8 Attention Quantization 与 GPU Kernel 优化协同，保持高效推理所需数值精度。 |
| 2025 | [SageAttention2: Efficient Attention with Thorough Outlier Smoothing and Per-thread INT4 Quantization](https://proceedings.mlr.press/v267/zhang25ae.html) | ICML 2025 | 结合 Outlier Smoothing 与 per-thread INT4 算子，更深入地利用 GPU 低精度执行。 |
| 2025 | [SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs](https://doi.org/10.1145/3689031.3717481) | EuroSys 2025 | 以 SpMM 和新稀疏格式利用推理 GEMM 的低级稀疏性，减少存储和计算开销。 |
| 2025 | [ThunderKittens: Simple, Fast, and Adorable Kernels](https://proceedings.iclr.cc/paper_files/paper/2025/file/05dc08730e32441edff52b0fa6caab5f-Paper-Conference.pdf) | ICLR 2025 | 面向 GPU Tile/布局的数据抽象与原生执行流水，用于高性能 Attention Kernel。 |
| 2025 | [TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives](https://proceedings.mlsys.org/paper_files/paper/2025/hash/c6ee784cbe46d854843e4c883a3321ef-Abstract-Conference.html) | MLSys 2025 | 以 Tile 为接口生成重叠通信与计算的分布式 Kernel。 |
| 2026 | [AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0f8426558905746fc38da5e335700aec-Abstract-Conference.html) | MLSys 2026 | 通过实测反馈和优化记忆改善 Trainium NKI Kernel 搜索。 |
| 2026 | [BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c6ee784cbe46d854843e4c883a3321ef-Abstract-Conference.html) | MLSys 2026 | 利用 Online Softmax 统计直接跳过可忽略的 Attention Block。 |
| 2026 | [CoPilotIO: CPU as a Co-Pilot for GPU I/O to Free GPU Compute](https://www.usenix.org/conference/osdi26/presentation/chen-guanyi) | OSDI 2026 | GPU 发起异步 I/O，由 CPU 代理轮询并以设备硬件 Barrier 同步；包含 MoE 推理实测。 |
| 2026 | [DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bbd7d8bd780fcf7143add2317ba04638-Abstract-Conference.html) | MLSys 2026 | 分离计算定义与物理算子调度，并使用异步数据流优化 GPU 并发执行。 |
| 2026 | [Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel](https://openreview.net/forum?id=PJqFhAbUHa) | MLSys 2026 | Event Tensor 用统一事件张量抽象编译动态 megakernel，减少 LLM inference 中 kernel launch 和跨算子同步开销 |
| 2026 | [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ae8b0b5838ba510daff1198474e7b984-Abstract-Conference.html) | MLSys 2026 | 针对 Blackwell 的算力与非矩阵单元不对称扩展，重构异步 MMA、Softmax 流水及 CuTe-DSL 实现。 |
| 2026 | [Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bc52716d13d2d72ea0f335667d86c0f8-Abstract-Conference.html) | MLSys 2026 | PyTorch 原生编译器为多种数据相关 Attention 自动生成 Fusion/Tiling Kernel。 |
| 2026 | [HipKittens: Fast and Furious AMD Kernels](https://openreview.net/forum?id=xxSSrndQrI) | MLSys 2026 | HipKittens 面向 AMD GPU 提供高性能 kernel 编程与优化路径，补齐 AI 推理/训练算子在非 CUDA 平台上的性能生态 |
| 2026 | [IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ea5ffdf7da91256ecd2770f9fd2dade9-Abstract-Conference.html) | MLSys 2026 | 用 IndexSoftmax 和整数查表消除边缘 Attention 中反量化、Softmax、再量化的执行往返；Armv8 实测。 |
| 2026 | [LLMFolder: Revisiting Constant Folding in Large Language Models](https://doi.org/10.1145/3767295.3769339) | EuroSys 2026 | 从编译器 constant folding 视角重新审视 LLM 推理，将可预计算结构识别与模型推理执行结合，属于执行编译与模型服务交界的系统优化方向 |
| 2026 | [MoonBright: A GPU Memory Allocator with Device-Side Page Table Materialization and Deferred TLB Coherence](https://www.usenix.org/conference/osdi26/presentation/zhang-yangyu) | OSDI 2026 | MoonBright 在商品 GPU 上实现设备侧页表物化与延迟 TLB 一致性：元数据留主机、批量页表构建移到 GPU，并以新虚拟地址避免热路径上的 TLB shootdown，降低分配延迟、提升 LLM 推理性能并缓解分配器级外部碎片，纯软件改动即可跑在 NVIDIA/AMD GPU |
| 2026 | [MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs](https://www.usenix.org/conference/osdi26/presentation/cheng) | OSDI 2026 | MPK 用 SM 级图表示把多 GPU 推理编译为单一 mega-kernel，实现跨算子软件流水与计算-通信重叠，并以持久内核内运行时执行，端到端 latency 降低至多 1.7× |
| 2026 | [Optimal Software Pipelining and Warp Specialization for Tensor Core GPUs](https://www.usenix.org/conference/osdi26/presentation/soi) | OSDI 2026 | Twill 把软件流水（SWP）与 warp 特化（WS）建模为可由约束求解器整体优化的联合问题，为迭代程序自动推导最优且无启发式的调度，并证明 Hopper/Blackwell 上 Flash Attention 调度的最优性 |
| 2026 | [Optimizing PyTorch Inference with LLM-Based Multi-Agent Systems](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bd49b53516ce9ea248fb73522d71a508-Abstract-Conference.html) | MLSys 2026 | 通过多智能体调优并真实运行 H100 上的推理算子。 |
| 2026 | [PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion](https://2026.hpca-conf.org/details/hpca-2026-main-conference/3/PADE-A-Predictor-Free-Sparse-Attention-Accelerator-via-Unified-Execution-and-Stage-F) | HPCA 2026 | 将稀疏选择与 Attention 执行融合，消除专用预测关键路径。 |
| 2026 | [ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ff997469ac66cf893c4183efeb22212a-Abstract-Conference.html) | MLSys 2026 | 用可重用通信与同步原语编写 TP/SP/EP 跨卡重叠 Kernel。 |
| 2026 | [Wave: A Symbolic Python DSL And Compiler for High-Performance Machine Learning](https://proceedings.mlsys.org/paper_files/paper/2026/hash/48c34730ff9a8574481a00ce8cb5e2cb-Abstract-Conference.html) | MLSys 2026 | Python DSL 自动优化 GPU Kernel 的矩阵核心地址映射与张量布局。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
