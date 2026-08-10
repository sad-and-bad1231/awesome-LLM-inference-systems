# 工业界 LLM 推理系统方案追踪

<!-- generated from data/papers.jsonl, data/industry.jsonl, or data/candidates.jsonl; do not edit directly -->

更新时间：由 `data/industry.jsonl` 生成。

## 观察框架

- TTFT under Drift：基础设施漂移、广域网抖动、Spot 节点切换时的首 token 延迟恶化边界。
- Generation Stall Rate：推测解码验证失败、MoE all-to-all 热点或 tool-call 挂起造成的生成中断率。
- Numerical Reproducibility：低精度混合量化、scale search 和异构执行导致的数值不稳定与非确定性。

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

## 项目级工程主线

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
| AMD | ROCm + vLLM/SGLang/TensorRT-LLM ecosystem | 2024 | Compiler / DSL / Runtime / Scheduling | 通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。 | [primary](https://rocm.docs.amd.com/) |
| PyTorch Foundation / vLLM community | vLLM V1 + torch.compile | 2025 | Prefill–Decode 与传输 / Runtime / Scheduling | vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。 | [primary](https://pytorch.org/projects/vllm/) |
| SGLang maintainers / RadixArk | SGLang 商业化 | 2026 | Runtime / Scheduling | 围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。 | [primary](https://github.com/sgl-project/sglang) |
| NVIDIA | NIXL / KV cache transfer | 2025 | KV Cache / Prefill–Decode 与传输 | 面向推理数据移动的传输层，在 prefill/decode 分离时把 KV cache 从 prefill worker 传到 decode worker。 | [primary](https://docs.nvidia.com/dynamo/archive/0.8.0/backends/trtllm/kv-cache-transfer.html) |
| IBM / Red Hat / llm-d | llm-d + LMCache + vLLM | 2025 | Runtime / Scheduling | Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。 | [primary](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes) |
| NVIDIA | Dynamo KVBM | 2026 | Runtime / Scheduling | KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。 | [primary](https://docs.dynamo.nvidia.com/dynamo/components/kvbm) |
| Microsoft | DeepSpeed-MoE | 2022 | MoE | 联合 expert parallel、通信优化和模型压缩，使稀疏大模型的推理成本可控。 | [primary](https://arxiv.org/abs/2201.05596) |
| Microsoft Research Asia | Tutel | 2022 | MoE | 提供自适应 expert parallel、all-to-all、fused kernel 和动态配置，是通用 MoE 软件栈的重要来源。 | [primary](https://github.com/microsoft/tutel) |
| PyTorch | torch.compile / Inductor | 2023 | Compiler / DSL / Runtime / Scheduling | 捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。 | [primary](https://docs.pytorch.org/docs/stable/torch.compiler.html) |
| vLLM / PyTorch Foundation | vLLM V1 | 2023 | Prefill–Decode 与传输 / Runtime / Scheduling | 以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。 | [primary](https://github.com/vllm-project/vllm) |
| FlashInfer community / NVIDIA | FlashInfer kernel ecosystem | 2024 | Prefill–Decode 与传输 / Runtime / Scheduling | 针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。 | [primary](https://github.com/flashinfer-ai/flashinfer) · [FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) |
| Huawei | P/D-Serve | 2024 | Prefill–Decode 与传输 | 在数万 xPU/NPU 规模上部署 prefill/decode disaggregated serving，做 P/D 组织、调度和 D2D KV transfer。 | [primary](https://arxiv.org/abs/2408.08147) |
| IBM Research | PagedAttention + FlexAttention / FMS | 2025 | Attention / Kernel | 在 IBM Foundation Model Stack 中把 PagedAttention 与 FlexAttention 融合，处理 scattered KV gather。 | [primary](https://arxiv.org/abs/2506.07311) |
| Huawei Cloud / Ascend | Ascend-vLLM prefix caching / KV offload | 2025 | KV Cache / Runtime / Scheduling | 在 Ascend NPU 上支持 prefix caching、KV cache CPU offload 和 Mooncake/LMCache 连接。 | [primary](https://support.huaweicloud.com/intl/en-us/bestpractice-modelarts/modelarts_llm_infer_5906020.html) |
| DeepSeek | DeepGEMM / DeepEP | 2025 | MoE | FP8 GEMM 与 MoE expert-parallel 通信库，支撑 DeepSeek 系列训练和推理的 dense/MoE fast path。 | [primary](https://flashmla.net/) |
| ByteDance | InfiniStore | 2025 | Runtime / Scheduling | 高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。 | [primary](https://github.com/bytedance/InfiniStore) |
| KServe | KV Cache Offloading | 2025 | KV Cache / Runtime / Scheduling | 在 KServe generative inference 中集成 LMCache/vLLM KV offloading，面向云原生模型服务。 | [primary](https://kserve.github.io/website/docs/model-serving/generative-inference/kvcache-offloading) |
| ByteDance Seed | MegaScale-Infer | 2025 | MoE | 将 attention 和 MoE FFN 分池部署，以 disaggregated expert parallelism、ping-pong pipeline 和 M2N 通信提升专家利用率。 | [primary](https://arxiv.org/abs/2504.02263) |
| NVIDIA | NVFP4 KV cache | 2025 | KV Cache / MoE | Blackwell 侧使用 4-bit KV 存储、attention 前解量化到 FP8，面向长上下文、大 batch、多 agent/MoE 降低 HBM 压力。 | [primary](https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/) |
| Microsoft Research | Online Scheduling with KV Cache Constraints | 2025 | KV Cache / Runtime / Scheduling | 将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。 | [primary](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/) |
| 阶跃星辰 | Step-Audio2 | 2025 | Runtime / Scheduling | 端到端音频理解和语音对话模型，提供推理示例与 vLLM backend。 | [primary](https://github.com/stepfun-ai/Step-Audio2) |
| NVIDIA | TensorRT-LLM KV cache reuse | 2025 | KV Cache / Prefill–Decode 与传输 / Runtime / Scheduling | 用 KV cache event API 和 KV-aware routing 提高 prefix/cache 命中，减少重复 prefill。 | [primary](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/) |
| MLC / SGLang / vLLM ecosystem | XGrammar production integration | 2025 | Prefill–Decode 与传输 / Runtime / Scheduling | 将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html) |
| Red Hat / IBM / Google / NVIDIA 社区 | llm-d | 2025 | Runtime / Scheduling | 将 vLLM、Gateway API、KV-aware routing、PD disaggregation、LMCache 和可观测性组合为云原生分布式推理栈。 | [primary](https://github.com/llm-d/llm-d) |
| AMD / ROCm | AITER: AI Tensor Engine for ROCm | 2026 | MoE / Compiler / DSL / Runtime / Scheduling | AMD AITER (AI Tensor Engine for ROCm) provides C++/Python APIs and optimized Triton, Composable Kernel, and assembly operators for ROCm inference, including attention, MoE, GEMM, quantization, and communication kernels; it integrates with… | [primary](https://github.com/ROCm/aiter) |
| AMD ROCm | ATOM inference engine | 2026 | MoE / Compiler / DSL / Runtime / Scheduling | 以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。 | [primary](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html) |
| AMD ROCm | ATOMesh distributed serving gateway | 2026 | Prefill–Decode 与传输 / Compiler / DSL / Runtime / Scheduling | 作为 AMD GPU 集群的分布式推理控制面，统一 prefill/decode routing、KV-aware scheduling、worker lifecycle、retries、observability，并协调 ATOM、vLLM、SGLang 后端。 | [primary](https://rocm.blogs.amd.com/software-tools-optimization/atomesh-inference/README.html) |
| Tencent Cloud TACO + NVIDIA | FlexKV | 2026 | Runtime / Scheduling | 分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。 | [primary](https://github.com/taco-project/FlexKV) |
| vLLM | KV Offloading Connector | 2026 | Runtime / Scheduling | vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。 | [primary](https://vllm.ai/blog/kv-offloading-connector) |
| Moonshot AI; PyTorch | Mooncake Joins PyTorch Ecosystem | 2026 | Runtime / Scheduling | Mooncake 加入 PyTorch 生态，面向 SGLang、vLLM、TensorRT-LLM 提供 KVCache transfer 和 storage 能力。 | [primary](https://pytorch.org/blog/mooncake-joins-pytorch-ecosystem/) |
| vLLM Project; Mooncake Project | MooncakeStoreConnector | 2026 | Runtime / Scheduling | vLLM 文档化 MooncakeStoreConnector，支持 embedded 和 standalone-store 模式，扩展 CPU/SSD KV pool。 | [primary](https://docs.vllm.ai/en/v0.22.0/features/mooncake_store_connector_usage/) |
| NVIDIA | NIXL / Inference Transfer Library | 2026 | Prefill–Decode 与传输 | 非阻塞传输 API 和动态元数据交换，覆盖 disaggregated KV movement、long-context storage、weight transfer 和 expert parallelism。 | [primary](https://developer.nvidia.com/blog/?p=113426) |
| NVIDIA / ai-dynamo maintainers | NVIDIA Dynamo | 2026 | Prefill–Decode 与传输 / Runtime / Scheduling | Dynamo 在 vLLM、SGLang 和 TensorRT-LLM 之上提供多节点编排，组合 P/D 解耦、KV-aware 路由、多层 KV 缓存和自动扩缩容。 | [primary](https://github.com/ai-dynamo/dynamo) |
| NVIDIA / ai-dynamo maintainers | NVIDIA Inference Xfer Library (NIXL) | 2026 | Prefill–Decode 与传输 | NIXL 为分布式推理提供统一的点到点数据传输抽象，在 HBM、DRAM、SSD 和对象存储之间选择 UCX、GPUDirect Storage 等后端。 | [primary](https://github.com/ai-dynamo/nixl) |
| Novita AI + vLLM | PegaFlow External KV Cache | 2026 | KV Cache / Runtime / Scheduling | PegaFlow 作为 Rust standalone external KV cache service 通过 vLLM connector 接入，面向生产级外部 KV cache。 | [primary](https://vllm.ai/blog/2026-05-18-pegaflow) |
| AMD ROCm + vLLM | Productionizing TurboQuant on AMD GPUs | 2026 | Compiler / DSL / Runtime / Scheduling | 在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。 | [primary](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html) |
| Dell + NVIDIA + LMCache/vLLM | RDMA-Accelerated KV Cache Storage Offload | 2026 | KV Cache / Prefill–Decode 与传输 / Runtime / Scheduling | 将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。 | [primary](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/) |
| Alibaba Cloud Tair | Tair-KVCache-HiSim | 2026 | KV Cache | 面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。 | [primary](https://www.alibabacloud.com/blog/603164) |
| IBM / Red Hat / Google 等 | UCCL | 2026 | Prefill–Decode 与传输 | GPU 通信库，覆盖 collectives、P2P KV cache transfer、RL weight transfer 和 expert parallelism，进入 llm-d 分布式推理栈。 | [primary](https://github.com/uccl-project/uccl) |
| llm-d | llm-d KV Cache | 2026 | KV Cache / Runtime / Scheduling | 用 vLLM KVEvents 构建全局 near-real-time KV block locality 视图，支持跨 pod KV-aware routing 和 offloading。 | [primary](https://github.com/llm-d/llm-d-kv-cache) |
| vLLM Project maintainers | vLLM Production Stack | 2026 | Runtime / Scheduling | vLLM Production Stack 是面向 Kubernetes 的参考部署层，提供 Helm、服务发现、路由、可观测性和集群级运行入口。 | [primary](https://github.com/vllm-project/production-stack) |
| Moonshot / Mooncake / vLLM | vLLM x Mooncake Store | 2026 | Runtime / Scheduling | 将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。 | [primary](https://vllm.ai/blog/2026-05-06-mooncake-store) |
| vLLM maintainers / Inferact | vLLM 商业化 | 2026 | Runtime / Scheduling | vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。 | [primary](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/) |
| Ant Group + vLLM 社区 | vLLM-Omni | 2026 | Runtime / Scheduling | 用 stage graph 拆分 LLM、扩散模型和编码器，各阶段独立批处理、分配 GPU，并通过统一 connector 传递中间状态。 | [primary](https://arxiv.org/abs/2602.02204) |
| Ant Group + vLLM | vLLM-Omni runtime | 2026 | Runtime / Scheduling | 将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。 | [primary](https://github.com/vllm-project/vllm-omni) |
| NVIDIA / Linux Foundation ecosystem | UCX |  | Prefill–Decode 与传输 / Compiler / DSL | 统一 InfiniBand、RoCE、shared memory、CUDA memory 等传输，为 MPI、NCCL 和分布式 runtime 提供底层能力。 | [primary](https://github.com/openucx/ucx) |
| NVIDIA | CUTLASS / CuTe DSL | 2017 | Prefill–Decode 与传输 / MoE / Compiler / DSL | 提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives；4.4/4.5 系列继续补充 Blackwell GQA decode、int4 KV、MX/NVFP4 block-scaled GEMM 和 MoE grouped GEMM 示例。 | [primary](https://github.com/NVIDIA/cutlass) |
| NVIDIA | Triton Inference Server | 2018 | Compiler / DSL / Runtime / Scheduling | 负责模型仓库、dynamic batching、ensemble、metrics 和多框架后端，常作为 TensorRT-LLM/vLLM 外层生产服务面。 | [primary](https://github.com/triton-inference-server/server) |
| NVIDIA | FasterTransformer | 2020 | Compiler / DSL / Runtime / Scheduling | 用融合 CUDA kernel、GEMM 调优、量化和多 GPU 并行提供早期生产级 Transformer 推理库，后续能力并入 TensorRT-LLM。 | [primary](https://github.com/NVIDIA/FasterTransformer) |
| ByteDance | LightSeq | 2021 | Compiler / DSL | 通过 fused layer、定制 CUDA kernel 和显存复用部署 NLP 与生成模型。 | [primary](https://github.com/bytedance/lightseq) |
| Tsinghua University | FasterMoE | 2022 | MoE | 用 expert shadowing、smart scheduling 和 topology-aware communication 缓解动态路由不均。 | [primary](https://github.com/thu-pacman/FasterMoE) |
| BentoML | BentoML / BentoCloud | 2023 | Runtime / Scheduling | 统一模型容器、API、batching、资源声明和 autoscaling，并与 vLLM、SGLang、TensorRT-LLM 等 runtime 集成。 | [primary](https://docs.bentoml.com/) |
| Databricks / Stanford ecosystem | MegaBlocks | 2023 | MoE | 用 block-sparse operation 替代 capacity padding，为高效 MoE kernel 和 serving 提供基础。 | [primary](https://github.com/databricks/megablocks) |
| NVIDIA | TensorRT-LLM | 2023 | Runtime / Scheduling | 提供 inflight batching、paged KV、FP8/FP4、speculative decoding、TP/PP/EP 和多节点执行，是 NVIDIA 平台的产品级 LLM 引擎。 | [primary](https://github.com/NVIDIA/TensorRT-LLM) |
| Huawei Cloud + NUS + SJTU | CachedAttention | 2024 | KV Cache / Runtime / Scheduling | 用 DRAM/SSD 分层保存跨轮 KV，配合 layer-wise preload、异步保存和 scheduler-aware eviction 降低 TTFT。 | [primary](https://www.usenix.org/conference/atc24/technical-sessions) |
| Intel | Gaudi 2/3 software stack | 2024 | Runtime / Scheduling | 通过 SynapseAI、HCCL、FP8 和 vLLM/Optimum Habana 支持 LLM serving，以标准 Ethernet 和成本为差异点。 | [primary](https://docs.habana.ai/) |
| Apple / MLX community | MLX-LM / vllm-mlx | 2024 | Runtime / Scheduling | 利用 Apple silicon 统一内存和 MLX 图执行提供本地 LLM 推理，并开始向 continuous batching 和 vLLM API 兼容扩展。 | [primary](https://github.com/ml-explore/mlx-lm) |
| Together AI + Princeton 等 | Medusa | 2024 | Speculative Decoding | 在目标模型上增加多组 decoding heads，一次预测并验证多个未来 token；其思想已进入主流 serving runtime。 | [primary](https://arxiv.org/abs/2401.10774) |
| Ray / Anyscale | Ray Serve LLM | 2024 | Runtime / Scheduling | 将 vLLM 等 engine 包装为 Ray actor/deployment，提供多节点 replica、路由、autoscaling 和 Python 应用编排。 | [primary](https://docs.ray.io/en/latest/serve/llm/index.html) |
| NVIDIA | TensorRT-LLM FP8/INT8 KV cache | 2024 | KV Cache / Prefill–Decode 与传输 / Runtime / Scheduling | MHA/MQA kernel 中支持 on-the-fly dequantize 的 FP8/INT8 KV cache，降低 decode 阶段读带宽。 | [primary](https://nvidia.github.io/TensorRT-LLM/advanced/gpt-attention.html) |
| NVIDIA | TensorRT-LLM Speculative Decoding | 2024 | Speculative Decoding / Runtime / Scheduling | 在产品级 runtime 中集成 draft-target、Medusa、EAGLE 等推测策略，并与 inflight batching、量化和并行执行组合。 | [primary](https://nvidia.github.io/TensorRT-LLM/advanced/speculative-decoding.html) |
| OpenAI / Triton ecosystem | Triton language and kernels in inference stacks | 2024 | Prefill–Decode 与传输 / MoE / Compiler / DSL / Runtime / Scheduling | 工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。 | [primary](https://triton-lang.org/) |
| Baseten | Truss / TensorRT-LLM serving stack | 2024 | Runtime / Scheduling | 把容器构建、模型打包、TensorRT-LLM 优化、流量伸缩和可观测性组合为生产推理平台。 | [primary](https://docs.baseten.co/) |
| Alibaba Cloud | COMET | 2025 | MoE | 细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html) |
| Microsoft Research | LeanAttention / TurboAttention | 2025 | Attention / Kernel / Prefill–Decode 与传输 | 分别从精确 decode dataflow 和端到端量化 attention 两条路线降低长上下文 memory wall。 | [primary](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html) |
| Google TPU ecosystem | Gemma 4 on vLLM-TPU | 2026 | Runtime / Scheduling | 展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。 | [primary](https://arxiv.org/abs/2605.25645) |

## 探索观察

最近 180 天内最多展示 20 个有系统证据的新语境项目。

| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |
|---|---|---:|---|---|---|
|  | OpenVINO Model Server 2025.4 | 2025 | 探索观察 | 官方发布记录。 | [primary](https://github.com/openvinotoolkit/model_server/releases/tag/v2025.4) |
|  | AITER v0.1.16.post5 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/ROCm/aiter/releases/tag/v0.1.16.post5) |
|  | Dynamo v1.4.0-kimi-k3-dev.1 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/ai-dynamo/dynamo/releases/tag/v1.4.0-kimi-k3-dev.1) |
|  | KTransformers v0.6.4 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/kvcache-ai/ktransformers/releases/tag/v0.6.4) |
| Google / TPU ecosystem | Ragged Paged Attention for TPU | 2026 | 探索观察 | 面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。 | [primary](https://arxiv.org/abs/2604.15464) |
|  | Ray-2.55.0 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/ray-project/ray/releases/tag/ray-2.55.0) |
|  | Release v0.6.16 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.6.16) |
| Microsoft Research | SPIN | 2026 | 探索观察 | 把 sparse attention execution pipeline 与 CPU/GPU hierarchical KV storage 联合设计，解决不规则 KV subset 检索开销。 | [primary](https://www.microsoft.com/en-us/research/publication/unifying-sparse-attention-with-hierarchical-memory-for-scalable-long-context-llm-serving/) |
|  | ciflow/trunk/776ba0ccd00c619c20a6bcb27181815e4a90cb8e: Record LLM model execution latency (#21040) | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/pytorch/executorch/releases/tag/ciflow%2Ftrunk%2F776ba0ccd00c619c20a6bcb27181815e4a90cb8e) |
|  | v0.14.0 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/InternLM/lmdeploy/releases/tag/v0.14.0) |
|  | v0.26.dev0: [Refactor] Update TVM runtime integration (#3501) | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/mlc-ai/mlc-llm/releases/tag/v0.26.dev0) |
|  | v0.5.2 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/LMCache/LMCache/releases/tag/v0.5.2) |
|  | v1.2.1-dev: feat(inference): add Meta AI remote inference provider (#6275) | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/ogx-ai/ogx/releases/tag/v1.2.1-dev) |
|  | v1.95.0-dev.1 | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/BerriAI/litellm/releases/tag/v1.95.0-dev.1) |
|  | v2.17: Disable cuDNN 9.23.0/9.23.1 for MXFP8 attention (#3173) | 2026 | 探索观察 | 官方发布记录。 | [primary](https://github.com/NVIDIA/TransformerEngine/releases/tag/v2.17) |
