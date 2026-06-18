# Paper List（按主题与核验批次整理；会议栏为最新发表/审稿状态）

核验口径：正式录用状态优先采用会议官方 program/proceedings；预印本采用 arXiv 当前版本；无法从公开稿可靠确认的作者单位明确标注为“官方目录/公开稿未列单位”，不根据作者姓名猜测。

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Splitwise: Efficient Generative LLM Inference Using Phase Splitting | ISCA 2024 | University of Washington; Microsoft | Splitwise 将 prompt computation 与 token generation 部署到不同机器池，在吞吐、成本和功耗之间做阶段化资源优化。 |
| DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving | OSDI 2024 | Peking University; StepFun; UC San Diego | DistServe 将 prefill 和 decode 放到不同 GPU 上，并按 TTFT/TPOT 约束联合优化资源与并行策略。 |
| Inference without Interference: Disaggregate LLM Inference for Mixed Downstream Workloads | arXiv 预印本, 2024 | University of Chinese Academy of Sciences; ICT, CAS; Huawei Cloud | TetriInfer 通过请求分组、prefill/decode 分离和两级调度降低混合下游任务之间的推理干扰。 |
| DejaVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving | ICML 2024 | ETH Zurich; Carnegie Mellon University; Microsoft Research | DejaVu 用 KV-cache streaming 支持 prompt-token 分离、microbatch swapping 和状态复制，缓解流水线空泡、显存过配和故障恢复问题。 |
| CacheBlend: Fast Large Language Model Serving for RAG with Cached Knowledge Fusion | EuroSys 2025 | CUHK Shenzhen; University of Chicago; Stanford University; Microsoft Research | CacheBlend 复用非前缀知识片段的预计算 KV，并用知识融合机制降低 RAG prefill 延迟。 |
| Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | FAST 2025 | Moonshot AI; Tsinghua University | Mooncake 以 KVCache 为中心构建分离式 LLM serving 架构，利用 CPU/DRAM/SSD/NIC 资源扩展在线长上下文服务能力。 |
| P/D-Serve: Serving Disaggregated Large Language Model at Scale | arXiv 预印本, 2024 | Huawei Technologies Co., Ltd. | P/D-Serve 面向大规模商业部署，将 prefill/decode 组织、调度和 KVCache 传输做端到端优化，以提升分离式 LLM 服务吞吐和 SLO 表现。 |
| POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference | ASPLOS 2025 | University of Washington; Microsoft Research | POD-Attention 设计可同时处理 prefill/decode 混合批的 GPU attention kernel，提升两阶段重叠执行效率。 |
| ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | ICML 2025 Spotlight | ByteDance Seed; Carnegie Mellon University | ShadowKV 在 GPU 侧保留低秩 keys、landmarks 和少量 outliers，并按需从 CPU DRAM 拉取匹配 value 以提升长上下文吞吐。 |
| RefreshKV: Updating Small KV Cache During Long-form Generation | ACL 2025 Long Papers | New York University; Cornell University | RefreshKV 在长文本生成中交替执行全量注意力和小 KV cache 注意力，动态刷新保留 token 以改善长生成质量。 |
| Cache-Craft: Managing Chunk-Caches for Efficient Retrieval-Augmented Generation | PACMMOD / SIGMOD 2025 | Adobe Research; IIT Bombay; IIT Kanpur | Cache-Craft 管理 RAG 中可复用的 chunk KV cache，并通过少量重计算修正位置影响以减少重复 prefill。 |
| HexGen-2: Disaggregated Generative Inference of LLMs in Heterogeneous Environment | ICLR 2025 | The Hong Kong University of Science and Technology | HexGen-2 在异构 GPU 集群上联合优化资源分配、并行策略和跨阶段 KV 传输以降低成本。 |
| RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression | ICML 2025 | NVIDIA; Georgia Institute of Technology | RocketKV 先粗粒度永久淘汰输入 KV token，再用动态稀疏注意力进行细粒度 top-k 选择以加速长上下文解码。 |
| FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling | arXiv 预印本, 2025 | Alibaba Cloud Computing | FlowKV 优化块级 KV cache 传输并引入负载感知调度，降低 prefill 到 decode 的传输延迟和节点不均衡。 |
| Towards High-Goodput LLM Serving with Prefill-decode Multiplexing | ASPLOS 2026 | Shanghai Jiao Tong University; National University of Singapore | MuxWise 在单 GPU 内对 prefill/decode 进行多路复用，并结合估计器和 SLO 调度提升 goodput。 |
| semi-PD: Towards Efficient LLM Serving via Phase-Wise Disaggregated Computation and Unified Storage | arXiv 预印本, 2025 | Tsinghua University; Infinigence-AI; Shanghai Jiao Tong University | semi-PD 在 SM 级别分离 prefill/decode 计算但统一显存管理，减少完全 PD 分离带来的存储浪费和迁移开销。 |
| TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate | ICLR 2026 | Google Research; New York University; Google DeepMind | TurboQuant 通过随机旋转、近最优标量量化和 QJL 残差校正，实现面向 KV cache 的在线低比特向量量化。 |
| PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | ICLR 2026 Poster | Tsinghua University; Infinigence-AI; Columbia University; OPPO AI Center; Shanghai Jiao Tong University | PM-KVQ 采用渐进式混合精度量化和长位置分布校准，降低长 CoT 推理中 KV cache 量化的累积误差。 |
| Beyond the Buzz: A Pragmatic Take on Inference Disaggregation | MLSys 2026 | NVIDIA Corporation | 该文系统分析分离式推理在真实规模下的设计空间，指出动态速率匹配和弹性扩缩容对 Pareto 最优性能很关键。 |
| SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference | NeurIPS 2025 | Shanghai Jiao Tong University; Fudan University; Nanjing University; Wuhan University; University of Goettingen | SmallKV 用小模型注意力补偿大模型 KV 压缩中的显著性漂移和边际信息过压缩。 |
| SparseCache: Extreme Sparse Coding for KV Cache Compression | ICLR 2026 withdrawn submission | Dnotitia; Hanyang University | SparseCache 通过跨层共享 Key/Value 字典和稀疏编码压缩预计算 RAG 的 KV cache，降低存储和加载压力。 |
| PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference | ACL ARR 2026 January submission / ICLR 2026 withdrawn submission | Beijing Academy of Artificial Intelligence (BAAI) | PDTrim 针对 prefill 与 decode 阶段的不同敏感性分别搜索剪枝块，使模型剪枝更适配 PD 分离式推理部署。 |
| Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM | TMLR under review / ICLR 2026 withdrawn submission | RBC Borealis | K-VEC 用跨头和跨层覆盖度模块提升被保留 token 的多样性，缓解低覆盖带来的长上下文性能下降。 |
| ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | ICLR 2026 Oral | Georgia Institute of Technology; NVIDIA Research | ThinKV 根据 CoT 中不同 thought 类型的重要性进行自适应量化和逐级淘汰，并用扩展 PagedAttention kernel 复用释放页。 |
| SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference | arXiv 预印本, 2025 | Princeton University; University of Washington | SPAD 分别设计面向 prefill 和 decode 的专用芯片，以更低硬件成本匹配两阶段不同的算力和带宽需求。 |
| Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | ICML 2026 | Westlake University; McGill University; Mila; Zhejiang University; MBZUAI | RLKV 用强化学习探针识别对推理链关键的注意力头，并优先保留这些头的 KV cache 来压缩长 CoT 推理开销。 |
| KV Cache Transform Coding for Compact Storage in LLM Inference | ICLR 2026 | NVIDIA; University of Warsaw | KVTC 借鉴媒体压缩，用 PCA 去相关、自适应量化和熵编码压缩可复用 KV cache。 |
| Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs | ICLR 2026 | Yale University; JPMorganChase AI Research | TRIM-KV 在 token 生成时预测长期保留价值，并随时间衰减以在固定内存预算下保留最有用的 KV。 |
| EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving | arXiv 预印本, 2025 | University of Chicago; UC Berkeley; Tensormesh; MIT; UC Santa Cruz; Stanford; Microsoft | EVICPRESS 联合优化 KV cache 的有损压缩和多层存储淘汰，在质量和延迟之间做全局权衡。 |
| Efficient Multi-round LLM Inference over Disaggregated Serving | arXiv 预印本, 2026 | Southeast University; University of Cambridge; Peking University; Ant Group; Shanghai Jiao Tong University | AMPD 面向多轮 agent/RAG 工作流，在 PD 分离式服务中自适应协调增量 prefill 和阶段部署。 |
| LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation | ICLR 2026 Poster | Samsung Research | LookaheadKV 用轻量 lookahead tokens 和 LoRA 模块预测未来注意力分布，在无需草稿生成的情况下指导 KV 淘汰。 |

## 2026-06-02 追加：KV 状态管理与分离式推理系统

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference | MLSys 2026 | University of Chicago; Microsoft; Google; IBM/Red Hat 等 | LMCache 将 KV cache 抽象为独立可复用层，支持跨请求、跨 engine、跨存储层的 KV offload、传输和复用。 |
| RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference | PVLDB 19(5), 2026 | Microsoft Research; Peking University; Moonshot AI 等 | RetroInfer 把 KV cache 看作向量存储系统，用 attention-aware index 和 GPU-CPU buffer manager 支撑百万 token 级稀疏召回。 |
| DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants | NSDI 2026 | University of Chicago; Microsoft Research; UC Berkeley 等 | DroidSpeak 在同架构微调模型之间选择性共享 KV cache，并重算少量关键层以降低多模型 agent 工作流的重复 prefill。 |
| SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems | NSDI 2026 | Adobe Research; University of Chicago; Microsoft Research 等 | SYMPHONY 将计算和 KV cache 存储解耦为 disaggregated memory management layer，以满足多轮会话状态的低延迟访问。 |
| KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving | SIGCOMM 2026 | 作者公开稿未列单位 | KVServe 用 Bayesian profiling 建立压缩策略 Pareto 集，并由在线 controller 按 workload、网络、SLO 和质量约束选择 KV 传输压缩方案。 |
| Medha: Efficient LLM Inference on Multi-Million Context Lengths Without Approximation | arXiv 预印本, 2025 | Microsoft Research; Carnegie Mellon University; University of Washington 等 | Medha 通过 adaptive prefill chunking、sequence pipeline parallelism 和 KV-cache parallelism 支撑千万 token 级精确长上下文推理。 |
| SPIN: Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving | arXiv 预印本, 2026 | Microsoft Research; University of Virginia 等 | SPIN 用统一 page-based partition、locality-aware KV manager 和分层元数据把 sparse attention 与 CPU/GPU 分层 KV 存储协同起来。 |
| KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning | arXiv 预印本, 2026 | Microsoft Research; Peking University 等 | KEEP 面向 embodied planning，将静态/动态记忆分组、multi-hop 重算和分层加载结合，减少长程记忆 prompt 的重复 prefill。 |
| Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Tutti 构建 GPU-centric KV object store、GPU io_uring 和 slack-aware I/O 调度，使 SSD-backed KV 恢复绕开 CPU 控制瓶颈。 |
| SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving | arXiv 预印本, 2026 | Apple; University of Michigan 等 | SAW-INT4 面向真实 serving 约束设计 4-bit KV quantization，强调 paged layout、规则访存和 fused attention 可落地性。 |
| TraCT: Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale | arXiv 预印本, 2025 | University/industry collaboration | TraCT 用 CXL shared memory 同时作为 KV transfer substrate 和 rack-wide prefix-aware KV cache，探索机架级 KV cache 共享。 |
| CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving | arXiv 预印本, 2025 | Academic/industry collaboration | CXL-SpecKV 将 KV cache offload 到远端 FPGA/CXL memory，并用 speculative prefetch 与压缩/解压引擎降低带宽压力。 |

## 2026-06-11 追加：推理系统广域扩展

