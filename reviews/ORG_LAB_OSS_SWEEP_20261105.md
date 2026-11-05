# 2026-11-05 UTC — broad inference infrastructure and research-source follow-up

**Scope:** a source-backed *incremental* sweep after [2026-11-04 Organizations/Labs/OSS](ORG_LAB_OSS_SWEEP_20261104.md). The goal is useful **executed inference mechanisms**, not a directory of every company that hosts AI models.

**Result:** **33 additional unique repositories** in the [five-layer community index](../communities/README.md), **43 → 76**; **10 additional named research/maintainer source nodes**, now **22 across the two dated November addenda**; **1 new company profile** ([Modular](../organizations/Modular.md)), and **3 existing company pages corrected or enriched** (JD.com, AMD, Huawei). Organizations now **19 China / 30 US**. We did **not** add canonical papers, increase the Frontier count, or run benchmarks. Source/identity review is **not hardware reproduction**.

## Methods and inclusion rules

- **Primary source:** GitHub project upstream, author-maintained artifact, formal proceedings or the original organization's engineering documentation. For new repositories, independently resolve each GitHub repository owner and inspect its public or archived status. Avoid third-party awesome lists as standalone proof.
- **One executable role per record:** inference engine, orchestration, KV/transport, kernel/compiler/verification, multimodal/device backend. A named project can span roles; it appears **once** in its primary role. Do not claim that multiple independent commercial deployments use it merely because it is open source.
- **Status:** COMPANY FIRST-PARTY, MULTI-ORG COMMUNITY, UNIVERSITY ARTIFACT, PREPRINT, PUBLISHED, PRODUCT/SERVICE, or SOURCE-ONLY. Authors' self-reported benchmark numbers are not independently verified.
- **System attribution:** serving E2E Goodput, operator microbench, model-quality change, quantization scheme, hardware/compiler support and distributed network performance are different comparison units.

## High-information incremental code arrivals

