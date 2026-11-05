# November 4, 2026 — inference organizations, research labs & open-source systems sweep

**Scope.** Extend the engineering-first inference source map beyond foundation-model labs, based on original software, engineering reports and actual research-group pages. **Deliverables:** 7 new organization profiles (1 China / 6 US), 43 grouped public inference-related repositories in [Communities](../communities/README.md) (**total across five groups, not 43 newly discovered**), 12 additional institution/collaboration research **source nodes** (not necessarily twelve independently established labs), and a correction to [ForgeKernel's formerly unresolved identity](../frontiers/README.md). China index 18→19; US index 23→29. No new canonical-paper rows and no measured speedup replication.

## Scope / evidence discipline

A candidate needs a direct link to **first-party code, a named research-group project/publication page, or a documented production inference system**. Every entry describes one reusable execution contract and the important source limitation. **CODE** means source exists; it does not certify production usage. **PUBLISHED** does not prove artifact reproducibility. **PREPRINT** is not final proceedings. **HISTORICAL/ARCHIVED** must not be called an active mainline project. **COLLABORATION** prevents attributing a community repository to a single employer or university.

We group by **engine, control plane, KV/communication, compiler/kernel or multimodal/backend**. These are learning paths, **not new canonical paper categories** and not a parallel paper inventory. Kernels, RL-rollout systems, local single-device engines, distributed gateways and hosted-model APIs have different performance contracts.

## Open-source: newly material coverage

| Systems boundary | Representative primary sources | Important correctness / version question |
|---|---|---|
| Engine & portable local runtime | [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), [DeepInfer](https://github.com/deepseek-ai/DeepInfer), [LMDeploy](https://github.com/InternLM/lmdeploy), [llama.cpp](https://github.com/ggml-org/llama.cpp), [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai) | Offline DeepInfer drop vs online serving, model/precision/backend compatibility, local memory policies vs cloud Goodput. |
| Routing, disaggregated service & autoscaling | [llm-d](https://github.com/llm-d/llm-d), [llm-d Router](https://github.com/llm-d/llm-d-router), [Inference Gateway](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [AIBrix](https://github.com/vllm-project/aibrix), [Dynamo](https://github.com/ai-dynamo/dynamo), [Ray Serve](https://github.com/ray-project/ray) | Distinguish engine scheduler from endpoint routing, resource topology and failure recovery; versioned moved APIs. |
| KV and communications | [Mooncake](https://github.com/kvcache-ai/Mooncake), [LMCache](https://github.com/LMCache/LMCache), [NIXL](https://github.com/ai-dynamo/nixl), [DeepEP](https://github.com/deepseek-ai/DeepEP), [HYPIC](https://github.com/redai-studio/HYPIC) | KV identity, lifetime/isolation, transport fallback, cross-request reuse and hybrid recurrent state correctness. |
| Kernel/compiler/autonomous optimization | [FlashInfer](https://github.com/flashinfer-ai/flashinfer), [FlashAttention](https://github.com/Dao-AILab/flash-attention), [TileLang](https://github.com/tile-ai/tilelang), [Triton](https://github.com/triton-lang/triton), [CUTLASS](https://github.com/NVIDIA/cutlass), [AITER](https://github.com/ROCm/aiter), [KDA](https://github.com/NVlabs/kda), [ForgeKernel](https://github.com/OpenBMB/ForgeKernel), [JustGoal](https://github.com/OpenBMB/JustGoal), [FlashInfer-Bench](https://github.com/flashinfer-ai/flashinfer-bench) | Correctness, hidden shapes, equal precision, search budget, cross-kernel composition and engine-level verification. |
| Multi-stage/backends | [vLLM-Omni](https://github.com/vllm-project/vllm-omni), [SGLang-Omni](https://github.com/sgl-project/sglang-omni), [vLLM-Ascend](https://github.com/vllm-project/vllm-ascend), [vLLM-TorchTPU](https://github.com/vllm-project/vllm-torchtpu), [TT-Metal](https://github.com/tenstorrent/tt-metal) | Runtime stage ownership, hardware generation, backend ABI, CANN/driver and per-model support matrix. |

### Three status corrections (important)

1. **[TGI](https://github.com/huggingface/text-generation-inference)** is archived (owner timestamp **2026-03-21**); a historical Rust/Python serving reference, not a live engineering target.
2. The [Inference Gateway Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) moved its **Endpoint Picker / InferenceObjective / InferenceModelRewrite** implementations into [llm-d-router](https://github.com/llm-d/llm-d-router). The InferencePool API/protocol remains with the Gateway repo. Read current code in the correct owner.
3. Tenstorrent's [TT-LLK](https://github.com/tenstorrent/tt-llk) repository is frozen; its maintained low-level kernels moved into [tt-metal](https://github.com/tenstorrent/tt-metal).

## Labs/research source highlights

| Source group | Link | Reusable systems question |
|---|---|---|
| UW SyFI | [Publications](https://syfi.cs.washington.edu/publications/) · [Trainium2 VibeSys (Nov 4)](https://syfi.cs.washington.edu/blog/2026-11-04-vibesys-trainium/) | Agent-written engines on under-served hardware; fair baseline/optimizer budget, compiler + runtime generation. |
| Stanford MAST | [Publications](https://mast.stanford.edu/pubs/) · [ARGUS](https://mast.stanford.edu/pubs/argus_agentic_gpu_optimization_guided_by_data_flow_invariants/) | Compiler-level data-flow invariants and counterexample-guided GPU kernel agent. |
| University of Chicago SEIS authors | [Paper](https://arxiv.org/abs/2610.04646) · [project](https://nehzux.github.io/SEIS/) | Long-lived code/history inheritance improves a miniature engine; fixed agent does **not** prove RSI. |
| Tsinghua/OpenBMB multi-institution authors | [ForgeKernel code](https://github.com/OpenBMB/ForgeKernel) · [2026-11-03 preprint](https://arxiv.org/abs/2611.04998) | Profiling-grounded search, architecture/milestone curriculum, knowledge across runs; kernel ≠ engine. |
| Peking University collaborators | [TileLang](https://github.com/tile-ai/tilelang) | Multi-backend kernel compiler, tiling and lowering; verify claims specifically for Ascend 950. |
| Shanghai AI Lab | [Official OSS](https://www.shlab.org.cn/open) · [LMDeploy](https://github.com/InternLM/lmdeploy) | Mixed-precision inference and TurboMind deployment; not a new model API listing. |
| HKUST IE Lab | [KV-aware cμ scheduling](https://ielab.hkust.edu.hk/LLM-inference.html) | Memory-constrained queue theory with trace replay; real engine settings matter. |
| KAIST INA | [SpecEdge](https://ina.kaist.ac.kr/projects/specedge/) | Edge/server speculative decode and network overlap. |
| Korea University CSL | [Lab statement](https://sites.google.com/korea.ac.kr/csl) | LLM engine and accelerator co-design (discovery agenda, not a documented deployed engine). |
| UIUC IllinoisData authors | [Orthrus](https://github.com/illinoisdata/Orthrus) · [EMNLP](https://aclanthology.org/2026.emnlp-main.28/) | Embedding/generation co-execution; multi-institution source, not independent paper admission. |

Other retained group entry points in Communities: UC Berkeley Sky, LMSYS/SGLang, MIT HAN, Stanford Hazy, Tsinghua PACMAN, SJTU IPADS, ETH SPCL, CMU InfiniAI, Google Research, Georgia Tech Sarathi-Serve, Seoul National University Orca and UW SyFI.

## Newly admitted organizations (source profiles, **not** papers)

| Region | Organization | Public implementation/evidence | Status limitation |
|---|---|---|---|
| China | [Cambricon](../organizations/Cambricon.md) | [torch_mlu](https://github.com/Cambricon/torch_mlu) | Historic device-PyTorch backend docs; not a current vLLM compatibility result. |
| US | [Hugging Face](../organizations/Hugging-Face.md) | Transformers/Optimum + archived TGI | Hosting models does not imply owning architectures; TGI status explicitly historical. |
| US | [Inferact](../organizations/Inferact.md) | [Inferact × Google TorchTPU](https://vllm.ai/blog/2026-10-20-vllm-torchtpu) | Shared vLLM community implementation. |
| US | [RadixArk](../organizations/RadixArk.md) | [RadixArk × Google SGLang TorchTPU](https://developers.googleblog.com/en/announcing-new-vllm-and-sglang-inference-engines-on-tpu/) | Shared SGLang community. |
| US | [Tenstorrent](../organizations/Tenstorrent.md) | [TT-Metal / TT-NN](https://github.com/tenstorrent/tt-metal) | Device-specific; TT-LLK standalone is frozen. |
| US | [IBM](../organizations/IBM.md) | [llm-d](https://github.com/llm-d/llm-d), historic Spyre backend | No sole ownership of llm-d; Spyre plugin archived in 2025. |
| US | [BentoML](../organizations/BentoML.md) | [BentoML serving framework](https://github.com/bentoml/BentoML) | Deployment/service integration, not core token-kernel innovation. |

## Existing Frontier identity correction

**ForgeKernel is no longer an unresolved discovery name.** [Official repo](https://github.com/OpenBMB/ForgeKernel) and [arXiv preprint](https://arxiv.org/abs/2611.04998) are distinct from [JustGoal](https://github.com/OpenBMB/JustGoal) and unrelated [Kernel Forge](https://arxiv.org/abs/2607.24762). Authors report results on GPUs and Ascend operator benchmarks. No trusted public evidence here establishes **self-sustaining recursive improvement of an LLM optimizer**, nor verified end-to-end vLLM/SGLang improvements on Ascend 910B2.

## Explicit HOLD / non-admission

Do not add: generic agent frameworks, chatbot UI wrappers, RAG vector stores, ordinary model-hosting catalogs, uncertain GitHub look-alikes, training-only model releases, and unverified claims of private schedulers/kernels. University/group projects without precise primary publications remain **DISCOVERY**. Cross-listed collaborations do not become independent labs or duplicate canonical bibliography entries.

**Reproduction:** not_attempted across this sweep. Future evaluation must separate kernel microbench, simulated serving, engine end-to-end Goodput, and cluster-level SLO; pin model, prompt/length distribution, dtype, backend commits, hardware, allocator topology and verifier. This is a navigation/source-audit update, not a claim of total coverage or published performance superiority.
