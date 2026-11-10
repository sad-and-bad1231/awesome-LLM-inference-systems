# November 9, 2026 — Inference systems, organizations and arXiv source audit

**Baseline:** `main@6bcdd81` (Nov 6); 852 canonical source-curated papers; eight technical mechanisms, 44 directions, 49 organization profiles, seven frontiers. **This proposed batch: 10 preprints → 862 papers, with a unique canonical home for each.** All are *arXiv 2026 preprints*, not peer-reviewed conference publications. All claimed benefits are **author-reported**; reproduction status of each is `not_attempted`. Source review ≠ independent execution/GPU or NPU benchmark.

## First-party organization/model release reconciliation

| Topic | Primary evidence | Verdict and exact inference boundary |
|---|---|---|
| **Kimi K3.1 Pro** | [Official open weights](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [vLLM day-0 technical report, Nov 4](https://vllm.ai/blog/2026-11-04-kimi-k31-pro) | **UPDATE** Nov 4 weights are released (custom Kimi model license). **69 KDA layers / 24 DSA-indexed MLA layers**, packed MLA latent/indexer/KDA states, exact distributed Top-K merge, token-sharded prefill, sparse Decode. Reported 1.69× TTFT in 8×GB300 at 340K tokens, **not Ascend 910B2 evidence** |
| **Claude Fable 5.2 / Mythos 5.2** | [Anthropic Nov 9 launch](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [model catalog](https://platform.claude.com/docs/en/models/overview) | **UPDATE** Fable available; Mythos restricted (same underlying model). Vendor cites output up to 30% faster than 5.1 and optional fast mode up to 2.5×. **API behavior/price is not public implementation of KV layout, Scheduler or kernels** |
| **AMD ROCm InferaSim** | [AMD Nov 6 blog](https://rocm.blogs.amd.com/software-tools-optimization/inferasim/README.html) · [paper](https://arxiv.org/html/2611.04032v1) | **UPDATE** MI355X kernel transfer laws + measured anchors + DES for Serving config and P/D planning. Reported 9.1 GPU-h for 11 anchors vs 204 GPU-h for 226 measured configurations. **Predicted Goodput ≠ deployed Goodput** |
| **Qwen4** | [Qwen3.8-Flash-Next primary repository](https://github.com/QwenLM/Qwen3.8-Flash-Next) | **WATCH_RELEASE** no verified general-availability Qwen4 checkpoint/model-card evidence. The earlier **Gated DeltaNet + QSA indexer/offloading** architecture is a legitimate technical signal, not proof of a Qwen4 product release |
| **DeepSeek V4.1 Pro** | [Official DeepSeek news](https://www.deepseek.com/en/news/) · [API updates](https://api-docs.deepseek.com/updates/) | **WATCH_RELEASE** “coming soon” is not a verified model/API/weights release. Distinguish already released V4.1 Flash / DeepInfer from speculative Pro details |
| **Astra 6.2** | [Official OpenAI model catalog](https://platform.openai.com/docs/models) | **WATCH_IDENTITY** no verifiable dated official Astra 6.2 release in this scan; no live organization assertion |
| **AMD Fused-Softmax** | [Preprint](https://arxiv.org/html/2611.09225v1) | **NON_CANONICAL_ORG_CONTEXT** low-bit Fused Softmax kernels in AITER and real MI355X, but full-model evaluations are **video diffusion Wan2.2/HunyuanVideo**, not text-LLM Serving |
| **vLLM Stable ABI / Kinference** | [CUDA ABI engineering](https://vllm.ai/blog/2026-11-06-stable-abi-cuda) · [Kinference announcement](https://vllm.ai/blog/2026-11-04-introducing-kinference) | **ENGINEERING_WATCH** packaging/compatibility and token-aware Kubernetes ingress; these are runtime infrastructure signals, not new academic entries or proof of Ascend equivalence |

## G0–G5 KEEP_STRICT: ten new unique canonical entries

**G0:** primary author arXiv HTML/title/2026 preprint status checked, no unverified formal venue. **G1/G2:** true inference bottleneck and a distinguishable mechanism against strong prior. **G3:** bounded real system measurements, model semantics/accuracy conditions and proper metric explicitly noted. **G4:** code recorded where disclosed, never executed locally. **G5:** lasting system engineering value; no quotas.

| Source | Primary home; closest baselines; actual evidence and caveat | Disposition |
|---|---|---|
| [FlashOffloading](https://arxiv.org/html/2611.07542v1) | **KV/Offloading** vs resident/paged offload designs: **GLM-5.2/MTP3, 32×Ascend 910C / 64 dies, vLLM-Ascend PD**, prefill and decode throughput with **TPOT under 30ms**; author stage maxima 1.38×/1.91×. No 910B2 portability inference | KEEP_STRICT; REAL_NPU; not_attempted |
| [Nebula](https://arxiv.org/html/2611.09474v1) | **KV/Distributed Sharing** vs prefix-only cluster routing and single-node PIC: **SGLang/Dynamo/NIXL, 2×4 H20-3e, 7P1D, four RAG/agent workloads**, author mean median-TTFT −61.4%; non-prefix cache reuse has position/quality contracts | KEEP_STRICT; REAL_GPU_RDMA; not_attempted |
| [ChainFlow](https://arxiv.org/html/2611.08669v1) | **Decoding/Draft** vs matched EAGLE-3/DFlash. **Qwen3.5, B300, vLLM 0.31.0, greedy batch1**, target hidden-state flow drafter must be **trained**; limited concurrency tests | KEEP_STRICT; TRAINED_DRAFTER; not_attempted |
| [SpecPilot](https://arxiv.org/html/2611.02501v1) | **Decoding/Adaptive** vs baseline SGLang 0.5.20 speculative paths, lossless W12/tree verification/admission; **H100 and RTX PRO 6000, Qwen/Gemma, single and batched**. Token forcing detects shortcuts; optimizing an engine is not optimizer RSI | KEEP_STRICT; REAL_GPU; not_attempted |
| [BitDecoding-FP4](https://arxiv.org/html/2611.09825v1) · [code](https://github.com/OpenBitSys/BitDecoding-FP4) | **Quantization/KV** vs BF16, FP8, other FP4: **B300, Qwen3-4B and 30B-A3B, 64K–128K**, vendor/author max peak-serving throughput 2.4–3.0×; **non-bitwise equivalent, quality evaluated** | KEEP_STRICT; APPROXIMATE_QUALITY_CHECKED; not_attempted |
| [TriAttention](https://arxiv.org/html/2611.07256v1) · [code](https://github.com/HanzhiZhang-Ulrica/TriAttention) | **Kernels/Attention** vs dense BF16 and Torch: per-head Skip/4b/8b calibrated fused attention/packed KV; **A100 and other GPU tests, model generation quality**; largest generation speedups **not online vLLM Goodput** | KEEP_STRICT; APPROXIMATE_OUTPUT; not_attempted |
| [CISA](https://arxiv.org/html/2611.03200v1) | **MoE/Sparse Attention** vs dense/sparse GPU baselines: **NVIDIA real GPU, vLLM Paged Attention, fixed-output throughput**; calibrates indexer without gradient updates, but very-long-context quality still degrades for some tasks; QShare prefill only | KEEP_STRICT; APPROXIMATE_OUTPUT; not_attempted |
| [cμ scheduling](https://arxiv.org/html/2611.04807v1) | **Runtime/Batching** vs alternative priority policies: memory-/bandwidth-aware fluid cμ with **H800 real-engine trace and numerical controls**; asymptotic theorem does not prove finite dynamic SLO performance | KEEP_STRICT; REAL_GPU + MODEL_THEORY; not_attempted |
| [ServerBench](https://arxiv.org/html/2611.06841v1) · [project](https://infini-ai-lab.github.io/Server-Bench/) | **Benchmarking/Workloads**: **11 coding agents ×3 L40 deployments, Qwen/Gemma**; frozen agent-written serving implementation, held-out correctness and session replay vs vLLM 0.28/SGLang 0.5.19. **Closed-loop replay ≠ production online demand** | KEEP_STRICT; REAL_GPU_REPLAY; not_attempted |
| [ROCm InferaSim](https://arxiv.org/html/2611.04032v1) | **Benchmarking/Models**: **MI355X measured anchors + DES**, synthetic/predicted configs calibrated against real engine points. Accuracy and applicability must be checked per workloads; no simulator output claimed as real deployment gain | KEEP_STRICT; MEASURED_ANCHOR+SIMULATED_PREDICTION; not_attempted |

## Explicit holds and removals — **not** canonical paper rows

| Candidate | Decision & specific missing evidence |
|---|---|
| [LeanSparse](https://arxiv.org/abs/2611.04671) | **HOLD_G3_G4**: mechanism promising for native sparse DSA, but evaluation HTML inaccessible in this pass. Need exact checkpoint, backend, quality vs strongest offload baseline and runnable artifact |
| [HELIX](https://arxiv.org/abs/2611.06513) | **HOLD_G3**: operator-level heterogeneous vLLM partitioning worth comparing, but full methods unavailable here; separate measured H100/B200 from any **modeled** emerging accelerators |
| [ReKV](https://arxiv.org/html/2611.08770v1) | **HOLD_G3**: main handoff improvement uses **model-shaped synthetic benchmark**, and real-weight BF16 recompute is a separate result; no claim of full online disaggregated Goodput |
| [Fused-Softmax](https://arxiv.org/html/2611.09225v1) | **HOLD_SCOPE for text-LLM canon**: evidence is MI355X Video-Diffusion/DiT; strong adjacent low-bit kernel signal in AMD engineering context |
| [KOSMOS](https://arxiv.org/html/2611.07477v1) | **HOLD_G1_G3**: persistent queue-driven TP/SP+MoE communication/computation overlap is promising but paper devotes main evidence to training/forward kernel; need true inference serving end-to-end |
| [TileQuant](https://arxiv.org/abs/2611.07217) | **HOLD_G3_G5**: inspect equal-quality execution vs existing quantization, not bulk-admit sibling work |
| [Intent-Aware Caching](https://arxiv.org/abs/2611.09715) | **HOLD_G3**: distinguish engine-measured TTFT/TPOT from pure trace-driven hit-rate and eviction simulations, match cache budget |
| [Kernel library issues study](https://arxiv.org/abs/2611.09280) | **WATCH_AGENTIC_KERNEL**: strong engineering hygiene context but no distinctive new execution bottleneck optimization proven |
| “MORTIS”/“DARIC” in secondary digests | **HOLD_IDENTITY** pending stable original DOI/arXiv and full-paper sources |
| Existing [ARK](https://arxiv.org/abs/2610.41160) | Historical **HOLD_G3**: packet-level simulated PD RDMA vs actual NIC/Serving measurements; no status upgrade |

## Complete taxonomy pass and the seven frontier boundaries

All **eight** technical categories inspected. New: **Kernels +1, KV +2, Decoding +2, Quantization +1, MoE/Sparse +1, Runtime +1, Benchmarking +2**. **Distributed Serving +0**: HELIX/ReKV remain HOLD rather than filling a quota. Eight categories remain the canonical homes, and 44 directions remain unchanged.

1. **Agent-native inference:** Nebula's RAG/agent session PIC and FlashOffloading's real Decode KV residency are relevant, but belong to the established KV mechanisms, not a new frontier.
2. **Real-time omni-modal serving:** K3.1 Pro multimodal availability does not by itself demonstrate duplex streaming/backpressure/stage scheduling.
3. **Diffusion-language-model serving:** no new November dLLM scheduler with sufficient distinct real-serving evidence in this intake; DiT video-only Fused-Softmax is not an AR text Serving speedup.
4. **Interactive world-model inference:** no new real action-to-first-frame/jitter/state-persistence result admitted; retain previous StreamDiffusionV2 anchor.
5. **Embodied/VLA loops:** no sufficiently measured hard perception-to-action SoC deployment admitted; retain prior VLA hardware characterization.
6. **Agentic kernel engineering:** SpecPilot uses coding-agent optimization with Token Forcing and fixed execution tests. KOSMOS/AMD kernel sources provide engineering constraints, **not proof of reliable automatic kernel generation**.
7. **Autonomous inference-engine evolution, RSI-adjacent:** ServerBench's frozen code/held-out replay is the strongest **evaluation methodology signal**; SpecPilot offers a narrower optimized executable. **Neither improves the optimizer's own policy under equal unseen-task budgets or proves recursive self-improvement.**

## Reproducibility, next steps and limits

- **Ascend 910B2:** audit whether FlashOffloading's CopySFA, pinned host-memory, H2D overlap and 910C native streams are implementable in pinned CANN 9.1 before designing an experiment. This source itself does **not** demonstrate that.
- **Kimi hybrid+DSA:** study packed KV cache semantics, exact global Top-K merge, token-sharded prefill and sparse Decode. Model metrics do not establish serving throughput.
- **Agent-written engines:** freeze oracle and versions, enforce semantic equivalence, hidden out-of-distribution correctness, fixed search budget, shared held-out workloads and final independent replay. Treat prior code improvements separately from RSI.
- **Unresolved historical debt:** NovaServe/Select-N identity hold, 42 program-index provisional entries and broader legacy corpus are **unchanged**. This sweep does not certify the prior 852 paper rows.
