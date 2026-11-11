# Baidu deep-dive II — mechanisms, code boundaries and evidence decisions (2026-11-11)

**Status:** source-and-code inspection, **no benchmark execution**. This second pass follows [the first organization audit](BAIDU_PRIMARY_SOURCE_AUDIT_20261111.md). The first pass answered *what Baidu built*; this pass asks *what is new, what is borrowed, what is actually executable, and which claims pass an inference-systems evidence gate*. Evidence: original research/preprint abstracts, first-party technical descriptions, official model cards, GitHub source/docs and exposed reproduction harnesses. No CUDA/XPU/Ascend GPU runs, and no private commercial deployment inspection.

**Disposition:** 1 **KEEP_STRICT** candidate admitted to the [Benchmarking & Systems Analysis](../topics/benchmarking-analysis.md) corpus: [When Does Better Acceptance Pay?](https://arxiv.org/abs/2610.24993) / [DCore](https://github.com/ernie-research/DCore), categorized primarily as **controlled evaluation**, not a separate claimed production serving engine. Original FlashMask, FlashMask-3, PLAS, ECHO and VHA remain in the Baidu technical map as context, with explicit G1/G3 scope boundaries; this is not rejection of their technical quality. Baseline corpus changes **852 → 853**, while the category count remains eight and frontiers remain seven.

## 1. Research lineage: compare questions and mechanisms, not corporate myth

| Era / anchor | Research question answered | Mechanism | Original source | Attribution boundary |
|---|---|---|---|---|
| 2016 open framework | Who controls low-level AI execution infrastructure? | Open deep-learning framework and ecosystem | [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) | Public Paddle repo says open-source since 2016; a framework is not itself a model-quality win |
| 2019 ERNIE | How should BERT masking expose multi-token knowledge? | Entity/phrase-level masking, with Chinese NLU evaluations | [ERNIE](https://arxiv.org/abs/1904.09223) | Builds on BERT; cannot claim invention of NLP, Transformers or language pretraining |
| 2019/2020 ERNIE 2.0 | How can pretraining tasks be accumulated without starting over? | Continual lexical, syntactic and semantic tasks | [AAAI 2020 paper](https://ojs.aaai.org/index.php/aaai/article/view/6428) | Primarily pretraining, not an inference-system paper |
| 2021 ERNIE Titan | Can knowledge-aware models scale to hundreds of billions of dense parameters? | ERNIE 3.0 Titan 260B dense pretraining and online distillation | [Report](https://arxiv.org/abs/2112.12731) | Do not turn a model-training scale claim into deployed serving efficiency |
| 2021 JIZHI | Can ultra-high-QPS web recommendation inference use less resource? | Staged event-driven pipeline, asynchronous processors, tiered state, log-guided resource management | [KDD 2021 paper](https://arxiv.org/abs/2106.01674) | Production **recommendation/search ranking**, not autoregressive KV/request scheduling |
| 2024/2025 FlashMask | How to represent expressive sparse Attention masks without dense O(N²) mask state? | Column-wise interval/boundary representation with mask skipping | [ICLR 2025 paper](https://arxiv.org/abs/2410.01359) · [code](https://github.com/PaddlePaddle/FlashMask) | Important **attention kernel lineage**, mostly training evidence; not proven direct token-decoding acceleration |
| 2025 ERNIE 4.5 / FastDeploy | How to jointly deploy MoE/VL models across devices? | Heterogeneous modality routing + P/D, KV handoff, quantization, EP | [ERNIE code/report references](https://github.com/PaddlePaddle/ERNIE) · [FastDeploy](https://github.com/PaddlePaddle/FastDeploy) | Distinguish new ERNIE architecture from established P/D and vLLM-derived interfaces |
| 2025 PLAS | How to retrofit sparse attention into an existing dense model? | Lightweight block-gating trained separately, token/head union for irregular sparse execution | [Technical implementation doc](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/features/plas_attention.md) · [industry test](https://ernie.baidu.com/blog/posts/plas/) | **Model path changed via trained gate**. Long-context author tests do not prove exact quality or universal online gains |
| 2026 ERNIE 5.5 / DCore / Evolve | Can model-state budget, expert communication and self-drafting be co-designed, and can automated experiments tune real serving? | Hybrid HCA/MLA/DSA + Multi-Router Latent MoE + ECHO; controlled draft recipe comparisons; outer/inner agent research loops | [ERNIE 5.5 Base](https://ernie.baidu.com/release/ernie-5-5-flash-base/) · [DCore](https://github.com/ernie-research/DCore) · [ERNIE Evolve](https://ernie.baidu.com/research/posts/ernie-evolve/) | Three different units of evaluation: **model architecture**, **reproducible methodology**, **industry agent process** |

**Historical conclusion:** Baidu has long-running original ideas and executable systems; original contribution should be attributed per paper rather than inferred from the company label or chatbot rankings. The evidence reviewed still **does not** establish a Baidu priority claim for Looped Transformers or a direct architectural transfer to another company's model.

## 2. ERNIE 5.5 Flash: decompose model innovation into runtime costs

**Pinned first-party baseline:** [ERNIE 5.5 Flash Base](https://ernie.baidu.com/release/ernie-5-5-flash-base/) / [model card](https://huggingface.co/baidu/ERNIE-5.5-Flash-Base), released **2026-11-05**, **280B total / 14B activated**, 43 layers = 1 dense + 42 MoE, 37 HCA + 6 MLA/DSA, 512 routed experts (top 10) + one shared; BF16/FP8 base weights. The **2026-11-11 Flash Preview** is a post-trained service release and is **not** the same checkpoint. 128K pretraining context vs 1M supported fine-tuning/inference is a separate extrapolation/quality-validation boundary. The model card says ECHO has **0.36B additional parameters excluded from base parameter totals**: 'no standalone MTP layer' must **not** be paraphrased as 'zero extra parameters.'

### A. Hybrid KV-state budget: compression factor is per path, not whole-system 128×

HCA layers retain one compressed historical cache entry per 128 past tokens **plus a recent uncompressed window**; six MLA layers preserve tokenwise information with compressed latent KV, and DSA restricts the **attention selection/compute**, not automatically the resident original KV storage. HCA's compressed entry and an MLA KV entry also have different layouts/byte widths.

A **dimension-normalized toy model only** (not a byte-accurate inference measurement) is:

```text
B_HCA(N) ∝ ceil(N/128) + min(N, W)      # recent raw window W; retained compressed entries
B_MLA(N) ∝ N                            # requires MLA-specific per-token latent byte size
B_total(N) = 37*b_HCA*B_HCA(N) + 6*b_MLA*B_MLA(N) + indexer + auxiliary state
```

- **Known:** 37 vs 6 split, 128-token compression in HCA, 512 vs 256 nominal head dimensions, sparse selection in MLA, and first-party base-model ablations comparing HCA+MLA to HCA+CSA at similar KV budgets.
- **Unknown:** actual bytes per layer/cache pool, HCA compression working state, MLA rope/latent packing, prefix cache interaction, indexer resident bytes, P/D handoff size and server fragmentation; **cannot** claim global 128× KV saving or translate base evaluation into real TPOT.
- **Test:** equal prompt/output distribution and quality; per-layer allocated KV bytes and memory high-water mark; prefill construction and decode indexer kernel traces, end-to-end goodput/TTFT/TPOT vs a strong model-compatible baseline. Any model-architecture change requires **MODEL_CHANGED / QUALITY_CHECKED**; not an exact swap on Qwen.

### B. Multi-Router Latent MoE: routing quality ≠ free communication speedup

Separate (i) multi-router expert preference/selection from (ii) latent-domain expert execution. The first-party paper [Multi-View Latent MoE](https://arxiv.org/abs/2610.40577) covers Multi-Router and the additional Multi-View extension. **ERNIE 5.5 Flash uses Multi-Router**; do not claim it necessarily implements the paper's additional Multi-View per-expert view mixing. With 4096→2048 projection, dispatch/combine tensor width halves **for the selected transferred activation representation**, not automatically the total MoE operator latency or communication cost.

```text
T_MoE = T_project + T_router_topk + T_pack + T_dispatch + T_expert
       + T_combine + T_up_project + T_sync
```

- **Known:** top-10 of 512 routed + one shared, auxiliary-loss-free load balancing, narrower latent activation; official report says expert FLOPs and dispatch bytes can be reduced relative to a full-width expert *under its design comparison*.
- **Unknown:** rank-level expert skew, small-batch occupancy, TP/EP scheduling, all-to-all packet count, launch overhead, additional projection cost. Multi-Router is not a device-level expert-placement algorithm.
- **Test:** profile dispatch, expert, combine and up-projection separately; report tokens/expert/rank, bytes, max/mean expert load, p95 tail; compare total service latency and quality, not only activation width.

### C. ECHO vs Looped Transformer: a *different* recurrence notion

[ECHO](https://arxiv.org/abs/2610.24766) (2026 preprint, first-party authors) reuses the backbone's final layer as a future-token predictor; includes Dynamic Depth Sampling for training horizons. It can be a drafter within a verified speculative decoder, but the label **causal self-recursion** is not evidence of repeatedly applying a tied hidden-state Transformer block for arbitrarily deep latent reasoning (the Looped/Universal Transformer notion). Comparing ECHO to auxiliary MTP requires target-model compatibility and training parity.

```text
T_per_output ≈ (T_draft(k) + T_target_verify(k) + T_sample + T_sync) /
               E[committed tokens per verified step]
```

This is an **analysis approximation**, not a deterministic speed formula: actual serving includes batching, rejected-prefix fallback, caching, variable context, and target distribution. Publish acceptance length **and** target-only TPS, drafter latency, verifier latency, correctness/distribution checks and SLO-aware goodput. **No inference-speed proof** follows from a better ECHO training loss alone.

### D. VHA, FlashMask-4, mHC and DSA: explicitly attribute origins

- [Virtual Head Attention](https://arxiv.org/abs/2610.17959) (Baidu-linked 2026 paper): linear pre-/post-mixing among heads. The paper says they can be **folded into projections at inference**, potentially preserving a conventional GQA execution path; latency requires code confirmation, and ERNIE-specific integration may differ.
- [FlashMask-4](https://github.com/PaddlePaddle/FlashMask): SM90/SM100 CuTe-DSL flexible masked attention, sink bias, deterministic path; large 512/512 or 576/512 head support is **SM100-specific**. Its README compares with the **mask_mod path** of FlashAttention-4, not every FlashAttention version.
- [FlashMask-3](https://arxiv.org/abs/2610.17901) (NeurIPS 2026 main paper; [project](https://enigmatisms.github.io/flashmask-3/)): mask-localization, sparsity-aware context parallel work balance, distributed overlap; demonstrated **long-context training**, including backward and training throughput. Training CP speedup is not decode serving speedup. README says CPB code is **open-sourcing in progress**, while overlap CuTe path currently **SM100**; no claimed Ascend 910B2 implementation.
- **mHC** (Manifold-constrained Hyper-Connections) and DSA/MLA are **related established techniques adopted** by ERNIE 5.5. Their presence is not evidence Baidu originated every component; the contribution may lie in allocation, training and fusion of the combined architecture.
- Distributed Muon optimizer and MultiMax output-head loss belong principally to **training**, not independent serving acceleration.

## 3. FastDeploy: actual code path and control/data boundaries

**Inspected directly on the upstream repository's default branch (not a pinned immutable commit; line numbers can drift):**

| Functional boundary | Source code / doc anchor | Verified in source | What still needs runtime tracing |
|---|---|---|---|
| Request routing | [Go Router docs](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/online_serving/router.md) · [Go implementation](https://github.com/PaddlePaddle/FastDeploy/tree/develop/fastdeploy/golang_router) | PD prefill/decode policy config; `cache_aware`, `remote_cache_aware`, `process_tokens`, `request_num`, `power_of_two`; cache-aware radix-prefix and load scoring documented. Remote policy warns **synchronous HTTP call per decision** | Which policy executes, actual scoring code path, router enqueue/registration time, policy overhead p95 |
| In-engine scheduling | [resource_manager_v1.py](https://github.com/PaddlePaddle/FastDeploy/blob/develop/fastdeploy/engine/sched/resource_manager_v1.py) | Actual `schedule()`, `_select_preempt_candidate()`, `_trigger_preempt()`, `_allocate_gpu_blocks()`, `get_prefix_cached_blocks()`, `preallocate_resource_in_p()` and `preallocate_resource_in_d()` methods | Is the v1 scheduler actually active for the pinned release? Confirm hook from engine entrypoint and `v2`/platform alternatives |
| KV transfer | [cache_transfer_manager.py](https://github.com/PaddlePaddle/FastDeploy/blob/develop/fastdeploy/cache_manager/cache_transfer_manager.py) | `CacheTransferManager`, `do_data_transfer()`, `_transfer_data()`, swap-to-CPU/GPU functions; transfer factory imports multiple backends including Mooncake | Timestamp/bytes per layer; latency of RDMA/IPC vs fallbacks; P/D barrier/wakeup timing |
| PD handoff contract | [disaggregated.md](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/features/disaggregated.md) | Router selects P/D instance pair; P asks D for blocks; P prefill streams KV layerwise then sends first token; D continues | Track block ownership across P/D, no first-token race/double ownership, request preemption during transfer |
| Sparse attention | [PLAS document](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/features/plas_attention.md) | Learned block gate with 1B-token post-training; prefill token union (128 consecutive queries), decode GQA-head union, approximate top-k by binary-search strategy | Quality vs dense full attention; gather overhead, union density, indexer occupancy; whether **one full-attention final layer** dominates cost |
| Kernel/backend | [FlashMask](https://github.com/PaddlePaddle/FlashMask) · [XPU deployment docs](https://github.com/PaddlePaddle/FastDeploy/blob/develop/docs/zh/usage/kunlunxin_xpu_deployment.md) | Separate CUDA CuTe support matrix vs Kunlunxin XPU deployment | Do not infer a CUDA kernel runs on Kunlunxin or Ascend; inspect native backend and supported versions |

**Potentially significant engineering discovery:** the official [FastDeploy code overview](https://paddlepaddle.github.io/FastDeploy/usage/code_overview/) marks older top-level `scheduler/` paths as being deprecated; actual core scheduling is principally under `engine/sched/`, while Go `router/` handles disaggregated pair selection. Treat this as two control planes, not one interchangeable 'scheduler'. The runtime's own README explicitly acknowledges incorporation/reuse of portions of vLLM code. **Neither full invention nor simple copy** is supported without file-by-file implementation comparison.

**Independent benchmarking obligation:** routing latency, prefix locality/hit ratio, P/D pairing, transfer overlap, cache migration, request preemption, EP/TP utilization and goodput at a specified load. An API-compatible server does not guarantee vLLM-equivalent scheduling or cache behavior.

## 4. ERNIE Evolve: read the negative experiments, not just the large win

[Original November 9 report](https://ernie.baidu.com/research/posts/ernie-evolve/) specifies Director (research direction) → Selector (version/hypothesis) → Executor (isolated code changes) → independent **fixed evaluator outside editable repository** + Reviewer → experiment/version tree and experience bank. The publicly released [result repository](https://github.com/ernie-research/ERNIE-Evolve-Results) includes NanoChat, NanoGPT and **seven SOL-ExecBench kernel submissions**, logs/build instructions/hashes. It **does not** publish the same full code, workloads and complete replay harness for the commercial ERNIE 5.5 serving tasks.

| Real engineering task | Reported measured results | Mechanism learned from positive and negative interventions | Boundary |
|---|---|---|---|
| Kunlunxin **P800** low-latency inference | Final speed **623.6% of baseline** (a **6.236× ratio**, not +623.6%) | First enabled native mHC fused operator & built-in speculative path; then removed Python/wrapper/host-sync overhead and switched to native attention; later fixed decoding dispatch to low-latency communication path. **Replacing specialized communication with generic collectives regressed 14.0%** | Hardware/pair/workload-specific; the starting service had **unused existing optimizations**; not proof of a new 6× kernel |
| Deterministic GPU inference | **+33.7% throughput** author-reported | Profiling found deterministic sampling occupied ~14% GPU step time; Triton sampler and small-M/sparse attention work; **communication flag alone was noise-level**, only paired with kernel path had effect; many 'idle compute unit' hypotheses failed | Determinism and tested batch/temperature policies must be preserved; no comparable full public production replay |
| Already-optimized single-request GPU decode | **+14.9% speed** author-reported | MoE compute-unit sharing, fused mHC→FP8, **small-M operand role swap** avoiding FP8 padding for M<8, two-level expert indexing and fused draft sampling+reduction. **NVLink communication near floor**, kernel gaps only 2–4% and several directions rejected | This is not the previous 6.236× baseline; cumulative micro-gains on distinct hardware/test setup are **not additive** |

The **scientific lesson** is conditional gate design and repeated re-profiling. The negative results and low-gain results are at least as informative as the headline. There is no disclosed controlled comparison of a fixed coding agent with versus without transferred experience on unseen inference engines under the same tokens/GPU-hours. Therefore **ENGINE_OPTIMIZATION_DEMONSTRATED_AS_VENDOR_ACCOUNT**, **AGENT_OPTIMIZER_SELF_IMPROVEMENT_UNVERIFIED**, **MODEL_RSI_UNVERIFIED**.

**Reproduction-specific warning:** NanoGPT track 1 artifact lists **18 trials** (38.915 ± 0.034 s), but its README says first-run compile/graph capture (~7 min) is **excluded from reported training time**; do not compare wall-clock optimization budgets as if they were identical. SOL-ExecBench results list seven B200 kernel cases and official scores; private benchmark definitions/workload inputs are **not redistributed**.

## 5. New strict-admission receipt: controlled speculative decoding study (DCore)

**Title and identity:** [When Does Better Acceptance Pay? A Controlled Study of Speculative Decoding](https://arxiv.org/abs/2610.24993), **arXiv 2610.24993 v3, 2026-10-25**; 2026 *preprint*, **not a conference publication**. Author [code/checkpoints](https://github.com/ernie-research/DCore) released **2026-10-30**; [evaluation guide](https://github.com/ernie-research/DCore/blob/main/docs/evaluation.md). The author-led work is part of ERNIE Research; however the paper draws on Qwen3 target models and SGLang/SpecForge foundations, **not on ERNIE 5.5 target inference**.

| G0–G5 | Evidence and source-bound decision |
|---|---|
| **G0 IDENTITY — PASS** | Original arXiv title/ID; official authors' GitHub README and CITATION.cff; **preprint** identity maintained |
| **G1 SCOPE — PASS** | Studies inference throughput and acceptance vs execution overhead under actual SGLang speculative-decoding paths |
| **G2 MECHANISM — PASS** | Aligns released-checkpoint comparison vs matched **retraining** and deployment; uses common data/runtime and cost-aware ablations; DCore synthesizes DFlash efficient backbone, DFlare target-layer context mixture and D-PACE objective. Related baselines: [EAGLE-3](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c7b5a35ea98b62512a869c19ea7b03cb-Abstract-Conference.html), [DSpark / DeepSpec](https://github.com/deepseek-ai/DeepSpec), [DFlash](https://github.com/z-lab/dflash), plus DFlare/D-PACE/Domino; also benchmark-design context in [On Evaluating Performance of LLM Inference Serving Systems](https://arxiv.org/abs/2507.09019) |
| **G3 EVIDENCE — PASS WITH CAVEATS** | 7 methods (DCore + 6 recipes), 26 retrained draft checkpoints, two targets **Qwen3-4B/8B**, 10 benchmarks, draft budget **8/16**, three target:draft temperature pairs **0:0/1:0/1:1**, concurrency sweeps; authors report TPS, proposal latency, acceptance and target-only comparisons. **Author-report**, not independent. Some experiment optimization is single-request; do not present as generic production goodput. Training configurations must match |
| **G4 REPRO — ARTIFACT_INSPECTED, NOT_RUN** | [Public code](https://github.com/ernie-research/DCore) and checkpoints, data/training/evaluation scripts, SGLang submodule; reference H800 and CUDA/Python environment. We verified README and source navigation but **did not install or run**, so cannot certify exact replication |
| **G5 VALUE — PASS** | Solves a recurrent failure in system papers: *acceptance length ≠ throughput, and trained-drafter comparison ≠ model/hardware-neutral evaluation*. Strong actionable baseline for new speculative research, directly aligned with this repo's audit policy |

**Decision:** **KEEP_STRICT** under [Benchmarking & Systems Analysis → Performance & Efficiency Studies](../topics/benchmarking-analysis.md) as a methodologically controlled comparison with executable DCore exemplar, rather than adding the same work a second time under Decoding Acceleration. **AUTHOR_REPORTED / MODEL_CHANGED / REQUIRES_TRAINED_DRAFTER / PUBLIC_ARTIFACT / NOT_REPRODUCED**. No global 'fastest drafter' assertion. Dataset/task selection, 26 checkpoints, target sampling policy, batch/concurrency and hardware are all comparability conditions.

### DCore metric and reproducibility traps (inspected upstream evaluation guide)

The [authors' evaluation guide](https://github.com/ernie-research/DCore/blob/main/docs/evaluation.md) explicitly separates `tokens_per_second` (request-level at concurrency=1) from `extra.wall_toks_per_s` (aggregate wall-clock across replicas); **do not interchange these denominators**. `accept_length` counts committed tokens **including** the bonus token. In the published setting, eight H800 instances with `--dp-size 8 --concurrencies 1` mean **eight global concurrent requests**, not one; the target-only baseline and DCore must use the same per-replica concurrency and sampled target/draft temperatures.

The docs warn that (i) a small eight-prompt / 128-token smoke run is not the paper's full benchmark; (ii) paper-style TPS for sampled targets uses the **mean of three repeats**, while some formatting utilities choose the **fastest**; (iii) a freshly collected target-only reference need not equal the paper's shared reference; and (iv) resuming an old `--run-dir` fails to detect every parameter change. The full reported runs use a **2048-token cap**, bf16, FlashInfer, CUDA graphs and a pinned SGLang fork rather than merely a package version. These are substantive reproducibility limitations, not footnotes.

## 6. Why other candidates are not added as canonical LLM-inference rows here

| Candidate | Decision | Reason / next evidence needed |
|---|---|---|
| ERNIE 2019–3.0 and 5.0 model reports | **KEEP_ORG_ONLY** | NLP/model architecture and training lineage; architectural novelty can motivate systems work but is not a measured new serving engine |
| ERNIE 5.5 Flash Base announcement | **KEEP_ORG_ONLY** | Valuable model architectural budget allocation with published weights, but **model-change + vendor base evaluation**, not controlled deployment-performance paper |
| FlashMask (ICLR 2025) and FlashMask-3 (NeurIPS 2026) | **KEEP_ORG_KERNEL_LINEAGE; HOLD_TOPIC_SCOPE** | Good original attention kernels and distributed training mechanisms, mostly forward+backward/long-context **training** evidence; strict list is inference-driven. A real serving prefill/decode impact study could change this judgment |
| FlashMask-4 code | **KEEP_ORG_IMPL** | Executable GPU kernel with hardware/shape/forward/backward contracts; no separate peer-reviewed FlashMask-4 serving paper established |
| PLAS | **KEEP_ORG_ENGINEERING; HOLD_TOPIC_EVIDENCE** | FastDeploy docs and limited ERNIE 4.5 long-context benchmark; trained gating is an approximate model path; broad quality/other context distributions and comparator parity not established |
| VHA / Multi-View Latent MoE / ECHO | **KEEP_ORG_OR_MODEL_CONTEXT; HOLD_TOPIC_G1/G3** | Strong architecture and training ideas; separately prove real serving overhead/quality and model-compatible end-to-end gains for canonical inference systems |
| JIZHI | **KEEP_ORG_ADJACENT** | Genuine KDD 2021 production recommendation inference, not autoregressive LLM serving; historically valuable for serving research lineage |
| ERNIE Evolve | **KEEP_FRONTIER_INDUSTRY_SOURCE** | Interesting cross-layer optimizer/experience-bank account; benchmark artifacts public, **commercial inference optimization replay/held-out optimizer transfer absent** |

## 7. Practical reading and test priority

**P0 — read (no NPU needed):** [ERNIE 5.5 full architecture](https://ernie.baidu.com/release/ernie-5-5-flash-base/) → [FastDeploy code overview](https://paddlepaddle.github.io/FastDeploy/usage/code_overview/) → [resource manager](https://github.com/PaddlePaddle/FastDeploy/blob/develop/fastdeploy/engine/sched/resource_manager_v1.py) + [KV transfer manager](https://github.com/PaddlePaddle/FastDeploy/blob/develop/fastdeploy/cache_manager/cache_transfer_manager.py) → [DCore evaluation guide](https://github.com/ernie-research/DCore/blob/main/docs/evaluation.md) → [Evolve positive/negative experiments](https://ernie.baidu.com/research/posts/ernie-evolve/).

**P1 — comparison without changing current Ascend project:** extract a *contract comparison* of FastDeploy vs vLLM-Ascend pinned pair: request admission/priority and preemption; prefix-cache ownership and eviction; P/D block allocation and KV transfer; EP routing + synchronization. **Do not pretend its XPU/GPU kernel timings are portable to CANN 9.1 / Ascend 910B2.** Run only if a concrete mechanisms gap survives source-side audit.

**P2 — experimental candidates only after P1:** (a) Small-M GEMM operand/padding path vs native shape/precision and downstream consumer; (b) speculative draft/verify cost-aware scheduling, with DCore's fair baseline methodology; (c) whether per-layer compressed-attention KV contracts change residency/scheduling enough to produce new dynamic-Serving problems. Use matched quality, correctness, real hardware, same arrival process and output length; keep profiling and hypothesis-gate receipts.

**Conclusion:** Baidu is neither 'just an underperforming chatbot' nor the sole inventor of mechanisms shared across the industry. Its evidenced strength is an unusually broad *research → architecture → kernel/framework → production-derived execution → experimental optimization* chain. The high-value lesson for the awesome repository is to capture **mechanism and falsifiable cost**, without confusing borrowed components, pretraining accomplishments, single-kernel results and end-to-end serving.
