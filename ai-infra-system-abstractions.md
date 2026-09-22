# AI Infra System Abstractions

<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->

主视图只保留结构、统计和代表条目；公开全量入口见 `papers/README.md` 和 `industry/README.md`，机器事实源见 JSONL。

## Reading Entry Points

| Need | File |
|---|---|
| 按系统抽象快速定位方向 | `ai-infra-system-abstractions.md` |
| 查 verified 学术论文全量明细 | `papers/README.md` |
| 查工业界/开源系统全量明细 | `industry/README.md` |
| 查待处理候选 | `ai-infra-candidates.md` |
| 机器可读论文事实源 | `data/papers.jsonl` |
| 机器可读工业事实源 | `data/industry.jsonl` |
| 候选 staging | `data/candidates.jsonl` |

## Coverage

| System Abstraction | Total | Papers | Industry/Projects | Candidates | Scope |
|---|---:|---:|---:|---:|---|
| Memory Topology & Virtualization | 142 | 96 | 20 | 26 | KV cache、long-context state、offload、prefix/RAG cache、CXL/分层内存。 |
| Disaggregated Interconnects | 203 | 94 | 13 | 96 | P/D 分离、KV transfer、RDMA/NIXL/UCCL、collective 和跨节点路由。 |
| State Compression & Signal Coding | 527 | 251 | 20 | 256 | 低比特 KV、MLA latent、稀疏/量化/编码压缩与质量-成本权衡。 |
| Execution Compilation & Kernel Fusion | 272 | 86 | 18 | 168 | Triton/CUDA/HIP kernel、attention/GEMM/MoE 算子、编译和硬件后端。 |
| Program-Aware Scheduling | 107 | 65 | 13 | 29 | agent graph、structured generation、多阶段工作流和程序感知调度。 |
| SRE/Fault-Tolerance/Sparing | 58 | 20 | 6 | 32 | trace/benchmark、SLO、故障恢复、漂移、数值稳定性和生产降级。 |

## SRE Metrics To Track

| Metric | Meaning |
|---|---|
| TTFT under Drift | 基础设施漂移、广域网抖动、Spot 节点切换时的首 token 延迟恶化边界。 |
| Generation Stall Rate | 推测解码验证失败、MoE all-to-all 热点或 tool-call 挂起造成的生成中断率。 |
| Numerical Reproducibility | 低精度混合量化、scale search 和异构执行导致的数值不稳定与非确定性。 |

## Representative Items

### Memory Topology & Virtualization

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving | paper | 2026 | AdaCache 把缓存感知的部分重计算与自适应检索深度结合用于 RAG serving，在保留生成质量的同时减少长输入的冗余处理。 | [phase:prefill,serving] [hardware:npu] [workload:agent,rag] |
| ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning | paper | 2026 | ArborKV（ICML 2026）利用推理任务本身的树状结构来组织 KV cache，对树中共享前缀做复用、对分支节点有选择地保留与回收，以在分支式（tree-based）LLM 推理中提升显存效率与吞吐。 | [optimization_layer:kv-cache,memory] |
| Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths | paper | 2026 | 该方法为 MoE 设计同时走「HBF 直连 GPU」与「HBF 经 HBM 中转 GPU」两条专家传输路径并并发传输，配合提前专家判定与权重/KV cache 分治，相对仅经 HBM 中转的设计在代表负载上吞吐高 1.94×、端到端加速 1.90×。 | [phase:serving] [hardware:gpu] [optimization_layer:kv-cache,memory,moe] [workload:moe] |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | paper | 2026 | Beyond Prediction 用分布感知而非长度预测的调度与 cache-aware preemption 联合优化在线 LLM serving 的 TTFT 和尾延迟。 | [phase:serving] [metrics:ttft] |
| Decouple and Cache: KV Cache Construction for Streaming Video Understanding | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] [workload:video] |
| DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants | paper | 2026 | DroidSpeak 是首个跨不同 LLM（同架构）复用前缀 KV cache 的分布式推理系统：选择性重算另一模型产生的少数层、复用其余层，并以流水线叠加重算与加载；相较不允许跨模型共享的基线最高提升 4× 吞吐、prefill（TTFT）快约 3.1×，质量损失可忽略。 | [phase:prefill,serving] [hardware:npu] [optimization_layer:kv-cache] [workload:agent,edge,rag] |
| ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs | paper | 2026 | ECHO 为原生稀疏注意力 LLM 设计 KV 卸载服务系统：图友好缓存管理器在 GPU graph 内动态淘汰/召回 KV，并以无损的查询内（decode）与查询间（prefill）预取配合融合 kernel 把召回开销与索引计算重叠；长上下文下生成吞吐比 SGLang/vLLM 高至多 2.1×、轻载延迟相当。 | [phase:serving] [optimization_layer:kv-cache] |
| EpiCache: Episodic KV Cache Management for Long-Term Conversation on Resource-Constrained Environments | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |
| FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure | paper | 2026 | 提出 FailureAtlas 双轴分类法，按故障起源层（网络/传输、流/协议、状态/会话、模型行为、治理/成本）与可检测性（显性/隐性）刻画多供应商 LLM 网关故障，以公开 bug 报告与压测归纳 5 条已验证条目，指出最严重的是返回 HTTP 200 却悄然破坏状态的隐性故障。 | [phase:serving] |
| FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference | paper | 2026 | 以输出 token 为粒度实现可抢占的分布式 LLM serving，提出 skip-join 多级反馈队列，并主动在 GPU/主机内存间搬运中间状态；官方 NSDI 2026 页面报告相对 vLLM 吞吐最高提升 6.1 倍。 | [phase:serving] [hardware:gpu,npu,tpu] [optimization_layer:compiler,kernel,memory] [workload:agent,edge,rag] |
| FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management | paper | 2026 | FlexiCache 利用 attention head 重要性的时间稳定性动态管理 KV cache，减少长上下文生成中不必要的保留和加载。 | [optimization_layer:compression,kv-cache] [workload:rag] |
| ForesightKV: Optimizing KV Cache Eviction for Reasoning Models by Learning Long-Term Contribution | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [optimization_layer:kv-cache] |

