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
| Memory Topology & Virtualization | 222 | 171 | 49 | 2 | KV cache、long-context state、offload、prefix/RAG cache、CXL/分层内存。 |
| Disaggregated Interconnects | 84 | 57 | 18 | 9 | P/D 分离、KV transfer、RDMA/NIXL/UCCL、collective 和跨节点路由。 |
| State Compression & Signal Coding | 126 | 80 | 25 | 21 | 低比特 KV、MLA latent、稀疏/量化/编码压缩与质量-成本权衡。 |
| Execution Compilation & Kernel Fusion | 189 | 83 | 61 | 45 | Triton/CUDA/HIP kernel、attention/GEMM/MoE 算子、编译和硬件后端。 |
| Program-Aware Scheduling | 232 | 183 | 48 | 1 | agent graph、structured generation、多阶段工作流和程序感知调度。 |
| SRE/Fault-Tolerance/Sparing | 38 | 25 | 8 | 5 | trace/benchmark、SLO、故障恢复、漂移、数值稳定性和生产降级。 |

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
| A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs | paper | 2026 | 该工作把长上下文离线推理的数据密集部分下沉到近存储处理器，降低主机内存和 I/O 成本。 | [workload:long-context,rag] |
| A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints | paper | 2026 | 该工作把计算和 KV cache 显存同时纳入排队稳定性分析，给出 LLM inference 系统何时会因内存约束失稳的理论条件。 | [optimization_layer:kv-cache,memory] |
| Accelerating Model Loading in LLM Inference by Programmable Page Cache | paper | 2026 | PPC 提供非侵入可编程 page-cache 策略，MAIO 再以 I/O template、XPU affinity 和局部性优化模型加载。 |  |
| AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving | paper | 2026 | AdaCache 针对 RAG 中高频检索片段做自适应缓存和上下文增强，减少重复处理长输入带来的 prefill 开销。 | [phase:prefill,serving] [workload:agent,rag] |
| Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG | paper | 2026 | 该工作分析 RAG 中非前缀 KV cache 的侧信道风险，展示 agent 辅助攻击可从 vLLM/LMCache 类复用路径恢复敏感上下文。 | [optimization_layer:kv-cache] [workload:agent,rag] [framework_binding:lmcache,vllm] |
| Agentic AI Workload Characteristics | paper | 2026 | 该工作用端到端 tracing 刻画 ReAct 类 agent workload，指出有效上下文缓存会让执行转向 decode-dominated 且依赖长寿命 KV 状态。 | [phase:decode,serving] [workload:agent,rag] |
| AgenticCache: Cache-Driven Asynchronous Planning for Embodied AI Agents | paper | 2026 | AgenticCache 用缓存命中和状态复用驱动 embodied agent 的异步规划，减少重复上下文构造和工具调用等待。 | [phase:serving] [workload:agent,rag] |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | paper | 2026 | Beyond Prediction 用分布感知而非长度预测的调度与 cache-aware preemption 联合优化在线 LLM serving 的 TTFT 和尾延迟。 | [phase:serving] [metrics:ttft] |
| Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes | paper | 2026 | LSP scheduler 只提交最长稳定前缀，把 DLM 的 scattered acceptance 转成连续 KV append 和逐步收缩的 active suffix。 | [optimization_layer:scheduler] |
| Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning | paper | 2026 | 该工作把 KV cache 从单纯加速结构扩展为采样和 reasoning-time reuse 的状态载体，探索更高层次的推理复用。 | [optimization_layer:kv-cache] |
| Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation-Storage Awareness | paper | 2026 | Bidaw 让计算调度感知 KV 加载延迟，并让两级存储利用模型响应预测访问与淘汰，提高多轮会话 KV 命中。 | [phase:serving] [workload:rag] |
| Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving | paper | 2026 | Bifrost 将线性层密文卸载到加速器、把非线性与 KV 状态更新留在 CPU TEE 中，构建 TEE 加 FHE 的混合隐私推理路径。 | [phase:serving] |

