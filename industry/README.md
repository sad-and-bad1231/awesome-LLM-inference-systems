# Industry & Open-Source Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Academic papers](../papers/README.md)

A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Industrial material | With artifact | Tagged records |
|---:|---:|---:|---:|
| 89 | 89 | 71 | 87 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (2)
- [KV Cache](#kv-cache) (14)
- [Prefill–Decode 与传输](#prefill-decode) (13)
- [Speculative Decoding](#speculative-decoding) (4)
- [MoE](#moe) (9)
- [Compiler / DSL](#compiler-dsl) (14)
- [Runtime / Scheduling](#runtime-scheduling) (29)
- [探索观察](#探索观察) (2)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | `core` records form the main reading themes; a bounded `adjacent` window appears under exploration, with full adjacent/archive history on the archive page. |
| Featured | A small editorial starting set; all core records remain below. |

## DeepSeek AI 系统专题

从模型架构到 kernel、通信、存储和应用数据路径的官方系统材料；专题仅作聚合导航，项目仍保留在原主题主表中。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| DeepSeek-V2 | 架构与系统 | [MLA / Multi-head Latent Attention](https://arxiv.org/abs/2412.19437) | 把 KV cache 压到 latent 向量，DeepSeek-V3/R1 系列用 MLA 降低 long-context decode 的 KV 内存和带宽。 | [official](https://arxiv.org/abs/2412.19437) |
| DeepSeek-V2.5 | 架构与系统 | [DeepSeek-V2.5](https://www.deepseek.com/news/deepseek-v2-5/) | DeepSeek-V2.5 官方发布：合并 Chat 与 Coder 两条模型线，官方称在写作、指令跟随与代码等方面大幅提升。 | [official](https://www.deepseek.com/news/deepseek-v2-5/) |
| DeepSeek-V3 | 架构与系统 | [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | DeepSeek-V3 官方模型与推理参考，公开 MLA、DeepSeekMoE、FP8 权重转换及多种 GPU/NPU 运行入口。 | [official](https://github.com/deepseek-ai/DeepSeek-V3) |
| DeepSeek-V3 | 架构与系统 | [Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures](https://arxiv.org/abs/2505.09343) | 从 DeepSeek-V3/R1 的 MLA、MoE、FP8 与 Multi-Plane Network 出发，总结 2,048 张 H800 规模下的模型—硬件协同设计与系统瓶颈。 | [official](https://arxiv.org/abs/2505.09343) |
| DeepSeek-V3.1 | 架构与系统 | [DeepSeek-V3.1](https://api-docs.deepseek.com/news/news250821) | DeepSeek-V3.1 官方发布：一个模型两种模式（Think / Non-Think），128K 上下文，在 V3 之上继续预训练 840B tokens 扩展长上下文。 | [official](https://api-docs.deepseek.com/news/news250821) |
| DeepSeek-V3.2 | 架构与系统 | [DeepSeek-V3.2 / DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) | 在模型架构中加入 sparse attention/indexer，目标是在长上下文和 reasoning/agent 任务中降低推理成本。 | [official](https://arxiv.org/abs/2512.02556) |
| DeepSeek-V4 | 架构与系统 | [DeepSeek-V4](https://api-docs.deepseek.com/news/news260424) | DeepSeek-V4 官方发布：V4-Pro（1.6T 总参 / 49B 激活）与 V4-Flash（284B / 13B 激活），1M 上下文成为默认，引入 token 级压缩 + DSA 稀疏注意力。 | [official](https://api-docs.deepseek.com/news/news260424) |
| DeepSeek-V4.1-Flash | 架构与系统 | [DeepSeek-V4.1-Flash](https://api-docs.deepseek.com/news/news260910) | DeepSeek-V4.1-Flash 官方发布：552B MoE 与因果编码器-解码器架构（输入 8B / 输出 16B 激活），KV cache 仅需上一代 1/4 的 HBM 与 1/8 的 SSD 存储。 | [official](https://api-docs.deepseek.com/news/news260910) |
| DeepSeek-R1 | 架构与系统 | [DeepSeek-R1](https://api-docs.deepseek.com/news/news250120) | DeepSeek-R1 官方发布：大规模 RL 后训练得到的推理模型，性能对标 OpenAI-o1，MIT 许可并开源 6 个蒸馏小模型。 | [official](https://api-docs.deepseek.com/news/news250120) |
| DeepSeek-OCR | OCR 与生态 | [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | 通过视觉 token 压缩处理长文档上下文，并提供 OCR 推理与大规模页面数据生成路径。 | [official](https://github.com/deepseek-ai/DeepSeek-OCR) |
| DeepSeek-OCR-2 | OCR 与生态 | [DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | DeepSeek OCR 的后续官方项目，以 Visual Causal Flow 组织文档视觉理解与生成流程。 | [official](https://github.com/deepseek-ai/DeepSeek-OCR-2) |
| — | 核心算子与通信 | [DeepEP](https://github.com/deepseek-ai/DeepEP) | 面向 MoE expert parallel 的高吞吐、低延迟通信库，提供 dispatch/combine、低延迟模式与 GPU 通信优化。 | [official](https://github.com/deepseek-ai/DeepEP) |
| — | 核心算子与通信 | [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | 面向 FP8/BF16 的 GPU GEMM kernel 库，为 DeepSeek dense 与 MoE 路径提供紧凑、可调优的矩阵乘实现。 | [official](https://github.com/deepseek-ai/DeepGEMM) |
| — | 核心算子与通信 | [DeepGEMM / DeepEP](https://flashmla.net/) | FP8 GEMM 与 MoE expert-parallel 通信库，支撑 DeepSeek 系列训练和推理的 dense/MoE fast path。 | [official](https://flashmla.net/) |
| — | 核心算子与通信 | [FlashMLA](https://github.com/deepseek-ai/FlashMLA) | 面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。 | [official](https://github.com/deepseek-ai/FlashMLA) |
| — | 核心算子与通信 | [TileKernels](https://github.com/deepseek-ai/TileKernels) | 以 TileLang 编写的 kernel library，用 tile 级抽象组织和优化 GPU 算子实现。 | [official](https://github.com/deepseek-ai/TileKernels) |
| — | 存储与数据路径 | [3FS](https://github.com/deepseek-ai/3FS) | 面向 AI 训练与推理负载的高性能分布式文件系统，强调并行数据路径、吞吐与大规模 checkpoint/data access。 | [official](https://github.com/deepseek-ai/3FS) |
| — | 推测解码 | [DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 用于训练、评估和复现实用 speculative decoding 方法的官方工具集，覆盖 draft/verify 与接受率评测。 | [official](https://github.com/deepseek-ai/DeepSpec) |
| — | OCR 与生态 | [Awesome DeepSeek Agents](https://github.com/deepseek-ai/awesome-deepseek-agent) | 面向 DeepSeek Agent、coding agent 与工具调用生态的官方项目索引。 | [official](https://github.com/deepseek-ai/awesome-deepseek-agent) |
| — | OCR 与生态 | [Awesome DeepSeek Integrations](https://github.com/deepseek-ai/awesome-deepseek-integration) | DeepSeek API 在应用、Agent、RAG、开发工具和基础设施中的官方集成索引。 | [official](https://github.com/deepseek-ai/awesome-deepseek-integration) |
| — | OCR 与生态 | [DeepSeek Open Infra Index](https://github.com/deepseek-ai/open-infra-index) | DeepSeek 官方 AI infrastructure 导航入口，集中索引其生产验证的 kernel、通信、存储和系统工具。 | [official](https://github.com/deepseek-ai/open-infra-index) |

## 通义千问 / Qwen 系统专题

Qwen 模型全系代际及其推理、多模态、语音与 Agent 工程材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Qwen | 模型架构 | [Qwen](https://github.com/QwenLM/Qwen) | Qwen 系列首个官方仓库：通义千问对话与预训练大语言模型。 | [official](https://github.com/QwenLM/Qwen) |
| Qwen-VL | 多模态与 Agent | [Qwen-VL](https://github.com/QwenLM/Qwen-VL) | Qwen-VL：通义千问视觉语言模型，支持图文理解与视觉定位。 | [official](https://github.com/QwenLM/Qwen-VL) |
| Qwen-Audio | 多模态与 Agent | [Qwen-Audio](https://github.com/QwenLM/Qwen-Audio) | Qwen-Audio：通义千问音频语言模型，覆盖语音与通用音频理解。 | [official](https://github.com/QwenLM/Qwen-Audio) |
| Qwen2.5 | 模型架构 | [Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) | Qwen2.5-Math：面向数学推理的专用大语言模型系列。 | [official](https://github.com/QwenLM/Qwen2.5-Math) |
| Qwen2.5-Omni | 多模态与 Agent | [Qwen2.5-Omni](https://github.com/QwenLM/Qwen2.5-Omni) | Qwen2.5-Omni：端到端多模态模型，统一文本、图像、音频与视频。 | [official](https://github.com/QwenLM/Qwen2.5-Omni) |
| Qwen2-Audio | 多模态与 Agent | [Qwen2-Audio](https://github.com/QwenLM/Qwen2-Audio) | Qwen2-Audio：音频对话与预训练大语言模型系列。 | [official](https://github.com/QwenLM/Qwen2-Audio) |
| Qwen3 | 模型架构 | [Qwen3](https://github.com/QwenLM/Qwen3) | Qwen3：阿里通义千问第三代大语言模型系列官方仓库。 | [official](https://github.com/QwenLM/Qwen3) |
| Qwen3-VL | 多模态与 Agent | [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | Qwen3-VL：通义千问第三代视觉语言模型系列。 | [official](https://github.com/QwenLM/Qwen3-VL) |
| Qwen3-Coder | 模型架构 | [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | Qwen3-Coder：Qwen3 的代码版本，面向代码生成与 agentic 编码。 | [official](https://github.com/QwenLM/Qwen3-Coder) |
| Qwen3-Omni | 多模态与 Agent | [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) | Qwen3-Omni：原生端到端全模态大语言模型。 | [official](https://github.com/QwenLM/Qwen3-Omni) |
| Qwen3-Embedding | 模型架构 | [Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding) | Qwen3-Embedding：Qwen3 系列的文本嵌入与重排序模型。 | [official](https://github.com/QwenLM/Qwen3-Embedding) |
| Qwen3-TTS | 多模态与 Agent | [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | Qwen3-TTS：开源语音合成模型系列。 | [official](https://github.com/QwenLM/Qwen3-TTS) |
| Qwen3-ASR | 多模态与 Agent | [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | Qwen3-ASR：开源语音识别模型系列。 | [official](https://github.com/QwenLM/Qwen3-ASR) |
| Qwen3.8 | 模型架构 | [Qwen3.8](https://github.com/QwenLM/Qwen3.8) | Qwen3.8：阿里通义千问最新一代大语言模型系列。 | [official](https://github.com/QwenLM/Qwen3.8) |
| Qwen3.8-Flash-Next | 模型架构 | [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) | Qwen3.8-Flash-Next：阿里通义团队的基础模型，面向高吞吐 Flash 推理。 | [official](https://github.com/QwenLM/Qwen3.8-Flash-Next) |
| QwQ | 模型架构 | [QwQ](https://github.com/QwenLM/QwQ) | QwQ：阿里通义团队推理模型系列官方仓库。 | [official](https://github.com/QwenLM/QwQ) |
| Qwen-Image | 多模态与 Agent | [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | Qwen-Image：图像生成基础模型，官方强调复杂文本渲染与精准图像编辑。 | [official](https://github.com/QwenLM/Qwen-Image) |
| Qwen-Image | 多模态与 Agent | [Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) | Qwen-Image-Layered：把图像分解为可独立编辑的图层，实现固有可编辑性。 | [official](https://github.com/QwenLM/Qwen-Image-Layered) |
| Qwen-Image-2.1 | 多模态与 Agent | [Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1) | Qwen-Image-2.1：官方定位为 Qwen 最强的开源图像生成模型。 | [official](https://github.com/QwenLM/Qwen-Image-2.1) |
| Qwen-VLA | 多模态与 Agent | [Qwen-VLA](https://github.com/QwenLM/Qwen-VLA) | Qwen-VLA：视觉-语言-动作模型的官方仓库。 | [official](https://github.com/QwenLM/Qwen-VLA) |
| — | 推理系统 | [Aegaeon](https://dblp.org/db/conf/sosp/sosp2025.html) | 在共享 GPU 池中复用模型和显存，避免 marketplace 中大量低流量模型各自独占设备。 | [official](https://dblp.org/db/conf/sosp/sosp2025.html) |
| — | 推理系统 | [BladeLLM](https://www.alibabacloud.com/help/doc-detail/2865199.html) | PAI 上的高性能 LLM inference engine，用于低延迟、高吞吐部署 Qwen 等模型。 | [official](https://www.alibabacloud.com/help/doc-detail/2865199.html) |
| — | 推理系统 | [COMET](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) | 细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。 | [official](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) |
| — | 推理系统 | [FlashQLA](https://github.com/QwenLM/FlashQLA) | FlashQLA：基于 TileLang 构建的高性能线性注意力 kernel 库。 | [official](https://github.com/QwenLM/FlashQLA) |
| — | 推理系统 | [FlowKV](https://arxiv.org/abs/2504.03775) | 在 PD 分离式架构中优化 KV cache transfer，并做 load-aware scheduling。 | [official](https://arxiv.org/abs/2504.03775) |
| — | 推理系统 | [HydraServe](https://www.usenix.org/conference/nsdi26/technical-sessions) | 主动分发模型并重叠加载、runtime 初始化和 worker 启动，同时通过拓扑感知放置避免多实例网络争用。 | [official](https://www.usenix.org/conference/nsdi26/technical-sessions) |
| — | 推理系统 | [qwen.cpp](https://github.com/QwenLM/qwen.cpp) | qwen.cpp：通义千问的 C++ 推理实现。 | [official](https://github.com/QwenLM/qwen.cpp) |
| — | 推理系统 | [Qwen3-ASR-Toolkit](https://github.com/QwenLM/Qwen3-ASR-Toolkit) | Qwen3-ASR API 官方 Python 工具包，支持并行高吞吐转写。 | [official](https://github.com/QwenLM/Qwen3-ASR-Toolkit) |
| — | 推理系统 | [RTP-LLM](https://arxiv.org/abs/2605.29639) | 将并行加载、PD 分离、分层 KV 复用、模块化推测解码、自适应 KV 量化和多模态解耦整合进生产引擎，论文称已服务超过一亿用户。 | [official](https://arxiv.org/abs/2605.29639) |
| — | 推理系统 | [ServeGen](https://github.com/alibaba/ServeGen) | 从全球云端 LLM 服务提取语言、多模态和 reasoning workload 特征，并开源按 client 组合的 trace generator。 | [official](https://github.com/alibaba/ServeGen) |
| — | 推理系统 | [Tair-KVCache-HiSim](https://www.alibabacloud.com/blog/603164) | 面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。 | [official](https://www.alibabacloud.com/blog/603164) |
| — | 多模态与 Agent | [Qwen-Drive-1.0](https://github.com/QwenLM/Qwen-Drive-1.0) | Qwen-Drive-1.0：面向自动驾驶的视觉语言基础模型（官方定位为初始一步）。 | [official](https://github.com/QwenLM/Qwen-Drive-1.0) |
| — | 工具与生态 | [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | Qwen-Agent：基于 Qwen 的 agent 框架与应用，支持函数调用与代码解释器。 | [official](https://github.com/QwenLM/Qwen-Agent) |
| — | 工具与生态 | [Qwen-AgentWorld](https://github.com/QwenLM/Qwen-AgentWorld) | Qwen-AgentWorld：面向通用 agent 的语言世界模型。 | [official](https://github.com/QwenLM/Qwen-AgentWorld) |
| — | 工具与生态 | [qwen-code](https://github.com/QwenLM/qwen-code) | qwen-code：运行在终端中的开源 AI 编码 agent。 | [official](https://github.com/QwenLM/qwen-code) |
| — | 工具与生态 | [Qwen-Cookbook](https://github.com/QwenLM/Qwen-Cookbook) | Qwen Cookbook：面向 Qwen 的开源示例与使用指南。 | [official](https://github.com/QwenLM/Qwen-Cookbook) |
| — | 工具与生态 | [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) | Qwen-MM-Plugins：让任意 agent harness 原生支持多模态。 | [official](https://github.com/QwenLM/Qwen-MM-Plugins) |
| — | 工具与生态 | [Qwen3Guard](https://github.com/QwenLM/Qwen3Guard) | Qwen3Guard：多语言安全护栏（guardrail）模型系列。 | [official](https://github.com/QwenLM/Qwen3Guard) |

## Moonshot / Kimi 系统专题

Kimi 模型代际与其配套的推理、存储与 Agent 工程材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Kimi-K1.5 | 模型架构 | [Kimi-k1.5](https://github.com/MoonshotAI/Kimi-k1.5) | Kimi k1.5 官方仓库，K 系列推理模型代际之一（官方仓库未附描述文本）。 | [official](https://github.com/MoonshotAI/Kimi-k1.5) |
| Kimi-K2 | 模型架构 | [Kimi-K2](https://github.com/MoonshotAI/Kimi-K2) | Kimi K2 是月之暗面团队开发的大语言模型系列官方仓库，公开模型与使用入口。 | [official](https://github.com/MoonshotAI/Kimi-K2) |
| Kimi-K2.5 | 模型架构 | [Kimi-K2.5](https://github.com/MoonshotAI/Kimi-K2.5) | Kimi K2.5 官方仓库，官方定位为 Open Visual Agentic Intelligence。 | [official](https://github.com/MoonshotAI/Kimi-K2.5) |
| Kimi-K3 | 模型架构 | [Kimi-K3](https://github.com/MoonshotAI/Kimi-K3) | Kimi K3 官方仓库，官方定位为 Open Frontier Intelligence。 | [official](https://github.com/MoonshotAI/Kimi-K3) |
| Kimi-Linear | 模型架构 | [Kimi-Linear](https://github.com/MoonshotAI/Kimi-Linear) | Kimi 线性注意力模型线的官方仓库（官方仓库未附描述文本）。 | [official](https://github.com/MoonshotAI/Kimi-Linear) |
| — | 模型架构 | [MoBA](https://github.com/MoonshotAI/MoBA) | MoBA: Mixture of Block Attention for Long-Context LLMs，面向长上下文的块稀疏注意力机制。 | [official](https://github.com/MoonshotAI/MoBA) |
| — | 推理系统 | [checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine) | Checkpoint-engine：用于在 LLM 推理引擎中更新模型权重的轻量中间件。 | [official](https://github.com/MoonshotAI/checkpoint-engine) |
| — | 推理系统 | [FlashKDA](https://github.com/MoonshotAI/FlashKDA) | FlashKDA：高性能 Kimi Delta Attention kernel 库。 | [official](https://github.com/MoonshotAI/FlashKDA) |
| — | 推理系统 | [MoonEP](https://github.com/MoonshotAI/MoonEP) | MoonEP：通过动态冗余专家实现负载均衡的专家并行（expert parallelism）库。 | [official](https://github.com/MoonshotAI/MoonEP) |
| — | 训练与数据 | [Moonlight](https://github.com/MoonshotAI/Moonlight) | Moonlight：验证 Muon 优化器在 LLM 训练中可扩展性的官方工作。 | [official](https://github.com/MoonshotAI/Moonlight) |
| — | 多模态与 Agent | [Kimi-Audio](https://github.com/MoonshotAI/Kimi-Audio) | Kimi-Audio：开源音频基础模型，覆盖音频理解、生成与对话。 | [official](https://github.com/MoonshotAI/Kimi-Audio) |
| — | 多模态与 Agent | [Kimi-VL](https://github.com/MoonshotAI/Kimi-VL) | Kimi-VL：MoE 视觉语言模型，面向多模态推理、长上下文理解与 Agent 能力。 | [official](https://github.com/MoonshotAI/Kimi-VL) |
| — | 工具与生态 | [kimi-code](https://github.com/MoonshotAI/kimi-code) | Kimi Code CLI，官方定位为面向下一代 Agent 的起点。 | [official](https://github.com/MoonshotAI/kimi-code) |

## MiniMax 系统专题

MiniMax 模型代际与其推理、多模态与 Agent 工具链材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| MiniMax-01 | 模型架构 | [MiniMax-01](https://github.com/MiniMax-AI/MiniMax-01) | MiniMax-Text-01 与 MiniMax-VL-01 官方仓库，基于 Linear Attention 的大语言模型与视觉语言模型。 | [official](https://github.com/MiniMax-AI/MiniMax-01) |
| MiniMax-M1 | 模型架构 | [MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) | MiniMax-M1：官方称其为全球首个开放权重的大规模 hybrid-attention 推理模型。 | [official](https://github.com/MiniMax-AI/MiniMax-M1) |
| MiniMax-M2 | 模型架构 | [MiniMax-M2](https://github.com/MiniMax-AI/MiniMax-M2) | MiniMax-M2：为 coding 与 agentic 工作流打造的模型。 | [official](https://github.com/MiniMax-AI/MiniMax-M2) |
| MiniMax-M2.1 | 模型架构 | [MiniMax-M2.1](https://github.com/MiniMax-AI/MiniMax-M2.1) | MiniMax M2.1：官方定位为面向真实开发与 agent 场景的 SOTA 模型。 | [official](https://github.com/MiniMax-AI/MiniMax-M2.1) |
| MiniMax-M2.5 | 模型架构 | [MiniMax-M2.5](https://github.com/MiniMax-AI/MiniMax-M2.5) | MiniMax-M2.5 官方仓库；官方 README 将其定位为 MiniMax 最新模型（M2 系列代际之一）。 | [official](https://github.com/MiniMax-AI/MiniMax-M2.5) |
| MiniMax-M2.7 | 模型架构 | [MiniMax-M2.7](https://github.com/MiniMax-AI/MiniMax-M2.7) | MiniMax-M2.7 是官方首个深度参与自身演进的模型，能构建复杂 agent harness，并借助 Agent Teams 与 Skills 完成复杂生产力任务（官方 README）。 | [official](https://github.com/MiniMax-AI/MiniMax-M2.7) |
| MiniMax-M3 | 模型架构 | [MiniMax-M3](https://github.com/MiniMax-AI/MiniMax-M3) | MiniMax-M3 是原生多模态模型，支持 1M 上下文，约 428B 总参数 / 23B 激活参数（官方 README）。 | [official](https://github.com/MiniMax-AI/MiniMax-M3) |
| MiniMax-Music3 | 多模态与 Agent | [MiniMax-Music3](https://github.com/MiniMax-AI/MiniMax-Music3) | MiniMax Music 3：高性能音乐生成模型，可依歌词与音乐描述生成最长五分钟、结构完整的歌曲（官方 README）。 | [official](https://github.com/MiniMax-AI/MiniMax-Music3) |
| — | 训练与数据 | [SynLogic](https://github.com/MiniMax-AI/SynLogic) | SynLogic（NeurIPS 2025）：面向可验证推理任务的合成数据工作。 | [official](https://github.com/MiniMax-AI/SynLogic) |
| — | 训练与数据 | [VTP](https://github.com/MiniMax-AI/VTP) | VTP（ECCV 2026）：面向生成任务的视觉 tokenizer 可扩展预训练。 | [official](https://github.com/MiniMax-AI/VTP) |
| — | 多模态与 Agent | [audio-tools](https://github.com/MiniMax-AI/audio-tools) | 面向文本转音频的优化工具集，覆盖训练与推理工作流。 | [official](https://github.com/MiniMax-AI/audio-tools) |
| — | 多模态与 Agent | [One-RL-to-See-Them-All](https://github.com/MiniMax-AI/One-RL-to-See-Them-All) | One RL to See Them All：视觉三重统一强化学习的官方实现。 | [official](https://github.com/MiniMax-AI/One-RL-to-See-Them-All) |
| — | 工具与生态 | [cli](https://github.com/MiniMax-AI/cli) | MiniMax 官方 CLI：生成文本、图像、视频、语音与音乐。 | [official](https://github.com/MiniMax-AI/cli) |
| — | 工具与生态 | [Mini-Agent](https://github.com/MiniMax-AI/Mini-Agent) | Mini-Agent：最小但完整的单 agent 示例工程，展示 agent 的核心执行流水线与生产级特性。 | [official](https://github.com/MiniMax-AI/Mini-Agent) |
| — | 工具与生态 | [MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | MiniMax 官方 MCP server，接入其 TTS、图像生成与视频生成 API。 | [official](https://github.com/MiniMax-AI/MiniMax-MCP) |
| — | 工具与生态 | [OpenRoom](https://github.com/MiniMax-AI/OpenRoom) | OpenRoom：浏览器内的桌面环境，让 AI Agent 以自然语言操作各类应用。 | [official](https://github.com/MiniMax-AI/OpenRoom) |

## 智谱 / Z.ai 系统专题

GLM 模型代际与其推理、多模态与 Agent 工程材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| GLM-130B | 模型架构 | [GLM-130B](https://github.com/zai-org/GLM-130B) | GLM-130B：开源双语预训练模型（ICLR 2023）。 | [official](https://github.com/zai-org/GLM-130B) |
| ChatGLM-6B | 模型架构 | [ChatGLM-6B](https://github.com/zai-org/ChatGLM-6B) | ChatGLM-6B：开源双语对话语言模型。 | [official](https://github.com/zai-org/ChatGLM-6B) |
| ChatGLM2-6B | 模型架构 | [ChatGLM2-6B](https://github.com/zai-org/ChatGLM2-6B) | ChatGLM2-6B：开源双语对话 LLM。 | [official](https://github.com/zai-org/ChatGLM2-6B) |
| ChatGLM3 | 模型架构 | [ChatGLM3](https://github.com/zai-org/ChatGLM3) | ChatGLM3 系列：开源双语对话 LLM。 | [official](https://github.com/zai-org/ChatGLM3) |
| GLM-4 | 模型架构 | [GLM-4](https://github.com/zai-org/GLM-4) | GLM-4 系列：开源多语言多模态对话模型。 | [official](https://github.com/zai-org/GLM-4) |
| GLM-4-Voice | 多模态与 Agent | [GLM-4-Voice](https://github.com/zai-org/GLM-4-Voice) | GLM-4-Voice：端到端中英语音对话模型。 | [official](https://github.com/zai-org/GLM-4-Voice) |
| GLM-4.5 | 模型架构 | [GLM-4.5](https://github.com/zai-org/GLM-4.5) | GLM-4.5：面向 Agentic、Reasoning 与 Coding（ARC）的基础模型。 | [official](https://github.com/zai-org/GLM-4.5) |
| GLM-5 | 模型架构 | [GLM-5](https://github.com/zai-org/GLM-5) | GLM-5：官方定位从 Vibe Coding 走向 Agentic Engineering。 | [official](https://github.com/zai-org/GLM-5) |
| GLM-5.2 | 模型架构 | [GLM-5.2](https://z.ai/blog/glm-5.2) | GLM-5.2 官方发布：面向长程任务的新旗舰，稳定 1M 上下文；提出 IndexShare（每 4 层共享 indexer，1M 上下文下每 token FLOPs 降低 2.9×）并改进 MTP，推测解码接受长度最高提升 20%。 | [official](https://z.ai/blog/glm-5.2) |
| GLM-5.3 | 模型架构 | [GLM-5.3](https://z.ai/blog/glm-5.3) | GLM-5.3 官方发布：与 GLM-5.2 共用基座、仅靠扩展后训练，在复杂编码、长程任务与新兴网络攻防能力上取得大幅跃升。 | [official](https://z.ai/blog/glm-5.3) |
| GLM-Edge | 模型架构 | [GLM-Edge](https://github.com/zai-org/GLM-Edge) | GLM-Edge：GLM 系列端侧模型。 | [official](https://github.com/zai-org/GLM-Edge) |
| GLM-V | 多模态与 Agent | [GLM-V](https://github.com/zai-org/GLM-V) | GLM-4.6V / 4.5V / 4.1V-Thinking：以可扩展强化学习迈向通用多模态推理。 | [official](https://github.com/zai-org/GLM-V) |
| GLM-Image | 多模态与 Agent | [GLM-Image](https://github.com/zai-org/GLM-Image) | GLM-Image：采用混合自回归 + 扩散解码器架构的图像生成模型；官方 README 称其通用生成质量对齐主流 latent diffusion，并在密集知识场景有优势。 | [official](https://github.com/zai-org/GLM-Image) |
| GLM-OCR | 多模态与 Agent | [GLM-OCR](https://github.com/zai-org/GLM-OCR) | GLM-OCR：官方定位为准确、快速、全面的 OCR 模型。 | [official](https://github.com/zai-org/GLM-OCR) |
| GLM-TTS | 多模态与 Agent | [GLM-TTS](https://github.com/zai-org/GLM-TTS) | GLM-TTS：基于多奖励强化学习的可控、富情感零样本 TTS。 | [official](https://github.com/zai-org/GLM-TTS) |
| GLM-ASR | 多模态与 Agent | [GLM-ASR](https://github.com/zai-org/GLM-ASR) | GLM-ASR-Nano：1.5B 参数的鲁棒开源语音识别模型。 | [official](https://github.com/zai-org/GLM-ASR) |
| — | 模型架构 | [CodeGeeX4](https://github.com/zai-org/CodeGeeX4) | CodeGeeX4-ALL-9B：覆盖代码补全、代码解释器、Web 搜索与函数调用等场景的多用途模型。 | [official](https://github.com/zai-org/CodeGeeX4) |
| — | 工具与生态 | [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM) | Open-AutoGLM：开源手机 Agent 模型与框架。 | [official](https://github.com/zai-org/Open-AutoGLM) |
| — | 工具与生态 | [Synapse](https://github.com/zai-org/Synapse) | Synapse：自托管 AI 工作空间，支持可共享的 AI 队友、共享会话与记忆。 | [official](https://github.com/zai-org/Synapse) |

## 阶跃星辰 / StepFun 系统专题

Step 模型代际与其推理、语音、视频与多模态工程材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Step3 | 模型架构 | [Step3](https://github.com/stepfun-ai/Step3) | Step3：MoE 架构的多模态推理模型，321B 总参数 / 38B 激活；官方 README 称其端到端以最小化解码成本为设计目标。 | [official](https://github.com/stepfun-ai/Step3) |
| Step3-VL-10B | 多模态与 Agent | [Step3-VL-10B](https://github.com/stepfun-ai/Step3-VL-10B) | Step3-VL-10B：10B 规模的紧凑多模态模型；官方称达到该量级 SOTA，可比肩 10–20 倍参数量的模型。 | [official](https://github.com/stepfun-ai/Step3-VL-10B) |
| Step-3.5-Flash | 模型架构 | [Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash) | Step-3.5-Flash：官方定位快速、锐利且可靠的 agentic intelligence。 | [official](https://github.com/stepfun-ai/Step-3.5-Flash) |
| Step-3.7-Flash | 模型架构 | [Step-3.7-Flash](https://github.com/stepfun-ai/Step-3.7-Flash) | Step-3.7-Flash：面向真实 agent 场景的高效率 Flash 模型。 | [official](https://github.com/stepfun-ai/Step-3.7-Flash) |
| Step-Audio | 多模态与 Agent | [Step-Audio](https://github.com/stepfun-ai/Step-Audio) | Step-Audio：面向智能语音交互的开源框架，统一理解与生成，含 130B 多模态模型与 3B TTS，支持多语言、情感语气与方言。官方已标注该仓库不再维护，指向 Step-Audio2 / Step-Audio-R1 / Step-Audio-EditX。 | [official](https://github.com/stepfun-ai/Step-Audio) |
| Step-Audio2 | 多模态与 Agent | [Step-Audio2](https://github.com/stepfun-ai/Step-Audio2) | Step-Audio 2：面向工业级音频理解与语音对话的端到端多模态大模型。 | [official](https://github.com/stepfun-ai/Step-Audio2) |
| Step-Audio-R1 | 多模态与 Agent | [Step-Audio-R1](https://github.com/stepfun-ai/Step-Audio-R1) | Step-Audio-R1 方向；官方随仓库发布 Step-Audio-R1.5 的三个独立评测基准。 | [official](https://github.com/stepfun-ai/Step-Audio-R1) |
| Step-Audio-EditX | 多模态与 Agent | [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) | Step-Audio-EditX：3B 参数、基于强化学习的音频编辑模型，可编辑情感、说话风格与副语言特征。 | [official](https://github.com/stepfun-ai/Step-Audio-EditX) |
| Step-Video-T2V | 多模态与 Agent | [Step-Video-T2V](https://github.com/stepfun-ai/Step-Video-T2V) | Step-Video-T2V：文生视频模型的官方推理代码与权重（含 Turbo 版本），技术报告 arXiv 2502.10248。 | [official](https://github.com/stepfun-ai/Step-Video-T2V) |
| Step-Video-TI2V | 多模态与 Agent | [Step-Video-TI2V](https://github.com/stepfun-ai/Step-Video-TI2V) | 基于 Step-Video-T2V 的图像到视频（I2V）模型，提供 motion score 控制生成动态幅度。 | [official](https://github.com/stepfun-ai/Step-Video-TI2V) |
| Step1X-Edit | 多模态与 Agent | [Step1X-Edit](https://github.com/stepfun-ai/Step1X-Edit) | Step1X-Edit：开源图像编辑模型；官方称其可比肩 GPT-4o、Gemini 2 Flash 等闭源模型。 | [official](https://github.com/stepfun-ai/Step1X-Edit) |
| Step1X-3D | 多模态与 Agent | [Step1X-3D](https://github.com/stepfun-ai/Step1X-3D) | Step1X-3D：高保真、可控的带纹理 3D 资产生成。 | [official](https://github.com/stepfun-ai/Step1X-3D) |
| NextStep-1 | 多模态与 Agent | [NextStep-1](https://github.com/stepfun-ai/NextStep-1) | NextStep-1（ICLR 2026 Oral）：以连续 token 做自回归图像生成的 SOTA 工作。 | [official](https://github.com/stepfun-ai/NextStep-1) |
| — | 推理系统 | [StepMesh](https://github.com/stepfun-ai/StepMesh) | StepMesh：面向 Attention-FFN 解耦架构的高性能、低延迟通信库。 | [official](https://github.com/stepfun-ai/StepMesh) |
| — | 训练与数据 | [SteptronOss](https://github.com/stepfun-ai/SteptronOss) | SteptronOss：轻量、AI-native 的大语言模型训练框架，强调快速迭代、可复现实验与模块化配置。 | [official](https://github.com/stepfun-ai/SteptronOss) |
| — | 工具与生态 | [gelab-zero](https://github.com/stepfun-ai/gelab-zero) | STEP-GUI：由 StepFun-GELab 团队开发的 GUI agent 方案。 | [official](https://github.com/stepfun-ai/gelab-zero) |
| — | 工具与生态 | [Step-Realtime-CLI](https://github.com/stepfun-ai/Step-Realtime-CLI) | step-realtime-cli：终端 AI 编码助手，支持文本与实时语音交互，用于读代码、改文件与执行命令。 | [official](https://github.com/stepfun-ai/Step-Realtime-CLI) |

## 字节 Seed / 火山引擎系统专题

Seed 模型代际与其推理、训练与系统基础设施材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Seed1.5-VL | 多模态与 Agent | [Seed1.5-VL](https://github.com/ByteDance-Seed/Seed1.5-VL) | Seed1.5-VL：面向通用多模态理解与推理的视觉语言基础模型。 | [official](https://github.com/ByteDance-Seed/Seed1.5-VL) |
| Seed-Thinking-v1.5 | 模型架构 | [Seed-Thinking-v1.5](https://github.com/ByteDance-Seed/Seed-Thinking-v1.5) | Seed-Thinking-v1.5：具备先思考再作答能力的推理模型；官方 README 给出 AIME 2024 86.7、Codeforces 55.0 等指标。 | [official](https://github.com/ByteDance-Seed/Seed-Thinking-v1.5) |
| seed-oss | 模型架构 | [seed-oss](https://github.com/ByteDance-Seed/seed-oss) | seed-oss 系列模型，以 Apache-2.0 许可向开源社区发布（官方 README）。 | [official](https://github.com/ByteDance-Seed/seed-oss) |
| Seed-Coder | 模型架构 | [Seed-Coder](https://github.com/ByteDance-Seed/Seed-Coder) | Seed-Coder：轻量开源代码 LLM 系列，含 base、instruct 与 reasoning 三个版本。 | [official](https://github.com/ByteDance-Seed/Seed-Coder) |
| Seed-X-7B | 模型架构 | [Seed-X-7B](https://github.com/ByteDance-Seed/Seed-X-7B) | Seed-X：开源多语言翻译模型系列，包含 instruct 模型、强化学习模型与奖励模型。 | [official](https://github.com/ByteDance-Seed/Seed-X-7B) |
| Seed-Prover | 模型架构 | [Seed-Prover](https://github.com/ByteDance-Seed/Seed-Prover) | Seed AI4Math 组的形式化证明项目页，涵盖 Seed-Prover 1.5、Seed-Prover 与 Delta-Prover。 | [official](https://github.com/ByteDance-Seed/Seed-Prover) |
| BFS-Prover-V2 | 模型架构 | [BFS-Prover-V2](https://github.com/ByteDance-Seed/BFS-Prover-V2) | BFS-Prover-V2：面向 Lean4 的 SOTA 开源步级定理证明系统，针对训练与推理两侧的可扩展性。 | [official](https://github.com/ByteDance-Seed/BFS-Prover-V2) |
| Stable-DiffCoder | 模型架构 | [Stable-DiffCoder](https://github.com/ByteDance-Seed/Stable-DiffCoder) | Stable-DiffCoder：轻量开源代码扩散语言模型（DLLM）系列，含 base 与 instruct 版本。 | [official](https://github.com/ByteDance-Seed/Stable-DiffCoder) |
| — | 模型架构 | [AHN](https://github.com/ByteDance-Seed/AHN) | AHN（Artificial Hippocampus Networks）：面向高效长上下文建模。 | [official](https://github.com/ByteDance-Seed/AHN) |
| — | 模型架构 | [decoupleQ](https://github.com/ByteDance-Seed/decoupleQ) | decoupleQ：一种面向 LLM 的量化算法。 | [official](https://github.com/ByteDance-Seed/decoupleQ) |
| — | 推理系统 | [Astral](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) | 从拓扑、路由、拥塞控制和作业编排构建大模型数据中心网络，是企业 AI fabric 的生产案例。 | [official](https://dblp.org/db/conf/sigcomm/sigcomm2025.html) |
| — | 推理系统 | [cudaLLM](https://github.com/ByteDance-Seed/cudaLLM) | cudaLLM：训练 LLM 自动生成高效且正确 CUDA kernel 的完整流水线，采用 SFT + RL 两阶段。 | [official](https://github.com/ByteDance-Seed/cudaLLM) |
| — | 推理系统 | [entangle](https://github.com/ByteDance-Seed/entangle) | entangle（ASPLOS'26）：论文 “It Takes Two to Entangle” 的官方代码。 | [official](https://github.com/ByteDance-Seed/entangle) |
| — | 推理系统 | [FlexPrefill](https://github.com/ByteDance-Seed/FlexPrefill) | FlexPrefill（ICLR 2025 Oral）：面向高效长序列推理的上下文感知稀疏注意力机制。 | [official](https://github.com/ByteDance-Seed/FlexPrefill) |
| — | 推理系统 | [InfiniStore](https://github.com/bytedance/InfiniStore) | 高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。 | [official](https://github.com/bytedance/InfiniStore) |
| — | 推理系统 | [LightSeq](https://github.com/bytedance/lightseq) | 通过 fused layer、定制 CUDA kernel 和显存复用部署 NLP 与生成模型。 | [official](https://github.com/bytedance/lightseq) |
| — | 推理系统 | [MegaScale-Infer](https://arxiv.org/abs/2504.02263) | 将 attention 和 MoE FFN 分池部署，以 disaggregated expert parallelism、ping-pong pipeline 和 M2N 通信提升专家利用率。 | [official](https://arxiv.org/abs/2504.02263) |
| — | 推理系统 | [ShadowKV](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference) | GPU 只保留低秩 keys、landmarks 和少量 outliers，values 放 CPU DRAM，decode 时按需召回 Top-K value。 | [official](https://seed.bytedance.com/zh/public_papers/shadowkv-kv-cache-in-shadows-for-high-throughput-long-context-llm-inference) |
| — | 推理系统 | [SwiftSpec](https://arxiv.org/abs/2506.11309) | 异步扩展 draft/target 执行，配合 tree-aware KV 管理和 fused kernel，面向交互式单请求降低解码延迟。 | [official](https://arxiv.org/abs/2506.11309) |
| — | 推理系统 | [Triton-distributed](https://github.com/ByteDance-Seed/Triton-distributed) | Triton-distributed：分布式编译器与优化并行 kernel。 | [official](https://github.com/ByteDance-Seed/Triton-distributed) |
| — | 训练与数据 | [ByteCheckpoint](https://github.com/ByteDance-Seed/ByteCheckpoint) | ByteCheckpoint：面向大基础模型（LFM）的统一 checkpoint 库。 | [official](https://github.com/ByteDance-Seed/ByteCheckpoint) |
| — | 训练与数据 | [DATAMASK](https://github.com/ByteDance-Seed/DATAMASK) | DATAMASK：基于策略梯度掩码学习的大规模预训练数据联合筛选。 | [official](https://github.com/ByteDance-Seed/DATAMASK) |
| — | 训练与数据 | [SDP4Bit](https://github.com/ByteDance-Seed/SDP4Bit) | SDP4Bit：面向 LLM 训练的 sharded data parallelism 4-bit 通信量化。 | [official](https://github.com/ByteDance-Seed/SDP4Bit) |
| — | 训练与数据 | [VeOmni](https://github.com/ByteDance-Seed/VeOmni) | VeOmni：以模型为中心的分布式训练配方库，覆盖任意模态的模型训练扩展。 | [official](https://github.com/ByteDance-Seed/VeOmni) |
| — | 多模态与 Agent | [Bagel](https://github.com/ByteDance-Seed/Bagel) | Bagel：开源统一多模态模型。 | [official](https://github.com/ByteDance-Seed/Bagel) |

## 小米 MiMo 系统专题

MiMo 模型代际与其音频、视觉语言、具身与代码工程材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| MiMo | 模型架构 | [MiMo](https://github.com/XiaomiMiMo/MiMo) | MiMo：小米官方仓库，官方定位为从预训练解锁语言模型推理潜力。 | [official](https://github.com/XiaomiMiMo/MiMo) |
| MiMo-VL | 多模态与 Agent | [MiMo-VL](https://github.com/XiaomiMiMo/MiMo-VL) | MiMo-VL：小米视觉语言模型官方仓库。 | [official](https://github.com/XiaomiMiMo/MiMo-VL) |
| MiMo-Audio | 多模态与 Agent | [MiMo-Audio](https://github.com/XiaomiMiMo/MiMo-Audio) | MiMo-Audio：音频语言模型，官方定位为 few-shot learner。 | [official](https://github.com/XiaomiMiMo/MiMo-Audio) |
| MiMo-Embodied | 多模态与 Agent | [MiMo-Embodied](https://github.com/XiaomiMiMo/MiMo-Embodied) | MiMo-Embodied：面向具身智能的官方模型。 | [official](https://github.com/XiaomiMiMo/MiMo-Embodied) |
| MiMo-V2-Flash | 模型架构 | [MiMo-V2-Flash](https://github.com/XiaomiMiMo/MiMo-V2-Flash) | MiMo-V2-Flash：面向推理、编码与 agent 的高效基础模型。 | [official](https://github.com/XiaomiMiMo/MiMo-V2-Flash) |
| MiMo-V2.5 | 多模态与 Agent | [MiMo-V2.5-ASR](https://github.com/XiaomiMiMo/MiMo-V2.5-ASR) | MiMo-V2.5-ASR：官方定位跨语言、跨方言与复杂声学环境下的鲁棒语音识别。 | [official](https://github.com/XiaomiMiMo/MiMo-V2.5-ASR) |
| MiMo-Code | 工具与生态 | [MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) | MiMo Code：官方定位「模型与 agent 共同演化」。 | [official](https://github.com/XiaomiMiMo/MiMo-Code) |
| — | 训练与数据 | [MiMo-Audio-Training](https://github.com/XiaomiMiMo/MiMo-Audio-Training) | MiMo-Audio 的训练代码与配方。 | [official](https://github.com/XiaomiMiMo/MiMo-Audio-Training) |
| — | 多模态与 Agent | [MiMo-Audio-Tokenizer](https://github.com/XiaomiMiMo/MiMo-Audio-Tokenizer) | 统一音频 tokenizer，可同时抽取语义与声学信息。 | [official](https://github.com/XiaomiMiMo/MiMo-Audio-Tokenizer) |
| — | 工具与生态 | [awesome-mimo-agent](https://github.com/XiaomiMiMo/awesome-mimo-agent) | MiMo agent 方向的官方资源索引。 | [official](https://github.com/XiaomiMiMo/awesome-mimo-agent) |
| — | 工具与生态 | [MiMo-Skills](https://github.com/XiaomiMiMo/MiMo-Skills) | 小米 MiMo 系列模型的 agent skills。 | [official](https://github.com/XiaomiMiMo/MiMo-Skills) |

## 腾讯混元 / Tencent AI 系统专题

腾讯混元模型代际与其推理引擎、注意力与压缩算子、KV 缓存、通信与端侧部署材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Hunyuan-Large | 模型代际 | [Tencent-Hunyuan-Large](https://github.com/Tencent-Hunyuan/Tencent-Hunyuan-Large) | 腾讯混元大语言模型 Hunyuan-Large 官方仓库，混元 LLM 线最早的开源入口。 | [official](https://github.com/Tencent-Hunyuan/Tencent-Hunyuan-Large) |
| HunyuanVideo | 模型代际 | [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | HunyuanVideo 官方仓库：面向大规模视频生成的系统化框架。 | [official](https://github.com/Tencent-Hunyuan/HunyuanVideo) |
| HunyuanVideo | 模型代际 | [HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | HunyuanVideo-1.5 官方仓库，官方定位为领先的轻量级视频生成模型。 | [official](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) |
| Hunyuan-TurboS | 模型代际 | [Hunyuan-TurboS](https://github.com/Tencent-Hunyuan/Hunyuan-TurboS) | Hunyuan-TurboS 官方仓库：通过 Mamba-Transformer 协同与自适应思维链推进的混元大模型。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan-TurboS) |
| Hunyuan3D | 模型代际 | [Hunyuan3D-1](https://github.com/Tencent-Hunyuan/Hunyuan3D-1) | Hunyuan3D-1.0 官方仓库：统一的文生 3D 与图生 3D 生成框架。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan3D-1) |
| Hunyuan3D | 模型代际 | [Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) | Hunyuan3D-2 官方仓库：基于大规模扩散模型生成高分辨率 3D 资产。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) |
| Hunyuan3D | 模型代际 | [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) | Hunyuan3D-2.1 官方仓库：从图像生成带生产级 PBR 材质的高保真 3D 资产。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) |
| Hunyuan3D | 模型代际 | [Hunyuan3D-Omni](https://github.com/Tencent-Hunyuan/Hunyuan3D-Omni) | Hunyuan3D-Omni 官方仓库：可控 3D 资产生成的统一框架。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan3D-Omni) |
| Hunyuan-A13B | 模型代际 | [Hunyuan-A13B](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) | Hunyuan-A13B 官方仓库，官方定位为基于细粒度 MoE 架构的开源大语言模型。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) |
| Hunyuan-MT | 模型代际 | [Hunyuan-MT](https://github.com/Tencent-Hunyuan/Hunyuan-MT) | Hunyuan-MT 官方仓库：由翻译模型 Hunyuan-MT-7B 与集成模型 Hunyuan-MT-Chimera 组成。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan-MT) |
| Hunyuan-MT | 模型代际 | [Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) | Hy-MT2 官方仓库：「快思考」多语言翻译模型族，含 1.8B / 7B / 30B-A3B（MoE）三档，支持 33 语种互译。 | [official](https://github.com/Tencent-Hunyuan/Hy-MT2) |
| Hunyuan-7B | 模型代际 | [Hunyuan-7B](https://github.com/Tencent-Hunyuan/Hunyuan-7B) | 腾讯混元 7B 稠密大语言模型官方仓库。 | [official](https://github.com/Tencent-Hunyuan/Hunyuan-7B) |
| HunyuanImage | 模型代际 | [HunyuanImage-2.1](https://github.com/Tencent-Hunyuan/HunyuanImage-2.1) | HunyuanImage-2.1 官方仓库：面向高分辨率（2K）文生图的高效扩散模型。 | [official](https://github.com/Tencent-Hunyuan/HunyuanImage-2.1) |
| HunyuanImage | 模型代际 | [HunyuanImage-3.0](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) | HunyuanImage-3.0 官方仓库，官方定位为面向图像生成的原生多模态模型。 | [official](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) |
| HunyuanVision | 模型代际 | [HunyuanVision](https://github.com/Tencent-Hunyuan/HunyuanVision) | Hunyuan-Vision-1.5 官方仓库：Mamba-Transformer 混合架构的视觉语言模型，官方强调多语言多模态理解与推理。 | [official](https://github.com/Tencent-Hunyuan/HunyuanVision) |
| HunyuanOCR | 模型代际 | [HunyuanOCR](https://github.com/Tencent-Hunyuan/HunyuanOCR) | HunyuanOCR-1.5 官方仓库，官方定位为更快更强的轻量级 OCR 视觉语言模型。 | [official](https://github.com/Tencent-Hunyuan/HunyuanOCR) |
| HunyuanWorld | 模型代际 | [HunyuanWorld-1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) | HunyuanWorld-1.0 官方仓库：从文字或图像生成可沉浸、可探索、可交互的 3D 世界。 | [official](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) |
| HunyuanWorld | 模型代际 | [HunyuanWorld-Voyager](https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager) | Voyager 官方仓库：以相机输入为条件的交互式 RGBD 视频生成模型，支持实时 3D 重建。 | [official](https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager) |
| HunyuanWorld | 模型代际 | [HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) | HY-World 2.0 官方仓库：面向 3D 世界重建、生成与仿真的多模态世界模型。 | [official](https://github.com/Tencent-Hunyuan/HY-World-2.0) |
| HunyuanWorld | 模型代际 | [HY-WorldPlay](https://github.com/Tencent-Hunyuan/HY-WorldPlay) | HY-World 1.5 官方仓库：面向实时延迟与几何一致性的交互式世界建模系统化框架。 | [official](https://github.com/Tencent-Hunyuan/HY-WorldPlay) |
| Hy3 | 模型代际 | [Hy3](https://github.com/Tencent-Hunyuan/Hy3) | Hy3 官方仓库：295B 总参 / 21B 激活的推理与 agent 模型，官方强调同规模下的成本效率。 | [official](https://github.com/Tencent-Hunyuan/Hy3) |
| Hy4 | 模型代际 | [Hy4-preview](https://github.com/Tencent-Hunyuan/Hy4-preview) | Hy4-preview 官方仓库：混元新一代旗舰预览，README 提供 vLLM 与 SGLang 部署路径。 | [official](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| — | 推理系统 | [AngelSlim](https://github.com/Tencent/AngelSlim) | AngelSlim：面向易用性、全面性与效率的模型压缩工具包。 | [official](https://github.com/Tencent/AngelSlim) |
| — | 推理系统 | [AngelSpec](https://github.com/Tencent/AngelSpec) | AngelSpec：面向 MTP 与块并行推测解码的统一、torch 原生训练框架。 | [official](https://github.com/Tencent/AngelSpec) |
| — | 推理系统 | [FlexKV](https://github.com/taco-project/FlexKV) | 分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。 | [official](https://github.com/taco-project/FlexKV) |
| — | 推理系统 | [KsanaLLM](https://github.com/Tencent/KsanaLLM) | KsanaLLM：腾讯高性能、易用的 LLM 推理与服务引擎。 | [official](https://github.com/Tencent/KsanaLLM) |
| — | 推理系统 | [ncnn](https://github.com/Tencent/ncnn) | ncnn：面向移动平台优化的高性能神经网络推理框架。 | [official](https://github.com/Tencent/ncnn) |
| — | 推理系统 | [TNN](https://github.com/Tencent/TNN) | TNN：腾讯优图与光影实验室的跨平台深度学习推理框架，基于 ncnn 与 RapidNet，强调移动端性能与模型压缩。 | [official](https://github.com/Tencent/TNN) |
| — | 推理系统 | [TurboTransformers](https://github.com/Tencent/TurboTransformers) | 按序列长度动态组织 batch，并通过融合 kernel 和内存管理加速 Transformer 在线服务。 | [official](https://github.com/Tencent/TurboTransformers) |
| — | 推理系统 | [WeDLM](https://github.com/Tencent/WeDLM) | WeDLM：采用标准因果注意力、原生兼容 KV cache 的扩散语言模型，官方称相对 vLLM 优化基线有实际加速。 | [official](https://github.com/Tencent/WeDLM) |
| — | Kernel 与编译 | [FlashVDM](https://github.com/Tencent-Hunyuan/FlashVDM) | FlashVDM：释放 Vecset 扩散模型的快速形状生成能力，官方称可在 1 秒内完成。 | [official](https://github.com/Tencent-Hunyuan/FlashVDM) |
| — | Kernel 与编译 | [flex-block-attn](https://github.com/Tencent-Hunyuan/flex-block-attn) | flex-block-attn：腾讯混元开源的高效块稀疏注意力计算库。 | [official](https://github.com/Tencent-Hunyuan/flex-block-attn) |
| — | Kernel 与编译 | [HiLS-Attention](https://github.com/Tencent-Hunyuan/HiLS-Attention) | HiLS-Attention 官方代码：论文《Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling》。 | [official](https://github.com/Tencent-Hunyuan/HiLS-Attention) |
| — | Kernel 与编译 | [hpc-ops](https://github.com/Tencent/hpc-ops) | hpc-ops：腾讯高性能 LLM 推理算子库（High Performance LLM Inference Operator Library）。 | [official](https://github.com/Tencent/hpc-ops) |
| — | Kernel 与编译 | [Simple-Attention-Sparsification](https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification) | SAS 官方代码：通过端到端优化实现简单注意力稀疏化的研究实现。 | [official](https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification) |
| — | 训练与数据 | [llm.hunyuan.T1](https://github.com/Tencent/llm.hunyuan.T1) | 混元 T1 的强化学习后训练工程仓库，README 以 RL 在后训练阶段的新 Scaling 范式开篇。 | [official](https://github.com/Tencent/llm.hunyuan.T1) |
| — | 训练与数据 | [Rosetta-inference](https://github.com/Tencent-Hunyuan/Rosetta-inference) | Rosetta-inference：腾讯混元开源的原生多模态预训练方案，官方强调不出现灾难性遗忘。 | [official](https://github.com/Tencent-Hunyuan/Rosetta-inference) |

## NVIDIA AI 系统专题

NVIDIA 加速器平台、推理运行时、Kernel/编译、互连与生产 Serving 材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Hopper | 加速器与平台 | [Hopper](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/) | Hopper 架构官方页：NVIDIA 数据中心 GPU 架构，引入 Transformer Engine 与 FP8 等面向大模型推理的机制。 | [official](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/) |
| Blackwell | 推理运行时 | [Boost Inference Performance up to 15x on NVIDIA Blackwell Using DFlash Speculative Decoding](https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/) | DFlash 用块扩散（block-diffusion）drafter 在单次前向中并行生成多个候选 token 再并行验证；在 Blackwell Ultra 上对 gpt-oss-120b 实现同等交互性下最高 15 倍吞吐提升，对 Llama 3.1 8B 的交互性接近 EAGLE-3 的两倍，并已集成 SGLang、vLLM 与 TensorRT-LLM。 | [official](https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/) |
| Rubin | 加速器与平台 | [Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/technologies/rubin/) | 将 72 张 Rubin GPU、36 颗 Vera CPU、ConnectX-9 和 BlueField-4 组合为单一 NVLink 域，强调长上下文、低 cost/token 和 rack-scale RAS。 | [official](https://www.nvidia.com/en-us/data-center/technologies/rubin/) |
| — | 加速器与平台 | [BlueField-4 + DOCA in-silicon security for AI factories](https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/) | NVIDIA BlueField DPU 把安全能力做进芯片，独立于主机运行 DOCA 安全栈（Argus、Vault、Flow），运行时威胁检测比纯软件方案快最多 1000 倍，并在最高 800 Gb/s 线速下执行网络与文件访问策略且不占用主机 CPU。 | [official](https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/) |
| — | 加速器与平台 | [BlueField-4 STX / context memory storage](https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai) | 用 DPU/加速存储绕过 host CPU，把长上下文 KV cache 放到近存储路径，面向 agentic AI 的大上下文状态。 | [official](https://www.tomshardware.com/tech-industry/nvidia-launches-bluefield-4-stx-storage-architecture-for-agentic-ai) |
| — | 推理运行时 | [NVFP4 KV cache](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/) | NVFP4 KV cache 量化把显存占用相对 FP8 再压缩最高 50%，等效把上下文预算翻倍；在 LiveCodeBench、MMLU-PRO、MBPP、Ruler 64K 上精度损失低于 1%，decode 阶段缓解显存带宽压力，prefill 阶段 TTFT 最高改善 3 倍。 | [official](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/) |
| — | 推理运行时 | [TensorRT diffusion pipelines](https://developer.nvidia.com/tensorrt) | NVIDIA TensorRT 是面向深度学习推理的编译器与运行时生态（含 TensorRT-LLM、Model Optimizer、TensorRT for RTX/Cloud），通过量化、层与张量融合、kernel 自动调优提供低延迟高吞吐；官方称相对纯 CPU 平台最高加速 36 倍。 | [official](https://developer.nvidia.com/tensorrt) |
| — | 推理运行时 | [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 提供 inflight batching、paged KV、FP8/FP4、speculative decoding、TP/PP/EP 和多节点执行，是 NVIDIA 平台的产品级 LLM 引擎。 | [official](https://github.com/NVIDIA/TensorRT-LLM) |
| — | 推理运行时 | [TensorRT-LLM FP8/INT8 KV cache](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html) | MHA/MQA kernel 中支持 on-the-fly dequantize 的 FP8/INT8 KV cache，降低 decode 阶段读带宽。 | [official](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html) |
| — | 推理运行时 | [TensorRT-LLM KV cache reuse](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) | TensorRT-LLM 引入基于优先级的 KV cache 驱逐机制，可按 token 区间与 decode block 指定保留优先级与时长，并通过 Executor API 与 KV cache 事件 API 支撑跨实例的 KV-aware 路由；内部基准中缓存命中率提升约 20%。 | [official](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) |
| — | 推理运行时 | [TensorRT-LLM Speculative Decoding](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html) | 在产品级 runtime 中集成 draft-target、Medusa、EAGLE 等推测策略，并与 inflight batching、量化和并行执行组合。 | [official](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html) |
| — | Kernel 与编译 | [Co-Designing AI Model Attention for Fast, Interactive Long-Context Inference](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/) | NVIDIA 系统刻画了 GPU 上 dense attention 的性能边界：prefill 受算力约束、decode 受显存带宽约束；增大 group size（如 GQA/MQA）可提升 decode 吞吐而几乎不影响 prefill，head dim 取 128 或 256 才能与 GPU tile 尺寸和 128 字节访存对齐。 | [official](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/) |
| — | Kernel 与编译 | [CUTLASS / CuTe DSL](https://github.com/NVIDIA/cutlass) | 提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives；4.4/4.5 系列继续补充 Blackwell GQA decode、int4 KV、MX/NVFP4 block-scaled GEMM 和 MoE grouped GEMM 示例。 | [official](https://github.com/NVIDIA/cutlass) |
| — | Kernel 与编译 | [FlashInfer kernel ecosystem](https://github.com/flashinfer-ai/flashinfer) | 针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。 | [official](https://github.com/flashinfer-ai/flashinfer) |
| — | Kernel 与编译 | [FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) | 从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。 | [official](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) |
| — | Kernel 与编译 | [KVTC](https://arxiv.org/abs/2511.01815) | 把 KV cache 看成可压缩信号，用 transform coding、PCA 去相关、自适应量化和熵编码降低可复用 KV 存储。 | [official](https://arxiv.org/abs/2511.01815) |
| — | Kernel 与编译 | [RocketKV](https://arxiv.org/abs/2502.14051) | 两阶段 KV 压缩：先永久淘汰部分 prompt token，再做动态 top-k sparse attention。 | [official](https://arxiv.org/abs/2502.14051) |
| — | Kernel 与编译 | [ThinKV](https://openreview.net/forum?id=M3CeHnZKNC) | thought-adaptive KV cache compression，根据推理过程中的 thought 类型做保留、量化和逐级淘汰。 | [official](https://openreview.net/forum?id=M3CeHnZKNC) |
| — | 通信与互连 | [NCCL](https://github.com/NVIDIA/nccl) | 提供 all-reduce、all-to-all、broadcast 等 GPU collective，是 TP、PP、EP 和 MoE 推理的默认通信层。 | [official](https://github.com/NVIDIA/nccl) |
| — | 通信与互连 | [NIXL / Inference Transfer Library](https://developer.nvidia.com/blog/?p=113426) | NIXL 是开源的厂商无关数据搬运库，为 GPU 显存、CPU 内存与存储层之间的传输提供统一 API，后端覆盖 RDMA、GPU-initiated networking、GPU-Direct storage、NVMe 与 S3／Azure Blob；核心场景是 P/D 分离的 KV 传输、长上下文 KV 落盘与权重快速换入。 | [official](https://developer.nvidia.com/blog/?p=113426) |
| — | 通信与互连 | [NIXL / KV cache transfer](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html) | 面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。 | [official](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html) |
| — | 通信与互连 | [UCX](https://github.com/openucx/ucx) | 统一 InfiniBand、RoCE、shared memory、CUDA memory 等传输，为 MPI、NCCL 和分布式 runtime 提供底层能力。 | [official](https://github.com/openucx/ucx) |
| — | 服务与部署 | [Dynamo](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) | NVIDIA Dynamo 是开源的分布式推理服务框架，用 Planner、Smart Router 与分布式 KV Cache Manager 编排 prefill/decode 分离；官方在 GB200 NVL72 上跑 DeepSeek-R1 时请求处理量最高提升 30 倍。 | [official](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/) |
| — | 服务与部署 | [Dynamo 1.0 Production-Scale Multi-Node Inference](https://developer.nvidia.com/blog/?p=113961) | Dynamo 1.0 面向生产规模的多节点推理，支持 SGLang、TensorRT-LLM、vLLM 三种后端；官方在 SemiAnalysis InferenceX 基准上于 Blackwell 实现最多 7 倍的请求处理量提升，并已被多家云厂商集成进托管 Kubernetes 环境。 | [official](https://developer.nvidia.com/blog/?p=113961) |
| — | 服务与部署 | [Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm) | KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。 | [official](https://docs.dynamo.nvidia.com/dynamo/components/kvbm) |
| — | 服务与部署 | [Dynamo Snapshot](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/) | Dynamo Snapshot 为 Kubernetes 上的推理负载引入 checkpoint/restore：用 CRIU 保存主机状态、cuda-checkpoint 保存 GPU 状态，由特权 DaemonSet 写入共享存储并在同节点或异节点恢复，把冷启动从分钟级压到接近光速；配合 CUDA VMM 解除映射可缩小 checkpoint 体积。 | [official](https://developer.nvidia.com/blog/nvidia-dynamo-snapshot-fast-startup-for-inference-workloads-on-kubernetes/) |
| — | 服务与部署 | [FasterTransformer](https://github.com/NVIDIA/FasterTransformer) | 用融合 CUDA kernel、GEMM 调优、量化和多 GPU 并行提供早期生产级 Transformer 推理库，后续能力并入 TensorRT-LLM。 | [official](https://github.com/NVIDIA/FasterTransformer) |
| — | 服务与部署 | [Full-Stack Optimizations for Agentic Inference with Dynamo](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/) | Dynamo 为 agentic 推理增加统一的基础设施层，通过 nvext API 让 Claude Code、Codex 等 harness 传递优先级、预期输出长度与 speculative prefill 意图；KV-aware 路由用全局 Flash Indexer 把请求放到缓存重叠度最高的 worker，并以 GPU、CPU、本地 NVMe、远端存储四层内存层级让高价值 KV 块全局可用。 | [official](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/) |
| — | 服务与部署 | [How to Size GPUs for AI Inference and TCO Without Overspending](https://developer.nvidia.com/blog/how-to-size-gpus-for-ai-inference-and-tco-without-overspending/) | NVIDIA 给出 GPU 选型与 TCO 的量化方法：先把推理负载归入聊天／助手、Agent、内容生成、翻译四类并刻画各自 token 模式，再按模型、DAU、并发、输入输出长度、缓存命中率与延迟目标推算显存与算力需求，并用「核心 + 弹性」容量模型平衡稳态与突发。 | [official](https://developer.nvidia.com/blog/how-to-size-gpus-for-ai-inference-and-tco-without-overspending/) |
| — | 服务与部署 | [QServe / OmniServe](https://github.com/mit-han-lab/omniserve) | 将 4-bit 权重、8-bit 激活和 4-bit KV 与 SmoothAttention、重排及定制 kernel 联合设计。 | [official](https://github.com/mit-han-lab/omniserve) |
| — | 服务与部署 | [Restore LLM Inference Capacity in Seconds with Shadow Engine Recovery in NVIDIA Dynamo](https://developer.nvidia.com/blog/restore-llm-inference-capacity-in-seconds-with-shadow-engine-recovery-in-nvidia-dynamo/) | Dynamo 的 Shadow Engine Recovery 在同一批 GPU 上常驻一个已初始化的影子引擎，由 GPU Memory Service 在引擎间共享权重而不额外占用 HBM；在 B200 上双 worker 的 GLM-5.2 部署中恢复服务耗时 7.3 秒，相比冷重启的 283 秒快约 39 倍。 | [official](https://developer.nvidia.com/blog/restore-llm-inference-capacity-in-seconds-with-shadow-engine-recovery-in-nvidia-dynamo/) |
| — | 服务与部署 | [TensorRT Edge-LLM Completes the MLPerf Edge Agentic Benchmark 6.4x Faster on Jetson AGX Thor](https://developer.nvidia.com/blog/tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor/) | TensorRT Edge-LLM 在单台 Jetson AGX Thor 上用 Qwen3.6-27B 完成 MLPerf Inference v6.1 Edge Agentic 基准：52.33 tokens/s，1007 轮性能负载 24 分 36 秒跑完，比 llama.cpp 参考实现的 2 小时 37 分快 6.4 倍；靠 NVFP4 权重量化、FP8 KV cache、树式多 token 预测与跨轮 KV 复用，其中 KV／递归状态复用贡献约 96%。 | [official](https://developer.nvidia.com/blog/tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor/) |
| — | 服务与部署 | [Triton Inference Server](https://github.com/triton-inference-server/server) | 负责模型仓库、dynamic batching、ensemble、metrics 和多框架后端，常作为 TensorRT-LLM/vLLM 外层生产服务面。 | [official](https://github.com/triton-inference-server/server) |
| — | 服务与部署 | [When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/) | Dynamo 实现 encode-prefill-decode（EPD）三级解耦，把视觉编码从 LLM 的 prefill／decode 中拆出；对图像密集、输出中短与量化 MoE 模型，TTFT 最高快 5 倍、端到端响应时间最高快 7 倍。编码器可聚合部署、与 P/D worker 共卡，或放到更低成本的独立 GPU 层经 NIXL 连接。 | [official](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/) |
| — | 生态与工具 | [Benchmarking LLM Inference at Scale with AIPerf](https://developer.nvidia.com/blog/benchmarking-llm-inference-at-scale-with-aiperf/) | AIPerf 取代 GenAI-Perf，用多进程架构避免客户端在高并发压测中成为瓶颈；支持 15 种以上端点类型与 ShareGPT、Mooncake／Baseten／WEKA AgentX 的 trace 回放，可配置 constant／Poisson／gamma 到达分布，输出 TTFT、ITL、请求延迟与输出吞吐的分位数。 | [official](https://developer.nvidia.com/blog/benchmarking-llm-inference-at-scale-with-aiperf/) |
| — | 生态与工具 | [cuVS / CAGRA](https://github.com/rapidsai/cuvs) | 提供 GPU graph ANN、IVF、brute-force 和多节点能力，并被向量数据库用于 GPU 加速。 | [official](https://github.com/rapidsai/cuvs) |
| — | 生态与工具 | [Megatron-LM / Megatron-Core](https://github.com/NVIDIA/Megatron-LM) | 建立 tensor parallel 等核心拆分，并发展为支持 TP、PP、CP、EP 的大模型训练推理核心库。 | [official](https://github.com/NVIDIA/Megatron-LM) |

## AMD / ROCm AI 系统专题

AMD Instinct 平台与 ROCm 软件栈上的推理运行时、算子库、通信与 Serving 材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| MI300X | 加速器与平台 | [MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300.html) | AMD Instinct MI300X 官方产品页：CDNA 3 架构，192 GB HBM3 与 5.3 TB/s 峰值带宽，面向生成式 AI 与 HPC。 | [official](https://www.amd.com/en/products/accelerators/instinct/mi300.html) |
| MI325X | 加速器与平台 | [MI325X architecture-aware deployment study](https://arxiv.org/abs/2603.10031) | 说明 MLA、GQA、MoE 和视觉模型需要不同的 AITER、KV offload 与 block-size 配置，不能沿用统一参数。 | [official](https://arxiv.org/abs/2603.10031) |
| MI350X | 加速器与平台 | [Instinct MI350 Series](https://www.amd.com/en/products/accelerators/instinct/mi350.html) | CDNA 4 引入 FP4/FP6 并提供 288 GB HBM3E，面向大模型、MoE 和长上下文的高容量推理。 | [official](https://www.amd.com/en/products/accelerators/instinct/mi350.html) |
| MI350X | 推理运行时 | [Efficiently Serving NVFP4 Models on AMD Instinct™ MI350X/MI355X Accelerators via Online NVFP4 to Quark MXFP4 Requantization](https://rocm.blogs.amd.com/software-tools-optimization/nvfp4-to-mxfp4/README.html) | SGLang 中的在线 NVFP4→MXFP4 重量化管线在权重加载时一次性把 NVFP4 参数转为 MXFP4，使 NVFP4 模型能跑在 MI350X/MI355X 的原生 MXFP4 路径上，无需离线预处理，精度与原生 NVFP4 持平、吞吐与原生 MXFP4 相当。 | [official](https://rocm.blogs.amd.com/software-tools-optimization/nvfp4-to-mxfp4/README.html) |
| MI355X | 推理运行时 | [4-bit KV Caching in LMCache: Offloading Quantized KV Beyond HBM for Context-Heavy Agents on AMD MI355X](https://rocm.blogs.amd.com/software-tools-optimization/4bit-KV-LMcache/README.html) | LMCache 在 AMD MI355X 上将 TurboQuant 4-bit KV 量化与分层缓存结合，用布局感知连接器把量化 KV 越过 HBM 边界卸载到 CPU DRAM 再取回，做到位精确、精度无损，使上下文密集智能体在量化与分层叠加时仍能兼顾 goodput、latency 与 accuracy。 | [official](https://rocm.blogs.amd.com/software-tools-optimization/4bit-KV-LMcache/README.html) |
| MI355X | 推理运行时 | [DFlash Speculative Decoding on AMD Instinct MI355X: Up to 5× Faster Qwen3.5 Inference](https://rocm.blogs.amd.com/artificial-intelligence/dflash-on-MI355x/README.html) | 在 AMD MI355X 上经 vLLM/ROCm 部署 DFlash 这一 block-diffusion drafter，对标 Qwen3.5 内置 MTP drafter，并通过 mxfp4 量化目标模型证明其可与 speculation 叠加，使 Qwen3.5 推理最高加速 5×。 | [official](https://rocm.blogs.amd.com/artificial-intelligence/dflash-on-MI355x/README.html) |
| MI355X | 服务与部署 | [Serving 64Mi-Token Contexts on One AMD Instinct™ MI355X Node](https://rocm.blogs.amd.com/artificial-intelligence/long-context-serving/README.html) | 在单台 8-GPU MI355X 节点上用 vLLM（FP8 KV cache、TP=8）服务 Kimi Linear 48B-A3B，覆盖 1024 到 64Mi token 共六个数量级的上下文，以 FP8 KV 存储让最长上下文也能落在单节点内，并报告各长度的 TTFT 与 decode throughput。 | [official](https://rocm.blogs.amd.com/artificial-intelligence/long-context-serving/README.html) |
| MI455X | 加速器与平台 | [Helios / Instinct MI455X rack-scale platform](https://www.tomshardware.com/tech-industry/semiconductors/hpe-adopts-amd-helios-rack-architecture-for-2026-ai-systems) | 以 72 GPU、HBM4、EPYC 和 Ethernet scale-up fabric 构建开放机架方案，代表非 NVLink 的 rack-scale AI 路线。 | [official](https://www.tomshardware.com/tech-industry/semiconductors/hpe-adopts-amd-helios-rack-architecture-for-2026-ai-systems) |
| — | 加速器与平台 | [hip](https://github.com/ROCm/hip) | HIP：C++ 异构计算可移植接口，把 CUDA 代码迁移到 ROCm。 | [official](https://github.com/ROCm/hip) |
| — | 推理运行时 | [ATOM inference engine](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html) | 以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。 | [official](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html) |
| — | 推理运行时 | [Efficient MiniMax-M3 Inference on AMD Instinct GPUs with ATOM and ATOMesh](https://rocm.blogs.amd.com/artificial-intelligence/minmax-m3-atomesh/README.html) | ATOM 与 ATOMesh 在 AMD Instinct GPU 上高效服务 MiniMax-M3——这一 428B 总参/22B 激活的多模态 MoE，其 MiniMax Sparse Attention 以块级 KV cache 选择替代平方注意力、将每 token 计算降至前代的 1/20——兼顾单机优化与多机编排。 | [official](https://rocm.blogs.amd.com/artificial-intelligence/minmax-m3-atomesh/README.html) |
| — | 推理运行时 | [Hyperloom - Autonomous Agentic Inference Optimization for AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/hyperloom/README.html) | ROCm Hyperloom 是开源的自治式智能体系统，用自主优化循环自动完成端到端推理调优，将优化耗时从数周压缩到数小时，在 AMD Instinct GPU 上榨取模型与配置的峰值性能。 | [official](https://rocm.blogs.amd.com/software-tools-optimization/hyperloom/README.html) |
| — | 推理运行时 | [rocm-systems](https://github.com/ROCm/rocm-systems) | ROCm 系统层项目的 super repo（运行时、编译器、RCCL 等）。 | [official](https://github.com/ROCm/rocm-systems) |
| — | 推理运行时 | [TheRock](https://github.com/ROCm/TheRock) | TheRock：轻量、开源的 ROCm 构建与打包工具链。 | [official](https://github.com/ROCm/TheRock) |
| — | Kernel 与编译 | [AITER: AI Tensor Engine for ROCm](https://github.com/ROCm/aiter) | AMD AITER 为 ROCm 推理提供 C++/Python API 与优化的 Triton、Composable Kernel 及汇编算子（覆盖 attention、MoE、GEMM、quantization、通信 kernel），并直接接入 vLLM 与 SGLang。 | [official](https://github.com/ROCm/aiter) |
| — | Kernel 与编译 | [AMDMIGraphX](https://github.com/ROCm/AMDMIGraphX) | MIGraphX：AMD 的图优化与推理引擎。 | [official](https://github.com/ROCm/AMDMIGraphX) |
| — | Kernel 与编译 | [FlyDSL](https://github.com/ROCm/FlyDSL) | FlyDSL：灵活布局（Flexible Layout）DSL 的 Python 前端。 | [official](https://github.com/ROCm/FlyDSL) |
| — | Kernel 与编译 | [Productionizing TurboQuant on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html) | 在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。 | [official](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html) |
| — | Kernel 与编译 | [rocm-libraries](https://github.com/ROCm/rocm-libraries) | ROCm 数学与算子库的 super repo（rocBLAS、Tensile、MIOpen 等）。 | [official](https://github.com/ROCm/rocm-libraries) |
| — | 服务与部署 | [ATOMesh distributed serving gateway](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html) | 作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。 | [official](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html) |
| — | 服务与部署 | [FastFlowLM](https://github.com/ROCm/FastFlowLM) | FastFlowLM：在 AMD Ryzen AI NPU 上运行 LLM 的推理引擎。 | [official](https://github.com/ROCm/FastFlowLM) |
| — | 服务与部署 | [Introducing AMD ROCm™ Infera: Scaling Goodput for Agentic AI with Distributed Inference Orchestration](https://rocm.blogs.amd.com/software-tools-optimization/infera-di/README.html) | ROCm Infera 是面向大规模部署的分布式推理编排参考方案，作为「GPU 乐团指挥」协调多实例，内部测试显示真实智能体负载下每 GPU 的 goodput 最高提升 2.6×，并原生集成 vLLM、SGLang 与 ATOM。 | [official](https://rocm.blogs.amd.com/software-tools-optimization/infera-di/README.html) |
| — | 生态与工具 | [ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/) | 通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。 | [official](https://rocm.docs.amd.com/) |

## OpenAI 系统专题

OpenAI 开放权重模型、推理与 Kernel/编译生态、Agent 工具链材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| GPT-2 | 模型代际 | [gpt-2](https://github.com/openai/gpt-2) | GPT-2：论文《Language Models are Unsupervised Multitask Learners》的官方代码与模型。 | [official](https://github.com/openai/gpt-2) |
| GPT-3 | 模型代际 | [gpt-3](https://github.com/openai/gpt-3) | GPT-3：论文《Language Models are Few-Shot Learners》官方仓库。 | [official](https://github.com/openai/gpt-3) |
| CLIP | 模型代际 | [CLIP](https://github.com/openai/CLIP) | CLIP：对比式语言-图像预训练模型，支持零样本图像分类。 | [official](https://github.com/openai/CLIP) |
| DALL-E | 模型代际 | [DALL-E](https://github.com/openai/DALL-E) | DALL·E 所用离散 VAE 的 PyTorch 实现。 | [official](https://github.com/openai/DALL-E) |
| Whisper | 模型代际 | [whisper](https://github.com/openai/whisper) | Whisper：通过大规模弱监督实现的鲁棒语音识别模型。 | [official](https://github.com/openai/whisper) |
| gpt-oss | 模型代际 | [gpt-oss](https://github.com/openai/gpt-oss) | gpt-oss-120b / gpt-oss-20b：两个开放权重的语言模型。 | [official](https://github.com/openai/gpt-oss) |
| Codex | 工具与生态 | [codex](https://github.com/openai/codex) | OpenAI Codex：运行在终端里的轻量编码 agent。 | [official](https://github.com/openai/codex) |
| — | Kernel 与编译 | [Triton language and kernels in inference stacks](https://triton-lang.org/) | 工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。 | [official](https://triton-lang.org/) |
| — | 工具与生态 | [evals](https://github.com/openai/evals) | Evals：面向 LLM 与 LLM 系统的评测框架与开源基准注册表。 | [official](https://github.com/openai/evals) |
| — | 工具与生态 | [openai-agents-python](https://github.com/openai/openai-agents-python) | 轻量、强大的多 agent 工作流框架（官方 Python 实现）。 | [official](https://github.com/openai/openai-agents-python) |
| — | 工具与生态 | [openai-python](https://github.com/openai/openai-python) | OpenAI API 的官方 Python 库。 | [official](https://github.com/openai/openai-python) |
| — | 工具与生态 | [swarm](https://github.com/openai/swarm) | Swarm：探索符合工效学的轻量多 agent 编排的教学框架。 | [official](https://github.com/openai/swarm) |
| — | 工具与生态 | [tiktoken](https://github.com/openai/tiktoken) | tiktoken：用于 OpenAI 模型的快速 BPE 分词器。 | [official](https://github.com/openai/tiktoken) |

## Anthropic 系统专题

Anthropic Claude 的 Agent 运行时、沙箱隔离、工具链与训练数据材料；官方未开源推理栈，本专题只收可核验的官方材料。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Claude 3 | 模型代际 | [Claude 3](https://www.anthropic.com/news/claude-3-family) | Claude 3 模型家族官方发布：按能力升序为 Haiku、Sonnet、Opus 三档，官方称在多项认知任务上刷新业界基准。 | [official](https://www.anthropic.com/news/claude-3-family) |
| Claude 3.5 | 模型代际 | [Claude 3.5](https://www.anthropic.com/news/claude-3-5-sonnet) | Claude 3.5 Sonnet 官方发布：官方称其为当时最强模型，关键评测超过 Claude 3 Opus 且速度翻倍。 | [official](https://www.anthropic.com/news/claude-3-5-sonnet) |
| Claude 3.7 | 工具与生态 | [claude-code](https://github.com/anthropics/claude-code) | Claude Code：运行在终端里的 agentic 编码工具（官方仓库）。 | [official](https://github.com/anthropics/claude-code) |
| Claude 4 | 模型代际 | [Claude 4](https://www.anthropic.com/news/claude-4) | Claude 4 官方发布：面向复杂任务提供更强的推理能力与更可靠、可解释的辅助。 | [official](https://www.anthropic.com/news/claude-4) |
| Claude 4.5 | 模型代际 | [Claude Opus 4.5](https://www.anthropic.com/news/claude-opus-4-5) | Claude Opus 4.5 官方发布：Anthropic 新旗舰，官方称在领先的编码与 agent 能力下价格更低。 | [official](https://www.anthropic.com/news/claude-opus-4-5) |
| — | 推理系统 | [claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | Claude Agent SDK 的官方 Python 实现。 | [official](https://github.com/anthropics/claude-agent-sdk-python) |
| — | 推理系统 | [sandbox-runtime](https://github.com/anthropics/sandbox-runtime) | sandbox-runtime：用于强制文件系统与网络隔离的轻量沙箱工具。 | [official](https://github.com/anthropics/sandbox-runtime) |
| — | 训练与数据 | [hh-rlhf](https://github.com/anthropics/hh-rlhf) | 论文《Training a Helpful and Harmless Assistant》的人类偏好数据。 | [official](https://github.com/anthropics/hh-rlhf) |
| — | 工具与生态 | [anthropic-sdk-go](https://github.com/anthropics/anthropic-sdk-go) | Anthropic API 的官方 Go SDK。 | [official](https://github.com/anthropics/anthropic-sdk-go) |
| — | 工具与生态 | [anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) | Anthropic API 的官方 Python SDK。 | [official](https://github.com/anthropics/anthropic-sdk-python) |
| — | 工具与生态 | [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript) | Anthropic API 的官方 TypeScript SDK。 | [official](https://github.com/anthropics/anthropic-sdk-typescript) |
| — | 工具与生态 | [claude-code-action](https://github.com/anthropics/claude-code-action) | 把 Claude Code 集成进 GitHub 工作流的官方 Action。 | [official](https://github.com/anthropics/claude-code-action) |
| — | 工具与生态 | [claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 基于 Claude 的 AI 代码安全审查 GitHub Action。 | [official](https://github.com/anthropics/claude-code-security-review) |
| — | 工具与生态 | [claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Claude 官方 cookbook：notebook 与配方集合。 | [official](https://github.com/anthropics/claude-cookbooks) |
| — | 工具与生态 | [claude-quickstarts](https://github.com/anthropics/claude-quickstarts) | 帮助开发者快速上手 Claude 的项目合集。 | [official](https://github.com/anthropics/claude-quickstarts) |
| — | 工具与生态 | [skills](https://github.com/anthropics/skills) | Agent Skills 官方公共仓库。 | [official](https://github.com/anthropics/skills) |

## Google / DeepMind 系统专题

Google TPU 平台、推理运行时与 Kernel、Gemma 模型代际及检索/端侧工具材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Gemma 2 | 模型代际 | [Gemma 2](https://arxiv.org/abs/2408.00118) | Gemma 2 官方技术报告：在实用规模上改进开源语言模型的 Gemma 第二代。 | [official](https://arxiv.org/abs/2408.00118) |
| Gemma 3 | 模型代际 | [Gemma 3](https://deepmind.google/models/gemma/gemma-3/) | Gemma 3 官方模型页：具备多模态理解与多语言支持的轻量 Gemma，官方称可在单个 GPU 或 TPU 上运行。 | [official](https://deepmind.google/models/gemma/gemma-3/) |
| Gemma 4 | 模型代际 | [Gemma 4 on vLLM-TPU](https://arxiv.org/abs/2605.25645) | 展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。 | [official](https://arxiv.org/abs/2605.25645) |
| Gemini 2 | 模型代际 | [Gemini 2.5](https://arxiv.org/abs/2507.06261) | Gemini 2.5 官方技术报告：Gemini 2 代的前沿模型，覆盖高级推理、多模态、长上下文与下一代 agent 能力。 | [official](https://arxiv.org/abs/2507.06261) |
| Gemini 3 | 模型代际 | [Gemini 3](https://deepmind.google/models/gemini/pro/) | Gemini 3 官方模型页：Google DeepMind 第三代 Gemini（Pro 系列），官方定位复杂任务与创意实现。 | [official](https://deepmind.google/models/gemini/pro/) |
| — | 加速器与平台 | [Ironwood TPU](https://cloud.google.com/tpu) | 第七代 TPU 明确以推理为中心，结合大规模 pod、HBM 和 Google 软件栈服务长上下文与 reasoning workload。 | [official](https://cloud.google.com/tpu) |
| — | 加速器与平台 | [TPU 8i / TPU 8t](https://www.itpro.com/infrastructure/google-cloud-eighth-generation-tpu-8t-8i-ai-inference-training) | 第八代首次将 inference 优化的 8i 与 training 优化的 8t 分开，8i 强调片上 SRAM、内存带宽和低延迟互连；尚待正式交付验证。 | [official](https://www.itpro.com/infrastructure/google-cloud-eighth-generation-tpu-8t-8i-ai-inference-training) |
| — | 模型代际 | [gemma](https://github.com/google-deepmind/gemma) | Gemma 开放权重 LLM 的官方库（Google DeepMind）。 | [official](https://github.com/google-deepmind/gemma) |
| — | 推理系统 | [JetStream + MaxText](https://cloud.google.com/tpu/docs/tutorials/LLM/jetstream-maxtext-inference-v6e) | 面向 XLA/TPU 的 throughput 和 memory optimized LLM inference engine，配合 MaxText 在 TPU/GKE 上服务 LLM。 | [official](https://cloud.google.com/tpu/docs/tutorials/LLM/jetstream-maxtext-inference-v6e) |
| — | 推理系统 | [JetStream / MaxText / Pathways on TPU](https://github.com/AI-Hypercomputer/JetStream) | 用 JAX/XLA、paged attention、模型并行和 TPU pod serving 构成 Gemini 与开源模型的 TPU 推理路径。 | [official](https://github.com/AI-Hypercomputer/JetStream) |
| — | 推理系统 | [LiteRT](https://ai.google.dev/edge/litert) | 在 TensorFlow Lite 演进基础上统一 CPU/GPU/NPU delegate 和生成式模型部署，服务 Android 与边缘设备。 | [official](https://ai.google.dev/edge/litert) |
| — | 推理系统 | [TurboQuant](https://arxiv.org/abs/2504.19874) | 通过随机旋转、近最优量化和 QJL 残差校正，面向 KV cache 和向量检索做低比特在线向量量化。 | [official](https://arxiv.org/abs/2504.19874) |
| — | Kernel 与编译 | [Perfect Recall, Parallel Efficiency: MLA for Million-Token Decoding](https://www.microsoft.com/en-us/research/publication/perfect-recall-parallel-efficiency-multi-head-latent-attention-for-million-token-context-decoding/) | 分析 DSA/MLA 在百万 token 分布式 decoding 中的全局 Top-K 同步瓶颈，并探索并行高效的精确召回路线。 | [official](https://www.microsoft.com/en-us/research/publication/perfect-recall-parallel-efficiency-multi-head-latent-attention-for-million-token-context-decoding/) |
| — | Kernel 与编译 | [Ragged Paged Attention for TPU](https://arxiv.org/abs/2604.15464) | 面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。 | [official](https://arxiv.org/abs/2604.15464) |
| — | 工具与生态 | [ScaNN](https://github.com/google-research/google-research/tree/master/scann) | 用 anisotropic vector quantization、partitioning 和 reordering 提供高召回低延迟检索。 | [official](https://github.com/google-research/google-research/tree/master/scann) |

## Meta 系统专题

Meta Llama 模型代际与其注意力 Kernel、并行策略、通信库与端侧运行时材料；专题仅作聚合导航。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| Llama-2 | 模型代际 | [llama](https://github.com/meta-llama/llama) | Llama 模型的官方推理代码。 | [official](https://github.com/meta-llama/llama) |
| CodeLlama | 模型代际 | [codellama](https://github.com/meta-llama/codellama) | CodeLlama 模型的官方推理代码。 | [official](https://github.com/meta-llama/codellama) |
| Llama-3 | 模型代际 | [llama-models](https://github.com/meta-llama/llama-models) | 配合 Llama 模型使用的官方工具集。 | [official](https://github.com/meta-llama/llama-models) |
| Llama-3 | 模型代际 | [llama3](https://github.com/meta-llama/llama3) | Meta Llama 3 官方 GitHub 站点。 | [official](https://github.com/meta-llama/llama3) |
| — | 推理系统 | [Context Parallelism for Million-Token Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) | 用 pass-KV/pass-Q 精确 ring attention 在常见数据中心网络上扩展百万 token prefill。 | [official](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html) |
| — | 推理系统 | [ExecuTorch](https://pytorch.org/executorch/) | 将模型导出到轻量 runtime，并通过 Core ML、QNN、XNNPACK、Vulkan 等 backend 在手机和嵌入式设备执行。 | [official](https://pytorch.org/executorch/) |
| — | 推理系统 | [llama.cpp](https://github.com/ggml-org/llama.cpp) | 用 GGUF、低比特量化和多种 CPU/GPU/NPU backend 把本地 LLM 推理扩展到 PC、服务器、手机和嵌入式设备。 | [official](https://github.com/ggml-org/llama.cpp) |
| — | 推理系统 | [Scaling LLM inference: TP/CP/EP](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/) | 公开 Meta 在 tensor/context/expert parallelism 上扩展 LLM inference 的工程经验。 | [official](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/) |
| — | Kernel 与编译 | [FlexAttention](https://pytorch.org/blog/flexattention/) | 允许用户用 score modification 和 block mask 表达 attention variant，再由编译器生成 fused kernel，覆盖 sparse/paged inference。 | [official](https://pytorch.org/blog/flexattention/) |
| — | Kernel 与编译 | [FlexAttention for inference](https://pytorch.org/blog/flexattention-for-inference/) | 用 PyTorch API 表达 attention variants，经 torch.compile 降到 fused attention kernel，支持 inference/paged attention 方向。 | [official](https://pytorch.org/blog/flexattention-for-inference/) |
| — | 通信与互连 | [Gloo](https://github.com/facebookincubator/gloo) | 为 PyTorch distributed 提供跨 TCP、IB 等传输的 collective backend，是控制面和非 NCCL 路径的基础组件。 | [official](https://github.com/facebookincubator/gloo) |
| — | 训练与数据 | [synthetic-data-kit](https://github.com/meta-llama/synthetic-data-kit) | 生成高质量合成数据集的官方工具。 | [official](https://github.com/meta-llama/synthetic-data-kit) |
| — | 工具与生态 | [Faiss](https://github.com/facebookresearch/faiss) | 提供 IVF、PQ、HNSW、GPU k-selection 等索引，是自建 RAG 和向量检索 benchmark 的基础库。 | [official](https://github.com/facebookresearch/faiss) |
| — | 工具与生态 | [prompt-ops](https://github.com/meta-llama/prompt-ops) | prompt-ops：开源的 LLM prompt 优化工具。 | [official](https://github.com/meta-llama/prompt-ops) |
| — | 工具与生态 | [PurpleLlama](https://github.com/meta-llama/PurpleLlama) | PurpleLlama：评估与提升 LLM 安全性的官方工具集。 | [official](https://github.com/meta-llama/PurpleLlama) |

## vLLM 社区专题

vLLM 开源推理引擎与其插件、Connector、跨硬件后端生态；只收社区与厂商的官方工程材料，不收版本流水。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| — | 核心引擎 | [afd-plugin](https://github.com/vllm-project/afd-plugin) | vLLM 的 attention-FFN 解耦（AFD）支持插件。 | [official](https://github.com/vllm-project/afd-plugin) |
| — | 核心引擎 | [humming](https://github.com/vllm-project/humming) | Humming：高性能、轻量且高度灵活的推理组件（官方仓库）。 | [official](https://github.com/vllm-project/humming) |
| — | 核心引擎 | [vLLM V1](https://github.com/vllm-project/vllm) | 以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。 | [official](https://github.com/vllm-project/vllm) |
| — | 核心引擎 | [vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/) | vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。 | [official](https://pytorch.org/projects/vllm/) |
| — | 核心引擎 | [vllm-ascend](https://github.com/vllm-project/vllm-ascend) | vLLM 在昇腾 NPU 上的官方硬件后端插件。 | [official](https://github.com/vllm-project/vllm-ascend) |
| — | 核心引擎 | [vLLM-Omni](https://arxiv.org/abs/2602.02204) | 用 stage graph 拆分 LLM、扩散模型和编码器，各阶段独立批处理、分配 GPU，并通过统一 connector 传递中间状态。 | [official](https://arxiv.org/abs/2602.02204) |
| — | 核心引擎 | [vLLM-Omni runtime](https://github.com/vllm-project/vllm-omni) | 将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。 | [official](https://github.com/vllm-project/vllm-omni) |
| — | KV 与缓存 | [Ascend-vLLM prefix caching / KV offload](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html) | 在 Ascend NPU 上支持 prefix caching、KV cache CPU offload 和 Mooncake/LMCache 连接。 | [official](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html) |
| — | KV 与缓存 | [KV Offloading Connector](https://vllm.ai/blog/kv-offloading-connector) | vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。 | [official](https://vllm.ai/blog/kv-offloading-connector) |
| — | KV 与缓存 | [PegaFlow External KV Cache](https://vllm.ai/blog/2026-05-18-pegaflow) | PegaFlow 作为 Rust standalone external KV cache service 通过 vLLM connector 接入，面向生产级外部 KV cache。 | [official](https://vllm.ai/blog/2026-05-18-pegaflow) |
| — | KV 与缓存 | [vLLM x Mooncake Store](https://vllm.ai/blog/2026-05-06-mooncake-store) | 将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。 | [official](https://vllm.ai/blog/2026-05-06-mooncake-store) |
| — | Kernel 与编译 | [tml-fa4](https://github.com/vllm-project/tml-fa4) | 基于 FA4 的相对注意力 kernel（TML 与 Colfax 合作）。 | [official](https://github.com/vllm-project/tml-fa4) |
| — | 生态与工具 | [agentic-api](https://github.com/vllm-project/agentic-api) | 基于 vLLM 的 agentic 应用有状态 API 逻辑。 | [official](https://github.com/vllm-project/agentic-api) |
| — | 生态与工具 | [dllm-plugin](https://github.com/vllm-project/dllm-plugin) | vLLM 的块式扩散语言模型（dLLM）支持插件。 | [official](https://github.com/vllm-project/dllm-plugin) |
| — | 生态与工具 | [MLX-LM / vllm-mlx](https://github.com/ml-explore/mlx-lm) | 利用 Apple silicon 统一内存和 MLX 图执行提供本地 LLM 推理，并开始向 continuous batching 和 vLLM API 兼容扩展。 | [official](https://github.com/ml-explore/mlx-lm) |
| — | 生态与工具 | [vime](https://github.com/vllm-project/vime) | vime：基于 vLLM 做 RL 扩展的 LLM 后训练框架。 | [official](https://github.com/vllm-project/vime) |
| — | 生态与工具 | [vLLM 商业化](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/) | vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。 | [official](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/) |
| — | 生态与工具 | [vllm-bench](https://github.com/vllm-project/vllm-bench) | vLLM serving 端点的高性能 Rust 压测客户端。 | [official](https://github.com/vllm-project/vllm-bench) |
| — | 生态与工具 | [vllm-bnb-plugin](https://github.com/vllm-project/vllm-bnb-plugin) | vLLM 的 bitsandbytes 量化插件。 | [official](https://github.com/vllm-project/vllm-bnb-plugin) |
| — | 生态与工具 | [vllm-gguf-plugin](https://github.com/vllm-project/vllm-gguf-plugin) | vLLM 的 GGUF 量化插件。 | [official](https://github.com/vllm-project/vllm-gguf-plugin) |

## SGLang 社区专题

SGLang 开源推理引擎及其 Kernel、结构化输出与生态集成材料；不收版本流水。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| — | 核心引擎 | [mini-sglang](https://github.com/sgl-project/mini-sglang) | mini-sglang：为揭示 SGLang 设计原理而做的精简实现。 | [official](https://github.com/sgl-project/mini-sglang) |
| — | 核心引擎 | [sglang-omni](https://github.com/sgl-project/sglang-omni) | SGLang-Omni：面向音频等全模态模型的高性能服务框架。 | [official](https://github.com/sgl-project/sglang-omni) |
| — | Kernel 与编译 | [sgl-kernel-npu](https://github.com/sgl-project/sgl-kernel-npu) | SGLang 的 NPU kernel 库。 | [official](https://github.com/sgl-project/sgl-kernel-npu) |
| — | Kernel 与编译 | [sgl-kernel-xpu](https://github.com/sgl-project/sgl-kernel-xpu) | SGLang 的 Intel XPU kernel 库。 | [official](https://github.com/sgl-project/sgl-kernel-xpu) |
| — | 生态与工具 | [rbg](https://github.com/sgl-project/rbg) | 在 Kubernetes 上部署 LLM 推理服务的工作负载（Router Benchmark Generator）。 | [official](https://github.com/sgl-project/rbg) |
| — | 生态与工具 | [sgl-eval](https://github.com/sgl-project/sgl-eval) | SGLang 的评测工具。 | [official](https://github.com/sgl-project/sgl-eval) |
| — | 生态与工具 | [SGLang 商业化](https://github.com/sgl-project/sglang) | 围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。 | [official](https://github.com/sgl-project/sglang) |
| — | 生态与工具 | [XGrammar production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) | 将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。 | [official](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) |

## LMCache 社区专题

LMCache 分层 KV 缓存与跨引擎 KV 复用材料；不收版本流水。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| — | KV 与缓存 | [kvcache-view](https://github.com/LMCache/kvcache-view) | KV cache 可视化工具。 | [official](https://github.com/LMCache/kvcache-view) |
| — | KV 与缓存 | [LMCache](https://arxiv.org/abs/2510.09665) | 将 KV cache 抽成独立层，支持跨 engine/query 复用和 GPU/CPU/storage/network 多层编排。 | [official](https://arxiv.org/abs/2510.09665) |
| — | KV 与缓存 | [LMCache Operator](https://github.com/LMCache/LMCache/releases/tag/operator-v0.1.1) | 首个 Kubernetes Operator 将 LMCacheEngine CRD 编排为与 vLLM worker 共置的 LMCache MP DaemonSet、Service、ConfigMap 和 Secret，并加入 RESP L2 backend、AMD GPU 支持与端到端 smoke tests。 | [official](https://github.com/LMCache/LMCache/releases/tag/operator-v0.1.1) |
| — | KV 与缓存 | [LMCache-Ascend](https://github.com/LMCache/LMCache-Ascend) | LMCache 在昇腾 NPU 上运行的插件。 | [official](https://github.com/LMCache/LMCache-Ascend) |
| — | KV 与缓存 | [lmcache_frontend](https://github.com/LMCache/lmcache_frontend) | LMCache 的前端组件。 | [official](https://github.com/LMCache/lmcache_frontend) |
| — | KV 与缓存 | [RDMA-Accelerated KV Cache Storage Offload](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/) | 将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。 | [official](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/) |
| — | 生态与工具 | [LMBenchmark](https://github.com/LMCache/LMBenchmark) | 面向 LLM 系统的系统化、全面基准测试。 | [official](https://github.com/LMCache/LMBenchmark) |
| — | 生态与工具 | [lmcache-agent-trace](https://github.com/LMCache/lmcache-agent-trace) | agent 应用的 workload trace 集合，用于 KV 缓存研究。 | [official](https://github.com/LMCache/lmcache-agent-trace) |
| — | 生态与工具 | [LMCache-Examples](https://github.com/LMCache/LMCache-Examples) | LMCache 的官方示例集。 | [official](https://github.com/LMCache/LMCache-Examples) |

## llm-d 社区专题

llm-d 分布式推理网关与调度、路由、P/D 分离材料；不收版本流水。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| — | KV 与缓存 | [llm-d KV Cache](https://github.com/llm-d/llm-d-kv-cache) | 用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。 | [official](https://github.com/llm-d/llm-d-kv-cache) |
| — | 调度与路由 | [llm-d](https://github.com/llm-d/llm-d) | 将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。 | [official](https://github.com/llm-d/llm-d) |
| — | 调度与路由 | [llm-d + LMCache + vLLM](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes) | Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。 | [official](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes) |
| — | 调度与路由 | [llm-d-async](https://github.com/llm-d/llm-d-async) | Inference Gateway 的异步处理器与编排器。 | [official](https://github.com/llm-d/llm-d-async) |
| — | 调度与路由 | [llm-d-autoscaling](https://github.com/llm-d/llm-d-autoscaling) | 面向分布式推理工作负载的变体优化自动扩缩器。 | [official](https://github.com/llm-d/llm-d-autoscaling) |
| — | 调度与路由 | [llm-d-router](https://github.com/llm-d/llm-d-router) | llm-d Router：推理请求的智能入口。 | [official](https://github.com/llm-d/llm-d-router) |
| — | 调度与路由 | [llm-d-routing-sidecar](https://github.com/llm-d/llm-d-routing-sidecar) | llm-d 的 P/D 分离 sidecar（孵化中）。 | [official](https://github.com/llm-d/llm-d-routing-sidecar) |
| — | 生态与工具 | [llm-d-batch-gateway](https://github.com/llm-d/llm-d-batch-gateway) | 后端无关、OpenAI 兼容的批处理网关。 | [official](https://github.com/llm-d/llm-d-batch-gateway) |
| — | 生态与工具 | [llm-d-benchmark](https://github.com/llm-d/llm-d-benchmark) | llm-d 的基准测试脚本与工具。 | [official](https://github.com/llm-d/llm-d-benchmark) |

## Mooncake 社区专题

Mooncake 以 KVCache 为中心的分离式 Serving 与传输层材料；不收版本流水。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| — | KV 与缓存 | [Mooncake](https://www.usenix.org/conference/fast25/presentation/qin) | 以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。 | [official](https://www.usenix.org/conference/fast25/presentation/qin) |
| — | KV 与缓存 | [MooncakeStoreConnector](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/) | vLLM 文档化 MooncakeStoreConnector，支持 embedded 和 standalone-store 模式，扩展 CPU/SSD KV pool。 | [official](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/) |
| — | 生态与工具 | [AgentENV](https://github.com/kvcache-ai/AgentENV) | AgentENV（AENV）：运行 agent 环境的分布式平台。 | [official](https://github.com/kvcache-ai/AgentENV) |
| — | 生态与工具 | [Mooncake Joins PyTorch Ecosystem](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) | Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。 | [official](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) |

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

### KV Cache (14)

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
  NVFP4 KV cache 量化把显存占用相对 FP8 再压缩最高 50%，等效把上下文预算翻倍；在 LiveCodeBench、MMLU-PRO、MBPP、Ruler 64K 上精度损失低于 1%，decode 阶段缓解显存带宽压力，prefill 阶段 TTFT 最高改善 3 倍。
- **[Online Scheduling with KV Cache Constraints](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `memory`
  将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。
- **[TensorRT-LLM KV cache reuse](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `prefill` `routing` `kv-cache` `tensorrt-llm`
  TensorRT-LLM 引入基于优先级的 KV cache 驱逐机制，可按 token 区间与 decode block 指定保留优先级与时长，并通过 Executor API 与 KV cache 事件 API 支撑跨实例的 KV-aware 路由；内部基准中缓存命中率提升约 20%。
- **[kvcache-view](https://github.com/LMCache/kvcache-view)**
  `LMCache community` · `2025` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving`
  KV cache 可视化工具。
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
- **[Tiered KV cache for large LLMs on Amazon SageMaker HyperPod with Curvine](https://aws.amazon.com/blogs/machine-learning/tiered-kv-cache-for-large-llms-on-amazon-sagemaker-hyperpod-with-curvine/)**
  `Amazon Web Services` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `gpu` `kv-cache` `slo`
  在 SageMaker HyperPod 上用 Curvine 把 KV cache 扩展为共享的分布式 NVMe 池形成分层缓存，使副本以近本地磁盘速度复用缓存，从而在低成本实例上缓解「大 GPU 实例 vs 慢 TTFT」的取舍。
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

### Prefill–Decode 与传输 (13)

#### Featured

- **Featured:** **[vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/)**
  `PyTorch Foundation / vLLM community` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `vllm`
  vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。
- **Featured:** **[FlashInfer kernel ecosystem](https://github.com/flashinfer-ai/flashinfer)**
  `FlashInfer community / NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `kernel` `rag` `sglang` `vllm`
  针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。
- **Featured:** **[P/D-Serve](https://arxiv.org/abs/2408.08147)**
  `Huawei` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `decode` `prefill` `npu`
  在数万 xPU/NPU 规模上部署 prefill/decode disaggregated serving，做 P/D 组织、调度和 D2D KV transfer。
#### Full Resource List

- **[vLLM V1](https://github.com/vllm-project/vllm)**
  `vLLM / PyTorch Foundation` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `serving` `vllm`
  以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。
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
  NIXL 是开源的厂商无关数据搬运库，为 GPU 显存、CPU 内存与存储层之间的传输提供统一 API，后端覆盖 RDMA、GPU-initiated networking、GPU-Direct storage、NVMe 与 S3／Azure Blob；核心场景是 P/D 分离的 KV 传输、长上下文 KV 落盘与权重快速换入。
- **[UCCL](https://github.com/uccl-project/uccl)**
  `IBM / Red Hat / Google 等` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `kv-cache` `llm-d`
  GPU 通信库，覆盖 collectives、P2P KV cache transfer、RL weight transfer 和 expert parallelism，进入 llm-d 分布式推理栈。
- **[When to Use Encode-Prefill-Decode Disaggregation to Accelerate Multimodal Model Serving](https://developer.nvidia.com/blog/when-to-use-encode-prefill-decode-disaggregation-to-accelerate-multimodal-model-serving/)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `decode` `prefill` `multimodal`
  Dynamo 实现 encode-prefill-decode（EPD）三级解耦，把视觉编码从 LLM 的 prefill／decode 中拆出；对图像密集、输出中短与量化 MoE 模型，TTFT 最高快 5 倍、端到端响应时间最高快 7 倍。编码器可聚合部署、与 P/D worker 共卡，或放到更低成本的独立 GPU 层经 NIXL 连接。
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
- **[Amazon SageMaker Inference: 2026 year-to-date launches in review](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-inference-2026-year-to-date-launches-in-review/)**
  `Amazon Web Services` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: supporting`
  Tags: `decode` `prefill`
  AWS 回顾 2026 年以来 SageMaker AI 在托管端点与 HyperPod Inference 两条路径上的 13 项推理发布，覆盖推理推荐、容量感知实例池、分层 KV 缓存与 prefill/decode 分离等能力。

### Speculative Decoding (4)

#### Full Resource List

- **[Boost Inference Performance up to 15x on NVIDIA Blackwell Using DFlash Speculative Decoding](https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `blackwell` `cuda` `compiler` `kernel` `agent` `latency`
  DFlash 用块扩散（block-diffusion）drafter 在单次前向中并行生成多个候选 token 再并行验证；在 Blackwell Ultra 上对 gpt-oss-120b 实现同等交互性下最高 15 倍吞吐提升，对 Llama 3.1 8B 的交互性接近 EAGLE-3 的两倍，并已集成 SGLang、vLLM 与 TensorRT-LLM。
- **[DFlash Speculative Decoding on AMD Instinct MI355X: Up to 5× Faster Qwen3.5 Inference](https://rocm.blogs.amd.com/artificial-intelligence/dflash-on-MI355x/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `amd` `rocm` `compiler` `kernel`
  在 AMD MI355X 上经 vLLM/ROCm 部署 DFlash 这一 block-diffusion drafter，对标 Qwen3.5 内置 MTP drafter，并通过 mxfp4 量化目标模型证明其可与 speculation 叠加，使 Qwen3.5 推理最高加速 5×。
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
  AMD AITER 为 ROCm 推理提供 C++/Python API 与优化的 Triton、Composable Kernel 及汇编算子（覆盖 attention、MoE、GEMM、quantization、通信 kernel），并直接接入 vLLM 与 SGLang。
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

### Compiler / DSL (14)

#### Featured

- **Featured:** **[ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/)**
  `AMD` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `amd` `gpu` `kernel` `sglang` `tensorrt-llm`
  通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。
#### Full Resource List

- **[torch.compile / Inductor](https://docs.pytorch.org/docs/stable/torch.compiler.html)**
  `PyTorch` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `kernel` `vllm`
  捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。
- **[4-bit KV Caching in LMCache: Offloading Quantized KV Beyond HBM for Context-Heavy Agents on AMD MI355X](https://rocm.blogs.amd.com/software-tools-optimization/4bit-KV-LMcache/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `amd` `rocm` `compiler` `kernel` `agent` `lmcache`
  LMCache 在 AMD MI355X 上将 TurboQuant 4-bit KV 量化与分层缓存结合，用布局感知连接器把量化 KV 越过 HBM 边界卸载到 CPU DRAM 再取回，做到位精确、精度无损，使上下文密集智能体在量化与分层叠加时仍能兼顾 goodput、latency 与 accuracy。
- **[Co-Designing AI Model Attention for Fast, Interactive Long-Context Inference](https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `compiler` `kernel` `agent` `long-context`
  NVIDIA 系统刻画了 GPU 上 dense attention 的性能边界：prefill 受算力约束、decode 受显存带宽约束；增大 group size（如 GQA/MQA）可提升 decode 吞吐而几乎不影响 prefill，head dim 取 128 或 256 才能与 GPU tile 尺寸和 128 字节访存对齐。
- **[Efficient MiniMax-M3 Inference on AMD Instinct GPUs with ATOM and ATOMesh](https://rocm.blogs.amd.com/artificial-intelligence/minmax-m3-atomesh/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `amd` `gpu` `compiler` `kernel`
  ATOM 与 ATOMesh 在 AMD Instinct GPU 上高效服务 MiniMax-M3——这一 428B 总参/22B 激活的多模态 MoE，其 MiniMax Sparse Attention 以块级 KV cache 选择替代平方注意力、将每 token 计算降至前代的 1/20——兼顾单机优化与多机编排。
- **[Efficiently Serving NVFP4 Models on AMD Instinct™ MI350X/MI355X Accelerators via Online NVFP4 to Quark MXFP4 Requantization](https://rocm.blogs.amd.com/software-tools-optimization/nvfp4-to-mxfp4/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `compiler` `compression`
  SGLang 中的在线 NVFP4→MXFP4 重量化管线在权重加载时一次性把 NVFP4 参数转为 MXFP4，使 NVFP4 模型能跑在 MI350X/MI355X 的原生 MXFP4 路径上，无需离线预处理，精度与原生 NVFP4 持平、吞吐与原生 MXFP4 相当。
- **[Hyperloom - Autonomous Agentic Inference Optimization for AMD GPUs](https://rocm.blogs.amd.com/software-tools-optimization/hyperloom/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `amd` `gpu` `compiler` `kernel` `agent` `rag`
  ROCm Hyperloom 是开源的自治式智能体系统，用自主优化循环自动完成端到端推理调优，将优化耗时从数周压缩到数小时，在 AMD Instinct GPU 上榨取模型与配置的峰值性能。
- **[Introducing AMD ROCm™ Infera: Scaling Goodput for Agentic AI with Distributed Inference Orchestration](https://rocm.blogs.amd.com/software-tools-optimization/infera-di/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `compiler` `kernel` `agent` `rag` `goodput`
  ROCm Infera 是面向大规模部署的分布式推理编排参考方案，作为「GPU 乐团指挥」协调多实例，内部测试显示真实智能体负载下每 GPU 的 goodput 最高提升 2.6×，并原生集成 vLLM、SGLang 与 ATOM。
- **[Productionizing TurboQuant on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html)**
  `AMD ROCm + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `amd` `gpu` `kernel` `kv-cache` `agent` `vllm` `ttft`
  在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。
- **[Restore LLM Inference Capacity in Seconds with Shadow Engine Recovery in NVIDIA Dynamo](https://developer.nvidia.com/blog/restore-llm-inference-capacity-in-seconds-with-shadow-engine-recovery-in-nvidia-dynamo/)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `compiler` `kernel` `agent` `rag`
  Dynamo 的 Shadow Engine Recovery 在同一批 GPU 上常驻一个已初始化的影子引擎，由 GPU Memory Service 在引擎间共享权重而不额外占用 HBM；在 B200 上双 worker 的 GLM-5.2 部署中恢复服务耗时 7.3 秒，相比冷重启的 283 秒快约 39 倍。
- **[Serving 64Mi-Token Contexts on One AMD Instinct™ MI355X Node](https://rocm.blogs.amd.com/artificial-intelligence/long-context-serving/README.html)**
  `AMD` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `compiler` `kernel`
  在单台 8-GPU MI355X 节点上用 vLLM（FP8 KV cache、TP=8）服务 Kimi Linear 48B-A3B，覆盖 1024 到 64Mi token 共六个数量级的上下文，以 FP8 KV 存储让最长上下文也能落在单节点内，并报告各长度的 TTFT 与 decode throughput。
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

### Runtime / Scheduling (29)

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
- **Featured:** **[mini-sglang](https://github.com/sgl-project/mini-sglang)**
  `SGLang community` · `2025` · `Industry / engineering material` · `Industrial Material` · `Reading priority: foundation`
  Tags: `serving`
  mini-sglang：为揭示 SGLang 设计原理而做的精简实现。
- **Featured:** **[sglang-omni](https://github.com/sgl-project/sglang-omni)**
  `SGLang community` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: foundation`
  Tags: `serving`
  SGLang-Omni：面向音频等全模态模型的高性能服务框架。
#### Full Resource List

- **[InfiniStore](https://github.com/bytedance/InfiniStore)**
  `ByteDance` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `kv-cache` `lmcache` `vllm`
  高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。
- **[llm-d](https://github.com/llm-d/llm-d)**
  `Red Hat / IBM / Google / NVIDIA 社区` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `routing` `kubernetes` `llm-d`
  将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。
- **[llm-d-autoscaling](https://github.com/llm-d/llm-d-autoscaling)**
  `llm-d community` · `2025` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving`
  面向分布式推理工作负载的变体优化自动扩缩器。
- **[vllm-ascend](https://github.com/vllm-project/vllm-ascend)**
  `vLLM community` · `2025` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving`
  vLLM 在昇腾 NPU 上的官方硬件后端插件。
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
- **[vllm-bench](https://github.com/vllm-project/vllm-bench)**
  `vLLM community` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving`
  vLLM serving 端点的高性能 Rust 压测客户端。
- **[vllm-bnb-plugin](https://github.com/vllm-project/vllm-bnb-plugin)**
  `vLLM community` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving`
  vLLM 的 bitsandbytes 量化插件。
- **[vllm-gguf-plugin](https://github.com/vllm-project/vllm-gguf-plugin)**
  `vLLM community` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving`
  vLLM 的 GGUF 量化插件。
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
- **[ThunderAgent: 2x Faster Agentic Inference for Synthetic Data Generation at Scale](https://www.together.ai/blog/thunderagent)**
  `Together AI` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: supporting`
  Tags: `serving` `kv-cache` `scheduler` `agent` `rag` `throughput`
  ThunderAgent 是面向智能体推理的「程序感知」调度器，把每个智能体工作流当作可调度程序来消除 KV cache 抖动，带来超过 2× 的单节点吞吐与近线性的多节点扩展。

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
