# Quantization & Compression

Low-bit model representation integrated with actual inference execution and memory/compute savings.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** Accept model quantization only with substantial inference implementation and evaluated systems effect; compression theory alone is insufficient.

**Foundational context.** See also: [QServe (2025)](../README.md#foundational-and-influential-papers).

## Papers (20)

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
| 2025 | [DecDEC: A Systems Approach to Advancing Low-Bit LLM Quantization](https://www.usenix.org/conference/osdi25/presentation/park-yeonhong) | OSDI 2025 | 将量化残差置于 CPU，仅按动态显著通道回传，在低比特质量、显存与延迟间做运行时权衡。 |
| 2025 | [DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs](https://doi.org/10.1145/3689031.3717468) | EuroSys 2025 | 使用权重 Delta 编码与服务端加载/切换设计支撑多个全量微调模型。 |
| 2025 | [MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators](https://proceedings.mlsys.org/paper_files/paper/2025/hash/9032e5c9ec394ce768a2fa9bdc56af6c-Abstract-Conference.html) | MLSys 2025 | 结合低秩补偿、混合位宽和 Tensor Core 友好 INT3 MoE GEMM。 |
| 2025 | [SpinQuant: LLM Quantization with Learned Rotations](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b1c0d4866f72393c522c8a00eed4eb-Abstract-Conference.html) | ICLR 2025 | 学习等价旋转降低量化 Outlier，兼顾 Weight、Activation 和 KV Cache 精度。 |
| 2026 | [ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping](https://www.usenix.org/conference/osdi26/presentation/liu-yao) | OSDI 2026 | 面向不对称精度 GEMM 构建 DPR 计算族和轻量 Runtime Dispatch，依据形状与位宽选择 Kernel。 |
| 2026 | [Approaching Shannon Bound with Lossless LLM Weight Compression](https://doi.org/10.1109/ISCA66397.2026.00024) | ISCA 2026 | 面向推理 GEMM Tile 的熵编码与在线无损解码，实测 Serving。 |
| 2026 | [AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization](https://2026.hpca-conf.org/details/hpca-2026-main-conference/22/AQPIM-Breaking-the-PIM-Capacity-Wall-for-LLMs-with-In-Memory-Activation-Quantization) | HPCA 2026 | 在 PIM 内部融合激活压缩和计算以降低带宽与容量瓶颈。 |
| 2026 | [GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference](https://2026.hpca-conf.org/details/hpca-2026-main-conference/38/GyRot-Leveraging-Hidden-Synergy-between-Rotation-and-Fine-grained-Group-Quantization) | HPCA 2026 | 旋转与细粒度分组量化协同，结合低位宽 GEMM 执行。 |
| 2026 | [MixLLM: LLM Quantization with Global Mixed-precision between Output-features and Highly-efficient System Design](https://proceedings.mlsys.org/paper_files/paper/2026/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html) | MLSys 2026 | 跨层按输出特征重要性分配量化位宽，设计反量化与 GEMM 重叠流水。 |
| 2026 | [Search Your Block Floating Point Scales!](https://proceedings.mlsys.org/paper_files/paper/2026/hash/633b0e871a48d542280c3ad03928e60d-Abstract-Conference.html) | MLSys 2026 | 优化 BFP Scale 并通过 FP4 Attention Kernel 验证低精度执行。 |
| 2026 | [ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression](https://doi.org/10.1145/3779212.3790250) | ASPLOS 2026 | 压缩态权重和 Tensor Core 友好解码协同，减少无损权重 I/O。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