### Disaggregated Interconnects

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving | paper | 2026 | 3DLS 用 logic-on-logic 3D chiplet 将 PD 分离中的 KV 传输切到垂直互连、把 decode 侧 TP collective 留在横向 D2D fabric，以隔离混合通信争用。 | [phase:decode,serving] |
| A Lightweight High-Throughput Collective-Capable NoC for Large-Scale ML Accelerators | paper | 2026 | 该工作为大规模 ML accelerator 设计支持 collective 的轻量高吞吐 NoC，针对多核/多芯粒训练和推理通信瓶颈优化片上互连。 | [metrics:throughput] |
| Beyond the Buzz: A Pragmatic Take on Inference Disaggregation | paper | 2026 | 该文系统分析分离式推理在真实规模下的设计空间，指出动态速率匹配和弹性扩缩容对 Pareto 最优性能很关键。 | [workload:rag] |
| CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation | paper | 2026 | CrossPool 面向冷门 MoE 模型服务，把 KV cache 和权重分别做池化/分离管理，降低多模型长尾部署的显存常驻成本。 | [phase:serving] [optimization_layer:kv-cache,moe] [workload:moe] |
| ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving | paper | 2026 | ELDR 根据 prefill expert activation 构建 expert signature，并用 locality-band routing 把请求发往 expert locality 更好的 decode worker，降低 PD 分离式 MoE serving 的 decode 延迟。 | [phase:decode,prefill,routing] [optimization_layer:moe,routing] [workload:moe] |
| Efficient Long-Context Language Model Training by Core Attention Disaggregation | paper | 2026 | 该工作将核心 attention 计算解耦来支撑长上下文训练，减少超长序列训练中的显存、通信和负载不均压力。 | [phase:training] [workload:long-context] |
| Efficient Multi-round LLM Inference over Disaggregated Serving | paper | 2026 | AMPD 面向多轮 agent/RAG 工作流，在 PD 分离式服务中自适应协调增量 prefill 和阶段部署。 | [phase:prefill,serving] [workload:agent,rag] |
| FarSkip-Collectives: Unhobbling Blocking Communication in Mixture of Experts Models | paper | 2026 | FarSkip-Collectives 针对 MoE 阻塞式通信设计可跳过或重排的 collective 路径，减少 expert 并行中的通信等待。 | [optimization_layer:moe] [workload:moe] |
| HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators | paper | 2026 | HMA-Serve 将 GDDR 加速器用于 prefill、HBM GPU 用于 decode，并通过 phase-wise quantization、compute-transfer overlap 和 deferred dequantization 支撑跨厂商异构 PD serving。 | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:memory,quantization] |
| HybridTier: An Adaptive and Lightweight CXL-Memory Tiering System | paper | 2026 | HybridTier 以轻量在线策略在本地 DRAM 与 CXL memory 间迁移热页，为模型权重和 KV 的容量扩展提供通用基础。 | [hardware:cxl] [optimization_layer:memory] |
| ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories | paper | 2026 | ITME 用 CXL 混合远端内存把 TB 级共享上下文层做成字节寻址扩展，并主动分层搬运权重与 prefix cache。 | [hardware:cxl] [optimization_layer:memory] |
| InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models | paper | 2026 | InfiniLoRA 将 LoRA execution 从 base-model inference 解耦，通过共享 LoRA server 和专用 kernel 扩展 MoE/大 rank adapter 服务。 | [phase:serving] [optimization_layer:kernel,moe] [workload:moe] |

