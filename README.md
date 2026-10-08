# Awesome LLM Inference Systems

**Systems research worth reading — from first principles to production.**

An edited bibliography of the ideas and implementations that shape efficient large language model inference: attention kernels, KV memory, request scheduling, disaggregated execution, and production serving.

Selection follows the **systems question, the mechanism, and the evidence**. We favor work that establishes a lasting abstraction, demonstrates convincing end-to-end value, or changes how real inference systems are built. Venue and affiliation are useful context, never admission criteria on their own. This list is deliberately selective—not a leaderboard or an exhaustive paper dump.

## Explore

| Collection | What to expect |
|---|---|
| [Surveys](#surveys--start-here) | Six complementary reading maps, clearly separating peer-reviewed publications from preprints. |
| [Foundational and influential papers](#foundational-and-influential-papers) | Thirty selected milestones, from historical prerequisites to modern inference systems. |
| [Papers by mechanism](topics/README.md) | Eight technical categories, 248 canonical topic entries and a concise admission history. |
| [Serving Systems review](topics/serving-systems.md) | Migration decisions for the former 50-paper Serving shortlist; no duplicate records. |
| [Organizations](#organizations) | Selected first-party model and infrastructure work: China and the United States. |
| [Research labs & open source](communities/README.md) | Maintainers, labs and open systems worth following for inference research. |

**One primary home per paper.** The homepage keeps historic foundations and surveys; technical additions live under [eight topic categories](topics/README.md). The former 50-paper Serving cohort has been reviewed: 49 were moved to their technical home, and 1 general AI-serving work was held out under the stricter LLM-specific boundary.

**Editorial standard:** primary publication or project sources, a concrete systems contribution, and explicit provenance. Paper mechanisms are summarized from source materials; reported speedups are not treated as independently reproduced results. See [Curation policy](CURATION.md).

## Organizations

Brief maps of publicly documented model-inference techniques and first-party infrastructure. Organized by region only for navigation, not by perceived research quality.

[**Companies — China & US**](organizations/README.md) · [**Research labs & open-source communities**](communities/README.md)

## Surveys — start here

Only complementary surveys with useful systems synthesis are retained. **Preprints are explicitly marked.**

| Lens | Survey | Publication | Why it matters / scope boundary |
|---|---|---|---|
| Serving: algorithms → systems | [Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems](https://arxiv.org/abs/2312.15234) | arXiv 2023; revised 2025 | CMU/Purdue 等团队，研究解码算法到部署体系结构的完整 Serving 脉络；不覆盖所有 2026 工作。 |
| Hardware / full-stack | [Full Stack Optimization of Transformer Inference: a Survey](https://arxiv.org/abs/2302.14017) | arXiv 2023 | UC Berkeley 团队；算子分析、Mapping、专用加速器与 Gemmini 案例；不限于 LLM Serving。 |
| Resource efficiency | [Resource-efficient Algorithms and Systems of Foundation Models: A Survey](https://doi.org/10.1145/3706418) | ACM Computing Surveys 2025 | PKU/BUPT；覆盖跨计算、存储和部署的优化；包含训练、ViT 和 Diffusion。 |
| Inference architecture | [A Survey of LLM Inference Systems](https://arxiv.org/abs/2506.21901) | arXiv 2025 (preprint) | 清华团队；从 Kernel、Batching、KV 到多副本、P/D 分离和 Serverless；未标为已审稿。 |
| KV: token / model / systems | [A Survey on Large Language Model Acceleration based on KV Cache Management](https://openreview.net/forum?id=z3JZzu9EA3) | TMLR 2025 | HKUST/PolyU/HUST 等；比较 KV 选择、压缩、量化及系统管理；包含算法层。 |
| KV: system behavior | [Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization](https://aclanthology.org/2026.findings-acl.1916/) | ACL Findings 2026 | 墨尔本大学/HUST；Temporal/Spatial/Structural 维度分析 Serving-time KV；排除重训型方法。 |

**Reading path:** *Inference systems* → *KV system behavior* → *KV algorithm+system taxonomy*. Consult the *full-stack* survey for hardware/kernel/compiler context.

## Foundational and influential papers

**2017–2019 papers are historical prerequisites**, not evidence of modern LLM Serving performance. Later selections have distinct system mechanisms or deployment value.

### 2017

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Attention Is All You Need](https://papers.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) | NeurIPS 2017 | Google Brain | Transformer self-attention；LLM 架构前提（不是现代 Serving 论文）。 |

### 2018

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Blockwise Parallel Decoding for Deep Autoregressive Models](https://papers.nips.cc/paper/8212-blockwise-parallel-decoding-for-deep-autoregressive-models) | NeurIPS 2018 | Google Brain | 候选块并行预测、验证最长正确前缀；投机/并行解码前驱。 |

### 2019

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150) | arXiv 2019 | Google Research | Multi-Query Attention (MQA) 共享 KV heads，降低增量解码访存带宽。 |

### 2022

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) | OSDI 2022 | Seoul National University · FriendliAI | Iteration-level scheduling 与 selective batching，确立自回归 serving 的调度抽象。 |
| [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://papers.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) | NeurIPS 2022 | Stanford · University at Buffalo | IO-aware exact attention / tiling；从内存访问出发重构 Attention Kernel。 |
| [DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale](https://sc22.supercomputing.org/proceedings/tech_paper/tech_paper_pages/pap307.html) | SC 2022 | Microsoft | 多 GPU 与 CPU/NVMe 异构推理，体现跨设备资源系统设计。 |

### 2023

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | SOSP 2023 | UC Berkeley · Stanford · UC San Diego | Paged KV Cache 与 vLLM；突破动态 KV 内存碎片和请求间复用。 |
| [FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU](https://proceedings.mlr.press/v202/sheng23a.html) | ICML 2023 | Stanford · UC Berkeley · ETH Zürich | 异构内存卸载与调度优化，展示资源受限场景的系统权衡。 |
| [AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving](https://www.usenix.org/conference/osdi23/presentation/li-zhouhan) | OSDI 2023 | UC Berkeley · Peking University · collaborators | 利用 Model Parallelism 改善多模型负载下的统计复用与 SLO。 |
| [Efficiently Scaling Transformer Inference](https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html) | MLSys 2023 | Google Research | 解析性能模型指导 TPU 模型并行、MQA 和延迟/吞吐权衡。 |
| [Fast Inference from Transformers via Speculative Decoding](https://proceedings.mlr.press/v202/leviathan23a.html) | ICML 2023 | Google Research | Draft–Verify 和保留目标分布的采样规则；现代 Speculative Decoding 基础。 |
| [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://aclanthology.org/2023.emnlp-main.298/) | EMNLP 2023 | Google Research | Grouped-Query Attention；在 MHA 与 MQA 之间平衡 KV 带宽和模型质量。 |

### 2024

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://www.usenix.org/conference/osdi24/presentation/agrawal) | OSDI 2024 | Georgia Tech · Microsoft Research | Chunked Prefill 与 stall-free scheduling，重新平衡 TTFT、TPOT 和吞吐。 |
| [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) | OSDI 2024 | Peking University · UC San Diego · StepFun | P/D 分离、SLO-aware 配置与 Goodput 导向的服务部署。 |
| [Splitwise: Efficient Generative LLM Inference Using Phase Splitting](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) | ISCA 2024 | Microsoft Research · University of Washington | 依据 Prefill/Decode 计算特征划分资源与机器；关注成本、功耗和传输。 |
| [Llumnix: Dynamic Scheduling for Large Language Model Serving](https://www.usenix.org/conference/osdi24/presentation/sun-biao) | OSDI 2024 | Alibaba Group | 请求与 KV 状态的 live migration，实现跨实例动态重调度。 |
| [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html) | NeurIPS 2024 | Stanford · UC Berkeley · collaborators | 将结构化程序执行、RadixAttention 和高效输出解码纳入统一 Runtime。 |
| [Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads](https://proceedings.mlr.press/v235/cai24b.html) | ICML 2024 | Princeton · Together AI · UIUC · collaborators | 多解码头与 Tree-based Verification，拓展推测解码设计空间。 |
| [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://proceedings.iclr.cc/paper_files/paper/2024/hash/98ed250b203d1ac6b24bbcf263e3d4a7-Abstract-Conference.html) | ICLR 2024 | Princeton · Stanford | 优化块/warp 工作划分与非矩阵 FLOPs，提升 GPU Attention 效率。 |
| [SLoRA: Scalable Serving of Thousands of LoRA Adapters](https://proceedings.mlsys.org/paper_files/paper/2024/hash/906419cd502575b617cc489a1a696a67-Abstract-Conference.html) | MLSys 2024 | UC Berkeley · Stanford · SJTU | Unified Paging 统一管理 Adapter/KV，配合异构 Batching 与 Kernel。 |
| [SpecInfer: Accelerating Large Language Model Serving with Tree-based Speculative Inference and Verification](https://doi.org/10.1145/3620666.3651335) | ASPLOS 2024 | CMU · Tsinghua · Stanford · collaborators | Token-tree parallel verification 集成到分布式和 Offloading Serving。 |
| [FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](https://proceedings.neurips.cc/paper_files/paper/2024/hash/7ede97c3e082c6df10a8d6103a2eebd2-Abstract-Conference.html) | NeurIPS 2024 | Colfax Research · NVIDIA · Meta · Princeton | Hopper 上的异步流水、Warp Specialization 与 FP8 Attention。 |

### 2025

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) | MLSys 2025 | University of Washington · NVIDIA · CMU | 可组合 KV 格式、JIT 模板与负载均衡的 Serving Attention Engine。 |
| [NanoFlow: Towards Optimal Large Language Model Serving Throughput](https://www.usenix.org/conference/osdi25/presentation/zhu-kan) | OSDI 2025 | University of Washington · collaborators | Operation-level Nano-batching，重叠设备上的 Compute/Memory/Network。 |
| [Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot](https://www.usenix.org/conference/fast25/presentation/qin) | FAST 2025 | Moonshot AI · Tsinghua University | 生产 KV Cache 共享与分离式存储，构建长上下文 Serving 数据路径。 |
| [QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html) | MLSys 2025 | MIT Han Lab · collaborators | 量化算法与 GPU 执行内核协同设计，避免低比特推理的反量化开销。 |
| [vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention](https://doi.org/10.1145/3669940.3707256) | ASPLOS 2025 | Microsoft Research · IISc | CUDA 虚拟内存实现 KV 虚拟连续、物理按需分配；PagedAttention 的替代。 |

### 2026

| Paper | Venue | Representative affiliations* | Why it matters |
|---|---|---|---|
| [Strata: Hierarchical Context Caching for Long Context Language Model Serving](https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang) | OSDI 2026 | Stanford · NVIDIA · collaborators | 分层 KV Cache I/O 与 cache-aware scheduling，针对缓存加载瓶颈。 |
| [Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning](https://www.usenix.org/conference/osdi26/presentation/yu-shan) | OSDI 2026 | UCLA · UC Berkeley · Harvard · collaborators | GPU Memory Ballooning 统一多模型空间/时间共享，有生产部署证据。 |
| [FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang) | NSDI 2026 | Peking University · collaborators | 迭代级可抢占调度与状态卸载，将抢占机制用于 LLM Serving。 |

*Affiliations are representative, not exhaustive; institutional prestige is not the primary admission criterion. Descriptions reflect authors' reported contributions, not independently reproduced benchmarks.

## Contributing

Read [CURATION.md](CURATION.md). Prefer official proceedings/publisher URLs, concrete mechanisms, and small reviewed PRs. No automated conference dumps.