### Runtime、调度与弹性服务

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SGLang: Efficient Execution of Structured Language Model Programs | NeurIPS 2024 | Stanford University; UC Berkeley; Shanghai Jiao Tong University; Texas A&M University | SGLang 用 RadixAttention、结构化生成语言和高性能 runtime 统一优化多调用、共享前缀和约束生成工作流。 |
| Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve | OSDI 2024 | Microsoft Research; Georgia Institute of Technology | Sarathi-Serve 用 chunked prefill 和 stall-free scheduling 缓解 prefill/decode 混批中的吞吐-延迟冲突。 |
| Llumnix: Dynamic Scheduling for Large Language Model Serving | OSDI 2024 | Tsinghua University; Alibaba Cloud | Llumnix 通过请求及其 KV 状态的 live migration，在多实例间动态重调度以改善尾延迟、隔离和负载均衡。 |
| ServerlessLLM: Low-Latency Serverless Inference for Large Language Models | OSDI 2024 | University of Edinburgh 等 | ServerlessLLM 利用近 GPU 多层存储、快速 checkpoint loading 和 live migration 降低 serverless LLM 冷启动延迟。 |
| Andes: Defining and Enhancing Quality-of-Experience in LLM-Based Text Streaming Services | OSDI 2024 | University of Michigan | Andes 将用户可感知的首 token 和流式平滑度建模为 QoE，并用 token-level preemptive scheduling 优化体验。 |
| One Queue Is All You Need: Resolving Head-of-Line Blocking in Large Language Model Serving | arXiv 预印本, 2024 | IBM Research; University of Illinois Urbana-Champaign | QLM 用多模型队列编排、模型换入换出和请求状态迁移缓解 burst workload 下的队头阻塞。 |
| NanoFlow: Towards Optimal Large Language Model Serving Throughput | OSDI 2025 | University of Washington | NanoFlow 将请求拆成 operation-level nano-batches，并在单 GPU 内重叠 compute、memory 和 network 资源。 |
| BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching | OSDI 2025 | Shanghai Jiao Tong University; Huawei Cloud | BlitzScale 使用 compute network 加载参数并按层协作执行，实现少 host cache 的快速、在线模型扩缩容。 |
| AdaServe: SLO-Customized LLM Serving with Fine-Grained Speculative Decoding | arXiv 预印本, 2025 | Carnegie Mellon University; Peking University 等 | AdaServe 将 speculative token tree 构造和请求级 SLO 结合，动态选择验证 token 以提高 goodput。 |
| TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity | arXiv 预印本, 2025 | University of Edinburgh 等 | TokenScale 用 token velocity 统一衡量 PD 各阶段压力，并允许 decoder 临时执行 prefill 以吸收突发流量。 |
| OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration | arXiv 预印本, 2026 | University of Cambridge; Shanghai Jiao Tong University 等 | OServe 针对请求空间异质性和流量时间变化，动态选择异构模型部署并迁移并行配置。 |
| vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models | arXiv 预印本, 2026 | Ant Group; vLLM community 等 | vLLM-Omni 把任意到任意多模态模型分解为独立 stage graph，为 LLM、扩散模型和编码器分别批处理和分配 GPU。 |
| RTP-LLM: High-Performance Alibaba LLM Inference Engine | arXiv 预印本, 2026 | Alibaba Group | RTP-LLM 汇总阿里生产推理栈中的快速加载、PD 分离、分层 KV、推测解码、量化和多模态解耦能力。 |

### 推测解码与生成加速

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SpecInfer: Accelerating Generative Large Language Model Serving with Tree-based Speculative Inference and Verification | ASPLOS 2024 | Carnegie Mellon University; Peking University; Meta 等 | SpecInfer 用多个小模型构造候选 token tree，并由目标模型一次并行验证多条生成路径。 |
| Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | ICML 2024 | Princeton University; Together AI; University of Illinois Urbana-Champaign | Medusa 在目标模型上添加多个 decoding heads，无需独立 draft model 即可并行预测和验证多个未来 token。 |
| EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty | ICML 2024 | Microsoft Research Asia; Peking University 等 | EAGLE 在倒数第二层 feature space 中自回归预测草稿，降低 token-level drafting 的不确定性和开销。 |
| EAGLE-2: Faster Inference of Language Models with Dynamic Draft Trees | EMNLP 2024 | Microsoft Research Asia; Peking University 等 | EAGLE-2 根据 draft confidence 动态构建候选树，避免静态树在不同上下文中的效率损失。 |
| MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding | ICML 2025 | Microsoft Research 等 | MagicDec 指出长上下文下 target verification 成本相对下降，并联合优化 draft/target KV cache 以兼顾 batch throughput 和 latency。 |
| SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding | arXiv 预印本, 2025 | ByteDance Seed; University of Chicago 等 | SwiftSpec 将 draft 与 target 异步解耦扩展，并加入 tree-aware KV management 和 fused kernels 追求单请求极低延迟。 |
| Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference | arXiv 预印本, 2025 | Samsung Research 等 | Mirror-SD 在异构 GPU/NPU 上并行运行互补的 draft/target 推测流水线，突破串行 drafting 的延迟上限。 |
| SpecMemo: Speculative Decoding is in Your Pocket | arXiv 预印本, 2025 | University of Illinois Urbana-Champaign | SpecMemo 建模推测解码的内存下界并优化 rejected-token 状态，使受限 GPU 和移动场景也能获得加速。 |
| SparseSpec: Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | arXiv 预印本, 2025 | 多机构联合团队（公开稿未列单位） | SparseSpec 以稀疏注意力版本的同一模型充当 draft，并联合调度 drafting、verification 和动态 KV 管理以加速长 CoT。 |
| Speculative Speculative Decoding | arXiv 预印本, 2026 | 作者公开稿未列单位 | Saguaro 在目标模型验证当前草稿时预先推测验证结果并并行准备下一批草稿，从而进一步隐藏 drafting 串行开销。 |

### MoE、多租户与适配器服务

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Punica: Multi-Tenant LoRA Serving | arXiv 预印本, 2023/持续使用 | University of Washington | Punica 用 heterogeneous batching CUDA kernel 和共享 base model 支撑多租户 LoRA serving。 |
| S-LoRA: Serving Thousands of Concurrent LoRA Adapters | MLSys 2024 | UC Berkeley; Stanford University | S-LoRA 用 unified paging、异构 LoRA kernel 和 tensor parallelism 在单集群中服务数千 adapter。 |
| MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism | arXiv 预印本, 2025 | ByteDance Seed; Peking University 等 | MegaScale-Infer 将 attention 与 MoE FFN 解耦部署，并以 ping-pong pipeline 和 M2N 通信库提高专家利用率。 |
| BrownoutServe: SLO-Aware Inference Serving under Bursty Workloads for MoE-based LLMs | arXiv 预印本, 2025 | Shenzhen University 等 | BrownoutServe 在突发流量下动态减少部分 expert 访问并使用 united experts，在精度和 SLO 之间调节。 |
| DuoServe-MoE: Dual-Phase Expert Prefetch and Cache Scheduling for Efficient MoE LLM Inference | arXiv 预印本, 2025 | University of Sydney 等 | DuoServe-MoE 为 prefill 和 decode 设计不同 expert prefetch/cache 策略，以较小显存运行大型 MoE。 |
| Tarragon: Making MoE-based LLM Inference Resilient | arXiv 预印本, 2026 | University of California, Riverside 等 | Tarragon 将 attention worker 和 expert worker 设为独立故障域，用 KV 增量 checkpoint 和 shadow experts 快速恢复。 |
| InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models | arXiv 预印本, 2026 | Shanghai Jiao Tong University; National University of Singapore 等 | InfiniLoRA 将 LoRA execution 从 base-model inference 解耦，通过共享 LoRA server 和专用 kernel 扩展 MoE/大 rank adapter 服务。 |

### 内存、算子、编译与异构硬件

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention | ASPLOS 2025 | Microsoft Research India | vAttention 通过 CUDA virtual memory 保留连续虚拟 KV layout，同时按需分配物理页，避免重写 attention kernel。 |
| FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | MLSys 2025 | University of Washington; NVIDIA | FlashInfer 用 block-sparse/composable KV format、JIT attention template 和 load-balanced scheduling 提供 serving-oriented kernel。 |
| FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision | arXiv 预印本, 2024 | Colfax Research; Princeton University | FlashAttention-3 利用 Hopper TMA、warp specialization 和 FP8 block quantization 重叠数据移动、matmul 与 softmax。 |
| TileLang: A Composable Tiled Programming Model for AI Systems | arXiv 预印本, 2025 | Microsoft Research Asia; Alibaba 等 | TileLang 将 kernel dataflow 与线程绑定、layout、tensorize 和 pipeline 调度分离，提高 AI kernel 编程的表达力和性能。 |
| Mirage: A Multi-Level Superoptimizer for Tensor Programs | OSDI 2025 | Carnegie Mellon University; Peking University; Purdue University | Mirage 用跨 kernel、thread block 和 thread 层级的统一表示搜索代数变换、调度和新 custom kernel。 |
| Mirage Persistent Kernel: A Compiler and Runtime for Mega-Kernelizing Tensor Programs | arXiv 预印本, 2025 | Carnegie Mellon University; University of Washington 等 | MPK 将多 GPU 模型推理降为 SM-level task graph 和单个 persistent megakernel，实现跨算子软件流水。 |
| Prism: Symbolic Superoptimization of Tensor Programs | arXiv 预印本, 2026 | Carnegie Mellon University 等 | Prism 用 symbolic hierarchical graph 和 e-graph verification 对 LLM tensor program 做可剪枝的符号超优化。 |
| NeuronMM: High-Performance Matrix Multiplication for LLM Inference on AWS Trainium | arXiv 预印本, 2025 | University of California, Merced 等 | NeuronMM 针对 Trainium 的 systolic array、SRAM 和数据布局设计 fused/cached matmul，加速端到端 LLM inference。 |
| PowerInfer-2: Fast Large Language Model Inference on a Smartphone | arXiv 预印本, 2024 | Shanghai Jiao Tong University | PowerInfer-2 以 neuron cluster 为单位在 NPU/CPU/存储间调度和流水，实现超内存 LLM 的手机端推理。 |
| InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management | OSDI 2024 | Seoul National University 等 | InfiniGen 用少量 rehearsal 预测下一层重要 KV，仅从 host memory 预取必要状态以加速 offloaded inference。 |
| Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache | OSDI 2024 | Tsinghua University; Alibaba Cloud | Infinite-LLM 将 attention layer 解耦并使用 pooled distributed KVCache，支撑最长约两百万 token 的弹性服务。 |

### Workload、评测与基础设施方法论

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems | arXiv 预印本, 2024 | Hong Kong Baptist University; Microsoft Azure 等 | BurstGPT 发布 Azure OpenAI 服务的五百余万条真实 trace，揭示 burst、长度和失败模式对调度评估的影响。 |
| Online Scheduling for LLM Inference with KV Cache Constraints | arXiv 预印本, 2025 | Microsoft Research | 该工作将 KV cache 容量约束纳入 online scheduling 理论，分析 batching、延迟与 hindsight optimal 的竞争关系。 |

## 2026-06-11 第二轮追加：奠基系统、正式会议与新兴工作负载