### State Compression & Signal Coding

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping | paper | 2026 | ADAngel 为任意精度量化 LLM 自适应映射计算路径，使不同 bit-width 的解码和矩阵运算更好匹配硬件资源。 |  |
| Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | paper | 2026 | SparseSpec 以稀疏注意力版本的同一模型充当 draft，并联合调度 drafting、verification 和动态 KV 管理以加速长 CoT。 | [optimization_layer:kv-cache] |
| Accelerating Speculative Diffusions via Block Verification | paper | 2026 | 该工作把 LLM speculative decoding 的 block verification 扩展到 diffusion 采样，在无需额外训练的前提下提升 draft acceptance 和生成速度。 | [optimization_layer:kv-cache] |
| Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design | paper | 2026 | 该工作用 stream-loading prefill、SmallEP、零拷贝 prefill/decode 分离和 CPU FP8 kernel，把本地 CPU-GPU 平台上的 MoE serving 拉近云端 SLO。 | [phase:decode,prefill,serving] [hardware:gpu] [optimization_layer:kernel,kv-cache,moe] [workload:moe] |
| AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor | paper | 2026 | AnchorKV 在 KV 压缩保留分数中引入 refusal anchor 的软惩罚，使压缩后的长上下文推理兼顾内存节省与安全对齐。 | [optimization_layer:compression,kv-cache] |
| Beat the long tail: Distribution-Aware Speculative Decoding for RL Training | paper | 2026 | DAS 利用历史 rollout 维护非参数 drafter，并按轨迹长度分配 speculative budget，缩短 RL post-training 中长尾生成阶段。 | [phase:training] |
| Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning | paper | 2026 | Bottlenecked Transformer 用轻量 cache processor 周期性重写和整合 KV segments，把推理链中的 latent memory 作为可优化状态。 | [optimization_layer:kv-cache,memory] |
| CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents | paper | 2026 | CacheWise 将 coding agent 的前缀复用与 tool-call 元数据结合做复用感知驱逐和前缀感知调度，显著降低 KV eviction 并缩短会话完成时间。 | [phase:serving] [optimization_layer:kv-cache] [workload:agent] |
| Channel-Aware Mixed-Precision Quantization for Efficient Long-Context Inference | paper | 2026 | ChanMix 按 KV channel 敏感度重新分配低比特预算，并用 Triton kernel 支持 2-bit/FP8 混合精度长上下文推理。 | [optimization_layer:kernel,kv-cache,quantization] [workload:long-context] |
| DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU | paper | 2026 | DFVG 将 draft 放在 FPGA、verify 放在 GPU，以异构流水降低推测解码的草稿成本并提高验证硬件利用率。 | [hardware:gpu] [optimization_layer:kv-cache] |
| Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM | paper | 2026 | Dynamic-dLLM 用动态 cache 更新预算和自适应并行解码阈值，在无需训练的情况下提升 diffusion LLM 长序列推理效率。 | [phase:training] |
| EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts | paper | 2026 | EfficientRollout 为 RL rollout 设计自推测解码和系统感知开关策略，在活跃 batch 缩小时继续利用并行验证加速。 | [optimization_layer:kv-cache] |

