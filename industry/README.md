# Industry & Open-Source Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Academic papers](../papers/README.md)

A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. A bounded rolling exploration section keeps new workloads visible; the full adjacent/archive history remains in the [archive](../archive/README.md).

## At a Glance

| Records | Industrial material | With artifact | Tagged records |
|---:|---:|---:|---:|
| 31 | 31 | 25 | 30 |

## Collection Navigation

- [Attention / Kernel](#attention-kernel) (2)
- [KV Cache](#kv-cache) (5)
- [Prefill–Decode 与传输](#prefill-decode) (5)
- [Speculative Decoding](#speculative-decoding) (4)
- [MoE](#moe) (5)
- [Compiler / DSL](#compiler-dsl) (5)
- [Runtime / Scheduling](#runtime-scheduling) (5)
- [探索观察](#探索观察) (5)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | `core` records form the main reading themes; a bounded `adjacent` window appears under exploration, with full adjacent/archive history on the archive page. |
| Featured | A small editorial starting set within the bounded core reading set; complete facts remain in JSONL and the archive. |

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

## 昇腾 / 华为 AI 系统专题

昇腾 NPU 的 CANN/Ascend C 工具链、推理运行时与生产 Serving 系统材料；第一阶段仅收录直接作用于推理执行路径的官方或正式证据。

| 代际 | 类别 | 材料 / 项目 | 系统作用 | 来源 |
|---|---|---|---|---|
| — | 芯片工具链与算子 | [CANN / Ascend C](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/index/index.html) | CANN 为昇腾硬件提供 AI 计算软件栈、框架接口与运行时能力，Ascend C 用于开发和优化设备侧自定义算子。 | [official](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/900/index/index.html) |
| — | 生产推理系统 | [LLM Serving on Huawei CloudMatrix384](https://arxiv.org/abs/2506.12708) | CloudMatrix384 以昇腾超节点互联和生产级系统软件组织大规模 LLM Serving，覆盖并行执行、P/D 分离、KV 传输与集群调度。 | [official](https://arxiv.org/abs/2506.12708) |
| — | 训练与推理框架 | [MindSpore](https://github.com/mindspore-ai/mindspore) | MindSpore 是面向端、边、云训练与推理的开源框架，原生支持昇腾处理器并强调软硬件协同优化。 | [official](https://github.com/mindspore-ai/mindspore) |
| — | 云平台与资源管理 | [ModelArts](https://support.huaweicloud.com/intl/en-us/productdesc-modelarts/modelarts_01_0001.html) | ModelArts 提供数据、开发、分布式训练、模型部署、异构资源调度和运维的一站式平台，并支持昇腾推理栈。 | [official](https://support.huaweicloud.com/intl/en-us/productdesc-modelarts/modelarts_01_0001.html) |
| — | CPU 与异构基础设施 | [Kunpeng BoostKit Inference](https://www.hikunpeng.com/document/detail/en/SRA/accelFeatures/SRA_Inference/kunpengsra_inference_16_0001.html) | Kunpeng BoostKit SRA Inference 为鲲鹏平台提供推理加速套件和优化算子，补足通用 CPU 与昇腾 NPU 协同栈的 CPU 侧能力。 | [official](https://www.hikunpeng.com/document/detail/en/SRA/accelFeatures/SRA_Inference/kunpengsra_inference_16_0001.html) |

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

### KV Cache (5)

#### Full Resource List

- **[llm-d KV Cache](https://github.com/llm-d/llm-d-kv-cache)**
  `llm-d` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `routing` `kv-cache` `kubernetes` `llm-d`
  用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。
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

### Prefill–Decode 与传输 (5)

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
- **Featured:** **[vLLM V1](https://github.com/vllm-project/vllm)**
  `vLLM / PyTorch Foundation` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `prefill` `serving` `vllm`
  以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。
#### Full Resource List

- **[ATOMesh distributed serving gateway](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `decode` `prefill` `amd` `gpu` `routing` `sglang` `vllm`
  作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。

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

### MoE (5)

#### Full Resource List

- **[DeepSpeed-MoE](https://arxiv.org/abs/2201.05596)**
  `Microsoft` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `moe`
  联合 expert parallel、通信优化和模型压缩，使稀疏大模型的推理成本可控。
- **[Tutel](https://github.com/microsoft/tutel)**
  `Microsoft Research Asia` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `kernel` `moe`
  提供自适应 expert parallel、all-to-all、fused kernel 和动态配置，是通用 MoE 软件栈的重要来源。
- **[AITER: AI Tensor Engine for ROCm](https://github.com/ROCm/aiter)**
  `AMD / ROCm` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `compiler` `kernel` `moe` `sglang` `vllm`
  AMD AITER 为 ROCm 推理提供 C++/Python API 与优化的 Triton、Composable Kernel 及汇编算子（覆盖 attention、MoE、GEMM、quantization、通信 kernel），并直接接入 vLLM 与 SGLang。
- **[ATOM inference engine](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `serving` `amd` `rocm` `kernel` `moe`
  以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。
- **[COMET](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html)**
  `Alibaba Cloud` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `gpu` `moe`
  细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。

### Compiler / DSL (5)

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

### Runtime / Scheduling (5)

#### Featured

- **Featured:** **[SGLang 商业化](https://github.com/sgl-project/sglang)**
  `SGLang maintainers / RadixArk` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `sglang`
  围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。
- **Featured:** **[sglang-omni](https://github.com/sgl-project/sglang-omni)**
  `SGLang community` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: foundation`
  Tags: `serving`
  SGLang-Omni：面向音频等全模态模型的高性能服务框架。
- **Featured:** **[FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)**
  `NVIDIA / University of Washington` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: foundation`
  Tags: `serving` `kernel` `sglang` `vllm`
  从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。
- **Featured:** **[mini-sglang](https://github.com/sgl-project/mini-sglang)**
  `SGLang community` · `2025` · `Industry / engineering material` · `Industrial Material` · `Reading priority: foundation`
  Tags: `serving`
  mini-sglang：为揭示 SGLang 设计原理而做的精简实现。
- **Featured:** **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: frontier`
  Tags: `memory` `tensorrt-llm` `vllm`
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。

### 探索观察

最近 180 天内有正式或工程证据、但尚未成为稳定主线的新语境工作。

- **[Kunpeng BoostKit Inference](https://www.hikunpeng.com/document/detail/en/SRA/accelFeatures/SRA_Inference/kunpengsra_inference_16_0001.html)**
  `Huawei Kunpeng` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: supporting`
  Tags: `serving` `cpu` `kernel` `tensorflow`
  Kunpeng BoostKit SRA Inference 为鲲鹏平台提供推理加速套件和优化算子，补足通用 CPU 与昇腾 NPU 协同栈的 CPU 侧能力。
- **[MindSpore](https://github.com/mindspore-ai/mindspore)**
  `MindSpore community / Huawei` · `2026` · `Open-source project` · `Industrial Material` · `Reading priority: supporting`
  Tags: `serving` `npu` `gpu` `compiler` `kernel` `mindspore`
  MindSpore 是面向端、边、云训练与推理的开源框架，原生支持昇腾处理器并强调软硬件协同优化。
- **[ModelArts](https://support.huaweicloud.com/intl/en-us/productdesc-modelarts/modelarts_01_0001.html)**
  `Huawei Cloud` · `2026` · `Industry / engineering material` · `Industrial Material` · `Reading priority: supporting`
  Tags: `serving` `npu` `gpu` `scheduler` `mindspore` `pytorch` `availability`
  ModelArts 提供数据、开发、分布式训练、模型部署、异构资源调度和运维的一站式平台，并支持昇腾推理栈。
- **[Ragged Paged Attention for TPU](https://arxiv.org/abs/2604.15464)**
  `Google / TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `tpu` `kernel` `rag`
  面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。
- **[SPIN](https://www.microsoft.com/en-us/research/publication/unifying-sparse-attention-with-hierarchical-memory-for-scalable-long-context-llm-serving/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import` · `Reading priority: supporting`
  Tags: `gpu` `rag`
  把 sparse attention execution pipeline 与 CPU/GPU hierarchical KV storage 联合设计，解决不规则 KV subset 检索开销。
