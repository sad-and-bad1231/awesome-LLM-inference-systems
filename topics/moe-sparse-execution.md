# MoE & Sparse Execution

**Start with the engineering bottleneck, then pick papers.** 要优化 MoE：路由/通信、专家放置与负载均衡、专家权重驻留/卸载，还是利用 Attention/FFN 稀疏性？

[← Topics](README.md) · [← Home](../README.md)

**Engineering references:** [vLLM expert parallelism](https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/) · [DeepEP](https://github.com/deepseek-ai/DeepEP) · [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM).

**Foundational context.** See also: [SGLang structured runtime (2024) and QServe quantization](../README.md#foundational-and-influential-papers) for adjacent mechanisms.

## Research directions (4)

这些是可直接立项/实现/Benchmark 的**方向**，不是严密的学术分类。论文按主要优化对象只出现一次；不同方向的论文也可以互为 Related Work。

| Direction | Papers | What to work on |
|---|---:|---|
| [Expert Routing & Communication](#expert-routing--communication-16) | 16 | Token Dispatch、Expert Parallel 和计算通信重叠。 |
| [Placement, Balance & MoE Serving](#placement-balance--moe-serving-11) | 11 | 专家放置/复制/动态负载均衡与 MoE 服务容量。 |
| [Expert Offload & Heterogeneous Execution](#expert-offload--heterogeneous-execution-18) | 18 | 权重驻留、CPU/NPU/GPU Offload、Prefetch 与异构执行。 |
| [Sparse Attention & Conditional Compute](#sparse-attention--conditional-compute-19) | 19 | 稀疏 Attention、FFN/Neuron 剪枝及选择性计算。 |
| **Total** | **64** | |

## Papers (64)

### Expert Routing & Communication (16)

Token Dispatch、Expert Parallel 和计算通信重叠。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2022 | [DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale](https://proceedings.mlr.press/v162/rajbhandari22a.html) | ICML 2022 | MoE Expert 并行与通信/分层策略协同，覆盖生产规模推理和训练系统。（KEEP_FOUNDATIONAL） |
| 2023 | [Tutel: Adaptive Mixture-of-Experts at Scale](https://proceedings.mlsys.org/paper_files/paper/2023/hash/5616d34cf8ff73942cfd5aa922842556-Abstract-mlsys2023.html) | MLSys 2023 | 自适应 MoE Parallelism 与 All-to-All 通信路径，作为推理和训练的共享执行基础设施。（KEEP_FOUNDATIONAL） |
| 2025 | [COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) | MLSys 2025 | 细粒度 MoE 任务调度与通信/计算重叠，含生产环境执行证据。 |
| 2025 | [Shortcut-connected Expert Parallelism for Accelerating Mixture of Experts](https://proceedings.mlr.press/v267/cai25c.html) | ICML 2025 | ScMoE 用 Shortcut-connected 结构与 EP 计算/通信 Overlap 缓解 All-to-All 串行依赖，并包含分布式推理实测。（REQUIRES_FINETUNING） |
| 2026 | [Balancing and Beyond: Communication-Centric Optimizations in Expert Parallelism](https://doi.org/10.1145/3789240.3829201) | SIGCOMM 2026 | 面向大规模 Expert Parallelism 联合调整 Expert Placement、跨机数据传输及算通重叠，而非仅优化负载均衡。（HOLD_EVIDENCE） |
| 2026 | [Capacity-Aware Inference: Mitigating the Straggler Effect in Mixture of Experts](https://proceedings.iclr.cc/paper_files/paper/2026/hash/94e845868a9ace4bc239d0c529d32f4c-Abstract-Conference.html) | ICLR 2026 | 通过 Expert Capacity 约束和本地候选扩展缓解 EP 负载不均；存在精度/加速权衡。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [FarSkip-Collective: Unhobbling Blocking Communication in Mixture of Experts Models](https://proceedings.mlsys.org/paper_files/paper/2026/hash/6feb9b30798abcfae937760d183605e1-Abstract-Conference.html) | MLSys 2026 | 模型跳连变换与推理系统协同设计，将 EP 阻塞通信隐藏在计算之下。（HOLD_EVIDENCE） |
| 2026 | [LYNX: Workload-Agnostic Expert Remapping for Efficient MoE Inference](https://mlsys.org/virtual/2026/poster/10188) | MLSys 2026 (conference index; camera-ready HOLD) | **AffinityBinning** 在 MoE Batch 内重映射低亲和度的 Token→Expert 选择，以减少激活 Expert 数；**MODEL_CHANGED / 非严格输出等价**。作者 [arXiv 2411.08982](https://arxiv.org/abs/2411.08982) 使用不同标题并报告四模型家族/九任务吞吐与质量权衡；[vLLM 插件](https://github.com/gt-nexs/lynx)可供检查，但 README 的 2.0× 口径不应与论文的 1.30× 混用。最终 MLSys 标题/实验版本与在线 Baseline Parity 待复审。（HOLD_IDENTITY） |
| 2026 | [MoEntwine: Unleashing the Potential of Wafer-scale Chips for Large-scale Expert Parallel Inference](https://2026.hpca-conf.org/details/hpca-2026-main-conference/25/MoEntwine-Unleashing-the-Potential-of-Wafer-scale-Chips-for-Large-scale-Expert-Paral) | HPCA 2026 | 根据 Wafer-scale 互联重组 MoE Expert Parallel 执行和通信。 |
| 2026 | [Opportunistic Expert Activation: Batch-Aware Expert Routing for Faster Decode Without Retraining](https://proceedings.mlr.press/v306/oncescu26a.html) | ICML 2026 | Batch-aware Expert Piggybacking 将部分 Token 路由到 Batch 中已加载的 Expert，降低 MoE Decode 活跃 Expert 数；作者在 Qwen3 报告 Layer Latency 下降，必须注明可能有质量退化。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [Patterns Behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference](https://doi.org/10.1109/ISCA66397.2026.00021) | ISCA 2026 | 预测 MoE 专家访问与搬运模式，减少跨设备专家交换。 |
| 2026 | [SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5d07eb2335d88b1dfcefcc3d2da2a230-Abstract-Conference.html) | ICLR 2026 | 利用 Batch 中的 Expert 相似性，将 Secondary Expert Token 重新路由到可替代 Primary Expert，辅以 CUDA Kernel/vLLM 集成；需分别审查速度收益、专家语义变化和模型质量。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [Surviving Partial Rank Failures in Wide Expert-Parallel MoE Inference](https://arxiv.org/abs/2605.10670) | arXiv 2026 (preprint) | 研究宽 EP 组单 Rank 故障后重建通信成员、专家布局和 CUDA Graph Routing Metadata。（HOLD_EVIDENCE） |
| 2026 | [SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading](https://www.usenix.org/conference/nsdi26/presentation/li-xingyi) | NSDI 2026 | 将 Expert All-to-All 的多次缓冲复制融合，并利用 TMA/NVLink 实现低占用的 MoE 通信。 |
| 2026 | [UBEP: Re-architecting Expert Parallelism Communication Library for Production Superpods](https://doi.org/10.1145/3789240.3829183) | SIGCOMM 2026 | 面向 SuperPod 拓扑重构 MoE Expert All-to-All 的通信和同步路径，减少 EP 调度的跨节点序列化。 |
| 2026 | [UEP: Portable Expert-Parallel Communication](https://www.usenix.org/conference/osdi26/presentation/mao-ziming-uep) | OSDI 2026 | UEP 用 GPU-CPU 控制通道取代 GPU 发起的 RDMA，由 CPU 代理发 GPUDirect RDMA 以 immediate data 模拟保序，在 EFA 上 dispatch/combine 吞吐提升 2.1×、SGLang token 吞吐提升至多 40% |

### Placement, Balance & MoE Serving (11)

专家放置/复制/动态负载均衡与 MoE 服务容量。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2025 | [Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving](https://doi.org/10.1145/3725843.3756043) | MICRO 2025 | 结合 Mono3D DRAM/NMP/GPU 的 Hot/Cold Expert 多级放置，利用主题感知路由管理推理吞吐与 SLO。 |
| 2026 | [AFORE: Attention-FFN Disaggregation with Overlapped Reconfiguration of Experts](https://arxiv.org/abs/2610.03203) | arXiv 2026 (preprint) | 利用 AFD Microbatch 前瞻负载信号，在流水窗口内重配与迁移 Hot Experts。（HOLD_EVIDENCE） |
| 2026 | [BrownoutServe: SLO-Aware Inference Serving Under Bursty Workloads for MoE-Based LLMs](https://doi.org/10.1109/TC.2026.3655019) | IEEE Transactions on Computers 2026 | 采用 United Experts 与受控 Brownout 对 Burst MoE 请求动态调整 Expert 访问和精度/SLO 预算，并公开 Serving Runtime、比较真实 vLLM 吞吐及 SLO Violation。 |
| 2026 | [CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving](https://proceedings.mlsys.org/paper_files/paper/2026/hash/3a7f9e485845dac27423375c934cb4db-Abstract-Conference.html) | MLSys 2026 | CRAFT（MLSys 2026）在给定内存预算下对大规模 MoE 模型做细粒度的逐层专家复制（expert replication），把热门专家复制到多个设备以缓解专家负载不均，从而在不超预算的前提下提升 serving goodput |
| 2026 | [Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement](https://arxiv.org/abs/2607.08782) | arXiv 2026 (preprint) | 预测请求的 Expert 激活并在计算窗口内迁移专家，在线更新分布式 Expert Placement。（HOLD_IDENTITY） |
| 2026 | [Dynamo-MoE: Accelerating Sparse Large Model Inference with Dynamic Parallelization](https://doi.org/10.1145/3806645.3807820) | HPDC 2026 | 针对 MoE 稀疏 Expert 动态激活造成的负载不均，结合 Token Sorting、动态并行和按需 Expert Loading；有正式论文与作者开源实现，大规模实测/模拟比例待全文复核。（HOLD_EVIDENCE） |
| 2026 | [Least-Loaded Expert Parallelism: Load Balancing An Imbalanced Mixture-of-Experts](https://proceedings.mlr.press/v306/nguyen26m.html) | ICML 2026 | 将超载设备的 Token 及关联 Expert 参数动态重路由至闲置设备，减少 Collective Straggler。（HOLD_EVIDENCE） |
| 2026 | [Libra: Effective yet Efficient Load Balancing for Large-scale MoE Inference](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9ff1ac9a659085fed0735362cafe5e53-Abstract-Conference.html) | ICLR 2026 | 预测未来 Expert Activation 并在 MoE Execution Flow 中重排与重叠负载均衡开销；8×H200 上真实大模型 MoE 推理验证，作者代码开源，优先二次核查其吞吐和质量基线。（HOLD_EVIDENCE） |
| 2026 | [MoE-Lens: Towards the Hardware Limit of High-Throughput MoE LLM Serving Under Resource Constraints](https://doi.org/10.1145/3806645.3807594) | HPDC 2026 | CPU/GPU 混合执行结合硬件上界模型推导 Expert Placement/执行策略，实验比较性能模型与真实吞吐。 |
| 2026 | [Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f0552f14388d95b19740dee809f5cad1-Abstract-Conference.html) | ICLR 2026 | 联合安排 Expert Placement 与 DP 请求/TP Token 数据位置，减少 EP All-to-All 跨设备流量。 |
| 2026 | [ViBE: Co-Optimizing Workload Skew and Hardware Variability for MoE Serving](https://arxiv.org/abs/2606.00735) | arXiv 2026 (preprint) | 结合 GPU 性能异构性和 Expert Token Load 做硬件感知 Expert Placement，按负载变化轻量重校准，报告服务 SLO 达标率及 P90 TTFT；不修改模型路由语义。（HOLD_EVIDENCE） |

### Expert Offload & Heterogeneous Execution (18)

权重驻留、CPU/NPU/GPU Offload、Prefetch 与异构执行。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [PowerInfer-2: Fast Large Language Model Inference on a Smartphone](https://arxiv.org/abs/2406.06282) | arXiv 2024 (preprint) | Neural Cluster 级 NPU/CPU 异构执行与分段权重缓存把稀疏 MoE/LLM 部署到内存不足的智能手机。（HOLD_EVIDENCE） |
| 2024 | [SiDA: Sparsity-Inspired Data-Aware Serving for Efficient and Scalable Large Mixture-of-Experts Models](https://proceedings.mlsys.org/paper_files/paper/2024/hash/698cfaf72a208aef2e78bcac55b74328-Abstract-Conference.html) | MLSys 2024 | 利用专家激活稀疏性，在 GPU/主存间数据感知地调度 MoE 权重以提升可部署规模。 |
| 2025 | [Diff-MoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching](https://doi.org/10.1145/3712285.3759903) | SC 2025 | 依据跨请求全局热度和解码局部热度维护分层 GPU Expert Cache，结合预测式 Prefetch 隐藏 CPU–GPU Expert 搬运；报告实机 Batched MoE Inference 评测。 |
| 2025 | [Fiddler: CPU-GPU Orchestration for Fast Inference of Mixture-of-Experts Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8cd1ce03ea58b3d7dfd809e4d42f08ea-Abstract-Conference.html) | ICLR 2025 | 以 CPU-GPU 协同执行减少专家权重搬运和空闲 GPU Stall。 |
| 2025 | [KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models](https://doi.org/10.1145/3731569.3764843) | SOSP 2025 | 针对 MoE 将常驻 Dense/Attention 与部分 Experts 异构放置，结合 CPU 计算优化和流水调度运行大模型。 |
| 2025 | [MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs](https://doi.org/10.1145/3669940.3707267) | ASPLOS 2025 | 面向显存受限设备的 Expert 加载与流水执行，缓解 MoE 权重驻留瓶颈。 |
| 2026 | [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://www.usenix.org/conference/osdi26/presentation/wang-wenxin) | OSDI 2026 | 该 CPU-GPU 混合方案以流式/分布式加载 prefill（1200、1800 tokens/s）、节点内 P/D 分离与双批 overlap（延迟增 <15%、吞吐 +50%）、AVX-512 FP8 GEMV（CPU 延迟降 4–5×）和细粒度 CPU 并行（INT4 DeepSeek-V3 达 28 toke… |
| 2026 | [CommitMoE: Efficient Fallback-Free MoE Inference with Offloading Under GPU Memory Constraints](https://doi.org/10.1609/aaai.v40i27.39454) | AAAI 2026 (full paper) | 对 CPU/GPU MoE Expert Offload 的预测失败避免退回正确 Expert：**Commit Router** 按置信度直接使用预测 Expert，并用异步 CUDA Streams 重叠传输/计算。作者在真实 **RTX 4090 / RTX 2080 Ti**、vLLM 0.7.0 和 MoE-Infinity 对照、DeepSeek-V2-Lite/Qwen-MoE 等模型报告 1.3–9.4× 配置相关速度；**MODEL_CHANGED/APPROXIMATE_QUALITY_CHECKED**，任务质量接近不等于相同输出，在线并发/P95/SLO Goodput 尚无证据。 |
| 2026 | [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](https://arxiv.org/abs/2605.17889) | arXiv 2026 (preprint) | 将 Expert Microbatches 合并为常规 Batch，利用 CPU AMX 与 GPU 同步执行 Expert/Attention，并按热点分层放置专家减少 PCIe 迁移；与 MoE-Lightning、FlexGen 做端到端吞吐对照。（HOLD_EVIDENCE） |
| 2026 | [DoMoE: Domain-Aware Semantic Expert Prediction for Efficient MoE Inference Under Expert Offloading](https://www.ijcai.org/proceedings/2026/657) | IJCAI 2026 (Main Track) | 利用 Domain-specific Expert Routing Table 缩小语义相似度预测范围，在 Expert Offload 下平衡命中率与预测开销；作者报告多模型/负载平均 Throughput 和 Hit Ratio 收益。真实硬件、在线 Tail Latency 和预测误路由造成的模型质量变化仍待 R1。（HOLD_EVIDENCE） |
| 2026 | [Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs (NPUMoE)](https://arxiv.org/abs/2604.18788) | arXiv 2026 (preprint) | 利用静态 Expert Capacity Tiers、Grouped Execution 与 Load-aware Graph Residency 将 MoE Prefill 卸载至 Apple ANE；在真实 M-series 设备评测时延和能耗。（HOLD_EVIDENCE） |
| 2026 | [Efficient MoE Inference on Single Consumer-grade GPU with Dynamic Expert Caching](https://doi.org/10.1109/IPDPS65963.2026.00101) | IPDPS 2026 | 正式全文标题包含 Consumer-grade；在有限显存单卡上协同 Expert Cache、异构卸载与负载均衡，评估大规模 MoE 端到端推理而不是仅模拟不存在的 NPU/PIM。 |
| 2026 | [Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling](https://arxiv.org/abs/2603.27624) | arXiv 2026 (preprint) | FSE-DP 在多 Chiplet 互联上按动态专家轨迹流式分配 MoE 执行并重叠通信。（HOLD_EVIDENCE） |
| 2026 | [FIRM-MoE: Fine-Grained Expert Decomposition for Resource-Adaptive MoE Inference](https://ojs.aaai.org/index.php/AAAI/article/download/39106/43068) | AAAI 2026 (full paper) | GPU 显存不足时将 Expert 的线性子层做 Fine-grained Predictive Prefetch，配合 MoL 预测融合和 Cache-size-aware HEOP 调参；论文在 **RTX 3090 24GB + 32-core CPU PCIe 4.0**、五种 MoE（Qwen/DeepSeek/OLMoE）实测，对比 AP、MI、Fiddler、llama.cpp、ZeRO-style Offload；批大小固定 1，主要报告 50 样本 Mean Decode Latency/Tokens/s（作者报告平均约 1.31× 相对部分基线），未验证在线 P95/Goodput 或作者完整工件。（HOLD_EVIDENCE） |
| 2026 | [LayerScope: Predictive Cross-Layer Scheduling for Efficient Multi-Batch MoE Inference on Legacy Servers](https://doi.org/10.1145/3797905.3807834) | ICS 2026 | PreScope 采用层级 Expert Activation 预测、跨层 Prefetch Scheduling 和异步 CPU–GPU I/O 协调，在普通服务器上隐藏 MoE Expert Offload 延迟；作者报告推理吞吐/延迟实验。 |
| 2026 | [MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading](https://doi.org/10.1145/3779212.3790187) | ASPLOS 2026 | 按 Token/Layer/Sequence 分层管理 Expert 的精度、预取和缓存，减轻显存受限设备的 Expert Loading。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [Taming Latency-Memory Trade-Off in MoE-Based LLM Serving via Fine-Grained Expert Offloading](https://doi.org/10.1145/3767295.3769319) | EuroSys 2026 | FineMoE 从 Prompt 语义及细粒度 Expert 激活模式驱动 Expert 预取、缓存与 CPU Offload，在六 GPU 原型和真实 MoE 工作负载中对照时延及 Cache Hit。 |
| 2026 | [ZipMoE: Efficient On-Device MoE Serving via Lossless Compression and Cache-Affinity Scheduling](https://proceedings.mlr.press/v306/yang26ds.html) | ICML 2026 | 联合无损 Expert 权重压缩、缓存亲和调度与边缘硬件特性，实现低显存 MoE Serving 原型。 |

### Sparse Attention & Conditional Compute (19)

稀疏 Attention、FFN/Neuron 剪枝及选择性计算。

| Year | Paper | Venue | Distinct mechanism |
|---|---|---|---|
| 2024 | [MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5dfbe6f5671e82c76841ba687a8a9ecb-Abstract-Conference.html) | NeurIPS 2024 | 按 Head 动态识别长文本 Attention 稀疏模式并配套高效 Sparse Prefill Kernel。（APPROXIMATE_QUALITY_CHECKED） |
| 2025 | [Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking](https://proceedings.mlsys.org/paper_files/paper/2025/hash/afd6374c7f2839cba22f537f15f4f760-Abstract-Conference.html) | MLSys 2025 | 在移动端按 SwiGLU 输入激活进行预测器无关的剪枝，并根据缓存位置调整 Mask。（APPROXIMATE_QUALITY_CHECKED） |
| 2025 | [Kascade: A Practical Sparse Attention Method for Long-Context LLM Inference](https://arxiv.org/abs/2512.16391) | arXiv 2025 (preprint; NOT MLSys 2026 main proceedings) | 按 Head 在少量 Anchor Layers 求精确 Top-k Attention Index，并在相邻 Reuse Layers 共享；有公开 H100 CUDA Kernel、与 FlashAttention-3 的 Prefill/Decode 基准、LongBench/AIME 精度验证。（APPROXIMATE_QUALITY_CHECKED） |
| 2025 | [LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/cc8c6b9d89f7a898a29f58869b238e46-Abstract-Conference.html) | MLSys 2025 | 统一 Prefill/Decode 的结构化稀疏 Attention，并设计分层 KV Page 选择。（APPROXIMATE_QUALITY_CHECKED） |
| 2025 | [SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/2d04d97593c8c33d415337f408ed0e1b-Abstract-Conference.html) | MLSys 2025 | 按 Head 和输入自适应选取稀疏结构，以 Cumulative Residual Attention 控制稀疏率与精度。（APPROXIMATE_QUALITY_CHECKED） |
| 2025 | [SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference](https://proceedings.mlr.press/v267/zhang25ch.html) | ICML 2025 | 无需重训的训练无关稀疏 Attention，与计算执行策略协同保持效果。（APPROXIMATE_QUALITY_CHECKED） |
| 2025 | [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://proceedings.mlr.press/v267/xu25ag.html) | ICML 2025 | 用 Antidiagonal Scoring 快速识别高价值 Attention Block 并以块稀疏 Kernel 减少 Prefill。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [Attribution-based Sparse Activation in Large Language Models](https://proceedings.mlsys.org/paper_files/paper/2026/hash/29591f355702c3f4436991335784b503-Abstract-Conference.html) | MLSys 2026 | 校正神经元 Attribution 相互依赖，用低贡献神经元跳过减少推理计算；作者报告延迟/内存改善但方法非严格无损。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [Long-Context Modeling with Dynamic Hierarchical Sparse Attention for Memory-Constrained LLM Inference](https://proceedings.mlr.press/v306/xiong26q.html) | ICML 2026 | DHSA 按 Chunk→Token 动态预测 Attention 稀疏性，包含 GPU/CPU Tiled Backend；提供 100K/128K 长上下文推理性能和任务精度，需计入掩码预测成本。（KEEP_ADJACENT） |
| 2026 | [LycheeDecode: Accelerating Long-Context LLM Inference via Hybrid-Head Sparse Decoding](https://arxiv.org/abs/2602.04541) | arXiv 2026 (authors indicate ICLR 2026) | HardKuma 将 Head 划为 Retrieval 和复用其 Top-k 的 Sparse Heads，在 128K Decode 上报告 GPU 加速，并针对 LongBench、RULER、AIME 比较精度。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference](https://doi.org/10.1145/3779212.3790194) | ASPLOS 2026 | 同时重排 FFN Weight 行列实现 Outlier-aware 预测和 Hot/Cold Neuron 分流，在 ReLU LLM 的真实自回归 Decode 中优化稀疏 FFN 算子与端到端性能。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Fine-Grained Expert Merging and Bit-packed Inference](https://proceedings.mlr.press/v306/zhao26ay.html) | ICML 2026 | 细粒度 Element-wise Expert Merging 配合指数字段复用的 Bit-packed 编码，使压缩后 Expert 可以在 GPU 上直接推理；包含实际端到端吞吐/质量权衡。 |
| 2026 | [SALE: Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling](https://proceedings.mlr.press/v306/ji26m.html) | ICML 2026 | 通过低 Bit QK 估计和 Relative Attention Score 产生细粒度稀疏 Mask，定制 CUDA Attention Kernel；GPU 长上下文 Prefill 实测，需计入 Mask 构造开销。（KEEP_ADJACENT） |
| 2026 | [Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference](https://proceedings.mlr.press/v306/le26c.html) | ICML 2026 | Hadamard Sketch 估计 Attention Score，跨 Layer Walk 汇总重要性，并使用可复用的动态稀疏 Kernel 同时处理 Prefill/Decode；Kernel 级收益不能等同完整 Serving Goodput。（KEEP_ADJACENT） |
| 2026 | [SparseInfer: Accelerating Large Language Model Inference with Semantics-Inspired Adaptive Sparse Activation](https://proceedings.mlr.press/v306/wang26hn.html) | ICML 2026 | 基于句子语义预测稀疏神经元的实际 FFN 执行；快速准入（正式出版入口），实机执行、Strong Baseline 与端到端服务指标待二审。（HOLD_EVIDENCE） |
| 2026 | [Stochastic Sparse Attention for Memory-Bound Inference](https://proceedings.mlr.press/v306/lee26j.html) | ICML 2026 | SANTA 采用方差受控的 Softmax 分布采样减少 Value-cache 全量读取，实现 GPU Stratified/Systematic Sampling Attention；有 RTX 6000 Ada Kernel 和端到端 Decode 测量。（KEEP_ADJACENT） |
| 2026 | [Tactic: Adaptive Sparse Attention with Clustering and Distribution Fitting for Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/33f94d79acf71051d6a27f4d8889e20e-Abstract-Conference.html) | ICLR 2026 | 根据累计 Attention Score 占比自适应选择 KV 而非固定 Top-k，以聚类排序/分布拟合减轻筛选开销；评估 Decode Kernel、端到端时延和质量。（APPROXIMATE_QUALITY_CHECKED） |
| 2026 | [Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection](https://proceedings.mlr.press/v306/jo26a.html) | ICML 2026 | 跨 Head/Layer 动态选择 Token 执行 Attention，后续 Layer 可重新考虑此前 Token；与既有 FlashAttention 兼容，作者报告 128K Attention Kernel 和质量对照。（KEEP_ADJACENT） |
| 2026 | [Unified Static–Dynamic Pruning for Efficient LLM Inference](https://doi.org/10.14778/3836663.3836665) | PVLDB 2026 | SPDP 将静态权重与动态激活剪枝映射到 Tiled-CBC 稀疏存储及 Prefill SpMM/Decode SpMspV 专用 GPU Kernel。（APPROXIMATE_QUALITY_CHECKED） |

*Paper links, venue, and mechanism notes are preserved from the prior curation. Inline HOLD/KEEP labels are review notes, not G0–G5 acceptance verdicts. Reported speedups are not independently reproduced.*
