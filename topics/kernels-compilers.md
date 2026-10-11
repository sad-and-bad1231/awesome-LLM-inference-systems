# Kernels & Compilers

Efficient execution of model operators: attention, GEMM, tiling, fusion, hardware-aware mapping and compilation.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Compute kernels; technical contribution changes the GPU/NPU execution path, not only the model architecture.

**Foundational context.** See also: [FlashAttention (2022), FlashAttention-2 (2024), FlashAttention-3 (2024), FlashInfer (2025)](../README.md#foundational-and-influential-papers).

## Papers (49)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2018 | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://www.usenix.org/conference/osdi18/presentation/chen) | OSDI 2018 | 端到端张量编译、算子调度与自动调优；作为现代 LLM Kernel Compiler 的体系结构前驱。 |
| 2020 | [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://www.usenix.org/conference/osdi20/presentation/zheng) | OSDI 2020 | 以搜索空间和 Cost Model 代替人工模板调参，实现跨硬件张量程序自动生成。 |
| 2023 | [TensorIR: An Abstraction for Automatic Tensorized Program Optimization](https://doi.org/10.1145/3575693.3576933) | ASPLOS 2023 | 张量化计算块和数据变换的结构化 IR，支撑 Tensor Core 自动映射。 |
| 2024 | [FlashDecoding++: Faster Large Language Model Inference with Asynchronization, Flat GEMM Optimization, and Heuristics](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5321b1dabcd2be188d796c21b733e8c7-Abstract-Conference.html) | MLSys 2024 | 解码 Softmax 的异步化、Flat GEMM 专项优化与形状感知 Dataflow；跨 NVIDIA/AMD 的 Operator + Engine 评测。 |
| 2024 | [Hydragen: High-Throughput LLM Inference with Shared Prefixes](https://arxiv.org/abs/2402.05099) | arXiv 2024 (preprint) | 将共享 Prefix 与独有 Suffix 的 Exact Attention 分解执行，把重复 Query 合并为高效矩阵计算并支持 Tree Prefix。 |
| 2024 | [Ladder: Enabling Efficient Low-Precision Deep Learning Computing through Hardware-aware Tensor Transformation](https://www.usenix.org/conference/osdi24/presentation/wang-lei) | OSDI 2024 | 数据布局变换与硬件原生低精度张量指令协同，避免低位宽执行的转换开销。 |
| 2025 | [FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference](https://doi.org/10.1109/HPCA61900.2025.00127) | HPCA 2025 | 对 SoC GEMM 与 PIM GEMV 提供不同虚实地址映射，在 Prefill/Decode 切换时避免权重 Memory Relayout。 |
| 2025 | [Fast On-device LLM Inference with NPUs](https://doi.org/10.1145/3669940.3707239) | ASPLOS 2025 | llm.npu 将模型子图映射到手机 NPU/CPU/GPU 并流水化执行，处理 NPU 不支持算子及动态 LLM Decode。 |
| 2025 | [FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/96894468eb44631a32d7ebd56f9892c7-Abstract-Conference.html) | MLSys 2025 | 联合设计 Radix Tree Prefix Share Attention Kernel 与树划分 Runtime。 |
| 2025 | [FlexAttention: A Programming Model for Generating Fused Attention Variants](https://proceedings.mlsys.org/paper_files/paper/2025/hash/61a9278dfef5f871b5e472389f8d6fa1-Abstract-Conference.html) | MLSys 2025 | 以 PyTorch 组合式表达实现并编译融合 Attention 变体。 |
| 2025 | [GeneralSparse: Bridging the Gap in SpMM for Pruned Large Language Model Inference on GPUs](https://www.usenix.org/conference/atc25/presentation/wang-yaoyu) | USENIX ATC 2025 | 在 Memory-access Space 与 Reduction Space 上抽象可变稀疏模式，生成适应 GPU 层级的通用 SpMM Kernel。 |
| 2025 | [LeanAttention: Hardware-Aware Scalable Attention Mechanism for the Decode-Phase of Transformers](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html) | MLSys 2025 | 为 Long-context Decode 重排 Exact Attention 的 Split-K 和跨 CTA Reduction，提升长序列并行度及 GPU 利用率。 |
| 2025 | [LUT Tensor Core: A Software-Hardware Co-Design for LUT-Based Low-Bit LLM Inference](https://doi.org/10.1145/3695053.3731057) | ISCA 2025 | LUT-based Mixed-precision GEMM 的融合、表项对称化与低比特 Tile 专用硬件共同设计。 |
| 2025 | [MAS-ATTENTION: MEMORY-AWARE STREAM PROCESSING FOR ATTENTION ACCELERATION ON RESOURCE-CONSTRAINED EDGE DEVICES](https://proceedings.mlsys.org/paper_files/paper/2025/hash/d3cf1559a8795eb1ed2b3ad52409ac7d-Abstract-Conference.html) | MLSys 2025 | 协调边缘加速器的向量与矩阵执行流水，以多级 Tiling 和缓存覆盖减少片上空间开销；含真实 NPU 验证。 |
| 2025 | [MEADOW: Memory-efficient Dataflow and Data Packing for Low Power Edge LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/259a5df46308d60f8454bd4adcc3b462-Abstract-Conference.html) | MLSys 2025 | 在低功耗 FPGA 上采用 Token-parallel/Head-sequential Dataflow 与无损 Weight Packing，减少 Prefill/Decode 外存访问。 |
| 2025 | [Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking](https://doi.org/10.1145/3676642.3736114) | ASPLOS 2025 | 基于 Neuron Co-Activation 重排手机 Flash 上的稀疏权重，联合预取和访问模式优化减少 IOPS。 |
| 2025 | [POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference](https://doi.org/10.1145/3676641.3715996) | ASPLOS 2025 | 在共享 SM 中重叠计算密集 Prefill 与访存密集 Decode Attention。 |
| 2025 | [QFactory: Accelerating Quantized Large Language Model Serving with Qtile Graphs](https://www.usenix.org/conference/atc25/presentation/zhang-qihao) | USENIX ATC 2025 | 以 Qtile Graph 描述量化张量变换与 Dequantize/Fused GEMM，联合图变换和 Tile Scheduling 生成 Kernel。 |
| 2025 | [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b286c344d38e10d2466c0514b78e2f36-Abstract-Conference.html) | ICLR 2025 | INT8 Attention Quantization 与 GPU Kernel 优化协同，保持高效推理所需数值精度。 |
| 2025 | [SageAttention2: Efficient Attention with Thorough Outlier Smoothing and Per-thread INT4 Quantization](https://proceedings.mlr.press/v267/zhang25ae.html) | ICML 2025 | 结合 Outlier Smoothing 与 per-thread INT4 算子，更深入地利用 GPU 低精度执行。 |
| 2025 | [SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs](https://doi.org/10.1145/3689031.3717481) | EuroSys 2025 | 以 SpMM 和新稀疏格式利用推理 GEMM 的低级稀疏性，减少存储和计算开销。 |
| 2025 | [T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge](https://doi.org/10.1145/3689031.3696099) | EuroSys 2025 | 以 Group-wise Lookup Table 替换低比特 CPU Decode 的反量化乘加，利用 SIMD 改善边缘 LLM 推理。 |
| 2025 | [ThunderKittens: Simple, Fast, and Adorable Kernels](https://proceedings.iclr.cc/paper_files/paper/2025/file/05dc08730e32441edff52b0fa6caab5f-Paper-Conference.pdf) | ICLR 2025 | 面向 GPU Tile/布局的数据抽象与原生执行流水，用于高性能 Attention Kernel。 |
| 2025 | [TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives](https://proceedings.mlsys.org/paper_files/paper/2025/hash/c6ee784cbe46d854843e4c883a3321ef-Abstract-Conference.html) | MLSys 2025 | 以 Tile 为接口生成重叠通信与计算的分布式 Kernel。 |
| 2025 | [TurboAttention: Efficient Attention Approximation for High-Throughput LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/f4f55846501f3336f293fd8b6de10770-Abstract-Conference.html) | MLSys 2025 | FlashQ 与整数 Softmax 近似融合量化 Attention 算子，避免 KV 解量化并评估端到端吞吐。 |
| 2025 | [VQ-LLM: High-performance Code Generation for Vector Quantization Augmented LLM Inference](https://arxiv.org/abs/2503.02236) | HPCA 2025 | 以 Codebook Cache、融合数据流和自适应 Tile 生成向量量化 LLM Kernel，减少码本与权重访存。 |
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
| 2026 | [PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel](https://doi.org/10.1145/3779212.3790200) | ASPLOS 2026 | 按共享 Prefix 组织 Decode Query 和 CTA，执行 Pack-Forward-Merge 以减少重复 KV 读取并消除 Tile 资源空洞。 |
| 2026 | [Purlin: Separating Orchestration from the Datapath of Collectives](https://arxiv.org/abs/2609.36954) | arXiv 2026 (preprint) | 以 SNAC 编排层和硬件特定 Copy/Reduce Atom 解耦 Collective 语义、同步与数据通路，并集成 SGLang 评估。 |
| 2026 | [SAS: Sparse Attention Synthesizer for Efficient Language Model Inference](https://doi.org/10.1145/3767295.3769364) | EuroSys 2026 | 可组合静态/动态 Sparse Attention 原语，自动推导最小 KV 状态并生成面向 GPU 的稀疏 Kernel。 |
| 2026 | [Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation](https://doi.org/10.1145/3760250.3762219) | ASPLOS 2026 | 通过 Tile-level DSL、层次寄存器/共享内存及 Layout Algebra 生成 1–8 bit GEMM，含 LLM 低精度内核实测。 |
| 2026 | [Vec-LUT: Vector Table Lookup for Parallel Ultra-Low-Bit LLM Inference on Edge Devices](https://doi.org/10.1145/3745756.3809200) | MobiSys 2026 | 将单 Token 标量 LUT 升级为跨 Token 向量查表，改善边缘设备 Ultra-low-bit Batch Decode 的访存合并。 |
| 2026 | [Wave: A Symbolic Python DSL And Compiler for High-Performance Machine Learning](https://proceedings.mlsys.org/paper_files/paper/2026/hash/48c34730ff9a8574481a00ce8cb5e2cb-Abstract-Conference.html) | MLSys 2026 | Python DSL 自动优化 GPU Kernel 的矩阵核心地址映射与张量布局。 |
| 2026 | [XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads](https://doi.org/10.1145/3760250.3762228) | ASPLOS 2026 | 在 Ascend NPU 上把动态 Prefill/Decode 分解为可复用 Meta-kernels 和虚拟 Padding，减少 Dynamic Shape 执行开销。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
