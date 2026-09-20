# Industry & Open-Source Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Academic papers](../papers/README.md)

A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Industrial material | With artifact | Tagged records |
|---:|---:|---:|---:|
| 63 | 63 | 63 | 62 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (2)
- [KV Cache](#kv-cache) (12)
- [Prefill–Decode 与传输](#prefill-decode) (11)
- [Speculative Decoding](#speculative-decoding) (2)
- [MoE](#moe) (9)
- [Compiler / DSL](#compiler-dsl) (6)
- [Runtime / Scheduling](#runtime-scheduling) (21)
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
| DeepSeek-V3 | 架构与系统 | [DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | DeepSeek-V3 官方模型与推理参考，公开 MLA、DeepSeekMoE、FP8 权重转换及多种 GPU/NPU 运行入口。 | [official](https://github.com/deepseek-ai/DeepSeek-V3) |
| DeepSeek-V3 | 架构与系统 | [Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures](https://arxiv.org/abs/2505.09343) | 从 DeepSeek-V3/R1 的 MLA、MoE、FP8 与 Multi-Plane Network 出发，总结 2,048 张 H800 规模下的模型—硬件协同设计与系统瓶颈。 | [official](https://arxiv.org/abs/2505.09343) |
| DeepSeek-V3.2 | 架构与系统 | [DeepSeek-V3.2 / DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) | 在模型架构中加入 sparse attention/indexer，目标是在长上下文和 reasoning/agent 任务中降低推理成本。 | [official](https://arxiv.org/abs/2512.02556) |
| DeepSeek-OCR | OCR 与生态 | [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | 通过视觉 token 压缩处理长文档上下文，并提供 OCR 推理与大规模页面数据生成路径。 | [official](https://github.com/deepseek-ai/DeepSeek-OCR) |
| DeepSeek-OCR-2 | OCR 与生态 | [DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | DeepSeek OCR 的后续官方项目，以 Visual Causal Flow 组织文档视觉理解与生成流程。 | [official](https://github.com/deepseek-ai/DeepSeek-OCR-2) |
| — | 核心算子与通信 | [DeepEP](https://github.com/deepseek-ai/DeepEP) | 面向 MoE expert parallel 的高吞吐、低延迟通信库，提供 dispatch/combine、低延迟模式与 GPU 通信优化。 | [official](https://github.com/deepseek-ai/DeepEP) |
| — | 核心算子与通信 | [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | 面向 FP8/BF16 的 GPU GEMM kernel 库，为 DeepSeek dense 与 MoE 路径提供紧凑、可调优的矩阵乘实现。 | [official](https://github.com/deepseek-ai/DeepGEMM) |
| — | 核心算子与通信 | [FlashMLA](https://github.com/deepseek-ai/FlashMLA) | 面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。 | [official](https://github.com/deepseek-ai/FlashMLA) |
| — | 核心算子与通信 | [TileKernels](https://github.com/deepseek-ai/TileKernels) | 以 TileLang 编写的 kernel library，用 tile 级抽象组织和优化 GPU 算子实现。 | [official](https://github.com/deepseek-ai/TileKernels) |
| — | 存储与数据路径 | [3FS](https://github.com/deepseek-ai/3FS) | 面向 AI 训练与推理负载的高性能分布式文件系统，强调并行数据路径、吞吐与大规模 checkpoint/data access。 | [official](https://github.com/deepseek-ai/3FS) |
| — | 推测解码 | [DeepSpec](https://github.com/deepseek-ai/DeepSpec) | 用于训练、评估和复现实用 speculative decoding 方法的官方工具集，覆盖 draft/verify 与接受率评测。 | [official](https://github.com/deepseek-ai/DeepSpec) |
| — | OCR 与生态 | [Awesome DeepSeek Agents](https://github.com/deepseek-ai/awesome-deepseek-agent) | 面向 DeepSeek Agent、coding agent 与工具调用生态的官方项目索引。 | [official](https://github.com/deepseek-ai/awesome-deepseek-agent) |
| — | OCR 与生态 | [Awesome DeepSeek Integrations](https://github.com/deepseek-ai/awesome-deepseek-integration) | DeepSeek API 在应用、Agent、RAG、开发工具和基础设施中的官方集成索引。 | [official](https://github.com/deepseek-ai/awesome-deepseek-integration) |
| — | OCR 与生态 | [DeepSeek Open Infra Index](https://github.com/deepseek-ai/open-infra-index) | DeepSeek 官方 AI infrastructure 导航入口，集中索引其生产验证的 kernel、通信、存储和系统工具。 | [official](https://github.com/deepseek-ai/open-infra-index) |

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
| — | 推理系统 | [Mooncake](https://www.usenix.org/conference/fast25/presentation/qin) | 以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。 | [official](https://www.usenix.org/conference/fast25/presentation/qin) |
| — | 推理系统 | [Mooncake Joins PyTorch Ecosystem](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) | Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。 | [official](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) |
| — | 推理系统 | [MoonEP](https://github.com/MoonshotAI/MoonEP) | MoonEP：通过动态冗余专家实现负载均衡的专家并行（expert parallelism）库。 | [official](https://github.com/MoonshotAI/MoonEP) |
| — | 推理系统 | [vLLM x Mooncake Store](https://vllm.ai/blog/2026-05-06-mooncake-store) | 将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。 | [official](https://vllm.ai/blog/2026-05-06-mooncake-store) |
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

### Runtime / Scheduling (21)

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