### Execution Compilation & Kernel Fusion

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving | paper | 2026 | AGENTSERVESIM 用 program orchestration、tool gap 模拟、session-aware routing 和 KV residency 模型，在 CPU 上逼真评估多轮 agent serving 策略。 | [phase:routing,serving] [optimization_layer:routing] [workload:agent] |
| AXLearn: Modular, Hardware-Agnostic Large Model Training | paper | 2026 | AXLearn 提供模块化、硬件无关的大模型训练框架，统一不同硬件后端上的模型构建、训练和扩展流程。 | [phase:training] |
| AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization | paper | 2026 | AccelOpt 将 LLM agent 用于 AI accelerator kernel 优化闭环，让生成、profile、修复和迭代搜索共同改进算子实现。 | [optimization_layer:kernel] [workload:agent] |
| AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size | paper | 2026 | AdaBlock-dLLM 根据 denoising 过程中的语义置信度动态调整 semi-AR block size，在相同吞吐预算下改善 DLM 解码质量。 |  |
| Agentic Operator Generation for ML ASICs | paper | 2026 | 该工作用 agentic generation 生成和优化 ML ASIC operator，把硬件目标、算子约束和验证反馈纳入自动化代码生成流程。 | [workload:agent] |
| ApproxMLIR: Accuracy-Aware Compiler for Compound ML System | paper | 2026 | ApproxMLIR 把精度影响纳入 compound ML system 编译优化，使近似执行、算子替换和系统性能可以一起权衡。 | [optimization_layer:compiler] |
| Asynchrony and GPUs: Bridging this Dichotomy for I/O with AGIO | paper | 2026 | AGIO 为 GPU 构建真正异步的 I/O 路径，使模型数据和状态传输可以与 kernel 执行重叠。 | [hardware:gpu] [optimization_layer:kernel] |
| Attention Is All You Need for KV Cache in Diffusion LLMs | paper | 2026 | Elastic-Cache 基于 attention-aware drift test 和 layer-aware schedule 选择何时、何处刷新 DLM KV cache，减少 denoising step 间重复计算。 | [optimization_layer:kv-cache] |
| BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal | paper | 2026 | BaseRT 以原生 Metal kernel fusion、unified-memory-aware 优化和自定义 dispatch 逻辑，在 Apple Silicon 上提升 prefill/decode 吞吐并扩大 MoE 模型的本地推理能力。 | [phase:decode,prefill] [optimization_layer:kernel,memory,moe] [workload:moe] |
| CATWILD: Compiler Autotuning for TPU workloads in the Wild | paper | 2026 | CATWILD 面向真实 TPU workload 做 compiler autotuning，降低手工调参成本并改善生产模型在 TPU 上的执行效率。 | [hardware:tpu] [optimization_layer:compiler] |
| CDLM: CONSISTENCY DIFFUSION LANGUAGE MODELS FOR FASTER SAMPLING | paper | 2026 | CDLM 将 consistency/diffusion language model 的采样过程系统化加速，减少扩散式文本生成需要的迭代步数。 |  |
| Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference | paper | 2026 | Concordia 用 JIT 编译的 persistent-kernel checkpointing 降低小 batch LLM 推理的容错快照开销。 | [optimization_layer:kernel] |

### Program-Aware Scheduling

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| A First Look at Bugs in LLM Inference Serving Systems | paper | 2026 | 该工作系统归纳 LLM serving runtime 中的正确性、并发、内存和性能故障模式，为可靠性研究建立问题分类。 | [phase:serving] |
| A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference | paper | 2026 | ST-MoE 利用跨层和跨 token 的 expert 激活相关性做时空联合预取，以重叠 expert 加载和 MoE 推理计算。 | [optimization_layer:moe] [workload:moe] |
| AAFLOW: Scalable Patterns for Agentic AI Workflows | paper | 2026 | AAFLOW 将 agent workflow 建模为算子图，并用 Arrow/Cylon 的零拷贝数据平面与异步批处理降低 embedding、upsert 与 orchestration 开销。 | [phase:serving] [workload:agent,rag] |
| AIRS: Scaling Live Inference in Resource Constrained Environments | paper | 2026 | AIRS 面向资源受限的在线推理流水线动态分配加速器与任务优先级，提高多阶段 LLM 评估/预测服务的吞吐和延迟稳定性。 |  |
| Agentix: An Efficient Serving Engine for LLM Agents as General Programs | paper | 2026 | Agentix 把 agent program 而非单次请求作为调度对象，利用程序依赖和已完成调用对后续 LLM call 抢占与提权。 | [phase:serving] [workload:agent,rag] |
| Attribution-based Sparse Activation in Large Language Models | paper | 2026 | 该工作用 attribution 信号选择性激活 LLM 中的计算路径，为稀疏推理和低成本动态执行提供模型-系统接口。 |  |
| Automated Algorithm Design for Auto-Tuning Optimizers | paper | 2026 | 该工作把算法设计自动化用于 optimizer auto-tuning，减少大模型训练优化器在不同模型和硬件上的手工搜索成本。 |  |
| BAT: Efficient Generative Recommender Serving with Bipartite Attention | paper | 2026 | BAT 为生成式推荐设计 bipartite attention 和相应 serving 路径，减少推荐上下文与生成阶段的冗余计算。 | [phase:serving] |
| BEAM: Joint Resource-Power Optimization for Energy-Efficient LLM Inference under SLO constraints | paper | 2026 | BEAM 联合选择资源分配和功耗状态，在满足 SLO 的同时降低 LLM inference 的能耗。 | [metrics:slo] |
| BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding | paper | 2026 | BLASST 在 online softmax 中按阈值动态跳过低贡献 attention block，减少 Value block 加载和后续矩阵乘法以加速长上下文 prefill/decode。 | [phase:decode,prefill] |
| BOOST: BOttleneck-Optimized Scalable Training Framework for Low-Rank Large Language Models | paper | 2026 | BOOST 针对低秩大语言模型训练识别并优化瓶颈阶段，提高参数高效训练在大模型上的可扩展性。 | [phase:training] |
| BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization | paper | 2026 | BOute 用多目标贝叶斯优化在异构模型和 GPU 组合中选择 serving 配置，联合降低成本并满足质量和延迟目标。 | [phase:serving] [hardware:gpu] |

