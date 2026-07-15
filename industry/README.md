# Industry & Open-Source Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Academic papers](../papers/README.md)

A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then use the abstraction sections to compare mechanism, artifact, hardware, and serving evidence.

## At a Glance

| Records | Industrial material | With artifact | Tagged records |
|---:|---:|---:|---:|
| 121 | 121 | 121 | 114 |

## Collection Navigation

- [KV State & Memory](#kv-state-memory) (38)
- [P/D Disaggregation & KV Transfer](#p-d-disaggregation-kv-transfer) (12)
- [KV Compression & Low-Bit State](#kv-compression-low-bit-state) (22)
- [Kernel & Compiler](#kernel-compiler) (24)
- [Runtime & Serving](#runtime-serving) (20)
- [Reliability & Benchmarks](#reliability-benchmarks) (5)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Featured | A small editorial starting set; all records remain below. |

## Resource List

### KV State & Memory (38)

KV blocks, prefix state, offload, external memory, and memory-aware serving.

#### Featured

- **Featured:** **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `memory` `tensorrt-llm` `vllm`
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。
- **Featured:** **[SGLang 商业化](https://github.com/sgl-project/sglang)**
  `SGLang maintainers / RadixArk` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `sglang`
  围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。
- **Featured:** **[LMCache](https://arxiv.org/abs/2510.09665)**
  `LMCache 社区 / 企业采用` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `kv-cache` `rag` `lmcache`
  将 KV cache 抽成独立层，支持跨 engine/query 复用和 GPU/CPU/storage/network 多层编排。
- **Featured:** **[Mooncake](https://www.usenix.org/conference/fast25/presentation/qin)**
  `Moonshot AI + Tsinghua` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。
- **Featured:** **[llm-d + LMCache + vLLM](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes)**
  `IBM / Red Hat / llm-d` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kubernetes` `llm-d`
  Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。
- **Featured:** **[vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/)**
  `PyTorch Foundation / vLLM community` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `vllm`
  vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。
#### Full Resource List

- **[BlueField-4 STX / context memory storage](https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `memory` `agent` `rag`
  用 DPU/加速存储绕过 host CPU，把长上下文 KV cache 放到近存储路径，面向 agentic AI 的大上下文状态。
- **[DroidSpeak](https://www.microsoft.com/en-us/research/publication/droidspeak-kv-cache-sharing-for-efficient-multi-llm-serving/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `serving` `kv-cache` `agent`
  在相同架构的 fine-tuned model variants 之间共享 KV cache，降低企业多模型/多 agent 的重复 prefill。
- **[Dynamo 1.0 Production-Scale Multi-Node Inference](https://developer.nvidia.com/blog/?p=113961)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `routing` `agent` `multimodal` `kubernetes`
  Dynamo 1.0 强化多节点部署、Kubernetes 编排、agentic/multimodal KV routing、ModelExpress 快速启动和 KV Block Manager。
- **[FlexKV](https://github.com/taco-project/FlexKV)**
  `Tencent Cloud TACO + NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `sglang` `vllm`
  分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。
- **[KEEP](https://www.microsoft.com/en-us/research/publication/keep-a-kv-cache-centric-memory-management-system-for-efficient-embodied-planning/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `memory`
  Embodied planning 中用 KV-cache-centric memory management 替代原始文本记忆，减少频繁 KV 更新和重算。
- **[KV Offloading Connector](https://vllm.ai/blog/kv-offloading-connector)**
  `vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `vllm`
  vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。
- **[LookaheadKV](https://research.samsung.com/research-papers/LookaheadKV-Fast-and-Accurate-KV-Cache-Eviction-by-Glimpsing-into-the-Future-without-Generation)**
  `Samsung Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  不生成未来草稿，训练轻量模块预测未来重要性分布以指导 KV cache eviction。
- **[Memento](https://www.microsoft.com/en-us/research/articles/memento-teaching-llms-to-manage-their-own-context/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  训练模型把 CoT block 压成 dense memento，释放已经完成推理块的 KV，提升 reasoning serving 吞吐。
- **[Mooncake Joins PyTorch Ecosystem](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/)**
  `Moonshot / PyTorch` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `rag` `sglang` `tensorrt-llm`
  Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。
- **[MooncakeStoreConnector](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/)**
  `vLLM / Mooncake ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `vllm`
  vLLM 文档化 MooncakeStoreConnector，支持 embedded 和 standalone-store 模式，扩展 CPU/SSD KV pool。
- **[PegaFlow External KV Cache](https://vllm.ai/blog/2026-05-18-pegaflow)**
  `Novita AI + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `vllm`
  PegaFlow 作为 Rust standalone external KV cache service 通过 vLLM connector 接入，面向生产级外部 KV cache。
- **[Tair-KVCache-HiSim](https://www.alibabacloud.com/blog/603164)**
  `Alibaba Cloud Tair` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。
- **[Tutti](https://arxiv.org/abs/2605.03375)**
  `University/industry collaboration` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `lmcache`
  让 SSD-backed KV cache 接近 DRAM-backed LMCache 的性能，扩大长上下文服务的低成本 KV 容量。
- **[llm-d KV Cache](https://github.com/llm-d/llm-d-kv-cache)**
  `llm-d` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `routing` `kv-cache` `kubernetes` `llm-d`
  用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。
- **[AlayaDB](https://arxiv.org/abs/2504.10326)**
  `AlayaDB AI + academia` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  将 KV cache 和 attention 处理抽象为数据库查询，由 query optimizer 决定索引、放置和执行计划。
- **[Ascend-vLLM prefix caching / KV offload](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html)**
  `Huawei Cloud / Ascend` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `npu` `kv-cache` `lmcache` `vllm`
  在 Ascend NPU 上支持 prefix caching、KV cache CPU offload 和 Mooncake/LMCache 连接。
- **[Cache-Craft](https://arxiv.org/abs/2502.15734)**
  `Adobe Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `rag`
  管理 RAG chunk-caches，通过少量重计算修复位置问题，实现 chunk KV cache 复用。
- **[CacheBlend](https://www.microsoft.com/en-us/research/uploads/prod/2024/09/eurosys25-final999.pdf)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `edge` `rag`
  复用 RAG cached knowledge 的 KV，并处理非前缀片段融合问题，减少长输入 prefill。
- **[Context Parallelism for Million-Token Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html)**
  `Meta` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill`
  用 pass-KV/pass-Q 精确 ring attention 在常见数据中心网络上扩展百万 token prefill。
- **[FlowKV](https://arxiv.org/abs/2504.03775)**
  `Alibaba Cloud` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  在 PD 分离式架构中优化 KV cache transfer，并做 load-aware scheduling。
- **[InfiniStore](https://github.com/bytedance/InfiniStore)**
  `ByteDance` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `lmcache` `vllm`
  高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。
- **[KV Cache Offloading](https://kserve.github.io/website/docs/model-serving/generative-inference/kvcache-offloading)**
  `KServe` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `kserve` `kubernetes`
  在 KServe generative inference 中集成 LMCache/vLLM KV offloading，面向云原生模型服务。
- **[MagicDec](https://arxiv.org/abs/2408.11049)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `latency` `throughput`
  联合优化 draft 与 target 的 KV cache，在长上下文下利用验证阶段相对便宜的特性打破 latency-throughput 冲突。
- **[Medha](https://www.microsoft.com/en-us/research/publication/medha-efficient-llm-inference-on-multi-million-context-lengths-without-approximation/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `npu` `kv-cache`
  用 adaptive prefill chunking、Sequence Pipeline Parallelism、KV-Cache Parallelism 和 input-length-aware scheduling 支撑千万 token 精确推理。
- **[Online Scheduling with KV Cache Constraints](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `memory`
  将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。
- **[RetroInfer / RetrievalAttention](https://www.microsoft.com/en-us/research/publication/retroinfer-a-vector-storage-engine-for-scalable-long-context-llm-inference/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `kv-cache`
  把 KV cache 重新抽象成向量存储系统，在 CPU/GPU 间用 attention-aware index 召回关键 KV。
- **[ShadowKV](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference)**
  `ByteDance Seed` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `gpu`
  GPU 只保留低秩 keys、landmarks 和少量 outliers，values 放 CPU DRAM，decode 时按需召回 Top-K value。
- **[TensorRT-LLM KV cache reuse](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `routing` `kv-cache` `tensorrt-llm`
  用 KV cache event API 和 KV-aware routing 提高 prefix/cache 命中，减少重复 prefill。
- **[Unified Cache Manager, UCM](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-releases-new-tool-to-get-chinese-firms-around-crushing-hbm-export-blacklist-new-ucm-software-claims-up-to-22x-throughput-gain-and-90-percent-latency-reduction-for-traditional-cache-hierarchies-in-ai-workloads)**
  `Huawei` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  用分层 KV cache 管理缓解 HBM 受限环境下的推理吞吐/延迟问题。
- **[CachedAttention](https://www.usenix.org/conference/atc24/technical-sessions)**
  `Huawei Cloud + NUS + SJTU` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `scheduler` `ttft`
  用 DRAM/SSD 分层保存跨轮 KV，配合 layer-wise preload、异步保存和 scheduler-aware eviction 降低 TTFT。
- **[JetStream + MaxText](https://cloud.google.com/tpu/docs/tutorials/LLM/jetstream-maxtext-inference-v6e)**
  `Google Cloud` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `tpu` `memory` `throughput`
  面向 XLA/TPU 的 throughput 和 memory optimized LLM inference engine，配合 MaxText 在 TPU/GKE 上服务 LLM。
- **[ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai)**
  `Microsoft` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `npu` `kv-cache`
  在 ONNX Runtime 上封装 generation loop、KV cache、sampling、量化和 CPU/GPU/NPU provider，面向 Windows 与边缘部署。

### P/D Disaggregation & KV Transfer (12)

Prefill/decode separation, KV transfer, routing, and distributed transport.

#### Featured

- **Featured:** **[Dynamo](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `routing` `serving` `kv-cache`
  分布式/分离式推理框架，组合 disaggregated serving、KV cache-aware routing、KV offloading，并用 NIXL 做低延迟 KV 传输。
- **Featured:** **[NIXL / KV cache transfer](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `kv-cache`
  面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。
#### Full Resource List

- **[AI200 / AI250](https://www.tomshardware.com/tech-industry/artificial-intelligence/qualcomm-unveils-ai200-and-ai250-ai-inference-accelerators-hexagon-takes-on-amd-and-nvidia-in-the-booming-data-center-realm)**
  `Qualcomm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `npu` `memory`
  将 Hexagon NPU 扩展到数据中心，强调大容量 LPDDR、低比特格式、near-memory compute、机架扩展和 disaggregated inference。
- **[NIXL / Inference Transfer Library](https://developer.nvidia.com/blog/?p=113426)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `long-context` `rag`
  非阻塞传输 API 和动态元数据交换，覆盖 disaggregated KV movement、long-context storage、weight transfer 和 expert parallelism。
- **[RDMA-Accelerated KV Cache Storage Offload](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/)**
  `Dell + NVIDIA + LMCache/vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `rdma` `kv-cache` `rag` `lmcache` `vllm`
  将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。
- **[SYMPHONY](https://www.usenix.org/conference/nsdi26/presentation/agarwal)**
  `UC/industry collaboration` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `memory` `rag`
  NSDI 2026 工作，将 KV cache storage 从 compute 解耦，形成满足严格延迟的 disaggregated memory management layer。
- **[UCCL](https://github.com/uccl-project/uccl)**
  `IBM / Red Hat / Google 等` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `kv-cache` `llm-d`
  GPU 通信库，覆盖 collectives、P2P KV cache transfer、RL weight transfer 和 expert parallelism，进入 llm-d 分布式推理栈。
- **[vLLM-Omni](https://arxiv.org/abs/2602.02204)**
  `Ant Group + vLLM 社区` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu` `vllm`
  用 stage graph 拆分 LLM、扩散模型和编码器，各阶段独立批处理、分配 GPU，并通过统一 connector 传递中间状态。
- **[MegaScale-Infer](https://arxiv.org/abs/2504.02263)**
  `ByteDance Seed` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `moe`
  将 attention 和 MoE FFN 分池部署，以 disaggregated expert parallelism、ping-pong pipeline 和 M2N 通信提升专家利用率。
- **[llm-d](https://github.com/llm-d/llm-d)**
  `Red Hat / IBM / Google / NVIDIA 社区` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `routing` `kubernetes` `llm-d`
  将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。
- **[P/D-Serve](https://arxiv.org/abs/2408.08147)**
  `Huawei` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `npu`
  在数万 xPU/NPU 规模上部署 prefill/decode disaggregated serving，做 P/D 组织、调度和 D2D KV transfer。
- **[CUTLASS / CuTe DSL](https://github.com/NVIDIA/cutlass)**
  `NVIDIA` · `2017` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `blackwell` `moe`
  提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives；4.4/4.5 系列继续补充 Blackwell GQA decode、int4 KV、MX/NVFP4 block-scaled GEMM 和 MoE grouped GEMM 示例。

### KV Compression & Low-Bit State (22)

KV quantization, latent state, sparsity, and quality-cost tradeoffs.

#### Featured

- **Featured:** **[AITER: AI Tensor Engine for ROCm](https://github.com/ROCm/aiter)**
  `AMD / ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `amd` `rocm` `compiler` `kernel` `moe` `sglang` `vllm`
  AMD AITER (AI Tensor Engine for ROCm) provides C++/Python APIs and optimized Triton, Composable Kernel, and assembly operators for ROCm inference, including attention, MoE, GEMM, quantization, and communication kernels; it integrates with vLLM and SGLang.
- **Featured:** **[FlashMLA](https://github.com/deepseek-ai/FlashMLA)**
  `DeepSeek` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `gpu` `hopper` `kernel` `kv-cache`
  面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。
#### Full Resource List

- **[ATOM inference engine](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `amd` `rocm` `kernel` `moe`
  以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。
- **[Full-Stack Optimizations for Agentic Inference with Dynamo](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `agent`
  针对 coding agent / multi-agent 的 write-once-read-many KV 模式，强调 router、cache pinning、ephemeral KV block 生命周期和 agent-native KV 管理。
- **[KVServe](https://arxiv.org/abs/2605.13734)**
  `KVServe Team` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `compression` `slo`
  在分离式 LLM serving 中根据 workload、网络和 SLO 在线选择 KV compression profile，面向通信瓶颈。
- **[KVTC](https://arxiv.org/abs/2511.01815)**
  `NVIDIA + University of Warsaw` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  把 KV cache 看成可压缩信号，用 transform coding、PCA 去相关、自适应量化和熵编码降低可复用 KV 存储。
- **[Maia 200](https://www.techradar.com/pro/microsoft-unveils-maia-200-its-powerhouse-accelerator-looking-to-unlock-the-power-of-large-scale-ai)**
  `Microsoft` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  面向 Azure AI inference 设计低精度 tensor core、片上 SRAM、定制 DMA 与 NoC，并开始用于 Microsoft 内部 AI 服务。
- **[Productionizing TurboQuant on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html)**
  `AMD ROCm + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `gpu` `kernel` `kv-cache` `agent` `vllm` `ttft`
  在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。
- **[SAW-INT4](https://arxiv.org/abs/2604.19157)**
  `Apple / academic collaboration` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kv-cache` `quantization`
  面向真实 serving 约束设计 4-bit KV cache quantization，考虑 paged layout、规则访存和 fused attention。
- **[Shift Parallelism / Arctic Inference](https://www.asplos-conference.org/asplos2026/program/)**
  `Snowflake AI Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  根据流量在 TP 与 sequence parallelism 间切换，并结合 speculative decoding、SwiftKV 和 embedding fast path。
- **[ThinKV](https://openreview.net/forum?id=M3CeHnZKNC)**
  `NVIDIA Research + Georgia Tech` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `compression` `kv-cache`
  thought-adaptive KV cache compression，根据推理过程中的 thought 类型做保留、量化和逐级淘汰。
- **[TurboQuant](https://arxiv.org/abs/2504.19874)**
  `Google Research / DeepMind` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  通过随机旋转、近最优量化和 QJL 残差校正，面向 KV cache 和向量检索做低比特在线向量量化。
- **[NVFP4 KV cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `blackwell` `kv-cache` `moe` `agent`
  Blackwell 侧使用 4-bit KV 存储、attention 前解量化到 FP8，面向长上下文、大 batch、多 agent/MoE 降低 HBM 压力。
- **[Gaudi 2/3 software stack](https://docs.habana.ai/)**
  `Intel` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `vllm`
  通过 SynapseAI、HCCL、FP8 和 vLLM/Optimum Habana 支持 LLM serving，以标准 Ethernet 和成本为差异点。
- **[MLA / Multi-head Latent Attention](https://arxiv.org/abs/2412.19437)**
  `DeepSeek` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `kv-cache` `long-context`
  把 KV cache 压到 latent 向量，DeepSeek-V3/R1 系列用 MLA 降低 long-context decode 的 KV 内存和带宽。
- **[Medusa](https://arxiv.org/abs/2401.10774)**
  `Together AI + Princeton 等` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  在目标模型上增加多组 decoding heads，一次预测并验证多个未来 token；其思想已进入主流 serving runtime。
- **[OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai)**
  `Intel` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `npu`
  为 Intel 硬件提供 stateful model、continuous batching、paged attention、量化和 speculative decoding pipeline。
- **[TensorRT-LLM FP8/INT8 KV cache](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html)**
  `NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `kernel` `kv-cache` `tensorrt-llm`
  MHA/MQA kernel 中支持 on-the-fly dequantize 的 FP8/INT8 KV cache，降低 decode 阶段读带宽。
- **[TensorRT-LLM Speculative Decoding](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html)**
  `NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `tensorrt-llm`
  在产品级 runtime 中集成 draft-target、Medusa、EAGLE 等推测策略，并与 inflight batching、量化和并行执行组合。
- **[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)**
  `NVIDIA` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `tensorrt-llm`
  提供 inflight batching、paged KV、FP8/FP4、speculative decoding、TP/PP/EP 和多节点执行，是 NVIDIA 平台的产品级 LLM 引擎。
- **[vLLM V1](https://github.com/vllm-project/vllm)**
  `vLLM / PyTorch Foundation` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `serving` `vllm`
  以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。
- **[Text Generation Inference, TGI](https://github.com/huggingface/text-generation-inference)**
  `Hugging Face` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `quantization`
  面向 Hugging Face 模型提供 continuous batching、tensor parallelism、quantization、speculative decoding 和 OpenAI-compatible API。

### Kernel & Compiler (24)

CUDA, Triton, HIP, attention, GEMM, MoE kernels, and compiler backends.

#### Featured

- **Featured:** **[ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/)**
  `AMD` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `gpu` `kernel` `sglang` `tensorrt-llm`
  通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。
#### Full Resource List

- **[ATOMesh distributed serving gateway](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `amd` `gpu` `routing` `sglang` `vllm`
  作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。
- **[Dynamo Snapshot](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `cuda` `kv-cache` `kubernetes`
  用 CRIU + cuda-checkpoint 做 Kubernetes 上推理 worker 快照恢复，并通过 KV cache unmap 减小 checkpoint 体积。
- **[LMCache Operator](https://github.com/LMCache/LMCache/releases/tag/operator-v0.1.1)**
  `LMCache 社区` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `gpu` `kubernetes` `lmcache`
  首个 Kubernetes Operator 将 `LMCacheEngine` CRD 编排为与 vLLM worker 共置的 LMCache MP DaemonSet、Service、ConfigMap 和 Secret，并加入 RESP L2 backend、AMD GPU 支持与端到端 smoke tests。
- **[Ragged Paged Attention for TPU](https://arxiv.org/abs/2604.15464)**
  `Google / TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `tpu` `kernel` `rag`
  面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。
- **[vLLM-Omni runtime](https://github.com/vllm-project/vllm-omni)**
  `Ant Group + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `multimodal` `vllm`
  将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。
- **[FlashInfer](https://proceedings.mlsys.org/paper_files/paper/2025/file/dbf02b21d77409a2db30e56866a8ab3a-Paper-Conference.pdf)**
  `FlashInfer 社区` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `kernel`
  面向 LLM serving 的可定制 attention engine，支持 paged KV、decode/prefill kernel、与多 runtime 集成。
- **[FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)**
  `NVIDIA / University of Washington` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel` `sglang` `vllm`
  从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。
- **[FlexAttention for inference](https://pytorch.org/blog/flexattention-for-inference/)**
  `Meta / PyTorch` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  用 PyTorch API 表达 attention variants，经 torch.compile 降到 fused attention kernel，支持 inference/paged attention 方向。
- **[InferenceMAX](https://www.tomshardware.com/tech-industry/inferencemax-ai-benchmark-tests-software-stacks-efficiency-and-tco-vendor-neutral-suite-runs-nightly-and-tracks-performance-changes-over-time)**
  `SemiAnalysis` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `kernel`
  夜间滚动测试完整 driver/kernel/runtime/hardware 组合，以 tok/s/GPU、tok/s/user 和美元/百万 token 跟踪软件演进。
- **[LeanAttention / TurboAttention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `kernel` `memory`
  分别从精确 decode dataflow 和端到端量化 attention 两条路线降低长上下文 memory wall。
- **[WaferLLM on Cerebras WSE-2](https://www.usenix.org/conference/osdi25/technical-sessions)**
  `Microsoft Research + University of Edinburgh` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  以 PLMR 模型、MeshGEMM/MeshGEMV 和 wafer-scale parallelism 将 LLM inference 映射到数十万片上 core。
- **[FlashInfer kernel ecosystem](https://github.com/flashinfer-ai/flashinfer)**
  `FlashInfer community / NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `kernel` `rag` `sglang` `vllm`
  针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。
- **[FlexAttention](https://pytorch.org/blog/flexattention/)**
  `PyTorch` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  允许用户用 score modification 和 block mask 表达 attention variant，再由编译器生成 fused kernel，覆盖 sparse/paged inference。
- **[MAX Engine](https://docs.modular.com/max/)**
  `Modular` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `cuda` `gpu` `compiler` `kernel`
  用 MAX graph/compiler 和 Mojo kernel 统一 CPU/GPU 推理，瞄准摆脱单一 CUDA runtime 的可移植高性能部署。
- **[QServe / OmniServe](https://github.com/mit-han-lab/omniserve)**
  `MIT Han Lab / NVIDIA ecosystem` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel`
  将 4-bit 权重、8-bit 激活和 4-bit KV 与 SmoothAttention、重排及定制 kernel 联合设计。
- **[Triton language and kernels in inference stacks](https://triton-lang.org/)**
  `OpenAI / Triton ecosystem` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `kernel` `moe` `sglang` `vllm`
  工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。
- **[LightLLM](https://github.com/ModelTC/lightllm)**
  `ModelTC community` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel`
  用 token attention、动态 batch、共享显存管理和定制 Triton kernel 提供低开销分布式 LLM serving。
- **[MegaBlocks](https://github.com/databricks/megablocks)**
  `Databricks / Stanford ecosystem` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel` `moe`
  用 block-sparse operation 替代 capacity padding，为高效 MoE kernel 和 serving 提供基础。
- **[torch.compile / Inductor](https://docs.pytorch.org/docs/stable/torch.compiler.html)**
  `PyTorch` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel` `vllm`
  捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。
- **[DeepSpeed-Inference](https://www.deepspeed.ai/tutorials/inference-tutorial/)**
  `Microsoft` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel` `memory`
  以 inference-adapted parallelism、kernel injection、量化和 heterogeneous memory 支撑超大 Transformer。
- **[TurboTransformers](https://github.com/Tencent/TurboTransformers)**
  `Tencent` · `2021` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu` `kernel`
  按序列长度动态组织 batch，并通过融合 kernel 和内存管理加速 Transformer 在线服务。
- **[FasterTransformer](https://github.com/NVIDIA/FasterTransformer)**
  `NVIDIA` · `2020` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `cuda` `gpu` `kernel` `tensorrt-llm`
  用融合 CUDA kernel、GEMM 调优、量化和多 GPU 并行提供早期生产级 Transformer 推理库，后续能力并入 TensorRT-LLM。
- **[Triton Inference Server](https://github.com/triton-inference-server/server)**
  `NVIDIA` · `2018` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `tensorrt-llm` `vllm`
  负责模型仓库、dynamic batching、ensemble、metrics 和多框架后端，常作为 TensorRT-LLM/vLLM 外层生产服务面。

### Runtime & Serving (20)

Runtime scheduling, agent graphs, structured generation, and SLO-aware dispatch.

#### Full Resource List

- **[MX-SAFE](https://arxiv.org/abs/2605.24391)**
  `Open Compute numerical-format ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  动态切换 mantissa/exponent 模式，使低精度格式同时覆盖 direct-cast inference 和训练需求。
- **[TPU 8i / TPU 8t](https://www.itpro.com/infrastructure/google-cloud-eighth-generation-tpu-8t-8i-ai-inference-training)**
  `Google Cloud` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `training` `tpu` `agent`
  第八代首次将 inference 优化的 8i 与 training 优化的 8t 分开，8i 强调片上 SRAM、内存带宽和低延迟互连；尚待正式交付验证。
- **[vLLM 商业化](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/)**
  `vLLM maintainers / Inferact` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `vllm`
  vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。
- **[BladeLLM](https://www.alibabacloud.com/help/doc-detail/2865199.html)**
  `Alibaba Cloud` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  PAI 上的高性能 LLM inference engine，用于低延迟、高吞吐部署 Qwen 等模型。
- **[DynamoLLM](https://www.microsoft.com/en-us/research/publication/dynamollm-designing-llm-inference-clusters-for-performance-and-energy-efficiency/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `slo`
  动态重配置 LLM inference cluster，在 SLO 下优化能耗和成本。
- **[Scaling LLM inference: TP/CP/EP](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/)**
  `Meta` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  公开 Meta 在 tensor/context/expert parallelism 上扩展 LLM inference 的工程经验。
- **[XGrammar production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html)**
  `MLC / SGLang / vLLM ecosystem` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `gpu` `sglang` `vllm`
  将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。
- **[高速推理 API / Llama API 合作](https://www.cerebras.ai/)**
  `Cerebras` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  用 wafer-scale engine 做极高 token/s 推理，Meta Llama API 等使用其高速推理能力。
- **[Fireworks Inference Platform](https://docs.fireworks.ai/)**
  `Fireworks AI` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  将高性能 runtime、量化、LoRA serving 和模型路由封装成推理云，代表独立 inference provider 的产品化路线。
- **[GroqCloud / LPU Inference](https://groq.com/groqcloud)**
  `Groq` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `latency`
  用静态调度的 LPU 架构和编译器降低动态调度开销，主攻低 batch、稳定 token latency 的在线生成。
- **[JetStream / MaxText / Pathways on TPU](https://github.com/AI-Hypercomputer/JetStream)**
  `Google` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `tpu`
  用 JAX/XLA、paged attention、模型并行和 TPU pod serving 构成 Gemini 与开源模型的 TPU 推理路径。
- **[MLX-LM / vllm-mlx](https://github.com/ml-explore/mlx-lm)**
  `Apple / MLX community` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `vllm`
  利用 Apple silicon 统一内存和 MLX 图执行提供本地 LLM 推理，并开始向 continuous batching 和 vLLM API 兼容扩展。
- **[MindIE](https://www.hiascend.com/software/mindie)**
  `Huawei Ascend` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `npu`
  面向昇腾 NPU 提供 LLM 推理、服务化、并行执行、量化和调度能力，是国产算力生产栈的重要入口。
- **[Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html)**
  `Ray / Anyscale` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `vllm`
  将 vLLM 等 engine 包装为 Ray actor/deployment，提供多节点 replica、路由、autoscaling 和 Python 应用编排。
- **[Together Inference Engine](https://docs.together.ai/)**
  `Together AI` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu`
  将 FlashAttention、Medusa 等研究与多 GPU serving、量化和私有部署结合，形成模型云和企业推理平台。
- **[Truss / TensorRT-LLM serving stack](https://docs.baseten.co/)**
  `Baseten` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `tensorrt-llm`
  把容器构建、模型打包、TensorRT-LLM 优化、流量伸缩和可观测性组合为生产推理平台。
- **[Wafer-scale Inference](https://www.cerebras.ai/inference)**
  `Cerebras` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  用 wafer-scale engine 和片上大容量存储减少跨芯片数据搬移，主攻极高 token/s 和交互式推理。
- **[XGrammar structured generation engine](https://github.com/mlc-ai/xgrammar)**
  `MLC / CMU` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu`
  预编译 grammar、持久化 parser stack 并与 GPU execution overlap，已进入多种 serving engine 的 JSON/tool-call fast path。
- **[BentoML / BentoCloud](https://docs.bentoml.com/)**
  `BentoML` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `sglang` `tensorrt-llm`
  统一模型容器、API、batching、资源声明和 autoscaling，并与 vLLM、SGLang、TensorRT-LLM 等 runtime 集成。
- **[DeepSpeed-MII / DeepSpeed-FastGen](https://github.com/microsoft/DeepSpeed-MII)**
  `Microsoft` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  以 DeepSpeed-Inference 为底座，用 Dynamic SplitFuse、模型并行、量化和持久部署服务长 prompt 与 generation 混合负载。

### Reliability & Benchmarks (5)

SLOs, drift, recovery, reproducibility, benchmarks, and graceful degradation.

#### Featured

- **Featured:** **[KServe Generative Inference Stack](https://kserve.github.io/website/docs/model-serving/generative-inference/overview)**
  `KServe` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu` `kserve` `kubernetes`
  Artifact: [source](https://github.com/kserve/kserve)
  KServe official documentation covering LLMInferenceService, multi-node/multi-GPU inference, model caching, and AI Gateway integration for Kubernetes-based generative serving.
#### Full Resource List

- **[Gemma 4 on vLLM-TPU](https://arxiv.org/abs/2605.25645)**
  `Google TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu` `tpu` `vllm`
  展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。
- **[vLLM x Mooncake Store](https://vllm.ai/blog/2026-05-06-mooncake-store)**
  `Moonshot / Mooncake / vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kv-cache` `agent` `vllm` `ttft`
  将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。
- **[Inference evaluation anti-patterns](https://arxiv.org/abs/2507.09019)**
  `Microsoft Research 等` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `stall`
  系统总结 baseline 公平性、workload 代表性和 metric 设计中的反模式，强调 burst、stall 与双阶段行为。
- **[MLPerf Inference](https://mlcommons.org/benchmarks/inference-datacenter/)**
  `MLCommons` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  以统一模型、精度规则、server/offline 场景和可审计 submission 比较数据中心及边缘推理系统。