### Disaggregated Interconnects

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| A Photonic-CXL Memory Appliance for Scalable KV Cache Management in LLM Inference | paper | 2026 | Marvell 光子-CXL 内存设备用无源光纤取代电交换，经无交换机全交叉拓扑在 16 主机间提供 32TB 共享内存；时延较电 CXL 池降逾 50%，多轮对话 TTFT 提升 6.6x。 | [hardware:cxl,gpu] [optimization_layer:kv-cache,memory] [workload:long-context] [metrics:latency] |
| ARKV: Adaptive Resource-Efficient KV Cache Management for Long Context LLM Inference under Memory Constraints | paper | 2026 | CCGrid 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache,memory] [workload:edge,long-context] |
| BYSTANDER: State-Aware Execution-Time Prediction for Heterogeneous LLM Inference Scheduling | paper | 2026 | IEEE CLOUD 2026 official conference program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,rag] |
| Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling | paper | 2026 | DOPS 是硬件感知的闭环框架，用阶段感知 DAG 联合优化算子调度与分块权重布局：Bifocal 调度器做算子到设备的动态放置，Weight Layout Arbiter 在严格内存约束下选高效权重布局；在 NPU+PIM 异构系统上 Bifocal 比 PD 基线几何均值快 1.20×–2.23×，WLA 再叠加 1.28×–1.33×。 | [phase:decode,prefill,serving] [hardware:npu] [optimization_layer:memory,scheduler] [workload:edge] |
| CRISP: Co-designing Pruning and Scheduling for Efficient MoE Inference on Edge Servers | paper | 2026 | MobiCom 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel,moe] [workload:edge,moe] |
| Calibrate, Then Route: A Measured Study of Learned Request Routing for Disaggregated LLM Serving | paper | 2026 | 该「先标定再路由」的学习式路由器用精确提示长度、预测输出长度、KV cache 压力与 SLO 类别估计各实例的附加完成时间，在 8 张 A40 上以 NIXL 跨池搬运 KV，平均 goodput 达 0.864（高于轮询/最闲的 0.835–0.847），且用 6 卡即可匹配轮询 7 卡的 goodput。 | [phase:decode,prefill,routing] [hardware:gpu,tpu] [optimization_layer:compiler,kernel,kv-cache] [framework_binding:vllm] |
| Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding | paper | 2026 | Cassandra 面向边端设备，以自投机解码（self-speculative decoding）使推理型 LLM 在资源受限环境下高效运行，无需额外草稿模型即可在端侧完成推理，成果发表于 ISCA 2026。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving | paper | 2026 | ConServe 面向多轮对话 LLM 服务，以保留连续性的内存管理策略组织 KV cache 与各轮上下文，减少碎片化并提升多轮场景下的显存利用率，发表于 ISCA 2026。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Connex: Endpoint Mobility Primitives for Dynamic LLM Serving | paper | 2026 | ACM SIGCOMM 2026 accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel] |
| DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture | paper | 2026 | DIAMoND（ISCA 2026）提出面向边缘 MoE 的动态推理架构，结合异构的 In-NAND 与 Near-DRAM 计算以适配边缘设备上的 MoE 推理，具体方法与结果未在摘要中给出。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| DoMoE: Domain-Aware Semantic Expert Prediction for Efficient MoE Inference Under Expert Offloading | paper | 2026 | IJCAI-ECAI 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compression,moe] [workload:agent,edge,moe] |
| Dynamo-MoE: Accelerating Sparse Large Model Inference | paper | 2026 | HPDC 2026 official program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |

