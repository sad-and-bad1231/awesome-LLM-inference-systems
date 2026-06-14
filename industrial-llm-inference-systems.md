# 工业界 LLM 推理系统方案追踪

更新时间：2026-06-12
时间口径：2024-2026，优先收企业论文、官方博客、技术报告、开源 runtime、工程文档和顶会系统论文。

## 来源等级

- **A 级**：正式会议论文、官方论文/技术报告、官方文档和官方代码仓库，可直接作为技术事实依据。
- **B 级**：企业官方博客、产品发布和工程复盘，可用于理解生产方案，但性能数字需结合测试条件阅读。
- **C 级**：媒体报道、融资或未来硬件路线图，只用于判断产业方向；产品交付和技术指标应在后续更新中复核。

## 观察框架

| 方向 | 工业界核心问题 | 典型解决路线 |
|---|---|---|
| 推理执行与运行时优化 | 如何在多模型、多租户、长输出、SLO 约束下提高 GPU/NPU 利用率 | continuous batching、chunked prefill、prefill/decode disaggregation、KV-aware routing、speculative decoding、multi-token prediction、token-level autoscaling |
| 长上下文与状态管理 | KV cache 线性增长后，显存、HBM 带宽、跨节点传输和复用都成为瓶颈 | prefix/cache reuse、KV offload、KV transfer、remote KV store、vector-storage KV retrieval、CPU/SSD/CXL/DPU 多层存储 |
| 压缩与成本优化 | 如何降低每 token 成本、显存占用、HBM 读写和能耗，同时不破坏 long-context/reasoning 质量 | FP8/NVFP4/int4 KV、MLA、低秩、稀疏召回、token/head/layer 保留、模型池化、能耗感知调度 |
| 算子与编译优化 | attention/GEMM/MoE decode 是实际吞吐瓶颈，且长上下文形状动态、ragged、paged | FlashAttention/FlashMLA/FlashInfer/FlexAttention/CUTLASS/Triton/torch.compile、FP8 GEMM、paged attention kernel、TPU ragged paged attention |
| 分离式架构与网络 | PD、KV 和 expert 分离后，状态搬运与 collective 可能替代计算成为瓶颈 | NIXL/UCCL/RDMA/CXL、KV compression、multi-NIC、all-to-all fusion、compute-memory disaggregation |
| MoE 推理 | expert 数量、动态路由和 all-to-all 导致显存容量、负载倾斜与通信放大 | expert parallelism、attention/expert disaggregation、expert cache/prefetch、buffer fusion、低比特 expert |
| Agent 与程序级 serving | agent 会产生调用图、tool-call stall、多轮共享状态和长 CoT，单请求调度无法表达真实目标 | program-aware scheduling、agent KV 生命周期、collective KV sharing、structured generation、tool execution offload |
| RAG 与外部记忆 | 检索延迟、索引更新、过滤、reranking 和生成阶段相互影响，向量数据库无法再被视为独立黑盒 | GPU/SSD ANN、动态向量索引、检索生成联合优化、semantic cache、KV/vector database 融合、query optimizer |
| 多模态与生成模型 | encode、LLM、DiT、audio/video decoder 的硬件需求和扩展规律不同 | stage graph、encode-prefill-decode disaggregation、component placement、cross-stage batching、intermediate-state transfer |
| 异构与端侧推理 | CPU/GPU/NPU/统一内存的算力、带宽和可编程性不匹配 | phase-aware placement、operator fallback、unified memory、GGUF/低比特、MLX/Core ML/QNN/OpenVINO |
| 可靠性与弹性 | GPU 故障、spot interruption、扩缩容和模型加载会中断有状态 generation | KV backup、live migration、checkpoint/restore、failure-domain isolation、layer-wise loading、resilient TP |
| AI 集群 OS 与 SRE | GPU kernel、collective、远程内存、checkpoint 和多租户隔离形成跨层故障，传统容器指标无法定位 | GPU OS、dependency tracing、collective diagnosis、device checkpoint、spot-aware scheduling、failure automation |
| 评测、能耗与 TCO | benchmark 易受 batch、长度、SLO、软件版本和硬件价格影响，单一 tok/s 缺乏可比性 | goodput、TTFT/TPOT/P99、energy/token、$/M token、production trace、rolling benchmark、完整软硬件版本记录 |