### 奠基性推理系统回补

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Orca: A Distributed Serving System for Transformer-Based Generative Models | OSDI 2022 | Seoul National University; FriendliAI | Orca 以 iteration-level scheduling 和 selective batching 奠定现代 continuous batching LLM serving 的基础。 |
| AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving | OSDI 2023 | UC Berkeley; Peking University | AlpaServe 将模型并行用于多模型 statistical multiplexing，在 burst workload 下联合优化模型放置和并行配置。 |
| FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU | ICML 2023 | Stanford University; UC Berkeley; ETH Zurich | FlexGen 用线性规划在 GPU、CPU 和磁盘间放置权重、激活和 KV cache，使单张消费级 GPU 也能做高吞吐超大模型离线推理。 |
| FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference | NSDI 2026 | Peking University | FastServe 用 token 粒度抢占、skip-join MLFQ 和 KV 状态换入换出降低长请求造成的队头阻塞。 |
| Efficient Memory Management for Large Language Model Serving with PagedAttention | SOSP 2023 | UC Berkeley | vLLM/PagedAttention 用块式虚拟内存管理 KV cache，显著减少碎片并支持 beam search、parallel sampling 和前缀共享。 |
| Prompt Cache: Modular Attention Reuse for Low-Latency Inference | MLSys 2024 | Yale University | Prompt Cache 用显式 prompt module schema 预计算并复用非连续文本模块的 attention state，降低长提示 TTFT。 |
| Hydragen: High-Throughput LLM Inference with Shared Prefixes | arXiv 预印本, 2024 | Stanford University; Georgia Institute of Technology | Hydragen 将共享前缀与独有后缀的 attention 分开计算，把共享部分转成更高效的矩阵运算并扩展到树状前缀。 |
| ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference | ASPLOS 2024 | Seoul National University; Samsung Research | ExeGPT 根据输入输出长度分布和延迟约束搜索 batch、并行度及执行计划，以最大化约束下吞吐。 |
| MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving | arXiv 预印本, 2024 | Shanghai AI Laboratory; UC Berkeley; UC San Diego | MuxServe 结合模型流行度、空间共置和 prefill/decode 时间复用，提高多模型 serving 的显存与算力利用率。 |
| DeepSpeed-FastGen: High-throughput Text Generation for LLMs via MII and DeepSpeed-Inference | arXiv 预印本, 2024 | Microsoft | DeepSpeed-FastGen 以 Dynamic SplitFuse 将长 prompt 拆分并与 generation 动态组合，兼顾有效吞吐和 token 尾延迟。 |
| MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool | arXiv 预印本, 2024 | Institute of Computing Technology, CAS; Huawei 等 | MemServe 以 MemPool 统一管理跨实例分布式 KV，并联合 context caching、PD 分离和全局 locality-aware scheduling。 |
| LoongServe: Efficiently Serving Long-Context Large Language Models with Elastic Sequence Parallelism | arXiv 预印本, 2024 | Peking University | LoongServe 用弹性 sequence parallelism 按请求和阶段实时改变并行度，降低长短请求混合下的 KV 迁移和资源浪费。 |
| Preble: Efficient Distributed Prompt Scheduling for LLM Serving | arXiv 预印本, 2024 | University of California, San Diego | Preble 在分布式集群中联合优化共享前缀 KV 复用和计算负载均衡，并用分层调度处理 prompt locality。 |
| Parrot: Efficient Serving of LLM-based Applications with Semantic Variable | arXiv 预印本, 2024 | Microsoft Research; Shanghai Jiao Tong University | Parrot 用 Semantic Variable 暴露多调用应用的数据流和依赖，使服务端能跨请求做 batching、缓存与流水优化。 |
| Fairness in Serving Large Language Models | arXiv 预印本, 2024 | UC Berkeley; Stanford University | VTC 用输入输出 token 成本定义 work-conserving fairness，避免长请求或大客户长期占用 continuous batching 能力。 |

### MLSys 2025 正式论文补全

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| LeanAttention: Hardware-Aware Scalable Attention Mechanism for the Decode-Phase of Transformers | MLSys 2025 | Microsoft Research | LeanAttention 重构 decode attention 的执行流，在保持精确 attention 的同时提高超长上下文可扩展性。 |
| Rethinking Key-Value Cache Compression Techniques for Large Language Model Serving | MLSys 2025 | Nanyang Technological University | 该工作从生产实现、逐样本质量和输出变长三个角度重新评估 KV 压缩，指出内存节省不必然转化为端到端加速。 |
| SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention | MLSys 2025 | Shanghai AI Laboratory; Tsinghua University; Infinigence-AI | SampleAttention 用 CRA 指标和两阶段 query-guided 结构化筛选，为不同 head 和输入动态选择最低必要稀疏度。 |
| AI Metropolis: Scaling Large Language Model-based Multi-Agent Simulation with Out-of-order Execution | MLSys 2025 | Stanford University; Georgia Institute of Technology | AI Metropolis 跟踪 agent 间真实依赖并乱序执行，消除全局同步造成的伪依赖和 GPU 空闲。 |
| XGrammar: Flexible and Efficient Structured Generation Engine for Large Language Models | MLSys 2025 | Carnegie Mellon University; MLC community | XGrammar 预处理上下文无关 token、压缩运行时 grammar 状态，并与 GPU 推理重叠以实现近零开销结构化生成。 |
| NEO: Saving GPU Memory Crisis with CPU Offloading for Online LLM Inference | MLSys 2025 | UC Berkeley | NEO 将部分 attention 计算和 KV 状态卸载到 CPU，并以非对称 GPU-CPU 流水和负载感知调度扩大在线 batch。 |
| FlexInfer: Flexible LLM Inference with CPU Computations | MLSys 2025 | Georgia Institute of Technology | FlexInfer 根据硬件、序列长度和 batch 为 prefill/decode 分别选择 CPU-GPU 执行策略，降低单 GPU offload 延迟。 |
| Context Parallelism for Scalable Million-Token Inference | MLSys 2025 | Meta | 该工作用 pass-KV/pass-Q 两种精确 ring attention 在 128 张 H100 上扩展百万 token prefill 和 persistent-KV decode。 |
| Marconi: Prefix Caching for the Era of Hybrid LLMs | MLSys 2025 | University of Michigan; Together AI; Amazon | Marconi 为 attention-SSM hybrid models 设计基于复用概率和计算收益的 prefix cache admission/eviction。 |
| MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators | MLSys 2025 | Microsoft Research; University of Illinois Urbana-Champaign | MiLo 用自适应低秩补偿器恢复超低比特 MoE 的精度，并配套 Tensor Core 友好的 3-bit kernel。 |
| FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference | MLSys 2025 | UC San Diego; Amazon | FastTree 为 radix-tree KV 共享设计专用 attention kernel，并在 runtime 中自适应划分共享上下文查询组。 |
| Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking | MLSys 2025 | Qualcomm AI Research | 该工作用 predictor-free 动态输入剪枝和 cache-aware masking 减少移动端 SwiGLU 模型的 DRAM 流量。 |
| SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling | MLSys 2025 | Tsinghua University; Infinigence-AI | SOLA 在每次迭代感知请求状态和系统状态，动态平衡 TTFT、TPOT 及请求间公平性。 |
| ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments | MLSys 2025 | University of Cambridge; Peking University; ETH Zurich | ThunderServe 在异构 GPU 和网络环境中联合优化部署与并行策略，并以轻量重调度适应故障和流量漂移。 |
| Seesaw: High-throughput LLM Inference via Model Re-sharding | MLSys 2025 | University of Toronto; Microsoft | Seesaw 在 prefill/decode 阶段间动态重分片模型，并用分层 KV buffer 和 transition-aware scheduling 控制切换成本。 |
| LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention | MLSys 2025 | MIT Han Lab | LServe 将 prefill 与 decode 的硬件友好结构化稀疏统一起来，以 streaming heads 和层次 KV page selection 加速长序列服务。 |
| COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts | MLSys 2025 | Alibaba Cloud; Peking University | COMET 通过依赖分析、任务重排和自适应工作量分配细粒度重叠 MoE 通信与计算，并已用于万卡级生产集群。 |
| TurboAttention: Efficient Attention Approximation for High-Throughput LLMs | MLSys 2025 | Microsoft Research; Georgia Institute of Technology | TurboAttention 结合量化 attention 乘法和 softmax 近似，减少 KV 带宽、反量化与指数计算开销。 |
| QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving | MLSys 2025 | MIT Han Lab | QServe 联合 W4A8KV4 量化、SmoothAttention、权重重排和寄存器级并行，将理论低比特节省转成云端 serving 吞吐。 |
| MAS-Attention: Memory-Aware Stream Processing for Attention Acceleration on Resource-Constrained Edge Devices | MLSys 2025 | University of Toronto | MAS-Attention 在边缘 NPU 上将向量和矩阵计算组织为双流多级 tiling，并主动覆盖 cache 以减少 spill。 |

### OSDI 2025 正式论文补全

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| KPerfIR: Towards an Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads | OSDI 2025 | UC San Diego; Meta; OpenAI | KPerfIR 将可编程 profiling pass 集成进 Triton compiler，在较低开销下分析 GPU kernel 内细粒度单元重叠与瓶颈。 |
| QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach | OSDI 2025 | ICT, CAS; Cambricon; USTC | QiMeng-Xpiler 结合 LLM 代码生成、符号修复和分层 autotuning，在 CUDA、HIP、VNNI 和 BANG 间转译 tensor program。 |
| WaferLLM: Large Language Model Inference at Wafer Scale | OSDI 2025 | University of Edinburgh; Microsoft Research | WaferLLM 用 PLMR 模型、wafer-scale parallelism、MeshGEMM 和 MeshGEMV 将 LLM inference 映射到数十万片上 core。 |
| FuseLink: Enabling Efficient GPU Communication over Multiple NICs | OSDI 2025 | HKUST; USTC; Meta; Peking University | FuseLink 允许 GPU 经机内高速链路转发到空闲 NIC，消除静态 GPU-NIC 绑定造成的热点并加速首 token 生成。 |
| PipeThreader: Software-Defined Pipelining for Efficient DNN Execution | OSDI 2025 | Georgia Institute of Technology; Intel | PipeThreader 在 operator 和 kernel 内分片，按硬件资源流水执行 DNN stage，从系统层提高异构执行重叠。 |
| DecDEC: A Systems Approach to Advancing Low-bit LLM Quantization | OSDI 2025 | UC Berkeley; Stanford University | DecDEC 将低比特表示、解码数据流和硬件执行联合设计，减少超低比特权重反量化对 LLM inference 的实际开销。 |