### State Compression & Signal Coding

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs | paper | 2026 | JoLT（Joint Lagrangian Tucker）对 KV cache 做部分 Tucker 分解只压 token 与 feature 轴、保留 head/layer 轴，再用旋转低比特残差补回被截断的能量，由单一拉格朗日对偶在字节预算下联合分配秩与位宽，实现近无损 2×–3× 压缩，其 FlashJoLT 变体压缩耗时再快 5×–13×。 | [optimization_layer:compiler,compression,kernel] [workload:long-context] [metrics:throughput] |
| A Sparse Glimpse of the Whole: Train-Free Self-Speculative Decoding | paper | 2026 | SparseSpec-L 是免训练自推测解码框架，用动态稀疏可召回 KV cache 从目标直接生成轻量 draft，复用验证时 per-head attention 统计量作重要性信号，并以熵控制器选推测长度；多长上下文任务上一致加速且保分布。 | [phase:serving,training] [hardware:tpu] [optimization_layer:compiler,compression,kernel] [workload:long-context] |
| ACCEPTANCE-GUIDED ADAPTIVE SPECULATIVE DECODING FOR EFFICIENT LARGE LANGUAGE MODEL INFERENCE | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,edge,multimodal] |
| ADAPTIVE ERASURE CODING FOR FAULT-TOLERANT LLM SERVING WITH CONTINUOUS BATCHING | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] |
| ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping | paper | 2026 | ADAngel 基于 DPR（分解-部分积-重构）计算模型为任意精度量化（如 W4A8）的 mpGEMM 生成多样化 kernel，并用 Oracle 策略图让轻量分发器按负载选最优 kernel，decode 吞吐比 llama.cpp 最高快 5.10×、prefill 的 TTFT 比 TensorRT-LLM 快 1.17×–2.38×。 | [phase:prefill,decode,serving] [hardware:gpu] [optimization_layer:compiler,compression,kernel] [framework_binding:tensorrt-llm] |
| ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference | paper | 2026 | COLM 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,long-context,rag] |
| AUM: Unleashing the Efficiency Potential of Shared Processors with Accelerator Units for LLM Serving | paper | 2026 | HPCA 2026 official detailed program 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:edge,moe] |
| Accelerating Speculative Decoding with Block Diffusion Draft Trees | paper | 2026 | COLM 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,compression,kernel] [workload:agent,rag] |
| Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design | paper | 2026 | 该 CPU-GPU 混合方案以流式/分布式加载 prefill（1200、1800 tokens/s）、节点内 P/D 分离与双批 overlap（延迟增 <15%、吞吐 +50%）、AVX-512 FP8 GEMV（CPU 延迟降 4–5×）和细粒度 CPU 并行（INT4 DeepSeek-V3 达 28 tokens/s）在消费级平台达成云级 SLO。 | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:kernel,kv-cache,moe] [workload:moe] |
| AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters | paper | 2026 | AdaFlash 针对 diffusion drafter 的双向注意力方差问题，用 reverse-KL 的在线策略蒸馏（OPD）稳定域级方差，并以自适应长度头动态调节候选序列长度来压低目标模型验证开销，高并发下吞吐比此前最佳高约 66%。 | [optimization_layer:compiler,kernel] [workload:agent,edge,rag] [metrics:throughput] |
| AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [metrics:slo] |
| AdaSpec: Adaptive Multilingual Speculative Decoding with Self-Synthesized Language-Aware Training and Vocabulary Simplification | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving,training] [workload:agent,edge,multimodal] |

