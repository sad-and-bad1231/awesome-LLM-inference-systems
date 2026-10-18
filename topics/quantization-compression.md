# Quantization & Compression

Low-bit model representation integrated with actual inference execution and memory/compute savings. **The decisive reusable mechanism determines the subsection**, not bit-width headline, hardware vendor, workload modality, or claimed speedup.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Numeric-representation mechanisms lead this category: weight-only PTQ with codebook/vector/residual compensation, joint weight–activation (W8A8→W4A4KV4) formats with outlier handling, rotation/equivalent-transform quantization, mixed-precision and adaptive-bitwidth allocation, microscaling and extreme low-bit formats with co-designed datapaths, lossless weight compression with entropy coding, and multi-model delta compression. Entries need a substantial inference implementation and an evaluated systems effect; compression theory alone is insufficient. KV-cache-only quantization is kept here but its natural home is [KV Cache & Context Memory](kv-cache-memory.md), and quantized-GEMM kernel/operator implementation belongs to [Kernels & Compilers](kernels-compilers.md).

**Foundational context.** See also: [QServe (2025)](../README.md#foundational-and-influential-papers); rows that anchor a sub-direction of this taxonomy carry an inline `KEEP_FOUNDATIONAL` tag.

## Mechanism map

Eight internal groups, **33 canonical entries in total**. Subsections are a reading/navigation structure, **not new public categories** and not G0–G5 admission verdicts.

| Research mechanism | Papers |
|---|---:|
| [Weight-Only PTQ, Codebook & Residual Quantization](#weight-only-ptq-codebook--residual-quantization-5) | 5 |
| [Weight-Activation Quantization & Outlier Handling](#weight-activation-quantization--outlier-handling-4) | 4 |
| [Rotation & Equivalent-Transform Quantization](#rotation--equivalent-transform-quantization-5) | 5 |
| [Mixed-Precision & Adaptive-Bitwidth Allocation](#mixed-precision--adaptive-bitwidth-allocation-3) | 3 |
| [Extreme Low-Bit Formats, Microscaling & Hardware Co-design](#extreme-low-bit-formats-microscaling--hardware-co-design-7) | 7 |
| [KV-Cache Quantization](#kv-cache-quantization-4) | 4 |
| [Lossless Weight Compression & Entropy Coding](#lossless-weight-compression--entropy-coding-4) | 4 |
| [Multi-Model Delta Compression](#multi-model-delta-compression-1) | 1 |
| **Total** | **33** |

### Where this taxonomy came from

- **vLLM 的量化方法注册表**把权重/激活方案并列陈列：`awq`/`auto_awq`、`gptq`/`auto_gptq`/`gptq_marlin`/`awq_marlin`、`fp8`、`modelopt(_fp4/_mxfp8/_mixed)`、`mxfp4`/`gpt_oss_mxfp4`、`compressed-tensors`、`quark`、`torchao`、`inc`、`experts_int8`、`moe_wna16` 与 online 逐张量/逐块/逐通道缩写——这支撑了本文件"weight-only、W/A 联合、microscaling、混合精度"的分组（[vLLM quantization registry](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/__init__.py)、[vLLM quantization docs](https://docs.vllm.ai/en/stable/features/quantization/)）。
- **TensorRT LLM 的 recipe/硬件矩阵**明确区分 FP4、FP8 per-tensor/block-scaling/rowwise、FP8 与 NVFP4 KV cache、W4A16/W4A8 AWQ 与 GPTQ，并按 Hopper/Blackwell 架构 gate；NVIDIA Model Optimizer 另提供 FP8/FP4 per-block/INT8-SmoothQuant/W4A16/W4A8 AWQ 与 QAT/Distillation 配方（[TensorRT LLM quantization](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/features/quantization.md)、[ModelOpt support matrix](https://nvidia.github.io/Model-Optimizer/guides/0_support_matrix.html)）。
- **SGLang 把 "Quantization" 与 "Quantized KV Cache" 写成两个独立文档章节**，说明工业界把权重/激活量化与 KV-cache-only 量化视为两条线；本文件据此把 KV-cache-only 量化单列成节并标注其自然归属（[SGLang quantization](https://docs.sglang.io/docs/advanced_features/quantization)、[SGLang quantized KV cache](https://docs.sglang.io/docs/advanced_features/quantized_kv_cache)）。
- **Microscaling 已是标准格式而非论文概念**：OCP MX 规范定义 block=32 + E8M0 共享 scale 的 MXFP4/MXFP6/MXFP8/MXINT8；NVIDIA NVFP4 采用 16 值 micro-block + E4M3 scale + 张量级 FP32 的两级缩放；DeepGEMM 的 FP8/MXFP4 kernel 在 SM100 使用 UE8M0 packed scale——"格式 → kernel"的耦合决定了本文件 microscaling/极端低比特分组的边界（[OCP MX spec](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf)、[NVIDIA NVFP4 blog](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)、[DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)）。
- **Weight-only 端侧/CPU 栈**：llama.cpp GGUF 的 k-quants/imatrix 量化、Intel Neural Compressor 的 Static/Dynamic/SmoothQuant/Weight-Only/QAT/Mixed-Precision（含 MXFP8/MXFP4/NVFP4 实验支持）与 AMD Quark 的 OCP FP8/MX 数据类型、AWQ/GPTQ/Qronos 算法及 SmoothQuant/QuaRot 旋转预处理——它们共同划定了"weight-only PTQ、codebook、旋转预处理"三组的边界（[llama.cpp quantize](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md)、[Intel Neural Compressor](https://github.com/intel/neural-compressor)、[AMD Quark](https://quark.docs.amd.com/latest/basic_usage.html)）。
- **同类 awesome list 的分法**与本文件一致：把量化、KV 量化与无损/多模型压缩分开陈列，而非按会议 session 归堆（[LLM-inference-optimization-paper](https://github.com/chenhongyu2048/LLM-inference-optimization-paper)、[Awesome-Efficient-LLM](https://github.com/horseee/Awesome-Efficient-LLM)）。

**Coverage gaps for later discovery — not new admissions:** ① 本页没有 QAT/QLoRA 式量化感知训练与 QAD/蒸馏的独立条目，故未单列 "QAT" 节；② FP8/FP4 训练-服务协同（DeepSeek-V3 FP8 训练、DeepGEMM UE8M0 scale、MX 训练格式）目前主要由 Kernels 页与组织页收录，本页缺专门论文；③ GGUF/k-quant 在 CPU/边缘的执行、imatrix 校准，以及 Marlin/bitsandbytes/compressed-tensors 式 kernel 侧反量化属 Kernels & Compilers 页；④ 2-bit 以下 weight-only、MXFP6/MXINT8 级格式与学习型正交旋转的理论分析在本页偏薄；⑤ 第 6 组 KV-cache-only 量化条目是向 KV Cache & Context Memory 页的再分类候选。机制缺失不作为把"仅实现细节"材料当作同行评审论文引入的理由。

## Papers (33)

### Weight-Only PTQ, Codebook & Residual Quantization (5)

**离线低比特权重表示**：Hessian 引导逐块量化、激活感知缩放、多 Codebook/非均匀码本、CPU 残差保留；区分压缩率与实际 Decode 吞吐。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) | ICLR 2023 | 近似二阶权重逐块量化并设计 GPU 权重量化执行路径，降低大模型显存占用。（KEEP_FOUNDATIONAL） |
| 2024 | [AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2024 | 依据激活选择重要通道并优化权重缩放，配合设备侧低比特推理执行框架。（KEEP_FOUNDATIONAL） |
| 2024 | [Extreme Compression of Large Language Models via Additive Quantization](https://proceedings.mlr.press/v235/egiazarian24a.html) | ICML 2024 | 多 Codebook Additive Quantization 和快速 GPU/CPU 生成路径，覆盖极低位宽模型部署。 |
| 2024 | [SqueezeLLM: Dense-and-Sparse Quantization](https://proceedings.mlr.press/v235/kim24f.html) | ICML 2024 | 非均匀稠密低比特表示与 Outlier 稀疏补偿结合，优化生成执行的精度/速度。 |
| 2025 | [DecDEC: A Systems Approach to Advancing Low-Bit LLM Quantization](https://www.usenix.org/conference/osdi25/presentation/park-yeonhong) | OSDI 2025 | 将量化残差置于 CPU，仅按动态显著通道回传，在低比特质量、显存与延迟间做运行时权衡。 |

### Weight-Activation Quantization & Outlier Handling (4)

**权重与激活联合低比特**：W8A8→W4A4KV4 格式、异常值分解/迁移与可执行低比特 GEMM/serving 路径。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2022 | [GPT3.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://papers.neurips.cc/paper_files/paper/2022/hash/c3ba4962c05c49636d4c6206a97e9c8a-Abstract-Conference.html) | NeurIPS 2022 | LLM.int8 混合精度分解把异常值维度保留 FP16，其余低位宽 GEMM 实际执行。（KEEP_FOUNDATIONAL） |
| 2023 | [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://proceedings.mlr.press/v202/xiao23c.html) | ICML 2023 | 利用数学等价变换将 Activation Outlier 量化难度迁移到权重，实现可执行的 W8A8 GEMM。（KEEP_FOUNDATIONAL） |
| 2024 | [Atom: Low-Bit Quantization for Efficient and Accurate LLM Serving](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5edb57c05c81d04beb716ef1d542fe9e-Abstract-Conference.html) | MLSys 2024 | W4A4 混合精度、细粒度量化与 INT4 算子共同设计，报告 Serving SLO 下的端到端吞吐。 |
| 2025 | [COMET: Towards Practical W4A4KV4 LLMs Serving](https://doi.org/10.1145/3676641.3716252) | ASPLOS 2025 | 联合设计 W4A4KV4 量化、Outlier 处理与低比特 GPU 执行路径，实现端到端 LLM Serving。 |

### Rotation & Equivalent-Transform Quantization (5)

**等价变换抑制量化异常值**：Hadamard/学习/Givens 旋转与可学习等价变换，及其与 W/A/KV 低比特执行路径的融合。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://openreview.net/forum?id=8Wuvhh0LYW) | ICLR 2024 | Block-wise Outlier Suppression 与等价变换学习，支持可部署的 W/A 低比特推理。 |
| 2024 | [QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b5b939436789f76f08b9d0da5e81af7c-Abstract-Conference.html) | NeurIPS 2024 | Hadamard Rotation 去除 Quantization Outliers，结合端到端 INT4 执行实现 W/A/KV 量化。 |
| 2025 | [SpinQuant: LLM Quantization with Learned Rotations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b1c0d4866f72393c522c8a00eed4eb-Abstract-Conference.html) | ICLR 2025 | 学习等价旋转降低量化 Outlier，兼顾 Weight、Activation 和 KV Cache 精度。 |
| 2026 | [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](https://2026.hpca-conf.org/details/hpca-2026-main-conference/38/GyRot-Leveraging-Hidden-Synergy-between-Rotation-and-Fine-grained-Group-Quantization) | HPCA 2026 | 旋转与细粒度分组量化协同，结合低位宽 GEMM 执行。 |
| 2026 | [ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](https://openreview.net/forum?id=1USeVjsKau) | ICLR 2026 (full paper) | 以 Givens Pairwise Rotation + Channel Scaling 抑制 Reasoning LLM Outliers，用 AWQ W4A16 GEMM 加自有变换 Kernel；附录在 RTX A6000、RTX 6000 Ada、RTX 4090、PyTorch 2.6/CUDA Graph、**Batch=1** 逐模型报告 Tokens/s：如 Llama-3-8B **AWQ 120 vs ParoQ 112 tok/s**（A6000），主要收益是较高任务准确率而非优于 AWQ 的运行速度。作者 [GitHub](https://github.com/z-lab/paroquant) 当前开发头已演化，README 要求 `legacy` Branch 重现原论文；在线 Goodput 未验证。（HOLD_EVIDENCE） |

### Mixed-Precision & Adaptive-Bitwidth Allocation (3)

**位宽作为一等分配策略**：按输出特征/全局混合精度、形状自适应 Kernel Dispatch 与运行时质量感知精度调节。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping](https://www.usenix.org/conference/osdi26/presentation/liu-yao) | OSDI 2026 | 面向不对称精度 GEMM 构建 DPR 计算族和轻量 Runtime Dispatch，依据形状与位宽选择 Kernel。 |
| 2026 | [MixLLM: LLM Quantization with Global Mixed-precision between Output-features and Highly-efficient System Design](https://proceedings.mlsys.org/paper_files/paper/2026/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2026 | 跨层按输出特征重要性分配量化位宽，设计反量化与 GEMM 重叠流水。 |
| 2026 | [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/abs/2607.16184) | arXiv 2026 (preprint) | 根据在线 KV 容量压力调节 MoE Expert Weights 的精度，将模型质量、显存与 Batch 吞吐联合优化；真实 MoE Serving 工作负载报告 GPU 内存与端到端性能。（HOLD_EVIDENCE） |

### Extreme Low-Bit Formats, Microscaling & Hardware Co-design (7)

**≤3-bit 数值格式与共设计数据通路**：Microscaling/BFP 格式、自定义数值类型、Bit-serial/PIM 数据通路与极端低比特执行；区分模拟评估与原生硅。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration](https://doi.org/10.1109/HPCA61900.2025.00084) | HPCA 2025 | 软硬协同的 Bit-serial Datapath 支持自适应低比特数值格式与矩阵计算映射，在真实 LLM 模型上评估精度与执行效率。（HOLD_EVIDENCE） |
| 2025 | [M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type](https://doi.org/10.1109/HPCA61900.2025.00086) | HPCA 2025 | 为组级 Weight 和动态 KV 构造 Adaptive Numeric Type 与低成本 PE/量化路径，配套 LLM 硬件执行评估。（HOLD_EVIDENCE） |
| 2025 | [MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators](https://proceedings.mlsys.org/paper_files/paper/2025/hash/9032e5c9ec394ce768a2fa9bdc56af6c-Abstract-Conference.html) | MLSys 2025 | 结合低秩补偿、混合位宽和 Tensor Core 友好 INT3 MoE GEMM。 |
| 2025 | [MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving](https://doi.org/10.1145/3725843.3756118) | MICRO 2025 | 通过 Microscaling Block 中的异常值编码扩展 Mantissa，改善 MXFP4 的精度与格式开销权衡，并评估 GPU 低精度推理的软件执行和硬件映射；非纯精度 Benchmark。 |
| 2026 | [AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization](https://2026.hpca-conf.org/details/hpca-2026-main-conference/22/AQPIM-Breaking-the-PIM-Capacity-Wall-for-LLMs-with-In-Memory-Activation-Quantization) | HPCA 2026 | 在 PIM 内部融合激活压缩和计算以降低带宽与容量瓶颈。（HOLD_EVIDENCE） |
| 2026 | [High-Throughput Non-Uniformly Quantized 3-bit LLM Inference](https://doi.org/10.1145/3774934.3786423) | PPoPP 2026 | Quantix 将非均匀 3-bit 量化的硬件对齐 Bit Shuffle 与 Dequant-Multiply Fusion 映射到 L40 GPU CUDA/TensorCores，报告实际 Kernel 与端到端低精度推理吞吐。 |
| 2026 | [Search Your Block Floating Point Scales!](https://proceedings.mlsys.org/paper_files/paper/2026/hash/633b0e871a48d542280c3ad03928e60d-Abstract-Conference.html) | MLSys 2026 | 优化 BFP Scale 并通过 FP4 Attention Kernel 验证低精度执行。 |

### KV-Cache Quantization (4)

**仅 KV 状态的低比特量化**：KV Outlier 阈值、运行时平滑与 Recent-token 分层表示；KV-cache-only 量化的自然归属是 KV Cache & Context Memory 页，本节仅为阅读结构保留（再分类候选，KEEP_ADJACENT）。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization](https://doi.org/10.1145/3695053.3731019) | ISCA 2025 | 离线确定 KV Outlier Threshold，在线低成本量化并协同 KV MMU/硬件引擎，减少长 Batch Attention 带宽。（KEEP_ADJACENT） |
| 2026 | [JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference](https://doi.org/10.1145/3774934.3786428) | PPoPP 2026 | RtSmooth 运行时平滑离群值，配合 Fast Absmax、Recent-token 分层表示和 Mixed-precision Attention Kernel；报告 KV 质量、显存与端到端 Decode 吞吐对照。（KEEP_ADJACENT） |
| 2026 | [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157) | arXiv 2026 (preprint) | 将 Token-wise INT4 与 Block-diagonal Hadamard Rotation 融合至 Paged KV 的 Quantization/Attention Kernel，公开 SGLang 运行与复现脚本；质量近 BF16 同时保持 Plain INT4 Serving Throughput。（KEEP_ADJACENT） |
| 2026 | [TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5c802ef38ab6e366c2ea06eee554c088-Abstract-Conference.html) | ICLR 2026 | 旋转与向量量化用于低比特 KV 表示；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（KEEP_ADJACENT） |

### Lossless Weight Compression & Entropy Coding (4)

**权重的无损压缩与熵编码**：熵编码/rANS、硬件解压与计算重叠、减少权重 I/O；与有损低比特格式互补，须区分完整精度路径与低比特路径。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [Approaching Shannon Bound with Lossless LLM Weight Compression](https://doi.org/10.1109/ISCA66397.2026.00024) | ISCA 2026 | 面向推理 GEMM Tile 的熵编码与在线无损解码，实测 Serving。 |
| 2026 | [LILo: Harnessing the On-chip Accelerators in Intel CPUs for Compressed LLM Inference Acceleration](https://doi.org/10.1109/HPCA68181.2026.11408577) | HPCA 2026 | Intel IAA 无损权重解压与 AMX/AVX 推理计算重叠，并按 MoE 特征选择性压缩以减少超大模型存储卸载；作者公开了 Xeon IAA 实验 Artifact，复现依赖特定 CPU。 |
| 2026 | [Reducing Memory Requirements of LLM Inference Through Online rANS Decompression](https://doi.org/10.1109/CLOUD72782.2026.00039) | IEEE CLOUD 2026 (full paper) | 对 CPU/磁盘 Weight Offloading 路径执行**无损 rANS** 压缩与在线解码，并将解压融合 GEMM；论文报告集成 vLLM，受权重搬运限制时有效内存容量最高约 +30%、吞吐收益约 2.5–4.4%（作者报告）。**LOSSLESS_OUTPUT** 仅在完整精度路径成立；实际 GPU、Online Decode Microbenchmark、Memory Overhead 与相比 CUDA/Fused Gemm Baseline 仍待严格审计。（HOLD_EVIDENCE） |
| 2026 | [ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression](https://doi.org/10.1145/3779212.3790250) | ASPLOS 2026 | 压缩态权重和 Tensor Core 友好解码协同，减少无损权重 I/O。 |

### Multi-Model Delta Compression (1)

**多模型增量压缩**：以基座模型 Delta 编码与服务端加载/切换，支撑多个全量微调模型的共存服务。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs](https://doi.org/10.1145/3689031.3717468) | EuroSys 2025 | 使用权重 Delta 编码与服务端加载/切换设计支撑多个全量微调模型。 |

---
*Publication source and mechanism screened; speedup claims are not independently reproduced. Kernel-only gains are not service-level TTFT/TPOT/Goodput, hardware simulation is not native silicon, and explicit HOLD tags remain unresolved strict-review items.*