### SRE/Fault-Tolerance/Sparing

_Showing up to 12 representative records; full detail stays in generated compatibility views and JSONL._

| Title | Type | Year/Channel | Why it matters | Tags |
|---|---|---|---|---|
| ADS: AN AGENTIC DETECTION SYSTEM FOR ENTERPRISE AGENTIC AI SECURITY | paper | 2026 | ADS 面向企业 agentic AI 安全构建检测系统，把 agent 行为、工具调用和安全策略纳入运行时监控。 | [phase:serving] [workload:agent,rag] |
| Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study | paper | 2026 | 该工作在 MI325X 上比较 MLA、GQA、MoE 和多模态模型，说明 AITER、KV offload 与 block size 必须按架构选择。 | [hardware:amd,gpu] [optimization_layer:moe] [workload:moe] |
| Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy | paper | 2026 | 该工作用 GEMM 维度统一重组 LLM pruning 设计空间，比较不同剪枝族在真实内核与硬件上的实际推理加速边界。 | [optimization_layer:kv-cache] |
| Blueprint, Bootstrap, and Bridge: A Security Look at NVIDIA GPU Confidential Computing | paper | 2026 | 该工作系统分析 NVIDIA GPU confidential computing 的安全边界、启动链和桥接机制，为隐私推理与受保护训练部署提供风险视角。 | [hardware:gpu] |
| CSLE: A Reinforcement Learning Platform for Autonomous Security Management | paper | 2026 | CSLE 提供自治安全管理的强化学习平台，可用于评估 AI 基础设施中的自动防御、响应和策略学习。 |  |
| DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems | paper | 2026 | DriftBench 用成体系的 prompt-response 集测量基础设施变化对 LLM serving 输出一致性的影响，并预测高风险变更。 | [phase:serving] |
| Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving | paper | 2026 | Execution-State Capsules 将 agent/physical-AI workflow 的执行状态绑定到图节点，用小批量 checkpoint/restore 降低端侧服务恢复延迟。 | [phase:serving] [workload:agent,rag] [metrics:latency] |
| Fast Cloud Storage for AI Jobs via Grouped I/O API with Transparent Read/Write Optimizations | paper | 2026 | AITURBO 利用加速器互连和 grouped I/O API 自动生成存储层读写计划，覆盖 checkpoint 与 KV-cache I/O。 | [optimization_layer:kv-cache] [workload:rag] |
| GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management | paper | 2026 | GFS 预测 spot instance 风险并进行抢占感知调度，降低 GPU 集群中任务中断和资源浪费。 | [hardware:gpu] |
| GPU Checkpoint/Restore Made Fast and Lightweight | paper | 2026 | GCR 通过控制/数据分离、CPU shadow execution 和 dirty template 降低 GPU checkpoint、restore 与增量快照开销。 | [hardware:gpu] |
| LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | paper | 2026 | LUMEN 把分布式 LLM serving 的故障恢复建模为 checkpoint 放置、请求重分配和 reload 期间容量恢复的联合负载协调问题。 | [phase:serving] |
| MLCommons Chakra: Advancing Performance Benchmarking and Co-design using Standardized Execution Traces | paper | 2026 | Chakra 用标准化 execution traces 支撑 ML 系统 benchmark 和软硬件协同设计，让不同 simulator、runtime 和硬件方案可比较。 |  |
