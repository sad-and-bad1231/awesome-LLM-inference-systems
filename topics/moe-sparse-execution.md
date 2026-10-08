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
