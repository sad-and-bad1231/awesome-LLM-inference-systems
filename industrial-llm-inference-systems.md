# 工业界 LLM 推理系统方案追踪

<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->

更新时间：由 `data/industry.jsonl` 生成。

## 观察框架

- TTFT under Drift：基础设施漂移、广域网抖动、Spot 节点切换时的首 token 延迟恶化边界。
- Generation Stall Rate：推测解码验证失败、MoE all-to-all 热点或 tool-call 挂起造成的生成中断率。
- Numerical Reproducibility：低精度混合量化、scale search 和异构执行导致的数值不稳定与非确定性。

## 企业方案清单

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| NVIDIA | Dynamo | 2025 | 运行时；状态管理 | 分布式/分离式推理框架，组合 disaggregated serving、KV cache-aware routing、KV offloading，并用 NIXL 做低延迟 KV 传输。 | [primary](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) |
| NVIDIA | NIXL / KV cache transfer | 2025 | 状态管理；运行时 | 面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。 | [primary](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html) |
| NVIDIA | TensorRT-LLM KV cache reuse | 2025 | 运行时；状态管理 | 用 KV cache event API 和 KV-aware routing 提高 prefix/cache 命中，减少重复 prefill。 | [primary](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) |
| NVIDIA | TensorRT-LLM FP8/INT8 KV cache | 2024 | 压缩；算子 | MHA/MQA kernel 中支持 on-the-fly dequantize 的 FP8/INT8 KV cache，降低 decode 阶段读带宽。 | [primary](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html) |
| NVIDIA | NVFP4 KV cache | 2025 | 压缩；成本 | Blackwell 侧使用 4-bit KV 存储、attention 前解量化到 FP8，面向长上下文、大 batch、多 agent/MoE 降低 HBM 压力。 | [primary](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/) |
| NVIDIA | BlueField-4 STX / context memory storage | 2026 | 状态管理；硬件系统 | 用 DPU/加速存储绕过 host CPU，把长上下文 KV cache 放到近存储路径，面向 agentic AI 的大上下文状态。 | [primary](https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai) |
| NVIDIA + Georgia Tech | RocketKV | 2025 | 长上下文；压缩 | 两阶段 KV 压缩：先永久淘汰部分 prompt token，再做动态 top-k sparse attention。 | [primary](https://arxiv.org/abs/2502.14051) |
| NVIDIA Research + Georgia Tech | ThinKV | 2026 | 长 CoT；动态保留 | thought-adaptive KV cache compression，根据推理过程中的 thought 类型做保留、量化和逐级淘汰。 | [primary](https://openreview.net/forum?id=M3CeHnZKNC) |
| NVIDIA + University of Warsaw | KVTC | 2026 | 状态管理；压缩 | 把 KV cache 看成可压缩信号，用 transform coding、PCA 去相关、自适应量化和熵编码降低可复用 KV 存储。 | [primary](https://arxiv.org/abs/2511.01815) |
| ByteDance Seed | ShadowKV | 2025 | 长上下文；状态管理；压缩 | GPU 只保留低秩 keys、landmarks 和少量 outliers，values 放 CPU DRAM，decode 时按需召回 Top-K value。 | [primary](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference) |
| DeepSeek | MLA / Multi-head Latent Attention | 2024 | 压缩；模型结构 | 把 KV cache 压到 latent 向量，DeepSeek-V3/R1 系列用 MLA 降低 long-context decode 的 KV 内存和带宽。 | [primary](https://arxiv.org/abs/2412.19437) |
| DeepSeek | FlashMLA | 2025 | 算子；长上下文 | 面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。 | [primary](https://github.com/deepseek-ai/FlashMLA) |
| DeepSeek | DeepGEMM / DeepEP | 2025 | 算子；MoE 通信 | FP8 GEMM 与 MoE expert-parallel 通信库，支撑 DeepSeek 系列训练和推理的 dense/MoE fast path。 | [primary](https://flashmla.net/) |
| Google Cloud | JetStream + MaxText | 2024 | 运行时；TPU serving | 面向 XLA/TPU 的 throughput 和 memory optimized LLM inference engine，配合 MaxText 在 TPU/GKE 上服务 LLM。 | [primary](https://cloud.google.com/tpu/docs/tutorials/LLM/jetstream-maxtext-inference-v6e) |
| Google Research / DeepMind | TurboQuant | 2026 | 压缩；成本 | 通过随机旋转、近最优量化和 QJL 残差校正，面向 KV cache 和向量检索做低比特在线向量量化。 | [primary](https://arxiv.org/abs/2504.19874) |
| Google / TPU ecosystem | Ragged Paged Attention for TPU | 2026 | 算子；编译 | 面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。 | [primary](https://arxiv.org/abs/2604.15464) |
| Microsoft Research | Splitwise | 2024 | 运行时；成本 | 把 prompt computation 和 token generation 放在不同机器池，分别匹配 compute-bound 与 memory-bound 阶段。 | [primary](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) |
| Microsoft Research | DynamoLLM | 2025 | 运行时；成本 | 动态重配置 LLM inference cluster，在 SLO 下优化能耗和成本。 | [primary](https://www.microsoft.com/en-us/research/publication/dynamollm-designing-llm-inference-clusters-for-performance-and-energy-efficiency/) |
| Microsoft Research | RetroInfer / RetrievalAttention | 2025 | 长上下文；状态管理 | 把 KV cache 重新抽象成向量存储系统，在 CPU/GPU 间用 attention-aware index 召回关键 KV。 | [primary](https://www.microsoft.com/en-us/research/publication/retroinfer-a-vector-storage-engine-for-scalable-long-context-llm-inference/) |
| Microsoft Research | DroidSpeak | 2026 | 状态管理；多模型 serving | 在相同架构的 fine-tuned model variants 之间共享 KV cache，降低企业多模型/多 agent 的重复 prefill。 | [primary](https://www.microsoft.com/en-us/research/publication/droidspeak-kv-cache-sharing-for-efficient-multi-llm-serving/) |
| Microsoft Research | CacheBlend | 2025 | RAG；状态管理 | 复用 RAG cached knowledge 的 KV，并处理非前缀片段融合问题，减少长输入 prefill。 | [primary](https://www.microsoft.com/en-us/research/uploads/prod/2024/09/eurosys25-final999.pdf) |
| Meta / PyTorch | FlexAttention for inference | 2025 | 算子；编译 | 用 PyTorch API 表达 attention variants，经 torch.compile 降到 fused attention kernel，支持 inference/paged attention 方向。 | [primary](https://pytorch.org/blog/flexattention-for-inference/) |
| Meta | Scaling LLM inference: TP/CP/EP | 2025 | 运行时；并行 | 公开 Meta 在 tensor/context/expert parallelism 上扩展 LLM inference 的工程经验。 | [primary](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/) |
| PyTorch Foundation / vLLM community | vLLM V1 + torch.compile | 2025 | 运行时；编译 | vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。 | [primary](https://pytorch.org/projects/vllm/) |
| IBM Research | PagedAttention + FlexAttention / FMS | 2025 | 算子；长上下文 | 在 IBM Foundation Model Stack 中把 PagedAttention 与 FlexAttention 融合，处理 scattered KV gather。 | [primary](https://arxiv.org/abs/2506.07311) |
| IBM / Red Hat / llm-d | llm-d + LMCache + vLLM | 2025 | 运行时；状态管理 | Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。 | [primary](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes) |
| LMCache 社区 / 企业采用 | LMCache | 2025 | 状态管理；运行时 | 将 KV cache 抽成独立层，支持跨 engine/query 复用和 GPU/CPU/storage/network 多层编排。 | [primary](https://arxiv.org/abs/2510.09665) |
| Moonshot AI + Tsinghua | Mooncake | 2025 | 状态管理；运行时 | 以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。 | [primary](https://www.usenix.org/conference/fast25/presentation/qin) |
| Huawei | P/D-Serve | 2024 | 运行时；状态管理 | 在数万 xPU/NPU 规模上部署 prefill/decode disaggregated serving，做 P/D 组织、调度和 D2D KV transfer。 | [primary](https://arxiv.org/abs/2408.08147) |
| Huawei Cloud / Ascend | Ascend-vLLM prefix caching / KV offload | 2025 | 状态管理；运行时 | 在 Ascend NPU 上支持 prefix caching、KV cache CPU offload 和 Mooncake/LMCache 连接。 | [primary](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html) |
| Huawei | Unified Cache Manager, UCM | 2025 | 状态管理；多层内存 | 用分层 KV cache 管理缓解 HBM 受限环境下的推理吞吐/延迟问题。 | [primary](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-releases-new-tool-to-get-chinese-firms-around-crushing-hbm-export-blacklist-new-ucm-software-claims-up-to-22x-throughput-gain-and-90-percent-latency-reduction-for-traditional-cache-hierarchies-in-ai-workloads) |
| Alibaba Cloud | FlowKV | 2025 | 运行时；KV 传输 | 在 PD 分离式架构中优化 KV cache transfer，并做 load-aware scheduling。 | [primary](https://arxiv.org/abs/2504.03775) |
| Alibaba Group | Aegaeon | 2025 | 长尾模型市场；GPU pooling | 在共享 GPU 池中复用模型和显存，避免 marketplace 中大量低流量模型各自独占设备。 | [primary](https://dblp.org/db/conf/sosp/sosp2025.html) |
| Alibaba Cloud | BladeLLM | 2025 | 运行时；产品化 | PAI 上的高性能 LLM inference engine，用于低延迟、高吞吐部署 Qwen 等模型。 | [primary](https://www.alibabacloud.com/help/doc-detail/2865199.html) |
| Alibaba Cloud Tair | Tair-KVCache-HiSim | 2026 | 状态管理；仿真 | 面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。 | [primary](https://www.alibabacloud.com/blog/603164) |
| Samsung Research | LookaheadKV | 2026 | 长上下文；动态淘汰 | 不生成未来草稿，训练轻量模块预测未来重要性分布以指导 KV cache eviction。 | [primary](https://research.samsung.com/research-papers/LookaheadKV-Fast-and-Accurate-KV-Cache-Eviction-by-Glimpsing-into-the-Future-without-Generation) |
| Adobe Research | Cache-Craft | 2025 | RAG；状态管理 | 管理 RAG chunk-caches，通过少量重计算修复位置问题，实现 chunk KV cache 复用。 | [primary](https://arxiv.org/abs/2502.15734) |
| OpenAI / Triton ecosystem | Triton language and kernels in inference stacks | 2024 | 算子；编译 | 工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。 | [primary](https://triton-lang.org/) |
| FlashInfer 社区 | FlashInfer | 2025 | 算子；serving kernel | 面向 LLM serving 的可定制 attention engine，支持 paged KV、decode/prefill kernel、与多 runtime 集成。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/file/dbf02b21d77409a2db30e56866a8ab3a-Paper-Conference.pdf) |
| Cerebras | 高速推理 API / Llama API 合作 | 2025 | 成本；硬件 serving | 用 wafer-scale engine 做极高 token/s 推理，Meta Llama API 等使用其高速推理能力。 | [primary](https://www.cerebras.ai/) |
| NVIDIA | Full-Stack Optimizations for Agentic Inference with Dynamo | 2026 | 运行时；状态管理 | 针对 coding agent / multi-agent 的 write-once-read-many KV 模式，强调 router、cache pinning、ephemeral KV block 生命周期和 agent-native KV 管理。 | [primary](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/) |
| NVIDIA | Dynamo 1.0 Production-Scale Multi-Node Inference | 2026 | 运行时；Kubernetes；状态管理 | Dynamo 1.0 强化多节点部署、Kubernetes 编排、agentic/multimodal KV routing、ModelExpress 快速启动和 KV Block Manager。 | [primary](https://developer.nvidia.com/blog/?p=113961) |
| NVIDIA | Dynamo Snapshot | 2026 | 运行时；冷启动 | 用 CRIU + cuda-checkpoint 做 Kubernetes 上推理 worker 快照恢复，并通过 KV cache unmap 减小 checkpoint 体积。 | [primary](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/) |
| NVIDIA | NIXL / Inference Transfer Library | 2026 | KV 传输；网络 | 非阻塞传输 API 和动态元数据交换，覆盖 disaggregated KV movement、long-context storage、weight transfer 和 expert parallelism。 | [primary](https://developer.nvidia.com/blog/?p=113426) |
| NVIDIA | Dynamo KVBM | 2026 | 状态管理；分层 KV | KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。 | [primary](https://docs.dynamo.nvidia.com/dynamo/components/kvbm) |
| Tencent Cloud TACO + NVIDIA | FlexKV | 2026 | 状态管理；多层 KV | 分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。 | [primary](https://github.com/taco-project/FlexKV) |
| ByteDance | InfiniStore | 2025 | 状态管理；KV store | 高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。 | [primary](https://github.com/bytedance/InfiniStore) |
| Moonshot / Mooncake / vLLM | vLLM x Mooncake Store | 2026 | 状态管理；agentic serving | 将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。 | [primary](https://vllm.ai/blog/2026-05-06-mooncake-store) |
| Moonshot / PyTorch | Mooncake Joins PyTorch Ecosystem | 2026 | 生态；KV 传输 | Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。 | [primary](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) |
| Novita AI + vLLM | PegaFlow External KV Cache | 2026 | 状态管理；外部 KV 服务 | PegaFlow 作为 Rust standalone external KV cache service 通过 vLLM connector 接入，面向生产级外部 KV cache。 | [primary](https://vllm.ai/blog/2026-05-18-pegaflow) |
| vLLM | KV Offloading Connector | 2026 | 状态管理；运行时 | vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。 | [primary](https://vllm.ai/blog/kv-offloading-connector) |
| llm-d | llm-d KV Cache | 2026 | Kubernetes；KV-aware routing | 用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。 | [primary](https://github.com/llm-d/llm-d-kv-cache) |
| IBM / Red Hat / Google 等 | UCCL | 2026 | 网络；KV transfer | GPU 通信库，覆盖 collectives、P2P KV cache transfer、RL weight transfer 和 expert parallelism，进入 llm-d 分布式推理栈。 | [primary](https://github.com/uccl-project/uccl) |
| Dell + NVIDIA + LMCache/vLLM | RDMA-Accelerated KV Cache Storage Offload | 2026 | 状态管理；存储 | 将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。 | [primary](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/) |
| KServe | KV Cache Offloading | 2025 | Kubernetes；运行时 | 在 KServe generative inference 中集成 LMCache/vLLM KV offloading，面向云原生模型服务。 | [primary](https://kserve.github.io/website/docs/model-serving/generative-inference/kvcache-offloading) |
| LMCache 社区 | LMCache Operator | 2026 | Kubernetes；状态管理 | 首个 Kubernetes Operator 将 `LMCacheEngine` CRD 编排为与 vLLM worker 共置的 LMCache MP DaemonSet、Service、ConfigMap 和 Secret，并加入 RESP L2 backend、AMD GPU 支持与端到端 smoke tests。 | [primary](https://github.com/LMCache/LMCache/releases/tag/operator-v0.1.1) |
| Microsoft Research | Memento | 2026 | 长 CoT；状态压缩 | 训练模型把 CoT block 压成 dense memento，释放已经完成推理块的 KV，提升 reasoning serving 吞吐。 | [primary](https://www.microsoft.com/en-us/research/articles/memento-teaching-llms-to-manage-their-own-context/) |
| Microsoft Research | Medha | 2025 | 长上下文；运行时 | 用 adaptive prefill chunking、Sequence Pipeline Parallelism、KV-Cache Parallelism 和 input-length-aware scheduling 支撑千万 token 精确推理。 | [primary](https://www.microsoft.com/en-us/research/publication/medha-efficient-llm-inference-on-multi-million-context-lengths-without-approximation/) |
| Microsoft Research | SPIN | 2026 | sparse attention；分层 KV | 把 sparse attention execution pipeline 与 CPU/GPU hierarchical KV storage 联合设计，解决不规则 KV subset 检索开销。 | [primary](https://www.microsoft.com/en-us/research/publication/unifying-sparse-attention-with-hierarchical-memory-for-scalable-long-context-llm-serving/) |
| Microsoft Research | KEEP | 2026 | 长程记忆；KV memory | Embodied planning 中用 KV-cache-centric memory management 替代原始文本记忆，减少频繁 KV 更新和重算。 | [primary](https://www.microsoft.com/en-us/research/publication/keep-a-kv-cache-centric-memory-management-system-for-efficient-embodied-planning/) |
| Microsoft Research | Online Scheduling with KV Cache Constraints | 2025 | 运行时；理论调度 | 将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。 | [primary](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/) |
| DeepSeek | DeepSeek-V3.2 / DeepSeek Sparse Attention | 2025 | 模型结构；长上下文成本 | 在模型架构中加入 sparse attention/indexer，目标是在长上下文和 reasoning/agent 任务中降低推理成本。 | [primary](https://arxiv.org/abs/2512.02556) |
| Google / DeepSeek 相关研究 | Perfect Recall, Parallel Efficiency: MLA for Million-Token Decoding | 2026 | MLA；分布式长上下文 | 分析 DSA/MLA 在百万 token 分布式 decoding 中的全局 Top-K 同步瓶颈，并探索并行高效的精确召回路线。 | [primary](https://www.microsoft.com/en-us/research/publication/perfect-recall-parallel-efficiency-multi-head-latent-attention-for-million-token-context-decoding/) |
| UC/industry collaboration | SYMPHONY | 2026 | compute-memory disaggregation | NSDI 2026 工作，将 KV cache storage 从 compute 解耦，形成满足严格延迟的 disaggregated memory management layer。 | [primary](https://www.usenix.org/conference/nsdi26/presentation/agarwal) |
| vLLM / Mooncake ecosystem | MooncakeStoreConnector | 2026 | 外部 KV store；vLLM | vLLM 文档化 MooncakeStoreConnector，支持 embedded 和 standalone-store 模式，扩展 CPU/SSD KV pool。 | [primary](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/) |
| Apple / academic collaboration | SAW-INT4 | 2026 | 4-bit KV；系统感知量化 | 面向真实 serving 约束设计 4-bit KV cache quantization，考虑 paged layout、规则访存和 fused attention。 | [primary](https://arxiv.org/abs/2604.19157) |
| KVServe Team | KVServe | 2026 | KV 通信压缩；PD serving | 在分离式 LLM serving 中根据 workload、网络和 SLO 在线选择 KV compression profile，面向通信瓶颈。 | [primary](https://arxiv.org/abs/2605.13734) |
| University/industry collaboration | Tutti | 2026 | SSD-backed KV | 让 SSD-backed KV cache 接近 DRAM-backed LMCache 的性能，扩大长上下文服务的低成本 KV 容量。 | [primary](https://arxiv.org/abs/2605.03375) |
| Alibaba Group | RTP-LLM | 2026 | 生产 runtime；PD 分离；多层 KV；量化 | 将并行加载、PD 分离、分层 KV 复用、模块化推测解码、自适应 KV 量化和多模态解耦整合进生产引擎，论文称已服务超过一亿用户。 | [primary](https://arxiv.org/abs/2605.29639) |
| Ant Group + vLLM 社区 | vLLM-Omni | 2026 | 多模态 serving；stage disaggregation | 用 stage graph 拆分 LLM、扩散模型和编码器，各阶段独立批处理、分配 GPU，并通过统一 connector 传递中间状态。 | [primary](https://arxiv.org/abs/2602.02204) |
| ByteDance Seed | MegaScale-Infer | 2025 | MoE serving；专家解耦 | 将 attention 和 MoE FFN 分池部署，以 disaggregated expert parallelism、ping-pong pipeline 和 M2N 通信提升专家利用率。 | [primary](https://arxiv.org/abs/2504.02263) |
| ByteDance Seed | SwiftSpec | 2025 | 推测解码；低延迟 | 异步扩展 draft/target 执行，配合 tree-aware KV 管理和 fused kernel，面向交互式单请求降低解码延迟。 | [primary](https://arxiv.org/abs/2506.11309) |
| Microsoft Research | MagicDec | 2025 | 长上下文；推测解码 | 联合优化 draft 与 target 的 KV cache，在长上下文下利用验证阶段相对便宜的特性打破 latency-throughput 冲突。 | [primary](https://arxiv.org/abs/2408.11049) |
| Together AI + Princeton 等 | Medusa | 2024 | 推测解码；产品 runtime | 在目标模型上增加多组 decoding heads，一次预测并验证多个未来 token；其思想已进入主流 serving runtime。 | [primary](https://arxiv.org/abs/2401.10774) |
| Microsoft Research Asia + Peking University | EAGLE 系列 | 2024 | 推测解码；feature drafting | 在目标模型内部 feature space 生成草稿并动态构建候选树，形成无需通用小模型的推测解码路线。 | [primary](https://github.com/SafeAILab/EAGLE) |
| NVIDIA | TensorRT-LLM Speculative Decoding | 2024 | 产品 runtime；生成加速 | 在产品级 runtime 中集成 draft-target、Medusa、EAGLE 等推测策略，并与 inflight batching、量化和并行执行组合。 | [primary](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html) |
| AWS / Neuron 生态 | Trainium / Trainium3 + Neuron runtime | 2024 | 专用硬件；编译器；算子 | 通过 Neuron Compiler、NKI kernel 和 Trainium 内存层级构建非 CUDA 推理栈，Trainium3 UltraServer 进一步把扩展单位提升到 144 芯片。 | [primary](https://awsdocs-neuron.readthedocs-hosted.com/) |
| Academic work on AWS Trainium | NeuronMM | 2025 | Trainium 算子；矩阵乘 | 针对 Trainium systolic array、SRAM 和特殊 layout 设计融合与缓存策略，展示专用硬件上端到端 LLM 推理优化空间。 | [primary](https://arxiv.org/abs/2510.25977) |
| Google Cloud | Ironwood TPU | 2025 | 推理专用芯片；scale-up | 第七代 TPU 明确以推理为中心，结合大规模 pod、HBM 和 Google 软件栈服务长上下文与 reasoning workload。 | [primary](https://cloud.google.com/tpu) |
| Google Cloud | TPU 8i / TPU 8t | 2026 | 推理专用芯片；agentic infrastructure | 第八代首次将 inference 优化的 8i 与 training 优化的 8t 分开，8i 强调片上 SRAM、内存带宽和低延迟互连；尚待正式交付验证。 | [primary](https://www.itpro.com/infrastructure/google-cloud-eighth-generation-tpu-8t-8i-ai-inference-training) |
| AMD + HPE | Helios / Instinct MI455X rack-scale platform | 2026 | 机架级推理；开放互连 | 以 72 GPU、HBM4、EPYC 和 Ethernet scale-up fabric 构建开放机架方案，代表非 NVLink 的 rack-scale AI 路线。 | [primary](https://www.tomshardware.com/tech-industry/semiconductors/hpe-adopts-amd-helios-rack-architecture-for-2026-ai-systems) |
| Qualcomm | AI200 / AI250 | 2026 | 推理专用加速器；近存计算 | 将 Hexagon NPU 扩展到数据中心，强调大容量 LPDDR、低比特格式、near-memory compute、机架扩展和 disaggregated inference。 | [primary](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-unveils-ai200-and-ai250-ai-inference-accelerators-hexagon-takes-on-amd-and-nvidia-in-the-booming-data-center-realm) |
| Cerebras | Wafer-scale Inference | 2024 | 专用硬件；低延迟 API | 用 wafer-scale engine 和片上大容量存储减少跨芯片数据搬移，主攻极高 token/s 和交互式推理。 | [primary](https://www.cerebras.ai/inference) |
| Groq | GroqCloud / LPU Inference | 2024 | 确定性执行；低延迟 | 用静态调度的 LPU 架构和编译器降低动态调度开销，主攻低 batch、稳定 token latency 的在线生成。 | [primary](https://groq.com/groqcloud) |
| Fireworks AI | Fireworks Inference Platform | 2024 | 托管推理；模型定制 | 将高性能 runtime、量化、LoRA serving 和模型路由封装成推理云，代表独立 inference provider 的产品化路线。 | [primary](https://docs.fireworks.ai/) |
| Together AI | Together Inference Engine | 2024 | 托管推理；推测解码；量化 | 将 FlashAttention、Medusa 等研究与多 GPU serving、量化和私有部署结合，形成模型云和企业推理平台。 | [primary](https://docs.together.ai/) |
| Baseten | Truss / TensorRT-LLM serving stack | 2024 | 模型部署；自动扩缩容 | 把容器构建、模型打包、TensorRT-LLM 优化、流量伸缩和可观测性组合为生产推理平台。 | [primary](https://docs.baseten.co/) |
| Cloudflare | Workers AI | 2024 | 边缘推理；全球调度 | 在分布式边缘网络上提供模型推理 API，将模型放置、流量路由和 serverless 调度下沉到全球基础设施。 | [primary](https://developers.cloudflare.com/workers-ai/) |
| Apple / MLX community | MLX-LM / vllm-mlx | 2024 | 端侧推理；统一内存 | 利用 Apple silicon 统一内存和 MLX 图执行提供本地 LLM 推理，并开始向 continuous batching 和 vLLM API 兼容扩展。 | [primary](https://github.com/ml-explore/mlx-lm) |
| vLLM maintainers / Inferact | vLLM 商业化 | 2026 | 开源 runtime；企业化信号 | vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。 | [primary](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/) |
| SGLang maintainers / RadixArk | SGLang 商业化 | 2026 | prefix reuse；企业化信号 | 围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。 | [primary](https://github.com/sgl-project/sglang) |
| vLLM / PyTorch Foundation | vLLM V1 | 2023 | 通用 runtime；多后端 | 以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。 | [primary](https://github.com/vllm-project/vllm) |
| NVIDIA | TensorRT-LLM | 2023 | NVIDIA runtime；量化；并行 | 提供 inflight batching、paged KV、FP8/FP4、speculative decoding、TP/PP/EP 和多节点执行，是 NVIDIA 平台的产品级 LLM 引擎。 | [primary](https://github.com/NVIDIA/TensorRT-LLM) |
| NVIDIA | Triton Inference Server | 2018 | 模型服务；调度；可观测性 | 负责模型仓库、dynamic batching、ensemble、metrics 和多框架后端，常作为 TensorRT-LLM/vLLM 外层生产服务面。 | [primary](https://github.com/triton-inference-server/server) |
| Hugging Face | Text Generation Inference, TGI | 2022 | 开源 serving；模型生态 | 面向 Hugging Face 模型提供 continuous batching、tensor parallelism、quantization、speculative decoding 和 OpenAI-compatible API。 | [primary](https://github.com/huggingface/text-generation-inference) |
| Microsoft | DeepSpeed-MII / DeepSpeed-FastGen | 2023 | 高吞吐 serving；SplitFuse | 以 DeepSpeed-Inference 为底座，用 Dynamic SplitFuse、模型并行、量化和持久部署服务长 prompt 与 generation 混合负载。 | [primary](https://github.com/microsoft/DeepSpeed-MII) |
| Meta / community | llama.cpp | 2023 | 本地推理；CPU/GPU；量化 | 用 GGUF、低比特量化和多种 CPU/GPU/NPU backend 把本地 LLM 推理扩展到 PC、服务器、手机和嵌入式设备。 | [primary](https://github.com/ggml-org/llama.cpp) |
| MLC community | MLC-LLM | 2023 | 编译部署；跨硬件 | 通过 Apache TVM/MLC 编译模型到 CUDA、ROCm、Metal、Vulkan、WebGPU 等后端，强调跨平台 kernel 生成和端侧部署。 | [primary](https://github.com/mlc-ai/mlc-llm) |
| InternLM / Shanghai AI Laboratory | LMDeploy | 2023 | 国产 runtime；量化；服务 | TurboMind 与 PyTorch engine 支持 persistent batch、KV 管理、AWQ/低比特量化、TP 和多模态模型部署。 | [primary](https://github.com/InternLM/lmdeploy) |
| ModelTC community | LightLLM | 2023 | 轻量 serving；kernel | 用 token attention、动态 batch、共享显存管理和定制 Triton kernel 提供低开销分布式 LLM serving。 | [primary](https://github.com/ModelTC/lightllm) |
| PaddlePaddle / Baidu | FastDeploy | 2022 | 国产部署；多硬件 | 覆盖 Paddle、ONNX、TensorRT 和多类硬件后端，提供从模型压缩到服务部署的推理工具链。 | [primary](https://github.com/PaddlePaddle/FastDeploy) |
| Huawei Ascend | MindIE | 2024 | Ascend serving；调度；算子 | 面向昇腾 NPU 提供 LLM 推理、服务化、并行执行、量化和调度能力，是国产算力生产栈的重要入口。 | [primary](https://www.hiascend.com/software/mindie) |
| Ray / Anyscale | Ray Serve LLM | 2024 | 分布式服务；自动伸缩 | 将 vLLM 等 engine 包装为 Ray actor/deployment，提供多节点 replica、路由、autoscaling 和 Python 应用编排。 | [primary](https://docs.ray.io/en/latest/serve/llm/index.html) |
| BentoML | BentoML / BentoCloud | 2023 | 模型打包；推理平台 | 统一模型容器、API、batching、资源声明和 autoscaling，并与 vLLM、SGLang、TensorRT-LLM 等 runtime 集成。 | [primary](https://docs.bentoml.com/) |
| KServe | Generative Inference | 2024 | Kubernetes；模型服务 | 以 Kubernetes CRD、Gateway、autoscaling 和 ModelMesh 管理生成式服务，并接入 vLLM、Hugging Face、KV offload。 | [primary](https://kserve.github.io/website/docs/model-serving/generative-inference/overview) |
| Red Hat / IBM / Google / NVIDIA 社区 | llm-d | 2025 | Kubernetes-native distributed inference | 将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。 | [primary](https://github.com/llm-d/llm-d) |
| NVIDIA | CUTLASS / CuTe DSL | 2017 | GEMM；attention；模板库 | 提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives；4.4/4.5 系列继续补充 Blackwell GQA decode、int4 KV、MX/NVFP4 block-scaled GEMM 和 MoE grouped GEMM 示例。 | [primary](https://github.com/NVIDIA/cutlass) |
| FlashInfer community / NVIDIA | FlashInfer kernel ecosystem | 2024 | serving attention；JIT kernel | 针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。 | [primary](https://github.com/flashinfer-ai/flashinfer) |
| Microsoft Research / community | TileLang | 2025 | GPU DSL；自动调优 | 将 tiled dataflow 与 layout、线程绑定、tensorization 和软件流水分离，降低编写高性能 attention/MoE kernel 的门槛。 | [primary](https://github.com/tile-ai/tilelang) |
| PyTorch | torch.compile / Inductor | 2023 | 图编译；kernel fusion | 捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。 | [primary](https://docs.pytorch.org/docs/stable/torch.compiler.html) |
| PyTorch | FlexAttention | 2024 | attention 编程模型 | 允许用户用 score modification 和 block mask 表达 attention variant，再由编译器生成 fused kernel，覆盖 sparse/paged inference。 | [primary](https://pytorch.org/blog/flexattention/) |
| MLC / CMU | XGrammar structured generation engine | 2024 | 结构化生成；约束解码 | 预编译 grammar、持久化 parser stack 并与 GPU execution overlap，已进入多种 serving engine 的 JSON/tool-call fast path。 | [primary](https://github.com/mlc-ai/xgrammar) |
| Microsoft | ONNX Runtime GenAI | 2024 | 跨平台生成式 runtime | 在 ONNX Runtime 上封装 generation loop、KV cache、sampling、量化和 CPU/GPU/NPU provider，面向 Windows 与边缘部署。 | [primary](https://github.com/microsoft/onnxruntime-genai) |
| Intel | OpenVINO GenAI | 2024 | Intel CPU/GPU/NPU；端侧推理 | 为 Intel 硬件提供 stateful model、continuous batching、paged attention、量化和 speculative decoding pipeline。 | [primary](https://github.com/openvinotoolkit/openvino.genai) |
| Modular | MAX Engine | 2024 | 编译器；异构 serving | 用 MAX graph/compiler 和 Mojo kernel 统一 CPU/GPU 推理，瞄准摆脱单一 CUDA runtime 的可移植高性能部署。 | [primary](https://docs.modular.com/max/) |
| AMD | ROCm + vLLM/SGLang/TensorRT-LLM ecosystem | 2024 | AMD GPU；开放软件栈 | 通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。 | [primary](https://rocm.docs.amd.com/) |
| AMD | Instinct MI350 Series | 2025 | 低精度推理；大 HBM | CDNA 4 引入 FP4/FP6 并提供 288 GB HBM3E，面向大模型、MoE 和长上下文的高容量推理。 | [primary](https://www.amd.com/en/products/accelerators/instinct/mi350.html) |
| NVIDIA | Vera Rubin NVL72 | 2026 | rack-scale agentic inference；NVLink | 将 72 张 Rubin GPU、36 颗 Vera CPU、ConnectX-9 和 BlueField-4 组合为单一 NVLink 域，强调长上下文、低 cost/token 和 rack-scale RAS。 | [primary](https://www.nvidia.com/en-us/data-center/technologies/rubin/) |
| Intel | Gaudi 2/3 software stack | 2024 | 专用加速器；以太网 scale-out | 通过 SynapseAI、HCCL、FP8 和 vLLM/Optimum Habana 支持 LLM serving，以标准 Ethernet 和成本为差异点。 | [primary](https://docs.habana.ai/) |
| AWS | Inferentia2 + Neuron | 2023 | 云端推理 ASIC | Inferentia2 以 Neuron compiler/runtime、NeuronLink 和多芯片实例服务低成本推理，与 Trainium 共享软件生态。 | [primary](https://aws.amazon.com/machine-learning/inferentia/) |
| Google | JetStream / MaxText / Pathways on TPU | 2024 | TPU serving；编译与调度 | 用 JAX/XLA、paged attention、模型并行和 TPU pod serving 构成 Gemini 与开源模型的 TPU 推理路径。 | [primary](https://github.com/AI-Hypercomputer/JetStream) |
| Meta / PyTorch | ExecuTorch | 2024 | 移动端；边缘 runtime | 将模型导出到轻量 runtime，并通过 Core ML、QNN、XNNPACK、Vulkan 等 backend 在手机和嵌入式设备执行。 | [primary](https://pytorch.org/executorch/) |
| Google | LiteRT | 2024 | Android；端侧生成式 AI | 在 TensorFlow Lite 演进基础上统一 CPU/GPU/NPU delegate 和生成式模型部署，服务 Android 与边缘设备。 | [primary](https://ai.google.dev/edge/litert) |
| Qualcomm | AI Engine Direct / QNN | 2024 | Snapdragon NPU；端侧推理 | 通过 QNN graph、低比特量化和 Hexagon NPU backend 部署移动端 LLM/MLLM，强调隐私、能耗和离线能力。 | [primary](https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk) |
| Apple | MLX / Core ML | 2023 | Apple Silicon；统一内存 | MLX 利用 unified memory 支持研究与本地生成，Core ML 负责产品端 CPU/GPU/ANE 部署，形成 Mac 与 iPhone 双层生态。 | [primary](https://github.com/ml-explore/mlx) |
| SambaNova Systems | SambaNova Cloud / RDU | 2024 | dataflow accelerator；托管推理 | 用 reconfigurable dataflow unit 和模型编译栈提供高吞吐推理 API，属于非 GPU 专用加速路线。 | [primary](https://sambanova.ai/) |
| Tenstorrent | TT-Metalium / Wormhole | 2024 | RISC-V AI accelerator；开放 kernel | 公开低层 TT-Metalium 编程栈和模型实现，探索可编程 many-core 芯片上的 LLM 推理。 | [primary](https://github.com/tenstorrent/tt-metal) |
| Hugging Face | Diffusers | 2022 | 图像/视频/音频生成 runtime | 以统一 DiffusionPipeline 组合 model、scheduler、LoRA 和量化/offload/torch.compile 优化，是开源扩散推理的基础 API。 | [primary](https://huggingface.co/docs/diffusers/index) |
| xDiT community | xDiT | 2024 | DiT 分布式推理；多维并行 | 为 diffusion transformer 提供 sequence、pipe、CFG、USP 等并行和通信优化，支撑高分辨率图像与长视频生成。 | [primary](https://github.com/xdit-project/xDiT) |
| Ant Group + vLLM | vLLM-Omni runtime | 2026 | any-to-any；统一 serving API | 将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。 | [primary](https://github.com/vllm-project/vllm-omni) |
| NVIDIA | TensorRT diffusion pipelines | 2024 | diffusion kernel；低精度 | 通过 TensorRT、Model Optimizer 和定制 attention/GEMM kernel 加速 Stable Diffusion、Flux 和视频生成模型。 | [primary](https://developer.nvidia.com/tensorrt) |
| Alibaba Cloud | COMET | 2025 | MoE 通信；生产集群 | 细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) |
| MIT Han Lab / NVIDIA ecosystem | QServe / OmniServe | 2024 | W4A8KV4；低比特 serving | 将 4-bit 权重、8-bit 激活和 4-bit KV 与 SmoothAttention、重排及定制 kernel 联合设计。 | [primary](https://github.com/mit-han-lab/omniserve) |
| MLC / SGLang / vLLM ecosystem | XGrammar production integration | 2025 | JSON；tool calling；约束生成 | 将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) |
| Meta | Context Parallelism for Million-Token Inference | 2025 | 长上下文；分布式 attention | 用 pass-KV/pass-Q 精确 ring attention 在常见数据中心网络上扩展百万 token prefill。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) |
| Microsoft Research | LeanAttention / TurboAttention | 2025 | decode kernel；量化 attention | 分别从精确 decode dataflow 和端到端量化 attention 两条路线降低长上下文 memory wall。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html) |
| NVIDIA / University of Washington | FlashInfer production integration | 2025 | serving kernel；生态集成 | 从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) |
| Microsoft Research + University of Edinburgh | WaferLLM on Cerebras WSE-2 | 2025 | wafer-scale inference；kernel | 以 PLMR 模型、MeshGEMM/MeshGEMV 和 wafer-scale parallelism 将 LLM inference 映射到数十万片上 core。 | [primary](https://www.usenix.org/conference/osdi25/technical-sessions) |
| Alibaba Group + Peking University | HydraServe | 2026 | serverless；冷启动 | 主动分发模型并重叠加载、runtime 初始化和 worker 启动，同时通过拓扑感知放置避免多实例网络争用。 | [primary](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| Alibaba Group + Peking University | ServeGen | 2026 | 生产 workload；benchmark | 从全球云端 LLM 服务提取语言、多模态和 reasoning workload 特征，并开源按 client 组合的 trace generator。 | [primary](https://github.com/alibaba/ServeGen) |
| MLCommons | MLPerf Inference |  | 标准 benchmark；软硬件比较 | 以统一模型、精度规则、server/offline 场景和可审计 submission 比较数据中心及边缘推理系统。 | [primary](https://mlcommons.org/benchmarks/inference-datacenter/) |
| SemiAnalysis | InferenceMAX | 2025 | 滚动 benchmark；TCO | 夜间滚动测试完整 driver/kernel/runtime/hardware 组合，以 tok/s/GPU、tok/s/user 和美元/百万 token 跟踪软件演进。 | [primary](https://www.tomshardware.com/tech-industry/inferencemax-ai-benchmark-tests-software-stacks-efficiency-and-tco-vendor-neutral-suite-runs-nightly-and-tracks-performance-changes-over-time) |
| Microsoft Research 等 | Inference evaluation anti-patterns | 2025 | 方法论；benchmark 审计 | 系统总结 baseline 公平性、workload 代表性和 metric 设计中的反模式，强调 burst、stall 与双阶段行为。 | [primary](https://arxiv.org/abs/2507.09019) |
| Snowflake AI Research | Shift Parallelism / Arctic Inference | 2026 | 动态并行；弹性服务 | 根据流量在 TP 与 sequence parallelism 间切换，并结合 speculative decoding、SwiftKV 和 embedding fast path。 | [primary](https://www.asplos-conference.org/asplos2026/program/) |
| Inspur + Huawei Cloud + Shanghai Jiao Tong University + Peking University | CacheSlide | 2026 | Agent KV 复用；位置校正 | 针对相对位置稳定但绝对位置变化的 agent prompt 片段，结合 RPDC、加权校正和 spill-aware KV 管理。 | [primary](https://www.usenix.org/conference/fast26/technical-sessions) |
| Microsoft Research + University of Chicago | AdaptCache | 2025 | KV 压缩；DRAM/SSD hierarchy | 按 KV entry 联合选择有损压缩方式、压缩率和存储位置，在生成质量与加载延迟之间做动态权衡。 | [primary](https://arxiv.org/abs/2509.00105) |
| Intel + University of Illinois Urbana-Champaign | DECA | 2025 | 权重解压；near-core accelerator | 用三维 roofline 指导 near-core 解压单元设计，使压缩模型不被在线解码开销抵消。 | [primary](https://arxiv.org/abs/2505.19349) |
| IBM + University of Illinois Urbana-Champaign | Chameleon | 2025 | 多 Adapter；缓存与调度 | 联合管理 adapter 缓存和请求调度，面向大量 LoRA tenant 减少换入及排队。 | [primary](https://arxiv.org/abs/2411.17741) |
| AlayaDB AI + academia | AlayaDB | 2025 | 长上下文；向量数据库；Attention | 将 KV cache 和 attention 处理抽象为数据库查询，由 query optimizer 决定索引、放置和执行计划。 | [primary](https://arxiv.org/abs/2504.10326) |
| VectorLiteRAG team | VectorLiteRAG | 2025 | RAG；CPU/GPU 索引分区 | 根据向量簇访问偏斜决定哪些 index 常驻 HBM，并联动 LLM batch size 平衡检索和生成阶段。 | [primary](https://arxiv.org/abs/2504.08930) |
| RAG-Stack team | RAG-Stack | 2025 | RAG optimizer；质量性能协同 | 用 RAG IR、成本模型和 plan explorer 联合搜索数据库、retrieval 和 generation 配置。 | [primary](https://arxiv.org/abs/2510.20296) |
| Microsoft | Maia 200 | 2026 | Azure 自研推理芯片；FP4/FP8 | 面向 Azure AI inference 设计低精度 tensor core、片上 SRAM、定制 DMA 与 NoC，并开始用于 Microsoft 内部 AI 服务。 | [primary](https://www.techradar.com/pro/microsoft-unveils-maia-200-its-powerhouse-accelerator-looking-to-unlock-the-power-of-large-scale-ai) |
| Google TPU ecosystem | Gemma 4 on vLLM-TPU | 2026 | TPU serving；GPU 对比 | 展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。 | [primary](https://arxiv.org/abs/2605.25645) |
| AMD ROCm ecosystem | MI325X architecture-aware deployment study | 2026 | ROCm；AITER；多模型架构 | 说明 MLA、GQA、MoE 和视觉模型需要不同的 AITER、KV offload 与 block-size 配置，不能沿用统一参数。 | [primary](https://arxiv.org/abs/2603.10031) |
| Open Compute numerical-format ecosystem | MX-SAFE | 2026 | Microscaling；训练推理统一格式 | 动态切换 mantissa/exponent 模式，使低精度格式同时覆盖 direct-cast inference 和训练需求。 | [primary](https://arxiv.org/abs/2605.24391) |
| Huawei Cloud + NUS + SJTU | CachedAttention | 2024 | 多轮会话；分层 KV cache | 用 DRAM/SSD 分层保存跨轮 KV，配合 layer-wise preload、异步保存和 scheduler-aware eviction 降低 TTFT。 | [primary](https://www.usenix.org/conference/atc24/technical-sessions) |
| Microsoft Research Asia | T-MAC | 2024 | CPU/边缘 LLM；查表低比特 | 以 lookup table 替代低比特乘法路径，在 CPU、移动端和 WebAssembly 上部署量化模型。 | [primary](https://2025.eurosys.org/program.html) |
| ByteDance | Astral | 2025 | 超大规模 AI 网络 | 从拓扑、路由、拥塞控制和作业编排构建大模型数据中心网络，是企业 AI fabric 的生产案例。 | [primary](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) |
| Microsoft Research + Clemson + Harvard | HACK | 2025 | PD 分离；KV 通信压缩 | 在压缩域执行部分 attention 计算，减少 KV 传输和反复压缩解压。 | [primary](https://arxiv.org/abs/2502.03589) |
| Microsoft | MSCCL / MSCCL++ | 2021 | Collective compiler；AI 通信 | 用 DSL、通信 primitive 和拓扑搜索生成高效 collective，服务 Azure AI、NCCL/RCCL 生态。 | [primary](https://github.com/microsoft/msccl) |
| NVIDIA | NCCL |  | GPU collective；NVLink/IB | 提供 all-reduce、all-to-all、broadcast 等 GPU collective，是 TP、PP、EP 和 MoE 推理的默认通信层。 | [primary](https://github.com/NVIDIA/nccl) |
| NVIDIA / Linux Foundation ecosystem | UCX |  | RDMA；统一通信抽象 | 统一 InfiniBand、RoCE、shared memory、CUDA memory 等传输，为 MPI、NCCL 和分布式 runtime 提供底层能力。 | [primary](https://github.com/openucx/ucx) |
| Meta | Gloo |  | Collective；CPU/GPU backend | 为 PyTorch distributed 提供跨 TCP、IB 等传输的 collective backend，是控制面和非 NCCL 路径的基础组件。 | [primary](https://github.com/facebookincubator/gloo) |
| NVIDIA | Megatron-LM / Megatron-Core | 2019 | Tensor/Sequence/Expert Parallel | 建立 tensor parallel 等核心拆分，并发展为支持 TP、PP、CP、EP 的大模型训练推理核心库。 | [primary](https://github.com/NVIDIA/Megatron-LM) |
| NVIDIA | FasterTransformer | 2020 | Transformer kernel；模型并行 | 用融合 CUDA kernel、GEMM 调优、量化和多 GPU 并行提供早期生产级 Transformer 推理库，后续能力并入 TensorRT-LLM。 | [primary](https://github.com/NVIDIA/FasterTransformer) |
| Tencent | TurboTransformers | 2021 | 动态 batch；GPU serving | 按序列长度动态组织 batch，并通过融合 kernel 和内存管理加速 Transformer 在线服务。 | [primary](https://github.com/Tencent/TurboTransformers) |
| ByteDance | LightSeq | 2021 | Transformer inference；CUDA fusion | 通过 fused layer、定制 CUDA kernel 和显存复用部署 NLP 与生成模型。 | [primary](https://github.com/bytedance/lightseq) |
| Microsoft | DeepSpeed-Inference | 2022 | 超大模型推理；并行；量化 | 以 inference-adapted parallelism、kernel injection、量化和 heterogeneous memory 支撑超大 Transformer。 | [primary](https://www.deepspeed.ai/tutorials/inference-tutorial/) |
| Microsoft | DeepSpeed-MoE | 2022 | MoE 训练与推理 | 联合 expert parallel、通信优化和模型压缩，使稀疏大模型的推理成本可控。 | [primary](https://arxiv.org/abs/2201.05596) |
| Microsoft Research Asia | Tutel | 2022 | MoE runtime；adaptive parallelism | 提供自适应 expert parallel、all-to-all、fused kernel 和动态配置，是通用 MoE 软件栈的重要来源。 | [primary](https://github.com/microsoft/tutel) |
| Databricks / Stanford ecosystem | MegaBlocks | 2023 | Block-sparse MoE | 用 block-sparse operation 替代 capacity padding，为高效 MoE kernel 和 serving 提供基础。 | [primary](https://github.com/databricks/megablocks) |
| Tsinghua University | FasterMoE | 2022 | MoE 调度；拓扑通信 | 用 expert shadowing、smart scheduling 和 topology-aware communication 缓解动态路由不均。 | [primary](https://github.com/thu-pacman/FasterMoE) |
| Intel | oneCCL |  | Intel collective；CPU/GPU | 为 Intel CPU/GPU 集群提供 collective communication，并接入 PyTorch、oneAPI 与分布式 AI 软件。 | [primary](https://github.com/uxlfoundation/oneCCL) |
| Meta | Faiss | 2017 | 向量检索；GPU ANN | 提供 IVF、PQ、HNSW、GPU k-selection 等索引，是自建 RAG 和向量检索 benchmark 的基础库。 | [primary](https://github.com/facebookresearch/faiss) |
| Google Research | ScaNN | 2020 | 最大内积；量化 ANN | 用 anisotropic vector quantization、partitioning 和 reordering 提供高召回低延迟检索。 | [primary](https://github.com/google-research/google-research/tree/master/scann) |
| Microsoft Research | DiskANN / FreshDiskANN / SPFresh | 2019 | SSD ANN；动态索引 | 以 SSD-resident graph 支撑十亿级搜索，并逐步加入动态更新和在线索引维护。 | [primary](https://github.com/microsoft/DiskANN) |
| Zilliz / LF AI & Data | Milvus | 2019 | 云原生向量数据库 | 将 query、index、data、storage 节点解耦，并支持多索引、标量过滤、GPU 和分布式扩展。 | [primary](https://github.com/milvus-io/milvus) |
| NVIDIA RAPIDS | cuVS / CAGRA | 2023 | GPU 向量搜索；RAG | 提供 GPU graph ANN、IVF、brute-force 和多节点能力，并被向量数据库用于 GPU 加速。 | [primary](https://github.com/rapidsai/cuvs) |
| Microsoft Research + academia | VBASE | 2023 | ANN + relational query | 将向量近邻搜索、关系过滤和查询 optimizer 放在同一数据库执行模型中。 | [primary](https://www.usenix.org/conference/osdi23/presentation/zhang-qianxi) |
| Spotify | Annoy | 2013 | 只读 ANN；内存映射 | 用随机投影树和 mmap 提供简单稳定的静态向量索引，适合中小规模只读检索服务。 | [primary](https://github.com/spotify/annoy) |
| NMSLIB community | HNSW / hnswlib | 2016 | 图 ANN；内存索引 | HNSW 成为多数向量数据库的默认高召回内存索引，也决定 RAG 的内存成本和更新行为。 | [primary](https://github.com/nmslib/hnswlib) |
| AMD ROCm | ATOM inference engine | 2026 | 运行时；算子；MoE 通信 | 以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。 | [primary](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html) |
| AMD ROCm | ATOMesh distributed serving gateway | 2026 | 运行时；状态管理；分离式架构 | 作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。 | [primary](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html) |
| AMD ROCm + vLLM | Productionizing TurboQuant on AMD GPUs | 2026 | 压缩；状态管理；成本 | 在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。 | [primary](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html) |
| NVIDIA | BlueField-4 + DOCA in-silicon security for AI factories | 2026 | AI 集群 OS 与 SRE；可靠性与安全 | 用 BlueField-4 DPU 和 DOCA Argus / Vault / Flow 在基础设施层做运行时威胁检测、零信任文件访问和高速网络策略 enforcement，保护 agentic AI factory 的模型、上下文内存和数据。 | [primary](https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/) |
|  | + 26 releases | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/releases) |
|  | .clang-format | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/blob/main/.clang-format) |
|  | .clang-tidy | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/blob/main/.clang-tidy) |
|  | .claude/skills | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/tree/main/.claude/skills) |
|  | .gitattributes | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/blob/main/.gitattributes) |
|  | .githooks | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/tree/main/.githooks) |
|  | .github | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/tree/main/.github) |
|  | .gitignore | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/blob/main/.gitignore) |
|  | .gitmodules | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/blob/main/.gitmodules) |
|  | 2,471 Commits | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/commits/main/) |
|  | 3rdparty | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/tree/main/3rdparty) |
|  | 404 forks | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/forks) |
|  | AITER v0.1.12.post1 Released | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/releases/tag/v0.1.12.post1) |
|  | AITER v0.1.16.post3 Latest Jun 26, 2026 | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/releases/tag/v0.1.16.post3) |
|  | ATOM | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/ATOM) |
|  | Accelerate DeepSeek-R1 Inference: Integrate AITER into SGLang | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://rocm.blogs.amd.com/artificial-intelligence/aiter-intergration-s/README.html) |
|  | Accelerated LLM Inference with vLLM 0.9.x and ROCm | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://rocm.blogs.amd.com/software-tools-optimization/vllm-0.9.x-rocm/README.html) |
|  | Accelerator | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/open-source/accelerator) |
|  | Actions | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/actions) |
|  | ActionsAutomate any workflow | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/features/actions) |
|  | Activity | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/activity) |
|  | App Modernization | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/solutions/use-case/app-modernization) |
|  | Beyond Porting: How vLLM Orchestrates High-Performance Inference on AMD ROCm | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://blog.vllm.ai/2026/02/27/rocm-attention-backend.html) |
|  | Branches | 2026 | AMD Instinct Inference Vector Kernels (AITER) |  | [primary](https://github.com/ROCm/aiter/branches) |