### 2025-2026 新兴工作负载与系统方向

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Niyama: Breaking the Silos of LLM Inference Serving | arXiv 预印本, 2025 | Microsoft Research | Niyama 以细粒度 QoS 分类、动态 chunking 和选择性请求降级在共享集群中混部交互式与批处理负载。 |
| Towards Efficient Large Multimodal Model Serving | arXiv 预印本, 2025 | Microsoft Research; Clemson University; Brown University | 该工作基于生产多模态 trace 分析 encode/prefill/decode 的异质性，并提出分阶段资源分配和自适应伸缩。 |
| HydraInfer: Hybrid Disaggregated Scheduling for Multimodal Large Language Model Serving | arXiv 预印本, 2025 | Chinese Academy of Sciences; Beihang University 等 | HydraInfer 将视觉 encode、prefill 和 decode 分到异构实例，以 stage-level batching 和并行执行提高 MLLM 吞吐。 |
| GreenLLM: SLO-Aware Dynamic Frequency Scaling for Energy-Efficient LLM Serving | arXiv 预印本, 2025 | EPFL | GreenLLM 对 prefill/decode 分别建模和调频，在维持 token SLO 的同时降低 GPU 能耗。 |
| LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems | arXiv 预印本, 2025 | University of California, Riverside 等 | LeMix 联合调度持续训练与在线推理，通过预测干扰和动态资源分配利用空闲 GPU 而不牺牲 serving 响应性。 |
| Cascadia: A Cascade Serving System for Large Language Models | arXiv 预印本, 2025 | University of Cambridge; HKUST | Cascadia 联合优化大小模型 cascade 的查询路由、资源分配和并行部署，在回答质量约束下改善延迟与成本。 |
| Prism: Unleashing GPU Sharing for Cost-Efficient Multi-LLM Serving | arXiv 预印本, 2025 | UCLA; UC Berkeley; Stanford University | Prism 用跨模型虚拟内存协调和两级调度动态调整 GPU 时空共享，以应对长尾模型流行度和流量波动。 |
| LoRAServe: Serving Heterogeneous LoRA Adapters in Distributed LLM Inference Systems | arXiv 预印本, 2025 | Microsoft Research; University of Illinois Urbana-Champaign | LoRAServe 感知 adapter rank 差异，动态重平衡放置并通过 GPUDirect RDMA 远程访问 adapter，降低多租户尾延迟。 |
| Tokencake: A KV-Cache-centric Serving Framework for LLM-based Multi-Agent Applications | arXiv 预印本, 2025 | Peking University | Tokencake 针对 tool-call stall 和 agent 优先级联合做 KV 空间隔离、主动 offload 与预测 upload。 |
| FailSafe: High-performance Resilient Serving | arXiv 预印本, 2025 | Stanford University | FailSafe 用循环 KV 放置、混合 attention、负载路由和主动 KV 备份，使 tensor-parallel serving 在 GPU 故障后继续运行。 |
| ORBITFLOW: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration | arXiv 预印本, 2026 | UNIST 等 | ORBITFLOW 以轻量 ILP 按请求和层动态决定 GPU/CPU KV 放置，并根据运行反馈重配置以控制尾延迟。 |
| Cornserve: Efficiently Serving Any-to-Any Multimodal Models | arXiv 预印本, 2025 | University of Michigan | Cornserve 从任意到任意多模态 computation graph 自动规划组件拆分和部署，并用分布式 runtime 处理路径异质性。 |
| Serve Programs, Not Prompts | arXiv 预印本, 2025 | Yale University | 该工作提出 LLM Inference Program 和 Symphony OS，将 token prediction、KV 文件系统及工具执行变成服务端可调度程序。 |
| TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing | arXiv 预印本, 2026 | Peking University | TokenDance 利用多 agent round 的 All-Gather 结构集中复用共享 KV，并用 block-sparse diff 压缩 sibling cache。 |
| SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips | arXiv 预印本, 2026 | University of Illinois Urbana-Champaign; Microsoft | SuperInfer 面向 GH200 的 NVLink-C2C 设计请求轮转调度和全双工 KV 搬运，缓解高负载下的 HOL blocking。 |
| CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | arXiv 预印本, 2026 | University of Michigan | CacheFlow 将 KV 恢复重构为 token、layer、GPU 三维并行，并以 batch-aware scheduler 联合分配重算和 I/O。 |
| VeriCache: Turning Lossy KV Cache into Lossless LLM Inference | arXiv 预印本, 2026 | University of Chicago; UIUC | VeriCache 用压缩 KV 起草、完整 KV 验证，并重叠 HBM 解码与 PCIe/网络换入，保证输出与 full-KV 完全一致。 |
| Joint Encoding of KV-Cache Blocks for Scalable LLM Serving | arXiv 预印本, 2026 | IBM Research | 该工作跨请求融合相似 KV block 为共享表示，在维持标准 cache layout 的同时提高并发容量。 |
| NPUMoE: Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs | arXiv 预印本, 2026 | University of Virginia | NPUMoE 将静态密集 expert 计算卸载到 Apple NPU，并为动态 routing 保留 CPU/GPU fallback。 |
| When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference | arXiv 预印本, 2026 | 多机构联合团队 | 该工作分离量化、通信和计算开销，揭示移动端 NPU 在 prefill/decode 中可能因调度和 fallback 而不如 CPU。 |

### NSDI 2026 正式论文补充

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds | NSDI 2026 | Peking University; Alibaba Group | HydraServe 主动分发模型、重叠 worker 冷启动阶段并规避网络争用，以 pipeline consolidation 降低 serverless LLM 启动资源。 |
| JITServe: SLO-aware LLM Serving with Imprecise Request Information | NSDI 2026 | UIUC; Google; Cisco Research | JITServe 在输出长度和调用依赖未知时逐步收紧估计，并只分配满足 SLO 所需的 just-in-time serving bandwidth。 |
| Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads | NSDI 2026 | National University of Singapore; USTC; UC Berkeley | Libra 在任意 token 边界把请求拆为 micro-requests，以全局/局部两级调度和 chunked KV transfer 平衡动态负载。 |
| SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading | NSDI 2026 | Tencent; Nanjing University | SwiftEP 用 buffer fusion 消除 MoE all-to-all staging copy，并以 TMA、RDMA scatter-gather 和 CUDA IPC 提高链路利用率。 |
| FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees | NSDI 2026 | Carnegie Mellon University; Purdue University; Anthropic; Mistral AI; AWS | FlexLLM 在 token 粒度交错在线推理和 PEFT 微调，并用静态图裁剪与 hybrid scheduler 保持 inference SLO。 |
| ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production | NSDI 2026 | Peking University; Alibaba Group | ServeGen 基于全球云服务 trace 刻画语言、多模态和 reasoning 模型负载，并按 client 组合生成更真实的 benchmark workload。 |
| PlanetServe: A Decentralized, Scalable, and Privacy-Preserving Overlay for Democratizing Large Language Model Serving | NSDI 2026 | UC Santa Cruz; University of Nevada, Reno | PlanetServe 用去中心化 overlay 聚合分散算力，并联合设计转发、隐私和服务质量验证。 |
| Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access for LLM via Semantic-Aware Knowledge Caching | NSDI 2026 | National University of Singapore; USTC; University of Toronto; Sea AI Lab | Cortex 以语义元素和两阶段判定实现跨区域 agent knowledge cache，并把延迟、成本和静态性纳入淘汰与预取。 |
| Agentix: An Efficient Serving Engine for LLM Agents as General Programs | NSDI 2026 | UC Berkeley; Google DeepMind; Shanghai Jiao Tong University | Agentix 把 agent program 而非单次请求作为调度对象，利用程序依赖和已完成调用对后续 LLM call 抢占与提权。 |

### 综述、评测方法与可持续性

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems | arXiv 综述, 2023 | Carnegie Mellon University 等 | 该综述从算法、单机 runtime 到分布式 serving 系统梳理生成式 LLM 推理的效率技术与研究问题。 |
| The CAP Principle for LLM Serving: A Survey of Long-Context Large Language Model Serving | arXiv 综述, 2024 | ICT, CAS; Huawei 等 | 该综述以 Context length、Accuracy、Performance 三目标冲突组织长上下文 serving，并强调用户感知指标定义。 |
| LLM Inference Serving: Survey of Recent Advances and Opportunities | arXiv 综述, 2024 | Northeastern University; MIT Lincoln Laboratory | 该综述聚焦 2023 年后的系统级 LLM serving 论文，覆盖调度、内存、并行和生产部署机会。 |
| Towards Sustainable Large Language Model Serving | HotCarbon 2024 | University of Waterloo; Purdue University | 该工作同时建模 GPU 运行能耗、电网碳强度和芯片 embodied carbon，分析硬件代际选择的碳排权衡。 |
| Taming the Titans: A Survey of Efficient LLM Inference Serving | arXiv 综述, 2025 | Soochow University; Alibaba Cloud 等 | 该综述按 instance、cluster 和新兴应用场景系统整理模型放置、调度、存储、分离架构及云端策略。 |
| On Evaluating Performance of LLM Inference Serving Systems | arXiv 预印本, 2025 | Microsoft Research; Georgia Institute of Technology | 该工作归纳 baseline、实验配置和 metric 反模式，并用推测解码案例说明错误归一化会掩盖 generation stall。 |
| SLOs-Serve: Optimized Serving of Multi-SLO LLMs | arXiv 预印本, 2025 | Carnegie Mellon University; Google | SLOs-Serve 用动态规划联合选择 chunked prefill、推测解码和 replica 路由，为不同应用与阶段分配 token budget。 |
| SCORPIO: Serving the Right Requests at the Right Time for Heterogeneous SLOs in LLM Inference | arXiv 预印本, 2025 | 作者公开稿未列单位 | SCORPIO 以 TTFT/TPOT 双 guard、deadline 重排、准入控制和 credit batching 提升异质 SLO goodput。 |
| AccelGen: Heterogeneous SLO-Guaranteed High-Throughput LLM Inference Serving for Diverse Applications | arXiv 预印本, 2025 | University of Virginia | AccelGen 用动态 chunk、iteration SLO 优先级和 compute/KV 双资源感知 batching 服务长短 prompt 与不同延迟约束。 |
| Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving | arXiv 预印本, 2025 | HKUST | Apt-Serve 将 KV cache 与更省内存的 hidden cache 组合，并动态优化 batch composition 以扩大并发和 TTFT goodput。 |
| AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving | arXiv 预印本, 2025 | Zhejiang University 等 | AugServe 针对 tool-augmented 请求用两阶段调度和动态 token batch limit 缓解未知暂停与队头阻塞。 |

### 扩散与多模态生成服务

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| DiffServe: Efficiently Serving Text-to-Image Diffusion Models with Query-Aware Model Scaling | MLSys 2025 | University of Massachusetts Amherst | DiffServe 按 prompt 难度在不同规模 diffusion model 间路由，并联合优化模型选择与资源配置。 |
| ScaleFusion: Scalable Inference of Spatial-Temporal Diffusion Transformers for High-Resolution Long Video Generation | MLSys 2025 | University of Toronto; AWS | ScaleFusion 针对高分辨率长视频 DiT 设计时空并行、通信重叠和动态执行策略。 |
| MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models | arXiv 预印本, 2025 | Intel Labs 等 | MoDM 以最终图像 cache 和大小 diffusion model 混合路由，在响应质量、延迟和 GPU 分配间动态权衡。 |
| CompactFusion: Accelerating Parallel Diffusion Model Serving with Residual Compression | arXiv 预印本, 2025 | Tsinghua University | CompactFusion 利用相邻 denoising step 激活的时间冗余，只传压缩 residual 并用误差反馈控制质量损失。 |
| HADIS: Hybrid Adaptive Diffusion Model Serving for Efficient Text-to-Image Generation | arXiv 预印本, 2025 | University of Massachusetts Amherst | HADIS 联合选择 cascade、prompt routing 和 GPU allocation，让明显困难的请求绕过无效轻量模型阶段。 |
| TridentServe: A Stage-level Serving System for Diffusion Pipelines | arXiv 预印本, 2025 | Peking University; Carnegie Mellon University; University of Cambridge | TridentServe 将 encode、diffuse、decode 分阶段放置，并动态联合优化模型 placement 与请求 dispatch。 |

## 2026-06-11 第三轮追加：ASPLOS 2026、FAST 2026 与系统方法扩展

### ASPLOS 2026：LLM Serving 吞吐、延迟与调度

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration | ASPLOS 2026 | Sun Yat-sen University | Bullet 在空间放置和时间调度两个维度动态编排 LLM 请求，以减少 GPU 碎片并提高服务利用率。 |
| QoServe: Breaking the Silos of LLM Inference Serving | ASPLOS 2026 | Microsoft Research India | QoServe 统一管理原本割裂的 LLM serving 资源池，以减少不同服务等级和工作负载之间的资源孤岛。 |
| Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads | ASPLOS 2026 | Snowflake AI Research | Shift Parallelism 在 TP 与 sequence parallelism 间动态切换，以适应实时流量中的延迟和吞吐变化。 |
| XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads | ASPLOS 2026 | Huawei Technologies; Tsinghua University; Shanghai AI Laboratory | XY-Serve 用 token-wise P/D/V 调度、任务分解重排和 Ascend meta-kernel 平滑动态 shape 与混合阶段负载。 |
| PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel | ASPLOS 2026 | Tianjin University; Stevens Institute of Technology | PAT 利用 prefix-aware attention 和 resource-efficient multi-tile kernel 加速共享前缀场景下的 LLM 解码。 |
| ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression | ASPLOS 2026 | HKUST Guangzhou; Harbin Institute of Technology Shenzhen; HKUST | ZipServ 以硬件感知无损压缩降低模型推理的内存占用和数据搬运，同时避免有损量化带来的质量风险。 |
| BlendServe: Optimizing Offline Inference with Resource-Aware Batching | ASPLOS 2026 | UC Berkeley; University of Washington; UC Davis; Rice University | BlendServe 用 resource-aware prefix tree 维持 prefix sharing，并将计算密集和带宽密集请求混合执行。 |
| BAT: Efficient Generative Recommender Serving with Bipartite Attention | ASPLOS 2026 | Zhejiang University; University of Hong Kong; Alibaba Group; National University of Singapore | BAT 为生成式推荐设计 bipartite attention 和相应 serving 路径，减少推荐上下文与生成阶段的冗余计算。 |
| MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading | ASPLOS 2026 | Shanghai Jiao Tong University; Chinese University of Hong Kong | MoE-APEX 根据 expert 热度和执行需求自适应选择精度与卸载方式，缓解 MoE 权重容量和传输瓶颈。 |
| DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU | ASPLOS 2026 | Shanghai Jiao Tong University; Southeast University; Eastern Institute of Technology Ningbo | DFVG 将 draft 放在 FPGA、verify 放在 GPU，以异构流水降低推测解码的草稿成本并提高验证硬件利用率。 |

