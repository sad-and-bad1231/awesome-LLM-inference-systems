# Industry & Open-Source Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Academic papers](../papers/README.md)

A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Industrial material | With artifact | Tagged records |
|---:|---:|---:|---:|
| 64 | 64 | 64 | 63 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (2)
- [KV Cache](#kv-cache) (12)
- [Prefill–Decode 与传输](#prefill-decode) (11)
- [Speculative Decoding](#speculative-decoding) (2)
- [MoE](#moe) (9)
- [Compiler / DSL](#compiler-dsl) (6)
- [Runtime / Scheduling](#runtime-scheduling) (22)
- [探索观察](#探索观察) (2)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | `core` records form the seven main themes; a bounded `adjacent` window appears under exploration, with full adjacent/archive history on the archive page. |
| Featured | A small editorial starting set; all core records remain below. |

## DeepSeek AI 系统专题

从模型架构到 kernel、通信、存储和应用数据路径的官方系统材料；专题仅作聚合导航，项目仍保留在原七主题主表中。

| 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|
| 架构与系统 | [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | DeepSeek-V3 官方模型与推理参考，公开 MLA、DeepSeekMoE、FP8 权重转换及多种 GPU/NPU 运行入口。 | [official](https://github.com/deepseek-ai/DeepSeek-V3) |
| 架构与系统 | [DeepSeek-V3.2 / DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) | 在模型架构中加入 sparse attention/indexer，目标是在长上下文和 reasoning/agent 任务中降低推理成本。 | [official](https://arxiv.org/abs/2512.02556) |
| 架构与系统 | [Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures](https://arxiv.org/abs/2505.09343) | 从 DeepSeek-V3/R1 的 MLA、MoE、FP8 与 Multi-Plane Network 出发，总结 2,048 张 H800 规模下的模型—硬件协同设计与系统瓶颈。 | [official](https://arxiv.org/abs/2505.09343) |
| 架构与系统 | [MLA / Multi-head Latent Attention](https://arxiv.org/abs/2412.19437) | 把 KV cache 压到 latent 向量，DeepSeek-V3/R1 系列用 MLA 降低 long-context decode 的 KV 内存和带宽。 | [official](https://arxiv.org/abs/2412.19437) |
| 核心算子与通信 | [DeepEP](https://github.com/deepseek-ai/DeepEP) | 面向 MoE expert parallel 的高吞吐、低延迟通信库，提供 dispatch/combine、低延迟模式与 GPU 通信优化。 | [official](https://github.com/deepseek-ai/DeepEP) |
| 核心算子与通信 | [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | 面向 FP8/BF16 的 GPU GEMM kernel 库，为 DeepSeek dense 与 MoE 路径提供紧凑、可调优的矩阵乘实现。 | [official](https://github.com/deepseek-ai/DeepGEMM) |
| 核心算子与通信 | [FlashMLA](https://github.com/deepseek-ai/FlashMLA) | 面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。 | [official](https://github.com/deepseek-ai/FlashMLA) |
| 核心算子与通信 | [TileKernels](https://github.com/deepseek-ai/TileKernels) | 以 TileLang 编写的 kernel library，用 tile 级抽象组织和优化 GPU 算子实现。 | [official](https://github.com/deepseek-ai/TileKernels) |
| 存储与数据路径 | [3FS](https://github.com/deepseek-ai/3FS) | 面向 AI 训练与推理负载的高性能分布式文件系统，强调并行数据路径、吞吐与大规模 checkpoint/data access。 | [official](https://github.com/deepseek-ai/3FS) |
| 推测解码 | [DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 用于训练、评估和复现实用 speculative decoding 方法的官方工具集，覆盖 draft/verify 与接受率评测。 | [official](https://github.com/deepseek-ai/DeepSpec) |
| OCR 与生态 | [Awesome DeepSeek Agents](https://github.com/deepseek-ai/awesome-deepseek-agent) | 面向 DeepSeek Agent、coding agent 与工具调用生态的官方项目索引。 | [official](https://github.com/deepseek-ai/awesome-deepseek-agent) |
| OCR 与生态 | [Awesome DeepSeek Integrations](https://github.com/deepseek-ai/awesome-deepseek-integration) | DeepSeek API 在应用、Agent、RAG、开发工具和基础设施中的官方集成索引。 | [official](https://github.com/deepseek-ai/awesome-deepseek-integration) |
| OCR 与生态 | [DeepSeek Open Infra Index](https://github.com/deepseek-ai/open-infra-index) | DeepSeek 官方 AI infrastructure 导航入口，集中索引其生产验证的 kernel、通信、存储和系统工具。 | [official](https://github.com/deepseek-ai/open-infra-index) |
| OCR 与生态 | [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | 通过视觉 token 压缩处理长文档上下文，并提供 OCR 推理与大规模页面数据生成路径。 | [official](https://github.com/deepseek-ai/DeepSeek-OCR) |
| OCR 与生态 | [DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | DeepSeek OCR 的后续官方项目，以 Visual Causal Flow 组织文档视觉理解与生成流程。 | [official](https://github.com/deepseek-ai/DeepSeek-OCR-2) |

## Kimi / Moonshot AI 系统专题

Kimi 模型架构、KV-centric serving、推理 kernel 与开发工具的官方材料。

| 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|
| 模型与架构 | [Kimi-K2.5](https://github.com/MoonshotAI/Kimi-K2.5) | Kimi 官方开放模型项目，提供多模态与 agentic 推理相关模型材料和运行入口。 | [official](https://github.com/MoonshotAI/Kimi-K2.5) |
| 模型与架构 | [Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | Kimi 新一代 MoE 模型，结合 Kimi Delta Attention、Attention Residuals 与高稀疏 expert 设计。 | [official](https://github.com/MoonshotAI/Kimi-K3) |
| 模型与架构 | [Kimi-Linear](https://github.com/MoonshotAI/Kimi-Linear) | 面向长上下文的线性注意力模型与技术材料，公开训练和推理使用入口。 | [official](https://github.com/MoonshotAI/Kimi-Linear) |
| 推理与 Serving | [checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine) | 在 LLM serving 中高效更新模型权重的中间件，面向在线模型切换与部署工作流。 | [official](https://github.com/MoonshotAI/checkpoint-engine) |
| 推理与 Serving | [Mooncake](https://www.usenix.org/conference/fast25/presentation/qin) | 以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。 | [official](https://www.usenix.org/conference/fast25/presentation/qin) |
| Kernel 与通信 | [FlashKDA](https://github.com/MoonshotAI/FlashKDA) | Kimi Delta Attention 的高性能 CUDA kernel，实现融合、数值稳定与硬件路径优化。 | [official](https://github.com/MoonshotAI/FlashKDA) |
| 工具与生态 | [Kimi Code](https://github.com/MoonshotAI/kimi-code) | Kimi 官方 coding agent 与命令行开发工作流。 | [official](https://github.com/MoonshotAI/kimi-code) |

## MiniMax AI 系统专题

MiniMax 开放模型、多模态接口与 Agent 工具链的官方材料。

| 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|
| 模型与架构 | [MiniMax-M2.7](https://github.com/MiniMax-AI/MiniMax-M2.7) | MiniMax 官方开放模型项目，提供模型说明、权重与部署入口。 | [official](https://github.com/MiniMax-AI/MiniMax-M2.7) |
| 模型与架构 | [MiniMax-M3](https://github.com/MiniMax-AI/MiniMax-M3) | MiniMax 新一代官方开放模型项目与推理使用入口。 | [official](https://github.com/MiniMax-AI/MiniMax-M3) |
| 模型与架构 | [VTP](https://github.com/MiniMax-AI/VTP) | 面向生成任务的可扩展视觉 tokenizer 预训练代码与论文材料。 | [official](https://github.com/MiniMax-AI/VTP) |
| 多模态与 Agent | [Mini-Agent](https://github.com/MiniMax-AI/Mini-Agent) | 展示单 Agent 核心执行管线和工程化组件的官方示例。 | [official](https://github.com/MiniMax-AI/Mini-Agent) |
| 多模态与 Agent | [OpenRoom](https://github.com/MiniMax-AI/OpenRoom) | 由 AI Agent 通过自然语言操作应用的浏览器桌面环境。 | [official](https://github.com/MiniMax-AI/OpenRoom) |
| 工具与生态 | [MiniMax CLI](https://github.com/MiniMax-AI/cli) | 面向文本、图像、视频、语音与音乐 API 的官方命令行工具。 | [official](https://github.com/MiniMax-AI/cli) |
| 工具与生态 | [MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 连接语音、图像和视频生成 API 的官方 Model Context Protocol 服务。 | [official](https://github.com/MiniMax-AI/MiniMax-MCP) |

## GLM / 智谱 AI 系统专题

GLM 模型、多模态推理、训练框架与开放工作空间的官方材料。

| 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|
| 模型与架构 | [GLM-5](https://github.com/zai-org/GLM-5) | GLM-5 官方模型、技术报告与推理部署入口，面向 agentic engineering。 | [official](https://github.com/zai-org/GLM-5) |
| 模型与架构 | [GLM-Image](https://github.com/zai-org/GLM-Image) | 自回归 dense-knowledge 图像生成模型及官方推理实现。 | [official](https://github.com/zai-org/GLM-Image) |
| 训练与数据 | [slime](https://github.com/THUDM/slime) | 面向大模型 RL scaling 的后训练框架，为 GLM 系列训练工作流提供支持。 | [official](https://github.com/THUDM/slime) |
| 多模态与 Agent | [GLM-V](https://github.com/zai-org/GLM-V) | GLM 多模态 reasoning 模型系列，提供开放权重、推理脚本与 serving 示例。 | [official](https://github.com/zai-org/GLM-V) |
| 工具与生态 | [Synapse](https://github.com/zai-org/Synapse) | 可自托管的 AI 工作空间，整合记忆、共享会话、插件、MCP 与本地设备访问。 | [official](https://github.com/zai-org/Synapse) |

## 阶跃星辰 AI 系统专题

Step 系列模型、训练框架、实时语音和多模态 Agent 的官方材料。

| 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|
| 模型与架构 | [Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash) | 强调快速 agentic inference 的官方开放模型项目。 | [official](https://github.com/stepfun-ai/Step-3.5-Flash) |
| 模型与架构 | [Step-3.7-Flash](https://github.com/stepfun-ai/Step-3.7-Flash) | 面向真实 Agent 工作负载的高效率 Flash 模型与推理入口。 | [official](https://github.com/stepfun-ai/Step-3.7-Flash) |
| 训练与数据 | [SteptronOss](https://github.com/stepfun-ai/SteptronOss) | 覆盖 SFT、RLVR、评测与模块化配置的大模型训练框架。 | [official](https://github.com/stepfun-ai/SteptronOss) |
| 多模态与 Agent | [gelab-zero](https://github.com/stepfun-ai/gelab-zero) | STEP-GUI Agent 的官方解决方案与执行环境。 | [official](https://github.com/stepfun-ai/gelab-zero) |
| 多模态与 Agent | [Step-Audio2](https://github.com/stepfun-ai/Step-Audio2) | 端到端音频理解和语音对话模型，提供推理示例与 vLLM backend。 | [official](https://github.com/stepfun-ai/Step-Audio2) |
| 多模态与 Agent | [Step1X-Edit](https://github.com/stepfun-ai/Step1X-Edit) | 开放图像编辑模型及其推理和评测实现。 | [official](https://github.com/stepfun-ai/Step1X-Edit) |
| 工具与生态 | [Step Realtime CLI](https://github.com/stepfun-ai/Step-Realtime-CLI) | 面向实时语音模型的官方命令行开发工具。 | [official](https://github.com/stepfun-ai/Step-Realtime-CLI) |

## 字节跳动 AI 系统专题

ByteDance Seed 的基础模型、长上下文推理与大规模训练系统材料。

| 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|
| 模型与架构 | [Seed-1.8](https://github.com/ByteDance-Seed/Seed-1.8) | 面向真实世界 Agent 的统一基础模型，支持搜索、代码执行、GUI 交互和成本感知推理。 | [official](https://github.com/ByteDance-Seed/Seed-1.8) |
| 推理系统 | [ShadowKV](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference) | GPU 只保留低秩 keys、landmarks 和少量 outliers，values 放 CPU DRAM，decode 时按需召回 Top-K value。 | [official](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference) |
| 训练、数据与通信 | [VeOmni](https://github.com/ByteDance-Seed/VeOmni) | 以模型为中心组织分布式 recipe 的多模态大模型训练框架。 | [official](https://github.com/ByteDance-Seed/VeOmni) |

## Resource List

### Attention / Kernel (2)

#### Featured

- **Featured:** **[PagedAttention + FlexAttention / FMS](https://arxiv.org/abs/2506.07311)**
  `IBM Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  在 IBM Foundation Model Stack 中把 PagedAttention 与 FlexAttention 融合，处理 scattered KV gather。
#### Full Resource List

- **[LeanAttention / TurboAttention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `kernel` `memory`
  分别从精确 decode dataflow 和端到端量化 attention 两条路线降低长上下文 memory wall。

### KV Cache (12)

#### Featured

- **Featured:** **[NIXL / KV cache transfer](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `kv-cache`
  面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。
#### Full Resource List

- **[Ascend-vLLM prefix caching / KV offload](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html)**
  `Huawei Cloud / Ascend` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `npu` `kv-cache` `lmcache` `vllm`
  在 Ascend NPU 上支持 prefix caching、KV cache CPU offload 和 Mooncake/LMCache 连接。
- **[KV Cache Offloading](https://kserve.github.io/website/docs/model-serving/generative-inference/kvcache-offloading)**
  `KServe` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `kserve` `kubernetes`
  在 KServe generative inference 中集成 LMCache/vLLM KV offloading，面向云原生模型服务。
- **[NVFP4 KV cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `blackwell` `kv-cache` `moe` `agent`
  Blackwell 侧使用 4-bit KV 存储、attention 前解量化到 FP8，面向长上下文、大 batch、多 agent/MoE 降低 HBM 压力。
- **[Online Scheduling with KV Cache Constraints](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。
- **[TensorRT-LLM KV cache reuse](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `prefill` `routing` `kv-cache` `tensorrt-llm`
  用 KV cache event API 和 KV-aware routing 提高 prefix/cache 命中，减少重复 prefill。
- **[PegaFlow External KV Cache](https://vllm.ai/blog/2026-05-18-pegaflow)**
  `Novita AI + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `vllm`
  PegaFlow 作为 Rust standalone external KV cache service 通过 vLLM connector 接入，面向生产级外部 KV cache。
- **[RDMA-Accelerated KV Cache Storage Offload](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/)**
  `Dell + NVIDIA + LMCache/vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `rdma` `kv-cache` `rag` `lmcache` `vllm`
  将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。
- **[Tair-KVCache-HiSim](https://www.alibabacloud.com/blog/603164)**
  `Alibaba Cloud Tair` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache`
  面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。
- **[llm-d KV Cache](https://github.com/llm-d/llm-d-kv-cache)**
  `llm-d` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `routing` `kv-cache` `kubernetes` `llm-d`
  用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。
- **[CachedAttention](https://www.usenix.org/conference/atc24/technical-sessions)**
  `Huawei Cloud + NUS + SJTU` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `kv-cache` `scheduler` `ttft`
  用 DRAM/SSD 分层保存跨轮 KV，配合 layer-wise preload、异步保存和 scheduler-aware eviction 降低 TTFT。
- **[TensorRT-LLM FP8/INT8 KV cache](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html)**
  `NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `kernel` `kv-cache` `tensorrt-llm`
  MHA/MQA kernel 中支持 on-the-fly dequantize 的 FP8/INT8 KV cache，降低 decode 阶段读带宽。

### Prefill–Decode 与传输 (11)

#### Featured

- **Featured:** **[vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/)**
  `PyTorch Foundation / vLLM community` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `vllm`
  vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。
- **Featured:** **[vLLM V1](https://github.com/vllm-project/vllm)**
  `vLLM / PyTorch Foundation` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `serving` `vllm`
  以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。
- **Featured:** **[FlashInfer kernel ecosystem](https://github.com/flashinfer-ai/flashinfer)**
  `FlashInfer community / NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `kernel` `rag` `sglang` `vllm`
  针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。
- **Featured:** **[P/D-Serve](https://arxiv.org/abs/2408.08147)**
  `Huawei` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `npu`
  在数万 xPU/NPU 规模上部署 prefill/decode disaggregated serving，做 P/D 组织、调度和 D2D KV transfer。
#### Full Resource List

- **[XGrammar production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html)**
  `MLC / SGLang / vLLM ecosystem` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `gpu` `sglang` `vllm`
  将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。
- **[ATOMesh distributed serving gateway](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `amd` `gpu` `routing` `sglang` `vllm`
  作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。
- **[NIXL / Inference Transfer Library](https://developer.nvidia.com/blog/?p=113426)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `long-context` `rag`
  非阻塞传输 API 和动态元数据交换，覆盖 disaggregated KV movement、long-context storage、weight transfer 和 expert parallelism。
- **[UCCL](https://github.com/uccl-project/uccl)**
  `IBM / Red Hat / Google 等` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `kv-cache` `llm-d`
  GPU 通信库，覆盖 collectives、P2P KV cache transfer、RL weight transfer 和 expert parallelism，进入 llm-d 分布式推理栈。
- **[UCX](https://github.com/openucx/ucx)**
  `NVIDIA / Linux Foundation ecosystem` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `cuda` `rdma` `memory`
  统一 InfiniBand、RoCE、shared memory、CUDA memory 等传输，为 MPI、NCCL 和分布式 runtime 提供底层能力。
- **[CUTLASS / CuTe DSL](https://github.com/NVIDIA/cutlass)**
  `NVIDIA` · `2017` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `blackwell` `moe`
  提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives；4.4/4.5 系列继续补充 Blackwell GQA decode、int4 KV、MX/NVFP4 block-scaled GEMM 和 MoE grouped GEMM 示例。
- **[Triton language and kernels in inference stacks](https://triton-lang.org/)**
  `OpenAI / Triton ecosystem` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `decode` `kernel` `moe` `sglang` `vllm`
  工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。

### Speculative Decoding (2)

#### Full Resource List

- **[Medusa](https://arxiv.org/abs/2401.10774)**
  `Together AI + Princeton 等` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `serving`
  在目标模型上增加多组 decoding heads，一次预测并验证多个未来 token；其思想已进入主流 serving runtime。
- **[TensorRT-LLM Speculative Decoding](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html)**
  `NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `tensorrt-llm`
  在产品级 runtime 中集成 draft-target、Medusa、EAGLE 等推测策略，并与 inflight batching、量化和并行执行组合。

### MoE (9)

#### Full Resource List

- **[DeepSpeed-MoE](https://arxiv.org/abs/2201.05596)**
  `Microsoft` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `moe`
  联合 expert parallel、通信优化和模型压缩，使稀疏大模型的推理成本可控。
- **[Tutel](https://github.com/microsoft/tutel)**
  `Microsoft Research Asia` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `kernel` `moe`
  提供自适应 expert parallel、all-to-all、fused kernel 和动态配置，是通用 MoE 软件栈的重要来源。
- **[COMET](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html)**
  `Alibaba Cloud` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `moe`
  细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。
- **[DeepGEMM / DeepEP](https://flashmla.net/)**
  `DeepSeek` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `moe`
  FP8 GEMM 与 MoE expert-parallel 通信库，支撑 DeepSeek 系列训练和推理的 dense/MoE fast path。
- **[MegaScale-Infer](https://arxiv.org/abs/2504.02263)**
  `ByteDance Seed` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `moe`
  将 attention 和 MoE FFN 分池部署，以 disaggregated expert parallelism、ping-pong pipeline 和 M2N 通信提升专家利用率。
- **[AITER: AI Tensor Engine for ROCm](https://github.com/ROCm/aiter)**
  `AMD / ROCm` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `compiler` `kernel` `moe` `sglang` `vllm`
  AMD AITER (AI Tensor Engine for ROCm) provides C++/Python APIs and optimized Triton, Composable Kernel, and assembly operators for ROCm inference, including attention, MoE, GEMM, quantization, and communication kernels; it integrates with…
- **[ATOM inference engine](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `kernel` `moe`
  以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。
- **[FasterMoE](https://github.com/thu-pacman/FasterMoE)**
  `Tsinghua University` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `moe`
  用 expert shadowing、smart scheduling 和 topology-aware communication 缓解动态路由不均。
- **[MegaBlocks](https://github.com/databricks/megablocks)**
  `Databricks / Stanford ecosystem` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `kernel` `moe`
  用 block-sparse operation 替代 capacity padding，为高效 MoE kernel 和 serving 提供基础。

### Compiler / DSL (6)

#### Featured

- **Featured:** **[ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/)**
  `AMD` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `amd` `gpu` `kernel` `sglang` `tensorrt-llm`
  通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。
- **Featured:** **[torch.compile / Inductor](https://docs.pytorch.org/docs/stable/torch.compiler.html)**
  `PyTorch` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `kernel` `vllm`
  捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。
#### Full Resource List

- **[Productionizing TurboQuant on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html)**
  `AMD ROCm + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `amd` `gpu` `kernel` `kv-cache` `agent` `vllm` `ttft`
  在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。
- **[Triton Inference Server](https://github.com/triton-inference-server/server)**
  `NVIDIA` · `2018` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `tensorrt-llm` `vllm`
  负责模型仓库、dynamic batching、ensemble、metrics 和多框架后端，常作为 TensorRT-LLM/vLLM 外层生产服务面。
- **[FasterTransformer](https://github.com/NVIDIA/FasterTransformer)**
  `NVIDIA` · `2020` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `cuda` `gpu` `kernel` `tensorrt-llm`
  用融合 CUDA kernel、GEMM 调优、量化和多 GPU 并行提供早期生产级 Transformer 推理库，后续能力并入 TensorRT-LLM。
- **[LightSeq](https://github.com/bytedance/lightseq)**
  `ByteDance` · `2021` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `cuda` `kernel`
  通过 fused layer、定制 CUDA kernel 和显存复用部署 NLP 与生成模型。

### Runtime / Scheduling (22)

#### Featured

- **Featured:** **[SGLang 商业化](https://github.com/sgl-project/sglang)**
  `SGLang maintainers / RadixArk` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `sglang`
  围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。
- **Featured:** **[llm-d + LMCache + vLLM](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes)**
  `IBM / Red Hat / llm-d` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kubernetes` `llm-d`
  Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。
- **Featured:** **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `memory` `tensorrt-llm` `vllm`
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。
- **Featured:** **[FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)**
  `NVIDIA / University of Washington` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel` `sglang` `vllm`
  从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。
#### Full Resource List

- **[InfiniStore](https://github.com/bytedance/InfiniStore)**
  `ByteDance` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `lmcache` `vllm`
  高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。
- **[Step-Audio2](https://github.com/stepfun-ai/Step-Audio2)**
  `阶跃星辰` · `2025` · `Open-source project` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving` `multimodal` `vllm`
  端到端音频理解和语音对话模型，提供推理示例与 vLLM backend。
- **[llm-d](https://github.com/llm-d/llm-d)**
  `Red Hat / IBM / Google / NVIDIA 社区` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `routing` `kubernetes` `llm-d`
  将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。
- **[FlexKV](https://github.com/taco-project/FlexKV)**
  `Tencent Cloud TACO + NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `sglang` `vllm`
  分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。
- **[Gemma 4 on vLLM-TPU](https://arxiv.org/abs/2605.25645)**
  `Google TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu` `tpu` `vllm`
  展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。
- **[KV Offloading Connector](https://vllm.ai/blog/kv-offloading-connector)**
  `vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `vllm`
  vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。
- **[Mooncake Joins PyTorch Ecosystem](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/)**
  `Moonshot / PyTorch` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `rag` `sglang` `tensorrt-llm`
  Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。
- **[MooncakeStoreConnector](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/)**
  `vLLM / Mooncake ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `vllm`
  vLLM 文档化 MooncakeStoreConnector，支持 embedded 和 standalone-store 模式，扩展 CPU/SSD KV pool。
- **[vLLM x Mooncake Store](https://vllm.ai/blog/2026-05-06-mooncake-store)**
  `Moonshot / Mooncake / vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `kv-cache` `agent` `vllm` `ttft`
  将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。
- **[vLLM 商业化](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/)**
  `vLLM maintainers / Inferact` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `vllm`
  vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。
- **[vLLM-Omni](https://arxiv.org/abs/2602.02204)**
  `Ant Group + vLLM 社区` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `gpu` `vllm`
  用 stage graph 拆分 LLM、扩散模型和编码器，各阶段独立批处理、分配 GPU，并通过统一 connector 传递中间状态。
- **[vLLM-Omni runtime](https://github.com/vllm-project/vllm-omni)**
  `Ant Group + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `multimodal` `vllm`
  将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。
- **[BentoML / BentoCloud](https://docs.bentoml.com/)**
  `BentoML` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `sglang` `tensorrt-llm`
  统一模型容器、API、batching、资源声明和 autoscaling，并与 vLLM、SGLang、TensorRT-LLM 等 runtime 集成。
- **[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)**
  `NVIDIA` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `tensorrt-llm`
  提供 inflight batching、paged KV、FP8/FP4、speculative decoding、TP/PP/EP 和多节点执行，是 NVIDIA 平台的产品级 LLM 引擎。
- **[Gaudi 2/3 software stack](https://docs.habana.ai/)**
  `Intel` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `vllm`
  通过 SynapseAI、HCCL、FP8 和 vLLM/Optimum Habana 支持 LLM serving，以标准 Ethernet 和成本为差异点。
- **[MLX-LM / vllm-mlx](https://github.com/ml-explore/mlx-lm)**
  `Apple / MLX community` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `vllm`
  利用 Apple silicon 统一内存和 MLX 图执行提供本地 LLM 推理，并开始向 continuous batching 和 vLLM API 兼容扩展。
- **[Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html)**
  `Ray / Anyscale` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `vllm`
  将 vLLM 等 engine 包装为 Ray actor/deployment，提供多节点 replica、路由、autoscaling 和 Python 应用编排。
- **[Truss / TensorRT-LLM serving stack](https://docs.baseten.co/)**
  `Baseten` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `serving` `tensorrt-llm`
  把容器构建、模型打包、TensorRT-LLM 优化、流量伸缩和可观测性组合为生产推理平台。

### 探索观察

最近 180 天内有正式或工程证据、但尚未成为稳定主线的新语境工作。

- **[Ragged Paged Attention for TPU](https://arxiv.org/abs/2604.15464)**
  `Google / TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `tpu` `kernel` `rag`
  面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。
- **[SPIN](https://www.microsoft.com/en-us/research/publication/unifying-sparse-attention-with-hierarchical-memory-for-scalable-long-context-llm-serving/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `rag`
  把 sparse attention execution pipeline 与 CPU/GPU hierarchical KV storage 联合设计，解决不规则 KV subset 检索开销。
