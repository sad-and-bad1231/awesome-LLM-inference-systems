# DeepSeek + Tencent — primary-source organization audit (2026-11-12)

## Scope and decision

Targeted repair of the existing organization profiles, not a rewrite or a paper-admission batch. The current page structure and reading order are retained. The changes distinguish model releases, first-party code, production architecture disclosures, product adoption and vendor-reported performance.

No canonical topic paper was added or removed; the paper inventory remains unchanged. This receipt is an organization-source map, not an independent benchmark reproduction.

## DeepSeek

### Production system boundary

- [DeepInfer](https://github.com/deepseek-ai/DeepInfer) publicly releases offline inference for V4.1-Flash, including Attention DP/balanced CP, MoE EP/EPLB, DSpark confidence-scheduled verification, bounded SWA replay, async scheduling and optimized kernels.
- The official [deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md) describes the production Vision Encoder / Prefill / Decode disaggregation, separate stage and expert-parallel load balancers, and 3FS-backed KV-cache storage. It gives workload-specific examples of Prefill EP2–8 / DP2–8 and Decode Wide-EP EP64–128 / DP64–128; these are not universal configurations.
- DeepSeek states that KV-cache management and load-balancing code remain tightly coupled to internal infrastructure and are not fully open-sourced. The public DeepInfer repository also lists a KV-cache system, VE/P/D disaggregation and DP-replica load balancing as components not included in that release.

### Ascend implementation boundaries

| Project | Publicly documented scope | Hardware boundary |
|---|---|---|
| [FlashMLA](https://github.com/deepseek-ai/FlashMLA) | Sparse prefill and FP8/FP4 KV-cache decoding; version compatibility changes materially | Ascend 950 / CANN 9.2.0+; 2026-09-30 release changes KV format and drops Hopper/older model-format support |
| [DeepGEMM-Ascend](https://github.com/deepseek-ai/DeepGEMM-Ascend) | BF16/FP8/FP4 GEMM, MQA logits and MegaMoE | Public release validated on Ascend 950/950DT, CANN 9.20 |
| [DeepEP-Ascend](https://github.com/deepseek-ai/DeepEP-Ascend) | MoE EP dispatch/combine, FP8 dispatch, deferred epilogues; HCCL/HCOMM, UBMEM, URMA | Public validation on Ascend 950DT / CANN 9.2.0 / PoC HDK; some collectives, expert load balancing and hybrid/Engram paths remain incomplete |
| [TileKernels](https://github.com/deepseek-ai/TileKernels) | TileLang-based MoE, Engram, quantization and mHC kernels | Ascend 950 / CANN 9.2.0+ |
| [DeepSelect](https://github.com/deepseek-ai/DeepSelect) | DSA indexer/sampler TopK | Ascend path is narrower than CUDA: BF16 input and int32 indices; documented TopK range is bounded |
| [DeepJIT](https://github.com/deepseek-ai/DeepJIT) | Shared header-only C++20 runtime JIT for CUDA and Ascend | Requires matching local compiler/runtime toolchain |

**Compatibility conclusion:** none of these 950/CANN 9.2.x validations establishes support on Ascend 910B2 with CANN 9.1.0. No such compatibility is claimed in the profile.

## Tencent

### Model and product boundaries

- [Hy4-preview](https://github.com/Tencent-Hunyuan/Hy4-preview) is the artifact with 770B total / 49B active parameters, 1M context, Gated DSA + IndexCache, iHC and native MTP. The preview repository attributes its architecture as inspired by DeepSeek and GLM.
- Tencent's [Nov 4 Hy4 final announcement](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/) describes visual understanding, computer use and long-horizon agentic capabilities. The final release's exact architecture is not inferred from Preview.
- Tencent identifies Shunyu Yao as Chief Scientist for AI; the public Foundation–Product–Frontier framing is a strategic statement, not proof of sole ownership of each Hunyuan engineering subsystem.
- Tencent Cloud's [WorkBuddy ecosystem update](https://www.tencent.com/zh-cn/tencent-cloud-accelerates-international-growth-advances-enterprise-ai-and-expands-global-partnerships/) reports 9B+ task requests, 50+ industries, 50% of China's Top 500 enterprises, 50K+ developers/partners and 200K+ skills. These remain company-reported adoption figures, not DAU.

### First-party inference tooling

- [AngelSlim](https://github.com/Tencent/AngelSlim): model compression/quantization toolkit; it integrates [AngelSpec](https://github.com/Tencent/AngelSpec).
- AngelSpec is a Torch-native **draft-model training framework**, not a serving runtime. It covers MTP and block-parallel methods such as DFly/DFlash/DFlare and uses a disaggregated inference/training workflow with Mooncake RDMA hidden-state transfer. See [technical report](https://arxiv.org/abs/2607.25852).
- [KsanaLLM](https://github.com/Tencent/KsanaLLM): open-source serving engine with prefix caching and optional Mooncake global KV-cache connector. Its README documents Ascend 910B2C with CANN 8.0RC2; this is not evidence of current Hy4 production deployment or CANN 9.x compatibility.
- TokenHub is the API/model-access layer, not the underlying inference engine.

### RSI evidence boundary

- The [Hy4-preview release](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) describes an early model-assisted loop over training/data/evaluation and low-level operators. Tencent reports 31.8% end-to-end inference throughput improvement from operator-fusion and communication optimization across different context lengths and concurrency. This is a **vendor-reported** claim; no public reproducible code/trace/config bundle was inspected to independently verify it.
- The [Hy4 final release](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/) separately describes Hyra 2.0 optimizing pre-training infrastructure for smaller models sharing the architecture, alongside HyCell and HyPDE. This is a training/research-infrastructure claim, not the same inference-engine RSI claim.

## Editorial changes

- Updated DeepSeek model crosswalk date and clarified V4 Pro vs unconfirmed V4.1 Pro.
- Corrected DeepSeek execution-library ownership/scope and added the missing DeepEP-Ascend row.
- Added the production architecture disclosure while preserving the boundary between that design and public DeepInfer code.
- Made Ascend 950 / CANN 9.2.x requirements explicit; did not imply 910B2 support.
- Corrected Tencent Hy4 final/Preview separation and removed the unsupported transfer of Preview's 770B specification to the final model.
- Added first-party AngelSlim/AngelSpec/KsanaLLM coverage, WorkBuddy/product co-design context and carefully tiered RSI claims.
- Updated the organization index and source chronology; no paper-count change.

## Primary sources

- [DeepInfer README](https://github.com/deepseek-ai/DeepInfer)
- [DeepInfer deployment Q&A](https://github.com/deepseek-ai/DeepInfer/blob/main/doc/inference_deployment_qa.md)
- [DeepEP-Ascend](https://github.com/deepseek-ai/DeepEP-Ascend)
- [DeepGEMM-Ascend](https://github.com/deepseek-ai/DeepGEMM-Ascend)
- [FlashMLA](https://github.com/deepseek-ai/FlashMLA)
- [DeepSelect](https://github.com/deepseek-ai/DeepSelect)
- [DeepJIT](https://github.com/deepseek-ai/DeepJIT)
- [TileKernels](https://github.com/deepseek-ai/TileKernels)
- [Hy4-preview repository](https://github.com/Tencent-Hunyuan/Hy4-preview)
- [Tencent Hy4 final announcement](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/)
- [Tencent Hy4-preview announcement](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/)
- [Tencent AI strategy dialogue](https://www.tencent.com/tencent-cloud-debuts-productivity-agent-suite-creating-a-new-gateway-to-ai-for-users-and-enterprises/)
- [WorkBuddy ecosystem update](https://www.tencent.com/zh-cn/tencent-cloud-accelerates-international-growth-advances-enterprise-ai-and-expands-global-partnerships/)
- [AngelSlim](https://github.com/Tencent/AngelSlim)
- [AngelSpec](https://github.com/Tencent/AngelSpec) · [Technical report](https://arxiv.org/abs/2607.25852)
- [KsanaLLM](https://github.com/Tencent/KsanaLLM)