### ASPLOS 2026：推测解码与 Agent 推理

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs | ASPLOS 2026 | Shanghai Jiao Tong University; Infinigence-AI; Tsinghua University; SII | SpeContext 推测长上下文中的稀疏访问区域，以减少 reasoning 阶段需要执行的 attention 上下文。 |
| It Takes Two to Entangle | ASPLOS 2026 | New York University; ByteDance | 该工作研究组合式 AI 系统中不同执行组件之间的耦合，揭示单独优化某一模型阶段可能无法改善端到端性能。 |
| Efficient LLM Serving for Agentic Workflows with Context-Aware State Management | EuroSys 2026 poster | University of Cambridge; Polytechnique Montréal | 该工作针对 agent 多轮调用中的可复用上下文和中间状态设计 context-aware 管理机制，减少重复 prefill 与状态搬运。 |
| A First Look at Bugs in LLM Inference Serving Systems | EuroSys 2026 poster | Cornell University | 该工作系统归纳 LLM serving runtime 中的正确性、并发、内存和性能故障模式，为可靠性研究建立问题分类。 |

### ASPLOS 2026：Attention、KV、MoE 与高效推理

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse | ASPLOS 2026 | Shanghai Jiao Tong University; National University of Defense Technology | EARTH 根据 gating entropy 推测预取 expert 并复用结果，以降低 MoE expert 加载等待与误预取代价。 |
| MSCCL++: Rethinking GPU Communication Abstractions for AI Inference | ASPLOS 2026 | Microsoft Research; Microsoft Azure | MSCCL++ 以可编程通信抽象和优化 collective 支撑 tensor/expert parallel 与分离式 AI inference。 |
| Insum: Sparse GPU Kernels Simplified and Optimized with Indirect Einsums | ASPLOS 2026 | MIT; Georgia Institute of Technology; NVIDIA | Insum 用 indirect einsum 抽象表达并优化稀疏 GPU kernel，降低实现不规则推理算子的复杂度。 |
| I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention | ASPLOS 2026 | Illinois Institute of Technology; ICT, CAS; University of Chinese Academy of Sciences | 该工作从 I/O 复杂度而非 FLOPs 分析长序列 attention，指导算法与硬件在数据搬运瓶颈下协同优化。 |
| REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing | ASPLOS 2026 | Shanghai Jiao Tong University | REPA 用可重构 PIM 同时加速 KV cache 的卸载传输与就地处理，减少长上下文推理的数据移动。 |
| STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems | ASPLOS 2026 | Rensselaer Polytechnic Institute; University of Massachusetts Amherst; IBM Research | STARC 通过 token 选择、重映射和聚类，让 PIM 系统只访问对当前解码关键的 KV 数据。 |
| Mugi: Value Level Parallelism For Efficient LLMs | ASPLOS 2026 | University of Central Florida; Carnegie Mellon University | Mugi 在数值层面开发新的并行粒度，以提高 LLM 中细粒度运算的硬件利用率。 |
| TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference | ASPLOS 2026 | Peking University; Tencent YouTu Lab | TPLA 将 latent attention 与 tensor parallel 结合，降低 PD 分离推理中的 KV 和跨卡通信压力。 |
| LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training | ASPLOS 2026 | Peking University; Shanghai Jiao Tong University; ByteDance Seed | LAER-MoE 根据 expert 负载动态重排布局，属于与推理基础设施相邻的 MoE 训练系统工作。 |
| oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference | ASPLOS 2026 | Sogang University; Santa Clara University | oFFN 感知 outlier 与 neuron 重要性构造结构化 FFN，在保持精度的同时提高规则硬件上的推理效率。 |
| FastTTS: Accelerating Test-Time Scaling for Edge LLM Reasoning | ASPLOS 2026 | Imperial College London; Microsoft Research | FastTTS 面向边缘设备优化 test-time scaling，使多次候选生成与验证能够在受限资源上高效执行。 |

### ASPLOS 2026：编译、GPU Kernel 与新型硬件

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context | ASPLOS 2026 | George Mason University; Google; Meta; Anthropic | Triton-Sanitizer 为 Triton kernel 提供跨设备内存错误检测和丰富诊断上下文，补齐生成式 AI kernel 的调试基础设施。 |
| Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F2 | ASPLOS 2026 | OpenAI; George Mason University | Linear Layouts 用有限域上的统一布局表示描述 tensor 数据映射，为高性能 GPU kernel 生成提供可组合基础。 |
| Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference | ASPLOS 2026 | ICT, CAS; University of Chinese Academy of Sciences | Ouroboros 以 wafer-scale SRAM compute-in-memory 和 token-grained pipeline 加速大模型推理。 |
| A Cost-Effective Near-Storage Processing Solution for Offline Inference of Long-Context LLMs | ASPLOS 2026 | Seoul National University; POSTECH | 该工作把长上下文离线推理的数据密集部分下沉到近存储处理器，降低主机内存和 I/O 成本。 |
| TetriServe: Efficiently Serving Mixed DiT Workloads | ASPLOS 2026 | University of Michigan; University of Wisconsin-Madison; Nanyang Technological University | TetriServe 面向不同扩散 Transformer 请求联合做批处理和资源编排，提高混合 DiT workload 的服务效率。 |
| Tilus: A Tile-Level GPGPU Programming Language for Low-Precision Computation | ASPLOS 2026 | University of Toronto; CentML; Carnegie Mellon University; University of Waterloo; Anyscale; Amazon | Tilus 用 tile-level 语言表达低精度 GPGPU 运算，为量化推理 kernel 提供可组合代码生成。 |
| Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking | ASPLOS 2026 | Tsinghua University; Tianjin University; Microsoft Research | Neuralink 利用 neuron co-activation 关系减少端侧 LLM 推理中的无效权重访问与计算。 |
| PF-LLM: Large Language Model Hinted Hardware Prefetching | ASPLOS 2026 | Hong Kong University of Science and Technology; Duke University | PF-LLM 让 LLM 辅助识别访存模式并向硬件预取器提供提示，提高复杂数据访问下的 cache 命中。 |
| M2XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization | ASPLOS 2026 | Shanghai Jiao Tong University; Huawei | M2XFP 用少量 metadata 扩展 microscaling 格式，在维持规则低比特硬件执行的同时恢复量化精度。 |
| gShare: Efficient GPU Sharing with Aggressive Scheduling in Multi-tenant FaaS Platform | ASPLOS 2026 | China Telecom | gShare 在多租户 FaaS 中采用激进 GPU 共享和调度，提高短时、突发 AI function 的设备利用率。 |
| GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management | ASPLOS 2026 | Shanghai Jiao Tong University; Zhejiang University; Alibaba Group | GFS 预测 spot instance 风险并进行抢占感知调度，降低 GPU 集群中任务中断和资源浪费。 |
| Asynchrony and GPUs: Bridging this Dichotomy for I/O with AGIO | ASPLOS 2026 | Pennsylvania State University; NVIDIA | AGIO 为 GPU 构建真正异步的 I/O 路径，使模型数据和状态传输可以与 kernel 执行重叠。 |
| HybridTier: An Adaptive and Lightweight CXL-Memory Tiering System | ASPLOS 2026 | University of Toronto; UC San Diego; University of Waterloo; CentML | HybridTier 以轻量在线策略在本地 DRAM 与 CXL memory 间迁移热页，为模型权重和 KV 的容量扩展提供通用基础。 |
| Transforming Torus Fabrics for Efficient Multi-tenant ML | ASPLOS 2026 | Cornell University; Lightmatter | 该工作重构 torus fabric 的路由和隔离方式，使多个 ML tenant 在共享互连上获得更稳定的 collective 性能。 |
| RedFuser: An Automatic Operator Fusion Framework for Cascaded Reductions on AI Accelerators | ASPLOS 2026 | Alibaba Cloud | RedFuser 自动融合级联 reduction 算子，减少 AI accelerator 上的中间张量写回和 kernel launch。 |
| Performance Predictability in Heterogeneous Memory | ASPLOS 2026 | Virginia Tech; Microsoft; NVIDIA | 该工作研究异构内存中的性能可预测性，为模型权重、KV 和中间状态的分层放置提供基础模型。 |

### FAST 2026：AI 存储、模型加载与容错

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs | FAST 2026 | Shanghai Jiao Tong University | SolidAttention 以动态稀疏注意力、SSD KV 分块和推测预取，在内存受限 PC 上支撑长上下文本地推理。 |
| CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | FAST 2026 | Shanghai Jiao Tong University; Inspur; Peking University; Huawei Cloud | CacheSlide 针对 agent prompt 中相对位置稳定的片段设计 RPDC、位置校正和 layer-wise spill-aware KV 复用。 |
| Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation-Storage Awareness | FAST 2026 | Tsinghua University; China University of Geosciences Beijing; China Telecom | Bidaw 让计算调度感知 KV 加载延迟，并让两级存储利用模型响应预测访问与淘汰，提高多轮会话 KV 命中。 |
| Accelerating Model Loading in LLM Inference by Programmable Page Cache | FAST 2026 | Huawei Technologies | PPC 提供非侵入可编程 page-cache 策略，MAIO 再以 I/O template、XPU affinity 和局部性优化模型加载。 |
| GPU Checkpoint/Restore Made Fast and Lightweight | FAST 2026 | Tsinghua University | GCR 通过控制/数据分离、CPU shadow execution 和 dirty template 降低 GPU checkpoint、restore 与增量快照开销。 |
| Fast Cloud Storage for AI Jobs via Grouped I/O API with Transparent Read/Write Optimizations | FAST 2026 | Shanghai Jiao Tong University; Huawei Cloud | AITURBO 利用加速器互连和 grouped I/O API 自动生成存储层读写计划，覆盖 checkpoint 与 KV-cache I/O。 |

### 2026 新兴评测、仿真与系统研究工具

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| LLMServingSim 2.0: An Enhanced Simulator for LLM Serving Systems with Graph-Based Workloads | arXiv 预印本, 2026 | Seoul National University | LLMServingSim 2.0 用图结构表达多阶段、分支和 agent 请求，为新调度与异构部署方案提供可重复仿真平台。 |
| Taming LLM Inference: Lessons Learned from Optimizing Large Language Model Inference Across Diverse Hardware | arXiv 预印本, 2026 | Databricks | 该工作总结跨 GPU 和专用加速器优化 LLM inference 的工程经验，强调端到端 profile、内核适配和工作负载匹配。 |
| Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Tangram 以确定性 head 预算、Head Group Page 和 AOT 负载均衡，把非均匀 KV 压缩转化为可高效执行的 serving layout。 |
| KV Cache Optimization Strategies for Scalable and Efficient LLM Inference | arXiv 综述, 2026 | 作者公开稿未列单位 | 该综述从淘汰、压缩、混合内存、新注意力和组合策略五条路线比较 KV 优化，并映射到七类部署场景。 |
| AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving | SOSP 2025 BigMem Workshop | University of Chicago; Microsoft Research 等 | AdaptCache 为每个 KV entry 联合选择有损压缩算法、压缩率和 DRAM/SSD 放置，在质量约束下提高 DRAM 命中并降低恢复延迟。 |

## 2026-06-12 第四轮追加：体系结构、数据系统与最新部署研究

