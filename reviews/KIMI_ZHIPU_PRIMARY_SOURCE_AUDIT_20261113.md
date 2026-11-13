# Moonshot AI / Kimi + Zhipu AI / GLM — organization source audit (2026-11-13)

## Purpose and decision

A **company-blueprint** closeout, modeled on the existing [Alibaba](../organizations/Qwen-Alibaba.md), [Baidu](../organizations/Baidu.md), [Tencent](../organizations/Tencent.md), [MiniMax](../organizations/MiniMax.md) and [ByteDance](../organizations/ByteDance.md) organization pages. The preexisting K3/K3.1 and GLM-5.3 information is preserved, but no single latest API model is allowed to obscure major original research or released inference systems.

**Changed:** [Moonshot/Kimi](../organizations/Moonshot-Kimi.md), [Zhipu/GLM](../organizations/Zhipu-GLM.md), [organization index](../organizations/README.md), this primary-source receipt and its review-index entry. **Unchanged:** all eight canonical topic lists, home count (**930**), grading/review standards and existing historical receipts.

## Moonshot — official source checks

| Source | Kept / newly mapped | Critical qualifier |
|---|---|---|
| [Moonshot official GitHub profile](https://github.com/MoonshotAI/.github/blob/main/profile/README.md) | The first-party catalog separates Research, Benchmarks, Agents and Service/Infra. Includes Kimi k1.5/K2/K2.5/K3, MoBA, Kimi Linear, AttnRes, Kimina-Prover, Kimi-VL/Audio, Moonlight, WorldVQA/PerceptionBench, Kimi Code and the infrastructure group. | Project-directory presence does not imply production deployment or current model availability. |
| [Kimi Code model IDs](https://www.kimi.com/code/docs/en/kimi-code/models) | Six documented service IDs, including K3.1 Pro and highspeed, K3 and 256k, and differently versioned `kimi-for-coding` vs highspeed. | API aliases/tiers/context windows are **not** separate inventions. |
| [K3 source](https://github.com/MoonshotAI/Kimi-K3) · [K3.1 model card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) · [vLLM K3.1 post](https://vllm.ai/blog/2026-11-04-kimi-k31-pro) | 69 KDA + 24 MLA attention layers, DSA sparse indexing in K3.1, separate recurrent/KV cache contracts and upstream serving integrations. | vLLM's reported 1.69× TTFT comparison at 340K on GB300 is **not** Moonshot-owned generic kernel gain or independently reproduced Ascend speed. |
| [Mooncake](https://github.com/kvcache-ai/Mooncake) · [MoonEP](https://github.com/MoonshotAI/MoonEP) · [FlashKDA](https://github.com/MoonshotAI/FlashKDA) · [Checkpoint Engine](https://github.com/MoonshotAI/checkpoint-engine) | KV-centric disaggregated serving, dynamic EP redundancy/token placement, CUTLASS KDA kernels, and in-place RL-rollout weight update. | Workload, ownership and hardware constraints explicitly separated. MoonEP != KV layer; Checkpoint Engine != cache engine; CUTLASS CUDA != Ascend. |
| [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code) · [Agent SDK](https://github.com/MoonshotAI/kimi-agent-sdk) | Public agent/runtime and product layer. | Application agent != LLM serving scheduler. |
| [Tsinghua event](https://www.tsinghua.edu.cn/info/1181/51205.htm) · [2014 interview transcript](https://tech.ifeng.com/c/8v1ZLaTFGkU) | Yang Zhilin's *undergraduate* research mentor Tang Jie later co-founded Zhipu. | Does not claim doctoral-supervisor status, shared source/code ownership or company genealogy. |

## Zhipu — official source checks

| Source | Kept / newly mapped | Critical qualifier |
|---|---|---|
| [THUDM GLM](https://github.com/THUDM/GLM), [ChatGLM3](https://github.com/zai-org/ChatGLM3), [GLM-4.5](https://github.com/zai-org/GLM-4.5) | Academic GLM/pretraining → ChatGLM → open MoE model history. | THUDM and Zhipu corporate/project ownership are **not equivalent**; clearly attribute co-research. |
| [GLM-5.2](https://z.ai/blog/glm-5.2), [GLM-5.3](https://z.ai/blog/glm-5.3), [GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) | 5.2 IndexShare and 1M context; **5.3 same base with new post-training**; **5.3-Flash separate new 320B/18B native multimodal base**, sparse+linear hybrid, IndexPool, mHC. | Three related releases but not identical model architectures or independent kernel results. |
| [GLM-Image](https://github.com/zai-org/GLM-Image), [CogVideo](https://github.com/zai-org/CogVideo), [GLM-ASR](https://github.com/zai-org/GLM-ASR), [GLM-OCR](https://github.com/zai-org/GLM-OCR) | Official multimodal architecture and generation family, speech and document understanding. | Image AR+diffusion, video diffusion and ASR are separate workload classes from LLM TPOT. |
| [Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM), [ZCode](https://github.com/zai-org/ZCode) | Public phone/computer-use agent and coding workspace/CLI source. | Harness/tool executions and UI do not reveal proprietary model serving. |
| [slime](https://github.com/THUDM/slime), [IndexCache](https://github.com/THUDM/IndexCache) | Open-source RL training–rollout integration; cross-layer DSA index reuse with published SGLang/vLLM patches. | These are specific **research/open implementations**, not automatic proof of the complete production GLM runtime. |
| [GLM-5.3-Flash technical post](https://z.ai/blog/glm-5.3-flash) · [Infra Agent retrospective](https://z.ai/blog/glm-built-its-inference-infrastructure) | Native Chinese-chip SGLang-based path, E/P/D split, ReplaySSM, hybrid INT8/FP8/BF16 cache, Layer Split and model-assisted kernel/serving iteration. | **~3× is vendor reported** vs an initial baseline on the same hardware. No public full production engine, matched vendor-independent benchmark or verified Ascend 910B2/CANN 9.1 pair is established. |

## Editorial acceptance and open questions

- **KEEP_ORG:** models, multimodal families, formal/agent research, training/RL, published systems implementations and product/developer platforms, with direct first-party URLs.
- **KEEP_CONTEXT:** historical Tang–Yang undergraduate mentorship; useful to understand the academic lineage, but irrelevant to technology ownership.
- **DEFER_TOPIC:** do not bulk-admit papers from company pages; any new canonical paper needs individual G0–G5 review and duplicate check.
- **UNVERIFIED:** product runtime internals, production code not open-sourced, vendor throughput without matching reproduction, and device compatibility not established.
- **Later deep dives (not required for this round):** MoonEP integration in concrete serving workloads; K3 recurrent-state scheduling; Zhipu Infra Agent reproducibility; specific SGLang EPD code and Chinese accelerator version matrices.

## Closeout contract

This change is **company main-work coverage**, not a paper sweep, kernel audit or new NPU study. Its acceptance criteria are a coherent blueprint (research → models → infra → agents/products), correct source attribution, a usable official reading path and preserved current paper counts.
