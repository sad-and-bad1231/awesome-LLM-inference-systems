# Core 论文作者单位与代码事实核验（2026-07-20）

范围：`status ∈ {verified, verified_legacy}` 且 `curation.scope = core`，共 241 篇。

判定口径：作者单位优先使用 Crossref 出版方元数据、arXiv 源文件/元数据与论文首页；代码只有在论文材料指向仓库且仓库内容能对应论文时才记为公开代码。根目录检测到许可证才记为 `open_source_confirmed`。`not_found_in_checked_sources` 仅表示本次核查的官方来源未发现代码，不能解读为作者没有发布代码。

## 结果

- 作者单位已核验：150；仍需人工核验：91。
- 公开代码且检测到许可证：54。
- 公开代码但根目录未检测到许可证：12。
- 已查来源未发现公开代码：175。
- 更正或补全历史单位字段：145 条。

## 逐条状态

| 论文 | 作者单位 | 代码 | 仓库 |
|---|---|---|---|
| 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| A First Look at Bugs in LLM Inference Serving Systems | `manual_needed` | `not_found_in_checked_sources` | — |
| A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints | `verified` | `not_found_in_checked_sources` | — |
| A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | `verified` | `open_source_confirmed` | [repo](https://github.com/sspec-project/SparseSpec) |
| AccelGen: Heterogeneous SLO-Guaranteed High-Throughput LLM Inference Serving for Diverse Applications | `manual_needed` | `not_found_in_checked_sources` | — |
| Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design | `manual_needed` | `not_found_in_checked_sources` | — |
| AdaCache: Adaptive Caching and Context Augmentation for Efficient LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping | `manual_needed` | `not_found_in_checked_sources` | — |
| AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving | `verified` | `not_found_in_checked_sources` | — |
| AdaServe: SLO-Customized LLM Serving with Fine-Grained Speculative Decoding | `manual_needed` | `not_found_in_checked_sources` | — |
| AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving | `verified` | `open_source_confirmed` | [repo](https://github.com/cerebellumking/AdaSpec) |
| Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market | `verified` | `not_found_in_checked_sources` | — |
| Agentix: An Efficient Serving Engine for LLM Agents as General Programs | `manual_needed` | `not_found_in_checked_sources` | — |
| Alibaba Stellar: A New Generation RDMA Network for Cloud AI | `verified` | `not_found_in_checked_sources` | — |
| AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor | `verified` | `not_found_in_checked_sources` | — |
| Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving | `verified` | `public_code_license_unverified` | [repo](https://github.com/eddiegaoo/Apt-Serve) |
| Attention Is All You Need for KV Cache in Diffusion LLMs | `verified` | `not_found_in_checked_sources` | — |
| AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE | `verified` | `open_source_confirmed` | [repo](https://github.com/Time-Rune/BEAM) |
| Beat the long tail: Distribution-Aware Speculative Decoding for RL Training | `verified` | `not_found_in_checked_sources` | — |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning | `verified` | `open_source_confirmed` | [repo](https://github.com/cmd2001/ICLR2026_KV-Embedding) |
| Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference | `verified` | `not_found_in_checked_sources` | — |
| Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation-Storage Awareness | `manual_needed` | `not_found_in_checked_sources` | — |
| Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning | `verified` | `not_found_in_checked_sources` | — |
| BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization | `verified` | `not_found_in_checked_sources` | — |
| Breaking the Ice: Analyzing Cold Start Latency in vLLM | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/upb-cn/vllm-startup-profiler) |
| BrownoutServe: SLO-Aware Inference Serving under Bursty Workloads for MoE-based LLMs | `verified` | `not_found_in_checked_sources` | — |
| Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration | `verified` | `not_found_in_checked_sources` | — |
| BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems | `verified` | `open_source_confirmed` | [repo](https://github.com/hpmll/burstgpt) |
| ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud | `verified` | `not_found_in_checked_sources` | — |
| Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/ngocbh/trimkv) |
| CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | `verified` | `not_found_in_checked_sources` | — |
| CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents | `verified` | `public_code_license_unverified` | [repo](https://github.com/cachewise-project/cachewise-coding-traces) |
| Can I Buy Your KV Cache? | `verified` | `not_found_in_checked_sources` | — |
| CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration | `verified` | `open_source_confirmed` | [repo](https://github.com/ElizaFuLan/CATS) |
| Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment | `verified` | `not_found_in_checked_sources` | — |
| Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments | `verified` | `not_found_in_checked_sources` | — |
| COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts | `verified` | `not_found_in_checked_sources` | — |
| Coordinated Scheduling for MoE LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution | `verified` | `not_found_in_checked_sources` | — |
| CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation | `verified` | `not_found_in_checked_sources` | — |
| CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving | `verified` | `public_code_license_unverified` | [repo](https://github.com/FastLM/CXL-SpecKV) |
| DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale | `verified` | `open_source_confirmed` | [repo](https://github.com/microsoft/DeepSpeed) |
| DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| DejaVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| DFVG: A Heterogeneous Architecture for Speculative Decoding with Draft-on-FPGA and Verify-on-GPU | `manual_needed` | `not_found_in_checked_sources` | — |
| Diff-MoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching | `verified` | `not_found_in_checked_sources` | — |
| DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/LLMServe/DistServe) |
| Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study | `verified` | `open_source_confirmed` | [repo](https://github.com/Analytics-Everywhere-Lab/edge-moe) |
| DriftBench: Measuring and Predicting Infrastructure Drift in LLM Serving Systems | `manual_needed` | `not_found_in_checked_sources` | — |
| DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants | `manual_needed` | `not_found_in_checked_sources` | — |
| DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving | `verified` | `open_source_confirmed` | [repo](https://github.com/ASISys/DualMap) |
| DuoServe-MoE: Dual-Phase Expert Prefetch and Cache Scheduling for Efficient MoE LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse | `verified` | `not_found_in_checked_sources` | — |
| ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs | `manual_needed` | `not_found_in_checked_sources` | — |
| Efficient LLM Serving for Agentic Workflows with Context-Aware State Management | `manual_needed` | `not_found_in_checked_sources` | — |
| Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/MLSysU/EcoServe) |
| Efficient Memory Management for Large Language Model Serving with PagedAttention | `verified` | `open_source_confirmed` | [repo](https://github.com/vllm-project/vllm) |
| Efficient Multi-round LLM Inference over Disaggregated Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts | `verified` | `open_source_confirmed` | [repo](https://github.com/furiosa-ai/EfficientRollout) |
| ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving | `verified` | `not_found_in_checked_sources` | — |
| Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs | `verified` | `not_found_in_checked_sources` | — |
| EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| FaaScale: Unlocking Fast LLM Scaling for Serverless Inference | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/lambda-scale/lambda-scale) |
| Fast MoE Inference via Predictive Prefetching and Expert Replication | `verified` | `not_found_in_checked_sources` | — |
| Fast State Restoration in LLM Serving with HCache | `verified` | `not_found_in_checked_sources` | — |
| Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | `verified` | `open_source_confirmed` | [repo](https://github.com/NVlabs/Fast-dLLM) |
| FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| FastTree: Optimizing Attention Kernel and Runtime for Tree-Structured LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| Fine-Tuning and Serving Gemma 4 31B on Google Cloud TPU: A Technical Comparison with GPU Baselines | `verified` | `not_found_in_checked_sources` | — |
| FlashAgents: Accelerating Multi-Agent LLM Systems via Streaming Prefill Overlap | `manual_needed` | `not_found_in_checked_sources` | — |
| FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision | `verified` | `not_found_in_checked_sources` | — |
| FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling | `manual_needed` | `not_found_in_checked_sources` | — |
| FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/flashinfer-ai/flashinfer) |
| Flashlight: PyTorch Compiler Extensions to Accelerate Attention Variants | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/bozhiyou/flashlight) |
| FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/NazmulTakbir/FlexiCache) |
| FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation | `manual_needed` | `not_found_in_checked_sources` | — |
| FlowKV: A Disaggregated Inference Framework with Low-Latency KV Cache Transfer and Load-Aware Scheduling | `manual_needed` | `not_found_in_checked_sources` | — |
| Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets | `verified` | `not_found_in_checked_sources` | — |
| FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error | `verified` | `not_found_in_checked_sources` | — |
| FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference | `verified` | `open_source_confirmed` | [repo](https://github.com/sjtu-zhao-lab/FreeKV) |
| From Tokens to Layers: Redefining Stall-Free Scheduling for LLM Serving with Layered Prefill | `manual_needed` | `not_found_in_checked_sources` | — |
| Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice | `verified` | `public_code_license_unverified` | [repo](https://github.com/Aurora-Kl/Geometry-Aware-Online-Scheduling) |
| GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/project-ghostserve/26mlsys-AE-GhostServe) |
| GreenLLM: SLO-Aware Dynamic Frequency Scaling for Energy-Efficient LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention | `verified` | `not_found_in_checked_sources` | — |
| HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators | `verified` | `not_found_in_checked_sources` | — |
| HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving | `verified` | `not_found_in_checked_sources` | — |
| HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval | `verified` | `not_found_in_checked_sources` | — |
| HydraInfer: Hybrid Disaggregated Scheduling for Multimodal Large Language Model Serving | `verified` | `not_found_in_checked_sources` | — |
| HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/LLMServe/hydraserve) |
| HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching | `verified` | `not_found_in_checked_sources` | — |
| I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention | `verified` | `not_found_in_checked_sources` | — |
| InfiniGen: Efficient Generative Inference of Large Language Models with Dynamic KV Cache Management | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/snu-comparch/infinigen) |
| Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache | `verified` | `not_found_in_checked_sources` | — |
| Information-Aware KV Cache Compression for Long Reasoning | `verified` | `not_found_in_checked_sources` | — |
| JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting | `manual_needed` | `not_found_in_checked_sources` | — |
| JITServe: SLO-aware LLM Serving with Imprecise Request Information | `verified` | `not_found_in_checked_sources` | — |
| Joint Encoding of KV-Cache Blocks for Scalable LLM Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/sef1/kv_fast_fusion) |
| Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost | `verified` | `open_source_confirmed` | [repo](https://github.com/Summer-Summer/Kitty) |
| KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models | `verified` | `not_found_in_checked_sources` | — |
| KV Cache Optimization Strategies for Scalable and Efficient LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| KV Cache Transform Coding for Compact Storage in LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing | `verified` | `open_source_confirmed` | [repo](https://github.com/Graph-COM/KVEraser) |
| KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving | `verified` | `open_source_confirmed` | [repo](https://github.com/hpdps-group/KVServe) |
| KVSwap: Disk-aware KV Cache Offloading for Long-Context On-device Inference | `verified` | `not_found_in_checked_sources` | — |
| LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training | `verified` | `open_source_confirmed` | [repo](https://github.com/Fizzmy/LAER-MoE-AE) |
| LeanAttention: Hardware-Aware Scalable Attention Mechanism for the Decode-Phase of Transformers | `manual_needed` | `not_found_in_checked_sources` | — |
| Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning | `verified` | `open_source_confirmed` | [repo](https://github.com/zhzihao/Learning-to-Draft) |
| LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems | `verified` | `public_code_license_unverified` | [repo](https://github.com/pejoule/LeMix) |
| LIA: A Single-GPU LLM Inference Acceleration with Layer Bypass and Adaptive Speculative Decoding | `manual_needed` | `not_found_in_checked_sources` | — |
| Libra: Effective yet Efficient Load Balancing for Large-scale MoE Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads | `verified` | `not_found_in_checked_sources` | — |
| LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| LLM Inference Serving: Survey of Recent Advances and Opportunities | `verified` | `not_found_in_checked_sources` | — |
| LLMServingSim 2.0: An Enhanced Simulator for LLM Serving Systems with Graph-Based Workloads | `manual_needed` | `not_found_in_checked_sources` | — |
| Llumnix: Dynamic Scheduling for Large Language Model Serving | `verified` | `open_source_confirmed` | [repo](https://github.com/AlibabaPAI/llumnix) |
| LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/SamsungLabs/LookaheadKV) |
| LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences | `verified` | `not_found_in_checked_sources` | — |
| LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/mit-han-lab/omniserve) |
| LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding | `verified` | `open_source_confirmed` | [repo](https://github.com/infini-ai-lab/magicdec) |
| MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/FasterDecoding/Medusa) |
| MegaBlocks: Efficient Sparse Training with Mixture-of-Experts | `manual_needed` | `not_found_in_checked_sources` | — |
| MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism | `verified` | `not_found_in_checked_sources` | — |
| MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool | `verified` | `not_found_in_checked_sources` | — |
| MiLo: Efficient Quantized MoE Inference with Mixture of Low-Rank Compensators | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/Supercomputing-System-AI-Lab/MiLo) |
| MiniPIC: Flexible Position-Independent Caching in <100LOC | `verified` | `not_found_in_checked_sources` | — |
| Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training | `verified` | `not_found_in_checked_sources` | — |
| Models Take Notes at Prefill: KV Cache Can Be Editable and Composable | `verified` | `not_found_in_checked_sources` | — |
| MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading | `verified` | `not_found_in_checked_sources` | — |
| MoEBlaze: Breaking the Memory Wall for Efficient MoE Training on Modern GPUs | `verified` | `not_found_in_checked_sources` | — |
| Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | `verified` | `public_code_license_unverified` | [repo](https://github.com/kvcache-ai/Mooncake) |
| MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing | `verified` | `not_found_in_checked_sources` | — |
| Multiplexed Heterogeneous LLM Serving via Stage-Aligned Parallelism | `verified` | `not_found_in_checked_sources` | — |
| MuxServe: Flexible Spatial-Temporal Multiplexing for Multiple LLM Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/hao-ai-lab/MuxServe) |
| NexSpec: Towards Optimizing Speculative Decoding in Reinforcement Learning Systems | `manual_needed` | `not_found_in_checked_sources` | — |
| Niyama: Breaking the Silos of LLM Inference Serving | `verified` | `not_found_in_checked_sources` | — |
| No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/shutianluo/DirectKV) |
| Not-a-Bandit: Provably No-Regret Drafter Selection in Speculative Decoding for LLMs | `manual_needed` | `not_found_in_checked_sources` | — |
| NPUMoE: Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs | `manual_needed` | `not_found_in_checked_sources` | — |
| Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization | `verified` | `not_found_in_checked_sources` | — |
| On Evaluating Performance of LLM Inference Serving Systems | `verified` | `not_found_in_checked_sources` | — |
| Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving | `verified` | `open_source_confirmed` | [repo](https://github.com/UT-SysML/Oneiros) |
| Online Scheduling for LLM Inference with KV Cache Constraints | `manual_needed` | `not_found_in_checked_sources` | — |
| OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| OPKV: A High-Throughput Plugin-Driven Framework for Recallable Sparsity in Paged KV Cache Systems | `manual_needed` | `not_found_in_checked_sources` | — |
| ORBITFLOW: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration | `verified` | `open_source_confirmed` | [repo](https://github.com/omnia-postech/OrbitFlow) |
| OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration | `manual_needed` | `not_found_in_checked_sources` | — |
| P/D-Serve: Serving Disaggregated Large Language Model at Scale | `verified` | `not_found_in_checked_sources` | — |
| PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM | `verified` | `not_found_in_checked_sources` | — |
| ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels | `verified` | `not_found_in_checked_sources` | — |
| PARD: Accelerating LLM Inference with Low-Cost PARallel Draft Model Adaptation | `verified` | `open_source_confirmed` | [repo](https://github.com/AMD-AIG-AIMA/PARD) |
| PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation | `verified` | `open_source_confirmed` | [repo](https://github.com/SJTU-IPADS/PhoenixOS) |
| PLA-Serve: A Prefill-Length-Aware LLM Serving System | `verified` | `not_found_in_checked_sources` | — |
| PM-KVQ: Progressive Mixed-precision KV Cache Quantization for Long-CoT LLMs | `manual_needed` | `public_code_license_unverified` | [repo](https://github.com/thu-nics/PM-KVQ) |
| POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression | `verified` | `not_found_in_checked_sources` | — |
| Preble: Efficient Distributed Prompt Scheduling for LLM Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/WukLab/preble) |
| Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators | `manual_needed` | `not_found_in_checked_sources` | — |
| PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications | `verified` | `not_found_in_checked_sources` | — |
| Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning | `verified` | `open_source_confirmed` | [repo](https://github.com/ovg-project/kvcached) |
| Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| QoServe: Breaking the Silos of LLM Inference Serving | `verified` | `not_found_in_checked_sources` | — |
| QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/mit-han-lab/deepcompressor) |
| QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill | `verified` | `not_found_in_checked_sources` | — |
| RDMA Point-to-Point Communication for LLM Systems | `verified` | `public_code_license_unverified` | [repo](https://github.com/perplexityai/pplx-garden) |
| Reasoning Language Model Inference Serving Unveiled: An Empirical Study | `verified` | `not_found_in_checked_sources` | — |
| RefreshKV: Updating Small KV Cache During Long-form Generation | `manual_needed` | `public_code_license_unverified` | [repo](https://github.com/carriex/recycled-attention) |
| ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing | `verified` | `not_found_in_checked_sources` | — |
| ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing | `verified` | `not_found_in_checked_sources` | — |
| Revisiting Pipeline Parallelism for LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/NVlabs/RocketKV) |
| RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving | `verified` | `public_code_license_unverified` | [repo](https://github.com/AKafakA/route-balance) |
| RTP-LLM: High-Performance Alibaba LLM Inference Engine | `verified` | `not_found_in_checked_sources` | — |
| SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL | `verified` | `not_found_in_checked_sources` | — |
| SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving | `verified` | `open_source_confirmed` | [repo](https://github.com/togethercomputer/saw-int4) |
| SchedFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling | `manual_needed` | `not_found_in_checked_sources` | — |
| SDR-RDMA: Software-Defined Reliability Architecture for Planetary Scale RDMA Communication | `verified` | `not_found_in_checked_sources` | — |
| Self-Speculative Decoding Accelerates Lossless Inference in Any-Order and Any-Subset Autoregressive Models | `manual_needed` | `not_found_in_checked_sources` | — |
| Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling | `verified` | `not_found_in_checked_sources` | — |
| semi-PD: Towards Efficient LLM Serving via Phase-Wise Disaggregated Computation and Unified Storage | `manual_needed` | `not_found_in_checked_sources` | — |
| SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models | `verified` | `open_source_confirmed` | [repo](https://github.com/JL-Cheng/SERE) |
| Service-Induced Congestion in Memory-Constrained LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| SGLang: Efficient Execution of Structured Language Model Programs | `verified` | `public_code_license_unverified` | [repo](https://github.com/sgl-project/sglang) |
| ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference | `verified` | `open_source_confirmed` | [repo](https://github.com/ByteDance-Seed/ShadowKV) |
| SHIP: SRAM-Based Huge Inference Pipelines for Fast LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters | `verified` | `not_found_in_checked_sources` | — |
| Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/alibaba-edu/qwen-bailian-usagetraces-anon) |
| SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| SOLA: Optimizing SLO Attainment for Large Language Model Serving with State-Aware Scheduling | `manual_needed` | `not_found_in_checked_sources` | — |
| SPAD: Specialized Prefill and Decode Hardware for Disaggregated LLM Inference | `manual_needed` | `not_found_in_checked_sources` | — |
| SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding | `verified` | `not_found_in_checked_sources` | — |
| SpecMemo: Speculative Decoding is in Your Pocket | `manual_needed` | `not_found_in_checked_sources` | — |
| Speculative Decoding: Performance or Illusion? | `manual_needed` | `not_found_in_checked_sources` | — |
| Speculative Speculative Decoding | `verified` | `not_found_in_checked_sources` | — |
| SPIN: Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving | `verified` | `not_found_in_checked_sources` | — |
| Stream2LLM: Overlap Context Streaming and Prefill for Reduced Time-to-First-Token | `manual_needed` | `not_found_in_checked_sources` | — |
| SuperInfer: SLO-Aware Rotary Scheduling and Memory Management for LLM Inference on Superchips | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/Supercomputing-System-AI-Lab/SuperInfer) |
| SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing | `verified` | `not_found_in_checked_sources` | — |
| SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading | `verified` | `not_found_in_checked_sources` | — |
| SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding | `verified` | `not_found_in_checked_sources` | — |
| SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems | `manual_needed` | `not_found_in_checked_sources` | — |
| Taming the Titans: A Survey of Efficient LLM Inference Serving | `verified` | `public_code_license_unverified` | [repo](https://github.com/zenrran4nlp/Awesome-LLM-Inference-Serving) |
| Tangram: Unlocking Non-Uniform KV Cache for Efficient Multi-turn LLM Serving | `manual_needed` | `not_found_in_checked_sources` | — |
| Tarragon: Making MoE-based LLM Inference Resilient | `manual_needed` | `not_found_in_checked_sources` | — |
| The CAP Principle for LLM Serving: A Survey of Long-Context Large Language Model Serving | `verified` | `not_found_in_checked_sources` | — |
| The Price of Anarchy in Disaggregated Inference | `verified` | `not_found_in_checked_sources` | — |
| ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models | `manual_needed` | `not_found_in_checked_sources` | — |
| THORN-ML: Transparent Hardware Offloaded Resilient Networks for RDMA based Distributed ML Workloads | `verified` | `not_found_in_checked_sources` | — |
| throttLL'eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving | `verified` | `not_found_in_checked_sources` | — |
| ThunderServe: High-performance and Cost-efficient LLM Serving in Cloud Environments | `manual_needed` | `not_found_in_checked_sources` | — |
| TimelyLLM: Time-sensitive LLM Serving System for Physical-I/O Limited Agents | `verified` | `not_found_in_checked_sources` | — |
| TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing | `verified` | `not_found_in_checked_sources` | — |
| TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling | `verified` | `not_found_in_checked_sources` | — |
| TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity | `verified` | `not_found_in_checked_sources` | — |
| Towards High-Goodput LLM Serving with Prefill-decode Multiplexing | `verified` | `not_found_in_checked_sources` | — |
| TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference | `verified` | `not_found_in_checked_sources` | — |
| TraCT: Disaggregated LLM Serving with CXL Shared Memory KV Cache at Rack-Scale | `manual_needed` | `not_found_in_checked_sources` | — |
| Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match | `verified` | `open_source_confirmed` | [repo](https://github.com/AMD-AGI/FLy) |
| Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing | `verified` | `not_found_in_checked_sources` | — |
| Tutel: Adaptive Mixture-of-Experts at Scale | `manual_needed` | `open_source_confirmed` | [repo](https://github.com/microsoft/tutel) |
| Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | `verified` | `not_found_in_checked_sources` | — |
| UEP: Portable Expert-Parallel Communication | `verified` | `not_found_in_checked_sources` | — |
| UniCache: Unifying Prefix Cache Eviction for Heterogeneous LLM Serving Workloads | `verified` | `not_found_in_checked_sources` | — |
| vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention | `verified` | `open_source_confirmed` | [repo](https://github.com/microsoft/vattention) |
| Vedrfolnir: RDMA Network Performance Anomalies Diagnosis in Collective Communications | `verified` | `not_found_in_checked_sources` | — |
| VeriCache: Turning Lossy KV Cache into Lossless LLM Inference | `verified` | `not_found_in_checked_sources` | — |
| vLLM-Omni: Fully Disaggregated Serving for Any-to-Any Multimodal Models | `manual_needed` | `not_found_in_checked_sources` | — |
| Which Heads Matter for Reasoning? RL-Guided KV Cache Compression | `manual_needed` | `not_found_in_checked_sources` | — |
| WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware | `manual_needed` | `not_found_in_checked_sources` | — |
| WISP: Waste- and Interference-Suppressed Distributed Speculative LLM Serving at the Edge via Dynamic Drafting and SLO-Aware Batching | `verified` | `not_found_in_checked_sources` | — |

## 单位字段更正

| 论文 | 原值 | 核验值 |
|---|---|---|
| 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving | 作者公开稿未列单位 | Graduate School of System Architect, KAIST, Daejeon, South Korea; School of Electrical Engineering, KAIST, Daejeon, South Korea |
| A Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints | 作者公开稿未列单位 | Affiliation: Department of Electrical and Computer Engineering, Stony Brook University; Affiliation: Department of Industrial Engineering and Decision Analytics, HKUST |
| A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference | 作者公开稿未列单位 | George Washington University; University of North Carolina at Charlotte; Ohio University |
| Accelerating Large-Scale Reasoning Model Inference with Sparse Self-Speculative Decoding | OpenReview 公开稿未列单位 | UC Berkeley; Massachusetts Institute of Technology; University of Washington; NVIDIA; Cornell University; Tsinghua University |
| AdaptCache: KV Cache Native Storage Hierarchy for Low-Delay and High-Quality Language Model Serving | University of Chicago; Microsoft Research 等 | University of Chicago; Microsoft |
| AdaSpec: Adaptive Speculative Decoding for Fast, SLO-Aware Large Language Model Serving | SoCC 2025 官方目录未列单位 | Tongji University, Shanghai, China and Shenzhen Research Institute of Big Data, The Chinese University of Hong Kong, Shenzhen, Shenzhen, Guangdong, China; Huazhong University of Science and Technology, Wuhan, Hubei, China; Tongji University, Shanghai, China; School of Data Science, The Chinese University of Hong Kong, Shenzhen, Shenzhen, Guangdong, China and Shenzhen Research Institute of Big Data, The Chinese University of Hong Kong, Shenzhen, Shenzhen, Guangdong, China |
| Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market | Alibaba Group 等 | Peking University, Beijing, Beijing, China; Alibaba Group, Hangzhou, Zhejiang, China |
| Alibaba Stellar: A New Generation RDMA Network for Cloud AI | Alibaba Cloud | Alibaba Cloud, Hangzhou, China; Alibaba Cloud, Hangzhou, USA; Alibaba Cloud, Sunnyvale, USA |
| AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor | 作者公开稿未列单位 | Affiliation: Department of Computer Science; Affiliation: Tufts University; Affiliation: Department of Electrical |
| Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving | HKUST | The Hong Kong University of Science and Technology, Hong Kong SAR, China; Shanghai Jiao Tong University, Shanghai, China; The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, China and The Hong Kong University of Science and Technology, Hong Kong SAR, China |
| Attention Is All You Need for KV Cache in Diffusion LLMs | OpenReview 公开稿未列单位 | VILA Lab, MBZUAI; FPT AI Residency |
| BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE | 作者公开稿未列单位 | Affiliation: Taobao & Tmall Group of Alibaba; Affiliation: Shenzhen Graduate School, Peking University |
| Beat the long tail: Distribution-Aware Speculative Decoding for RL Training | OpenReview 公开稿未列单位 | University of Illinois Urbana-Champaign; Together AI; UC San Diego; Prime Intellect |
| Beyond Prediction: Tail-Aware Scheduling for LLM Inference | 作者公开稿未列单位 | Affiliation: Cornell University, Computer Science Department, NY, USA; Affiliation: Microsoft Azure System Research, WA, USA; Affiliation: Cornell University, Electrical and Computer Engineering Department, NY, USA; Affiliation: NVIDIA Corporation, CA, USA; Affiliation: Cornell University, Operations Research and Information Engineering Department, NY, USA |
| Beyond Speedup - Utilizing KV Cache for Sampling and Reasoning | OpenReview 公开稿未列单位 | The Chinese University of Hong Kong; Huawei Technologies Co., Ltd. |
| Beyond Task-Agnostic: Task-Aware Grouping for Communication-Efficient Multi-Task MoE Inference | 作者公开稿未列单位 | Pengcheng Laboratory |
| Bottlenecked Transformers: Periodic KV Cache Consolidation for Generalised Reasoning | OpenReview 公开稿未列单位 | University College London; Huawei Noah's Ark Lab |
| BOute: Cost-Efficient LLM Serving with Heterogeneous LLMs and GPUs via Multi-Objective Bayesian Optimization | OpenReview 公开稿未列单位 | University of Cambridge; Shanghai Jiao Tong University |
| BrownoutServe: SLO-Aware Inference Serving under Bursty Workloads for MoE-based LLMs | Shenzhen University 等 | Southern University of Science and Technology, Shenzhen, China; Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences, Shenzhen, China; State Key Lab of IOTSC, University of Macau, Macau, China |
| Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration | Sun Yat-sen University | Sun Yat-sen University, Guangzhou, China |
| BurstGPT: A Real-world Workload Dataset to Optimize LLM Serving Systems | Hong Kong Baptist University; Microsoft Azure 等 | Huawei Hong Kong Research Center, Hong Kong, China; The Hong Kong University of Science and Technology (Guangzhou), Guangzhou, Guangdong, China; The Hong Kong University of Science and Technology (Guangzhou), GuangZhou, Guangdong, China; Huawei Technologies Ltd., Shenzhen, Guangdong, China; The Hong Kong University of Science and Technology, Hong Kong, China; Hong Kong Baptist University, Hong Kong, China; Tsinghua University, Beijing, China; Harbin Institute of Technology (Shenzhen), Shenzhen, Guangdong, China |
| ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud | ByteDance | ByteDance, Shanghai, China; ByteDance, Beijing, China; ByteDance, Hangzhou, China; ByteDance, San Jose, USA |
| CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration | University of Michigan | Affiliation: National University of Singapore |
| CacheWise: Understanding Workloads and Optimizing KVCache Management for Efficiently Serving LLM Coding Agents | 作者公开稿未列单位 | University of Washington; University of Virginia |
| Can I Buy Your KV Cache? | 作者公开稿未列单位 | Affiliation: Harbin Institute of Technology |
| CATS: Cascaded Adaptive Tree Speculation for Memory-Limited LLM Inference Acceleration | 作者公开稿未列单位 | Affiliation: University of Florida; Affiliation: Gainesville |
| Cauchy: A Cost-Efficient LLM Serving System through Adaptive Heterogeneous Deployment | SoCC 2025 官方目录未列单位 | Beihang University, Beijing, China; Kuaishou Inc., Beijing, China |
| Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments | University of Illinois Urbana-Champaign; IBM | University of Illinois Urbana-Champaign, Urbana, USA; IBM Research, Yorktown Heights, USA |
| COMET: Fine-grained Computation-communication Overlapping for Mixture-of-Experts | Alibaba Cloud; Peking University | ByteDance Seed; Shanghai Jiao Tong University |
| Coordinated Scheduling for MoE LLM Serving | 作者公开稿未列单位 | The University of Melbourne; Monash University; Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences |
| CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation | 作者公开稿未列单位 | Affiliation: School of Software, Beihang University |
| CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving | Academic/industry collaboration | Yale University, New Haven, Connecticut, USA; Columbia University, New York, New York, USA |
| Diff-MoE: Efficient Batched MoE Inference with Priority-Driven Differential Expert Caching | SC 2025 官方目录未列单位 | National Engineering Research Center for Big Data Technology and System, Services Computing Technology and System Lab, Cluster and Grid Computing Lab, School of Computer Science and Technology, Huazhong University of Science and Technology, Wuhan, China; School of Computer Science and Engineering, University of New South Wales, Sydney, NSW, Australia |
| Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study | 作者公开稿未列单位 | Affiliation: Analytics Everywhere Lab, University of New Brunswick, Fredericton, NB, Canada; Affiliation: TSAI Lab, University of New Brunswick, Fredericton, NB, Canada |
| DualMap: Enabling Both Cache Affinity and Load Balancing for Distributed LLM Serving | OpenReview 公开稿未列单位 | Huazhong University of Science and Technology; Huawei |
| EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse | Shanghai Jiao Tong University; National University of Defense Technology | Shanghai Jiao Tong University, Shanghai, China and Shanghai Qi Zhi Institute, Shanghai, China; Shanghai Jiao Tong University, Shanghai, China; National University of Defense Technology, Changsha, Hunan, China and Shanghai Qi Zhi Institute, Shanghai, China; Shanghai Jiaotong University, Shanghai, China and Shanghai Qi Zhi Institute, Shanghai, China |
| Efficient Memory Management for Large Language Model Serving with PagedAttention | UC Berkeley | UC Berkeley, Berkeley, United States of America; UC Berkeley, Berkeley, USA; UC Berkeley and Stanford University, Berkeley, USA; Independent Researcher, Berkeley, United States of America; UC San Diego, La Jolla, United States of America |
| EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts | 作者公开稿未列单位 | FuriosaAI; UC Berkeley |
| ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving | 作者公开稿未列单位 | KAIST; Microsoft Research; Shanghai Xingyunzhili \\ Artificial Intelligence Institute |
| Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs | 作者公开稿未列单位 | University of Pittsburgh; HPE Labs |
| ExeGPT: Constraint-Aware Resource Scheduling for LLM Inference | Seoul National University; Samsung Research | Hanyang University, Seoul, Republic of Korea; KT Corporation, Seoul, Republic of Korea |
| Fast MoE Inference via Predictive Prefetching and Expert Replication | 作者公开稿未列单位 | Iowa State University |
| Fast State Restoration in LLM Serving with HCache | EuroSys 2025 官方目录未列单位 | Tsinghua University |
| Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | OpenReview 公开稿未列单位 | The University of Hong Kong; NVIDIA; Massachusetts Institute of Technology; Independent Researcher |
| Fine-Tuning and Serving Gemma 4 31B on Google Cloud TPU: A Technical Comparison with GPU Baselines | 作者公开稿未列单位 | Affiliation: [5pt] Sairanjan Mishra |
| FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-Precision | Colfax Research; Princeton University | Colfax Research; Meta; NVIDIA; Georgia Tech; Princeton University; Together AI |
| Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets | 作者公开稿未列单位 | Department of Computer Science, Grinnell College; Department of Computer Science, Rice University; Workato; Lambda, Inc |
| FP8-Flow-MoE: A Casting-Free FP8 Recipe without Double Quantization Error | MLSys 2026 官方页面未列单位 | Zhejiang Lab |
| FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference | OpenReview 公开稿未列单位 | Shanghai Jiao Tong University; Huawei Technologies Co., Ltd. |
| Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice | Renmin University of China; Stanford University; Hong Kong University of Science and Technology | Affiliation: Gaoling School of Artificial Intelligence; Affiliation: Renmin University of China; Affiliation: Beijing; Affiliation: Department of Management Science; Affiliation: Stanford University; Affiliation: Stanford; Affiliation: Department of Industrial Engineering; Affiliation: HKUST; Affiliation: Hongkong |
| GreenLLM: SLO-Aware Dynamic Frequency Scaling for Energy-Efficient LLM Serving | EPFL | Embedded Systems Laboratory (ESL), École Polytechnique Fédérale de Lausanne (EPFL); Institute of Reconfigurable \& Embedded Digital Systems (REDS), School of Engineering and Management Vaud, HES-SO University of Applied Sciences and Arts Western Switzerland |
| Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention | 作者公开稿未列单位 | FrontiersMind |
| HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators | 作者公开稿未列单位 | Shanghai Jiao Tong University; UltraRISC |
| HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving | OpenReview 公开稿未列单位 | The University of Texas at Austin Austin TX USA; NVIDIA Austin TX USA |
| HERALD: High-Throughput Block Diffusion LLM Serving via CPU-GPU Cooperative KV Cache Retrieval | Seoul National University; University of California, Berkeley | Seoul National University; UC Berkeley |
| HydraInfer: Hybrid Disaggregated Scheduling for Multimodal Large Language Model Serving | Chinese Academy of Sciences; Beihang University 等 | University of Science and Technology of China; Beihang University; JD.com |
| HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching | 作者公开稿未列单位 | Xiaohongshu Inc.; Peking University; Shanghai Jiao Tong University |
| I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention | Illinois Institute of Technology; ICT, CAS; University of Chinese Academy of Sciences | Illinois Institute of Technology, Chicago, IL, USA; Institute of Computing Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences, Beijing, China; Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China |
| Infinite-LLM: Efficient LLM Service for Long Context with DistAttention and Distributed KVCache | Tsinghua University; Alibaba Cloud | Alibaba Group; Shanghai Jiao Tong University; Peking University |
| Information-Aware KV Cache Compression for Long Reasoning | 作者公开稿未列单位 | LUMIA Lab, Shanghai Jiao Tong University; University of Edinburgh; Shanghai Jiao Tong University |
| JITServe: SLO-aware LLM Serving with Imprecise Request Information | UIUC; Google; Cisco Research | University of Illinois Urbana-Champaign; Unaffiliated; Google; Cisco Research |
| Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost | OpenReview 公开稿未列单位 | University of Sydney; Together AI; University of Illinois Urbana-Champaign; Microsoft |
| KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models | Tsinghua University; ICT, CAS 等 | Tsinghua University, Beijing, China; Approaching.AI, Beijing, China; Approaching.Al, Beijing, China; Hangzhou Dianzi University, Hangzhou, China; University of Electronic Science and Technology of China, Chengdu, China; Beijing University of Posts and Telecommunications, Beijing, China; Beijing Institute of Technology, Beijing, China |
| KVEraser: Learning to Steer KV Cache for Efficient Localized Context Erasing | 作者公开稿未列单位 | Georgia Institute of Technology; Meta |
| KVServe: Service-Aware KV Cache Compression for Communication-Efficient Disaggregated LLM Serving | 作者公开稿未列单位 | University of Chinese Academy of Sciences; Institute of Computing Technology, Chinese Academy of Sciences; Shanghai Jiao Tong University |
| KVSwap: Disk-aware KV Cache Offloading for Long-Context On-device Inference | University of Leeds | University of Leeds, Leeds, United Kingdom |
| LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training | Peking University; Shanghai Jiao Tong University; ByteDance Seed | Peking University, Beijing, China; Shanghai Jiao Tong University, Shanghai, China; Bytedance Seed, Beijing, China; Bytedance Seed, Shenzhen, China |
| Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning | OpenReview 公开稿未列单位 | Peking University; Microsoft Research Asia |
| LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems | University of California, Riverside 等 | University of California,Riverside |
| Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads | National University of Singapore; University of Science and Technology of China; UC Berkeley | National University of Singapore; University of Science and Technology of China; UC Berkeley; Institute of Artificial Intelligence, Hefei Comprehensive National Science Center |
| LiquidGEMM: Hardware-Efficient W4A8 GEMM Kernel for High-Performance LLM Serving | SC 2025 官方目录未列单位 | Shanghai Jiao Tong University, Shanghai, China; ByteDance Seed, Shanghai, China; ByteDance Seed, Seattle, USA; ByteDance Seed, Beijing, China |
| Llumnix: Dynamic Scheduling for Large Language Model Serving | Tsinghua University; Alibaba Cloud | Alibaba Group |
| LMCache: An Efficient KV Cache Layer for Enterprise-Scale LLM Inference | University of Chicago; Microsoft; Google; IBM/Red Hat 等 | TensorMesh Inc.; University of Chicago |
| LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences | OpenReview 公开稿未列单位 | Peking University; Huawei Technologies Co., Ltd.; Chongqing University of Posts and Telecommunications |
| LUMEN: Coordinated Failure Recovery for Distributed LLM Serving | 作者公开稿未列单位 | Affiliation: University of Science and Technology of China |
| MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding | Microsoft Research 等 | Carnegie Mellon University; Moffett AI; Together AI |
| MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving | SC 2025 官方目录未列单位 | The University of Texas at Austin, Austin, USA; Cisco Systems, Bellevue, USA |
| MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism | ByteDance Seed; Peking University 等 | ByteDance Seed; Peking University |
| MemServe: Context Caching for Disaggregated LLM Serving with Elastic Memory Pool | Institute of Computing Technology, CAS; Huawei 等 | Huawei Cloud; University of Chinese Academy of Sciences; Institute of Computing Technology, Chinese Academy of Sciences; Peking University |
| MiniPIC: Flexible Position-Independent Caching in <100LOC | 作者公开稿未列单位 | IBM Research |
| Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference | Samsung Research 等 | Apple |
| MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training | SIGCOMM 2025 官方目录未列单位 | iSING Lab, Hong Kong University of Science and Technology, Hong Kong, Hong Kong; ITSC, Hong Kong University of Science and Technology, Hong Kong, Hong Kong; Massachusetts Institute of Technology, Cambridge, MA, USA; Peking University, Beijing, China; Meta, Menlo Park, CA, USA; EmbedWay, Shanghai, China; Xiamen University, Xiamen, China |
| Models Take Notes at Prefill: KV Cache Can Be Editable and Composable | 作者公开稿未列单位 | Affiliation: Pine AI |
| MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading | Shanghai Jiao Tong University; Chinese University of Hong Kong | Shanghai Jiaotong University, Shanghai, China; The Chinese University of Hong Kong, Hong Kong, China; Shanghai Jiao Tong University, Shanghai, China |
| MoEBlaze: Breaking the Memory Wall for Efficient MoE Training on Modern GPUs | MLSys 2026 官方页面未列单位 | Meta Platforms, Inc.; Thinking Machines Lab |
| Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving | Moonshot AI; Tsinghua University | Computer Science and Technology, Tsinghua University; Moonshot AI; Alibaba Cloud Computing; Independent Researcher; Tsinghua University; department of computer science and technology, Tsinghua University |
| MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing | OpenReview 公开稿未列单位 | University of Virginia; Harvard University |
| Multiplexed Heterogeneous LLM Serving via Stage-Aligned Parallelism | SoCC 2025 官方目录未列单位 | University of Pennsylvania, Philadelphia, Pennsylvania, USA |
| Niyama: Breaking the Silos of LLM Inference Serving | Microsoft Research | Microsoft Research India |
| Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization | KAIST | KAIST, Daejeon, Republic of Korea; HyperAccel, Seoul, Republic of Korea |
| On Evaluating Performance of LLM Inference Serving Systems | Microsoft Research; Georgia Institute of Technology | Georgia Institute of Technology; Microsoft Research; Intel Labs |
| Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving | SoCC 2025 官方目录未列单位 | The University of Texas at Austin, Austin, USA; Fairleigh Dickinson University, Vancouver, Canada |
| ORBITFLOW: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration | UNIST 等 | POSTECH; UNIST; Samsung Research |
| PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM | HPCA 2025 官方目录未列单位 | Cloud Research Team, Samsung SDS |
| ParallelKittens: Systematic and Practical Simplification of Multi-GPU AI Kernels | OpenReview 公开稿未列单位 | Department of Computer Science, Stanford University |
| PARD: Accelerating LLM Inference with Low-Cost PARallel Draft Model Adaptation | OpenReview 公开稿未列单位 | Advanced Micro Devices, Inc.; Tsinghua University |
| PhoenixOS: Concurrent OS-level GPU Checkpoint and Restore with Validated Speculation | SOSP 2025 官方目录未列单位 | Institute of Parallel and Distributed Systems, Shanghai Jiao Tong University, Shanghai, China; National University of Singapore, Singapore, Singapore |
| PLA-Serve: A Prefill-Length-Aware LLM Serving System | OpenReview 公开稿未列单位 | Mohamed bin Zayed University of Artificial Intelligence; University of North Carolina at Chapel Hill |
| POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference | University of Washington; Microsoft Research | University of Washington, Seattle, WA, USA; Microsoft Research, Bengaluru, India |
| PolyKV: Heterogeneous Retention and Allocation for KV Cache Compression | 作者公开稿未列单位 | Affiliation: King Abdullah University of Science |
| PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications | SOSP 2025 官方目录未列单位 | University of Chicago / TensorMesh, Inc., Foster City, California, USA; Sky Computing Lab, Tsinghua University / UC Berkeley, Berkeley, California, USA; University of Chicago, Chicago, Illinois, USA; LinkedIn, Mountain View, California, USA; Sky Computing Lab, UC Berkeley, Berkeley, California, USA |
| Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning | UCLA; UC Berkeley; Harvard University; Carnegie Mellon University; University of Edinburgh; Intel; Stanford University; LMSYS; ByteDance; Alibaba Cloud; Tsinghua University; Rice University | UCLA; UC Berkeley; Harvard University; Carnegie Mellon University; University of Edinburgh; Intel; Stanford University; LMSYS; ByteDance; Alibaba Cloud; Tsinghua University; Novita AI; Rice University |
| Pythia: Exploiting Workflow Predictability for Efficient Agent-Native LLM Serving | 作者公开稿未列单位 | UCLA; Alibaba Cloud Computing; Alibaba Group; Intel; Shanghai Jiao Tong University; UC Berkeley; Rice University; Tsinghua University; Peking University |
| QoServe: Breaking the Silos of LLM Inference Serving | Microsoft Research India | Microsoft Research, Bengaluru, India |
| QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill | OpenReview 公开稿未列单位 | Qualcomm AI Research |
| RDMA Point-to-Point Communication for LLM Systems | OpenReview 公开稿未列单位 | Perplexity AI |
| Reasoning Language Model Inference Serving Unveiled: An Empirical Study | OpenReview 公开稿未列单位 | The Hong Kong University of Science and Technology (Guangzhou); Tsinghua University; Hong Kong Baptist University; University of Wisconsin-Madison; Harbin Institute of Technology, Shenzhen; The Hong Kong University of Science and Technology |
| ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving | 作者公开稿未列单位 | Institute of Computing Technology, Chinese Academy of Sciences; Zhejiang Lab; Infinigence AI |
| REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing | Shanghai Jiao Tong University | Shanghai Jiao Tong University, Shanghai, China |
| ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing | OpenReview 公开稿未列单位 | Affiliation: School of Artificial Intelligence, University of Chinese Academy of Sciences, Beijing, China; Affiliation: University of Electronic ScienceTechnology of China, Chengdu, China; Affiliation: Wuhan AI Research, Wuhan, China |
| RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving | 作者公开稿未列单位 | University of Cambridge |
| RTP-LLM: High-Performance Alibaba LLM Inference Engine | Alibaba Group | Affiliation:; Alibaba Group; Peking University; Zhejiang University |
| SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL | 作者公开稿未列单位 | Peking University; Alibaba Cloud; Renmin University of China |
| SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving | Apple; University of Michigan 等 | Affiliation: Shuaiwen Leon Song, Ben Athiwaratkun, Chenfeng Xu, Tianyi Zhang, Xiaoxia Wu; footnotemark: 2; Affiliation: |
| SDR-RDMA: Software-Defined Reliability Architecture for Planetary Scale RDMA Communication | SC 2025 官方目录未列单位 | ETH Zürich, Zurich, Switzerland; Swiss National Supercomputing Centre (CSCS), Lugano, Switzerland; NVIDIA Corporation, Zwolle, Netherlands; NVIDIA Corporation, Zurich, Switzerland; NVIDIA Corporation, Santa Clara, USA; NVIDIA Corporation, Yokne'am Illit, Israel; Microsoft Corporation, Redmond, USA; Microsoft Corporation, Zurich, Switzerland |
| Semantic Parallelism: Redefining Efficient MoE Inference via Model-Data Co-Scheduling | OpenReview 公开稿未列单位 | Huawei Technologies; Sun Yat-sen University |
| SERE: Similarity-based Expert Re-routing for Efficient Batch Decoding in MoE Models | OpenReview 公开稿未列单位 | Taobao & Tmall Group, Alibaba; Peking University |
| SGLang: Efficient Execution of Structured Language Model Programs | Stanford University; UC Berkeley; Shanghai Jiao Tong University; Texas A&M University | Stanford University; UC Berkeley; Shanghai Jiao Tong University; Texas A&M University; Independent Researcher |
| ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters | 作者公开稿未列单位 | Affiliation: Hanyang University, Department of Data Science, Seoul, 04763, Republic of Korea; Affiliation: Hanyang University, Department of Artificial Intelligence, Seoul, 04763, Republic of Korea |
| SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding | MLSys 2026 官方页面未列单位 | University of Virginia |
| Speculative Speculative Decoding | 作者公开稿未列单位 | Department of Computer Science, Stanford University; Department of Computer Science, Princeton University; Together AI |
| Stratum: System-Hardware Co-Design with Tiered Monolithic 3D-Stackable DRAM for Efficient MoE Serving | UC San Diego; Georgia Institute of Technology 等 | University of California, San Diego, La Jolla, USA; Georgia Tech, Atlanta, USA; University of Illinois, Urbana-Champaign, Urbana, USA; Illinois Institute of Technology, Chicago, USA |
| SwiftCache: Efficient LLM Serving for Multi-turn Conversations with Heterogeneous KV Cache Sharing | 作者公开稿未列单位 | Institute for Clarity in Documentation; Southern University of Science and Technology; Shenzhen Institutes of Advanced Technology, CAS; Shenzhen Institutes of Advanced Technology, CAS; Institute of Computing Technology, CAS; Alibaba Group; University of Macau; % 1 Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences % 2 Southern University of Science and Technology % 3 Institute of Computing Technology, Chinese Academy of Sciences \\ % 4 Alibaba Group % 5 University of Macau % |
| SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading | Tencent; Nanjing University | Unaffiliated; Tencent; Nanjing University |
| SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding | ByteDance Seed; University of Chicago 等 | ByteDance Seed; University of Chicago |
| Taming the Titans: A Survey of Efficient LLM Inference Serving | Soochow University; Alibaba Cloud 等 | Soochow University; Huawei Cloud |
| The CAP Principle for LLM Serving: A Survey of Long-Context Large Language Model Serving | ICT, CAS; Huawei 等 | Huawei Cloud; Shanghai Jiao Tong University; Beijing University of Posts and Telecommunications; University of Electronic Science and Technology of China |
| The Price of Anarchy in Disaggregated Inference | 作者公开稿未列单位 | NCA |
| THORN-ML: Transparent Hardware Offloaded Resilient Networks for RDMA based Distributed ML Workloads | SoCC 2025 官方目录未列单位 | University of Colorado Boulder, Boulder, USA; Unaffiliated, Longmont, CO, USA; University of Colorado Boulder, Boulder, CO, USA |
| throttLL'eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving | HPCA 2025 官方目录未列单位 | ETH,Zürich; National Technical University of Athens |
| TimelyLLM: Time-sensitive LLM Serving System for Physical-I/O Limited Agents | Yale University | Yale University, New Haven, USA |
| TokenDance: Scaling Multi-Agent LLM Serving via Collective KV Cache Sharing | Peking University | Peking University; Shanghai Jiao Tong University |
| TokenFlow: Responsive LLM Text Streaming Serving under Request Burst via Preemptive Scheduling | Shanghai Jiao Tong University; George Mason University; China Telecom | Shanghai Jiao Tong University, Shanghai, Shanghai, China; George Mason University, Fairfax, VA, USA; China Telecom Corporation Limited Shanghai Branch, Shanghai, Shanghai, China |
| TokenScale: Timely and Accurate Autoscaling for Disaggregated LLM Serving with Token Velocity | University of Edinburgh 等 | Georgia Institute of Technology; Alibaba Group; University of Edinburgh; Nanyang Technological University |
| Towards High-Goodput LLM Serving with Prefill-decode Multiplexing | Shanghai Jiao Tong University; National University of Singapore | Shanghai Jiao Tong University, Shanghai, China; Shanghai Jiao Tong University, Shanghai, China and National University of Singapore, Singapore, Singapore; Researcher, Shanghai, China; National University of Singapore, Singapore, Singapore |
| TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference | Peking University; Tencent YouTu Lab | Peking University, Beijing, China; Tencent YouTu Lab, Shanghai, China |
| Training-Free Loosely Speculative Decoding: Accepting Semantically Correct Drafts Beyond Exact Match | OpenReview 公开稿未列单位 | Advanced Micro Devices, Inc.; The University of Hong Kong |
| Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing | 作者公开稿未列单位 | Shanghai Artificial Intelligence Laboratory; Peking University |
| Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving | 作者公开稿未列单位 | Xiamen University; Shanghai Jiao Tong University‌; Hong Kong University of Science and Technology; SJTU \& XMU; 2 Xiamen University; Shanghai Jiao Tong University |
| UEP: Portable Expert-Parallel Communication | UC Berkeley; UC Davis; University of Wisconsin-Madison; AMD; Tsinghua University; AWS; Broadcom | UC Berkeley; UC Davis; University of Wisconsin-Madison; AMD; Independent Researcher; Tsinghua University; Amazon Web Services; ICSI; Broadcom; University Politehnica of Bucharest |
| UniCache: Unifying Prefix Cache Eviction for Heterogeneous LLM Serving Workloads | Rice University; University of California, Berkeley | Rice University, Houston, Texas, USA; UC Berkeley, Berkeley, California, USA |
| vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention | Microsoft Research India | Microsoft Research, Bangalore, India; Indian Institute of Science, Bangalore, India |
| Vedrfolnir: RDMA Network Performance Anomalies Diagnosis in Collective Communications | SIGCOMM 2025 官方目录未列单位 | Beihang University |
| VeriCache: Turning Lossy KV Cache into Lossless LLM Inference | University of Chicago; UIUC | Affiliation:; University of Chicago; Tensormesh Inc.; Samsung Semiconductor; Microsoft Research |
| WISP: Waste- and Interference-Suppressed Distributed Speculative LLM Serving at the Edge via Dynamic Drafting and SLO-Aware Batching | Virginia Tech; University College Dublin; Queen’s University Belfast; National Technical University of Athens | Virginia Tech, Blacksburg, Virginia, USA; University College Dublin, Dublin, Ireland; National Technical University of Athens, Athens, Greece; Queen's University Belfast, Belfast, United Kingdom; Queens University Belfast, Belfast, United Kingdom |
