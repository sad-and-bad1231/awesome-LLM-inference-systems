# Awesome LLM Inference Systems

A **selectively curated**, lightweight list of papers with foundational or demonstrable engineering contributions to LLM inference systems. Not an exhaustive bibliography.

**Selection principle:** systems contribution and credible evaluation first; venue and research organization are supporting signals, not substitutes for technical merit. Entries point to publisher/conference records where available. See [CURATION.md](CURATION.md).

> **Rebuild status (2026-10-08):** seed list of 19 papers, screened from an uploaded 1,003-record JSONL collection (plus one missing foundational paper). This is **not** a full audit or a claim that unlisted papers lack merit. The original database remains in the unchanged `main` branch/history pending review of this draft.

## Papers

### 2022

| Paper | Venue | Research groups / institutions* | Systems contribution |
|---|---|---|---|
| [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu) | OSDI 2022 | Seoul National University · FriendliAI | Iteration-level scheduling 与 selective batching，确立自回归 serving 的调度抽象。 |
| [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://papers.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) | NeurIPS 2022 | Stanford · University at Buffalo | IO-aware exact attention / tiling；从内存访问出发重构 Attention Kernel。 |
| [DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale](https://sc22.supercomputing.org/proceedings/tech_paper/tech_paper_pages/pap307.html) | SC 2022 | Microsoft | 多 GPU 与 CPU/NVMe 异构推理，体现跨设备资源系统设计。 |

### 2023

| Paper | Venue | Research groups / institutions* | Systems contribution |
|---|---|---|---|
| [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://doi.org/10.1145/3600006.3613165) | SOSP 2023 | UC Berkeley · Stanford · UC San Diego | Paged KV Cache 与 vLLM；突破动态 KV 内存碎片和请求间复用。 |
| [FlexGen: High-Throughput Generative Inference of Large Language Models with a Single GPU](https://proceedings.mlr.press/v202/sheng23a.html) | ICML 2023 | Stanford · UC Berkeley · ETH Zürich | 异构内存卸载与调度优化，展示资源受限场景的系统权衡。 |
| [AlpaServe: Statistical Multiplexing with Model Parallelism for Deep Learning Serving](https://www.usenix.org/conference/osdi23/presentation/li-zhouhan) | OSDI 2023 | UC Berkeley · Peking University · collaborators | 利用 Model Parallelism 改善多模型负载下的统计复用与 SLO。 |

### 2024

| Paper | Venue | Research groups / institutions* | Systems contribution |
|---|---|---|---|
| [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://www.usenix.org/conference/osdi24/presentation/agrawal) | OSDI 2024 | Georgia Tech · Microsoft Research | Chunked Prefill 与 stall-free scheduling，重新平衡 TTFT、TPOT 和吞吐。 |
| [DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin) | OSDI 2024 | Peking University · UC San Diego · StepFun | P/D 分离、SLO-aware 配置与 Goodput 导向的服务部署。 |
| [Splitwise: Efficient Generative LLM Inference Using Phase Splitting](https://www.microsoft.com/en-us/research/publication/splitwise-efficient-generative-llm-inference-using-phase-splitting/) | ISCA 2024 | Microsoft Research · University of Washington | 依据 Prefill/Decode 计算特征划分资源与机器；关注成本、功耗和传输。 |
| [Llumnix: Dynamic Scheduling for Large Language Model Serving](https://www.usenix.org/conference/osdi24/presentation/sun-biao) | OSDI 2024 | Alibaba Group | 请求与 KV 状态的 live migration，实现跨实例动态重调度。 |
| [SGLang: Efficient Execution of Structured Language Model Programs](https://proceedings.neurips.cc/paper_files/paper/2024/hash/724be4472168f31ba1c9ac630f15dec8-Abstract-Conference.html) | NeurIPS 2024 | Stanford · UC Berkeley · collaborators | 将结构化程序执行、RadixAttention 和高效输出解码纳入统一 Runtime。 |
| [Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads](https://proceedings.mlr.press/v235/cai24b.html) | ICML 2024 | Princeton · Together AI · UIUC · collaborators | 多解码头与 Tree-based Verification，拓展推测解码设计空间。 |

### 2025

| Paper | Venue | Research groups / institutions* | Systems contribution |
|---|---|---|---|
| [FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html) | MLSys 2025 | University of Washington · NVIDIA · CMU | 可组合 KV 格式、JIT 模板与负载均衡的 Serving Attention Engine。 |
| [NanoFlow: Towards Optimal Large Language Model Serving Throughput](https://www.usenix.org/conference/osdi25/presentation/zhu-kan) | OSDI 2025 | University of Washington · collaborators | Operation-level Nano-batching，重叠设备上的 Compute/Memory/Network。 |
| [Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot](https://www.usenix.org/conference/fast25/presentation/qin) | FAST 2025 | Moonshot AI · Tsinghua University | 生产 KV Cache 共享与分离式存储，构建长上下文 Serving 数据路径。 |
| [QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html) | MLSys 2025 | MIT Han Lab · collaborators | 量化算法与 GPU 执行内核协同设计，避免低比特推理的反量化开销。 |

### 2026

| Paper | Venue | Research groups / institutions* | Systems contribution |
|---|---|---|---|
| [Strata: Hierarchical Context Caching for Long Context Language Model Serving](https://www.usenix.org/conference/osdi26/presentation/xie-zhiqiang) | OSDI 2026 | Stanford · NVIDIA · collaborators | 分层 KV Cache I/O 与 cache-aware scheduling，针对缓存加载瓶颈。 |
| [Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning](https://www.usenix.org/conference/osdi26/presentation/yu-shan) | OSDI 2026 | UCLA · UC Berkeley · Harvard · collaborators | GPU Memory Ballooning 统一多模型空间/时间共享，有生产部署证据。 |
| [FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang) | NSDI 2026 | Peking University · collaborators | 迭代级可抢占调度与状态卸载，将抢占机制用于 LLM Serving。 |

*Institution labels are concise representative affiliations, not exhaustive author lists or a ranking. Paper identity, publication, and the summarized mechanisms were checked against primary proceedings/project pages. They are **not** substitutes for independent re-benchmarking or complete peer review.

## Contributing

Before proposing a paper, read [CURATION.md](CURATION.md). Prefer one official paper link and one concrete sentence explaining the reusable mechanism. Do not add raw crawls, conference dumps, or automatically generated rankings. Submit a small PR for each batch.
