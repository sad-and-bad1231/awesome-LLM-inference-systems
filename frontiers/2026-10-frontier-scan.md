# Frontier scan — October 2026

**ARCHIVED SIGNAL LOG (2026-10-18); NOT THE CURRENT ACTIVE FRONTIER LIST.** The [October 19 active frontiers](README.md) retain only six genuinely new inference execution contracts. This note preserves earlier signals (including ordinary KV caching, hybrid attention, semantic response caching, general fleet metrics and deployment infrastructure) as **established engineering tracks or adjacent observations**, not active standalone frontiers.

**Historical context.** This is a dated signal scan, not a bibliography: it records the signals that stood out while the eight topic pages were expanded by 115 papers (669 → 784) against first-party sources, plus a few fresh pointers that have not been admitted anywhere yet. Rigour is deliberately lighter than in [the topic pages](../topics/README.md) — every claim below is backed by a link, but nothing here has been reproduced or full-text reviewed.

[← Frontiers](README.md) · [Papers by mechanism](../topics/README.md) · [Curation policy](../CURATION.md)

---

## Ten signals

### 1. The agentic *program*, not the request, is becoming the scheduling unit

- [ThunderAgent — a fast, simple, and program-aware agentic inference system](https://icml.cc/virtual/2026/poster/62040) ([arXiv](https://arxiv.org/abs/2602.13692), [code](https://github.com/SemiAnalysisAI/ThunderAgent)) pairs the paper with a production claim: [2× faster agentic inference for synthetic data generation at scale](https://www.together.ai/blog/thunderagent) at Together AI.
- The repo already keeps the scholarly edge of this wave canonical — FlashAgents (MLSys 2026), AgentSysBench, SMetric, Helios — and the operator side (Dynamo's agentic docs, llm-d's GLM-5.2 agentic note). ThunderAgent is the first artefact that is *simultaneously* a peer-reviewed system, an open-source stack, and a deployed production claim.
- Why it matters: TTFT/TPOT describe one request. An agent session's critical path runs through tool calls, sandboxes and retrieval, so the scheduler has to reason about a *program*. The interesting open question is what the fairness/isolation story is when two agent programs co-tenant one fleet.

### 2. World models crossed from paper demos into serving cookbooks

- The [SGLang cookbook](https://docs.sglang.io/cookbook/diffusion/LingBot-World/LingBot-World-2.0) now ships **LingBot World 2.0 with a REALTIME tag**, next to LingBot World and SANA-WM — a production serving stack publishing hardware recipes (`ulysses_degree=8, ring_degree=1`) for interactive world rollout is a category change, not a paper.
- [ABot-World-0](https://arxiv.org/abs/2607.19191) ([code](https://github.com/amap-cvlab/ABot-World), July 2026 preprint) is the full-stack co-design reference: a causal student distilled from a bidirectional teacher, LongForcing to fight autoregressive drift, then a streaming stack — lightweight VAE decoder, memory-aware scheduling, low-bit DiT inference, efficient attention — streaming **720P at up to 16 FPS on a single RTX 5090, 1.2 s action-to-first-frame, ~19 GiB peak VRAM**, driven by raw keyboard actions.
- The topic pages already host the mechanisms (FAST-AR, Rolling Forcing, BWCache, StreamDiffusionV2, LongLive, MoWorld, WorldPlay).
- Why it matters: LLM serving mechanisms transfer, but drift is a failure mode serving stacks do not model — the system must decide when the world it is rendering has *stopped being the world the user was in*.

### 3. dLLM serving is becoming its own subfield

- [dLLM-Serve (ICS 2026)](https://dl.acm.org/doi/full/10.1145/3797905.3800532) shows AR-tuned KV managers mis-predict diffusion memory curves; [Taming the Memory Footprint Crisis](https://arxiv.org/abs/2512.17077) (preprint) attacks the same production gap; and Google now ships [DiffusionGemma developer guidance](https://developers.googleblog.com/en/diffusiongemma-the-developer-guide/).
- `decoding-acceleration :: Diffusion & Non-AR Generation` already keeps 15+ dLLM rows; this scan adds the *serving-stack* half of the story.
- Why it matters: block-parallel decoding rewrites the memory curve, so the assumptions under every AR-era KV manager quietly break. Expect a dLLM-native page manager, not a port.

### 4. Fleet efficiency got a rigorous definition

- [Machine Learning Fleet Efficiency (MLSys 2026 oral)](https://mlsys.org/virtual/2026/oral/3734) — Google's ML Productivity Goodput decomposes thousands-of-accelerator fleet efficiency into **scheduling / runtime / program** goodput, reports >95% scheduling goodput in production, and names framework modernisation, async checkpointing and communication-computation overlap as the levers.
- Why it matters: ops teams finally have a shared measurement vocabulary that is not "utilisation". The repo's Fleet Scaling & Reliability direction now has its metric paper.

### 5. RL rollout and online serving share hardware, and the SLO fight is unresolved

- [Weave (OSDI '26)](https://www.usenix.org/conference/osdi26/presentation/wu-tianyuan), ROSE, and [llm-d's RL time-slicing](https://llm-d.ai/blog/rl-post-training-co-operative-time-slicing) (~40% more post-training experiments on identical GPUs) all co-tenant rollout with serving.
- Why it matters: preemption plus KV residency across two workloads with opposite SLO shapes is the hardest new scheduling problem. Neither side's failure is acceptable to the other.

### 6. Mature engineering signal: distributed KV state (demoted from Frontier)

- [llm-d v0.5](https://llm-d.ai/blog/llm-d-v0.5-sustaining-performance-at-scale) runs GPU → CPU → **filesystem** tiering with replica hydration; [P2P KV sharing](https://llm-d.ai/blog/p2p-kv-cache-sharing-llm-d) turns one replica's eviction into another's prefix hit; [Dynamo's Flash Indexer](https://docs.dynamo.nvidia.com/dynamo/v1.4.0/digest/flash-indexer) treats KV location as the routing substrate.
- OSDI '26 pushes the same direction: [ECHO](https://www.usenix.org/conference/osdi26/presentation/liu-guangda) (lossless prefetch for NSA models) and [No Buffer, No Bottleneck](https://www.usenix.org/conference/osdi26/presentation/luo) (zero-copy C2C offloading on GH200/GB200).
- Why it matters: this is a cache-coherence problem wearing a serving costume — index, placement, freshness, and now *ownership* across replicas.

### 7. Kernel automation is turning agentic — and its audit is the bottleneck

- [KernelBench-Verified](https://arxiv.org/abs/2607.16241) (2026 preprint, methodology watch — **not** canonically admitted) flags benchmark exploitation, hidden-test correctness and baseline-timing bias; KForge (cross-platform kernel generation for AI accelerators), KernelBand (ICML 2026), AlphaCu, AccelOpt and an IJCAI 2026 survey are the other canonical entries in `kernels-compilers :: Kernel Automation & Tools`.
- Why it matters: generating candidate kernels is no longer the hard part; *proving* which candidates are correct and faster is. The audit harness is the product.

### 8. Adjacent, not KV: semantic response caching and invalidation

- [CacheSense](https://ieeexplore.ieee.org/document/11621808) (freshness-aware selective invalidation) and [Semantic Caching for Low-Cost LLM Serving: From Offline Learning to Online Adaptation](https://ieeexplore.ieee.org/document/11571467) join [SmartCache](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fb74b63d225f846e6032bf3e3ab0f4ec-Abstract-Conference.html) (NeurIPS 2025).
- Why it matters: a stale semantic hit is worse than a miss — it is confidently wrong and cheap, which is the worst combination. Freshness tracking is what turns a dictionary into a cache.

### 9. Day-0 deployment is now an engineering product

- Reflection's [Beam](https://reflection.ai/blog/introducing-beam) (501B open-weight) shipped with [day-0 Google Cloud recipes on llm-d + NVIDIA Dynamo](https://www.computelabs.ai/research/2026-10-16/google-cloud-introduced-launch-day-beam-deployment-recipes-using-llm-d-nvidia), including GB300 NVL72, with a "5× perf" claim; [CoreWeave published its own serving path](https://wf.coreweave.com/blog/from-training-to-serving-reflections-beam-on-coreweave).
- Why it matters: the interval from *weights available* to *production serving recipe* is the industry's real benchmark, and it is measured in hours. Infra teams pre-build the recipe before the model lands.

### 10. Ecosystem maturity signal: systems venues publish LLM inference

- OSDI '26's LLM-serving slate is already canonical here: [EcoServe](https://www.usenix.org/conference/osdi26/presentation/du), [OpenTela](https://www.usenix.org/conference/osdi26/presentation/yao), [Kairox](https://www.usenix.org/conference/osdi26/presentation/jiang-yapeng), [BatchGen](https://www.usenix.org/conference/osdi26/presentation/xu-tairan), [Revisiting Pipeline Parallelism](https://www.usenix.org/conference/osdi26/presentation/hwang), [LMetric](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan), [Cloud-Grade SLOs for local MoE](https://www.usenix.org/conference/osdi26/presentation/wang-wenxin), [Sereno](https://www.usenix.org/conference/osdi26/presentation/xin), plus [UCCL-Tran](https://www.usenix.org/conference/osdi26/presentation/zhou-yang) — ten papers, one conference, all on the same page as 2019's kernel work.
- Why it matters: the research frontier and the production stack have converged to the point that a systems conference's programme reads like a deployment post-mortem.

## Three things that are just fun

- **Multiplication may be all you need.** [Simple Is Better (OSDI '26)](https://www.usenix.org/conference/osdi26/presentation/zhang-dingyan) replaces near-O(1) heap-based scheduling with a multiplication-based formulation — TTFT drops 92%/39% and TPOT 24%/51% in Alibaba's production, because the old schedulers spent their time in the wrong place entirely.
- **A playable world on one desktop GPU.** ABot-World-0's unit of interaction is a *raw keyboard action*, its unit of memory is ~19 GiB, and its failure mode is the world quietly drifting away from the one you were standing in. LongForcing is the paper's answer; nobody has a serving-stack answer yet.
- **Software eats the NIC.** [UCCL-Tran](https://www.usenix.org/conference/osdi26/presentation/zhou-yang) decouples the RDMA NIC's control path and runs it on host CPUs — up to 4.5× better collectives from a firmware-shaped problem solved in software.

## What this means for the repo

- The 43 directions held up: every signal above lands in an existing direction, and none demanded a new one. The five directions these signals stress hardest are **Agent & Workflow Serving**, **KV Transfer & Communication**, **Heterogeneous & Edge Serving**, **Diffusion & Non-AR Generation**, and **Kernel Automation & Tools**.
- Candidates for the next canonical round (not admitted here): ThunderAgent (ICML 2026 — `runtime-scheduling :: Agent & Workflow Serving`), KForge (`kernels-compilers :: Kernel Automation & Tools`), dLLM-Serve is already cross-indexed but deserves a canonical row, and ABot-World-0 (`decoding-acceleration :: Diffusion & Non-AR Generation`, preprint label).
- What to watch next: whether a serving stack ships *drift-aware* world-model rollout (signal 2), whether dLLM memory managers diverge from AR ones for good (signal 3), and whether anyone publishes a freshness-audited semantic cache at production scale (signal 8).

---

*Snapshot captured 2026-10-18 during the 669 → 784 discovery stage. Not a current paper count or a current frontier verdict. Reclassified on 2026-10-19: KV hierarchy, sparse/hybrid attention, semantic caching, fleet deployment and venue popularity are not standalone frontiers. Publication/status and linked author claims were not independently reproduced.*
