# 2026 Agent-native Serving — Conference / arXiv / Industry / Lab Gap Audit

**Audit date:** 2026-11-03 (America/Los_Angeles). **Repository baseline:** October 31 `main` = 851 canonical rows; pending November first pass [PR #72](https://github.com/sad-and-bad1231/awesome-LLM-inference-systems/pull/72) adds 3 = 854. This **stacked** agent audit adds **12 independently source-reviewed nonduplicates**, proposed **866** canonical rows after both PRs. The new branch is based on PR #72, not directly on `main`.

**Editorial scope:** selectively investigate 2026 ACL Main/Findings, EMNLP Main/Findings/Industry, ICML/MLSys/NSDI/OSDI, July–October 2026 arXiv (plus high-value earlier backfill), production engine code/RFCs and source-linked institutional reports. This is **not an exhaustive crawl** of every 2026 ACL/EMNLP/arXiv paper. Candidate sample audited here: **44 named research items**, with **8 implementation signals + 6 lab/source crosswalks**. No GPU/NPU code execution or independent quantitative replication was performed.

## 1. G0–G5 source-admission matrix — 12 new canonical records

**Every KEEP is source-level bibliographic + mechanism + author-evidence acceptance only**, not `G3 replicated` or `G4 executed`. One primary canonical home per paper. Specific hardware, baselines, task correctness and performance metrics do not transfer across contexts.

| Paper | Verified source identity | Decisive mechanism / closest distinction | Author evidence and G3 bound | G4 / verdict |
|---|---|---|---|---|
| [ThunderAgent](https://proceedings.mlr.press/v306/kang26j.html) | ICML 2026 / PMLR | **Runtime:** LLM program as schedule unit + tool environment/disk/KV coordinated | coding/routing/science agents; published serving throughput 1.5–3.6× and separate RL figures | public implementation; not_attempted; **KEEP_STRICT (source)** |
| [RoleKV](https://aclanthology.org/2026.emnlp-main.1982/) | EMNLP 2026 Main | **KV:** Role-aware block residency and eviction (system/tool/reasoning), without changing KV content | 8B–70B; multicard; measured preemptions, PCIe traffic and E2E latency; role-generalization unknown | public artifact not established; not_attempted; **KEEP_STRICT (source)** |
| [AgentKV](https://aclanthology.org/2026.emnlp-main.2514/) | EMNLP 2026 Main | **KV:** Think/Act/Tool query distributions; per-phase query buffers, importance and page compaction | SGLang persistent compressed cache; task score vs R-KV/Tri-attention and TPS vs full KV; accuracy-changing | author code; not_attempted; **KEEP_STRICT (source)** |
| [UltraQuant](https://aclanthology.org/2026.emnlp-industry.161/) | EMNLP 2026 Industry | **Quant:** AMD CDNA4 FP8 query / FP4 KV group scales + native MFMA attention and cache size | production Claude Code trace replay; BF16 SLO-qualified request TPS; approximation/architecture-dependence | author systems measurement; not_attempted; **KEEP_STRICT (source)** |
| [CacheScout](https://arxiv.org/abs/2608.14624) | 2026 preprint (first July, arXiv 2608) | **KV:** Learn Agent transition online; KV survival / conditional background prefetch without declared DAG | vLLM0.11; real RTX PRO6000 and H200; TTFT/turn throughput; workflow trace, not task success | public artifact not confirmed; not_attempted; **KEEP_STRICT (source)** |
| [Ask the Tool, Don't Guess](https://arxiv.org/abs/2609.18849) | 2026 Sep preprint | **KV:** Tool progress while running as retention/prefetch signal, not fixed pre-call duration guess | four corpus survey and 4×H100 replay; post-tool p90 TTFT improvement vs LRU, not total JCT | progress-source portability requires testing; not_attempted; **KEEP_STRICT (source)** |
| [Production Agent Serving Characterization](https://arxiv.org/abs/2609.34432) | 2026 Sep preprint (Ant Group/CUHKSZ) | **Benchmark:** Task→Workflow→GPU infrastructure joint trace and state residency analysis | 2 weeks, 11.7M requests, 948.4k sessions, >10k GPU infrastructure, proprietary platform | observational study, no causal speedup / public raw trace confirmed; not_attempted; **KEEP_STRICT (source)** |
| [Continuum](https://arxiv.org/abs/2511.02230) | arXiv first submitted 2025; 2026 Berkeley report / ICLR workshop | **Runtime:** Program-level FCFS + tool duration-aware cache TTL/pinning for turn continuity | SWE-bench/BFCL/other agent tasks; multiple real model/hardware setups; JCT not single-call TPS | author vLLM preview code; not_attempted; **KEEP_STRICT (source)** |
| [Sutradhara](https://arxiv.org/abs/2601.12967) | 2026 preprint / Microsoft Research tech report | **Runtime:** Orchestrator-engine thin hints for early tool dispatch, split prefill overlap and KV management | A100 / vLLM, controlled production-like synthetic requests; median final FTR and E2E are distinct | author system study; not_attempted; **KEEP_STRICT (source)** |
| [Helium](https://arxiv.org/abs/2603.16104) | 2026 preprint | **Runtime:** Agent workflow = query plan; LLM operators, plan rewrite/result reuse and cache-aware batching | real dual H100 NVL + vLLM0.16; script workflows; cached output can alter sampling semantics | public code not verified; not_attempted; **KEEP_STRICT (source)** |
| [SAGA](https://arxiv.org/abs/2605.00528) | 2026 preprint | **Runtime:** Workflow-atomic scheduling, agent fair share and affinity work stealing | author reports real 64-GPU SWE-bench/WebArena; JCT gain with 30% peak-TPS loss vs throughput optimum | code/hardware receipts not independently verified; not_attempted; **KEEP_STRICT (source)** |
| [TOPAS](https://arxiv.org/abs/2608.25523) | 2026 Aug preprint | **Runtime:** Joint per-agent prefix residency & ready request admission under workflow critical-path JCT | real SGLang; 3 synthetic DAGs plus 2 MetaGPT workloads; known DAG/limited production representativeness | code availability not independently verified; not_attempted; **KEEP_STRICT (source)** |

**Quality distinctions:** RoleKV selects whole-KV *residency* and claims lossless policy; AgentKV uses *compressed/pruned KV* and changes semantic quality. UltraQuant changes precision and relies on CDNA4 optimized math. Helium reuses completed prompt results and thus must separately control stochastic semantic equality. CacheScout learns agent transition structure; TOPAS requires a known DAG and co-optimizes residency + admission; SAGA is explicitly willing to lose peak token TPS for workflow JCT. DO NOT collapse these into a generic "Agent KV speedup".

## 2. Previously indexed, not new admissions — 20 sample anchors

The repository **already** holds the following canonical papers (or intentionally as a dedicated historical foundation); a second duplicate category row would be misleading. These are part of the audit denominator but **not** +12.

| Existing work | Primary verified reference | Disposition |
|---|---|---|
| [Agentix (NSDI 2026)](https://www.usenix.org/conference/nsdi26/presentation/luo) | https://www.usenix.org/conference/nsdi26/presentation/luo | **ALREADY_INDEXED** / cross-reference only |
| [Murakkab (OSDI 2026)](https://www.usenix.org/conference/osdi26/presentation/chaudhry) | https://www.usenix.org/conference/osdi26/presentation/chaudhry | **ALREADY_INDEXED** / cross-reference only |
| [Parrot (OSDI 2024)](https://www.usenix.org/conference/osdi24/presentation/lin-chaofan) | https://www.usenix.org/conference/osdi24/presentation/lin-chaofan | **ALREADY_INDEXED** / cross-reference only |
| [SMetric](https://arxiv.org/abs/2607.08565) | https://arxiv.org/abs/2607.08565 | **ALREADY_INDEXED** / cross-reference only |
| [TAO](https://arxiv.org/abs/2610.37230) | https://arxiv.org/abs/2610.37230 | **ALREADY_INDEXED** / cross-reference only |
| [PackServe](https://arxiv.org/abs/2609.33224) | https://arxiv.org/abs/2609.33224 | **ALREADY_INDEXED** / cross-reference only |
| [Vesta](https://arxiv.org/abs/2610.14686) | https://arxiv.org/abs/2610.14686 | **ALREADY_INDEXED** / cross-reference only |
| [AgentSysBench](https://arxiv.org/abs/2608.15127) | https://arxiv.org/abs/2608.15127 | **ALREADY_INDEXED** / cross-reference only |
| [TraceLab](https://arxiv.org/abs/2606.30560) | https://arxiv.org/abs/2606.30560 | **ALREADY_INDEXED** / cross-reference only |
| [MORI](https://arxiv.org/abs/2606.00866) | https://arxiv.org/abs/2606.00866 | **ALREADY_INDEXED** / cross-reference only |
| [TokenCake](https://arxiv.org/abs/2510.18586) | https://arxiv.org/abs/2510.18586 | **ALREADY_INDEXED** / cross-reference only |
| [PBKV](https://arxiv.org/abs/2605.06472) | https://arxiv.org/abs/2605.06472 | **ALREADY_INDEXED** / cross-reference only |
| [GraphTok](https://arxiv.org/abs/2610.13325) | https://arxiv.org/abs/2610.13325 | **ALREADY_INDEXED** / cross-reference only |
| [AgentSpec](https://aclanthology.org/2026.emnlp-main.585/) | https://aclanthology.org/2026.emnlp-main.585/ | **ALREADY_INDEXED** / cross-reference only |
| [HEAR Protocol](https://arxiv.org/abs/2610.06597) | https://arxiv.org/abs/2610.06597 | **ALREADY_INDEXED** / cross-reference only |
| [ProMCP](https://aclanthology.org/2026.findings-acl.1967/) | https://aclanthology.org/2026.findings-acl.1967/ | **ALREADY_INDEXED** / cross-reference only |
| [DualPath](https://doi.org/10.1145/3789240.3829159) | https://doi.org/10.1145/3789240.3829159 | **ALREADY_INDEXED** / cross-reference only |
| [KAIROS](https://arxiv.org/abs/2604.16682) | https://arxiv.org/abs/2604.16682 | **ALREADY_INDEXED** / cross-reference only |
| [FlashAgents (MLSys 2026)](https://proceedings.mlsys.org/paper_files/paper/2026/hash/9a6f6e0d6781d1cb8689192408946d73-Abstract-Conference.html) | https://proceedings.mlsys.org/paper_files/paper/2026/hash/9a6f6e0d6781d1cb8689192408946d73-Abstract-Conference.html | **ALREADY_INDEXED** / cross-reference only |
| [Pythia](https://arxiv.org/abs/2604.25899) | https://arxiv.org/abs/2604.25899 | **ALREADY_INDEXED** / cross-reference only |

*Technical caveat:* The current Frontier previously referenced **ThunderAgent** as its flagship anchor, but the canonical 8-topic paper pages contained **no** ThunderAgent entry. The topical inclusion in this PR repairs that omission. It does not make the ICML paper newly published in November.

## 3. Watch / HOLD / exclude decisions — 12 items

**These are not canonical admissions.** A HOLD is an evidence/scope need, not a claim the paper is defective. The candidate URL must be verified as paper-specific before future admission; two broad venue-list placeholders below are for discovery only.

| Source / candidate | G-gate and reason |
|---|---|
| [H-MAS](https://aclanthology.org/2026.findings-acl.1946/) | A multi-agent *controller for generic LLM scheduling*, not necessarily an agent-session workload; genuinely evaluates LLM server goodput, but belongs to independent generic runtime audit, not this Agent-native gap admission. |
| [LLM-as-Scheduler (LAS)](https://aclanthology.org/2026.acl-long.581/) | Application-level choice among workflows by confidence/cascade; token/latency improvements change which LLM operations run. No GPU engine scheduling mechanism; REMOVE_SCOPE for this selective inference bibliography. |
| [CondenseFlow](https://aclanthology.org/2026.findings-acl.669/) | Learned latent/KV message compression in multi-agent collaboration; performance and semantic fidelity do not yet establish generic vLLM/SGLang online serving benefit. HOLD_G3. |
| [A Policy-Driven Runtime Layer / CacheSage](https://arxiv.org/abs/2605.27744) | Earlier same-group runtime/transition-learning concept overlapping the later CacheScout system with stronger hardware details; keep as linked precursor, avoid second canonical row until distinct non-subsumed contribution. HOLD_G5_ALIAS_LINEAGE. |
| [Leyline](https://arxiv.org/abs/2606.01065) | Promising explicit KV edit directive; reuses Irminsul MLA RoPE correction. Editing an old causal prefix cannot generally preserve all downstream hidden states by rotation alone; paper treats splicing vs semantic forgetting separately. HOLD_CORRECTNESS/QUALITY until exact equivalence and quality conditions are audited. |
| [Irminsul](https://arxiv.org/abs/2605.05696) | MLA-specific content-addressable shifted-context reuse; position rotation alone does not remove causal-dependency effects of changing prefix. Contains narrow output-consistency tests, but universal exactness needs careful G3 evaluation. HOLD_G3 before canonical claim. |
| [From Static Templates to Dynamic Runtime Graphs (survey)](https://aclanthology.org/2026.findings-emnlp.1393/) | Useful adjacent workflow taxonomy, not inference-system optimization evidence; reference in review only. |
| [AgenticRAGTracer](https://aclanthology.org/2026.findings-acl/) | Agent evaluation dataset and reasoning quality, no direct serving engine tracing/latency/cost control shown. REMOVE_SCOPE for inference bibliography. |
| RealFin (paper-specific primary source not yet resolved) | Finance-domain MCP-style tool-orchestration benchmark; not admitted without an attributable primary paper and a demonstrated inference-engine systems mechanism. **HOLD_IDENTITY / REMOVE_SCOPE** pending verification. |
| [Toollery](https://aclanthology.org/volumes/2026.emnlp-industry/) | Tool retrieval/skills selection may reduce prompt tokens; without a controlled inference-engine execution study, not Agent-serving runtime. REMOVE_SCOPE for this tranche. |
| [Role-conditioned Context Routing](https://aclanthology.org/volumes/2026.findings-emnlp/) | Agent semantic memory selection under token budget; needs same-task semantic quality and serving runtime evidence, not exact KV residency. HOLD_SCOPE. |
| [Speculate While You Reason](https://arxiv.org/abs/2609.18849) | Self-speculating agent trained for tool-call prediction, cited in Ask the Tool; author-reported next-tool accuracy ≠ demonstrated generic inference serving runtime speedup. Separate model-policy/quality line, not canonical this batch. |

**Key false-positive pattern:** "multi-agent scheduler" may mean LLM **agents implement the scheduler**, not that the requests are agent-generated session DAGs; and an "agent workflow latency" paper can reduce calls by choosing simpler model policies without improving *the same* inference execution. Conversely, GPU/NPU Cache/Kernel mechanisms with a true agent workload are directly relevant.

## 4. Industrial implementations and research-lab source crosswalk

**Industrial source matrix (implementation≠publication; RFC≠deployed feature):**

| Source | First-party / source-linked implementation evidence |
|---|---|
| [vLLM + AgentX](https://vllm.ai/blog/2026-09-08-vllm-agentx) | AgentX trace, token profile, hybrid KV and P/D; session hints and programmable cache described as planned work, not all shipped. |
| [vLLM + Mooncake](https://vllm.ai/blog/2026-05-06-mooncake-store) | Distributed agent-prefix cache and trace-replay throughput/TTFT on GB200; blog results from constrained model/workloads, not universal speedup. |
| [NVIDIA Dynamo session-aware](https://pytorch.org/blog/session-aware-agentic-inference-with-nvidia-dynamo/) | Common session_id/parent ID, agent-linked tracing/replay, session admission/routing; shared-pool indexing and KvHint in experimental/proposed phases; verify feature branch before asserting prod support. |
| [NVIDIA Dynamo full-stack](https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/) | Harness metadata, routed KV, multi-tier residency and parser/tool-call streaming; first-party engineering blog, no extra paper entry. |
| [SGLang Session-aware Radix Cache](https://github.com/sgl-project/sglang/blob/main/docs/docs/advanced_features/session_radix_cache.mdx) | Implemented documented opt-in UnifiedRadixCache session references with soft eviction; session ID does not reconstruct full conversation. Hardware/backend variants must be checked. |
| [SGLang Programmable KV RFC](https://github.com/sgl-project/sglang/issues/27574) | Phase 1 session IDs / radix nodes, Phase 2 hint API proof-of-concept; TODO for some HiCache L3 and prefetch/demote pieces. RFC != production. |
| [Ant Group + CUHKSZ production](https://arxiv.org/abs/2609.34432) | Cross task/workflow/infra 11.7M request system characterization; distinguish proprietary observations vs published raw trace. |
| [Microsoft Research Sutradhara](https://www.microsoft.com/en-us/research/publication/sutradhara-an-intelligent-orchestrator-engine-co-design-for-tool-based-agentic-inference/) | Orchestrator-engine design on vLLM A100; public research report, not proof current vLLM upstream integrated design. |

**Labs and contributing research groups (coauthorship ≠ exclusive ownership):**

| Source group | Relation |
|---|---|
| [UW SyFI / TraceLab](https://github.com/uw-syfi/TraceLab) | ~4,300 coding sessions and 350k LLM steps; actual traces/analysis; local-team usage causes representativeness bias. |
| [UC Berkeley / Continuum & Agentix](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2026/EECS-2026-234.html) | Program-level scheduling and TTL from Berkeley research; do not merge 2025 arXiv, 2026 workshop, 2026 thesis into multiple independent papers. |
| [CMU/Georgia Tech collaborators / ThunderAgent](https://github.com/ThunderAgent-org/ThunderAgent) | Program-aware inference framework, genuine execution/tool-state abstraction; no single-institution ownership claim. |
| [Ant Group + CUHKSZ](https://arxiv.org/abs/2609.34432) | Production workload + PackServe; user-facing report is author analysis, not independent raw-trace validation. |
| [NVIDIA/Dynamo engineering contributors](https://github.com/ai-dynamo/dynamo) | Fast-moving code/RFC/documentation; source commits and versioned endpoints matter more than future-oriented blog. |
| [Microsoft Research](https://arxiv.org/abs/2601.12967) | Tool execution/prefill co-design with real A100; source architecture, not automatically a released production endpoint. |

## 5. Synthesis: what crosses the engine boundary?

A **stateful Session** (identity, parent-child relation, turn phase and tool wait) is a stronger optimization unit than isolated requests, but an Agent framework should not directly overwrite the inference engine's KV pointers. Separate *hint intent* from *executed authoritative state* and preserve isolation/correctness:

1. **Read-only trace contract:** `session_id`, `parent_session_id`, `turn_idx`, prompt prefix block hashes / state identity, timestamp, tool start/finish, durable/ephemeral scope, arrival/finish and SLO; avoid logging sensitive tool contents by default.
2. **Optional soft hints:** expected tool finish or ongoing progress, priority/deadline, anticipated fan-out or reuse horizon. A missing/wrong hint must safely fall back to regular serving and be measured as such.
3. **Engine-enforced resource contract:** cache admission, soft pin/demote/prefetch, per-session HBM/DRAM budget, backpressure, cancellation and cleanup; no cross-tenant sharing without explicit authorization.
4. **Measurements at two levels:** engine TTFT/TPOT/Goodput/cache miss/reloads/PCIe+RDMA/HBM, **and** full task/session P95 JCT, verified success per GPU-hour/joule and interference. Exactness for residency/transfer and quality parity for compression/result reuse must be separate gates.
5. **Closed-loop vs trace replay:** static request replay can establish an inference-path delta, not how changed latency affects tool timing, fan-out, retries, cancellation and task success. End-to-end validation must re-run a live/simulated-agent driver with controlled dependencies.

**Future Ascend route (not yet an experiment):** begin at read-only session/turn trace in vLLM-Ascend 0.23 pair; audit possible available request metadata before proposing extension. Compare fixed trace vs closed-loop harness only after instrumentation; measure KV residency and workload shape changes before modifying low-level kernels. Never infer that CUDA/NVIDIA/AMD source performance ports to CANN/NPU without independent correctness and profiling.

## 6. Verification and source limits

- **Admission delta (relative to pending 854):** KV +4; Runtime +6; Quantization +1; Benchmarking +1 = **12**; target **866**. All 8 source categories remain, no ninth Agent category.
- **One canonical URL each:** new source rows checked against already listed URLs and descriptive aliases. ThunderAgent previously frontier-only was a genuine canonical omission.
- **No independent G3/G4:** all 12 `not_attempted`; code presence is recorded only when author/full text identifies it. Author results remain unconfirmed on Ascend, and production numbers are owned by the citing companies.
- **Audit priority:** correctness of edited/shifted KV and compressed cache; fair comparison of Session-level vs Request-level objective; dynamic agent replay vs live; parent/child eviction and cache ownership; tool-progress observability and security.

**Decision:** Treat **Agent-native Serving as a first-class cross-cutting research program**, maintain eight mechanism homes for papers and extend the Frontier with (a) program-level execution control, (b) session/KV state lifecycle, (c) tool/engine cross-layer contracts, (d) production workload verification. Do not merge generic Agent prompt-workflow optimization into the inference corpus by keyword.