| Source | What to read and why | Important boundary |
|---|---|---|
| [ModelTC LightLLM](https://github.com/ModelTC/LightLLM) | Token-level KV management, pure-Python scheduling, hybrid model and P/D workflows | Active **CODE**; author performance claims workload-specific |
| [Tsinghua PACMAN Chitu](https://github.com/thu-pacman/chitu) | Real Ascend 910B, NVIDIA and domestic accelerator serving; multimode P/D; FP4→FP8/BF16 conversion | **CODE** and first-party release notes; exact CANN/model parity needs tests |
| [Modular MAX](https://github.com/modular/modular) | Mojo DSL → graph compiler → runtime → online inference server within one project | Vendor **PARTLY OPEN COMPONENTS**; confirm separate licenses and target GPU |
| [ROCm ATOM](https://github.com/ROCm/ATOM) | AITER kernels, two-batch overlap, EP/TP/DP and P/D disaggregation | AMD **CODE**; not independent vendor-neutral speedup |
| [JD xLLM Service](https://github.com/xLLM-AI/xllm-service) | Cluster-serving controller around xLLM engine, failure rescheduling and resource orchestration | JD-accredited **CODE**; not proof exact JoyMaaS runtime deployment |
| [KTransformers](https://github.com/kvcache-ai/ktransformers) | SOSP'25 CPU–GPU heterogeneous MoE runtime, packed experts, CPU/GPU memory | MADSys **PAPER + CODE** with external contributors; mixed inference/SFT tree |
| [M*](https://github.com/mstar-project/mstar) | Multimodal component graph/walk scheduling, per-component resources | Stanford/UW **PREPRINT + CODE**; modality-specific results and external baselines |
| [Prism](https://www.usenix.org/conference/osdi26/presentation/yu-shan) · [code](https://github.com/Multi-LLM/prism-research) · [kvcached](https://github.com/ovg-project/kvcached) | Cross-model GPU ballooning, elastic virtual/physical memory, two-level model scheduling | **OSDI'26 PAPER + ARTIFACT**; production usage is author-reported |
| [MORI](https://github.com/ROCm/mori) | EP, IO, SHMEM and RDMA/IR interface; KV transfer + NIC/topology-aware dispatch | AMD **CODE**; link state and transport fallback must be verified |
| [LeaderWorkerSet + DisaggregatedSet](https://github.com/kubernetes-sigs/lws) | Multi-node GPU-group topology, rollout, recovery, P/D lifecycle | Kubernetes **SIG CODE**; a cluster CRD, not per-token inference kernel |
| [KAITO](https://github.com/kaito-project/kaito) · [KubeRay](https://github.com/kuberay-project/kuberay) | Model-based node provisioning and Ray-cluster serving operations | **COMMUNITY CODE**; no direct accelerator speedup |
| [SpecForge](https://github.com/sgl-project/SpecForge) · [vLLM Speculators](https://github.com/vllm-project/speculators) | Reproducible draft/MTP training, online hidden-state distribution, verifier deployment | **COMMUNITY CODE**; draft acceptance/quality changes and hardware budgets must be measured |
| [EAGLE](https://github.com/SafeAILab/EAGLE) | Historical speculative decoding draft generation and verification method | **RESEARCH CODE**; not an entire Serving Engine |
| [SGL Kernel NPU](https://github.com/sgl-project/sgl-kernel-npu) · [SGL Kernel XPU](https://github.com/sgl-project/sgl-kernel-xpu) | Independent, backend-specific implementations of MLA/GDN/MoE and attention | **MULTI-CONTRIBUTOR CODE**; Ascend 950/Intel XPU features do not imply 910B2 parity |
| [DeepGEMM Ascend](https://github.com/deepseek-ai/DeepGEMM-Ascend) · [TorchNPU](https://github.com/Ascend/pytorch) | Ascend GEMM/MoE implementations, PyTorch PrivateUse1 and memory/stream integration | **DEVICE-SPECIFIC CODE**, TorchNPU GitHub is mirror; pin CANN/runtime |
| [DynaFlow](https://github.com/uw-syfi/DynaFlow) · [Ekka](https://github.com/amazon-science/automated-diagnosis-of-silent-errors-in-llm-inference) | Programmable operator overlap and differential inference debugging | **MLSys 2026 / RESEARCH CODE**; Ekka detects errors, not throughput gains |
| [vLLM-Metal](https://github.com/vllm-project/vllm-metal) · [MLX LM](https://github.com/ml-explore/mlx-lm) | vLLM paged attention adapter, native MLX/Metal model execution and local cache | **APPLE DEVICE CODE**; local memory and concurrency differ from datacenter GPU serving |
| [LLM Compressor](https://github.com/vllm-project/llm-compressor) · [BitNet](https://github.com/microsoft/BitNet) | Quantized weight/activation/KV and ternary model-specific inference | **MODEL/FORMAT-CHANGING**; accuracy/precision parity required |
| [Transformer Engine](https://github.com/NVIDIA/TransformerEngine) · [NCCL](https://github.com/NVIDIA/nccl) · [NVSHMEM](https://github.com/NVIDIA/nvshmem) | FP8/FP4 fused tensor kernels, topology collectives, GPU-initiated transfers | Infrastructure dependencies, not individually new online serving engines |

Other admitted and linked individual projects: [Ollama](https://github.com/ollama/ollama), [vLLM semantic-router](https://github.com/vllm-project/semantic-router), [Apache TVM](https://github.com/apache/tvm), [SGLang JAX](https://github.com/sgl-project/sglang-jax), and [ROCm/ATOM](https://github.com/ROCm/ATOM). These cover local serving, semantic model routing, compiler infrastructure and experimental alternative backends. All appear **once** in the community table.

## Research/lab follow-up

**Ten extra named source nodes** have been added in the Communities page: **Tsinghua MADSys; UCLA Prism authors/collaboration; Stanford SAIL/M* coauthors; Microsoft Research DeepSpeed; NVIDIA KDA research team; AMD MORI engineers; Amazon Science × UW SyFI Ekka authors; ModelTC LightLLM maintainers; Kubernetes SIG Apps LWS; Modular MAX team.** Their nature is explicitly labeled: some are **labs**, some **multi-organization papers**, and some **engineering communities**, not ten newly formed academic institutions. Existing Tsinghua PACMAN and UW SyFI entries have been refreshed with Chitu, DynaFlow and Trainium2 VibeSys artifacts.

### HOLD / nonadmission and source-conflict discipline

- **TokenSpeed:** found in secondary aggregators but its unique project-owner/source identity was not sufficiently resolved in this pass; **HOLD_IDENTITY**, not silently admitted.
- **Grove / generic inference operators:** some aggregator names map to multiple GitHub projects or lack a uniquely confirmed owner; **HOLD_IDENTITY** until the exact upstream source and active scope are verified.
- **Stanford branch-parallelism title collision:** a current Stanford MAST search exposed different names (PACE vs TAPER) around the same arXiv identity; **HOLD_IDENTITY** for any new canonical-paper entry until publisher/source versions are reconciled. The lab source itself remains useful.
- **LLM application tooling, RAG vector stores, API gateways:** kept outside the execution-engine mechanism list unless they directly expose model workload routing, hardware execution, KV lifecycle, or a specified measurable serving contract. No automatic intake from popularity/star counts.
- **Archived or backend-specific artifacts:** historical Hugging Face TGI remains explicitly archived; no claims that a newer ROCm/Ascend 950/TPU execution path works on Ascend 910B2/CANN 9.1.

## Priorities for actual systems research

1. **Cross-layer handoff:** Chitu, LightLLM, JD xLLM-service, DynaFlow.
2. **Memory/communications correctness:** kvcached, MORI, NVIDIA NVSHMEM, SGL NPU, Cloudflare incident report (covered in Organizations).
3. **Agentic optimization and trustworthy verification:** SEIS, VibeServe, ForgeKernel, SpecForge/Speculators, Ekka.
4. **Compiler-to-engine portability:** Modular MAX, TorchNPU, SGL NPU/XPU, AMD ATOM/ROCm.

**Gates before any technical performance claim:** exact commit, device/toolchain, precision, model/tokenizer, frozen request distribution, hidden correctness/quality tests, stable timing/noise characterization and true end-to-end TTFT/TPOT/Goodput. Source selection ≠ replication; this sweep admitted **zero new canonical paper rows**. Published original sources that pass G0–G5 later can be admitted **once** in their appropriate mechanism home.
