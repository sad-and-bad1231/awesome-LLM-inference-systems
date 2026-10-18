# Kernels & Compilers

Efficient LLM inference execution from hardware-conscious operators to compiler scheduling. **The decisive reusable mechanism determines the subsection**, not GPU vendor, academic venue, workload modality, or claimed speedup.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Papers in this page materially change the low-level inference execution path (operator implementation, data layout, compilation, fusion, communication or execution instrumentation), or are rare, explicitly labeled foundational compiler/tooling exceptions. Model-only, training-only and general-purpose KernelBench improvements do not automatically pass the strict [G0–G5 review](../STRICT_REVIEW.md).

**Foundational context.** [FlashAttention (2022), FlashAttention-2/3, and FlashInfer](../README.md#foundational-and-influential-papers) are historical/reference anchors on the homepage, **not duplicate canonical rows** here.

## Mechanism map

Nine internal groups, **71 canonical entries in total**. Subsections are a reading/navigation structure, **not nine new public categories** and not G0–G5 admission verdicts.

| Research mechanism | Papers |
|---|---:|
| [Attention & KV-aware Kernels](#attention--kv-aware-kernels-13) | 13 |
| [Sparse & Irregular Execution](#sparse--irregular-execution-5) | 5 |
| [GEMM & Low-Precision Kernels](#gemm--low-precision-kernels-10) | 10 |
| [Kernel DSL, Compiler IR & Layout](#kernel-dsl-compiler-ir--layout-13) | 13 |
| [Fusion, Pipelining & Megakernels](#fusion-pipelining--megakernels-12) | 12 |
| [Communication-Aware Kernels](#communication-aware-kernels-3) | 3 |
| [Memory, I/O & Hardware Co-design](#memory-io--hardware-co-design-10) | 10 |
| [Agentic Kernel Optimization](#agentic-kernel-optimization-3) | 3 |
| [Kernel Profiling & Correctness](#kernel-profiling--correctness-2) | 2 |
| **Total** | **71** |

### Where this taxonomy came from

The structure is cross-checked against actual operator/backend boundaries, not derived from conference session labels:

- **Serving backend contracts:** [vLLM Attention Backend support](https://docs.vllm.ai/en/latest/design/attention_backends/) distinguishes hardware/capability-specific Dense, MLA, Sparse and composite backends; [SGLang kernel namespace](https://github.com/sgl-project/sglang/blob/main/python/sglang/kernels/README.md) separates registry/dispatch from operator groups including GEMM, MoE, Sampling, Communication and KV Cache.
- **Operator implementations:** [FlashInfer](https://github.com/flashinfer-ai/flashinfer), [FlashAttention](https://github.com/Dao-AILab/flash-attention), [DeepSeek FlashMLA/DeepGEMM/DeepEP/DeepSelect](../organizations/DeepSeek.md), [ROCm AITER / Composable Kernel](../organizations/AMD.md), and [NVIDIA CUTLASS / CuTe / NCCL](../organizations/NVIDIA.md) expose distinct computation, communication and programming-model concerns.
- **Portability and hardware evidence:** [Ascend C / CANN and vLLM Ascend](../organizations/Huawei.md), [AWS Neuron/Trainium](../organizations/AWS.md), plus the [research lab map](../communities/README.md) motivate cross-backend compiler, architecture-specific kernels and rigorous real-device-vs-simulator labeling.

**Coverage gaps for later discovery — not new admissions:** broader Fused MoE/Grouped GEMM and Expert Dispatch beyond the admitted MonoMoE preprint, Token-level Sampling/TopK/TopP, RoPE/RMSNorm/Activation Fusion, KV Layout/Copy/Quantize kernels, and JIT/Graph Capture/Backend Dispatch integration. These matter in real serving runtimes even if this curated paper list has few dedicated landmark papers. A missing mechanism does **not** justify importing implementation-only material as a peer-reviewed paper. Papers whose main contribution is policy/scheduling/KV management still belong in their other existing canonical topic.

## Papers (71)

### Attention & KV-aware Kernels (13)

**Attention 的执行与 KV 布局相互作用**：Dense/MLA、Prefill/Decode、共享 Prefix、低比特 Attention；对照 FA/FlashInfer 与 Serving Batch/KV 格式。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [FlashDecoding++: Faster Large Language Model Inference with Asynchronization, Flat GEMM Optimization, and Heuristics](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5321b1dabcd2be188d796c21b733e8c7-Abstract-Conference.html) | MLSys 2024 | 解码 Softmax 的异步化、Flat GEMM 专项优化与形状感知 Dataflow；跨 NVIDIA/AMD 的 Operator + Engine 评测。 |
| 2024 | [Hydragen: High-Throughput LLM Inference with Shared Prefixes](https://arxiv.org/abs/2402.05099) | arXiv 2024 (preprint) | 将共享 Prefix 与独有 Suffix 的 Exact Attention 分解执行，把重复 Query 合并为高效矩阵计算并支持 Tree Prefix。 |
| 2025 | [FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/96894468eb44631a32d7ebd56f9892c7-Abstract-Conference.html) | MLSys 2025 | 联合设计 Radix Tree Prefix Share Attention Kernel 与树划分 Runtime。 |
| 2025 | [FlexAttention: A Programming Model for Generating Fused Attention Variants](https://proceedings.mlsys.org/paper_files/paper/2025/hash/61a9278dfef5f871b5e472389f8d6fa1-Abstract-Conference.html) | MLSys 2025 | 以 PyTorch 组合式表达实现并编译融合 Attention 变体。 |
| 2025 | [LeanAttention: Hardware-Aware Scalable Attention Mechanism for the Decode-Phase of Transformers](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html) | MLSys 2025 | 为 Long-context Decode 重排 Exact Attention 的 Split-K 和跨 CTA Reduction，提升长序列并行度及 GPU 利用率。 |
| 2025 | [POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference](https://doi.org/10.1145/3676641.3715996) | ASPLOS 2025 | 在共享 SM 中重叠计算密集 Prefill 与访存密集 Decode Attention。 |
| 2025 | [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b286c344d38e10d2466c0514b78e2f36-Abstract-Conference.html) | ICLR 2025 | INT8 Attention Quantization 与 GPU Kernel 优化协同，保持高效推理所需数值精度。 |
| 2025 | [SageAttention2: Efficient Attention with Thorough Outlier Smoothing and Per-thread INT4 Quantization](https://proceedings.mlr.press/v267/zhang25ae.html) | ICML 2025 | 结合 Outlier Smoothing 与 per-thread INT4 算子，更深入地利用 GPU 低精度执行。 |
| 2025 | [TurboAttention: Efficient Attention Approximation for High-Throughput LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/f4f55846501f3336f293fd8b6de10770-Abstract-Conference.html) | MLSys 2025 | FlashQ 与整数 Softmax 近似融合量化 Attention 算子，避免 KV 解量化并评估端到端吞吐。 |
| 2026 | [BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache](https://doi.org/10.1109/HPCA68181.2026.11408481) | HPCA 2026 | 长上下文低比特 KV Decode 中协同 CUDA Core/Tensor Core：自动 Layout 生成、Warp-level Dequantization 与混合精度流水；作者在 A100/H100/RTX 4090 实机比较 FlashDecoding-v2、QServe，并公开 [BitDecoding](https://github.com/OpenBitSys/BitDecoding)。报告的模型 Decode Latency 不代表多并发 SLO Goodput，量化质量另需核对。 |
| 2026 | [FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ae8b0b5838ba510daff1198474e7b984-Abstract-Conference.html) | MLSys 2026 | 针对 Blackwell 的算力与非矩阵单元不对称扩展，重构异步 MMA、Softmax 流水及 CuTe-DSL 实现。 |
| 2026 | [Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bc52716d13d2d72ea0f335667d86c0f8-Abstract-Conference.html) | MLSys 2026 | PyTorch 原生编译器为多种数据相关 Attention 自动生成 Fusion/Tiling Kernel。 |
| 2026 | [PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel](https://doi.org/10.1145/3779212.3790200) | ASPLOS 2026 | 按共享 Prefix 组织 Decode Query 和 CTA，执行 Pack-Forward-Merge 以减少重复 KV 读取并消除 Tile 资源空洞。 |

### Sparse & Irregular Execution (5)

**不规则形状、稀疏选择与动态执行**：Sparse Attention、SpMM、跳块调度和稀疏数据结构。单独比较有效稀疏率、Index/Pack 开销与精度。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [GeneralSparse: Bridging the Gap in SpMM for Pruned Large Language Model Inference on GPUs](https://www.usenix.org/conference/atc25/presentation/wang-yaoyu) | USENIX ATC 2025 | 在 Memory-access Space 与 Reduction Space 上抽象可变稀疏模式，生成适应 GPU 层级的通用 SpMM Kernel。 |
| 2025 | [SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs](https://doi.org/10.1145/3689031.3717481) | EuroSys 2025 | 以 SpMM 和新稀疏格式利用推理 GEMM 的低级稀疏性，减少存储和计算开销。 |
| 2026 | [Accelerating Sparse Transformer Inference on GPU](https://doi.org/10.1145/3774934.3786434) | PPoPP 2026 | STOF 根据稀疏 Mask、MHA 结构选择 Row/Block Kernel，融合下游算子并做两阶段 Autotuning；有 GPU 实测和 Transformer 推理对照。 |
| 2026 | [BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding](https://proceedings.mlsys.org/paper_files/paper/2026/hash/c6ee784cbe46d854843e4c883a3321ef-Abstract-Conference.html) | MLSys 2026 | 利用 Online Softmax 统计直接跳过可忽略的 Attention Block。 |
| 2026 | [SAS: Sparse Attention Synthesizer for Efficient Language Model Inference](https://doi.org/10.1145/3767295.3769364) | EuroSys 2026 | 可组合静态/动态 Sparse Attention 原语，自动推导最小 KV 状态并生成面向 GPU 的稀疏 Kernel。 |

### GEMM & Low-Precision Kernels (10)

**实际低比特算术路径**：GEMM/GEMV、量化/反量化融合、LUT、Codebook 与按 Batch/Shape 切换的 Kernel；区分 Kernel Speedup 和 Serving Goodput。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving](https://doi.org/10.1145/3712285.3759852) | SC 2025 | LiquidQuant 的低开销 W4A8 解量化配合跨 Warp-group 的加载/解量化/MMA 隐式流水；报告 GPU Kernel 与端到端 Serving 实测，官方代码发布状态未确认。 |
| 2025 | [MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models](https://doi.org/10.1145/3710848.3710871) | PPoPP 2025 | 面向 **batched** INT4×FP16 LLM Decode，以异步访存、权重布局和流水保持量化 GEMM 接近带宽上限；作者报告 vLLM 端到端加速（最高 2.8×），提供 [可执行 Artifact](https://github.com/IST-DASLab/marlin_artifact)。收益取决于 Batch/形状，不能把单层理论加速视作所有 Serving 场景通用结论。 |
| 2025 | [NeuronMM: High-Performance Matrix Multiplication for LLM Inference on AWS Trainium](https://arxiv.org/abs/2510.25977) | arXiv 2025 (preprint) | 利用 Trainium Systolic Array 与 Software-managed SRAM 的缓存、数据排布、融合规避转置；公开 Kernel 实现并测量 LLM End-to-end 延迟。 |
| 2025 | [QFactory: Accelerating Quantized Large Language Model Serving with Qtile Graphs](https://www.usenix.org/conference/atc25/presentation/zhang-qihao) | USENIX ATC 2025 | 以 Qtile Graph 描述量化张量变换与 Dequantize/Fused GEMM，联合图变换和 Tile Scheduling 生成 Kernel。 |
| 2025 | [T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge](https://doi.org/10.1145/3689031.3696099) | EuroSys 2025 | 以 Group-wise Lookup Table 替换低比特 CPU Decode 的反量化乘加，利用 SIMD 改善边缘 LLM 推理。 |
| 2025 | [VQ-LLM: High-performance Code Generation for Vector Quantization Augmented LLM Inference](https://doi.org/10.1109/HPCA61900.2025.00112) | HPCA 2025 | 针对 Vector-Quantized LLM 的 Codebook-cache 跨寄存器/Shared Memory/Global Memory 分层布局，结合 Codebook-centric Dataflow 和融合 Kernel 生成降低查表/量化计算开销；作者报告低比特 LLM 推理算子性能，非无条件的端到端 Serving Goodput 改进。 |
| 2026 | [FlashServe: Adaptive Kernel Provision for Quantized LLM Serving](https://doi.org/10.1109/2575-8411.2026.00078) | ICDCS 2026 | 面向动态 Batch Size，为不同量化 GEMM Kernel 建模选择成本与切换开销，使用异步预备/切换避免静态 Kernel 固化；原始来源 Dynamic GEMM 标题不等于正式出版 Adaptive Kernel Provision。 |
| 2026 | [IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ea5ffdf7da91256ecd2770f9fd2dade9-Abstract-Conference.html) | MLSys 2026 | 用 IndexSoftmax 和整数查表消除边缘 Attention 中反量化、Softmax、再量化的执行往返；Armv8 实测。 |
| 2026 | [QIGen: A Kernel Generator for Inference on Nonuniformly Quantized Large Language Models](https://2026.cgo.org/details/cgo-2026-papers/7/QIGen-A-Kernel-Generator-for-Inference-on-Nonuniformly-Quantized-Large-Language-Mode) | CGO 2026 | 针对 CPU 非均匀量化权重自动生成匹配其压缩布局和硬件特征的 GEMV/GEMM Kernel，提供实际 CPU 性能–准确率对照，非 GPU Serving。 |
| 2026 | [Vec-LUT: Vector Table Lookup for Parallel Ultra-Low-Bit LLM Inference on Edge Devices](https://doi.org/10.1145/3745756.3809200) | MobiSys 2026 | 将单 Token 标量 LUT 升级为跨 Token 向量查表，改善边缘设备 Ultra-low-bit Batch Decode 的访存合并。 |

### Kernel DSL, Compiler IR & Layout (13)

**如何表达、降级、验证 Kernel**：Tile/Dataflow、IR、Linear Layout、Tensorization、代码生成和跨 ISA 翻译；以可生成的真实算子及代码作为核心证据。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2018 | [TVM: An Automated End-to-End Optimizing Compiler for Deep Learning](https://www.usenix.org/conference/osdi18/presentation/chen) | OSDI 2018 | 端到端张量编译、算子调度与自动调优；作为现代 LLM Kernel Compiler 的体系结构前驱。 |
| 2020 | [Ansor: Generating High-Performance Tensor Programs for Deep Learning](https://www.usenix.org/conference/osdi20/presentation/zheng) | OSDI 2020 | 以搜索空间和 Cost Model 代替人工模板调参，实现跨硬件张量程序自动生成。 |
| 2023 | [Hidet: Task-Mapping Programming Paradigm for Deep Learning Tensor Programs](https://doi.org/10.1145/3575693.3575702) | ASPLOS 2023 | 以 Task Mapping 显式表达细粒度线程/计算分配与顺序，配合 Post-scheduling Fusion、低搜索成本调优；在真实 GPU 上与 TVM/Ansor/ONNX Runtime 比较，并公开 [ASPLOS Artifact](https://github.com/yaoyaoding/hidet-artifacts)。**KEEP_FOUNDATIONAL**：通用 Transformer/DNN Compiler 前驱，不冒充现代 LLM Serving 系统。 |
| 2023 | [TensorIR: An Abstraction for Automatic Tensorized Program Optimization](https://doi.org/10.1145/3575693.3576933) | ASPLOS 2023 | 张量化计算块和数据变换的结构化 IR，支撑 Tensor Core 自动映射。 |
| 2024 | [Ladder: Enabling Efficient Low-Precision Deep Learning Computing through Hardware-aware Tensor Transformation](https://www.usenix.org/conference/osdi24/presentation/wang-lei) | OSDI 2024 | 数据布局变换与硬件原生低精度张量指令协同，避免低位宽执行的转换开销。 |
| 2025 | [Mirage: A Multi-Level Superoptimizer for Tensor Programs](https://www.usenix.org/conference/osdi25/presentation/wu-mengdi) | OSDI 2025 | 以 Kernel/Thread-block/Thread 三层 µGraph 搜索代数变换与 GPU Kernel Schedule，辅以等价性验证；公开编译器并实测 Transformer Tensor Programs。 |
| 2025 | [QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach](https://www.usenix.org/conference/osdi25/presentation/dong) | OSDI 2025 | LLM Translation + Symbolic Repair + Hierarchical Autotuning，在 Intel VNNI/NVIDIA CUDA/AMD HIP/Cambricon BANG 实机验证跨 ISA 程序翻译；包含 LLM Kernel，但混合 DNN Workloads 的程序翻译成功率 **不是** LLM Serving 吞吐。作为跨设备编译前提保留（KEEP_ADJACENT）。 |
| 2025 | [ThunderKittens: Simple, Fast, and Adorable Kernels](https://proceedings.iclr.cc/paper_files/paper/2025/file/05dc08730e32441edff52b0fa6caab5f-Paper-Conference.pdf) | ICLR 2025 | 面向 GPU Tile/布局的数据抽象与原生执行流水，用于高性能 Attention Kernel。 |
| 2025 | [TileLang: A Composable Tiled Programming Model for AI Systems](https://arxiv.org/abs/2504.17577) | arXiv 2025 (preprint) | 将 Tile Dataflow 与线程映射、Tensorization、Layout 及 Pipeline Scheduling 解耦，在 GEMM/FlashAttention/MLA 等 GPU 推理 Kernel 上提供可执行编译器及实测。 |
| 2026 | [HipKittens: Fast and Furious AMD Kernels](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bc75fa9843a7905bbed9d83895a88f7f-Abstract-Conference.html) | MLSys 2026 | 把 Tile/Async Execution 编程抽象迁至 CDNA3/CDNA4 AMD GPU，针对 AMD 布局和指令约束重设算法；作者公开 [HipKittens](https://github.com/HazyResearch/HipKittens) 并报告真实 AMD GEMM/Attention Kernel 性能，部分集成到 AITER。不是泛化的 LLM Serving Goodput 证明。 |
| 2026 | [Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F₂](https://doi.org/10.1145/3760250.3762221) | ASPLOS 2026 | 以 F₂ 线性映射统一 Triton Tensor Layout 与 Layout Conversion，减少编译器特殊分支并修正布局缺陷；实现已进入 Triton，含真实 GPU Kernel 评测。 |
| 2026 | [Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation](https://doi.org/10.1145/3760250.3762219) | ASPLOS 2026 | 通过 Tile-level DSL、层次寄存器/共享内存及 Layout Algebra 生成 1–8 bit GEMM，含 LLM 低精度内核实测。 |
| 2026 | [Wave: A Symbolic Python DSL And Compiler for High-Performance Machine Learning](https://proceedings.mlsys.org/paper_files/paper/2026/hash/48c34730ff9a8574481a00ce8cb5e2cb-Abstract-Conference.html) | MLSys 2026 | Python DSL 自动优化 GPU Kernel 的矩阵核心地址映射与张量布局。 |

### Fusion, Pipelining & Megakernels (12)

**跨算子执行路径**：Persistent/Mega Kernel、Warp Specialization、软件流水、算子融合、动态 Shape/Graph 和启动开销；重点对照真实请求路径与执行图。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2021 | [LightSeq: A High Performance Inference Library for Transformers](https://aclanthology.org/2021.naacl-industry.15/) | NAACL 2021 Industry Track | 早期工业级 Transformer GPU 推理库，通过算子融合、Kernel 与内存优化实现跨模型框架高效推理；有公开 CUDA 实现，实验以 Transformer/机器翻译为主，不宣称现代自回归 LLM Serving。 |
| 2025 | [PipeThreader: Software-Defined Pipelining for Efficient DNN Execution](https://www.usenix.org/conference/osdi25/presentation/cheng) | OSDI 2025 | 通过 sTask Graph 对 GPU TensorCore/TMA 依赖建模，将 Kernel Pipelining 转为软件定义的编译期流水调度；以 FlashAttention/Mamba2 的真实 GPU Kernel 和 TileLang Artifact 验证。 |
| 2026 | [BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal](https://arxiv.org/abs/2607.00501) | arXiv 2026 (preprint) | Metal-native Runtime 采用零分配 Decode Loop、Chip-specialized Fusion 与 Unified-memory-aware Scheduling；公开实现并在 M3/M4 Pro 对照 llama.cpp/MLX。 |
| 2026 | [DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling](https://proceedings.mlsys.org/paper_files/paper/2026/hash/bbd7d8bd780fcf7143add2317ba04638-Abstract-Conference.html) | MLSys 2026 | 分离计算定义与物理算子调度，并使用异步数据流优化 GPU 并发执行。 |
| 2026 | [Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel](https://proceedings.mlsys.org/paper_files/paper/2026/hash/53d3f45797970d323bd8a0d379c525aa-Abstract-Conference.html) | MLSys 2026 | 将动态 Shape/数据依赖的细粒度 Task Dependency 表示为 Event Tensor，并静/动态调度生成 Persistent Megakernel，解决动态 LLM Serving 的 Launch/同步及 Warmup 开销；作者报告 Serving Latency 对照，尚未独立复现。 |
| 2026 | [GraCE: Unlocking CUDA Graphs with Compiler Support for ML Workloads](https://www.usenix.org/conference/osdi26/presentation/ghosh) | OSDI 2026 | 通过 PyTorch2 编译期代码变换扩大 CUDA Graph Capture 可用性，消除 Graph Kernel Parameter Copy 并依成本模型选择 Replay；有公开 [OSDI Artifact](https://github.com/csl-iisc/GraCE-OSDI26-Artifact)。**KEEP_ADJACENT**：通用 ML Graph Compiler，论文 TorchBench/HuggingFace/TIMM 收益不等于已验证 vLLM 在线服务收益。 |
| 2026 | [LLMFolder: Revisiting Constant Folding in Large Language Models](https://doi.org/10.1145/3767295.3769339) | EuroSys 2026 | 从编译器 constant folding 视角重新审视 LLM 推理，将可预计算结构识别与模型推理执行结合，属于执行编译与模型服务交界的系统优化方向 |
| 2026 | [MonoMoE: An Efficient Fused Mega-kernel for Quantized MoE Decoding](https://arxiv.org/abs/2609.04244) | arXiv 2026 (preprint) | 把小 Batch MoE Decode 改为 Weight-major Persistent Megakernel，在一次 Launch 中融合 Routing/TopK、Quantization、两个 Expert GEMM、Activation 与 Combine，减少 Expert-local Tile Padding；作者在 H200、vLLM 路径报告 Operator 和 TPOT 收益，[FlashInfer Kernel 代码](https://github.com/flashinfer-ai/flashinfer/tree/main/csrc/fused_moe/monomoe)可查。**无正式顶会身份**，Accuracy、Batch/硬件边界与可移植性待进一步严格核验。 |
| 2026 | [MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs](https://www.usenix.org/conference/osdi26/presentation/cheng) | OSDI 2026 | MPK 用 SM 级图表示把多 GPU 推理编译为单一 mega-kernel，实现跨算子软件流水与计算-通信重叠，并以持久内核内运行时执行，端到端 latency 降低至多 1.7× |
| 2026 | [Optimal Software Pipelining and Warp Specialization for Tensor Core GPUs](https://www.usenix.org/conference/osdi26/presentation/soi) | OSDI 2026 | Twill 把软件流水（SWP）与 warp 特化（WS）建模为可由约束求解器整体优化的联合问题，为迭代程序自动推导最优且无启发式的调度，并证明 Hopper/Blackwell 上 Flash Attention 调度的最优性 |
| 2026 | [Taming Dynamic Diffusion LLM Inference through Virtual Static Execution](https://doi.org/10.1145/3797905.3800520) | ICS 2026 | Prism 通过 Physical Bucket、跨迭代 Budget-aware 调度与跳过 Padding 的专用 Kernel，将动态 Diffusion LLM 推理映射为稳定执行计划；论文报告 LLaDA/MoE 推理性能。 |
| 2026 | [XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads](https://doi.org/10.1145/3760250.3762228) | ASPLOS 2026 | 在 Ascend NPU 上把动态 Prefill/Decode 分解为可复用 Meta-kernels 和虚拟 Padding，减少 Dynamic Shape 执行开销。 |

### Communication-Aware Kernels (3)

**跨 GPU/设备的算通协同**：Tile-level Collectives、通信与计算重叠、Device-side 原语；与 Distributed Serving 的区别是决定性贡献在 Kernel/DSL 而非全局服务部署。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [TileLink: Generating Efficient Compute-Communication Overlapping Kernels using Tile-Centric Primitives](https://proceedings.mlsys.org/paper_files/paper/2025/hash/c6ee784cbe46d854843e4c883a3321ef-Abstract-Conference.html) | MLSys 2025 | 以 Tile 为接口生成重叠通信与计算的分布式 Kernel。 |
| 2026 | [ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels](https://proceedings.mlsys.org/paper_files/paper/2026/hash/ff997469ac66cf893c4183efeb22212a-Abstract-Conference.html) | MLSys 2026 | 用可重用通信与同步原语编写 TP/SP/EP 跨卡重叠 Kernel。 |
| 2026 | [Purlin: Separating Orchestration from the Datapath of Collectives](https://arxiv.org/abs/2609.36954) | arXiv 2026 (preprint) | 以 SNAC 编排层和硬件特定 Copy/Reduce Atom 解耦 Collective 语义、同步与数据通路，并集成 SGLang 评估。 |

### Memory, I/O & Hardware Co-design (10)

**Memory Hierarchy、Data Movement 与异构硬件**：HBM/页表、PCIe/DMA、SoC/NPU/FPGA/PIM/TEE 和边缘数据流；必须区分实机、FPGA 原型、RTL 与模拟投影。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference](https://doi.org/10.1109/HPCA61900.2025.00127) | HPCA 2025 | SoC GEMM/PIM GEMV 针对 Prefill/Decode 不同访问模式设计 DRAM 地址重映射以降低权重 Relayout；定制 PIM 硬件性能归因和物理芯片验证尚未确认，不等同商品 GPU/NPU 推理提速（HOLD_EVIDENCE）。 |
| 2025 | [Fast On-device LLM Inference with NPUs](https://doi.org/10.1145/3669940.3707239) | ASPLOS 2025 | llm.npu 将模型子图映射到手机 NPU/CPU/GPU 并流水化执行，处理 NPU 不支持算子及动态 LLM Decode。 |
| 2025 | [LUT Tensor Core: A Software-Hardware Co-Design for LUT-Based Low-Bit LLM Inference](https://doi.org/10.1145/3695053.3731057) | ISCA 2025 | 低比特 LUT-GEMM 的 Fusion、表项对称化及特殊 Tile/指令集设计；论文关注定制硬件计算密度/能效，**不能当作 NVIDIA/Ascend 真实 Tensor Core Kernel 加速**。物理芯片/模拟验证边界与 End-to-end LLM 指标待复核（HOLD_EVIDENCE）。 |
| 2025 | [MAS-ATTENTION: MEMORY-AWARE STREAM PROCESSING FOR ATTENTION ACCELERATION ON RESOURCE-CONSTRAINED EDGE DEVICES](https://proceedings.mlsys.org/paper_files/paper/2025/hash/d3cf1559a8795eb1ed2b3ad52409ac7d-Abstract-Conference.html) | MLSys 2025 | 协调边缘加速器的向量与矩阵执行流水，以多级 Tiling 和缓存覆盖减少片上空间开销；含真实 NPU 验证。 |
| 2025 | [MEADOW: Memory-efficient Dataflow and Data Packing for Low Power Edge LLMs](https://proceedings.mlsys.org/paper_files/paper/2025/hash/259a5df46308d60f8454bd4adcc3b462-Abstract-Conference.html) | MLSys 2025 | 在低功耗 FPGA 上采用 Token-parallel/Head-sequential Dataflow 与无损 Weight Packing，减少 Prefill/Decode 外存访问。 |
| 2025 | [Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking](https://doi.org/10.1145/3676642.3736114) | ASPLOS 2025 | 基于 Neuron Co-Activation 重排手机 Flash 上的稀疏权重，联合预取和访问模式优化减少 IOPS。 |
| 2026 | [Communication-Efficient Verifiable Attention for LLM Inference (VeriAttn)](https://arxiv.org/abs/2606.16352) | arXiv 2026 (preprint) | 将 Attention 计算迁至 GPU、TEE 保留完整性验证，通过 Prefill Pipeline 和 Decode 分区减轻 TEE–GPU 通信；Intel TDX 平台实测。 |
| 2026 | [CoPilotIO: CPU as a Co-Pilot for GPU I/O to Free GPU Compute](https://www.usenix.org/conference/osdi26/presentation/chen-guanyi) | OSDI 2026 | GPU 发起异步 I/O，由 CPU 代理轮询并以设备硬件 Barrier 同步；包含 MoE 推理实测。 |
| 2026 | [I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention](https://doi.org/10.1145/3779212.3790174) | ASPLOS 2026 | 从 Tall-and-Skinny GEMM 推导 Exact Long-context Attention I/O 界，并设计 AttenIO 三层算通重叠、Tiling/Scheduling 和 Softmax 并行；这是 I/O 分析和专用 Accelerator 设计，不能替代真实 GPU/Serving Kernel Bench，完整物理评测待审（HOLD_EVIDENCE）。 |
| 2026 | [MoonBright: A GPU Memory Allocator with Device-Side Page Table Materialization and Deferred TLB Coherence](https://www.usenix.org/conference/osdi26/presentation/zhang-yangyu) | OSDI 2026 | MoonBright 在商品 GPU 上实现设备侧页表物化与延迟 TLB 一致性：元数据留主机、批量页表构建移到 GPU，并以新虚拟地址避免热路径上的 TLB shootdown，降低分配延迟、提升 LLM 推理性能并缓解分配器级外部碎片，纯软件改动即可跑在 NVIDIA/AMD GPU |

### Agentic Kernel Optimization (3)

**自动搜索正确、可运行且高效的 Kernel**：Agent、Bandit、Evolution、Profile Feedback；要求相同搜索预算、真实 Backend 和鲁棒 Correctness Gate。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization](https://proceedings.mlsys.org/paper_files/paper/2026/hash/0f8426558905746fc38da5e335700aec-Abstract-Conference.html) | MLSys 2026 | 针对 Trainium NKI Kernel 的迭代优化与慢/快 Kernel 经验记忆，作者提供 [AccelOpt](https://github.com/zhang677/AccelOpt) 和 LLM-derived NKIBench，在 Trainium 1/2 实机测量 % peak；属于专用 Agentic Kernel Optimization 而非在线 Serving 性能。 |
| 2026 | [KernelBand: Steering LLM-based Kernel Optimization via Hardware-Aware Multi-Armed Bandits](https://proceedings.mlr.press/v306/ran26b.html) | ICML 2026 | 使用 Multi-Armed Bandit、Profiling Bound 剪枝和 Runtime Behavior Clustering 控制 Kernel Search；作者在三种 GPU 架构的 TritonBench-G 实机验证并开源，未验证在线 LLM Serving Goodput。与 KernelFoundry 的 QD Evolution、AccelOpt 的 Optimization Memory 区别明确，作为 Agentic Kernel 前沿待 G5 精审。 |
| 2026 | [KernelFoundry: Hardware-Aware Evolutionary GPU Kernel Optimization](https://proceedings.mlr.press/v306/wiedemann26a.html) | ICML 2026 | Quality-Diversity MAP-Elites、Prompt Co-evolution 与 Template Parameter Search，在 SYCL/CUDA 的 KernelBench/robust-kbench 上实测；虽有跨设备工具价值，但没有 LLM Serving Goodput 证据，暂保留为 Agentic Kernel 前沿例外待 G5 去同质化。 |

### Kernel Profiling & Correctness (2)

**性能诊断和验证工具**：IR-level Profiling、Instrumentation、Memory Safety；工具能力不与 LLM Serving Speedup 混淆。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [KPerfIR: Towards a Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads](https://www.usenix.org/conference/osdi25/presentation/guan) | OSDI 2025 | 在 Triton 编译流程插入可编程 Profiling Pass，把微架构流水事件与源级 IR 关联，作者报告约 8.2% 测量开销、2% 相对误差；为通用 Kernel Profiling **工具**，不是 LLM 推理优化器，作为可迁移性能分析基础保留（KEEP_ADJACENT）。 |
| 2026 | [Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context](https://doi.org/10.1145/3779212.3790241) | ASPLOS 2026 | 针对真实 Triton Kernel 的内存越界/竞争检测提供跨设备 Instrumentation 与源码诊断定位；是可直接用于推理 Kernel Correctness 调试的通用工具，不是推理加速。作为极少数调试基础设施例外保留（KEEP_ADJACENT），Artifact 未复现。 |

*Source/implementation evidence comes from the cited publications. Kernel-only gains are not service-level TTFT/TPOT/Goodput, hardware simulation is not native silicon, and the paper entries are not claimed independently reproduced. Explicit HOLD tags remain unresolved strict-review items.*
