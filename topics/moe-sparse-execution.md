# MoE & Sparse Execution

Sparse expert activation, token dispatch, sparse attention and conditional computation.

[← Topics](README.md) · [← Home](../README.md)

**Scope.** The unifying question is executing fewer conditional operations efficiently, including expert placement and sparse-kernel data movement.

**Foundational context.** See also: [SGLang structured runtime (2024) and QServe quantization](../README.md#foundational-and-influential-papers) for adjacent mechanisms.

## Papers (36)

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2022 | [DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale](https://proceedings.mlr.press/v162/rajbhandari22a.html) | ICML 2022 | MoE Expert 并行与通信/分层策略协同，覆盖生产规模推理和训练系统。 |
| 2023 | [Tutel: Adaptive Mixture-of-Experts at Scale](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5616d34cf8ff73942cfd5aa922842556-Abstract-mlsys2023.html) | MLSys 2023 | 自适应 MoE Parallelism 与 All-to-All 通信路径，作为推理和训练的共享执行基础设施。 |
| 2024 | [MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5dfbe6f5671e82c76841ba687a8a9ecb-Abstract-Conference.html) | NeurIPS 2024 | 按 Head 动态识别长文本 Attention 稀疏模式并配套高效 Sparse Prefill Kernel。 |
| 2024 | [PowerInfer-2: Fast Large Language Model Inference on a Smartphone](https://arxiv.org/abs/2406.06282) | arXiv 2024 (preprint) | Neural Cluster 级 NPU/CPU 异构执行与分段权重缓存把稀疏 MoE/LLM 部署到内存不足的智能手机。 |
| 2024 | [SiDA: Sparsity-Inspired Data-Aware Serving for Efficient and Scalable Large Mixture-of-Experts Models](https://proceedings.mlsys.org/paper_files/paper/2024/hash/698cfaf72a208aef2e78bcac55b74328-Abstract-Conference.html) | MLSys 2024 | 利用专家激活稀疏性，在 GPU/主存间数据感知地调度 MoE 权重以提升可部署规模。 |
| 2025 | [COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) | MLSys 2025 | 细粒度 MoE 任务调度与通信/计算重叠，含生产环境执行证据。 |
| 2025 | [Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking](https://proceedings.mlsys.org/paper_files/paper/2025/hash/afd6374c7f2839cba22f537f15f4f760-Abstract-Conference.html) | MLSys 2025 | 在移动端按 SwiGLU 输入激活进行预测器无关的剪枝，并根据缓存位置调整 Mask。 |
| 2025 | [Fiddler: CPU-GPU Orchestration for Fast Inference of Mixture-of-Experts Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8cd1ce03ea58b3d7dfd809e4d42f08ea-Abstract-Conference.html) | ICLR 2025 | 以 CPU-GPU 协同执行减少专家权重搬运和空闲 GPU Stall。 |
| 2025 | [KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models](https://doi.org/10.1145/3731569.3764843) | SOSP 2025 | 针对 MoE 将常驻 Dense/Attention 与部分 Experts 异构放置，结合 CPU 计算优化和流水调度运行大模型。 |
| 2025 | [LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cc8c6b9d89f7a898a29f58869b238e46-Abstract-Conference.html) | MLSys 2025 | 统一 Prefill/Decode 的结构化稀疏 Attention，并设计分层 KV Page 选择。 |
| 2025 | [MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs](https://doi.org/10.1145/3669940.3707267) | ASPLOS 2025 | 面向显存受限设备的 Expert 加载与流水执行，缓解 MoE 权重驻留瓶颈。 |
| 2025 | [SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/2d04d97593c8c33d415337f408ed0e1b-Abstract-Conference.html) | MLSys 2025 | 按 Head 和输入自适应选取稀疏结构，以 Cumulative Residual Attention 控制稀疏率与精度。 |
| 2025 | [Shortcut-connected Expert Parallelism for Accelerating Mixture of Experts](https://proceedings.mlr.press/v267/cai25c.html) | ICML 2025 | ScMoE 用 Shortcut-connected 结构与 EP 计算/通信 Overlap 缓解 All-to-All 串行依赖，并包含分布式推理实测。 |
| 2025 | [SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference](https://proceedings.mlr.press/v267/zhang25ch.html) | ICML 2025 | 无需重训的训练无关稀疏 Attention，与计算执行策略协同保持效果。 |
| 2025 | [Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving](https://doi.org/10.1145/3725843.3756043) | MICRO 2025 | 结合 Mono3D DRAM/NMP/GPU 的 Hot/Cold Expert 多级放置，利用主题感知路由管理推理吞吐与 SLO。 |
| 2025 | [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://proceedings.mlr.press/v267/xu25ag.html) | ICML 2025 | 用 Antidiagonal Scoring 快速识别高价值 Attention Block 并以块稀疏 Kernel 减少 Prefill。 |
| 2026 | [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://www.usenix.org/conference/osdi26/presentation/wang-wenxin) | OSDI 2026 | 该 CPU-GPU 混合方案以流式/分布式加载 prefill（1200、1800 tokens/s）、节点内 P/D 分离与双批 overlap（延迟增 <15%、吞吐 +50%）、AVX-512 FP8 GEMV（CPU 延迟降 4–5×）和细粒度 CPU 并行（INT4 DeepSeek-V3 达 28 toke… |
| 2026 | [AFORE: Attention-FFN Disaggregation with Overlapped Reconfiguration of Experts](https://arxiv.org/abs/2610.03203) | arXiv 2026 (preprint) | 利用 AFD Microbatch 前瞻负载信号，在流水窗口内重配与迁移 Hot Experts。 |
| 2026 | [Balancing and Beyond: Communication-Centric Optimizations in Expert Parallelism](https://doi.org/10.1145/3789240.3829201) | SIGCOMM 2026 | 面向大规模 Expert Parallelism 联合调整 Expert Placement、跨机数据传输及算通重叠，而非仅优化负载均衡。 |
| 2026 | [Capacity-Aware Inference: Mitigating the Straggler Effect in Mixture of Experts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/94e845868a9ace4bc239d0c529d32f4c-Abstract-Conference.html) | ICLR 2026 | 通过 Expert Capacity 约束和本地候选扩展缓解 EP 负载不均；存在精度/加速权衡。 |
| 2026 | [CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving](https://proceedings.mlsys.org/paper_files/paper/2026/hash/3a7f9e485845dac27423375c934cb4db-Abstract-Conference.html) | MLSys 2026 | CRAFT（MLSys 2026）在给定内存预算下对大规模 MoE 模型做细粒度的逐层专家复制（expert replication），把热门专家复制到多个设备以缓解专家负载不均，从而在不超预算的前提下提升 serving goodput |
| 2026 | [Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement](https://arxiv.org/abs/2607.08782) | arXiv 2026 (preprint) | 预测请求的 Expert 激活并在计算窗口内迁移专家，在线更新分布式 Expert Placement。 |
| 2026 | [Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling](https://arxiv.org/abs/2603.27624) | arXiv 2026 (preprint) | FSE-DP 在多 Chiplet 互联上按动态专家轨迹流式分配 MoE 执行并重叠通信。 |
| 2026 | [FarSkip-Collective: Unhobbling Blocking Communication in Mixture of Experts Models](https://proceedings.mlsys.org/paper_files/paper/2026/hash/6feb9b30798abcfae937760d183605e1-Abstract-Conference.html) | MLSys 2026 | 模型跳连变换与推理系统协同设计，将 EP 阻塞通信隐藏在计算之下。 |
| 2026 | [Least-Loaded Expert Parallelism: Load Balancing An Imbalanced Mixture-of-Experts](https://proceedings.mlr.press/v306/nguyen26m.html) | ICML 2026 | 将超载设备的 Token 及关联 Expert 参数动态重路由至闲置设备，减少 Collective Straggler。 |
| 2026 | [MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading](https://doi.org/10.1145/3779212.3790187) | ASPLOS 2026 | 按 Token/Layer/Sequence 分层管理 Expert 的精度、预取和缓存，减轻显存受限设备的 Expert Loading。 |
| 2026 | [MoE-Lens: Towards the Hardware Limit of High-Throughput MoE LLM Serving Under Resource Constraints](https://doi.org/10.1145/3806645.3807594) | HPDC 2026 | CPU/GPU 混合执行结合硬件上界模型推导 Expert Placement/执行策略，实验比较性能模型与真实吞吐。 |
| 2026 | [MoEntwine: Unleashing the Potential of Wafer-scale Chips for Large-scale Expert Parallel Inference](https://2026.hpca-conf.org/details/hpca-2026-main-conference/25/MoEntwine-Unleashing-the-Potential-of-Wafer-scale-Chips-for-Large-scale-Expert-Paral) | HPCA 2026 | 根据 Wafer-scale 互联重组 MoE Expert Parallel 执行和通信。 |
| 2026 | [Patterns Behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference](https://doi.org/10.1109/ISCA66397.2026.00021) | ISCA 2026 | 预测 MoE 专家访问与搬运模式，减少跨设备专家交换。 |
| 2026 | [Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f0552f14388d95b19740dee809f5cad1-Abstract-Conference.html) | ICLR 2026 | 联合安排 Expert Placement 与 DP 请求/TP Token 数据位置，减少 EP All-to-All 跨设备流量。 |
| 2026 | [Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference](https://arxiv.org/abs/2605.10670) | arXiv 2026 (preprint) | 研究宽 EP 组单 Rank 故障后重建通信成员、专家布局和 CUDA Graph Routing Metadata。 |
| 2026 | [SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading](https://www.usenix.org/conference/nsdi26/presentation/li-xingyi) | NSDI 2026 | 将 Expert All-to-All 的多次缓冲复制融合，并利用 TMA/NVLink 实现低占用的 MoE 通信。 |
| 2026 | [UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods](https://doi.org/10.1145/3789240.3829183) | SIGCOMM 2026 | 面向 SuperPod 拓扑重构 MoE Expert All-to-All 的通信和同步路径，减少 EP 调度的跨节点序列化。 |
| 2026 | [UEP: Portable Expert-Parallel Communication](https://www.usenix.org/conference/osdi26/presentation/mao-ziming-uep) | OSDI 2026 | UEP 用 GPU-CPU 控制通道取代 GPU 发起的 RDMA，由 CPU 代理发 GPUDirect RDMA 以 immediate data 模拟保序，在 EFA 上 dispatch/combine 吞吐提升 2.1×、SGLang token 吞吐提升至多 40% |
| 2026 | [Unified Static–Dynamic Pruning for Efficient LLM Inference](https://doi.org/10.14778/3836663.3836665) | PVLDB 2026 | SPDP 将静态权重与动态激活剪枝映射到 Tiled-CBC 稀疏存储及 Prefill SpMM/Decode SpMspV 专用 GPU Kernel。 |
| 2026 | [ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling](https://proceedings.mlr.press/v306/yang26ds.html) | ICML 2026 | 联合无损 Expert 权重压缩、缓存亲和调度与边缘硬件特性，实现低显存 MoE Serving 原型。 |

*Publication source and mechanism screened; speedup claims are not independently reproduced.*
