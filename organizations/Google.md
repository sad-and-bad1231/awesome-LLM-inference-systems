# Google

A source-scoped map of Google's **inference kernels, TPU-native serving stacks, and agent-assisted infrastructure optimization**, plus publicly documented model architecture. This is not an account of Google's undisclosed Gemini production serving code.

[← Organizations](../README.md#organizations)

## Official Gemini and Gemma model portfolio (2026-10-24)

**Authorities:** [Gemini API complete model catalog](https://ai.google.dev/gemini-api/docs/models), [Gemma releases](https://ai.google.dev/gemma/docs/releases), [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4). This distinguishes **closed Gemini API IDs** from **downloadable Gemma weights**.

| Publicly listed family | Sub-models and inference implications | Official source |
|---|---|---|
| Gemini 4 | Gemini **4 Argon**, next flagship API family | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini 3 | 3.8 Flash; 3.6 Flash; 3.5 Flash-Lite; 3.1 Flash-Lite and older Pro/Flash preview entries | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini Live / speech | 3.8 Live, 3.8 Live Extended Thinking, 3.5 Live Translate, 3.8 Flash/Flash-Lite TTS, 3.5 Transcribe | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini 2.5 | 2.5 Pro, Flash, Flash-Lite and audio versions (generation lineage; not new 2026 releases) | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemini media and tools | Nano Banana image family, Gemini Omni Flash video, Lyria music, Deep Research, Robotics ER, Gemini Embedding | [Gemini API catalog](https://ai.google.dev/gemini-api/docs/models) |
| Gemma 4 | **E2B, E4B, 12B Unified, 26B A4B MoE, 31B Dense**; small-device/per-layer embeddings, attention variants, MTP edition | [Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4) |
| Other Gemma specializations | Gemma 3/3n, EmbeddingGemma 2, FunctionGemma, TranslateGemma, MedGemma, ShieldGemma | [Gemma release history](https://ai.google.dev/gemma/docs/releases) |

**Full API ID scope:** the provider catalog also lists preview, retired, embedding, media and agent-specific endpoints. Use the linked official model catalog for the full and changeable *exact ID* inventory; individual service IDs are not standalone systems papers.

## Foundational techniques and models

| Work | Inference relevance | Primary source |
|---|---|---|
| **Multi-Query Attention (MQA)** (2019) | Sharing key/value heads reduces autoregressive decode KV bandwidth. | [Paper](https://arxiv.org/abs/1911.02150) |
| **Efficiently Scaling Transformer Inference** (MLSys 2023) | TPU parallelism and performance-model-guided latency/throughput engineering. | [MLSys](https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html) |
| **Speculative Decoding** (ICML 2023) | Draft-and-verify decoding while preserving the target distribution. | [PMLR](https://proceedings.mlr.press/v202/leviathan23a.html) |
| **Grouped-Query Attention (GQA)** (EMNLP 2023) | Attention-head grouping trades off decode bandwidth and model quality. | [ACL Anthology](https://aclanthology.org/2023.emnlp-main.298/) |
| **Gemma family** | Open-weight architectures and deployment examples; model design, **not** a disclosed Google production serving stack. | [Official models/docs](https://ai.google.dev/gemma/docs) |

## TPU inference infrastructure and optimization

| Project | Role | Official source |
|---|---|---|
| **TorchTPU (2026)** | Native PyTorch `tpu` backend with ATen ops, XLA/`torch.compile`, distributed collectives and TPU-specific kernel integration; a supported **backend**, not automatic transfer of CUDA kernels. | [Google engineering launch](https://developers.googleblog.com/en/announcing-new-vllm-and-sglang-inference-engines-on-tpu/) · [source](https://github.com/google-pytorch/torch_tpu) |
| **vLLM-TorchTPU / SGLang-TorchTPU (2026-10-20)** | Google with **Inferact** (vLLM) and **RadixArk** (SGLang) integrated native PyTorch-based serving, Pallas custom ops, KV/parallelism paths and common engine schedulers. Their product announcement includes a TPU7x/AgentX performance claim, not a cross-backend speedup. | [First-party engineering report](https://developers.googleblog.com/en/announcing-new-vllm-and-sglang-inference-engines-on-tpu/) · [vLLM backend](https://github.com/vllm-project/vllm-torchtpu) · [SGLang backend](https://github.com/sgl-project/sglang-torchtpu) |
| **Ragged Paged Attention (2026)** | Pallas/Mosaic TPU kernel for dynamic ragged KV access, fused KV updates and distribution-aware prefill/decode specialization; the authors report real TPU7x kernel measurements. **Kernel/JAX-XLA baseline improvements are not end-to-end engine throughput.** | [Google Research paper page](https://research.google/pubs/ragged-paged-attention-a-high-performance-and-flexible-llm-inference-kernel-for-tpu/) |
| **JetStream** | High-throughput LLM inference engine targeting TPU-oriented deployments. | [GitHub](https://github.com/google/JetStream) |
| **SAX / SAXML** | Scalable JAX/TPU model-serving platform. | [GitHub](https://github.com/google/saxml) |
| **MaxText** | Open JAX/TPU LLM implementation with generation/inference paths; also a training framework. | [GitHub](https://github.com/google/maxtext) |
| **Gemma.cpp** | Lightweight C++ inference for Gemma on resource-constrained devices. | [GitHub](https://github.com/google/gemma.cpp) |

## Distributed serving topology: Google contributors to llm-d

| Engineering source | Executed contribution | Attribution / validation limit |
|---|---|---|
| [Topology as an End-to-End Contract](https://llm-d.ai/blog/topology-as-an-end-to-end-contract) (2026-10-29; Google engineers, llm-d project) | Treat **GPU ↔ NIC ↔ RoCE rail ↔ Prefill/Decode replica ↔ Router** mapping as a cross-layer constraint. On GKE H200/B200/GB200/GB300, describes RDMA bring-up, topology-aware KV handoff and request pairing. | **Cross-company llm-d engineering**, not proprietary Gemini serving; the reported H200 TTFT benefit came from a two-node benchmark and a **prototype** rail-locality scorer, not automatically the shipped router policy. |
| [llm-d project](https://github.com/llm-d/llm-d) | Google Cloud is a founding collaborator on the Kubernetes-native control plane with Red Hat, IBM Research, CoreWeave and NVIDIA. | A shared open-source organization; do not claim every component was Google-authored. |

**Engineering insight:** a correct RDMA topology is not enough: the allocator must preserve GPU/NIC affinity, transport must confirm real RDMA instead of TCP fallback, and routing must choose feasible P/D pairs. Evaluate topology and queueing jointly rather than attributing network improvements to a kernel.

## Algorithm discovery / RSI-adjacent infrastructure research

| Public work | Executed mechanism and evidence | Boundary / research implication |
|---|---|---|
| **[AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)** (DeepMind, 2025) | Gemini-backed code candidate generation + programmatic evaluators + evolutionary search for algorithms; Google reports use in TPU circuit-design optimization and infrastructure heuristics. | **Algorithm/code evolution, not demonstrated recursive weight/model self-improvement**, nor direct evidence of autonomously evolving vLLM/SGLang production engines. |
| **[AlphaEvolve infrastructure follow-up](https://deepmind.google/blog/alphaevolve-impact/)** (2026) | First-party report describes TPU design and cache policy improvements; [Google Cloud GA announcement](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-on-cloud/) documents a customer-accessible algorithm optimization service. | A deployed algorithm optimizer is evidence of optimization *capability* and operational investment; absence of matched-budget, held-out inference-engine experiments prevents an RSI-on-serving claim. |

**Research crosswalk:** [Autonomous inference-engine evolution](../frontiers/README.md#autonomous-inference-engine-evolution-separate-engine-evolution-from-rsi) is the relevant frontier. Google demonstrates a strong **general-purpose evaluator-guided optimization loop**, while [SEIS](https://arxiv.org/abs/2610.04646) and [Together Compiler](https://www.together.ai/blog/together-compiler-continual-compilation-for-ai-inference) are closer to explicit **inference-engine** evolution. Do not conflate the three.

**Boundary.** Selected Google-authored first-party and explicitly credited partner projects, not all Google Cloud managed model endpoints or Google's unpublished Gemini serving architecture. TPU benchmarks are specific to model, hardware, backend, shapes and baseline; **no independent reproduction claimed here**.
