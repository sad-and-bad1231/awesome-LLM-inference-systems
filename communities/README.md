# Research labs & open-source communities

An engineering-first **source map** of inference open-source communities, maintainers and research labs. **Updated 2026-11-04:** entries are grouped by execution boundary, not GitHub popularity. A runtime is not a laboratory; collaborative projects are not exclusively company-owned. This is navigation, **not an additional canonical paper bibliography**, and no benchmark is independently reproduced here.

[← Home](../README.md) · [Companies](../organizations/README.md)

## Open-source systems — grouped by execution boundary

**43 unique source repos**, grouped by their primary role. The tag **community** means shared contributors, not company ownership. Direct links point to project upstreams; a GitHub repository is evidence of code, **not** proof of measured speedup, production use, or a fully supported accelerator.

### 1. LLM engines and local runtimes

| Project | Mechanism worth learning | Evidence / compatibility caveat |
|---|---|---|
| [vLLM](https://github.com/vllm-project/vllm) | Paged KV, continuous batching, speculative decoding, multi-device model execution | Active community; verify upstream/plugin version pairs |
| [SGLang](https://github.com/sgl-project/sglang) | RadixAttention, cache-aware scheduling, structured/agent serving | Active community; runtime/backend code paths differ |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | NVIDIA model execution, kernels, inflight batching, parallel inference | Vendor engine; NVIDIA-specific |
| [LMDeploy / TurboMind](https://github.com/InternLM/lmdeploy) | LLM compression and TurboMind C++/CUDA execution | Shanghai AI Lab / community; model and GPU support pinned |
| [DeepInfer](https://github.com/deepseek-ai/DeepInfer) | DeepSeek-native asynchronous runtime, EP, DSpark, optimized kernels | Open release is **offline**; not entire production control plane |
| [RTP-LLM](https://github.com/alibaba/rtp-llm) | Alibaba C++ inference scheduler, KV, LoRA, distributed engine | Alibaba source; not exclusively Qwen model team |
| [FastDeploy](https://github.com/PaddlePaddle/FastDeploy) | Paddle deployment / inference engine and accelerator adaptation | Different from PaddleNLP model definitions |
| [xLLM](https://github.com/xLLM-AI/xllm) | Cross-device serving framework and execution | Inspect supported backends; not universal hardware parity |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | GGML quantization, CPU/GPU memory orchestration and local decode | Local/single-host focus; strong reference for heterogeneous layouts |
| [MLC-LLM](https://github.com/mlc-ai/mlc-llm) | TVM-based portable LLM compilation, Web/Metal/mobile deployment | Device compiler stack differs from high-concurrency cloud serving |
| [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai) | Continuous batching, prefix cache and optimized CPU/XPU execution | Intel/OpenVINO backend; needs exact model/operator compatibility |
| [TGI — archive](https://github.com/huggingface/text-generation-inference) | Historical Rust/Python LLM server and optimized-generation patterns | **Archived 2026-03-21**; do not list as an active primary engine |

### 2. Cluster orchestration and routing

| Project | Mechanism worth learning | Evidence / compatibility caveat |
|---|---|---|
| [llm-d](https://github.com/llm-d/llm-d) | Kubernetes-native distributed P/D, KV-aware routing, EP and QoS | Community project; separate router, engine and gateway ownership |
| [llm-d Router](https://github.com/llm-d/llm-d-router) | Endpoint Picker, cache/load-aware request routing and P/D sidecar | **Current EPP / Objective / Rewrite home** |
| [Inference Gateway Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) | Gateway API InferencePool, protocol and conformance checks | Core EPP moved to llm-d-router; don't read old code as current |
| [AIBrix](https://github.com/vllm-project/aibrix) | Gateway, autoscaling, weight warmup, LoRA/cache and multi-engine control | vLLM-project control plane, not vLLM per-token scheduler |
| [Dynamo](https://github.com/ai-dynamo/dynamo) | Distributed inference router, transport, P/D, runtime coordination | NVIDIA ecosystem; hardware/backend support matrix applies |
| [Ray Serve LLM](https://github.com/ray-project/ray) | Multi-replica model orchestration, deployment/elastic scaling and routing | Ray control plane around selected token engines |
| [KServe](https://github.com/kserve/kserve) | Kubernetes model-serving API/controller/rollout infrastructure | Generic model platform; not itself a new attention kernel |

### 3. KV ownership, memory transfer and communication

| Project | Mechanism worth learning | Evidence / compatibility caveat |
|---|---|---|
| [Mooncake](https://github.com/kvcache-ai/Mooncake) | KV Transfer Engine, distributed store, multi-backend P/D and EP transport | Transport/storage layers; specify actual supported device/release |
| [LMCache](https://github.com/LMCache/LMCache) | Tiered/distributed KV reuse and cache connector integrations | External cache hit/miss and retrieval overhead ≠ model throughput |
| [NIXL](https://github.com/ai-dynamo/nixl) | Async device/host/NVMe transport for KV and disaggregated inference | Data transfer substrate, not cache policy or scheduler |
| [DeepEP](https://github.com/deepseek-ai/DeepEP) | Expert-parallel dispatch/combine, latency/throughput communication modes | Kernel/collective microbenchmarks are not Serving Goodput |
| [HYPIC](https://github.com/redai-studio/HYPIC) | Position-independent segment reuse in hybrid recurrent/full-attention models | SGLang fork and accuracy-sensitive seam recompute; preprint |

### 4. Kernels, DSLs, compilers and agentic optimization

| Project | Mechanism worth learning | Evidence / compatibility caveat |
|---|---|---|
| [FlashInfer](https://github.com/flashinfer-ai/flashinfer) | Serving-oriented attention/GEMM/MoE primitives and backend dispatch | Kernel coverage/performance depends on SM/dtype/shape |
| [FlashAttention](https://github.com/Dao-AILab/flash-attention) | IO-aware exact attention kernels; FA2/3/4 paths | Kernel-only results must be composed into engine benchmarks |
| [TileLang](https://github.com/tile-ai/tilelang) | Tile IR, scheduler, GEMM, MLA, sparse/recurrent attention, multi-backend | Ascend support specifically lists 950; **not** 910B2 parity |
| [Triton](https://github.com/triton-lang/triton) | Tiled GPU language/IR for custom inference kernels | Backend compiler/device support matters |
| [CUTLASS / CuTe DSL](https://github.com/NVIDIA/cutlass) | GEMM/attention tiling, pipelining, precision and SM-aware data movement | NVIDIA CUDA/SM-specific primitives |
| [ROCm AITER](https://github.com/ROCm/aiter) | AMD attention, MoE, low-bit GEMM and fused serving primitives | gfx and ROCm versions fixed per benchmark |
| [DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | Low-level MoE/GEMM and low-precision optimized kernels | GPU-specific; no universal vendor parity |
| [Humming](https://github.com/vllm-project/humming) | JIT typed quantized dense/MoE kernels with Ant × vLLM community | Different activation precision invalidates strict precision-equal A/B |
| [KDA](https://github.com/NVlabs/kda) | Domain-aware agentic CUDA kernel search and validation | Generated kernels ≠ full inference-engine speedup |
| [ForgeKernel](https://github.com/OpenBMB/ForgeKernel) | Hardware-profile-guided curriculum, repeated kernel evolution, reuse of knowledge | 2026-11-03 **preprint**, authors' claims; not proven self-improving LLM |
| [JustGoal](https://github.com/OpenBMB/JustGoal) | Goal-only coding agent baseline on specified kernel definitions | Same-model, single-shape vs full-shape comparisons required |
| [FlashInfer-Bench](https://github.com/flashinfer-ai/flashinfer-bench) | Inference kernel tasks, test/benchmark harness for generated code | Benchmark correctness and hidden shapes ≠ deployed serving |

### 5. Multimodal and hardware backend communities

| Project | Mechanism worth learning | Evidence / compatibility caveat |
|---|---|---|
| [vLLM-Omni](https://github.com/vllm-project/vllm-omni) | Multi-stage multimodal, real-time, video/action and diffusion serving | Stage semantics differ from text-only autoregressive loops |
| [SGLang-Omni](https://github.com/sgl-project/sglang-omni) | Composed omni/speech/duplex pipelines and stage-specific schedulers | Distinct codebase from ordinary SGLang text runtime |
| [vLLM-Ascend](https://github.com/vllm-project/vllm-ascend) | CANN/NPU model runner, kernel and communication integration | Community-owned; exact vLLM/CANN/NPU pair mandatory |
| [vLLM TorchTPU](https://github.com/vllm-project/vllm-torchtpu) | PyTorch TPU backend with Pallas kernels, model CI and vLLM scheduler | Google × Inferact collaboration; v7x main tested target |
| [TT-Metal / TT-NN](https://github.com/tenstorrent/tt-metal) | Tenstorrent accelerator kernel/collective model and LLM bring-up | Backend-specific; TT-LLK standalone repo is frozen |
| [torch_mlu](https://github.com/Cambricon/torch_mlu) | MLU PyTorch backend and device-op integration | Visible older branch docs; **not** current vLLM compatibility |
| [vllm-musa](https://github.com/MooreThreads/vllm-musa) | Moore Threads MUSA-specific vLLM port | Vendor fork; upstream support and model parity not assumed |

**Historical status checks:** [TGI archived 2026-03-21](https://github.com/huggingface/text-generation-inference); [Inference Gateway moved EPP APIs to llm-d-router](https://github.com/kubernetes-sigs/gateway-api-inference-extension); [TT-LLK development moved to tt-metal](https://github.com/tenstorrent/tt-llk). These statuses matter as much as feature lists.

**October 31 EMNLP source follow-up (zero additional institutional paper rows):** [Orthrus](https://aclanthology.org/2026.emnlp-main.28/) ([Illinois Data project](https://github.com/illinoisdata/Orthrus)) pairs embedding/generation kernels; [WG-KV](https://aclanthology.org/2026.emnlp-main.1063/) ([author code](https://github.com/EMCLab-Sinica/WG-KV)) introduces write-time KV admission; [Beyond-KV](https://aclanthology.org/2026.emnlp-main.526/) and [Seer](https://aclanthology.org/2026.emnlp-main.1852/) provide low-bit/semantic retrieval code. These are **EMNLP 2026 papers** already counted **once** under their decisive mechanisms; first-party lab/project pages are cross-references, not new bibliographic identities. Review [the 16-item October follow-up receipt](../reviews/OCTOBER_2026_FOLLOWUP_SWEEP_20261031.md).

## October 2026 lab/industry-research cross-check

**One paper, one canonical topic entry.** The following are **research-source cross-references**, not a separate count or a university ranking; published venue must be independently checked. Collab coauthorship ≠ lab-exclusive ownership.

| Group/source | October systems signal | Editorial disposition |
|---|---|---|
| [Stanford Hazy](https://hazyresearch.stanford.edu/) | [Next-Concept Modeling](https://arxiv.org/abs/2610.14162) (Oct 9) | **Already canonical** Decoding adjacent: a **new trained hierarchy/tokenizer**, not drop-in existing-model serving. |
| [MIT Han Lab](https://hanlab.mit.edu/) | [Quant VideoGen](https://proceedings.mlr.press/v306/xi26f.html) (ICML'26) and [VLASH](https://arxiv.org/abs/2512.01031) (IROS'26 lab listing) | **Already canonical** as video KV / embodied action-loop systems; retain scope. |
| [UW SyFI](https://syfi.cs.washington.edu/publications/) | [VibeSys 4×MI300A report](https://syfi.cs.washington.edu/blog/2026-10-08-qwen35-mi300a/) | **BLOG / ENGINEERING**, not a new paper or independent GPU reproduction. |
| [SOSP'26 / expert-parallel collaborations](https://sigops.org/s/conferences/sosp/2026/schedule.html) | [StreamEP](https://doi.org/10.1145/3830418.3843869) | **New canonical** MoE; specific 16-GPU/NCCL network constraints, original author [artifact](https://zenodo.org/records/22100357). |
| [UW / ByteDance Seed collaborators](https://sigops.org/s/conferences/sosp/2026/schedule.html) | [TensorHub](https://arxiv.org/abs/2604.09107) SOSP'26 | **New canonical ADJACENT** distributed GPU-resident RL policy weight updates; not online request KV transport. |
| [SOSP'26 / voice-serving group](https://sigops.org/s/conferences/sosp/2026/schedule.html) | [llmovoice](https://doi.org/10.1145/3830418.3843860) | **New canonical ADJACENT** voice context orchestration; changes generated behavior and session cost. |
| [CMU InfiniAI](https://www.infini-ai-lab.cmu.edu/publications.html) | [FlashRT](https://arxiv.org/abs/2607.18171), [STAPLE](https://arxiv.org/abs/2610.12599) | FlashRT **already canonical**, STAPLE **HOLD** for model/upcycling/system attribution. |
| [Berkeley Sky](https://sky.cs.berkeley.edu/publications/) | [CommBench](https://arxiv.org/abs/2608.04450), [FreeToken](https://arxiv.org/abs/2608.16157) | **Already canonical**; institutional alias must not cause another row. |

Official October venues: SOSP published, EMNLP 2026 [ACL Anthology](https://aclanthology.org/volumes/2026.emnlp-main/), NeurIPS 2026 [accepted-program listing](https://neurips.cc/Downloads/2026) is **not yet a published proceedings full paper** by Oct 31. [Full source-gated monthly report](../reviews/OCTOBER_2026_MONTHLY_SWEEP_20261031.md).

## Research labs and source-linked systems signals

This is a **navigation crosswalk, not a second paper bibliography or institutional ranking**. A paper appears in an [existing canonical topic](../topics/README.md) only once, regardless of how many labs collaborated. A **BLOG/ENGINEERING** signal is not automatically a peer-reviewed paper, and **REVIEW/HOLD** is not admission.

| Research group | Inference-system focus | Representative verified source and its status |
|---|---|---|
| [UC Berkeley Sky](https://sky.cs.berkeley.edu/publications/) | Cloud inference, edge MoE and distributed serving | [CommBench](https://arxiv.org/abs/2608.04450) and [FreeToken](https://arxiv.org/abs/2608.16157) — **TOPIC**, already indexed; collaboration does not imply exclusive lab ownership |
| [LMSYS / SGLang](https://lmsys.org/) | Runtime, speculative decoding, serving infrastructure | [SGLang project](https://github.com/sgl-project/sglang) — **ENGINEERING**; separately cite published papers where applicable |
| [Stanford Hazy](https://hazyresearch.stanford.edu/) | IO-aware attention and generation mechanisms | [NCM](https://arxiv.org/abs/2610.14162) — **TOPIC / ADJACENT**; different trained model/tokenizer, not an existing-LLM kernel speedup |
| [MIT HAN Lab](https://hanlab.mit.edu/) | Quantization, efficient kernels, edge/video/robot inference | [Quant VideoGen](https://proceedings.mlr.press/v306/xi26f.html) — **TOPIC / ICML 2026 / ADJACENT**; [VLASH](https://arxiv.org/abs/2512.01031) — **TOPIC / VLA-ADJACENT**, lab-listed IROS |
| [Tsinghua PACMAN](https://pacman.cs.tsinghua.edu.cn/) | AI compilers, GPU/NPU mapping, parallel runtime | [Group publication source](https://pacman.cs.tsinghua.edu.cn/~zjd/publication/) — **DISCOVERY**; verify final venue and exact hardware per paper |
| [SJTU IPADS](https://ipads.sjtu.edu.cn/pub/publication) | OS, storage, distributed inference and reproducible evaluation | [Group publications](https://ipads.sjtu.edu.cn/pub/publication) — **DISCOVERY**; CHIME remains **REVIEW** pending hardware-scope clarity |
| [ETH Zurich SPCL](https://spcl.inf.ethz.ch/Publications/) | HPC collectives, communication and performance modeling | [Official publications](https://spcl.inf.ethz.ch/Publications/) — **DISCOVERY/REFERENCE**, not automatic LLM Serving admission |
| [UW SyFI](https://syfi.cs.washington.edu/publications/) | FlashInfer, agentic serving and multimodal execution | [VibeSys](https://syfi.cs.washington.edu/blog/2026-10-08-qwen35-mi300a/) and [ServingStudio](https://syfi.cs.washington.edu/blog/2026-09-24-introducing-servingstudio/) — **BLOG/ENGINEERING**, no invented formal paper identity |
| [CMU InfiniAI](https://www.infini-ai-lab.cmu.edu/publications.html) | Program IR and agent-driven distributed multimodal inference | [FlashRT](https://arxiv.org/abs/2607.18171) — **TOPIC / PREPRINT**; distinct from FlashRT-PAI. [STAPLE](https://arxiv.org/abs/2610.12599) remains **HOLD** for system/architecture attribution |

## Additional research source nodes — November 2026

These are **12 additional source nodes** (university labs, named collaborations and first-party research groups), **not 12 newly founded laboratories**. A multi-university paper does not establish one institute's exclusive authorship. Source status describes evidence level, not replication.

| Group / collaboration | Why follow | Source and qualification |
|---|---|---|
| [Stanford MAST](https://mast.stanford.edu/pubs/) | Agentic GPU correctness/DSL, sparse KV, resilient serving | [ARGUS (SOSP 2026)](https://mast.stanford.edu/pubs/argus_agentic_gpu_optimization_guided_by_data_flow_invariants/) and HiSparse: **LAB/PUBLISHED**; works are coauthored, not solely lab-owned |
| [University of Chicago SEIS authors](https://nehzux.github.io/SEIS/) | Long-horizon agent optimization of an entire mini-SGLang engine | [SEIS](https://arxiv.org/abs/2610.04646): **PREPRINT / ARTIFACT**; engine evolves, the foundation agent does not |
| [PKU TileLang research collaboration](https://github.com/tile-ai/tilelang) | Tiled compiler IR, lowering, scheduling, multi-accelerator kernels | [TileLang](https://github.com/tile-ai/tilelang): **CODE / GROUP-AUTHORED**; includes collaborators beyond PKU |
| [OpenBMB / Tsinghua collaboration](https://github.com/OpenBMB/ForgeKernel) | Cross-run kernel-agent knowledge and architecture evolution | [ForgeKernel](https://arxiv.org/abs/2611.04998): **2026-11-03 PREPRINT**; [JustGoal](https://github.com/OpenBMB/JustGoal) is separate; external coauthors credited |
| [Shanghai AI Laboratory / OpenMMLab](https://www.shlab.org.cn/open) | TurboMind/LMDeploy, model-serving and mixed-precision compiler/kernel systems | [LMDeploy](https://github.com/InternLM/lmdeploy) **CODE**; EuroSys 2027 acceptance is not 2026 proceedings |
| [HKUST IE Lab](https://ielab.hkust.edu.hk/LLM-inference.html) | KV-constrained queues and memory-aware serving policy | [cμ scheduling](https://ielab.hkust.edu.hk/LLM-inference.html) **LAB RESEARCH / TRACE**; claims require workload and policy verification |
| [KAIST INA Lab](https://ina.kaist.ac.kr/projects/specedge/) | Edge-assisted speculative draft / server verification with network overlap | [SpecEdge](https://ina.kaist.ac.kr/projects/specedge/) **NeurIPS 2025** lab source; edge setting, not commodity datacenter serving |
| [Korea University CSL](https://sites.google.com/korea.ac.kr/csl) | LLM serving, accelerator architecture and systems profiling | **LAB/DISCOVERY**; research agenda is not evidence of a particular deployed engine |
| [UIUC IllinoisData / Orthrus collaborators](https://github.com/illinoisdata/Orthrus) | Embedding–generation server composition and workload-specific inference | [Orthrus](https://aclanthology.org/2026.emnlp-main.28/) **EMNLP 2026 / CODE**; multi-author project |
| [Georgia Tech Sarathi-Serve authors](https://www.usenix.org/conference/osdi24/presentation/agrawal) | Chunked prefill and stall-free serving scheduling | **OSDI 2024 / FOUNDATION**; institution/collaboration, not a separately branded lab |
| [Seoul National University / Orca authors](https://www.usenix.org/conference/osdi22/presentation/yu) | Iteration-level batching and selective execution foundational to online serving | **OSDI 2022 / FOUNDATION**; historical origin, not current lab product |
| [Google Research TPU inference authors](https://research.google/pubs/ragged-paged-attention-a-high-performance-and-flexible-llm-inference-kernel-for-tpu/) | Pallas ragged paging and profile-driven distributed optimization | [RPA](https://research.google/pubs/ragged-paged-attention-a-high-performance-and-flexible-llm-inference-kernel-for-tpu/) and [PROMPTS](https://research.google/pubs/prompts-performance-optimization-via-multi-agent-planning-for-llm-training-and-serving/) **FIRST-PARTY PAPERS**; team-level credit, not Gemini serving source |

**Latest high-information signals:** [UW SyFI's 2026-11-04 VibeSys Trainium2 experiment](https://syfi.cs.washington.edu/blog/2026-11-04-vibesys-trainium/) and [ServingStudio](https://syfi.cs.washington.edu/blog/2026-09-24-introducing-servingstudio/) address **agent-driven model×hardware search and simulation-to-real evaluation**; [Stanford MAST ARGUS](https://mast.stanford.edu/pubs/argus_agentic_gpu_optimization_guided_by_data_flow_invariants/) addresses dense compiler correctness feedback; [ForgeKernel](https://arxiv.org/abs/2611.04998) examines iterative kernel evolution. Performance results remain authors' claims and incomparable across separate hardware/workloads.

**Status vocabulary:** **TOPIC** = indexed paper in one of eight topic tables; **FOUNDATION** = intentionally on the homepage; **ENGINEERING/BLOG** = software or first-party technical post; **DISCOVERY/REFERENCE** = useful source, no automatic admission; **REVIEW/HOLD** = insufficient source/evaluation/fit. Sub-labels such as *ADJACENT* or *PREPRINT* state scope and publication status, not reproduction.

Previous dated per-lab work lists and their explanations: [archived Oct 25/30 signals](../reviews/archive/LAB_SIGNALS_20261030.md). The [Oct 30 G0–G5 review](../reviews/ARXIV_LAB_SWEEP_20261030.md) owns individual KEEP/HOLD decisions. Update the canonical **paper row**, not a second paper inventory here.
