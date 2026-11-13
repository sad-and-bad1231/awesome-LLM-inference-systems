# Moonshot AI / Kimi

**Long-context model research → open MoE and native multimodal agents → KV-centric and distributed inference systems → Kimi products.** Moonshot's public record is broader than the latest K3 model: it includes attention algorithms, RL/training research, audio/vision/proving, and unusually substantial inference infrastructure.

[← Organizations](README.md) · [← Home](../README.md) · [2026-11-13 source audit](../reviews/KIMI_ZHIPU_PRIMARY_SOURCE_AUDIT_20261113.md)

## 1. The technology map

| Layer | Main work | Why it matters |
|---|---|---|
| **Foundation models** | [Kimi k1.5](https://github.com/MoonshotAI/Kimi-k1.5) · [K2](https://github.com/MoonshotAI/Kimi-K2) · [K2.5](https://github.com/MoonshotAI/Kimi-K2.5) · [K3](https://github.com/MoonshotAI/Kimi-K3) · [K3.1 Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | Open-model evolution from reasoning and agentic MoE to 1M-context, native vision and sparse/hybrid attention. |
| **Attention and architecture research** | [MoBA](https://github.com/MoonshotAI/MoBA) · [Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) · [KDA/FlashKDA](https://github.com/MoonshotAI/FlashKDA) · [AttnRes](https://github.com/MoonshotAI/Attention-Residuals) | Block-sparse selection, recurrent attention state, residual propagation and long-context execution. |
| **Multimodal and verifiable reasoning** | [Kimi-VL](https://github.com/MoonshotAI/Kimi-VL) · [Kimi-Audio](https://github.com/MoonshotAI/Kimi-Audio) · [Kimina-Prover](https://github.com/MoonshotAI/Kimina-Prover-Preview) | Image/audio understanding, speech-to-speech and Lean-style formal mathematical reasoning. |
| **Training / RL research** | [Moonlight / Muon](https://github.com/MoonshotAI/Moonlight) · [Kimi k1.5](https://github.com/MoonshotAI/Kimi-k1.5) · [K2.5 agent swarm](https://github.com/MoonshotAI/Kimi-K2.5) | Scalable optimization, reinforcement learning and parallel agentic workflows—not online decoding kernels. |
| **Inference infrastructure** | [Mooncake](https://github.com/kvcache-ai/Mooncake) · [MoonEP](https://github.com/MoonshotAI/MoonEP) · [FlashKDA](https://github.com/MoonshotAI/FlashKDA) · [Checkpoint Engine](https://github.com/MoonshotAI/checkpoint-engine) | Distributed KV transfer/storage, MoE expert balancing, KDA kernels and weight refresh across RL rollout engines. |
| **Agent and developer ecosystem** | [Kimi Code](https://github.com/MoonshotAI/kimi-code) · [Agent SDK](https://github.com/MoonshotAI/kimi-agent-sdk) · [Kimi Researcher](https://github.com/MoonshotAI/Kimi-Researcher) · [Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) | Coding, research and long-horizon workflows; separate **agent harnesses** from the model-serving engine. |
| **Evaluation / tooling** | [WorldVQA](https://github.com/MoonshotAI/WorldVQA) · [PerceptionBench](https://github.com/MoonshotAI/PerceptionBench) · [CombiBench](https://github.com/MoonshotAI/CombiBench) · [Vendor Verifier](https://github.com/MoonshotAI/Kimi-Vendor-Verifier) | Multimodal/math evaluation and vendor precision monitoring, not evidence of kernel speedups. |

**Fast orientation:** Moonshot's distinguishing systems contribution is not only an advanced model architecture: **Mooncake + MoonEP + FlashKDA + Checkpoint Engine** expose useful interfaces across state residency, distributed experts, low-level operators and training/rollout coordination. The company also maintains a broad open research portfolio. See the [official Moonshot project directory](https://github.com/MoonshotAI/.github/blob/main/profile/README.md).

## 2. Model lineage and current service names

| Model family / identity | Main contribution | Source |
|---|---|---|
| **Kimi k1.5 → K2** | Long-reasoning RL lineage; K2 introduces very large sparse MoE and agentic code/tool execution. | [k1.5](https://github.com/MoonshotAI/Kimi-k1.5) · [K2](https://github.com/MoonshotAI/Kimi-K2) |
| **Kimi K2.5** | Native visual-language agent model, continued multimodal pretraining from K2, and publicly described Agent Swarm-style parallel task execution. | [K2.5 technical repository](https://github.com/MoonshotAI/Kimi-K2.5) |
| **Kimi K3** | 2.8T total / 104B activated MoE; 69 Kimi Delta Attention (KDA) + 24 Gated MLA layers, AttnRes and 1M context. Recurrent state and standard KV caches are different runtime concerns. | [K3 architecture / weights](https://github.com/MoonshotAI/Kimi-K3) |
| **Kimi K3.1 Pro** | October service model with [November 4 public weights](https://huggingface.co/moonshotai/Kimi-K3.1-Pro); 24 MLA layers add DSA sparse indexers while KDA layers remain. Upstream vLLM documents sparse MLA and recurrent-state execution. | [Model card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [vLLM Nov 4 analysis](https://vllm.ai/blog/2026-11-04-kimi-k31-pro) |
| **Kimi-VL / Kimi-Audio / Kimina-Prover** | Specialized vision-language, audio conversation and verifiable mathematical reasoning research, separate from API deployment tiers. | [VL](https://github.com/MoonshotAI/Kimi-VL) · [Audio](https://github.com/MoonshotAI/Kimi-Audio) · [Prover](https://github.com/MoonshotAI/Kimina-Prover-Preview) |

**Live API ID crosswalk (2026-11-09):** [official Kimi Code models](https://www.kimi.com/code/docs/en/kimi-code/models) listed **six service IDs**: `k3.1-pro`, `k3.1-pro-highspeed`, `k3`, `k3-256k`, `kimi-for-coding` (K2.8 Preview), and `kimi-for-coding-highspeed` (K2.7 Code Highspeed). These do **not** represent six unrelated architectures: context limits, high-speed tiers and routing aliases must be distinguished from model versions. Read the provider catalog again when exact IDs matter.

## 3. Research directions beyond the flagship

- **Long-context computation:** [MoBA](https://github.com/MoonshotAI/MoBA) investigates Mixture of Block Attention; [Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) studies hybrid recurrent/attention execution; [Attention Residuals](https://github.com/MoonshotAI/Attention-Residuals) changes residual-stream propagation. These are **model research**, not three independent serving engines.
- **Multimodal foundations:** [Kimi-VL](https://github.com/MoonshotAI/Kimi-VL) and [Kimi-Audio](https://github.com/MoonshotAI/Kimi-Audio) provide model weights/research and evaluation artifacts. [WorldVQA](https://github.com/MoonshotAI/WorldVQA) and [PerceptionBench](https://github.com/MoonshotAI/PerceptionBench) help separate perception and reasoning benchmarks.
- **Mathematical reasoning and training:** [Kimina-Prover](https://github.com/MoonshotAI/Kimina-Prover-Preview) explores proof-oriented RL; [Moonlight/Muon](https://github.com/MoonshotAI/Moonlight) is training-optimizer research. Their published results should not be presented as decode kernel throughput.

## 4. Public inference and serving infrastructure

| Implementation | Actual technical role | Boundary |
|---|---|---|
| **[Mooncake](https://github.com/kvcache-ai/Mooncake)** | KV-centric disaggregated LLM serving with a Transfer Engine and distributed KV/cache storage; an established Moonshot-linked systems project. | KV between serving workers is not the KDA model's per-layer recurrent state; community project ownership should be attributed accurately. |
| **[MoonEP](https://github.com/MoonshotAI/MoonEP)** | Expert Parallelism (EP) communication library using dynamic redundant experts and direct token placement to mitigate routing imbalance. | Project benchmarks are hardware/workload specific; not a promise of perfect balance in every runtime or NPU. |
| **[FlashKDA](https://github.com/MoonshotAI/FlashKDA)** | CUTLASS-based KDA kernels used as an optional Flash Linear Attention backend. | README's CUDA SM90+/CUDA version requirements do not establish Ascend 910B2/CANN compatibility. |
| **[Checkpoint Engine](https://github.com/MoonshotAI/checkpoint-engine)** | Lightweight in-place model-weight update middleware for multi-GPU RL/rollout inference, with broadcast and P2P modes and SGLang integration. | Bridges training and rollout deployments; **not** a general KV-cache scheduler. |
| **[Kimi Vendor Verifier](https://github.com/MoonshotAI/Kimi-Vendor-Verifier)** · [moonpalace](https://github.com/MoonshotAI/moonpalace) | Model API numerical correctness monitoring and service debugging. | Reliability/verification tooling—not an inference speed result. |

**K3.1 deployment nuance:** the [vLLM technical post](https://vllm.ai/blog/2026-11-04-kimi-k31-pro) describes handling *packed MLA latent states, sparse index keys and KDA recurrent states* alongside specialized sparse-decode kernels. Its reported 1.69× TTFT comparison at 340K context was on **8× GB300**, not a matched Ascend result. Do not infer general GPU/Ascend compatibility or attribute upstream engine innovations solely to Moonshot.

## 5. Products, organization context and reading path

[Kimi](https://www.kimi.com/) is Moonshot's consumer/knowledge-work assistant; [Kimi Code](https://github.com/MoonshotAI/kimi-code) supplies a public terminal coding agent and [Agent SDK](https://github.com/MoonshotAI/kimi-agent-sdk) enables agent integrations. The [Kimi API/model documentation](https://www.kimi.com/code/docs/en/kimi-code/models) describes externally accessible model versions and service tiers. Agent code, model weights and provider runtimes are separate artifacts.

**Historical research connection:** founder **Yang Zhilin (杨植麟)** studied research methods under **Tang Jie (唐杰)** at Tsinghua as an *undergraduate research mentee*, before going to CMU. Tang later co-founded Zhipu AI. This is a mentorship relationship, not a claim Tang supervised Yang's CMU PhD or that the companies share technology ownership. [2014 Tsinghua scholarship event](https://www.tsinghua.edu.cn/info/1181/51205.htm) · [contemporary account and reconstructed statement](https://tech.ifeng.com/c/8v1ZLaTFGkU).

**Suggested overview:** [official research catalog](https://github.com/MoonshotAI/.github/blob/main/profile/README.md) → k1.5/K2/K2.5/K3/K3.1 → MoBA/Kimi Linear/AttnRes → Mooncake/MoonEP/FlashKDA/Checkpoint Engine → Kimi Code and API products. The goal is to understand the organization, not prematurely deep-dive one operator.

**Evidence boundary (2026-11-13):** model architecture, original code, co-developed community infra, API tiers and vendor benchmarks are distinct. No new canonical paper admission, reproduction claim or Ascend compatibility claim is made here.
