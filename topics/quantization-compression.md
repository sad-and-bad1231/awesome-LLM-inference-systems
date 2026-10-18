# Quantization & Compression

Low-bit model representation integrated with actual inference execution and memory/compute savings.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Accept model quantization only with substantial inference implementation and evaluated systems effect; compression theory alone is insufficient.

**Foundational context.** See also: [QServe (2025)](../README.md#foundational-and-influential-papers).

## Papers (34)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2022 | [GPT3.int8(): 8-bit Matrix Multiplication for Transformers at Scale](https://papers.neurips.cc/paper_files/paper/2022/hash/c3ba4962c05c49636d4c6206a97e9c8a-Abstract-Conference.html) | NeurIPS 2022 | LLM.int8 混合精度分解把异常值维度保留 FP16，其余低位宽 GEMM 实际执行。 |
| 2023 | [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323) | ICLR 2023 | 近似二阶权重逐块量化并设计 GPU 权重量化执行路径，降低大模型显存占用。 |
| 2023 | [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://proceedings.mlr.press/v202/xiao23c.html) | ICML 2023 | 利用数学等价变换将 Activation Outlier 量化难度迁移到权重，实现可执行的 W8A8 GEMM。 |
| 2024 | [Atom: Low-Bit Quantization for Efficient and Accurate LLM Serving](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5edb57c05c81d04beb716ef1d542fe9e-Abstract-Conference.html) | MLSys 2024 | W4A4 混合精度、细粒度量化与 INT4 算子共同设计，报告 Serving SLO 下的端到端吞吐。 |
| 2024 | [AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2024 | 依据激活选择重要通道并优化权重缩放，配合设备侧低比特推理执行框架。 |
| 2024 | [Extreme Compression of Large Language Models via Additive Quantization](https://proceedings.mlr.press/v235/egiazarian24a.html) | ICML 2024 | 多 Codebook Additive Quantization 和快速 GPU/CPU 生成路径，覆盖极低位宽模型部署。 |
| 2024 | [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://openreview.net/forum?id=8Wuvhh0LYW) | ICLR 2024 | Block-wise Outlier Suppression 与等价变换学习，支持可部署的 W/A 低比特推理。 |
| 2024 | [QuaRot: Outlier-Free 4-Bit Inference in Rotated LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b5b939436789f76f08b9d0da5e81af7c-Abstract-Conference.html) | NeurIPS 2024 | Hadamard Rotation 去除 Quantization Outliers，结合端到端 INT4 执行实现 W/A/KV 量化。 |
| 2024 | [SqueezeLLM: Dense-and-Sparse Quantization](https://proceedings.mlr.press/v235/kim24f.html) | ICML 2024 | 非均匀稠密低比特表示与 Outlier 稀疏补偿结合，优化生成执行的精度/速度。 |
| 2025 | [BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration](https://doi.org/10.1109/HPCA61900.2025.00084) | HPCA 2025 | 软硬协同的 Bit-serial Datapath 支持自适应低比特数值格式与矩阵计算映射，在真实 LLM 模型上评估精度与执行效率。 |
| 2025 | [COMET: Towards Practical W4A4KV4 LLMs Serving](https://doi.org/10.1145/3676641.3716252) | ASPLOS 2025 | 联合设计 W4A4KV4 量化、Outlier 处理与低比特 GPU 执行路径，实现端到端 LLM Serving。 |
| 2025 | [DecDEC: A Systems Approach to Advancing Low-Bit LLM Quantization](https://www.usenix.org/conference/osdi25/presentation/park-yeonhong) | OSDI 2025 | 将量化残差置于 CPU，仅按动态显著通道回传，在低比特质量、显存与延迟间做运行时权衡。 |
| 2025 | [DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs](https://doi.org/10.1145/3689031.3717468) | EuroSys 2025 | 使用权重 Delta 编码与服务端加载/切换设计支撑多个全量微调模型。 |
| 2025 | [M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type](https://doi.org/10.1109/HPCA61900.2025.00086) | HPCA 2025 | 为组级 Weight 和动态 KV 构造 Adaptive Numeric Type 与低成本 PE/量化路径，配套 LLM 硬件执行评估。 |
| 2025 | [MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators](https://proceedings.mlsys.org/paper_files/paper/2025/hash/9032e5c9ec394ce768a2fa9bdc56af6c-Abstract-Conference.html) | MLSys 2025 | 结合低秩补偿、混合位宽和 Tensor Core 友好 INT3 MoE GEMM。 |
| 2025 | [MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving](https://doi.org/10.1145/3725843.3756118) | MICRO 2025 | 通过 Microscaling Block 中的异常值编码扩展 Mantissa，改善 MXFP4 的精度与格式开销权衡，并评估 GPU 低精度推理的软件执行和硬件映射；非纯精度 Benchmark。 |
| 2025 | [Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization](https://doi.org/10.1145/3695053.3731019) | ISCA 2025 | 离线确定 KV Outlier Threshold，在线低成本量化并协同 KV MMU/硬件引擎，减少长 Batch Attention 带宽。 |
| 2025 | [SpinQuant: LLM Quantization with Learned Rotations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b1c0d4866f72393c522c8a00eed4eb-Abstract-Conference.html) | ICLR 2025 | 学习等价旋转降低量化 Outlier，兼顾 Weight、Activation 和 KV Cache 精度。 |
| 2026 | [ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping](https://www.usenix.org/conference/osdi26/presentation/liu-yao) | OSDI 2026 | 面向不对称精度 GEMM 构建 DPR 计算族和轻量 Runtime Dispatch，依据形状与位宽选择 Kernel。 |
| 2026 | [Approaching Shannon Bound with Lossless LLM Weight Compression](https://doi.org/10.1109/ISCA66397.2026.00024) | ISCA 2026 | 面向推理 GEMM Tile 的熵编码与在线无损解码，实测 Serving。 |
| 2026 | [AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization](https://2026.hpca-conf.org/details/hpca-2026-main-conference/22/AQPIM-Breaking-the-PIM-Capacity-Wall-for-LLMs-with-In-Memory-Activation-Quantization) | HPCA 2026 | 在 PIM 内部融合激活压缩和计算以降低带宽与容量瓶颈。 |
| 2026 | [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](https://2026.hpca-conf.org/details/hpca-2026-main-conference/38/GyRot-Leveraging-Hidden-Synergy-between-Rotation-and-Fine-grained-Group-Quantization) | HPCA 2026 | 旋转与细粒度分组量化协同，结合低位宽 GEMM 执行。 |
| 2026 | [High-Throughput Non-Uniformly Quantized 3-bit LLM Inference](https://doi.org/10.1145/3774934.3786423) | PPoPP 2026 | Quantix 将非均匀 3-bit 量化的硬件对齐 Bit Shuffle 与 Dequant-Multiply Fusion 映射到 L40 GPU CUDA/TensorCores，报告实际 Kernel 与端到端低精度推理吞吐。 |
| 2026 | [JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference](https://doi.org/10.1145/3774934.3786428) | PPoPP 2026 | RtSmooth 运行时平滑离群值，配合 Fast Absmax、Recent-token 分层表示和 Mixed-precision Attention Kernel；报告 KV 质量、显存与端到端 Decode 吞吐对照。 |
| 2026 | [LILo: Harnessing the On-chip Accelerators in Intel CPUs for Compressed LLM Inference Acceleration](https://doi.org/10.1109/HPCA68181.2026.11408577) | HPCA 2026 | Intel IAA 无损权重解压与 AMX/AVX 推理计算重叠，并按 MoE 特征选择性压缩以减少超大模型存储卸载；作者公开了 Xeon IAA 实验 Artifact，复现依赖特定 CPU。 |
| 2026 | [LO-BCQ: Locally Optimal Block Clustered Quantization for 4-bit (W4A4) LLM Inference](https://icml.cc/virtual/2026/poster/68796) | ICML 2026 | W4A4 分块聚类量化与实际算子效率；快速准入（会议节目／索引）。实际设备、强基线、精度与端到端 Serving 指标留待二审。 |
| 2026 | [MixLLM: LLM Quantization with Global Mixed-precision between Output-features and Highly-efficient System Design](https://proceedings.mlsys.org/paper_files/paper/2026/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2026 | 跨层按输出特征重要性分配量化位宽，设计反量化与 GEMM 重叠流水。 |
| 2026 | [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/abs/2607.16184) | arXiv 2026 (preprint) | 根据在线 KV 容量压力调节 MoE Expert Weights 的精度，将模型质量、显存与 Batch 吞吐联合优化；真实 MoE Serving 工作负载报告 GPU 内存与端到端性能。 |
| 2026 | [ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference](https://iclr.cc/virtual/2026/poster/10011824) | ICLR 2026 | 对推理模型进行 Pairwise Rotation 低比特量化；作者[实现](https://github.com/z-lab/paroquant)提供 Qwen3 量化/导出与 vLLM Serving 路径，论文附录对 RTX A6000 的 W4A16/FP16 Batch=1 Decoding Tokens/s 与 AWQ/QTIP 做比较。模型质量、同核公平性与在线 SLO Goodput 仍待审。 |
| 2026 | [Reducing Memory Requirements of LLM Inference Through Online rANS Decompression](https://services.conferences.computer.org/2026/cloud-program/#reducing-memory-requirements-of-llm-inference-through-online-rans-decompression) | IEEE CLOUD 2026 | 在线熵解码与 LLM 权重存储、计算的解压开销；快速准入（会议节目／索引）。实际设备、强基线、精度与端到端 Serving 指标留待二审。 |
| 2026 | [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157) | arXiv 2026 (preprint) | 将 Token-wise INT4 与 Block-diagonal Hadamard Rotation 融合至 Paged KV 的 Quantization/Attention Kernel，公开 SGLang 运行与复现脚本；质量近 BF16 同时保持 Plain INT4 Serving Throughput。 |
| 2026 | [Search Your Block Floating Point Scales!](https://proceedings.mlsys.org/paper_files/paper/2026/hash/633b0e871a48d542280c3ad03928e60d-Abstract-Conference.html) | MLSys 2026 | 优化 BFP Scale 并通过 FP4 Attention Kernel 验证低精度执行。 |
| 2026 | [TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5c802ef38ab6e366c2ea06eee554c088-Abstract-Conference.html) | ICLR 2026 | 旋转与向量量化用于低比特 KV 表示；快速准入（正式出版论文入口）。实际设备、强基线、精度与端到端 Serving 指标留待二审。 |
| 2026 | [ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression](https://doi.org/10.1145/3779212.3790250) | ASPLOS 2026 | 压缩态权重和 Tensor Core 友好解码协同，减少无损权重 I/O。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