### ISCA 2025：Wafer、低比特与端侧推理

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| WSC-LLM: Efficient LLM Service and Architecture Co-exploration for Wafer-scale Chips | ISCA 2025 | Tsinghua University; Shanghai AI Laboratory; Shanghai Jiao Tong University | WSC-LLM 联合搜索 wafer-scale 芯片架构和 serving 配置，使模型并行、片上互连与请求负载共同决定部署方案。 |
| H2-LLM: Hardware-Dataflow Co-Exploration for Efficient Heterogeneous Hybrid Bonding-based LLM Inference | ISCA 2025 | ISCA 2025 官方目录未列单位 | H2-LLM 围绕异构 hybrid-bonding 芯粒联合探索硬件组织和数据流，以减少 LLM 推理中的跨层数据移动。 |
| Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization | ISCA 2025 | KAIST | Oaken 将离线量化与在线自适应 KV 量化结合，在降低 cache 带宽和容量的同时控制运行时开销。 |
| LUT Tensor Core: Lookup Table Enables Efficient Low-Bit LLM Inference Acceleration | ISCA 2025 | Microsoft Research Asia 等 | LUT Tensor Core 用查找表数据通路处理低比特权重与激活，降低超低精度 LLM 推理的解码和乘加成本。 |
| AiF: Accelerating On-Device LLM Inference Using In-Flash Processing | ISCA 2025 | Seoul National University; Soongsil University; Kyungpook National University | AiF 将部分权重处理下沉到 flash 内部，缓解端侧设备加载大模型时的存储带宽和内存容量瓶颈。 |
| LIA: A Single-GPU LLM Inference Acceleration with Layer Bypass and Adaptive Speculative Decoding | ISCA 2025 | ISCA 2025 官方目录未列单位 | LIA 联合 layer bypass 与自适应推测解码，在单 GPU 上减少不必要的层执行和 token generation 延迟。 |

### HPCA 2025：量化、PIM、存储与能耗

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration | HPCA 2025 | HPCA 2025 官方目录未列单位 | BitMoD 用 bit-serial 数据通路支持多种低比特数据类型，使不同层和张量能按精度需求选择执行格式。 |
| VQ-LLM: High-performance Code Generation for Vector Quantization Augmented LLM Inference | HPCA 2025 | HPCA 2025 官方目录未列单位 | VQ-LLM 为向量量化模型自动生成高性能 kernel，将码本查找、解码与矩阵运算融合。 |
| Anda: Unlocking Efficient LLM Inference with a Variable-Length Grouped Activation Data Format | HPCA 2025 | KU Leuven; Nanjing University 等 | Anda 用可变长度 grouped activation 格式适配不同激活分布，在规则硬件上降低存储与计算成本。 |
| M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type | HPCA 2025 | HPCA 2025 官方目录未列单位 | M-ANT 根据分组数据分布选择数学自适应数值类型，提高低比特量化的精度和硬件效率。 |
| throttLL'eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving | HPCA 2025 | HPCA 2025 官方目录未列单位 | throttLL'eM 预测 token 阶段的性能余量并动态调节 GPU 功率或频率，在满足 serving SLO 时降低能耗。 |
| PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM | HPCA 2025 | HPCA 2025 官方目录未列单位 | PAISE 将 Transformer 请求调度与 PIM 执行特征联合建模，降低内存密集 decode 的排队和数据移动。 |
| Make LLM Inference Affordable to Everyone: Augmenting GPU Memory with NDP-DIMM | HPCA 2025 | HPCA 2025 官方目录未列单位 | NDP-DIMM 用带近数据处理能力的 DIMM 扩展 GPU 可用模型容量，并减少经 PCIe 搬运全部权重的开销。 |
| InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference | HPCA 2025 | HPCA 2025 官方目录未列单位 | InstAttention 将长上下文 attention 的部分 KV 访问和计算下沉到存储设备，以低成本容量替代全量 HBM 常驻。 |
| FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference | HPCA 2025 | HPCA 2025 官方目录未列单位 | FACIL 动态调整 DRAM 地址映射，使 SoC 与 PIM 在端侧 LLM 不同阶段间高效协作。 |
| DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency | HPCA 2025 | University of Illinois Urbana-Champaign; Microsoft | DynamoLLM 动态选择集群硬件、并行和功率配置，在请求 SLO、成本和能耗之间联合优化。 |
| Lincoln: Real-Time 50~100B LLM Inference on Consumer Devices with LPDDR-Interfaced, Compute-Enabled Flash Memory | HPCA 2025 | HPCA 2025 官方目录未列单位 | Lincoln 用 LPDDR 接口连接具备计算能力的 flash，使消费设备能够流式执行 50B 到 100B 级模型。 |
| LAD: Efficient Accelerator for Generative Inference of LLM with Locality Aware Decoding | HPCA 2025 | HPCA 2025 官方目录未列单位 | LAD 利用 token decoding 中的局部性组织权重、KV 和计算单元，减少生成阶段的无效数据访问。 |

### MICRO 2025：新型内存、混合模型与推理加速器

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving | MICRO 2025 | UC San Diego; Georgia Institute of Technology 等 | Stratum 将分层 monolithic-3D DRAM、近存计算和 expert 热度预测结合，提高 MoE decode 的带宽和能效。 |
| LLMulator: Generalizable Cost Modeling for Dataflow Accelerators with Input-Adaptive Control Flow | MICRO 2025 | ICT, CAS; University of Chinese Academy of Sciences | LLMulator 为带输入自适应控制流的数据流加速器建立可泛化成本模型，帮助预测 LLM workload 的性能。 |
| DECA: A Near-Core LLM Decompression Accelerator Grounded on a 3D Roofline Model | MICRO 2025 | University of Illinois Urbana-Champaign; Intel | DECA 用三维 roofline 模型确定压缩、内存和计算瓶颈，并在 near-core 路径加速低比特权重解压。 |
| Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments | MICRO 2025 | University of Illinois Urbana-Champaign; IBM | Chameleon 联合管理大量 LoRA/adapter 的缓存和请求调度，减少多租户适配器服务中的换入与等待。 |
| Accelerating Retrieval Augmented Language Model via PIM and PNM Integration | MICRO 2025 | MICRO 2025 官方目录未列单位 | 该工作把向量检索和生成前的数据处理分配到 PIM/PNM 路径，减少 RAG pipeline 的跨设备搬运。 |
| Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference | MICRO 2025 | MICRO 2025 官方目录未列单位 | Coruscant 联合设计 GPU kernel 和 sparse tensor core，使不规则稀疏权重能够获得端到端推理收益。 |
| HLX: A Unified Pipelined Architecture for Optimized Performance of Hybrid Transformer-Mamba Language Models | MICRO 2025 | KAIST | HLX 为 Transformer-Mamba 混合模型统一 attention、state update 与 GEMM pipeline，减少架构切换空泡。 |
| Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving | MICRO 2025 | KAIST; Microsoft Research 等 | Pimba 用共享 state-update processing unit 和 MX 低精度算术支持 SSM、线性注意力及 Transformer 服务。 |
| MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving | MICRO 2025 | Seoul National University | MX+ 为 block 中的 outlier 扩展有效尾数，在接近 MXFP4 存储成本下提高低比特 serving 精度。 |
| ORCHES: Orchestrated Test-Time-Compute-based LLM Reasoning on Collaborative GPU-PIM Heterogeneous System | MICRO 2025 | MICRO 2025 官方目录未列单位 | ORCHES 在 GPU 与 PIM 间编排 test-time reasoning 的候选生成和验证，扩大推理计算预算而控制延迟。 |
| LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention | MICRO 2025 | MICRO 2025 官方目录未列单位 | LongSight 在 compute-enabled memory 中筛选 sparse attention token，降低长上下文 KV 向 GPU 搬运的带宽。 |
| MCBP: A Memory-Compute Efficient LLM Inference Accelerator Leveraging Bit-Slice-enabled Sparsity and Repetitiveness | MICRO 2025 | Tsinghua University 等 | MCBP 在 bit-slice 粒度利用稀疏性和重复性，同时减少 GEMM、权重访问与 KV cache 访问。 |

### 数据系统、RAG 与外部记忆

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| AlayaDB: The Data Foundation for Efficient and Effective Long-context LLM Inference | arXiv 预印本, 2025 | AlayaDB AI; Hong Kong Polytechnic University 等 | AlayaDB 将 KV cache、稀疏 attention 与查询优化封装为向量数据库，把长上下文推理转化为数据系统查询规划问题。 |
| VectorLiteRAG: An Adaptive Vector Index Partitioning Scheme for Low-Latency RAG Pipeline | arXiv 预印本, 2025 | 作者公开稿未列单位 | VectorLiteRAG 根据索引访问偏斜动态在 CPU 与 GPU 间放置向量分区，并联动 LLM batch 控制端到端 TTFT。 |
| RAG-Stack: Co-Optimizing RAG Quality and Performance From the Vector Database Perspective | arXiv 预印本, 2025 | 作者公开稿未列单位 | RAG-Stack 以统一 IR、成本模型和计划搜索联合优化检索配置、系统性能与生成质量。 |

### 2026 最新部署、广域推理与数值格式

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| WANSpec: Leveraging Global Compute Capacity for LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | WANSpec 将 speculative draft 分发到低负载区域或本地算力，并用冗余控制广域网抖动带来的延迟风险。 |
| LLM Zeroth-Order Fine-Tuning is an Inference Workload | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 zeroth-order 微调的重复 forward scoring 重构为 serving workload，使 adapter 更新可复用推理 runtime。 |
| Fine-Tuning and Serving Gemma 4 31B on Google Cloud TPU: A Technical Comparison with GPU Baselines | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作给出从 JAX/Tunix 微调到 vLLM-TPU serving 的完整路径，并在统一配置下比较 TPU 与 H100 的成本和延迟。 |
| Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作在 MI325X 上比较 MLA、GQA、MoE 和多模态模型，说明 AITER、KV offload 与 block size 必须按架构选择。 |
| MX-SAFE: Versatile Inference- and Training-Proof Microscaling Format with On-the-Fly Exponent and Mantissa Bit Allocation | arXiv 预印本, 2026 | 作者公开稿未列单位 | MX-SAFE 在线切换 exponent/mantissa 分配模式，使同一 microscaling 格式同时适应训练和直接量化推理。 |

## 2026-06-12 第五轮追加：操作系统、云、网络与 HPC 推理基础设施

### EuroSys 2025：状态恢复、模型复用与跨云服务

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | SpInfer 将低层非结构稀疏性映射到 GPU kernel 和数据布局，使稀疏 LLM 的理论压缩转化为实际推理加速。 |
| Fast State Restoration in LLM Serving with HCache | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | HCache 缓存并恢复模型服务的中间状态，降低实例迁移、抢占或恢复后的重复 prefill 成本。 |
| A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | Faro 在本地容器化推理集群中联合做 workload 预测、资源分配与 autoscaling，以维持多模型 SLO。 |
| SkyServe: Serving AI Models across Regions and Clouds with Spot Instances | EuroSys 2025 | University of California, Berkeley 等 | SkyServe 跨区域和多云使用 spot instance 部署模型，并在价格、可用性和服务延迟间动态迁移。 |
| Comprehensive Deadlock Prevention for GPU Collective Communication | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | 该工作系统化检测和预防 GPU collective 中由并发 stream、顺序和资源依赖产生的死锁。 |
| T-MAC: CPU Renaissance via Table Lookup for Low-Bit LLM Deployment on Edge | EuroSys 2025 | Microsoft Research Asia 等 | T-MAC 用查表替代低比特矩阵乘的乘加路径，使 CPU 和边缘设备能够高效执行量化 LLM。 |
| DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | DeltaZip 只存储和加载相对基础模型的压缩参数增量，以较低显存成本服务大量全量微调模型。 |
| Stateful Large Language Model Serving with Pensieve | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | Pensieve 将会话 KV 和请求状态作为一等资源，在多轮 LLM 服务中联合管理迁移、复用和调度。 |
| Improving GPU Sharing Performance through Adaptive Bubbleless Spatial-Temporal Sharing | EuroSys 2025 | EuroSys 2025 官方目录未列单位 | 该工作在空间和时间两个维度自适应共享 GPU，并消除切换气泡，提高混合 AI workload 的利用率。 |

