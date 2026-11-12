# Alibaba Group / Qwen

**A compact map of Alibaba's public AI-system work:** Qwen models → inference/serving → agent harnesses → training/RL → edge runtimes and the chip/cloud substrate.

[← Organizations](README.md) · [← Home](../README.md) · [Detailed source audit and evidence boundaries](../reviews/ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md)

## 1. The technology map

| Layer | Main work | What to understand |
|---|---|---|
| **Models** | [Qwen3.5–3.8](https://github.com/QwenLM/Qwen3.8) · [Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) · [Qwen4-Max Preview](https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview) | Hybrid GDN/attention, QSA, MoE, multimodal and long-context execution contracts. |
| **Inference engines** | [RTP-LLM](https://github.com/alibaba/rtp-llm) · **BladeLLM** ([PAI docs](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/)) | Two distinct Alibaba engines; only RTP-LLM has a public engine repository. |
| **Serving / KV** | [InferX](https://www.alibabacloud.com/help/en/pai/inferx-overview) · [FlashKV](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache) · [Tair KVCache](https://github.com/alibaba/tair-kvcache) | Routing, shared multi-tier KV, global metadata management and trace simulation. |
| **Systems research** | [LMetric](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) · [ServeGen](https://github.com/alibaba/ServeGen) · [EPIC](https://doi.org/10.1145/3789240.3829201) · [RollArt](https://www.usenix.org/conference/osdi26/presentation/gao) · [MCP Gateway](https://atc.sigops.org/2026/accepted.html) | Request routing, production workloads, MoE communication, agentic RL and tool-access infrastructure. |
| **Agent stack** | [AgentScope 2.0](https://github.com/agentscope-ai/agentscope) · [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) · [Mobile-Agent / GUI-Owl](https://github.com/X-PLUG/MobileAgent) · [ToolCUA](https://github.com/X-PLUG/ToolCUA) · [AgentCore](https://www.alibabacloud.com/help/en/agentcore/agentcore-product-overview) | Agent harness, tool use/planning, GUI agents, enterprise lifecycle management. |
| **Training / RL** | [PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch) · [ChatLearn](https://github.com/alibaba/ChatLearn) · [ROLL](https://github.com/alibaba/ROLL) · [ROCK](https://github.com/alibaba/ROCK) · [ms-swift](https://github.com/modelscope/ms-swift) | Pretraining, post-training, distributed rollout, agent environments and fine-tuning. |
| **Compiler / kernels** | [BladeDISC](https://github.com/alibaba/BladeDISC) · [EasyDist](https://github.com/alibaba/easydist) · [AAAI KV prefetch](https://github.com/alibaba/vllm_xformers_prefetch) | Dynamic-shape compilation, parallelization, memory/compute overlap; EPIC covers MoE communication. |
| **Edge inference** | [MNN](https://github.com/alibaba/MNN) · [MNN-Pocket](https://arxiv.org/abs/2611.12311) · [Walle](https://www.usenix.org/conference/osdi22/presentation/lv) | Cross-platform on-device LLM inference and device-cloud execution. |
| **Chip / cloud substrate** | [Zhenwu V900 and AI roadmap](https://www.alibabagroup.com/en-US/document-2041268239081668608) · [Agentic Cloud](https://www.alibabacloud.com/blog/603589) | AI accelerator, supernode/network/storage, AI-native and agent-native cloud services. |

**Fast orientation:** Alibaba's public work spans the full stack, not only Qwen. Keep the open-source engine RTP-LLM separate from PAI's BladeLLM; distinguish the Tair codebase from the FlashKV managed service; and separate online inference research from agent harnesses, RL training, edge runtimes and cloud products. The newest additions worth noticing are Qwen4-Max Preview, AgentScope 2.0, GUI-Owl/ToolCUA, RollArt and the 2026 Agentic Cloud roadmap.

## 2. Qwen: model architecture that changes execution

- [Qwen official repositories](https://github.com/QwenLM) are the entry point for model implementations and open weights. Qwen3 includes dense and MoE variants, reasoning modes, coding and multimodal families.
- [Qwen3-Next / Qwen3.5–3.8](https://github.com/QwenLM/Qwen3.8) develops a hybrid **Gated DeltaNet (GDN) recurrent state + attention** architecture. This creates two different state-management paths: recurrent state and conventional attention KV.
- [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) is the most useful current architecture preview: **GDN + Qwen Sparse Attention (QSA)**, Gated Residual, N-gram Embedding and asynchronous host-memory prefetch. It is explicitly a preview of the architecture direction for Qwen4, **not the Qwen4 release itself**.
- [Qwen3.8-Max and Qwen3.8-Omni](https://github.com/QwenLM/Qwen3.8) extend the current flagship and multimodal families; the [Model Studio catalog](https://www.alibabacloud.com/help/en/model-studio/models) is the current API-family inventory.
- **[Qwen-AgentWorld-35B-A3B](https://github.com/QwenLM/Qwen-AgentWorld)** (June 2026) is a language world model for simulating agent environments across MCP, Search, Terminal, SWE, Android, Web and OS; [AgentWorldBench](https://huggingface.co/datasets/Qwen/AgentWorldBench) provides paired real-environment observations. This is agent training/evaluation infrastructure, not a serving engine.
- **Qwen4-Max-Preview (Nov 11, 2026)** is now available through Model Studio Token Plan: 1M context, image/video understanding, deep reasoning and tool calling. It is a time-limited preview (Nov 11–25), not an open-weight family release; the other Qwen4 variants and final architecture remain separate release questions. [Official model documentation](https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview).
- Alibaba's [September 2026 roadmap](https://www.alibabagroup.com/en-US/document-2041268239081668608) also names Qwen4.5 and Qwen5 as future generations, with a stated scale ambition up to 5–10T parameters. Treat this as a roadmap, not a released architecture or available checkpoint.
- [Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder), [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) and [Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) matter because long coding sessions and streaming multimodal inputs create different serving workloads from ordinary text chat.
- Historical context: [M6](https://arxiv.org/abs/2103.00823) and [OFA](https://proceedings.mlr.press/v162/wang22al.html) are earlier DAMO multimodal/pretraining work; useful lineage, but not today's online inference runtime.

**Read:** model repository → model card / technical report → the actual runtime implementation supporting that architecture. A model release is not, by itself, a serving-system contribution.

## 3. Inference engines and the PAI platform

### RTP-LLM — open-source production inference engine

[Code](https://github.com/alibaba/rtp-llm) · [Documentation](https://rtp-llm.ai/) · [May 2026 report](https://arxiv.org/abs/2605.29639) · [October 2026 engineering report](https://arxiv.org/abs/2611.00967)

Developed by Alibaba's Foundation Model Inference Team. The repository describes a C++ scheduling/batching runtime with KV management, quantization, multi-LoRA, speculative decoding, distributed execution and multimodal support. The 2026 reports discuss model loading, P/D disaggregation, multi-tier KV reuse and how a shared engine evolves across many models.

**Reading focus:** trace request lifecycle, scheduler, KV allocation/reuse, P/D transfer and backend dispatch in the code. The May and October reports describe the **same evolving engine**, not two independent systems.

### BladeLLM — PAI's in-house inference engine

[PAI deployment guide](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/) · [PAI acceleration overview](https://www.alibabacloud.com/help/en/pai/ai-acceleration-1/) · [Qwen2.5-1M technical report](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf)

PAI describes BladeLLM as its high-performance LLM inference engine, with model-specific optimization, quantization, batching, GPU-memory management and asynchronous/distributed execution. The Qwen2.5-1M report says its API service is powered by BladeLLM and discusses long-sequence prefill/decode optimizations.

**Boundary:** BladeLLM is distinct from RTP-LLM. The public evidence used here is product documentation and technical reports; no public BladeLLM engine repository was identified. Do not infer source-level behavior from the product description.

### PAI deployment and managed serving

- [PAI-EAS LLM deployment](https://www.alibabacloud.com/help/en/pai/deploy-an-llm/) is the managed deployment/service layer. It can expose different engines, including vLLM, SGLang and BladeLLM.
- [InferX](https://www.alibabacloud.com/help/en/pai/inferx-overview) documents inference orchestration such as routing, P/D coordination, cache-aware scheduling and model warm-up.

Keep the **engine**, **deployment platform** and **managed cache service** as separate layers.

## 4. KV infrastructure: Tair KVCache and FlashKV

### Tair KVCache — open-source global cache management and simulation

[Repository](https://github.com/alibaba/tair-kvcache) · [Architecture guide](https://github.com/alibaba/tair-kvcache/blob/main/docs/design/module_architecture.md) · [Chinese README](https://github.com/alibaba/tair-kvcache/blob/main/README_zh.md)

Two components are especially useful:

- **Tair KVCache Manager (KVCM):** a global metadata manager. It supports prefix / sliding-window / hybrid-attention matching, cache-location indexing, two-phase writes, capacity control, eviction, garbage collection and tier migration.
- **Tair KVCache HiSim:** a CPU-based inference simulator that replays workload traces to estimate TTFT, TPOT and throughput without occupying GPUs.

The key architectural idea is the separation of **metadata plane** (where is a cache entry, and is it readable?) from **data plane** (the engine transfers KV payloads directly to/from storage). Connectors are documented for vLLM, SGLang, RTP-LLM and TRT-LLM.

### FlashKV — PAI's managed cluster-wide KV cache service

[Official documentation](https://www.alibabacloud.com/help/en/pai/inferx-kv-cache)

FlashKV shares prefix KV across service replicas and uses memory, disk and remote-storage tiers. It is a cache service used alongside an inference engine, **not an inference engine itself**.

**Do not conflate them:** Tair KVCache is a public codebase with KVCM and HiSim; FlashKV is documented as a PAI managed service. The sources reviewed here do not establish that both expose the same implementation.

## 5. Production LLM systems research

These works reveal how Alibaba studies real serving systems beyond model architecture.

| Work | Venue | Main question | Entry point |
|---|---|---|---|
| **LMetric / Simple Is Better** | OSDI 2026 | Combine KV reuse opportunity and instance load for request routing without a tuned linear weight. | [Paper](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) |
| **ServeGen** | NSDI 2026 | Generate realistic online workloads from billions of production requests across 12 models. | [Paper](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) · [code and traces](https://github.com/alibaba/ServeGen) |
| **ACDC / Batched in Back** | SOSP 2026 | Characterize and optimize offline batch inference; a different problem from online TTFT/TPOT serving. | [Paper](https://doi.org/10.1145/3830418.3843877) · [offline traces](https://github.com/alibaba/ServeGen/tree/main/data/offline) |
| **Model-as-a-Service in the Wild (xMaaS)** | ATC 2026 | Analyze production LLM clusters, model/application diversity, GPU allocation and P/D imbalance. | [Paper and trace](https://github.com/alibaba/clusterdata/tree/master/cluster-trace-v2026-maas) |
| **StriaTrace** | OSDI 2026 | Low-overhead tracing and diagnosis for production LLM inference anomalies. | [Paper](https://www.usenix.org/conference/osdi26/presentation/wu-haonan) |
| **EPIC / Balancing and Beyond** | SIGCOMM 2026 | MoE Expert Parallelism: balance expert compute and NIC traffic, adapt transport to topology, and overlap communication. | [Paper DOI](https://doi.org/10.1145/3789240.3829201) · [accepted-paper list](https://conferences.sigcomm.org/sigcomm/2026/accepted/) |
| **Chorus** | ATC 2026 | GPU–CPU cooperative serving for length-skewed decode. | [Accepted paper](https://atc.sigops.org/2026/accepted.html) |
| **CacheFS** | ATC 2026 | Peer-to-peer cooperative caching for model-weight distribution; **weight cache, not KV cache**. | [Accepted paper](https://atc.sigops.org/2026/accepted.html) |
| **Axon** | ATC 2026 | Asynchronous global KV-aware scheduling across instances for agentic workloads. | [Accepted paper](https://atc.sigops.org/2026/accepted.html) |
| **Asynchronous KV Cache Prefetching** | AAAI 2026 | Overlap attention compute with Hopper L2 prefetch to hide KV memory latency. | [Paper](https://doi.org/10.1609/aaai.v40i25.39224) · [code](https://github.com/alibaba/vllm_xformers_prefetch) |
| **Scaling LLM Agent Tool Access: The MCP Gateway** | ATC 2026 | Manage and scale tool access for LLM agents; adjacent to serving infrastructure rather than a model execution engine. | [Accepted paper and authors](https://atc.sigops.org/2026/accepted.html) |

**How to read the list:** LMetric is request routing; ServeGen/ACDC/xMaaS are workload and production evidence; EPIC is MoE communication; Chorus is CPU–GPU decode cooperation; CacheFS is weight distribution; Axon is distributed KV-aware scheduling; StriaTrace is observability. They solve different layers and should not be collapsed into one “Alibaba inference engine”.

The AAAI prefetch paper is already in our canonical [KV Cache & Context Memory](../topics/kv-cache-memory.md) list. LMetric, ServeGen, ACDC, xMaaS and StriaTrace are also already indexed. **EPIC, Chorus, CacheFS and Axon are conference-accepted papers but still require our strict source/method/artifact review before canonical admission.**

[Heterogeneity at Hyperscale (OSDI 2026)](https://www.usenix.org/conference/osdi26/presentation/li-suyi) is another useful adjacent work on heterogeneous GPU-cluster resource management; it is cluster scheduling, not an LLM request scheduler.

## 6. Agent frameworks, GUI agents and enterprise harness

- **[AgentScope 2.0](https://github.com/agentscope-ai/agentscope)** — Tongyi Lab's open-source agent framework, repositioned as a general-purpose **Agent Harness** in the Nov 11, 2026 [first-party article](https://www.alibabacloud.com/blog/from-agent-framework-to-agent-harness-a-new-positioning-for-the-open-source-agentscope-project_603759). Focus: long-horizon task orchestration, tool execution, service-side coordination and isolated sandbox execution.
- **[AgentScope Java 2.0](https://github.com/agentscope-ai/agentscope-java)** — Java counterpart for distributed enterprise agents, with event streaming, permissions, workspace/sandbox, multi-agent orchestration and production deployment. The Python and Java repositories are distinct implementations under the AgentScope ecosystem.
- **[Spring AI Alibaba](https://github.com/alibaba/spring-ai-alibaba)** — Alibaba's Java agent framework and graph runtime, with workflow orchestration, context engineering, HITL, MCP/A2A and an Admin platform for visual development/observability. Treat it as an enterprise application framework, not an LLM inference engine.
- **[Qwen-Agent](https://github.com/QwenLM/Qwen-Agent)** — Qwen's tool-use, planning and RAG application framework; includes the [DeepPlanning benchmark](https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/). It is an application/agent framework, not the RTP-LLM engine.
- **[Mobile-Agent / GUI-Owl 1.5](https://github.com/X-PLUG/MobileAgent)** — Tongyi Lab's cross-platform GUI agent line for desktop, mobile and browser interaction; [GUI-Owl 1.5 report](https://arxiv.org/abs/2602.16855). **[ToolCUA](https://github.com/X-PLUG/ToolCUA)** (May 2026) adds GUI/tool path selection with trajectory synthesis and online Agentic RL; [paper](https://arxiv.org/abs/2605.12481). [UI-S1](https://arxiv.org/abs/2509.11543) was accepted to ACL 2026 main.
- **[AgentCore](https://www.alibabacloud.com/help/en/agentcore/agentcore-product-overview)** — Alibaba Cloud's managed agent build/run/governance platform; [Agent Security Center](https://www.alibabacloud.com/help/en/asc/product-overview/what-is-the-agent-security-center) covers lifecycle security and compliance. These are product services, not public agent-runtime source.
- **[Agent Context / Context Engine](https://www.alibabagroup.com/en-US/document-2041268239081668608)** — enterprise context and long-term memory service in Alibaba Cloud's 2026 full-stack roadmap.

## 7. Edge, training, RL and developer ecosystem

**Qwen4 release watch (Nov 9):** A verified first-party Qwen4 general-availability/weight-card release has **not been established**. The publicly inspectable [Qwen3.8-Flash-Next experimental architecture](https://github.com/QwenLM/Qwen3.8-Flash-Next) provides a **Gated DeltaNet + QSA indexer/offload** inference signal, but does not license a claim of published Qwen4 final weights, model IDs or compatibility. Recheck source identities on a real Qwen4 announcement.

- **[MNN](https://github.com/alibaba/MNN) / [MNN-LLM](https://github.com/alibaba/MNN/tree/master/transformers):** cross-platform inference runtime for mobile, PC and IoT. [Walle (OSDI 2022)](https://www.usenix.org/conference/osdi22/presentation/lv) is the earlier device-cloud collaborative ML system built around MNN.
- **[MNN-Pocket-0.3B](https://arxiv.org/abs/2611.12311):** Nov 2026 mobile-native model/runtime co-design; 32K context and INT4 package. Keep its phone throughput separate from cloud-serving measurements.
- **[PAI-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch):** Alibaba Cloud's Megatron-based LLM/VLM pretraining, SFT, RL and checkpoint-conversion toolkit.
- **[ChatLearn](https://github.com/alibaba/ChatLearn):** distributed alignment/RL orchestration, integrating Megatron/FSDP training with vLLM/SGLang rollout.
- **[ROLL](https://github.com/alibaba/ROLL) + [ROCK](https://github.com/alibaba/ROCK):** ROLL is a multi-role distributed RL training library; ROCK manages isolated, scalable environments for agentic RL.
- **[Let It Flow: Agentic Crafting on Rock and Roll](https://arxiv.org/abs/2512.24873)** (technical report) presents the Agentic Learning Ecosystem (ALE): ROLL for post-training, ROCK for environment management, iFlow CLI for agent execution, and the ROME agentic model trained on interaction trajectories. Keep it as an ecosystem report, distinct from the OSDI RollArt systems paper.
- **RollArt (OSDI 2026):** disaggregates multi-task agentic RL across compute-optimized GPUs, bandwidth-optimized GPUs, CPU environments and serverless reward evaluation. The authors report 1.31–2.05× training-time reduction and a 3,000+ GPU Alibaba deployment. [Paper](https://www.usenix.org/conference/osdi26/presentation/gao). This is **RL training infrastructure**, not online inference serving.
- **[ms-swift](https://github.com/modelscope/ms-swift):** ModelScope community's broad training/fine-tuning, RL, inference, evaluation, quantization and deployment toolkit. It is an ecosystem project, not an Alibaba-only inference engine.
- **[EasyDist](https://github.com/alibaba/easydist) + [BladeDISC](https://github.com/alibaba/BladeDISC):** supporting parallelization and compiler lines; useful infrastructure context, but not current standalone LLM serving engines.

## 8. Full-stack AI infrastructure roadmap

Alibaba's September 2026 Apsara roadmap connects four layers:

- **Compute:** T-Head's [Zhenwu V900](https://www.alibabagroup.com/en-US/document-2041268239081668608) AI training/inference accelerator and the Yitian CPU roadmap; V900 was announced with FP8/FP4 support and Q1 2027 commercial target. Treat these as roadmap/product claims, not an available public software stack or independently benchmarked result.
- **AI Native Cloud:** PAI for model training/inference, plus CPFS and high-performance networking as data and cluster substrate.
- **Agent Native Cloud:** [AgentCore](https://www.alibabacloud.com/help/en/agentcore/agentcore-product-overview) and Agent Security Center for agent build/run/governance/security.
- **Context Engine:** Agent Context and OpenLake for enterprise context, memory and multimodal data access.

The same announcement reports Qwen3.8-Max iterative optimization experiments (33 automated cycles). This is a useful **RSI-on-model-development** signal, but it is not evidence of recursive self-improvement inside an inference engine. [Full-stack announcement](https://www.alibabagroup.com/en-US/document-2041268239081668608).


## 9. Suggested overview order

1. **Model and architecture:** [Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) and the [Qwen4-Max preview docs](https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview).
2. **Inference and serving:** RTP-LLM, BladeLLM, InferX, FlashKV and Tair KVCache.
3. **Production systems research:** LMetric, ServeGen, ACDC, xMaaS, EPIC and StriaTrace.
4. **Agent stack:** AgentScope 2.0, Qwen-Agent, GUI-Owl/ToolCUA and AgentCore.
5. **Training and RL:** PAI-Megatron-Patch, ChatLearn, ROLL/RollArt and ROCK.
6. **Adjacent infrastructure:** MNN, BladeDISC/EasyDist and the T-Head/Agentic Cloud roadmap.

**Evidence boundary:** first-party code, co-authored papers, product documentation and author-reported benchmarks are labeled separately in the [detailed audit](../reviews/ALIBABA_PRIMARY_SOURCE_AUDIT_20261112.md). A product description is not source-code evidence; an accepted paper is not automatically a canonical admission; author-reported performance is not independent reproduction.
