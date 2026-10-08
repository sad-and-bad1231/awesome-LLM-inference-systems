# MoE & Sparse Execution

Sparse expert activation, token dispatch, sparse attention and conditional computation.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** The unifying question is executing fewer conditional operations efficiently, including expert placement and sparse-kernel data movement.

**Foundational context.** See also: [SGLang structured runtime (2024) and QServe quantization](../README.md#foundational-and-influential-papers) for adjacent mechanisms.

## Newly admitted · October 2026 (3)

These entries have individually checked primary publication records. Descriptions summarize *the authors' mechanisms and evidence*; they do not imply independent reproduction, nor final adjudication of all earlier repository entries.

| Year | Paper | Venue | Distinct system mechanism |
|---|---|---|---|
| 2024 | [SiDA: Sparsity-Inspired Data-Aware Serving for Efficient and Scalable Large Mixture-of-Experts Models](https://proceedings.mlsys.org/paper_files/paper/2024/hash/698cfaf72a208aef2e78bcac55b74328-Abstract-Conference.html) | MLSys 2024 | 利用专家激活稀疏性，在 GPU/主存间数据感知地调度 MoE 权重以提升可部署规模。 |
| 2025 | [SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/2d04d97593c8c33d415337f408ed0e1b-Abstract-Conference.html) | MLSys 2025 | 按 Head 和输入自适应选取稀疏结构，以 Cumulative Residual Attention 控制稀疏率与精度。 |
| 2026 | [SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading](https://www.usenix.org/conference/nsdi26/presentation/li-xingyi) | NSDI 2026 | 将 Expert All-to-All 的多次缓冲复制融合，并利用 TMA/NVLink 实现低占用的 MoE 通信。 |

**Legacy cohort.** Previously collected Serving papers remain on [Serving Systems](serving-systems.md) pending individual re-admission/reclassification. A paper is not automatically admitted into this category based on a prior status flag.

## Legacy Serving cohort — re-admitted (1)

Reclassified by **primary systems mechanism**, not legacy “Serving” keywords. Bibliographic links have been updated where a stronger individual source was found; other links preserve the original proceedings record.

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2025 | [LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cc8c6b9d89f7a898a29f58869b238e46-Abstract-Conference.html) | MLSys 2025 | 统一 Prefill/Decode 的结构化稀疏 Attention，并设计分层 KV Page 选择。 |

## Newly admitted · Wave 2 (7)

Publisher/conference identity and the distinct inference mechanism were reviewed. Very early compiler papers are included as *foundational execution primitives*; work with cross-model training applicability is explicitly described.

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2022 | [DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale](https://proceedings.mlr.press/v162/rajbhandari22a.html) | ICML 2022 | MoE Expert 并行与通信/分层策略协同，覆盖生产规模推理和训练系统。 |
| 2023 | [Tutel: Adaptive Mixture-of-Experts at Scale](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5616d34cf8ff73942cfd5aa922842556-Abstract-mlsys2023.html) | MLSys 2023 | 自适应 MoE Parallelism 与 All-to-All 通信路径，作为推理和训练的共享执行基础设施。 |
| 2024 | [MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5dfbe6f5671e82c76841ba687a8a9ecb-Abstract-Conference.html) | NeurIPS 2024 | 按 Head 动态识别长文本 Attention 稀疏模式并配套高效 Sparse Prefill Kernel。 |
| 2025 | [Fiddler: CPU-GPU Orchestration for Fast Inference of Mixture-of-Experts Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8cd1ce03ea58b3d7dfd809e4d42f08ea-Abstract-Conference.html) | ICLR 2025 | 以 CPU-GPU 协同执行减少专家权重搬运和空闲 GPU Stall。 |
| 2025 | [MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs](https://doi.org/10.1145/3669940.3707267) | ASPLOS 2025 | 面向显存受限设备的 Expert 加载与流水执行，缓解 MoE 权重驻留瓶颈。 |
| 2025 | [SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference](https://proceedings.mlr.press/v267/zhang25ch.html) | ICML 2025 | 无需重训的训练无关稀疏 Attention，与计算执行策略协同保持效果。 |
| 2025 | [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://proceedings.mlr.press/v267/xu25ag.html) | ICML 2025 | 用 Antidiagonal Scoring 快速识别高价值 Attention Block 并以块稀疏 Kernel 减少 Prefill。 |