### SOSP 2025：可编程 Serving、KV 内存与生产可靠性

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference | SOSP 2025 | SOSP 2025 官方目录未列单位 | 该工作测量移动 SoC 中 CPU、GPU、NPU 和内存子系统对不同 LLM 阶段的适配程度。 |
| KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models | SOSP 2025 | Tsinghua University; ICT, CAS 等 | KTransformers 把活跃 expert、attention 与其他算子分配到 CPU/GPU，并用定制 kernel 提升本地 MoE 推理。 |
| LithOS: An Operating System for Efficient Machine Learning on GPUs | SOSP 2025 | SOSP 2025 官方目录未列单位 | LithOS 以操作系统抽象管理 GPU kernel、内存和并发执行，为多租户 ML workload 提供隔离与复用。 |
| Mycroft: Tracing Dependencies in Collective Communication Towards Reliable LLM Training | SOSP 2025 | SOSP 2025 官方目录未列单位 | Mycroft 跟踪 collective 操作之间的依赖，定位分布式大模型中的 hang、顺序错误和通信故障。 |
| PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications | SOSP 2025 | SOSP 2025 官方目录未列单位 | PrefillOnly 专门优化 embedding、reranking 和 prompt encoding 等只有 prefill、没有 decode 的 LLM 应用。 |
| Pie: A Programmable Serving System for Emerging LLM Applications | SOSP 2025 | SOSP 2025 官方目录未列单位 | Pie 允许应用表达多阶段生成、工具调用和状态依赖，由可编程 runtime 统一调度。 |
| Mercury: Unlocking Multi-GPU Operator Optimization for LLMs via Remote Memory Scheduling | SOSP 2025 | SOSP 2025 官方目录未列单位 | Mercury 把远程 GPU 内存纳入 operator 调度，使单个算子可跨 GPU 利用空闲容量和带宽。 |
| HedraRAG: Co-Optimizing Generation and Retrieval for Heterogeneous RAG Workflows | SOSP 2025 | SOSP 2025 官方目录未列单位 | HedraRAG 联合优化检索器、生成器与异构硬件分配，避免分别优化 RAG 两阶段造成资源失衡。 |
| Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters | SOSP 2025 | SOSP 2025 官方目录未列单位 | Sailor 自动选择并调整跨区域异构集群的并行和通信计划，其动态规划方法也适用于广域推理。 |
| Robust LLM Training Infrastructure at ByteDance | SOSP 2025 | ByteDance | 该工作总结字节跳动大模型基础设施中的故障检测、恢复、网络与作业治理经验。 |
| PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation | SOSP 2025 | SOSP 2025 官方目录未列单位 | PhoenixOS 在操作系统层并发执行 GPU checkpoint/restore，并通过验证式推测减少暂停时间。 |
| Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market | SOSP 2025 | Alibaba Group 等 | Aegaeon 通过细粒度 GPU pooling 和模型复用服务长尾模型市场，降低每个模型独占设备的成本。 |
| IC-Cache: Efficient Large Language Model Serving via In-context Caching | SOSP 2025 | SOSP 2025 官方目录未列单位 | IC-Cache 缓存并组合可复用的 in-context computation，减少 few-shot、RAG 和 agent prompt 的重复 prefill。 |
| Jenga: Effective Memory Management for Serving LLM with Heterogeneity | SOSP 2025 | SOSP 2025 官方目录未列单位 | Jenga 在不同容量、带宽和互连的设备间联合管理权重与 KV，适配异构 serving 集群。 |
| DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction | SOSP 2025 | SOSP 2025 官方目录未列单位 | DiffKV 按请求和 KV 生命周期采用差异化内存策略，并并行压紧 cache 以缓解碎片。 |
| Oasis: Pooling PCIe Devices Over CXL to Boost Utilization | SOSP 2025 | SOSP 2025 官方目录未列单位 | Oasis 通过 CXL 池化 GPU、SSD 和 NIC 等 PCIe 设备，为弹性 AI 集群提供可组合硬件资源。 |

### SoCC 2025：多租户、推测解码与异构云

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| DyOrc: Efficient Serving of Dynamic Machine Learning Workflows | SoCC 2025 | SoCC 2025 官方目录未列单位 | DyOrc 将动态 ML workflow 的依赖、分支和资源变化纳入服务编排，而非只调度独立模型请求。 |
| Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving | SoCC 2025 | SoCC 2025 官方目录未列单位 | Oneiros 通过参数重映射提高不同 tenant 间 KV cache 的兼容和复用能力。 |
| Symbiosis: Multi-Adapter Inference and Fine-Tuning | SoCC 2025 | SoCC 2025 官方目录未列单位 | Symbiosis 在共享基础模型上协同执行多 adapter 推理和微调，减少参数副本与资源冲突。 |
| AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving | SoCC 2025 | SoCC 2025 官方目录未列单位 | AdaSpec 根据请求 SLO、草稿成本和接受率动态选择 speculative decoding 配置。 |
| Multiplexed Heterogeneous LLM Serving via Stage-Aligned Parallelism | SoCC 2025 | SoCC 2025 官方目录未列单位 | 该工作按模型阶段对齐异构设备的并行与复用方式，避免 prefill/decode 在不同硬件上的能力错配。 |
| THORN-ML: Transparent Hardware Offloaded Resilient Networks for RDMA based Distributed ML Workloads | SoCC 2025 | SoCC 2025 官方目录未列单位 | THORN-ML 将故障检测和恢复逻辑下沉到网络硬件，提高 RDMA 大模型作业的透明容错能力。 |
| ZipBatch: Multi-Tenant GPU Batching with Dual-Resource Regulation | SoCC 2025 | SoCC 2025 官方目录未列单位 | ZipBatch 同时约束计算和内存两类资源，将不同 tenant 请求组合为稳定高效的 GPU batch。 |
| Rethinking Web Cache Design for the AI Era | SoCC 2025 | SoCC 2025 官方目录未列单位 | 该工作重新审视 AI agent 与生成内容对传统 Web cache 的对象、更新和一致性语义。 |
| Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment | SoCC 2025 | SoCC 2025 官方目录未列单位 | Cauchy 在不同 GPU 类型和云实例间动态放置模型，根据负载变化降低满足 SLO 的成本。 |

### SIGCOMM 2025：AI 集群网络、KV 通信与 Collective

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Astral: A Datacenter Infrastructure for Large Language Model Training at Scale | SIGCOMM 2025 | ByteDance 等 | Astral 从拓扑、流量控制和作业编排层构建超大规模 LLM 集群网络，为推理集群提供生产级网络设计参照。 |
| HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference | SIGCOMM 2025 | Clemson University; Microsoft Research; Harvard University 等 | HACK 在压缩域直接执行可同态处理的 attention 运算，减少 PD 分离时 KV 传输和反复解压开销。 |
| SkeletonHunter: Diagnosing and Localizing Network Failures in Containerized Large Model Training | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | SkeletonHunter 从容器化大模型作业中提取通信骨架，定位网络故障和异常链路。 |
| SyCCL: Exploiting Symmetry for Efficient Collective Communication Scheduling | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | SyCCL 利用拓扑和 collective 的对称性缩小调度搜索空间，自动生成高效通信计划。 |
| Vedrfolnir: RDMA Network Performance Anomalies Diagnosis in Collective Communications | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | Vedrfolnir 关联 RDMA telemetry 与 collective 行为，诊断分布式 AI 集群的尾延迟和性能异常。 |
| ByteScale: Communication-Efficient Scaling of LLM Training with a 2048K Context Length on 16384 GPUs | SIGCOMM 2025 | ByteDance | ByteScale 为超长上下文训练优化并行、通信与负载均衡，其集群网络机制可迁移到大规模 prefill。 |
| MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | MixNet 根据 MoE 动态 all-to-all 流量重配置光电混合 fabric，缓解 expert routing 热点。 |
| ResCCL: Resource-Efficient Scheduling for Collective Communication | SIGCOMM 2025 | SIGCOMM 2025 官方目录未列单位 | ResCCL 联合考虑链路和 GPU/CPU 资源，降低 collective 与计算竞争造成的端到端减速。 |
| ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud | SIGCOMM 2025 | ByteDance | Jakiro 在 VPC 中统一支持 RDMA 和 TCP，使云端 AI workload 获得高性能且可隔离的网络。 |
| Alibaba Stellar: A New Generation RDMA Network for Cloud AI | SIGCOMM 2025 | Alibaba Cloud | Stellar 针对云 AI 集群重构 RDMA 网络的可靠性、拥塞控制和多租户隔离。 |

### SC 2025：HPC Serving、Kernel 与可靠性

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling | SC 2025 | SC 2025 官方目录未列单位 | gLLM 用全局平衡 pipeline 和 token throttling 控制阶段间流速，减少分布式 serving 的空泡和拥塞。 |
| A Streaming Collectives Interface Targeting Dataflow Acceleration and HPC Workloads | SC 2025 | SC 2025 官方目录未列单位 | 该工作提供 streaming collective 接口，使通信能够与细粒度 dataflow 和 kernel pipeline 重叠。 |
| LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving | SC 2025 | SC 2025 官方目录未列单位 | LiquidGEMM 针对 W4A8 推理设计硬件高效的反量化、数据布局和 GEMM kernel。 |
| HELM: Characterizing Unified Memory Accesses to Improve GPU Performance under Memory Oversubscription | SC 2025 | SC 2025 官方目录未列单位 | HELM 刻画统一内存超配时的访问与迁移行为，为超出 HBM 容量的模型部署提供优化依据。 |
| SDR-RDMA: Software-Defined Reliability Architecture for Planetary Scale RDMA Communication | SC 2025 | SC 2025 官方目录未列单位 | SDR-RDMA 将可靠性策略软件定义化，以支撑跨地域超大规模 RDMA 通信。 |
| Diff-MoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching | SC 2025 | SC 2025 官方目录未列单位 | Diff-MoE 根据 expert 优先级采用差异化缓存，并面向 batch 复用热点 expert。 |
| MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving | SC 2025 | SC 2025 官方目录未列单位 | MaverIQ 用 workload fingerprint 预测资源需求，并以碎片感知的分层配置实现 intent-based serving。 |
| Fine-grained Automated Failure Management for Extreme-Scale GPU Accelerated Systems | SC 2025 | SC 2025 官方目录未列单位 | 该工作自动定位并隔离极大 GPU 系统中的细粒度故障，为长时间运行的推理集群提供可靠性参考。 |

### USENIX ATC 2024：KV、Serverless 与异构加速器

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Cost-Efficient Large Language Model Serving for Multi-turn Conversations with CachedAttention | USENIX ATC 2024 | National University of Singapore; Shanghai Jiao Tong University; Huawei Cloud | CachedAttention 维护分层 KV cache，并用 layer-wise preload、异步保存和 scheduler-aware 淘汰降低多轮会话 TTFT。 |
| StreamBox: A Lightweight GPU SandBox for Serverless Inference Workflow | USENIX ATC 2024 | Huazhong University of Science and Technology; Inria | StreamBox 用 stream 级 sandbox、自动伸缩显存和跨 function GPU 通信降低 serverless inference 的启动与隔离开销。 |
| Power-aware Deep Learning Model Serving with μ-Serve | USENIX ATC 2024 | University of Illinois Urbana-Champaign; IBM Research | μ-Serve 联合优化模型复用和 GPU frequency scaling，在维持吞吐或延迟 SLO 时降低集群功耗。 |
| Harmonizing Efficiency and Practicability: Optimizing Resource Utilization in Serverless Computing with Jiagu | USENIX ATC 2024 | Shanghai Jiao Tong University; Huawei Cloud; EPFL | Jiagu 用 pre-decision scheduling 与 dual-staged scaling 提高 serverless 部署密度并降低冷启动。 |
| Starburst: A Cost-aware Scheduler for Hybrid Cloud | USENIX ATC 2024 | UC Berkeley; UC Santa Barbara | Starburst 通过可配置等待预算在私有集群与公有云间调度作业，优化云成本和 JCT。 |
| PUZZLE: Efficiently Aligning Large Language Models through Light-Weight Context Switch | USENIX ATC 2024 | Tsinghua University | PUZZLE 根据模型和阶段相似性降低 RLHF 多模型 workload 的上下文切换与参数迁移开销。 |

