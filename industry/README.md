# Industry & Open-Source Inference Systems

<!-- generated from data/papers.jsonl and data/industry.jsonl; do not edit directly -->

[Home](../README.md) · [System taxonomy](../ai-infra-system-abstractions.md) · [Academic papers](../papers/README.md)

A complete collection of production systems, open-source runtimes, infrastructure projects, and engineering material, with artifact and ecosystem signals where available.

![AI inference system map](../figs/ai-inference-system-map.png)

> **How to read this page.** Start with the featured entry points, then read foundation and frontier work before supporting records. Adjacent and archived material is kept in the [archive](../archive/README.md).

## At a Glance

| Records | Industrial material | With artifact | Tagged records |
|---:|---:|---:|---:|
| 90 | 90 | 90 | 89 |

## Collection Navigation

- [KV State & Memory](#kv-state-memory) (23)
- [P/D Disaggregation & KV Transfer](#p-d-disaggregation-kv-transfer) (10)
- [KV Compression & Low-Bit State](#kv-compression-low-bit-state) (15)
- [Kernel & Compiler](#kernel-compiler) (27)
- [Runtime & Serving](#runtime-serving) (13)
- [Reliability & Benchmarks](#reliability-benchmarks) (2)

## Evidence and Selection

Evidence labels describe the source material. Featured entries are editorial entry points, not a publication-quality ranking.

| Field | Reading rule |
|---|---|
| Venue / channel | What kind of source it is, not a quality score. |
| Technical tags | Searchable system surface; tags may be incomplete for legacy imports. |
| Artifact | A linked implementation, documentation page, or deployment entry point. |
| Curation priority | Foundation and frontier work appear first within each abstraction; supporting records follow. |
| Scope | Only `core` records are shown here; adjacent/archive material is in the archive page. |
| Featured | A small editorial starting set; all core records remain below. |

## Resource List

### KV State & Memory (23)

KV blocks, prefix state, offload, external memory, and memory-aware serving.

#### Featured

- **Featured:** **[SGLang 商业化](https://github.com/sgl-project/sglang)**
  `SGLang maintainers / RadixArk` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `sglang`
  围绕 RadixAttention、KV 复用和结构化生成提供企业化支持，显示 KV-aware runtime 正成为可独立商业化的软件层。
- **Featured:** **[vLLM V1 + torch.compile](https://pytorch.org/projects/vllm/)**
  `PyTorch Foundation / vLLM community` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `vllm`
  vLLM 作为 PyTorch Foundation 项目，集成 torch.compile、PagedAttention、prefix caching、chunked prefill 等。
- **Featured:** **[Dynamo KVBM](https://docs.dynamo.nvidia.com/dynamo/components/kvbm)**
  `NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `memory` `tensorrt-llm` `vllm`
  KVBM 作为统一 KV block memory layer，支持 vLLM/TensorRT-LLM 的远端共享、offload 和 write-through cache。
- **Featured:** **[Mooncake](https://www.usenix.org/conference/fast25/presentation/qin)**
  `Moonshot AI + Tsinghua` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving`
  以 KVCache 为中心做分离式 LLM serving 架构，面向长上下文在线服务。
- **Featured:** **[llm-d + LMCache + vLLM](https://research.ibm.com/publications/kv-cache-wins-you-can-feel-building-ai-aware-llm-routing-on-kubernetes)**
  `IBM / Red Hat / llm-d` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kubernetes` `llm-d`
  Kubernetes-native distributed LLM inference，把 vLLM、LMCache、Inference Gateway、KV-aware scheduling 组合起来。
#### Full Resource List

- **[DroidSpeak](https://www.microsoft.com/en-us/research/publication/droidspeak-kv-cache-sharing-for-efficient-multi-llm-serving/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `serving` `kv-cache` `agent`
  在相同架构的 fine-tuned model variants 之间共享 KV cache，降低企业多模型/多 agent 的重复 prefill。
- **[FlexKV](https://github.com/taco-project/FlexKV)**
  `Tencent Cloud TACO + NVIDIA` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `sglang` `vllm`
  分布式 KV store 和 multi-level cache manager，已进入 vLLM/Dynamo 生态，支持 TRT-LLM/SGLang/vLLM 的 KV offload。
- **[KV Offloading Connector](https://vllm.ai/blog/kv-offloading-connector)**
  `vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `vllm`
  vLLM 新 KV offloading connector 将 GPU cache block 迁移到外部存储/后端，提高长上下文和多轮复用能力。
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
- **[SPIN](https://www.microsoft.com/en-us/research/publication/unifying-sparse-attention-with-hierarchical-memory-for-scalable-long-context-llm-serving/)**
  `Microsoft Research` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `rag`
  把 sparse attention execution pipeline 与 CPU/GPU hierarchical KV storage 联合设计，解决不规则 KV subset 检索开销。
- **[Tair-KVCache-HiSim](https://www.alibabacloud.com/blog/603164)**
  `Alibaba Cloud Tair` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache`
  面向分布式多层 KV cache 管理的高精度仿真分析工具，辅助设计 cache 策略。
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
- **[Context Parallelism for Million-Token Inference](https://proceedings.mlsys.org/paper_files/paper/2025/hash/78834433edc3291f4c6cbbd2759324db-Abstract-Conference.html)**
  `Meta` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill`
  用 pass-KV/pass-Q 精确 ring attention 在常见数据中心网络上扩展百万 token prefill。
- **[InfiniStore](https://github.com/bytedance/InfiniStore)**
  `ByteDance` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `lmcache` `vllm`
  高性能分布式 KV cache store，支持 PD 分离中的 KV transfer、非分离集群的跨节点 KV reuse，并通过 LMCache 集成 vLLM。
- **[KV Cache Offloading](https://kserve.github.io/website/docs/model-serving/generative-inference/kvcache-offloading)**
  `KServe` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `kserve` `kubernetes`
  在 KServe generative inference 中集成 LMCache/vLLM KV offloading，面向云原生模型服务。
- **[Online Scheduling with KV Cache Constraints](https://www.microsoft.com/en-us/research/publication/online-scheduling-for-llm-inference-with-kv-cache-constraints/)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `memory`
  将 KV cache memory constraint 纳入在线 batching/scheduling 理论模型，提供与 hindsight optimal 对比的调度算法。
- **[TensorRT-LLM KV cache reuse](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/)**
  `NVIDIA` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `routing` `kv-cache` `tensorrt-llm`
  用 KV cache event API 和 KV-aware routing 提高 prefix/cache 命中，减少重复 prefill。
- **[CachedAttention](https://www.usenix.org/conference/atc24/technical-sessions)**
  `Huawei Cloud + NUS + SJTU` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kv-cache` `scheduler` `ttft`
  用 DRAM/SSD 分层保存跨轮 KV，配合 layer-wise preload、异步保存和 scheduler-aware eviction 降低 TTFT。
- **[JetStream + MaxText](https://cloud.google.com/tpu/docs/tutorials/LLM/jetstream-maxtext-inference-v6e)**
  `Google Cloud` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `tpu` `memory` `throughput`
  面向 XLA/TPU 的 throughput 和 memory optimized LLM inference engine，配合 MaxText 在 TPU/GKE 上服务 LLM。

### P/D Disaggregation & KV Transfer (10)

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

- **[Tutel](https://github.com/microsoft/tutel)**
  `Microsoft Research Asia` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel` `moe`
  提供自适应 expert parallel、all-to-all、fused kernel 和动态配置，是通用 MoE 软件栈的重要来源。
- **[RDMA-Accelerated KV Cache Storage Offload](https://infohub.delltechnologies.com/p/scaling-multi-turn-llm-inference-with-kv-cache-storage-offload-and-dell-rdma-accelerated-architecture/)**
  `Dell + NVIDIA + LMCache/vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `rdma` `kv-cache` `rag` `lmcache` `vllm`
  将 vLLM、LMCache、NVIDIA NIXL 和 Dell PowerScale/ObjectScale/Project Lightning 结合，做多轮推理的分层 KV offload。
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
- **[CUTLASS / CuTe DSL](https://github.com/NVIDIA/cutlass)**
  `NVIDIA` · `2017` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `blackwell` `moe`
  提供面向 Tensor Core 的可组合 GEMM、layout、pipeline 和 collective primitives；4.4/4.5 系列继续补充 Blackwell GQA decode、int4 KV、MX/NVFP4 block-scaled GEMM 和 MoE grouped GEMM 示例。
- **[NCCL](https://github.com/NVIDIA/nccl)**
  `NVIDIA` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `moe`
  提供 all-reduce、all-to-all、broadcast 等 GPU collective，是 TP、PP、EP 和 MoE 推理的默认通信层。

### KV Compression & Low-Bit State (15)

KV quantization, latent state, sparsity, and quality-cost tradeoffs.

#### Featured

- **Featured:** **[FlashMLA](https://github.com/deepseek-ai/FlashMLA)**
  `DeepSeek` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `gpu` `hopper` `kernel` `kv-cache`
  面向 MLA decode 的高性能 kernel，支持 paged KV cache、FP8 KV、Hopper/B200 等 GPU 优化。
#### Full Resource List

- **[vLLM V1](https://github.com/vllm-project/vllm)**
  `vLLM / PyTorch Foundation` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `prefill` `serving` `vllm`
  以 PagedAttention、continuous batching、chunked prefill、prefix caching、speculative decoding 和 torch.compile 形成事实上的开源 serving 基线。
- **[AITER: AI Tensor Engine for ROCm](https://github.com/ROCm/aiter)**
  `AMD / ROCm` · `2026` · `Industry / engineering material` · `Industrial Material`
  Tags: `serving` `amd` `rocm` `compiler` `kernel` `moe` `sglang` `vllm`
  AMD AITER (AI Tensor Engine for ROCm) provides C++/Python APIs and optimized Triton, Composable Kernel, and assembly operators for ROCm inference, including attention, MoE, GEMM, quantization, and communication kernels; it integrates with vLLM and SGLang.
- **[ATOM inference engine](https://rocm.blogs.amd.com/software-tools-optimization/atom-inference-engine/README.html)**
  `AMD ROCm` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `amd` `rocm` `kernel` `moe`
  以 ROCm-first 的独立推理引擎整合 AITER kernel、MoRI 通信、KV block/prefix cache、speculative decoding 与 TP/DP/EP 策略，面向 AMD Instinct 生产 serving。
- **[KVServe](https://arxiv.org/abs/2605.13734)**
  `KVServe Team` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `compression` `slo`
  在分离式 LLM serving 中根据 workload、网络和 SLO 在线选择 KV compression profile，面向通信瓶颈。
- **[Productionizing TurboQuant on AMD GPUs](https://rocm.blogs.amd.com/artificial-intelligence/turboquant-vllm-agentic/README.html)**
  `AMD ROCm + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `gpu` `kernel` `kv-cache` `agent` `vllm` `ttft`
  在 AMD GPU 上把 TurboQuant 的 KV cache 压缩做成 vLLM 可部署路径，并通过 Triton/HIP/FlyDSL kernel 优化提升长上下文 agent workload 的 TTFT、吞吐与 cache 命中。
- **[SAW-INT4](https://arxiv.org/abs/2604.19157)**
  `Apple / academic collaboration` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kv-cache` `quantization`
  面向真实 serving 约束设计 4-bit KV cache quantization，考虑 paged layout、规则访存和 fused attention。
- **[DeepGEMM / DeepEP](https://flashmla.net/)**
  `DeepSeek` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `moe`
  FP8 GEMM 与 MoE expert-parallel 通信库，支撑 DeepSeek 系列训练和推理的 dense/MoE fast path。
- **[Instinct MI350 Series](https://www.amd.com/en/products/accelerators/instinct/mi350.html)**
  `AMD` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `moe`
  CDNA 4 引入 FP4/FP6 并提供 288 GB HBM3E，面向大模型、MoE 和长上下文的高容量推理。
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

### Kernel & Compiler (27)

CUDA, Triton, HIP, attention, GEMM, MoE kernels, and compiler backends.

#### Featured

- **Featured:** **[FlashInfer](https://proceedings.mlsys.org/paper_files/paper/2025/file/dbf02b21d77409a2db30e56866a8ab3a-Paper-Conference.pdf)**
  `FlashInfer 社区` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `kernel`
  面向 LLM serving 的可定制 attention engine，支持 paged KV、decode/prefill kernel、与多 runtime 集成。
- **Featured:** **[FlashInfer production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)**
  `NVIDIA / University of Washington` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel` `sglang` `vllm`
  从论文发展为 vLLM、SGLang 等 runtime 共用的 attention/kernels 层，说明 kernel library 正成为独立基础设施层。
- **Featured:** **[FlexAttention for inference](https://pytorch.org/blog/flexattention-for-inference/)**
  `Meta / PyTorch` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  用 PyTorch API 表达 attention variants，经 torch.compile 降到 fused attention kernel，支持 inference/paged attention 方向。
- **Featured:** **[ROCm + vLLM/SGLang/TensorRT-LLM ecosystem](https://rocm.docs.amd.com/)**
  `AMD` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `gpu` `kernel` `sglang` `tensorrt-llm`
  通过 ROCm/HIP、Composable Kernel、Triton 和主流 runtime 支持 MI300/MI350 推理，核心竞争点是大 HBM 容量和开放集群。
#### Full Resource List

- **[FlashInfer kernel ecosystem](https://github.com/flashinfer-ai/flashinfer)**
  `FlashInfer community / NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `prefill` `kernel` `rag` `sglang` `vllm`
  针对 paged/ragged KV、decode、prefill、speculative tree 和 MLA 提供可组合 kernel，并集成 vLLM、SGLang 等 runtime。
- **[FlexAttention](https://pytorch.org/blog/flexattention/)**
  `PyTorch` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  允许用户用 score modification 和 block mask 表达 attention variant，再由编译器生成 fused kernel，覆盖 sparse/paged inference。
- **[torch.compile / Inductor](https://docs.pytorch.org/docs/stable/torch.compiler.html)**
  `PyTorch` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel` `vllm`
  捕获 PyTorch graph 并经 Inductor/Triton 生成 fused kernel，逐步进入 vLLM 和模型服务的默认优化路径。
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
- **[MI325X architecture-aware deployment study](https://arxiv.org/abs/2603.10031)**
  `AMD ROCm ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `amd` `rocm` `moe`
  说明 MLA、GQA、MoE 和视觉模型需要不同的 AITER、KV offload 与 block-size 配置，不能沿用统一参数。
- **[Ragged Paged Attention for TPU](https://arxiv.org/abs/2604.15464)**
  `Google / TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `tpu` `kernel` `rag`
  面向 TPU 的 ragged/paged LLM inference kernel，解决动态 batch、paged KV 和非规则序列形状。
- **[vLLM-Omni runtime](https://github.com/vllm-project/vllm-omni)**
  `Ant Group + vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `multimodal` `vllm`
  将 LLM、multimodal encoder、diffusion generator 组织成 stage graph，使文本与视觉生成共享 vLLM 风格的调度和部署接口。
- **[LeanAttention / TurboAttention](https://proceedings.mlsys.org/paper_files/paper/2025/hash/16ec6494e9b5a4138de7238761d715b4-Abstract-Conference.html)**
  `Microsoft Research` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `kernel` `memory`
  分别从精确 decode dataflow 和端到端量化 attention 两条路线降低长上下文 memory wall。
- **[TileLang](https://github.com/tile-ai/tilelang)**
  `Microsoft Research / community` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `kernel` `moe`
  将 tiled dataflow 与 layout、线程绑定、tensorization 和软件流水分离，降低编写高性能 attention/MoE kernel 的门槛。
- **[WaferLLM on Cerebras WSE-2](https://www.usenix.org/conference/osdi25/technical-sessions)**
  `Microsoft Research + University of Edinburgh` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  以 PLMR 模型、MeshGEMM/MeshGEMV 和 wafer-scale parallelism 将 LLM inference 映射到数十万片上 core。
- **[TT-Metalium / Wormhole](https://github.com/tenstorrent/tt-metal)**
  `Tenstorrent` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  公开低层 TT-Metalium 编程栈和模型实现，探索可编程 many-core 芯片上的 LLM 推理。
- **[TensorRT diffusion pipelines](https://developer.nvidia.com/tensorrt)**
  `NVIDIA` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel`
  通过 TensorRT、Model Optimizer 和定制 attention/GEMM kernel 加速 Stable Diffusion、Flux 和视频生成模型。
- **[Triton language and kernels in inference stacks](https://triton-lang.org/)**
  `OpenAI / Triton ecosystem` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `kernel` `moe` `sglang` `vllm`
  工业界大量自定义 decode/attention/MoE kernel 使用 Triton；与 torch.compile、vLLM、SGLang 形成底层优化生态。
- **[LightLLM](https://github.com/ModelTC/lightllm)**
  `ModelTC community` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel`
  用 token attention、动态 batch、共享显存管理和定制 Triton kernel 提供低开销分布式 LLM serving。
- **[MLC-LLM](https://github.com/mlc-ai/mlc-llm)**
  `MLC community` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `cuda` `gpu` `kernel`
  通过 Apache TVM/MLC 编译模型到 CUDA、ROCm、Metal、Vulkan、WebGPU 等后端，强调跨平台 kernel 生成和端侧部署。
- **[MegaBlocks](https://github.com/databricks/megablocks)**
  `Databricks / Stanford ecosystem` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kernel` `moe`
  用 block-sparse operation 替代 capacity padding，为高效 MoE kernel 和 serving 提供基础。
- **[DeepSpeed-Inference](https://www.deepspeed.ai/tutorials/inference-tutorial/)**
  `Microsoft` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `kernel` `memory`
  以 inference-adapted parallelism、kernel injection、量化和 heterogeneous memory 支撑超大 Transformer。
- **[LightSeq](https://github.com/bytedance/lightseq)**
  `ByteDance` · `2021` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `cuda` `kernel`
  通过 fused layer、定制 CUDA kernel 和显存复用部署 NLP 与生成模型。
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

### Runtime & Serving (13)

Runtime scheduling, agent graphs, structured generation, and SLO-aware dispatch.

#### Full Resource List

- **[DeepSpeed-MoE](https://arxiv.org/abs/2201.05596)**
  `Microsoft` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `moe`
  联合 expert parallel、通信优化和模型压缩，使稀疏大模型的推理成本可控。
- **[vLLM 商业化](https://techcrunch.com/2026/01/22/inference-startup-inferact-lands-150m-to-commercialize-vllm/)**
  `vLLM maintainers / Inferact` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `vllm`
  vLLM 创始团队成立公司推动生产支持，说明通用推理 runtime 已从学术开源项目演进为独立基础设施赛道。
- **[COMET](https://proceedings.mlsys.org/paper_files/paper/2025/hash/e27ea0cd50b798ff8942caf9203f0992-Abstract-Conference.html)**
  `Alibaba Cloud` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `gpu` `moe`
  细粒度重叠 expert communication 和 computation，论文报告已在万卡级生产集群节省数百万 GPU 小时。
- **[DeepSeek-V3.2 / DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556)**
  `DeepSeek` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `agent`
  在模型架构中加入 sparse attention/indexer，目标是在长上下文和 reasoning/agent 任务中降低推理成本。
- **[Scaling LLM inference: TP/CP/EP](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/)**
  `Meta` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  公开 Meta 在 tensor/context/expert parallelism 上扩展 LLM inference 的工程经验。
- **[XGrammar production integration](https://proceedings.mlsys.org/paper_files/paper/2025/hash/5c20ca4b0b20b0bd2f1d839dc605e70f-Abstract-Conference.html)**
  `MLC / SGLang / vLLM ecosystem` · `2025` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `decode` `gpu` `sglang` `vllm`
  将结构化生成从 Python parser 瓶颈下沉到预编译 grammar engine，并与 GPU decode overlap。
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
- **[Truss / TensorRT-LLM serving stack](https://docs.baseten.co/)**
  `Baseten` · `2024` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `tensorrt-llm`
  把容器构建、模型打包、TensorRT-LLM 优化、流量伸缩和可观测性组合为生产推理平台。
- **[BentoML / BentoCloud](https://docs.bentoml.com/)**
  `BentoML` · `2023` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `sglang` `tensorrt-llm`
  统一模型容器、API、batching、资源声明和 autoscaling，并与 vLLM、SGLang、TensorRT-LLM 等 runtime 集成。
- **[FasterMoE](https://github.com/thu-pacman/FasterMoE)**
  `Tsinghua University` · `2022` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `moe`
  用 expert shadowing、smart scheduling 和 topology-aware communication 缓解动态路由不均。

### Reliability & Benchmarks (2)

SLOs, drift, recovery, reproducibility, benchmarks, and graceful degradation.

#### Full Resource List

- **[Gemma 4 on vLLM-TPU](https://arxiv.org/abs/2605.25645)**
  `Google TPU ecosystem` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `gpu` `tpu` `vllm`
  展示 Gemma 从 JAX/Tunix 微调、Orbax checkpoint 转换到 vLLM-TPU serving 的可复现部署路径。
- **[vLLM x Mooncake Store](https://vllm.ai/blog/2026-05-06-mooncake-store)**
  `Moonshot / Mooncake / vLLM` · `2026` · `Industry / engineering material` · `Industrial Material · Legacy Import`
  Tags: `serving` `kv-cache` `agent` `vllm` `ttft`
  将 Mooncake distributed KV cache store 接入 vLLM，在 agentic traces 上提升吞吐、降低 TTFT 和端到端延迟。