## 企业方案清单

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| NVIDIA | Dynamo | 2025-2026 | 运行时；状态管理 | 分布式/分离式推理框架，组合 disaggregated serving、KV cache-aware routing、KV offloading，并用 NIXL 做低延迟 KV 传输。 | [介绍](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) / [文档](https://docs.dynamo.nvidia.com/dynamo/getting-started/introduction) |
| NVIDIA | NIXL / KV cache transfer | 2025 | 状态管理；运行时 | 面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。 | [Dynamo KV transfer](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html) |
| NVIDIA | TensorRT-LLM KV cache reuse | 2025 | 运行时；状态管理 | 用 KV cache event API 和 KV-aware routing 提高 prefix/cache 命中，减少重复 prefill。 | [技术博客](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) |
| NVIDIA | TensorRT-LLM FP8/INT8 KV cache | 2024-2026 | 压缩；算子 | MHA/MQA kernel 中支持 on-the-fly dequantize 的 FP8/INT8 KV cache，降低 decode 阶段读带宽。 | [TensorRT-LLM attention doc](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html) |
| NVIDIA | NVFP4 KV cache | 2025 | 压缩；成本 | Blackwell 侧使用 4-bit KV 存储、attention 前解量化到 FP8，面向长上下文、大 batch、多 agent/MoE 降低 HBM 压力。 | [技术博客](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/) |
| NVIDIA | BlueField-4 STX / context memory storage | 2026 | 状态管理；硬件系统 | 用 DPU/加速存储绕过 host CPU，把长上下文 KV cache 放到近存储路径，面向 agentic AI 的大上下文状态。 | [报道](https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai) |
| NVIDIA + Georgia Tech | RocketKV | 2025 | 长上下文；压缩 | 两阶段 KV 压缩：先永久淘汰部分 prompt token，再做动态 top-k sparse attention。 | [arXiv](https://arxiv.org/abs/2502.14051) |
| NVIDIA Research + Georgia Tech | ThinKV | 2026 | 长 CoT；动态保留 | thought-adaptive KV cache compression，根据推理过程中的 thought 类型做保留、量化和逐级淘汰。 | [OpenReview](https://openreview.net/forum?id=M3CeHnZKNC) |
| NVIDIA + University of Warsaw | KVTC | 2026 | 状态管理；压缩 | 把 KV cache 看成可压缩信号，用 transform coding、PCA 去相关、自适应量化和熵编码降低可复用 KV 存储。 | [arXiv](https://arxiv.org/abs/2511.01815) |
| ByteDance Seed | ShadowKV | 2025 | 长上下文；状态管理；压缩 | GPU 只保留低秩 keys、landmarks 和少量 outliers，values 放 CPU DRAM，decode 时按需召回 Top-K value。 | [ByteDance](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference) / [GitHub](https://github.com/ByteDance-Seed/ShadowKV) |
| DeepSeek | MLA / Multi-head Latent Attention | 2024-2025 | 压缩；模型结构 | 把 KV cache 压到 latent 向量，DeepSeek-V3/R1 系列用 MLA 降低 long-context decode 的 KV 内存和带宽。 | [DeepSeek-V3 report](https://arxiv.org/abs/2412.19437) |
| DeepSeek | FlashMLA | 2025 | 算子；长上下文 | 面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。 | [GitHub](https://github.com/deepseek-ai/FlashMLA) |
| DeepSeek | DeepGEMM / DeepEP | 2025 | 算子；MoE 通信 | FP8 GEMM 与 MoE expert-parallel 通信库，支撑 DeepSeek 系列训练和推理的 dense/MoE fast path。 | [FlashMLA/开源周入口](https://flashmla.net/) |
| Google Cloud | JetStream + MaxText | 2024-2025 | 运行时；TPU serving | 面向 XLA/TPU 的 throughput 和 memory optimized LLM inference engine，配合 MaxText 在 TPU/GKE 上服务 LLM。 | [Google Cloud TPU doc](https://cloud.google.com/tpu/docs/tutorials/LLM/jetstream-maxtext-inference-v6e) |
| Google Research / DeepMind | TurboQuant | 2026 | 压缩；成本 | 通过随机旋转、近最优量化和 QJL 残差校正，面向 KV cache 和向量检索做低比特在线向量量化。 | [arXiv](https://arxiv.org/abs/2504.19874) |
| Google / TPU ecosystem | Ragged Paged Attention for TPU | 2026 | 算子；编译 | 面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。 | [arXiv](https://arxiv.org/abs/2604.15464) |
| Microsoft Research | Splitwise | 2024 | 运行时；成本 | 把 prompt computation 和 token generation 放在不同机器池，分别匹配 compute-bound 与 memory-bound 阶段。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) |
| Microsoft Research | DynamoLLM | 2025 | 运行时；成本 | 动态重配置 LLM inference cluster，在 SLO 下优化能耗和成本。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/dynamollm-designing-llm-inference-clusters-for-performance-and-energy-efficiency/) |
| Microsoft Research | RetroInfer / RetrievalAttention | 2025-2026 | 长上下文；状态管理 | 把 KV cache 重新抽象成向量存储系统，在 CPU/GPU 间用 attention-aware index 召回关键 KV。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/retroinfer-a-vector-storage-engine-for-scalable-long-context-llm-inference/) / [GitHub](https://github.com/microsoft/RetrievalAttention) |
| Microsoft Research | DroidSpeak | 2026 | 状态管理；多模型 serving | 在相同架构的 fine-tuned model variants 之间共享 KV cache，降低企业多模型/多 agent 的重复 prefill。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/droidspeak-kv-cache-sharing-for-efficient-multi-llm-serving/) |
| Microsoft Research | CacheBlend | 2025 | RAG；状态管理 | 复用 RAG cached knowledge 的 KV，并处理非前缀片段融合问题，减少长输入 prefill。 | [PDF](https://www.microsoft.com/en-us/research/uploads/prod/2024/09/eurosys25-final999.pdf) |
| Meta / PyTorch | FlexAttention for inference | 2025-2026 | 算子；编译 | 用 PyTorch API 表达 attention variants，经 torch.compile 降到 fused attention kernel，支持 inference/paged attention 方向。 | [PyTorch blog](https://pytorch.org/blog/flexattention-for-inference/) / [FA4 update](https://pytorch.org/blog/flexattention-flashattention-4-fast-and-flexible/) |
| Meta | Scaling LLM inference: TP/CP/EP | 2025 | 运行时；并行 | 公开 Meta 在 tensor/context/expert parallelism 上扩展 LLM inference 的工程经验。 | [Meta Engineering](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/) |
| PyTorch Foundation / vLLM community | vLLM V1 + torch.compile | 2025 | 运行时；编译 | vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。 | [PyTorch vLLM](https://pytorch.org/projects/vllm/) / [Red Hat blog](https://developers.redhat.com/articles/2025/09/03/vllm-torchcompile-efficient-llm-inference-pytorch) |
| IBM Research | PagedAttention + FlexAttention / FMS | 2025 | 算子；长上下文 | 在 IBM Foundation Model Stack 中把 PagedAttention 与 FlexAttention 融合，处理 scattered KV gather。 | [arXiv](https://arxiv.org/abs/2506.07311) |
| IBM / Red Hat / llm-d | llm-d + LMCache + vLLM | 2025-2026 | 运行时；状态管理 | Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。 | [IBM Research](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes) |
| LMCache 社区 / 企业采用 | LMCache | 2025 | 状态管理；运行时 | 将 KV cache 抽成独立层，支持跨 engine/query 复用和 GPU/CPU/storage/network 多层编排。 | [arXiv](https://arxiv.org/abs/2510.09665) |
| Moonshot AI + Tsinghua | Mooncake | 2025 | 状态管理；运行时 | 以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。 | [USENIX FAST](https://www.usenix.org/conference/fast25/presentation/qin) |
| Huawei | P/D-Serve | 2024 | 运行时；状态管理 | 在数万 xPU/NPU 规模上部署 prefill/decode disaggregated serving，做 P/D 组织、调度和 D2D KV transfer。 | [arXiv](https://arxiv.org/abs/2408.08147) |
| Huawei Cloud / Ascend | Ascend-vLLM prefix caching / KV offload | 2025-2026 | 状态管理；运行时 | 在 Ascend NPU 上支持 prefix caching、KV cache CPU offload 和 Mooncake/LMCache 连接。 | [Prefix caching](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html) / [KV offload](https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_cache_cpu_offload.html) |
| Huawei | Unified Cache Manager, UCM | 2025 | 状态管理；多层内存 | 用分层 KV cache 管理缓解 HBM 受限环境下的推理吞吐/延迟问题。 | [报道](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-releases-new-tool-to-get-chinese-firms-around-crushing-hbm-export-blacklist-new-ucm-software-claims-up-to-22x-throughput-gain-and-90-percent-latency-reduction-for-traditional-cache-hierarchies-in-ai-workloads) |
| Alibaba Cloud | FlowKV | 2025 | 运行时；KV 传输 | 在 PD 分离式架构中优化 KV cache transfer，并做 load-aware scheduling。 | [arXiv](https://arxiv.org/abs/2504.03775) |
| Alibaba Group | Aegaeon | 2025 | 长尾模型市场；GPU pooling | 在共享 GPU 池中复用模型和显存，避免 marketplace 中大量低流量模型各自独占设备。 | [A：SOSP 2025](https://dblp.org/db/conf/sosp/sosp2025.html) |
| Alibaba Cloud | BladeLLM | 2025-2026 | 运行时；产品化 | PAI 上的高性能 LLM inference engine，用于低延迟、高吞吐部署 Qwen 等模型。 | [Alibaba Cloud doc](https://www.alibabacloud.com/help/doc-detail/2865199.html) |
| Alibaba Cloud Tair | Tair-KVCache-HiSim | 2026 | 状态管理；仿真 | 面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。 | [Alibaba Cloud blog](https://www.alibabacloud.com/blog/603164) |
| Samsung Research | LookaheadKV | 2026 | 长上下文；动态淘汰 | 不生成未来草稿，训练轻量模块预测未来重要性分布以指导 KV cache eviction。 | [Samsung Research](https://research.samsung.com/research-papers/LookaheadKV-Fast-and-Accurate-KV-Cache-Eviction-by-Glimpsing-into-the-Future-without-Generation) |
| Adobe Research | Cache-Craft | 2025 | RAG；状态管理 | 管理 RAG chunk-caches，通过少量重计算修复位置问题，实现 chunk KV cache 复用。 | [arXiv](https://arxiv.org/abs/2502.15734) |
| OpenAI / Triton ecosystem | Triton language and kernels in inference stacks | 2024-2026 | 算子；编译 | 工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。 | [Triton](https://triton-lang.org/) |
| FlashInfer 社区 | FlashInfer | 2025 | 算子；serving kernel | 面向 LLM serving 的可定制 attention engine，支持 paged KV、decode/prefill kernel、与多 runtime 集成。 | [MLSys 2025 PDF](https://proceedings.mlsys.org/paper_files/paper/2025/file/dbf02b21d77409a2db30e56866a8ab3a-Paper-Conference.pdf) |
| Cerebras | 高速推理 API / Llama API 合作 | 2025 | 成本；硬件 serving | 用 wafer-scale engine 做极高 token/s 推理，Meta Llama API 等使用其高速推理能力。 | [报道入口](https://www.cerebras.ai/) |

## 2026-06-02 追加：近期企业/生态更新

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| NVIDIA | Full-Stack Optimizations for Agentic Inference with Dynamo | 2026 | 运行时；状态管理 | 针对 coding agent / multi-agent 的 write-once-read-many KV 模式，强调 router、cache pinning、ephemeral KV block 生命周期和 agent-native KV 管理。 | [NVIDIA Blog](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/) |
| NVIDIA | Dynamo 1.0 Production-Scale Multi-Node Inference | 2026 | 运行时；Kubernetes；状态管理 | Dynamo 1.0 强化多节点部署、Kubernetes 编排、agentic/multimodal KV routing、ModelExpress 快速启动和 KV Block Manager。 | [NVIDIA Blog](https://developer.nvidia.com/blog/?p=113961) |
| NVIDIA | Dynamo Snapshot | 2026 | 运行时；冷启动 | 用 CRIU + cuda-checkpoint 做 Kubernetes 上推理 worker 快照恢复，并通过 KV cache unmap 减小 checkpoint 体积。 | [NVIDIA Blog](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/) |
| NVIDIA | NIXL / Inference Transfer Library | 2026 | KV 传输；网络 | 非阻塞传输 API 和动态元数据交换，覆盖 disaggregated KV movement、long-context storage、weight transfer 和 expert parallelism。 | [NVIDIA Blog](https://developer.nvidia.com/blog/?p=113426) |
| NVIDIA | Dynamo KVBM | 2026 | 状态管理；分层 KV | KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。 | [Dynamo Docs](https://docs.dynamo.nvidia.com/dynamo/components/kvbm) |
| Tencent Cloud TACO + NVIDIA | FlexKV | 2026 | 状态管理；多层 KV | 分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。 | [GitHub](https://github.com/taco-project/FlexKV) / [Dynamo Docs](https://docs.nvidia.com/dynamo/kv-managers/flex-kv) |
| ByteDance | InfiniStore | 2025-2026 | 状态管理；KV store | 高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。 | [GitHub](https://github.com/bytedance/InfiniStore) |
| Moonshot / Mooncake / vLLM | vLLM x Mooncake Store | 2026 | 状态管理；agentic serving | 将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。 | [vLLM Blog](https://vllm.ai/blog/2026-05-06-mooncake-store) |
| Moonshot / PyTorch | Mooncake Joins PyTorch Ecosystem | 2026 | 生态；KV 传输 | Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。 | [PyTorch Blog](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) |
| Novita AI + vLLM | PegaFlow External KV Cache | 2026 | 状态管理；外部 KV 服务 | PegaFlow 作为 Rust standalone external KV cache service 通过 vLLM connector 接入，面向生产级外部 KV cache。 | [vLLM Blog](https://vllm.ai/blog/2026-05-18-pegaflow) |
| vLLM | KV Offloading Connector | 2026 | 状态管理；运行时 | vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。 | [vLLM Blog](https://vllm.ai/blog/kv-offloading-connector) |
| llm-d | llm-d KV Cache | 2026 | Kubernetes；KV-aware routing | 用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。 | [GitHub](https://github.com/llm-d/llm-d-kv-cache) |
| IBM / Red Hat / Google 等 | UCCL | 2026 | 网络；KV transfer | GPU 通信库，覆盖 collectives、P2P KV cache transfer、RL weight transfer 和 expert parallelism，进入 llm-d 分布式推理栈。 | [GitHub](https://github.com/uccl-project/uccl) |
| Dell + NVIDIA + LMCache/vLLM | RDMA-Accelerated KV Cache Storage Offload | 2026 | 状态管理；存储 | 将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。 | [Dell InfoHub](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/) |
| KServe | KV Cache Offloading | 2025-2026 | Kubernetes；运行时 | 在 KServe generative inference 中集成 LMCache/vLLM KV offloading，面向云原生模型服务。 | [KServe Docs](https://kserve.github.io/website/docs/model-serving/generative-inference/kvcache-offloading) |
| Microsoft Research | Memento | 2026 | 长 CoT；状态压缩 | 训练模型把 CoT block 压成 dense memento，释放已经完成推理块的 KV，提升 reasoning serving 吞吐。 | [Microsoft Research](https://www.microsoft.com/en-us/research/articles/memento-teaching-llms-to-manage-their-own-context/) |
| Microsoft Research | Medha | 2025 | 长上下文；运行时 | 用 adaptive prefill chunking、Sequence Pipeline Parallelism、KV-Cache Parallelism 和 input-length-aware scheduling 支撑千万 token 精确推理。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/medha-efficient-llm-inference-on-multi-million-context-lengths-without-approximation/) |
| Microsoft Research | SPIN | 2026 | sparse attention；分层 KV | 把 sparse attention execution pipeline 与 CPU/GPU hierarchical KV storage 联合设计，解决不规则 KV subset 检索开销。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/unifying-sparse-attention-with-hierarchical-memory-for-scalable-long-context-llm-serving/) |
| Microsoft Research | KEEP | 2026 | 长程记忆；KV memory | Embodied planning 中用 KV-cache-centric memory management 替代原始文本记忆，减少频繁 KV 更新和重算。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/keep-a-kv-cache-centric-memory-management-system-for-efficient-embodied-planning/) |
| Microsoft Research | Online Scheduling with KV Cache Constraints | 2025 | 运行时；理论调度 | 将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/) |
| DeepSeek | DeepSeek-V3.2 / DeepSeek Sparse Attention | 2025-2026 | 模型结构；长上下文成本 | 在模型架构中加入 sparse attention/indexer，目标是在长上下文和 reasoning/agent 任务中降低推理成本。 | [arXiv](https://arxiv.org/abs/2512.02556) |
| Google / DeepSeek 相关研究 | Perfect Recall, Parallel Efficiency: MLA for Million-Token Decoding | 2026 | MLA；分布式长上下文 | 分析 DSA/MLA 在百万 token 分布式 decoding 中的全局 Top-K 同步瓶颈，并探索并行高效的精确召回路线。 | [Microsoft Research](https://www.microsoft.com/en-us/research/publication/perfect-recall-parallel-efficiency-multi-head-latent-attention-for-million-token-context-decoding/) |
| UC/industry collaboration | SYMPHONY | 2026 | compute-memory disaggregation | NSDI 2026 工作，将 KV cache storage 从 compute 解耦，形成满足严格延迟的 disaggregated memory management layer。 | [USENIX](https://www.usenix.org/conference/nsdi26/presentation/agarwal) |
| vLLM / Mooncake ecosystem | MooncakeStoreConnector | 2026 | 外部 KV store；vLLM | vLLM 文档化 MooncakeStoreConnector，支持 embedded 和 standalone-store 模式，扩展 CPU/SSD KV pool。 | [vLLM Docs](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/) |
| Apple / academic collaboration | SAW-INT4 | 2026 | 4-bit KV；系统感知量化 | 面向真实 serving 约束设计 4-bit KV cache quantization，考虑 paged layout、规则访存和 fused attention。 | [arXiv](https://arxiv.org/abs/2604.19157) |
| KVServe Team | KVServe | 2026 | KV 通信压缩；PD serving | 在分离式 LLM serving 中根据 workload、网络和 SLO 在线选择 KV compression profile，面向通信瓶颈。 | [arXiv](https://arxiv.org/abs/2605.13734) |
| University/industry collaboration | Tutti | 2026 | SSD-backed KV | 让 SSD-backed KV cache 接近 DRAM-backed LMCache 的性能，扩大长上下文服务的低成本 KV 容量。 | [arXiv](https://arxiv.org/abs/2605.03375) |

## 2026-06-11 追加：广域工业版图

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Alibaba Group | RTP-LLM | 2026 | 生产 runtime；PD 分离；多层 KV；量化 | 将并行加载、PD 分离、分层 KV 复用、模块化推测解码、自适应 KV 量化和多模态解耦整合进生产引擎，论文称已服务超过一亿用户。 | [A：arXiv](https://arxiv.org/abs/2605.29639) |
| Ant Group + vLLM 社区 | vLLM-Omni | 2026 | 多模态 serving；stage disaggregation | 用 stage graph 拆分 LLM、扩散模型和编码器，各阶段独立批处理、分配 GPU，并通过统一 connector 传递中间状态。 | [A：arXiv](https://arxiv.org/abs/2602.02204) / [A：GitHub](https://github.com/vllm-project/vllm-omni) |
| ByteDance Seed | MegaScale-Infer | 2025 | MoE serving；专家解耦 | 将 attention 和 MoE FFN 分池部署，以 disaggregated expert parallelism、ping-pong pipeline 和 M2N 通信提升专家利用率。 | [A：arXiv](https://arxiv.org/abs/2504.02263) |
| ByteDance Seed | SwiftSpec | 2025 | 推测解码；低延迟 | 异步扩展 draft/target 执行，配合 tree-aware KV 管理和 fused kernel，面向交互式单请求降低解码延迟。 | [A：arXiv](https://arxiv.org/abs/2506.11309) |
| Microsoft Research | MagicDec | 2025 | 长上下文；推测解码 | 联合优化 draft 与 target 的 KV cache，在长上下文下利用验证阶段相对便宜的特性打破 latency-throughput 冲突。 | [A：ICML 论文](https://arxiv.org/abs/2408.11049) |
| Together AI + Princeton 等 | Medusa | 2024-2026 | 推测解码；产品 runtime | 在目标模型上增加多组 decoding heads，一次预测并验证多个未来 token；其思想已进入主流 serving runtime。 | [A：ICML 论文](https://arxiv.org/abs/2401.10774) |
| Microsoft Research Asia + Peking University | EAGLE 系列 | 2024-2026 | 推测解码；feature drafting | 在目标模型内部 feature space 生成草稿并动态构建候选树，形成无需通用小模型的推测解码路线。 | [A：GitHub](https://github.com/SafeAILab/EAGLE) |
| NVIDIA | TensorRT-LLM Speculative Decoding | 2024-2026 | 产品 runtime；生成加速 | 在产品级 runtime 中集成 draft-target、Medusa、EAGLE 等推测策略，并与 inflight batching、量化和并行执行组合。 | [A：文档](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html) |
| AWS / Neuron 生态 | Trainium / Trainium3 + Neuron runtime | 2024-2026 | 专用硬件；编译器；算子 | 通过 Neuron Compiler、NKI kernel 和 Trainium 内存层级构建非 CUDA 推理栈，Trainium3 UltraServer 进一步把扩展单位提升到 144 芯片。 | [A：Neuron 文档](https://awsdocs-neuron.readthedocs-hosted.com/) / [B：AWS 发布](https://aws.amazon.com/blogs/aws/aws-trainium3-ultraservers-are-now-generally-available/) |
| Academic work on AWS Trainium | NeuronMM | 2025 | Trainium 算子；矩阵乘 | 针对 Trainium systolic array、SRAM 和特殊 layout 设计融合与缓存策略，展示专用硬件上端到端 LLM 推理优化空间。 | [A：arXiv](https://arxiv.org/abs/2510.25977) |
| Google Cloud | Ironwood TPU | 2025 | 推理专用芯片；scale-up | 第七代 TPU 明确以推理为中心，结合大规模 pod、HBM 和 Google 软件栈服务长上下文与 reasoning workload。 | [B：Google Cloud](https://cloud.google.com/tpu) |
| Google Cloud | TPU 8i / TPU 8t | 2026 路线图 | 推理专用芯片；agentic infrastructure | 第八代首次将 inference 优化的 8i 与 training 优化的 8t 分开，8i 强调片上 SRAM、内存带宽和低延迟互连；尚待正式交付验证。 | [C：ITPro 报道](https://www.itpro.com/infrastructure/google-cloud-eighth-generation-tpu-8t-8i-ai-inference-training) |
| AMD + HPE | Helios / Instinct MI455X rack-scale platform | 2026 路线图 | 机架级推理；开放互连 | 以 72 GPU、HBM4、EPYC 和 Ethernet scale-up fabric 构建开放机架方案，代表非 NVLink 的 rack-scale AI 路线。 | [C：Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/hpe-adopts-amd-helios-rack-architecture-for-2026-ai-systems) |
| Qualcomm | AI200 / AI250 | 2026-2027 路线图 | 推理专用加速器；近存计算 | 将 Hexagon NPU 扩展到数据中心，强调大容量 LPDDR、低比特格式、near-memory compute、机架扩展和 disaggregated inference。 | [C：Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-unveils-ai200-and-ai250-ai-inference-accelerators-hexagon-takes-on-amd-and-nvidia-in-the-booming-data-center-realm) |
| Cerebras | Wafer-scale Inference | 2024-2026 | 专用硬件；低延迟 API | 用 wafer-scale engine 和片上大容量存储减少跨芯片数据搬移，主攻极高 token/s 和交互式推理。 | [B：产品入口](https://www.cerebras.ai/inference) |
| Groq | GroqCloud / LPU Inference | 2024-2026 | 确定性执行；低延迟 | 用静态调度的 LPU 架构和编译器降低动态调度开销，主攻低 batch、稳定 token latency 的在线生成。 | [B：产品入口](https://groq.com/groqcloud) |
| Fireworks AI | Fireworks Inference Platform | 2024-2026 | 托管推理；模型定制 | 将高性能 runtime、量化、LoRA serving 和模型路由封装成推理云，代表独立 inference provider 的产品化路线。 | [B：官方文档](https://docs.fireworks.ai/) |
| Together AI | Together Inference Engine | 2024-2026 | 托管推理；推测解码；量化 | 将 FlashAttention、Medusa 等研究与多 GPU serving、量化和私有部署结合，形成模型云和企业推理平台。 | [B：官方文档](https://docs.together.ai/) |
| Baseten | Truss / TensorRT-LLM serving stack | 2024-2026 | 模型部署；自动扩缩容 | 把容器构建、模型打包、TensorRT-LLM 优化、流量伸缩和可观测性组合为生产推理平台。 | [B：官方文档](https://docs.baseten.co/) |
| Cloudflare | Workers AI | 2024-2026 | 边缘推理；全球调度 | 在分布式边缘网络上提供模型推理 API，将模型放置、流量路由和 serverless 调度下沉到全球基础设施。 | [B：官方文档](https://developers.cloudflare.com/workers-ai/) |
| Apple / MLX community | MLX-LM / vllm-mlx | 2024-2026 | 端侧推理；统一内存 | 利用 Apple silicon 统一内存和 MLX 图执行提供本地 LLM 推理，并开始向 continuous batching 和 vLLM API 兼容扩展。 | [A：MLX-LM](https://github.com/ml-explore/mlx-lm) / [A：vllm-mlx 论文](https://arxiv.org/abs/2601.19139) |
| vLLM maintainers / Inferact | vLLM 商业化 | 2026 | 开源 runtime；企业化信号 | vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。 | [C：TechCrunch](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/) |
| SGLang maintainers / RadixArk | SGLang 商业化 | 2026 | prefix reuse；企业化信号 | 围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。 | [A：SGLang](https://github.com/sgl-project/sglang) / [C：WSJ 报道](https://www.wsj.com/tech/ai/ai-computing-is-a-memory-hog-an-nvidia-backed-startup-has-an-answer-383a5710) |

### 本轮观察

- **推理仍是 AI infra 最热的增量市场之一**：模型训练次数有限，但 agent、搜索、代码生成、语音和多模态服务持续产生 token，成本中心自然转向 inference。
- **系统边界继续外扩**：优化对象从单 GPU attention kernel 扩展到 stage graph、KV state service、rack-scale fabric、外部存储和全局调度器。
- **分离式架构正在细化**：从简单的 prefill/decode 两分法，继续拆成 multimodal stages、attention/expert pools、draft/verify pipelines 和 compute/memory pools。
- **专用硬件开始按 workload 分叉**：TPU 8i、Qualcomm AI200/250、Cerebras、Groq 和 Trainium 都在押注 inference 的内存带宽、低精度、确定性执行或低延迟。
- **开源 runtime 出现商业化窗口**：vLLM 与 SGLang 团队的企业化动作说明，推理引擎、KV 管理和部署支持已形成独立产品层。
- **需要谨慎区分三类证据**：正式系统论文能说明机制，官方工程材料能说明可用性，融资和硬件路线图只能说明资本与产业预期。

## 2026-06-11 第二轮追加：生产软件栈与硬件生态

### 通用推理引擎与服务平台

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| vLLM / PyTorch Foundation | vLLM V1 | 2023-2026 | 通用 runtime；多后端 | 以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。 | [A：GitHub](https://github.com/vllm-project/vllm) / [A：文档](https://docs.vllm.ai/) |
| SGLang community | SGLang Runtime | 2024-2026 | agent runtime；KV 复用 | 用 RadixAttention 管理树状共享前缀，结合 structured generation、PD disaggregation、speculative decoding 和多模态 serving。 | [A：GitHub](https://github.com/sgl-project/sglang) / [A：文档](https://docs.sglang.ai/) |
| NVIDIA | TensorRT-LLM | 2023-2026 | NVIDIA runtime；量化；并行 | 提供 inflight batching、paged KV、FP8/FP4、speculative decoding、TP/PP/EP 和多节点执行，是 NVIDIA 平台的产品级 LLM 引擎。 | [A：GitHub](https://github.com/NVIDIA/TensorRT-LLM) |
| NVIDIA | Triton Inference Server | 2018-2026 | 模型服务；调度；可观测性 | 负责模型仓库、dynamic batching、ensemble、metrics 和多框架后端，常作为 TensorRT-LLM/vLLM 外层生产服务面。 | [A：GitHub](https://github.com/triton-inference-server/server) |
| Hugging Face | Text Generation Inference, TGI | 2022-2026 | 开源 serving；模型生态 | 面向 Hugging Face 模型提供 continuous batching、tensor parallelism、quantization、speculative decoding 和 OpenAI-compatible API。 | [A：GitHub](https://github.com/huggingface/text-generation-inference) |
| Microsoft | DeepSpeed-MII / DeepSpeed-FastGen | 2023-2026 | 高吞吐 serving；SplitFuse | 以 DeepSpeed-Inference 为底座，用 Dynamic SplitFuse、模型并行、量化和持久部署服务长 prompt 与 generation 混合负载。 | [A：GitHub](https://github.com/microsoft/DeepSpeed-MII) / [A：论文](https://arxiv.org/abs/2401.08671) |
| Meta / community | llama.cpp | 2023-2026 | 本地推理；CPU/GPU；量化 | 用 GGUF、低比特量化和多种 CPU/GPU/NPU backend 把本地 LLM 推理扩展到 PC、服务器、手机和嵌入式设备。 | [A：GitHub](https://github.com/ggml-org/llama.cpp) |
| MLC community | MLC-LLM | 2023-2026 | 编译部署；跨硬件 | 通过 Apache TVM/MLC 编译模型到 CUDA、ROCm、Metal、Vulkan、WebGPU 等后端，强调跨平台 kernel 生成和端侧部署。 | [A：GitHub](https://github.com/mlc-ai/mlc-llm) |
| InternLM / Shanghai AI Laboratory | LMDeploy | 2023-2026 | 国产 runtime；量化；服务 | TurboMind 与 PyTorch engine 支持 persistent batch、KV 管理、AWQ/低比特量化、TP 和多模态模型部署。 | [A：GitHub](https://github.com/InternLM/lmdeploy) |
| ModelTC community | LightLLM | 2023-2026 | 轻量 serving；kernel | 用 token attention、动态 batch、共享显存管理和定制 Triton kernel 提供低开销分布式 LLM serving。 | [A：GitHub](https://github.com/ModelTC/lightllm) |
| PaddlePaddle / Baidu | FastDeploy | 2022-2026 | 国产部署；多硬件 | 覆盖 Paddle、ONNX、TensorRT 和多类硬件后端，提供从模型压缩到服务部署的推理工具链。 | [A：GitHub](https://github.com/PaddlePaddle/FastDeploy) |
| Huawei Ascend | MindIE | 2024-2026 | Ascend serving；调度；算子 | 面向昇腾 NPU 提供 LLM 推理、服务化、并行执行、量化和调度能力，是国产算力生产栈的重要入口。 | [B：官方产品](https://www.hiascend.com/software/mindie) |
| Ray / Anyscale | Ray Serve LLM | 2024-2026 | 分布式服务；自动伸缩 | 将 vLLM 等 engine 包装为 Ray actor/deployment，提供多节点 replica、路由、autoscaling 和 Python 应用编排。 | [A：文档](https://docs.ray.io/en/latest/serve/llm/index.html) |
| BentoML | BentoML / BentoCloud | 2023-2026 | 模型打包；推理平台 | 统一模型容器、API、batching、资源声明和 autoscaling，并与 vLLM、SGLang、TensorRT-LLM 等 runtime 集成。 | [B：官方文档](https://docs.bentoml.com/) |
| KServe | Generative Inference | 2024-2026 | Kubernetes；模型服务 | 以 Kubernetes CRD、Gateway、autoscaling 和 ModelMesh 管理生成式服务，并接入 vLLM、Hugging Face、KV offload。 | [A：文档](https://kserve.github.io/website/docs/model-serving/generative-inference/overview) |
| Red Hat / IBM / Google / NVIDIA 社区 | llm-d | 2025-2026 | Kubernetes-native distributed inference | 将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。 | [A：GitHub](https://github.com/llm-d/llm-d) |

### 编译器、算子库与结构化生成

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| OpenAI / community | Triton | 2021-2026 | GPU DSL；kernel 编译 | 用 Python DSL 表达 tile-level GPU program，成为 vLLM、SGLang、FlashAttention 及企业自定义 attention/MoE kernel 的通用工具。 | [A：官方站点](https://triton-lang.org/) |
| NVIDIA | CUTLASS / CuTe DSL | 2017-2026 | GEMM；attention；模板库 | 提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives，是高性能低精度 kernel 的底层基石。 | [A：GitHub](https://github.com/NVIDIA/cutlass) |
| FlashInfer community / NVIDIA | FlashInfer kernel ecosystem | 2024-2026 | serving attention；JIT kernel | 针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。 | [A：GitHub](https://github.com/flashinfer-ai/flashinfer) |
| Microsoft Research / community | TileLang | 2025-2026 | GPU DSL；自动调优 | 将 tiled dataflow 与 layout、线程绑定、tensorization 和软件流水分离，降低编写高性能 attention/MoE kernel 的门槛。 | [A：GitHub](https://github.com/tile-ai/tilelang) |
| PyTorch | torch.compile / Inductor | 2023-2026 | 图编译；kernel fusion | 捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。 | [A：文档](https://docs.pytorch.org/docs/stable/torch.compiler.html) |
| PyTorch | FlexAttention | 2024-2026 | attention 编程模型 | 允许用户用 score modification 和 block mask 表达 attention variant，再由编译器生成 fused kernel，覆盖 sparse/paged inference。 | [A：文档](https://pytorch.org/blog/flexattention/) |
| MLC / CMU | XGrammar structured generation engine | 2024-2026 | 结构化生成；约束解码 | 预编译 grammar、持久化 parser stack 并与 GPU execution overlap，已进入多种 serving engine 的 JSON/tool-call fast path。 | [A：GitHub](https://github.com/mlc-ai/xgrammar) |
| Microsoft | ONNX Runtime GenAI | 2024-2026 | 跨平台生成式 runtime | 在 ONNX Runtime 上封装 generation loop、KV cache、sampling、量化和 CPU/GPU/NPU provider，面向 Windows 与边缘部署。 | [A：GitHub](https://github.com/microsoft/onnxruntime-genai) |
| Intel | OpenVINO GenAI | 2024-2026 | Intel CPU/GPU/NPU；端侧推理 | 为 Intel 硬件提供 stateful model、continuous batching、paged attention、量化和 speculative decoding pipeline。 | [A：GitHub](https://github.com/openvinotoolkit/openvino.genai) |
| Modular | MAX Engine | 2024-2026 | 编译器；异构 serving | 用 MAX graph/compiler 和 Mojo kernel 统一 CPU/GPU 推理，瞄准摆脱单一 CUDA runtime 的可移植高性能部署。 | [B：官方文档](https://docs.modular.com/max/) |

### 芯片后端与端侧生态

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| AMD | ROCm + vLLM/SGLang/TensorRT-LLM ecosystem | 2024-2026 | AMD GPU；开放软件栈 | 通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。 | [A：ROCm 文档](https://rocm.docs.amd.com/) |
| AMD | Instinct MI350 Series | 2025-2026 | 低精度推理；大 HBM | CDNA 4 引入 FP4/FP6 并提供 288 GB HBM3E，面向大模型、MoE 和长上下文的高容量推理。 | [B：产品页](https://www.amd.com/en/products/accelerators/instinct/mi350.html) |
| NVIDIA | Vera Rubin NVL72 | 2026 | rack-scale agentic inference；NVLink | 将 72 张 Rubin GPU、36 颗 Vera CPU、ConnectX-9 和 BlueField-4 组合为单一 NVLink 域，强调长上下文、低 cost/token 和 rack-scale RAS。 | [B：官方产品页](https://www.nvidia.com/en-us/data-center/technologies/rubin/) |
| NVIDIA | Groq 3 LPX for Vera Rubin | 2026 | 低延迟 inference；SRAM LPU | 在 Rubin 平台旁加入面向 agentic 低延迟和大上下文的 LPU rack，以大规模片上 SRAM 和高带宽 scale-up 补充 GPU 吞吐路径。 | [B：官方产品页](https://www.nvidia.com/en-us/data-center/technologies/rubin/) |
| Intel | Gaudi 2/3 software stack | 2024-2026 | 专用加速器；以太网 scale-out | 通过 SynapseAI、HCCL、FP8 和 vLLM/Optimum Habana 支持 LLM serving，以标准 Ethernet 和成本为差异点。 | [A：官方文档](https://docs.habana.ai/) |
| AWS | Inferentia2 + Neuron | 2023-2026 | 云端推理 ASIC | Inferentia2 以 Neuron compiler/runtime、NeuronLink 和多芯片实例服务低成本推理，与 Trainium 共享软件生态。 | [B：产品页](https://aws.amazon.com/machine-learning/inferentia/) |
| Google | JetStream / MaxText / Pathways on TPU | 2024-2026 | TPU serving；编译与调度 | 用 JAX/XLA、paged attention、模型并行和 TPU pod serving 构成 Gemini 与开源模型的 TPU 推理路径。 | [A：JetStream](https://github.com/AI-Hypercomputer/JetStream) |
| Meta / PyTorch | ExecuTorch | 2024-2026 | 移动端；边缘 runtime | 将模型导出到轻量 runtime，并通过 Core ML、QNN、XNNPACK、Vulkan 等 backend 在手机和嵌入式设备执行。 | [A：官方站点](https://pytorch.org/executorch/) |
| Google | LiteRT | 2024-2026 | Android；端侧生成式 AI | 在 TensorFlow Lite 演进基础上统一 CPU/GPU/NPU delegate 和生成式模型部署，服务 Android 与边缘设备。 | [A：官方文档](https://ai.google.dev/edge/litert) |
| Qualcomm | AI Engine Direct / QNN | 2024-2026 | Snapdragon NPU；端侧推理 | 通过 QNN graph、低比特量化和 Hexagon NPU backend 部署移动端 LLM/MLLM，强调隐私、能耗和离线能力。 | [B：官方入口](https://www.qualcomm.com/developer/software/qualcomm-ai-engine-direct-sdk) |
| Apple | MLX / Core ML | 2023-2026 | Apple Silicon；统一内存 | MLX 利用 unified memory 支持研究与本地生成，Core ML 负责产品端 CPU/GPU/ANE 部署，形成 Mac 与 iPhone 双层生态。 | [A：MLX](https://github.com/ml-explore/mlx) / [A：Core ML](https://developer.apple.com/machine-learning/core-ml/) |
| SambaNova Systems | SambaNova Cloud / RDU | 2024-2026 | dataflow accelerator；托管推理 | 用 reconfigurable dataflow unit 和模型编译栈提供高吞吐推理 API，属于非 GPU 专用加速路线。 | [B：官方站点](https://sambanova.ai/) |
| Tenstorrent | TT-Metalium / Wormhole | 2024-2026 | RISC-V AI accelerator；开放 kernel | 公开低层 TT-Metalium 编程栈和模型实现，探索可编程 many-core 芯片上的 LLM 推理。 | [A：GitHub](https://github.com/tenstorrent/tt-metal) |

### 扩散与多模态生成软件栈

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Hugging Face | Diffusers | 2022-2026 | 图像/视频/音频生成 runtime | 以统一 DiffusionPipeline 组合 model、scheduler、LoRA 和量化/offload/torch.compile 优化，是开源扩散推理的基础 API。 | [A：官方文档](https://huggingface.co/docs/diffusers/index) |
| xDiT community | xDiT | 2024-2026 | DiT 分布式推理；多维并行 | 为 diffusion transformer 提供 sequence、pipe、CFG、USP 等并行和通信优化，支撑高分辨率图像与长视频生成。 | [A：GitHub](https://github.com/xdit-project/xDiT) |
| Ant Group + vLLM | vLLM-Omni runtime | 2026 | any-to-any；统一 serving API | 将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。 | [A：GitHub](https://github.com/vllm-project/vllm-omni) |
| NVIDIA | TensorRT diffusion pipelines | 2024-2026 | diffusion kernel；低精度 | 通过 TensorRT、Model Optimizer 和定制 attention/GEMM kernel 加速 Stable Diffusion、Flux 和视频生成模型。 | [B：TensorRT](https://developer.nvidia.com/tensorrt) |

### 从论文进入生产的代表性案例

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Alibaba Cloud | COMET | 2025 | MoE 通信；生产集群 | 细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。 | [A：MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) |
| MIT Han Lab / NVIDIA ecosystem | QServe / OmniServe | 2024-2026 | W4A8KV4；低比特 serving | 将 4-bit 权重、8-bit 激活和 4-bit KV 与 SmoothAttention、重排及定制 kernel 联合设计。 | [A：GitHub](https://github.com/mit-han-lab/omniserve) |
| MLC / SGLang / vLLM ecosystem | XGrammar production integration | 2025-2026 | JSON；tool calling；约束生成 | 将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。 | [A：MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) |
| Meta | Context Parallelism for Million-Token Inference | 2025 | 长上下文；分布式 attention | 用 pass-KV/pass-Q 精确 ring attention 在常见数据中心网络上扩展百万 token prefill。 | [A：MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) |
| Microsoft Research | LeanAttention / TurboAttention | 2025 | decode kernel；量化 attention | 分别从精确 decode dataflow 和端到端量化 attention 两条路线降低长上下文 memory wall。 | [A：MLSys LeanAttention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html) / [A：MLSys TurboAttention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/f4f55846501f3336f293fd8b6de10770-Abstract-Conference.html) |
| NVIDIA / University of Washington | FlashInfer production integration | 2025-2026 | serving kernel；生态集成 | 从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。 | [A：MLSys 2025](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) |
| Microsoft Research + University of Edinburgh | WaferLLM on Cerebras WSE-2 | 2025 | wafer-scale inference；kernel | 以 PLMR 模型、MeshGEMM/MeshGEMV 和 wafer-scale parallelism 将 LLM inference 映射到数十万片上 core。 | [A：OSDI 2025](https://www.usenix.org/conference/osdi25/technical-sessions) / [A：GitHub](https://github.com/MeshInfra/WaferLLM) |
| Meta + OpenAI + UC San Diego | KPerfIR | 2025 | GPU profiling；Triton compiler | 把 profiling 逻辑实现为 compiler pass，为复杂 AI kernel 提供可扩展、可移植的细粒度性能分析。 | [A：OSDI 2025](https://www.usenix.org/conference/osdi25/technical-sessions) |
| Cambricon + ICT, CAS | QiMeng-Xpiler | 2025 | 跨硬件编译；kernel 移植 | 用 LLM 辅助生成和符号综合在 CUDA、HIP、VNNI、BANG 等异构接口间转译 tensor program。 | [A：OSDI 2025](https://www.usenix.org/conference/osdi25/technical-sessions) |

### NSDI 2026 工业信号

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Alibaba Group + Peking University | HydraServe | 2026 | serverless；冷启动 | 主动分发模型并重叠加载、runtime 初始化和 worker 启动，同时通过拓扑感知放置避免多实例网络争用。 | [A：NSDI 2026](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| Alibaba Group + Peking University | ServeGen | 2026 | 生产 workload；benchmark | 从全球云端 LLM 服务提取语言、多模态和 reasoning workload 特征，并开源按 client 组合的 trace generator。 | [A：GitHub](https://github.com/alibaba/ServeGen) / [A：NSDI 2026](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| Tencent | SwiftEP | 2026 | MoE 通信；all-to-all | 用 zero-copy buffer fusion、TMA offload、RDMA scatter-gather 和 CUDA IPC 优化 MoE prefill 通信，并降低 SM 占用。 | [A：NSDI 2026](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| Google DeepMind + UC Berkeley | Agentix | 2026 | agent serving；program scheduling | 将 agent program 的调用图、依赖和累计等待暴露给 scheduler，在 program 层而非单请求层做优先级和抢占。 | [A：NSDI 2026](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| Google + Cisco Research + UIUC | JITServe | 2026 | SLO；goodput；agent workload | 在请求长度和依赖信息不完整时渐进估计资源需求，以 grouped margin 算法分配刚好满足 SLO 的 serving capacity。 | [A：NSDI 2026](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| Anthropic + Mistral AI + AWS + academia | FlexLLM | 2026 | inference/finetuning co-serving | 在共享 GPU 上 token-level 融合 inference 和 PEFT finetuning，用图裁剪与 hybrid scheduling 保持在线 SLO。 | [A：NSDI 2026](https://www.usenix.org/conference/nsdi26/technical-sessions) |

### 评测与采购决策基础设施

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| MLCommons | MLPerf Inference | 持续更新 | 标准 benchmark；软硬件比较 | 以统一模型、精度规则、server/offline 场景和可审计 submission 比较数据中心及边缘推理系统。 | [A：官方结果](https://mlcommons.org/benchmarks/inference-datacenter/) |
| SemiAnalysis | InferenceMAX | 2025-2026 | 滚动 benchmark；TCO | 夜间滚动测试完整 driver/kernel/runtime/hardware 组合，以 tok/s/GPU、tok/s/user 和美元/百万 token 跟踪软件演进。 | [C：项目报道](https://www.tomshardware.com/tech-industry/inferencemax-ai-benchmark-tests-software-stacks-efficiency-and-tco-vendor-neutral-suite-runs-nightly-and-tracks-performance-changes-over-time) |
| Alibaba Group + Peking University | ServeGen traces | 2026 | 生产 trace；workload synthesis | 公开语言、多模态和 reasoning 服务的 client-level 统计与生成器，弥补只用 ShareGPT 合成流量的失真。 | [A：GitHub](https://github.com/alibaba/ServeGen) |
| Microsoft Research 等 | Inference evaluation anti-patterns | 2025 | 方法论；benchmark 审计 | 系统总结 baseline 公平性、workload 代表性和 metric 设计中的反模式，强调 burst、stall 与双阶段行为。 | [A：arXiv](https://arxiv.org/abs/2507.09019) |

## 2026-06-11 第三轮追加：正式会议中的企业系统方案

### ASPLOS 2026：运行时、调度与服务编排

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Snowflake AI Research | Shift Parallelism / Arctic Inference | 2026 | 动态并行；弹性服务 | 根据流量在 TP 与 sequence parallelism 间切换，并结合 speculative decoding、SwiftKV 和 embedding fast path。 | [A：ASPLOS 2026 program](https://www.asplos-conference.org/asplos2026/program/) / [A：arXiv](https://arxiv.org/abs/2507.11830) |
| Huawei + Tsinghua University + Shanghai AI Laboratory | XY-Serve | 2026 | Ascend serving；P/D/V 融合 | 用 token-wise 调度、动态任务分解、Meta-Attention 和 SmoothGEMM 处理 Ascend 上动态 shape 与混合阶段。 | [A：ASPLOS 2026 program](https://www.asplos-conference.org/asplos2026/program/) / [A：arXiv](https://arxiv.org/abs/2412.18106) |

### ASPLOS 2026：推测解码、MoE 与通信

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Microsoft | MSCCL++ | 2026 | GPU collective；通信编程 | 提供 primitive interface、通信 DSL 和优化 collective 库，已用于 Azure AI 服务并被 AMD RCCL 采用。 | [A：ASPLOS 2026 program](https://www.asplos-conference.org/asplos2026/program/) / [A：arXiv](https://arxiv.org/abs/2504.09014) |

### ASPLOS 2026：编译器、Kernel 与新型平台

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| OpenAI | Linear Layouts | 2026 | GPU 编译；tensor layout | 用统一代数表示组合 tensor 数据布局，降低复杂 GPU kernel 的映射、变换和代码生成难度。 | [A：ASPLOS 2026 program](https://www.asplos-conference.org/asplos2026/program/) |

### FAST 2026：模型加载、存储与有状态恢复

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Inspur + Huawei Cloud + Shanghai Jiao Tong University + Peking University | CacheSlide | 2026 | Agent KV 复用；位置校正 | 针对相对位置稳定但绝对位置变化的 agent prompt 片段，结合 RPDC、加权校正和 spill-aware KV 管理。 | [A：FAST 2026](https://www.usenix.org/conference/fast26/technical-sessions) |
| China Telecom + Tsinghua University | Bidaw | 2026 | 多轮会话；两级 KV 存储 | 让计算引擎按 KV 所在层和大小重排请求，同时由存储层利用模型响应预测后续访问与淘汰。 | [A：FAST 2026](https://www.usenix.org/conference/fast26/technical-sessions) |
| Huawei Technologies | PPC / MAIO programmable page cache | 2026 | 模型加载；弹性启动 | 用可插拔内核 page-cache policy、I/O template、XPU affinity 和数据局部性缩短模型加载。 | [A：FAST 2026](https://www.usenix.org/conference/fast26/technical-sessions) |
| Huawei Cloud + Shanghai Jiao Tong University | AITURBO | 2026 | AI 云存储；KV I/O | 借用加速器高带宽互连并提供 grouped I/O API，在存储层自动推导 checkpoint 和 KV-cache 读写优化。 | [A：FAST 2026](https://www.usenix.org/conference/fast26/technical-sessions) |
| Microsoft Research + University of Chicago | AdaptCache | 2025-2026 | KV 压缩；DRAM/SSD hierarchy | 按 KV entry 联合选择有损压缩方式、压缩率和存储位置，在生成质量与加载延迟之间做动态权衡。 | [A：arXiv / SOSP BigMem](https://arxiv.org/abs/2509.00105) |

### 第三轮趋势判断

- **推理已成为体系结构会议的主干议题。** ASPLOS 2026 不再只出现零散 LLM 论文，而是形成 serving throughput、latency/scheduling、speculative decoding、attention/KV、MoE 和 efficient inference 等连续专场。
- **存储系统正式进入推理关键路径。** FAST 2026 的 SolidAttention、CacheSlide、Bidaw、PPC/MAIO 与 AITURBO 分别覆盖 SSD-backed KV、跨位置 KV 复用、两级 KV 存储、模型加载和云端 KV I/O。
- **生产优化对象从单个 kernel 扩展到完整状态机。** Prefill、decode、verify、tool execution、KV restore 和 checkpoint/restore 需要被统一建模，单纯提高 GEMM 峰值已经不足以解释端到端收益。
- **通信编程与编译可靠性成为独立基础设施层。** MSCCL++、Linear Layouts、Triton-Sanitizer、KPerfIR 等工作说明企业正在建设可复用的 collective、layout、profiling 和 debugging 工具链。
- **Agent workload 改变缓存语义。** CacheSlide 的相对位置缓存、Bidaw 的多轮访问预测、Agentix 的程序级调度和 ServeGen 的生产 trace，表明未来系统要显式理解调用图、会话和可复用状态，而不只是 token 长度。
- **企业公开研究的分工开始清晰。** Snowflake 聚焦企业推理 runtime，Microsoft 深入 collective 和 serving 调度，OpenAI 改造 Triton 编译基础，Huawei 同时覆盖 Ascend kernel、模型加载和云存储数据路径。

## 2026-06-12 第四轮追加：芯片体系结构、数据系统与生产工具链

### 正式会议中的企业研究

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Microsoft Research India | QoServe | 2026 | 多服务池；资源共享 | 统一管理原本按 workload 或服务等级隔离的 LLM serving silo，提高集群资源复用。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Alibaba Group + Zhejiang University | BAT | 2026 | 生成式推荐；bipartite attention | 为生成式推荐设计 bipartite attention 和 serving 数据流，降低推荐上下文处理成本。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| ByteDance Seed + Peking University + SJTU | LAER-MoE | 2026 | MoE；expert layout | 根据 expert 负载动态重排布局；虽然论文面向训练，但其 expert placement 方法直接影响统一训练推理集群。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Tencent YouTu Lab + Peking University | TPLA | 2026 | MLA；PD 分离；Tensor Parallel | 将 Tensor Parallel 与 Latent Attention 结合，降低 prefill/decode 分离场景中的 KV 和 collective 压力。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| IBM Research + RPI + UMass Amherst | STARC | 2026 | PIM；选择性 KV 访问 | 在 PIM 系统中对关键 token 做选择、重映射和聚类，减少 decode 阶段的 KV 数据移动。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| NVIDIA Research + Penn State | AGIO | 2026 | GPU I/O；异步执行 | 重新设计 GPU 异步 I/O 路径，使模型状态和数据搬运能够更充分地与 GPU 计算重叠。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| China Telecom | gShare | 2026 | GPU sharing；FaaS | 在多租户 serverless 平台中采用激进 GPU 共享和调度，面向短时突发 AI function 提高利用率。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Alibaba Group + SJTU + Zhejiang University | GFS | 2026 | Spot GPU；抢占调度 | 预测 spot instance 风险并进行 preemption-aware GPU scheduling，减少任务重启和集群浪费。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Google + Meta + Anthropic + George Mason University | Triton-Sanitizer | 2026 | GPU kernel 调试；可靠性 | 为 Triton kernel 提供跨设备内存 sanitizer 和丰富诊断上下文，降低自定义推理 kernel 的生产风险。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Huawei + Shanghai Jiao Tong University | M2XFP | 2026 | 低比特格式；硬件协同 | 用少量 metadata 扩展 microscaling 格式，在规则低比特执行和模型精度之间取得更好平衡。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Alibaba Cloud | RedFuser | 2026 | 编译器；operator fusion | 自动融合 cascaded reduction，减少 AI accelerator 上的中间内存流量和 kernel launch。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Lightmatter + Cornell University | Torus fabric for multi-tenant ML | 2026 | 光互连；multi-tenant collective | 重构 torus fabric 以降低多租户 ML workload 之间的通信干扰，代表光互连进入 AI scale-up/scale-out 设计。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Microsoft + NVIDIA + Virginia Tech | Heterogeneous Memory Predictability | 2026 | CXL/异构内存；性能建模 | 研究不同内存层的延迟与带宽可预测性，为模型和 KV 分层放置建立系统依据。 | [A：ASPLOS 2026](https://www.asplos-conference.org/asplos2026/program/) |
| Intel + University of Illinois Urbana-Champaign | DECA | 2025 | 权重解压；near-core accelerator | 用三维 roofline 指导 near-core 解压单元设计，使压缩模型不被在线解码开销抵消。 | [A：MICRO 2025 / arXiv](https://arxiv.org/abs/2505.19349) |
| IBM + University of Illinois Urbana-Champaign | Chameleon | 2025 | 多 Adapter；缓存与调度 | 联合管理 adapter 缓存和请求调度，面向大量 LoRA tenant 减少换入及排队。 | [A：MICRO 2025 / arXiv](https://arxiv.org/abs/2411.17741) |

### 数据库与 RAG 系统层

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| AlayaDB AI + academia | AlayaDB | 2025 | 长上下文；向量数据库；Attention | 将 KV cache 和 attention 处理抽象为数据库查询，由 query optimizer 决定索引、放置和执行计划。 | [A：arXiv](https://arxiv.org/abs/2504.10326) |
| VectorLiteRAG team | VectorLiteRAG | 2025 | RAG；CPU/GPU 索引分区 | 根据向量簇访问偏斜决定哪些 index 常驻 HBM，并联动 LLM batch size 平衡检索和生成阶段。 | [A：arXiv](https://arxiv.org/abs/2504.08930) |
| RAG-Stack team | RAG-Stack | 2025 | RAG optimizer；质量性能协同 | 用 RAG IR、成本模型和 plan explorer 联合搜索数据库、retrieval 和 generation 配置。 | [A：arXiv](https://arxiv.org/abs/2510.20296) |

### 最新芯片与跨平台部署信号

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Microsoft | Maia 200 | 2026 | Azure 自研推理芯片；FP4/FP8 | 面向 Azure AI inference 设计低精度 tensor core、片上 SRAM、定制 DMA 与 NoC，并开始用于 Microsoft 内部 AI 服务。 | [C：TechRadar](https://www.techradar.com/pro/microsoft-unveils-maia-200-its-powerhouse-accelerator-looking-to-unlock-the-power-of-large-scale-ai) |
| Google TPU ecosystem | Gemma 4 on vLLM-TPU | 2026 | TPU serving；GPU 对比 | 展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。 | [A：arXiv](https://arxiv.org/abs/2605.25645) |
| AMD ROCm ecosystem | MI325X architecture-aware deployment study | 2026 | ROCm；AITER；多模型架构 | 说明 MLA、GQA、MoE 和视觉模型需要不同的 AITER、KV offload 与 block-size 配置，不能沿用统一参数。 | [A：arXiv](https://arxiv.org/abs/2603.10031) |
| Open Compute numerical-format ecosystem | MX-SAFE | 2026 | Microscaling；训练推理统一格式 | 动态切换 mantissa/exponent 模式，使低精度格式同时覆盖 direct-cast inference 和训练需求。 | [A：arXiv](https://arxiv.org/abs/2605.24391) |

### 第四轮趋势判断

- **“硬件峰值”正在让位于“数据路径匹配”。** ISCA、HPCA、MICRO 的论文大量围绕 KV、权重解压、flash、PIM、NDP-DIMM、3D DRAM 和低比特格式，说明推理瓶颈主要落在容量与搬运。
- **低比特不再只是量化算法。** LUT Tensor Core、BitMoD、Anda、M-ANT、MX+、M2XFP、MX-SAFE 都在共同设计数据格式、kernel、解码路径和硬件单元。
- **RAG 的优化边界开始跨越数据库与模型 runtime。** AlayaDB、VectorLiteRAG、RetroInfer、RAG-Stack 都把 index placement、attention、KV 和 generation SLO 放进同一个优化问题。
- **端侧大模型正在转向存储计算协同。** AiF、Lincoln、FACIL、InstAttention 和 SolidAttention 表明 flash、DRAM/PIM 与 SSD 不再只是被动容量层。
- **企业 AI infra 竞争逐渐形成三层。** 上层是 vLLM/SGLang/Dynamo 等 runtime，中层是 Triton/MSCCL++/AITER 等 kernel 与通信库，底层是 Rubin、MI350、TPU、Trainium、Maia 等芯片及机架系统。

## 2026-06-12 第五轮追加：云操作系统、AI 网络与奠基软件栈

### 云端 Serving、状态恢复与长尾模型市场

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Huawei Cloud + NUS + SJTU | CachedAttention | 2024 | 多轮会话；分层 KV cache | 用 DRAM/SSD 分层保存跨轮 KV，配合 layer-wise preload、异步保存和 scheduler-aware eviction 降低 TTFT。 | [A：USENIX ATC 2024](https://www.usenix.org/conference/atc24/technical-sessions) |
| Huawei Cloud + SJTU | Jiagu | 2024 | Serverless；冷启动；资源利用 | 通过 pre-decision scheduling 与 dual-staged scaling 提高函数部署密度并减少扩缩容冷启动。 | [A：USENIX ATC 2024](https://www.usenix.org/conference/atc24/technical-sessions) |
| IBM Research + UIUC | μ-Serve | 2024 | 能耗感知 serving；DVFS | 联合优化模型 multiplexing 和 GPU frequency scaling，在不违反 SLO 的情况下调低功耗。 | [A：USENIX ATC 2024](https://www.usenix.org/conference/atc24/technical-sessions) |
| Huazhong University of Science and Technology + Inria | StreamBox | 2024 | Serverless inference；GPU sandbox | 用轻量 GPU stream sandbox 替代每个 function 的独立 CUDA context，降低启动、显存和通信开销。 | [A：USENIX ATC 2024](https://www.usenix.org/conference/atc24/technical-sessions) |
| Microsoft Research Asia | T-MAC | 2024-2025 | CPU/边缘 LLM；查表低比特 | 以 lookup table 替代低比特乘法路径，在 CPU、移动端和 WebAssembly 上部署量化模型。 | [A：EuroSys 2025](https://2025.eurosys.org/program.html) / [A：GitHub](https://github.com/microsoft/T-MAC) |
| ByteDance | Robust LLM Training Infrastructure | 2025 | 生产可靠性；故障恢复 | 汇总大规模模型集群的故障检测、网络异常、恢复和作业治理经验，可直接迁移到推理平台 SRE。 | [A：SOSP 2025](https://dblp.org/db/conf/sosp/sosp2025.html) |

### 网络、Collective 与机架级通信

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| ByteDance | Astral | 2025 | 超大规模 AI 网络 | 从拓扑、路由、拥塞控制和作业编排构建大模型数据中心网络，是企业 AI fabric 的生产案例。 | [A：SIGCOMM 2025](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) |
| ByteDance | ByteScale | 2025 | 超长上下文；16K GPU 通信 | 针对 2048K context 和 16384 GPU 优化通信与并行，体现长上下文对 fabric 的极端需求。 | [A：SIGCOMM 2025](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) |
| ByteDance | Jakiro | 2025 | VPC；RDMA/TCP | 在虚拟私有云中统一 RDMA 与 TCP，兼顾 AI 网络性能、隔离和云网络可运维性。 | [A：SIGCOMM 2025](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) |
| Alibaba Cloud | Stellar RDMA Network | 2025 | 云 AI 网络；拥塞控制 | 为云端 AI workload 重构 RDMA 可靠性、拥塞控制和多租户隔离。 | [A：SIGCOMM 2025](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) |
| Microsoft Research + Clemson + Harvard | HACK | 2025 | PD 分离；KV 通信压缩 | 在压缩域执行部分 attention 计算，减少 KV 传输和反复压缩解压。 | [A：SIGCOMM 2025 / arXiv](https://arxiv.org/abs/2502.03589) |
| Microsoft | MSCCL / MSCCL++ | 2021-2026 | Collective compiler；AI 通信 | 用 DSL、通信 primitive 和拓扑搜索生成高效 collective，服务 Azure AI、NCCL/RCCL 生态。 | [A：GitHub](https://github.com/microsoft/msccl) / [A：MSCCL++](https://github.com/microsoft/mscclpp) |
| NVIDIA | NCCL | 持续更新 | GPU collective；NVLink/IB | 提供 all-reduce、all-to-all、broadcast 等 GPU collective，是 TP、PP、EP 和 MoE 推理的默认通信层。 | [A：GitHub](https://github.com/NVIDIA/nccl) |
| NVIDIA / Linux Foundation ecosystem | UCX | 持续更新 | RDMA；统一通信抽象 | 统一 InfiniBand、RoCE、shared memory、CUDA memory 等传输，为 MPI、NCCL 和分布式 runtime 提供底层能力。 | [A：GitHub](https://github.com/openucx/ucx) |
| Meta | Gloo | 持续更新 | Collective；CPU/GPU backend | 为 PyTorch distributed 提供跨 TCP、IB 等传输的 collective backend，是控制面和非 NCCL 路径的基础组件。 | [A：GitHub](https://github.com/facebookincubator/gloo) |

### 奠基 Runtime、MoE 与推理库

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| NVIDIA | Megatron-LM / Megatron-Core | 2019-2026 | Tensor/Sequence/Expert Parallel | 建立 tensor parallel 等核心拆分，并发展为支持 TP、PP、CP、EP 的大模型训练推理核心库。 | [A：GitHub](https://github.com/NVIDIA/Megatron-LM) |
| NVIDIA | FasterTransformer | 2020-2023 | Transformer kernel；模型并行 | 用融合 CUDA kernel、GEMM 调优、量化和多 GPU 并行提供早期生产级 Transformer 推理库，后续能力并入 TensorRT-LLM。 | [A：GitHub](https://github.com/NVIDIA/FasterTransformer) |
| Tencent | TurboTransformers | 2021 | 动态 batch；GPU serving | 按序列长度动态组织 batch，并通过融合 kernel 和内存管理加速 Transformer 在线服务。 | [A：PPoPP 2021 / GitHub](https://github.com/Tencent/TurboTransformers) |
| ByteDance | LightSeq | 2021-2023 | Transformer inference；CUDA fusion | 通过 fused layer、定制 CUDA kernel 和显存复用部署 NLP 与生成模型。 | [A：GitHub](https://github.com/bytedance/lightseq) |
| Microsoft | DeepSpeed-Inference | 2022-2026 | 超大模型推理；并行；量化 | 以 inference-adapted parallelism、kernel injection、量化和 heterogeneous memory 支撑超大 Transformer。 | [A：DeepSpeed](https://www.deepspeed.ai/tutorials/inference-tutorial/) |
| Microsoft | DeepSpeed-MoE | 2022 | MoE 训练与推理 | 联合 expert parallel、通信优化和模型压缩，使稀疏大模型的推理成本可控。 | [A：论文](https://arxiv.org/abs/2201.05596) |
| Microsoft Research Asia | Tutel | 2022-2026 | MoE runtime；adaptive parallelism | 提供自适应 expert parallel、all-to-all、fused kernel 和动态配置，是通用 MoE 软件栈的重要来源。 | [A：GitHub](https://github.com/microsoft/tutel) |
| Databricks / Stanford ecosystem | MegaBlocks | 2023-2026 | Block-sparse MoE | 用 block-sparse operation 替代 capacity padding，为高效 MoE kernel 和 serving 提供基础。 | [A：GitHub](https://github.com/databricks/megablocks) |
| Tsinghua University | FasterMoE | 2022 | MoE 调度；拓扑通信 | 用 expert shadowing、smart scheduling 和 topology-aware communication 缓解动态路由不均。 | [A：GitHub](https://github.com/thu-pacman/FasterMoE) |
| Intel | oneCCL | 持续更新 | Intel collective；CPU/GPU | 为 Intel CPU/GPU 集群提供 collective communication，并接入 PyTorch、oneAPI 与分布式 AI 软件。 | [A：GitHub](https://github.com/uxlfoundation/oneCCL) |

### RAG 与向量检索生产生态

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| Meta | Faiss | 2017-2026 | 向量检索；GPU ANN | 提供 IVF、PQ、HNSW、GPU k-selection 等索引，是自建 RAG 和向量检索 benchmark 的基础库。 | [A：GitHub](https://github.com/facebookresearch/faiss) |
| Google Research | ScaNN | 2020-2026 | 最大内积；量化 ANN | 用 anisotropic vector quantization、partitioning 和 reordering 提供高召回低延迟检索。 | [A：GitHub](https://github.com/google-research/google-research/tree/master/scann) |
| Microsoft Research | DiskANN / FreshDiskANN / SPFresh | 2019-2026 | SSD ANN；动态索引 | 以 SSD-resident graph 支撑十亿级搜索，并逐步加入动态更新和在线索引维护。 | [A：GitHub](https://github.com/microsoft/DiskANN) |
| Zilliz / LF AI & Data | Milvus | 2019-2026 | 云原生向量数据库 | 将 query、index、data、storage 节点解耦，并支持多索引、标量过滤、GPU 和分布式扩展。 | [A：GitHub](https://github.com/milvus-io/milvus) |
| NVIDIA RAPIDS | cuVS / CAGRA | 2023-2026 | GPU 向量搜索；RAG | 提供 GPU graph ANN、IVF、brute-force 和多节点能力，并被向量数据库用于 GPU 加速。 | [A：GitHub](https://github.com/rapidsai/cuvs) |
| Microsoft Research + academia | VBASE | 2023 | ANN + relational query | 将向量近邻搜索、关系过滤和查询 optimizer 放在同一数据库执行模型中。 | [A：OSDI 2023](https://www.usenix.org/conference/osdi23/presentation/zhang-qianxi) |
| Spotify | Annoy | 2013-2026 | 只读 ANN；内存映射 | 用随机投影树和 mmap 提供简单稳定的静态向量索引，适合中小规模只读检索服务。 | [A：GitHub](https://github.com/spotify/annoy) |
| NMSLIB community | HNSW / hnswlib | 2016-2026 | 图 ANN；内存索引 | HNSW 成为多数向量数据库的默认高召回内存索引，也决定 RAG 的内存成本和更新行为。 | [A：GitHub](https://github.com/nmslib/hnswlib) |

### 新一轮工业趋势判断

- **推理系统开始具备操作系统形态。** Pie、LithOS、PhoenixOS、Jenga、Mercury 不再只优化请求，而是在管理程序、GPU、远程内存和 checkpoint 生命周期。
- **网络成为推理成本模型的一部分。** HACK、KVServe、MSCCL++、NIXL、Stellar、Jakiro 表明 KV transfer、all-to-all 和 rack/region fabric 必须与 scheduler 联合设计。
- **长尾模型和 Adapter 正在形成独立市场。** Aegaeon、DeltaZip、Chameleon、Symbiosis、LoRAServe 分别处理模型池、参数增量、adapter cache 和训练推理共存。
- **Serverless 推理重点从容器启动转向 GPU runtime 启动。** StreamBox、Jiagu、HydraServe、PPC/MAIO 分别优化 CUDA context、函数伸缩、模型分发和 page cache。
- **成熟工业栈具有明显技术谱系。** FasterTransformer、LightSeq、DeepSpeed、Megatron、Tutel 等早期项目的 kernel、并行和通信设计，正在 TensorRT-LLM、vLLM、SGLang、Dynamo 中重新组合。

## 按四个方向的重点材料

### 1. 推理执行与运行时优化

优先读：

1. NVIDIA Dynamo：工业界最新“组合式 runtime”样板，包含 disaggregation、KV routing、offload、NIXL。
2. Microsoft Splitwise / DynamoLLM：一个讲 phase splitting，一个讲能耗/成本/SLO 动态配置。
3. Huawei P/D-Serve、Alibaba FlowKV、Moonshot Mooncake：国内大规模分离式 serving 与 KV 传输/存储路线。
4. Meta TP/CP/EP、vLLM V1：并行策略、runtime 和编译融合的真实工程方向。
5. Alibaba Aegaeon：多模型、serverless、token-level autoscaling，是成本优化和运行时调度的工业样板。
6. vLLM x Mooncake Store、PegaFlow、llm-d KV cache：2026 年外部 KV store 和 KV-aware routing 已经开始成为主流 runtime 接口。

常见工业设计模式：

- 把 prefill 和 decode 拆开，因为前者偏 compute-bound，后者偏 memory-bandwidth-bound。
- 用 chunked prefill 和 continuous batching 填平 GPU 空泡。
- 对长 CoT / agent workload，不能只优化单请求 latency，还要优化 goodput、P99、SLO attainment。
- 多模型场景下，GPU pool 和 token-level scheduling 比 request-level 独占更接近生产需求。

### 2. 长上下文与状态管理

优先读：

1. ShadowKV：ByteDance 的代表性长上下文 KV offload + sparse retrieval 工作。
2. RetroInfer：Microsoft 把 KV cache 看作 vector storage，是“状态管理数据库化”的强路线。
3. LMCache / llm-d：把 KV cache 抽成服务层，适合企业多应用、多 runtime 共享。
4. Mooncake / P/D-Serve / FlowKV：从系统架构侧解决 KV transfer 和存储放置。
5. NVIDIA BlueField-4 STX、Huawei UCM：从硬件/多层内存侧解决 context memory 问题。
6. FlexKV、InfiniStore、MooncakeStoreConnector、KVBM：说明 KV cache 正在从单机 buffer 演进成跨节点共享状态层。

常见工业设计模式：

- KV cache 不再只是 attention 的临时 buffer，而是可复用、可迁移、可查询、可分层放置的系统状态。
- 长上下文场景里，CPU DRAM、NVMe、DPU/CXL、远端 KV store 都会进入设计空间。
- RAG 和多轮 agent 的关键不是“缓存是否存在”，而是 cache key、位置编码、权限隔离、失效策略和复用粒度。

### 3. 压缩与成本优化

优先读：

1. DeepSeek MLA：模型结构直接压缩 KV cache，是比外部压缩更底层的成本路线。
2. Google TurboQuant：训练无关的极低比特 KV/向量量化路线。
3. NVIDIA NVFP4/FP8 KV cache：硬件格式、runtime 和 kernel 一体化。
4. RocketKV、ThinKV、KVTC、LookaheadKV：分别代表 sparse selection、reasoning/thought-aware compression、transform coding、future-aware eviction。
5. Aegaeon / DynamoLLM：不只压模型，还压部署成本、能耗和 GPU 数量。
6. Memento、DeepSeek Sparse Attention、SAW-INT4：分别代表 CoT 自压缩、模型结构稀疏化和系统感知 KV 量化三条新路线。

常见工业设计模式：

- KV cache 压缩需要分清是 capacity bottleneck、bandwidth bottleneck、transfer bottleneck 还是 reuse bottleneck。
- reasoning/长 CoT 场景比普通 long-context QA 更脆弱，FP8/4-bit KV 可能损伤精确召回或推理链。
- 成本优化越来越偏“系统 + 算法 + 硬件格式”共同设计，而不是单独做 quantization。

### 4. 算子与编译优化

优先读：

1. DeepSeek FlashMLA / DeepGEMM：企业开源的高性能 MLA decode 和 FP8 GEMM 样板。
2. PyTorch FlexAttention + FlashAttention-4：用编译器生成可定制 attention kernel 的代表路线。
3. FlashInfer：serving-oriented attention engine，覆盖 paged KV、decode/prefill kernel。
4. TensorRT-LLM attention kernels：工业产品级 MHA/MQA/GQA + FP8/INT8 KV 实现。
5. Ragged Paged Attention for TPU：说明 TPU 上也在补齐 GPU 生态里的 paged/ragged inference kernel。
6. NIXL、UCCL、Mooncake Transfer Engine：KV transfer 本身已经成为底层“算子/通信库”优化对象。

常见工业设计模式：

- decode 是小 batch、长 KV、强带宽约束；prefill 是大矩阵、compute-bound；两者 kernel 不能一套打天下。
- Paged KV 带来内存管理优势，但会引入 gather、non-contiguous access 和 kernel 复杂度。
- FP8/NVFP4/MLA/MoE 只有配套 kernel 成熟后，系统收益才会落地。

## 企业路线图对比

| 公司/生态 | 主要路线 | 可借鉴点 | 风险/局限 |
|---|---|---|---|
| NVIDIA | 软硬件全栈：TensorRT-LLM + Dynamo + NIXL + Blackwell/NVFP4/STX | 最接近工业落地全链路，适合看生产栈怎么拆层 | 强绑定 NVIDIA 生态，部分结论不一定可迁移 |
| ByteDance | 长上下文 sparse retrieval/offload：ShadowKV | 长上下文 KV offload 与高吞吐 retrieval 思路清晰 | 实现复杂，依赖 sparse attention pattern 稳定性 |
| DeepSeek | 模型结构 + kernel 共同设计：MLA + FlashMLA + DeepGEMM | 证明“模型结构改变 KV 形态”对 inference 成本影响巨大 | 需要模型训练/迁移配合，不是纯 serving 层可插拔 |
| Google | TPU serving + 量化：JetStream/MaxText/TurboQuant | TPU 运行时和极低比特向量量化值得跟踪 | TurboQuant 是否进入 Gemini 生产栈未公开 |
| Microsoft | phase split、vector-storage KV、multi-model KV sharing | 很多问题来自真实 enterprise multi-LLM 场景 | 部分系统论文代码/生产细节不完全开放 |
| Meta/PyTorch | runtime + compiler + kernel API：vLLM、FlexAttention、torch.compile | 开源生态影响大，适合做可复现实验 | 企业内部 Meta AI serving 细节仍有限 |
| Huawei/Ascend | NPU 生态下的 P/D serving、UCM、Ascend-vLLM | HBM 受限和国产 NPU 环境下很有参考价值 | 公开材料质量参差，需要区分论文和宣传口径 |
| Alibaba | FlowKV、Aegaeon、BladeLLM、Tair KVCache | 多模型 marketplace / serverless serving 的工业味很重 | 一些成果未完全开源，细节依赖云平台 |
| AWS | Trainium + Neuron Compiler/NKI | 可观察非 CUDA 专用加速器如何形成编译器、kernel 和 serving 软件栈 | 生态和可移植性弱于 CUDA，公开生产数据有限 |
| Google Cloud | JetStream/MaxText + Ironwood/TPU 8i | 展示模型、编译器、互连、芯片一体化的推理 co-design | 8i 属于 2026 路线图，交付后的真实性能仍需复核 |
| AMD/HPE | Helios + MI455X + Ethernet scale-up | 开放机架和 Ethernet scale-up 是 NVLink 之外的重要路线 | 当前主要是路线图和合作发布，成熟软件栈仍待验证 |
| Qualcomm | AI200/AI250 + Hexagon | 低功耗 NPU、LPDDR/近存计算进入数据中心推理的激进尝试 | 2026-2027 交付计划尚未形成可复现实测 |
| 独立推理云 | Cerebras、Groq、Fireworks、Together、Baseten | 直接围绕 token latency、吞吐、模型定制和 TCO 产品化 | 公开 benchmark 容易受模型、batch、提示长度和计费口径影响 |
| 开源 runtime 商业化 | Inferact/vLLM、RadixArk/SGLang | 说明 runtime 和 KV-aware serving 正形成独立企业软件层 | 公司动作不等同于技术领先，仍要回到开源版本和可复现测试 |

## 持续追踪清单

建议每月固定检查：

- NVIDIA Technical Blog / Dynamo docs / TensorRT-LLM release notes
- vLLM Blog / vLLM docs：Mooncake Store、PegaFlow、KV offloading connector、external KV connector
- Microsoft Research systems publications：NSDI、OSDI、VLDB、SOSP、EuroSys
- ByteDance Seed publications / GitHub
- ByteDance InfiniStore / Tencent FlexKV / Mooncake Store / LMCache / llm-d
- DeepSeek GitHub：FlashMLA、DeepGEMM、DeepEP、模型技术报告
- Google Research Blog / Google Cloud TPU docs / arXiv Google Research
- Meta Engineering / PyTorch blog / vLLM release notes
- Huawei Ascend / MindSpore / vLLM Ascend docs
- Alibaba Cloud community / PAI BladeLLM / Tair KVCache
- 顶会列表：OSDI、SOSP、NSDI、FAST、ASPLOS、ISCA、MICRO、HPCA、EuroSys、MLSys、SIGMOD、VLDB、ICML、NeurIPS、ICLR、ACL、EMNLP

建议追踪关键词：

- `LLM inference disaggregated serving`
- `prefill decode disaggregation KV cache transfer`
- `KV cache offloading long-context LLM`
- `KV cache reuse prefix cache multi-turn agent`
- `KV cache compression reasoning models`
- `FP8 KV cache NVFP4 KV cache`
- `MLA FlashMLA DeepGEMM inference`
- `PagedAttention FlexAttention FlashInfer`
- `LLM inference scheduler goodput SLO`
- `context memory storage agentic AI`
- `external KV cache connector vLLM`
- `distributed KV cache store Mooncake FlexKV InfiniStore`
- `KV cache communication compression disaggregated serving`
- `multimodal stage disaggregation diffusion LLM serving`
- `MoE disaggregated expert parallelism serving`
- `speculative decoding production inference runtime`
- `inference optimized accelerator rack scale HBM`
- `agentic inference infrastructure state management`
- `vLLM SGLang commercialization inference startup`

## 研究材料使用建议

如果目标是写“工业界如何解决 LLM 推理系统”的综述，建议结构如下：

1. 先讲 workload 变化：从短问答到长上下文、RAG、多轮 agent、长 CoT reasoning。
2. 再讲瓶颈迁移：从 GEMM/FLOPs 到 KV cache 容量、HBM 带宽、跨节点/跨层存储传输、P99 SLO。
3. 按四层展开方案：runtime scheduling、state/KV management、compression/cost、kernel/compiler。
4. 用企业案例串联：NVIDIA 全栈、DeepSeek 模型-算子协同、ByteDance ShadowKV、Microsoft RetroInfer/DroidSpeak、Huawei P/D-Serve、Alibaba FlowKV/Aegaeon。
5. 最后总结未解决问题：长 CoT 保真、cache 复用隔离、跨模型 KV 兼容、多层存储一致性、kernel 与动态 shape 的矛盾。