### Execution Compilation & Kernel Fusion

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference | paper | 2026 | APEX 用轻量预取路由器在 attention 前预测候选专家并提前取回以重叠专家加载与计算，提供正确性保持与零停顿两模式，前者把每 token 延迟降至多 26%、EDP 降至多 41%。 | [phase:routing,serving] [optimization_layer:compiler,kernel,memory] [workload:edge,moe] [metrics:latency,stall] |
| AccKV: Towards Efficient Audio-Video LLMs Inference via Adaptive-Focusing and Cross-Calibration KV Cache Optimization | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] |
| Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,edge,multimodal] [metrics:throughput] |
| Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference | paper | 2026 | 该研究诊断基于 attention 的 KV 淘汰在嵌套 JSON 上的角色偏差（KEY 被过度保留致 5% 预算下准确率从 88% 跌至 0%），提出免重训练的角色条件分配填补 H2O 差距 63–98%。 | [phase:training] [hardware:npu] [optimization_layer:compiler,kernel,kv-cache] [workload:edge,long-context] |
| Adaptive KV Retention for LLM Agents at Human-Approval Timescales | paper | 2026 | 面向等待人工批准的 agentic 请求，该分层 KV 保留控制器围绕 GPU 机会成本在无限期保留与按负载过期间选择，把活跃请求 goodput 相比 vLLM 提升 23–51%、相比 Continuum 提升 41–52%。 | [phase:serving] [hardware:gpu] [optimization_layer:memory] [workload:agent,rag] |
| AgentKV: Phase-Aware KV Eviction for Agentic LLMs | paper | 2026 | AgentKV 针对智能体生成跨 think/act/tool 等多相、未来查询不似近邻的问题，为每个相位维护小型查询缓冲并按其并集给缓存 key 打分，在多轮持久路径中跨轮携带压缩 KV；相较完整 KV 的 SGLang 输出 token 吞吐最高提升 1.80×，任务分比 R-KV 高 5.5 点。 | [phase:decode,serving] [hardware:tpu] [optimization_layer:compiler,kernel,kv-cache] [workload:agent,rag] |
| Auto-Scaling Heterogeneous Neural Processing Units for Energy and Cost-Efficient LLM Serving | paper | 2026 | NeuScale 用 vPod 抽象封装不同代次 NPU 的核心参数，以轻量 roofline 分析为各类推理请求分配最适配的 vPod，并支持细粒度动态扩缩，借异构 NPU 最优利用提升成本效率与 SLO 满足率。 | [phase:serving] [hardware:npu] [workload:edge] [metrics:slo] |
| AutoTuneBench: Trustworthy Measurement for Agent Auto-Tuning of LLM Serving Engines | paper | 2026 | AutoTuneBench 把 agent 调优测量的信任做成架构属性：代码冻结溯源、越界结果拒绝、反作弊在修改面外、5% 跨跑变异上限，显示最佳 kernel 相对诚实基线仅 2.03× 而非朴素 10.6×。 | [phase:serving] [hardware:gpu] [optimization_layer:compiler,kernel] [workload:agent] |
| Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices | paper | 2026 | ATSInfer 在消费设备（权重超显存需卸载）上以张量粒度做 CPU-GPU 混合卸载，结合静态放置与负载感知动态传输及异步协调，把 prefill 吞吐提升至多 1.94×、decode 至多 3.29×。 | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:memory,moe] [workload:agent,moe,rag] |
| COMPRESSING KV CACHE FOR LONG-CONTEXT LLM INFERENCE WITH INTER-LAYER ATTENTION SIMILARITY | paper | 2026 | ICASSP 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:compiler,kernel,kv-cache] [workload:agent,edge,long-context] |
| CasMoE: A Cascaded Framework for Efficient MoE Inference on Resource-constrained Devices | paper | 2026 | AAAI 2026 DBLP proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [optimization_layer:moe] [workload:agent,edge,moe] |
| Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving | paper | 2026 | Cascade 以「请求延迟预算」（SLO 减去预测剩余服务时间）统一协调调度与跨内存层级的 KV cache 管理：优先处理预算吃紧的请求，并按预算决定非驻留 KV 的复原/预取/保留/重算，相对 vLLM 默认 FCFS 的 goodput 最高提升 2.4×、SLO 违规降 40%。 | [phase:serving] [hardware:npu] [optimization_layer:kv-cache,memory,scheduler] [workload:agent,edge,rag] |