### 已形成工业基础的奠基 Runtime、MoE 与通信工作

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism | arXiv 预印本, 2019 | NVIDIA | Megatron-LM 建立 tensor model parallel 的核心拆分方法，后续成为训练和推理 runtime 的基础。 |
| TurboTransformers: An Efficient GPU Serving System for Transformer Models | PPoPP 2021 | Tencent; Peking University | TurboTransformers 用动态 batch、序列长度感知调度和融合 kernel 加速早期 Transformer 在线服务。 |
| LightSeq: A High Performance Inference Library for Transformers | NAACL 2021 System Demonstrations | ByteDance | LightSeq 通过 layer fusion、定制 CUDA kernel 和显存复用提供 Transformer 推理库。 |
| DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale | ICML 2022 | Microsoft | DeepSpeed-MoE 联合优化 expert parallel、通信和模型压缩，使大规模 MoE 同时具备训练和推理可行性。 |
| FasterMoE: Modeling and Optimizing Training of Large-Scale Dynamic Pre-Trained Models | PPoPP 2022 | Tsinghua University 等 | FasterMoE 用 shadowing、smart scheduling 和 topology-aware communication 缓解 MoE expert 负载不均。 |
| DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale | SC 2022 | Microsoft | DeepSpeed Inference 通过 inference-adapted parallelism、kernel injection 和量化部署超大 Transformer。 |
| MegaBlocks: Efficient Sparse Training with Mixture-of-Experts | MLSys 2023 | Stanford University; Google 等 | MegaBlocks 把动态 token routing 转化为 block-sparse operation，避免 expert capacity padding；其 kernel 思路影响 MoE inference。 |
| Tutel: Adaptive Mixture-of-Experts at Scale | MLSys 2023 | Microsoft Research Asia 等 | Tutel 以自适应并行、all-to-all 和 fused kernel 构建通用 MoE runtime。 |

### RAG 所依赖的向量检索与数据库基础

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| Billion-scale Similarity Search with GPUs | IEEE Big Data 2017 | Meta AI Research | Faiss 用 GPU k-selection、量化和倒排索引建立十亿级向量检索基础，成为大量 RAG 系统的底层库。 |
| Accelerating Large-Scale Inference with Anisotropic Vector Quantization | ICML 2020 | Google Research | ScaNN 用 anisotropic vector quantization 优先保留与最大内积相关的误差方向，提高 ANN 的速度和召回率。 |
| DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node | NeurIPS 2019 | Microsoft Research India | DiskANN 用 SSD-resident graph、内存导航结构和 beam search 在单机上支持十亿级低延迟 ANN。 |
| Milvus: A Purpose-Built Vector Data Management System | SIGMOD 2021 | Zilliz | Milvus 将索引、segment、计算节点和存储节点解耦，建立面向向量数据的分布式数据库架构。 |
| Manu: A Cloud Native Vector Database Management System | PVLDB 2022 | Zilliz | Manu 以 log-as-data、云原生组件和时间戳一致性支持弹性向量数据库服务。 |
| VBASE: Unifying Online Vector Similarity Search and Relational Queries via Relaxed Monotonicity | OSDI 2023 | University of Wisconsin-Madison; Microsoft Research 等 | VBASE 通过 relaxed monotonicity 将 ANN 与关系过滤和查询优化统一，减少 RAG 检索与数据库查询的割裂。 |
| SPFresh: Incremental In-Place Update for Billion-Scale Vector Search | SOSP 2023 | Microsoft Research | SPFresh 以 LIRE 和增量原地更新维持动态向量索引，避免频繁全量重建。 |
| CAGRA: Highly Parallel Graph Construction and Approximate Nearest Neighbor Search for GPUs | ICDE 2024 | NVIDIA | CAGRA 以 GPU 并行图构建和搜索支撑高吞吐 ANN，并进入 RAPIDS cuVS 向量检索栈。 |

## 2026-06-18 追加：最新 KV、调度与容错系统

| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |
|---|---|---|---|
| CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents | arXiv 预印本, 2026 | 作者公开稿未列单位 | CacheWise 将 coding agent 的前缀复用与 tool-call 元数据结合做复用感知驱逐和前缀感知调度，显著降低 KV eviction 并缩短会话完成时间。 |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | Beyond Prediction 用分布感知而非长度预测的调度与 cache-aware preemption 联合优化在线 LLM serving 的 TTFT 和尾延迟。 |
| Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Bifrost 将线性层密文卸载到加速器、把非线性与 KV 状态更新留在 CPU TEE 中，构建 TEE 加 FHE 的混合隐私推理路径。 |
| Can I Buy Your KV Cache? | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把热门文档的预填充 KV 视作可交易的 provider-side 资产，用服务端复用替代重复 prefill。 |
| Communication-Efficient Verifiable Attention for LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | VeriAttn 用 TEE 验证、GPU 执行 attention，并按 prefill/decode 两阶段减少验证与 KV 传输开销。 |
| Coordinated Scheduling for MoE LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Gimbal 联合前端 DP-engine 调度与后端 expert 放置，按 KV 压力、prefill 余量和 expert 热点协调 MoE serving。 |
| ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories | arXiv 预印本, 2026 | 作者公开稿未列单位 | ITME 用 CXL 混合远端内存把 TB 级共享上下文层做成字节寻址扩展，并主动分层搬运权重与 prefix cache。 |
| KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing | arXiv 预印本, 2026 | 作者公开稿未列单位 | KVEraser 用学习式 steering state 只改被删除跨度的 KV 区间，在不重算整段 suffix 的前提下做局部上下文擦除。 |
| LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | LUMEN 把分布式 LLM serving 的故障恢复建模为 checkpoint 放置、请求重分配和 reload 期间容量恢复的联合负载协调问题。 |
| MiniPIC: Flexible Position-Independent Caching in <100LOC | arXiv 预印本, 2026 | 作者公开稿未列单位 | MiniPIC 在 vLLM 中以未旋转 K cache 和少量用户侧 primitive 实现位置无关缓存，并与 CPU offload 共存。 |
| Models Take Notes at Prefill: KV Cache Can Be Editable and Composable | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 KV cache 视作可编辑、可组合的“笔记本”，支持附加勘误与 RoPE 重定位拼接来复用预填充结果。 |
| OTRO: Oblivious Tokenization Path with Square-Root ORAM | arXiv 预印本, 2026 | 作者公开稿未列单位 | OTRO 用 square-root ORAM 副本池、epoch 轮转和 KV-aware 重建重叠，把 tokenizer 侧信道防护开销压到接近生产可用。 |
| PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression | arXiv 预印本, 2026 | 作者公开稿未列单位 | PolyKV 在层级粒度上联合选择 KV 压缩策略和预算分配，用异构保留方案替代统一 cache budget。 |
| Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作按 Prefill/Decode 两阶段分别测 TTFT、TPOT 和批量吞吐，比较 GPU 与新型 AI 加速器的相位优势。 |
| A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference | arXiv 预印本, 2026 | 作者公开稿未列单位 | ST-MoE 利用跨层和跨 token 的 expert 激活相关性做时空联合预取，以重叠 expert 加载和 MoE 推理计算。 |
| AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor | arXiv 预印本, 2026 | 作者公开稿未列单位 | AnchorKV 在 KV 压缩保留分数中引入 refusal anchor 的软惩罚，使压缩后的长上下文推理兼顾内存节省与安全对齐。 |
| Dual Dimensionality for Local and Global Attention | arXiv 预印本, 2026 | 作者公开稿未列单位 | Dual Dimensionality 用近邻 token 全维、远距 token 低维的 DAR 表示降低长程 KV 容量，同时保持局部预测精度。 |
| Efficient On-Device Diffusion LLM Inference with Mobile NPU | arXiv 预印本, 2026 | 作者公开稿未列单位 | llada.cpp 通过多块推测解码、渐进式修正与 swap 优化运行时，把 diffusion LLM 对齐到手机 NPU 的执行特性。 |
| EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts | arXiv 预印本, 2026 | 作者公开稿未列单位 | EfficientRollout 为 RL rollout 设计自推测解码和系统感知开关策略，在活跃 batch 缩小时继续利用并行验证加速。 |
| From Tokens to Energy Flexibility: Quantization-Enabled Demand Response for Data Centers with LLM Inference Workloads | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把量化配置映射为可调度功率参数，并将 routing、实例切换与精度选择纳入推理数据中心的需求响应优化。 |
| JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting | arXiv 预印本, 2026 | 作者公开稿未列单位 | JetFlow 用单次前向的并行 draft head 生成具因果一致性的候选树，突破 speculative decoding 在更大 draft budget 下的扩展瓶颈。 |
| Latency Prediction for LLM Inference on NPU Systems | arXiv 预印本, 2026 | 作者公开稿未列单位 | LENS 只用少量端到端 profile 即可建模 NPU 上由 compiler 和 bucketing 引起的非线性推理时延。 |
| AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | AGENTSERVESIM 用 program orchestration、tool gap 模拟、session-aware routing 和 KV residency 模型，在 CPU 上逼真评估多轮 agent serving 策略。 |
| Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作用 stream-loading prefill、SmallEP、零拷贝 prefill/decode 分离和 CPU FP8 kernel，把本地 CPU-GPU 平台上的 MoE serving 拉近云端 SLO。 |
| Accelerating Speculative Diffusions via Block Verification | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把 LLM speculative decoding 的 block verification 扩展到 diffusion 采样，在无需额外训练的前提下提升 draft acceptance 和生成速度。 |
| ConSA: Controllable Sparsity in Hybrid Attention via Learnable Allocation | arXiv 预印本, 2026 | 作者公开稿未列单位 | ConSA 通过可学习的 FA/SWA 分配和稀疏度约束，为混合注意力模型学习层级或 KV-head 级的推理友好稀疏布局。 |
| Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents | arXiv 预印本, 2026 | 作者公开稿未列单位 | FCGraft 复用函数级代码骨架及其 KV cache，通过 stitching 和 patching 减少 embodied agent 代码策略生成中的重复 prefill。 |
| Image Prompt Reconstruction Attacks on Distributed MLLM Inference Frameworks | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作揭示分布式 MLLM 推理中间 embedding 可泄露图像提示，并通过黑盒重建攻击量化多模态推理框架的隐私风险。 |
| Agentic AI Workload Characteristics | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作用端到端 tracing 刻画 ReAct 类 agent workload，指出有效上下文缓存会让执行转向 decode-dominated 且依赖长寿命 KV 状态。 |
| Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作用 GEMM 维度统一重组 LLM pruning 设计空间，比较不同剪枝族在真实内核与硬件上的实际推理加速边界。 |
| Fast MoE Inference via Predictive Prefetching and Expert Replication | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作预测热点 expert 并做动态复制和预取，以减少稀疏激活造成的等待和 GPU 空转。 |
| KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | KAIROS 以 agent 上下文为控制信号，联合调节 GPU 频率、并发度与跨实例放置，在避免 thrashing 的前提下降低 agentic serving 功耗。 |
| MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs | arXiv 预印本, 2026 | 作者公开稿未列单位 | MemExplorer 联合搜索异构 NPU 与多级内存配置，在 agentic inference 的 prefill/decode 场景下平衡吞吐与功耗。 |
| Multi-Segment Attention: Enabling Efficient KV-Cache Management for Faster Large Language Model Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | AsymCache 通过 Multi-Segment Attention、位置感知驱逐与自适应 chunking，让 lossless KV 管理与 GPU attention kernel 的效率目标对齐。 |
| Observation, Not Prediction: Conversation-Level Disaggregated Scheduling for Agentic Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | ConServe 将调度单位从单 turn 提升到整段 conversation，用首轮输入长度和 KV 占用等可观测量替代 decode-side 预测。 |
| Parallel Context Compaction for Long-Horizon LLM Agent Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | 该工作把长程 agent 的上下文压缩拆成并行 block compaction，在相同压缩输出量下缩短阻塞式 summarization 带来的端到端时延。 |
| Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving | arXiv 预印本, 2026 | 作者公开稿未列单位 | Pythia 在 serving 层显式编码多 agent workflow 语义，用可预测拓扑结构改善 prefix cache、扩缩容与长上下文调度。 |
