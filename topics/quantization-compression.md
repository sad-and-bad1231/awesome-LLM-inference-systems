# Quantization & Compression

**Start with the engineering bottleneck, then pick papers.** 要降低权重、激活或 KV 的存储与算力成本：先选 Weight-only、W/A 量化、Mixed Precision、KV 低比特，还是无损压缩？

[← Topics](README.md) · [← Home](../README.md)

**Engineering references:** [vLLM quantization](https://docs.vllm.ai/en/stable/features/quantization/) · [NVIDIA Model Optimizer](https://github.com/NVIDIA/Model-Optimizer) · [SGLang quantized KV](https://docs.sglang.io/docs/advanced_features/quantized_kv_cache).

**Foundational context.** See also: [QServe (2025)](../README.md#foundational-and-influential-papers); rows that anchor a sub-direction of this taxonomy carry an inline `KEEP_FOUNDATIONAL` tag.

## Research directions (6)

这些是可直接立项/实现/Benchmark 的**方向**，不是严密的学术分类。论文按主要优化对象只出现一次；不同方向的论文也可以互为 Related Work。

| Direction | Papers | What to work on |
|---|---:|---|
| [Weight-Only & Rotation](#weight-only--rotation-12) | 12 | GPTQ/AWQ、Codebook 与旋转变换后的权重量化。 |
| [Weight-Activation & Hardware Formats](#weight-activation--hardware-formats-12) | 12 | W/A 量化、Outlier、FP8/FP4/MX 等格式与硬件映射。 |
| [Mixed Precision & Bit Allocation](#mixed-precision--bit-allocation-3) | 3 | 不同 Layer/Channel/专家分配 Bitwidth 与误差预算。 |
| [KV Cache Quantization](#kv-cache-quantization-4) | 4 | KV 独立低比特表示和解量化执行；不重复收录到 KV 主类。 |
| [Recurrent State Quantization](#recurrent-state-quantization-1) | 1 | 线性 Attention/递推模型的持久状态量化，关注误差累积、状态访存与 Serving 内存。 |
| [Lossless & Delta Compression](#lossless--delta-compression-6) | 6 | 无损熵编码、权重流式解压与多模型 Delta。 |
| **Total** | **38** | |

## Papers (38)

### Weight-Only & Rotation (12)

GPTQ/AWQ、Codebook 与旋转变换后的权重量化。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2023 | [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) | ICLR 2023 | 近似二阶权重逐块量化并设计 GPU 权重量化执行路径，降低大模型显存占用。（KEEP_FOUNDATIONAL） |
| 2024 | [AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2024 | 依据激活选择重要通道并优化权重缩放，配合设备侧低比特推理执行框架。（KEEP_FOUNDATIONAL） |
| 2024 | [Extreme Compression of Large Language Models via Additive Quantization](https://proceedings.mlr.press/v235/egiazarian24a.html) | ICML 2024 | 多 Codebook Additive Quantization 和快速 GPU/CPU 生成路径，覆盖极低位宽模型部署。 |
| 2024 | [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://openreview.net/forum?id=8Wuvhh0LYW) | ICLR 2024 | Block-wise Outlier Suppression 与等价变换学习，支持可部署的 W/A 低比特推理。 |
| 2024 | [QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b5b939436789f76f08b9d0da5e81af7c-Abstract-Conference.html) | NeurIPS 2024 | Hadamard Rotation 去除 Quantization Outliers，结合端到端 INT4 执行实现 W/A/KV 量化。 |
| 2024 | [SqueezeLLM: Dense-and-Sparse Quantization](https://proceedings.mlr.press/v235/kim24f.html) | ICML 2024 | 非均匀稠密低比特表示与 Outlier 稀疏补偿结合，优化生成执行的精度/速度。 |
| 2025 | [DecDEC: A Systems Approach to Advancing Low-Bit LLM Quantization](https://www.usenix.org/conference/osdi25/presentation/park-yeonhong) | OSDI 2025 | 将量化残差置于 CPU，仅按动态显著通道回传，在低比特质量、显存与延迟间做运行时权衡。 |
| 2025 | [Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment](https://openreview.net/forum?id=l4F50jpiVH) | NeurIPS 2025 | 推导高斯化权重在给定比特预算下的信息论最优比特分配，给出从格栅编码量化到向量、标量量化的分数比特量化器族与配套 CUDA 内核，并联合优化量化器选择与层融合决策。 |
| 2025 | [SpinQuant: LLM Quantization with Learned Rotations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b1c0d4866f72393c522c8a00eed4eb-Abstract-Conference.html) | ICLR 2025 | 学习等价旋转降低量化 Outlier，兼顾 Weight、Activation 和 KV Cache 精度。 |
| 2026 | [Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b87bb4f6346d727b265088235e5bc389-Abstract-Conference.html) | ICLR 2026 | 针对 NVFP4 小分组使离群抑制失效、MXFP4 二次幂缩放误差偏大的问题，提出旋转融合进权重的 GPTQ 变体并对激活在线旋转，配高性能 GPU 内核；B200 上层内 3.6 倍、端到端 2.2 倍加速。 |
| 2026 | [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](https://2026.hpca-conf.org/details/hpca-2026-main-conference/38/GyRot-Leveraging-Hidden-Synergy-between-Rotation-and-Fine-grained-Group-Quantization) | HPCA 2026 | 旋转与细粒度分组量化协同，结合低位宽 GEMM 执行。 |
| 2026 | [ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](https://openreview.net/forum?id=1USeVjsKau) | ICLR 2026 (full paper) | 以 Givens Pairwise Rotation + Channel Scaling 抑制 Reasoning LLM Outliers，用 AWQ W4A16 GEMM 加自有变换 Kernel；附录在 RTX A6000、RTX 6000 Ada、RTX 4090、PyTorch 2.6/CUDA Graph、**Batch=1** 逐模型报告 Tokens/s：如 Llama-3-8B **AWQ 120 vs ParoQ 112 tok/s**（A6000），主要收益是较高任务准确率而非优于 AWQ 的运行速度。作者 [GitHub](https://github.com/z-lab/paroquant) 当前开发头已演化，README 要求 `legacy` Branch 重现原论文；在线 Goodput 未验证。（HOLD_EVIDENCE） |

### Weight-Activation & Hardware Formats (12)

W/A 量化、Outlier、FP8/FP4/MX 等格式与硬件映射。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2022 | [GPT3.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://papers.neurips.cc/paper_files/paper/2022/hash/c3ba4962c05c49636d4c6206a97e9c8a-Abstract-Conference.html) | NeurIPS 2022 | LLM.int8 混合精度分解把异常值维度保留 FP16，其余低位宽 GEMM 实际执行。（KEEP_FOUNDATIONAL） |
| 2023 | [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://proceedings.mlr.press/v202/xiao23c.html) | ICML 2023 | 利用数学等价变换将 Activation Outlier 量化难度迁移到权重，实现可执行的 W8A8 GEMM。（KEEP_FOUNDATIONAL） |
| 2024 | [Atom: Low-Bit Quantization for Efficient and Accurate LLM Serving](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5edb57c05c81d04beb716ef1d542fe9e-Abstract-Conference.html) | MLSys 2024 | W4A4 混合精度、细粒度量化与 INT4 算子共同设计，报告 Serving SLO 下的端到端吞吐。 |
| 2025 | [BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration](https://doi.org/10.1109/HPCA61900.2025.00084) | HPCA 2025 | 软硬协同的 Bit-serial Datapath 支持自适应低比特数值格式与矩阵计算映射，在真实 LLM 模型上评估精度与执行效率。（HOLD_EVIDENCE） |
| 2025 | [COMET: Towards Practical W4A4KV4 LLMs Serving](https://doi.org/10.1145/3676641.3716252) | ASPLOS 2025 | 联合设计 W4A4KV4 量化、Outlier 处理与低比特 GPU 执行路径，实现端到端 LLM Serving。 |
| 2025 | [M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type](https://doi.org/10.1109/HPCA61900.2025.00086) | HPCA 2025 | 为组级 Weight 和动态 KV 构造 Adaptive Numeric Type 与低成本 PE/量化路径，配套 LLM 硬件执行评估。（HOLD_EVIDENCE） |
| 2025 | [MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators](https://proceedings.mlsys.org/paper_files/paper/2025/hash/9032e5c9ec394ce768a2fa9bdc56af6c-Abstract-Conference.html) | MLSys 2025 | 结合低秩补偿、混合位宽和 Tensor Core 友好 INT3 MoE GEMM。 |
| 2025 | [MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving](https://doi.org/10.1145/3725843.3756118) | MICRO 2025 | 通过 Microscaling Block 中的异常值编码扩展 Mantissa，改善 MXFP4 的精度与格式开销权衡，并评估 GPU 低精度推理的软件执行和硬件映射；非纯精度 Benchmark。 |
| 2026 | [AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization](https://2026.hpca-conf.org/details/hpca-2026-main-conference/22/AQPIM-Breaking-the-PIM-Capacity-Wall-for-LLMs-with-In-Memory-Activation-Quantization) | HPCA 2026 | 在 PIM 内部融合激活压缩和计算以降低带宽与容量瓶颈。（HOLD_EVIDENCE） |
| 2026 | [High-Throughput Non-Uniformly Quantized 3-bit LLM Inference](https://doi.org/10.1145/3774934.3786423) | PPoPP 2026 | Quantix 将非均匀 3-bit 量化的硬件对齐 Bit Shuffle 与 Dequant-Multiply Fusion 映射到 L40 GPU CUDA/TensorCores，报告实际 Kernel 与端到端低精度推理吞吐。 |
| 2026 | [Search Your Block Floating Point Scales!](https://proceedings.mlsys.org/paper_files/paper/2026/hash/633b0e871a48d542280c3ad03928e60d-Abstract-Conference.html) | MLSys 2026 | 优化 BFP Scale 并通过 FP4 Attention Kernel 验证低精度执行。 |
| 2026 | [TWLA: Achieving Ternary Weights and Low-Bit Activations for LLMs via Post-Training Quantization](https://openreview.net/forum?id=s1WSLFmnr8) | ICML 2026 | 用欧氏初始化到流形重定位的非对称三值量化器，加 Kronecker 结构正交旋转把权重整形成三峰分布并抑制激活离群，再以层间二阶交互代价做激活混合位宽分配，在 W1.58A4 下保持精度。 （APPROXIMATE_QUALITY_CHECKED；W1.58A4 与原精度模型须做质量-延迟同条件比较，非逐 Token 完全一致。） |

### Mixed Precision & Bit Allocation (3)

不同 Layer/Channel/专家分配 Bitwidth 与误差预算。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping](https://www.usenix.org/conference/osdi26/presentation/liu-yao) | OSDI 2026 | 面向不对称精度 GEMM 构建 DPR 计算族和轻量 Runtime Dispatch，依据形状与位宽选择 Kernel。 |
| 2026 | [MixLLM: LLM Quantization with Global Mixed-precision between Output-features and Highly-efficient System Design](https://proceedings.mlsys.org/paper_files/paper/2026/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2026 | 跨层按输出特征重要性分配量化位宽，设计反量化与 GEMM 重叠流水。 |
| 2026 | [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/abs/2607.16184) | arXiv 2026 (preprint) | 根据在线 KV 容量压力调节 MoE Expert Weights 的精度，将模型质量、显存与 Batch 吞吐联合优化；真实 MoE Serving 工作负载报告 GPU 内存与端到端性能。（HOLD_EVIDENCE） |

### KV Cache Quantization (4)

KV 独立低比特表示和解量化执行；不重复收录到 KV 主类。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization](https://doi.org/10.1145/3695053.3731019) | ISCA 2025 | 离线确定 KV Outlier Threshold，在线低成本量化并协同 KV MMU/硬件引擎，减少长 Batch Attention 带宽。（KEEP_ADJACENT） |
| 2026 | [JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference](https://doi.org/10.1145/3774934.3786428) | PPoPP 2026 | RtSmooth 运行时平滑离群值，配合 Fast Absmax、Recent-token 分层表示和 Mixed-precision Attention Kernel；报告 KV 质量、显存与端到端 Decode 吞吐对照。（KEEP_ADJACENT） |
| 2026 | [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157) | arXiv 2026 (preprint) | 将 Token-wise INT4 与 Block-diagonal Hadamard Rotation 融合至 Paged KV 的 Quantization/Attention Kernel，公开 SGLang 运行与复现脚本；质量近 BF16 同时保持 Plain INT4 Serving Throughput。（KEEP_ADJACENT） |
| 2026 | [TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5c802ef38ab6e366c2ea06eee554c088-Abstract-Conference.html) | ICLR 2026 | 旋转与向量量化用于低比特 KV 表示；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。（KEEP_ADJACENT） |

### Recurrent State Quantization (1)

线性 Attention / Hybrid LLM 的持久 Recurrent State 低比特表示；关注递推误差、状态读写流量与并发 Serving 内存，不等同于 KV Cache Quantization。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2026 | [LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization](https://arxiv.org/abs/2609.38166) | arXiv 2026 (preprint) | 对 Gated DeltaNet/Kimi Delta Attention 等递推状态采用窗口级量化，并用高精度 Compensator Tokens 与 Residual Smoothing 控制误差累积和离群值；作者在 NVIDIA B200、RTX PRO 6000、RTX 5090 报告 Kernel 加速 2.05–3.70×、端到端输出吞吐提升 1.23–1.65×，状态存储流量约降低 3.4×、特定模型端到端内存减少 41–56%。未找到作者公开完整复现代码；结果为作者报告，非独立复现。（KEEP_STRICT; PREPRINT; REAL_GPU; APPROXIMATE_QUALITY_CHECKED） |

### Lossless & Delta Compression (6)

无损熵编码、权重流式解压与多模型 Delta。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs](https://doi.org/10.1145/3689031.3717468) | EuroSys 2025 | 使用权重 Delta 编码与服务端加载/切换设计支撑多个全量微调模型。 |
| 2026 | [Approaching Shannon Bound with Lossless LLM Weight Compression](https://doi.org/10.1109/ISCA66397.2026.00024) | ISCA 2026 | 面向推理 GEMM Tile 的熵编码与在线无损解码，实测 Serving。 |
| 2026 | [ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs](https://arxiv.org/abs/2604.03298) | ISCA 2026 | 面向 Ascend NPU 的权重无损压缩：块式定长编码、分层折半位打包、向量化无分支整数变换与段内解耦前缀和扫描；吞吐比 DietGPU 高 3.43 倍，端到端最高加速 6.3 倍。 |
| 2026 | [LILo: Harnessing the On-chip Accelerators in Intel CPUs for Compressed LLM Inference Acceleration](https://doi.org/10.1109/HPCA68181.2026.11408577) | HPCA 2026 | Intel IAA 无损权重解压与 AMX/AVX 推理计算重叠，并按 MoE 特征选择性压缩以减少超大模型存储卸载；作者公开了 Xeon IAA 实验 Artifact，复现依赖特定 CPU。 |
| 2026 | [Reducing Memory Requirements of LLM Inference Through Online rANS Decompression](https://doi.org/10.1109/CLOUD72782.2026.00039) | IEEE CLOUD 2026 (full paper) | 对 CPU/磁盘 Weight Offloading 路径执行**无损 rANS** 压缩与在线解码，并将解压融合 GEMM；论文报告集成 vLLM，受权重搬运限制时有效内存容量最高约 +30%、吞吐收益约 2.5–4.4%（作者报告）。**LOSSLESS_OUTPUT** 仅在完整精度路径成立；实际 GPU、Online Decode Microbenchmark、Memory Overhead 与相比 CUDA/Fused Gemm Baseline 仍待严格审计。（HOLD_EVIDENCE） |
| 2026 | [ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression](https://doi.org/10.1145/3779212.3790250) | ASPLOS 2026 | 压缩态权重和 Tensor Core 友好解码协同，减少无损权重 I/O。 |

*Paper links, venue, and mechanism notes are preserved from the prior curation. Inline HOLD/KEEP labels are review notes, not G0–G5 acceptance verdicts. Reported speedups are not independently reproduced.*