### Program-Aware Scheduling

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving | paper | 2026 | 根据 prefill/decode 长度分类请求，逐步优化实例间 compute layout、负载平衡和选择性分布式执行，并用仿真估计器避免实际执行开销；基于生产工作负载评测，报告 SLO attainment 最高提升 3.6 倍、成本效率提升 2 倍。 | [phase:decode,prefill,serving] [optimization_layer:scheduler] [metrics:latency,slo] |
| Agentix: An Efficient Serving Engine for LLM Agents as General Programs | paper | 2026 | 把 agent 程序及其依赖的 LLM calls 作为 serving 调度的一等对象，利用已完成调用的程序级上下文进行抢占和优先级调度；官方 NSDI 2026 页面报告在相同延迟下，相比 vLLM 等系统程序吞吐提升 4–15 倍。 | [phase:serving] [hardware:tpu] [optimization_layer:compiler,kernel,scheduler] [workload:agent,rag] |
| BatchGen: An Architecture for Scalable and Efficient Batch Inference | paper | 2026 | BatchGen 以「序列协程」计算模型把每条序列表示为细粒度事件驱动协程，让运行时动态重组工作（更大专家级 batch、缓解掉队、跨设备重分配），在 128-GPU 集群上把批完成时间最多缩短 2.3×，在内存受限加速器上比最强卸载基线快至多 9.6×。 | [phase:serving] [hardware:gpu] [optimization_layer:scheduler,memory,moe] [workload:moe,heterogeneous] |
| Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration | paper | 2026 | Bullet 在空间放置和时间调度两个维度动态编排 LLM 请求，以减少 GPU 碎片并提高服务利用率。 | [phase:serving] [hardware:gpu] |
| CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving | paper | 2026 | CRAFT（MLSys 2026）在给定内存预算下对大规模 MoE 模型做细粒度的逐层专家复制（expert replication），把热门专家复制到多个设备以缓解专家负载不均，从而在不超预算的前提下提升 serving goodput。 | [phase:serving] [optimization_layer:memory,moe] [workload:moe] [metrics:goodput] |
| DecodeShare: Tracing the Shared Pathways of LLM Decode-Time Decisions | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,serving] |
| DuetServe: Harmonizing Prefill and Decode for LLM Serving via Adaptive GPU Multiplexing | paper | 2026 | ICML 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:decode,prefill,serving] [hardware:gpu] |
| Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration | paper | 2026 | EcoServe 面向商品 GPU 集群提出「部分分离」（PaDG）策略：在单实例内沿时间维分离 prefill/decode 以缓解干扰，并循环激活多实例保证 prefill 连续可用；配合自适应路由与有丝分裂式扩缩，在 32-GPU L20 以太网集群上 goodput 比 vLLM/Sarathi/DistServe/MoonCake 高 1.96×–2.51×。 | [phase:serving] [hardware:gpu] [metrics:goodput] |
| FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap | paper | 2026 | FlashAgents 用 agent 间 token streaming、增量 prefill 和 prefix-aware coordination 重叠多智能体调用链中的等待与计算。 | [phase:prefill,serving] [workload:agent,rag] |
| FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters | paper | 2026 | EuroSys 2026 official accepted papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill | paper | 2026 | MLSys 2026 official virtual papers 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:prefill,serving] [optimization_layer:moe] [workload:moe] [metrics:stall] |
| HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving | paper | 2026 | HELIOS 在线选择模型和 early-exit 层数，只加载满足任务目标所需的层，从而在质量约束下提高吞吐和能效。 | [phase:serving] |

