# November 20, 2026 — arXiv inference systems incremental intake and industry checkpoint

**Base:** `main` 944 canonical entries (2026-11-14). **Decision:** 21 distinct, primary-source-checked additions in the existing 8 topic homes: Kernel +6, KV +5, Decoding +1, Quantization +0, MoE +1, Runtime +4, Distributed +2, Benchmark +2. **Result: 965 / 8 / 44.** No new taxonomy, second paper database, venue inference, local device execution or independent benchmark replication. The 11/14 intake is not counted twice.

**Review standard:** [G0–G5](../STRICT_REVIEW.md) and [two-speed arXiv admission](../CURATION.md#two-speed-publication-review-arxiv-discovery-vs-conference-references). Confirm original arXiv paper ID/title/date, system relevance, mechanism and actual support; label pilot/simulation/model changes. Numeric gains below are **author-reported** and apply to their specified comparators, not universal deployment speedups. A kernel result is not Serving Goodput; a real trace is not an executed proposed system; an updated model is not the same model.

## 1. Admission decisions (21; primary arXiv links)

| Primary source (submission) | Canonical home / grade | Key mechanism, evidence and boundary |
|---|---|---|
| [AscMLA 2611.26106](https://arxiv.org/abs/2611.26106) (Nov 19) | Kernel / Attention · EVIDENCED | FP4 MLA asymmetric K/V scale; author real GPU kernel tests; KV -38.2% vs FP8, kernel 1.35× geo-mean vs TRT-LLM FP8. **Not Ascend, not E2E.** |
| [DTS 2611.25938](https://arxiv.org/abs/2611.25938) (Nov 19) | Kernel / Attention · EVIDENCED | Delta incremental sparse tile scoring; H100 and multi-H100 prefill study; approximate attention/quality checks remain essential. |
| [KIWI 2611.23848](https://arxiv.org/abs/2611.23848) (Nov 18) | Kernel / Communication · EVIDENCED | GPU→CPU programmable host-proxy for GPU-initiated collectives; AMD/MoE EP kernel and vLLM results, not HCCL compatibility. |
| [Together Compiler 2611.14681](https://arxiv.org/abs/2611.14681) (Nov 10) | Kernel / Automation · EVIDENCED | Persistent, hot-swappable inference engine plus high/low fidelity agent search; selected author E2E TPS gains. Distinguish **experiment throughput** from TPS; no model/agent self-improving-weight claim. |
| [EngineAgent 2611.14356](https://arxiv.org/abs/2611.14356) (Nov 10) | Kernel / Automation · EVIDENCED | Layered engine index, hardware capabilities, builder/auditor and actual execution; author 75% vs 33.3% cross-backend enablement success on 12 tasks; not a TPS comparison. |
| [CompoundingKernel 2611.19230](https://arxiv.org/abs/2611.19230) (Nov 14) | Kernel / Automation · EVIDENCED | Correct-kernel lineage archive and parallel search; B200 SOL-ExecBench reference-relative results, 235 verified correct; no end-to-end serving. |
| [KaleidoKV 2611.19253](https://arxiv.org/abs/2611.19253) (Nov 14) | KV / Prefix · EVIDENCED | Offline RAG evidence reordering with prefix-ready admission; author four workloads/four models and full planning-time accounting. |
| [RoCoKV 2611.25433](https://arxiv.org/abs/2611.25433) (Nov 19) | KV / Compression · EVIDENCED | Uncertainty/redundancy-aware reasoning KV retention and vLLM CUDA path; **approximate state and model quality**. |
| [Quantized Draft KV 2611.20565](https://arxiv.org/abs/2611.20565) (Nov 16) | KV / Compression · EXPLORE | K4V4 Draft-only cache; -66.20% draft cache, -23.95% total, mean acceptance 57.93→57.14%. **No E2E TPS.** |
| [TideCache 2611.26619](https://arxiv.org/abs/2611.26619) (Nov 19) | KV / Offload · EVIDENCED | Heterogeneous hybrid-layer cache mapping and streaming on GPU/CPU superchips; SGLang HiCache comparisons, hardware-specific. |
| [TripleKV 2611.25112](https://arxiv.org/abs/2611.25112) (Nov 18) | KV / Offload · EVIDENCED | Tool-completion-aware SSD→Host prefetch + victim protection; author real vLLM P95 TTFT up to -49% on tested workloads. |
| [SpecSearch 2611.22296](https://arxiv.org/abs/2611.22296) (Nov 17) | Decoding / Adaptive · EVIDENCED | HW × concurrency × length calibrated SpecDec optimizer; comparisons include DFlash and AR, not a universally best spec strategy. |
| [VelServe 2611.18392](https://arxiv.org/abs/2611.18392) (Nov 13) | Runtime / Batching · EVIDENCED | Decode-tail-calibrated prefill budget/admission; author SLO Goodput vs strongest tested scheduler rather than mean-only latency. |
| [Cap-and-Track 2611.24891](https://arxiv.org/abs/2611.24891) (Nov 18) | Runtime / Routing · EVIDENCED | Meta fail-fast backend capacity feedback + durable priority queue; same-traffic production A/B, bounded fleet/workload conclusions. |
| [Evolving Infra 2611.12304](https://arxiv.org/abs/2611.12304) (Nov 9) | Runtime / P-D · EVIDENCED | Fast P/D role switching decoupled from agent KV residency; author up to 256 GB300 vs Dynamo, selected E2E/TTFT gains. **Adaptive serving ≠ code-writing RSI.** |
| [Aggron 2611.26435](https://arxiv.org/abs/2611.26435) (Nov 19) | Runtime / Agent · EVIDENCED | Compress agent context during queue head-of-line stall; evaluate additional work, P99 completion and potential semantic loss. |
| [EchoMoE 2611.22215](https://arxiv.org/abs/2611.22215) (Nov 17) | MoE / Communication · EVIDENCED | Inter-layer residual delta compression for EP; author -58% communications / +22.6% throughput. **Requires finetuning; MODEL_CHANGED.** |
| [XM-Sparse 2611.22280](https://arxiv.org/abs/2611.22280) (Nov 17) | Distributed / KV Transfer · EXPLORE | Sparse KV fetch from scale-up pool with index/prefetch; **emulated memory-pool hardware**, not proven deployed remote-memory fabric. |
| [HyCoInfer 2611.22086](https://arxiv.org/abs/2611.22086) (Nov 17) | Distributed / Edge · EVIDENCED | GPU cloud prefill + FPGA edge decode; two V100 + U280 real hardware under imposed bandwidth limits. |
| [Validation-driven Deployment 2611.25905](https://arxiv.org/abs/2611.25905) (Nov 19) | Benchmark / Workloads · EVIDENCED | Agent trace capture/replay/verification with vLLM and llm-d; warning on unrealistic synthetic load/concurrency. |
| [Held While Waiting 2611.26480](https://arxiv.org/abs/2611.26480) (Nov 19) | Benchmark / Workloads · EXPLORE | Measured AgentCore env reservations and wait-dominant sessions; 64-way session multiplexing is a **SIMULATED counterfactual**, not a secure deployable runtime. |

**Admitted tiers:** 18 × `KEEP_PREPRINT_EVIDENCED`, 3 × `KEEP_PREPRINT_EXPLORE` (Quantized Draft KV, XM-Sparse, Held While Waiting). No paper was independently run on an Ascend NPU/GPU.

## 2. Scan context and explicit non-admissions

- **Already canonical before this branch:** [ForeSpark](https://arxiv.org/abs/2611.13442), [DForkTree](https://arxiv.org/abs/2611.12356), [D3Tree](https://arxiv.org/abs/2611.11371), [HybridSpec](https://arxiv.org/abs/2611.04055), [Twig](https://arxiv.org/abs/2608.01651), [REAL Loss](https://arxiv.org/abs/2611.14399), [Phrase-Level](https://arxiv.org/abs/2611.12464), [Olifant](https://arxiv.org/abs/2611.16714), [MegaOps](https://arxiv.org/abs/2611.16248), [SubGPU](https://arxiv.org/abs/2611.14904), [Evolving Agent Teams](https://arxiv.org/abs/2610.36848), [KOPE](https://arxiv.org/abs/2608.25570), [Weights That Stay](https://arxiv.org/abs/2611.00506). August/October originals are **not** reclassified as November-first-submission.
- **WATCH / not canonical:** [KV-LTM 2611.21998](https://arxiv.org/abs/2611.21998), proposes durable session KV and cost model but lacks an executed persistent-cache system or fidelity/TTL evaluation; re-evaluate when equivalent full-run replay and storage economics exist. [EAGLE-4 official release](https://github.com/eagle-hq/EAGLE-4) retains the earlier paper-identity/comparator WATCH pending source reconciliation.
- **No special quota** for Quantization; inference-relevant FP4 MLA is under **Kernel**, draft-KV bitwidth under **KV**, changed-weight EP under **MoE**, not triplicated into Quantization for cosmetic topic balance.
- **Identity/venue:** arXiv ID and original submission date govern the paper's provenance, not Google result age or author claims of a 2027 venue. No 2027 acceptance inference.
- **Coverage limit:** a targeted source-based sweep across eight categories, seven frontiers, and 11/1–11/20 sources; **not** a mathematically exhaustive scrape of every arXiv item.

## 3. Industry source checkpoint (first-party, not paper admission)

| Region / organization | Source/date | Engineering relevance and boundary |
|---|---|---|
| China · Tencent | [Hy4-flash official repository](https://github.com/Tencent-Hunyuan/Hy4-flash), Nov 2026 | 220B including Engram, 12B active rounded; 42-layer hybrid sparse/SWA, LatentMoE, Engram and built-in **DFly2** Draft with target KV/index reuse; model architecture + open weights, **not** a published optimized vLLM-Ascend backend. |
| China · Alibaba Qwen | [Qwen4-Max official Nov 16 release](https://qwen.ai/blog/qwen4-max) | 2.4T backbone + 328B N-gram embeddings / 71B active, 1M context; distinguish API deployment from public open weights and vendor-reported cost/task from isolated kernel gains. |
| US · OpenAI | [GPT-6.2 Astra/Sol official Nov 17](https://openai.com/index/introducing-gpt-6-2-astra-sol/) · [API changelog](https://developers.openai.com/api/docs/changelog) | Model/API tier, reasoning/agent economics and interface contract; **closed serving engine internals unknown**. |
| US · Google | [Gemini 4 Carbon general availability Nov 10](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) · [Hydrogen Nov 12](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Neon Nov 18](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/) | Argon Oct-origin; Carbon, Hydrogen, Neon differentiated public API deployment/workload tiers. TPU serving tech is evidenced **separately** by XLA Serving / TorchTPU code, not by API model names. |
| Open-source engine · vLLM / AMD | [FlyDSL MonoKernels Nov 18](https://vllm.ai/blog/2026-11-18-flydsl-monokernels) | Decoder-layer persistent MonoKernel on selected MI300-family workloads; useful native fusion comparator, hardware-specific (not an automatic Ascend port). |
| Open-source engine · SGLang/AWS | [SGLang-Neuron v0.1.0 Nov 12](https://www.lmsys.org/blog/2026-11-12-sglang-neuron-v0.1.0) | Trainium NKI native path + layer-level megakernel; public preview, **not** a CANN implementation. |

## 4. Decision-oriented follow-ups

1. **Engine/Kernel agents:** benchmark fixed agent vs persistent memory vs team/engine-level supervision at *matched foundation-model, GPU-hours, compilation runs and correctness checks*; include holdout models/shapes. Source: Together Compiler/EngineAgent/CompoundingKernel.
2. **Ascend execution:** study KIWI GPU→CPU invocation, FlyDSL MonoKernel and TideCache dataflow as *execution-contract references*; benchmark native CANN/HCCL and full model time before speculative kernel ports.
3. **Agent serving:** reproduce a minimal tool-wait KV miss trace and PD-role switching counterfactual from TripleKV/Evolving Infra/Aggron; measure session P95/P99 and aggregate GPU memory rather than only plain decoding TPS.
4. **SpecDec:** compare SpecSearch cost-model strategy against fixed draft on frozen model/hardware/workload first; optimize verified acceptance × draft cost × target verification critical path, then evaluate paired loads.

**Review status:** source-checked editorial intake; no locally executed experiments. Individual manuscript changes, code artifacts, and vendor releases should continue to be upgraded in-place, **never duplicated**.