### SRE/Fault-Tolerance/Sparing

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| Beyond Binary Priorities: Multi-Tier SLA Scheduling for Large Language Model Serving | paper | 2026 | 把 Llumnix 的二级优先级模型扩展为任意层级，在 Vidur 中以指数衰减的分层余量与层级感知派单实现细粒度 SLA 调度；四个优先级层最优，prefill 均值比 INFaaS 最高快 8.3×、P99 端到端最高快 3.1×、单位延迟成本降 46%–68%，并在 10 层时仍不出现尾延迟崩溃。 | [phase:prefill,routing,serving] [optimization_layer:routing,scheduler] [workload:agent,rag] [framework_binding:vllm] |
| DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems | paper | 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。 | [phase:serving] |
| ETCInfer: An Energy-efficient Thermal-aware Cooling-joint Scheduler for LLM Inference in AI Datacenters | paper | 2026 | ETCInfer 把 GPU 推理与机房制冷作为联合控制问题，用物理信息模型选定 CRAC 设定值并自适应调节每 GPU 频率与 micro-batch size（建模为 POMDP 由 ETCAdapter 学习控制），在环境温度高达 48°C 时把任务总能耗最多降 33.1%、热节流暴露最多降 92.9%，SLO 违规率低于 0.7%。 | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:scheduler] [metrics:latency,slo] |
| GAPS: Global-Aware Prediction-driven Scheduling for Large-Scale LLM Inference | paper | 2026 | AAMAS 2026 official proceedings 官方页面条目；发现源未提供摘要，需进一步核对正文。 | [phase:serving] [workload:agent,rag] |
| GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving | paper | 2026 | GhostServe 在 host memory 中以 erasure coding 为 streaming KV cache 生成 parity shards，故障时重建丢失 KV 状态并继续推理，避免完整重算或全量状态复制；单 batch checkpoint latency 最高降低 2.7x，recovery latency 降低 2.1x，中位响应延迟降低 1.2x。 | [phase:serving,decode] [hardware:gpu] [optimization_layer:compression,kv-cache,memory] [workload:long-context,agent] |
| HBF Sucks! A Full-Stack Characterization of High-Bandwidth Flash for KV-Centric LLM Serving | paper | 2026 | 该全栈测评把 HBF（高带宽闪存）当作 SSD 式 KV 卸载底层却适得其反：H100/B200 上端到端延迟升 2×–5.5×、峰值 SLO goodput 降 1.1×–2.7×，因瞬时 KV 写多于读且触发热限；结论指 HBF 仅在复用感知放置、写预算与热协同下才适合 LLM serving。 | [phase:serving] [hardware:gpu] [optimization_layer:moe] [workload:agent,moe,rag] |
| Heterogeneity at Hyperscale: Characterization and Scheduling of Large Production AI Clusters at Alibaba | paper | 2026 | 基于对阿里 ASI 超大规模生产集群（六个月 trace、跨厂商 155,410 张 GPU、81 个部门任务）的刻画，该工作指高需求并未带来高有效利用率，并提出实用 GPU 碎片整理（含松弛资源节点减 20.2%）与考虑抢占成本的 SpotGPU 调度，把 GPU 分配率从 68% 提至 93%。 | [phase:training] [hardware:gpu] [workload:rag] |
| Probe-and-Fetch: Dynamic KV Cache Pruning for Accelerated Long-Context Inference in Web-Scale AI Search | paper | 2026 | Probe-and-Fetch（The Web Conference 2026 industry，百度等）提出动态 KV cache 剪枝方法，用于网页级 AI 搜索中的长上下文推理加速，以「先探测再取回」的方式在剪枝后保住关键上下文；具体方法与结果未在摘要中给出。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent,long-context,rag] |
| Safeguarding LLM Training at Scale: Online SDC Detection and Insights from 35 Million GPU Hours | paper | 2026 | AEGIS 用 cSensor-cVerifier 两级抽象做大规模 LLM 训练在线静默数据错误检测，在 3500 万 GPU 小时内部署中以 0.86% 开销识别 18 起 SDC 事件与 13 块故障 GPU。 | [phase:training] [hardware:gpu] |
| Stage-Replay Divergence Follows the KV Cache: Fixed-Prefix Precision Controls and Bidirectional Cache Transplantation | paper | 2026 | 该文在 Qwen2.5 衍生系统阶段边界审计 stage-replay 假设，200 项实验显示 BF16 下留存缓存与一次性 prefill 在 166 后缀与 20 标签分歧，FP32 无分歧；对 48 层双向移植使分歧续写全跟随缓存供体。 | [phase:decode,prefill,serving] [optimization_layer:kv-cache] [workload:edge] |
| TensorCast: The Missing Tensor Management Layer in Large Language Model Infrastructure | paper | 2026 | TensorCast 把张量生命周期管理抽象为 Tensor-as-a-Service，解耦状态管理与计算并提供可编程生命周期原语与分离策略/执行的运行时，多轮 agent 负载下 TTFT 降低至多 93.2%。 | [phase:routing] [optimization_layer:kv-cache,routing] [workload:agent,rag] [framework_binding:sglang,vllm] |
| The Illusion of Local Privacy: Confidentiality Boundary Failures in Consumer LLM Serving Systems | paper | 2026 | 该文以 LLAnalyzer 测量消费级本地 LLM serving 在模型加载、运行时内存、封装持久化与 serving 接口这四道边界的提示泄露，发现明文残留在分配器内存中、封装延长提示寿命，并披露 llama.cpp 一处可被 200/200 次复现的越权恢复会话缺陷。 | [phase:serving] [optimization_layer:memory] [workload:agent,rag] |
