# November 4, 2026 — company-owned inference infrastructure source audit

**Scope:** a targeted expansion of [Organizations](../organizations/README.md) beyond closed foundation-model API vendors. **Result: 14 new profile pages, 7 China + 7 US; 3 existing company pages expanded (Meta, Google, Alibaba/Qwen).** This is **company/source mapping**, not G0–G5 admission of new canonical papers. No independent reproduction was attempted and the canonical paper count remains unchanged.

## Admission policy for this organization sweep

A company is documented when there is a first-party, traceable **(A) code artifact**, **(B) technical engineering/production report**, or **(C) serving/operational service contract** that changes how LLM inference is built, delivered or measured. Each profile must disclose which evidence class it actually has. A business selling AI endpoints does **not** thereby disclose a unique attention kernel, scheduler, proprietary model or RSI process. Research preprints are labeled preprints; vendor benchmark numbers remain attributed to authors. Named contributors to community projects receive credit without implying exclusive ownership.

### China: selected sources and precise status

| Company | Primary evidence | Included on what basis / boundary |
|---|---|---|
| Meituan | [SGLang-FluentLLM source](https://github.com/meituan-longcat/SGLang-FluentLLM), [LongCat-2.5 first-party technical release](https://tech.meituan.com/2026/11/02/Meituan-LongCat-2.5.html) | **A+B**: speculative graph/overlap, P/D KV transfer, W4A4 and domestic-device execution. Different engine/backends require separate verification. |
| Xiaohongshu | [RAI team](https://github.com/redai-studio), [HYPIC source](https://github.com/redai-studio/HYPIC), [Relax](https://github.com/redai-studio/Relax) | **A+B**: hybrid-attention segment reuse and rollout system. Not independently reproduced online-service throughput. |
| Ant Group | [vLLM/Ant Humming](https://vllm.ai/blog/2026-10-21-humming), [code](https://github.com/vllm-project/humming) | **A+B**: quantized dense/MoE JIT with community attribution and explicit precision/baseline differences. |
| Kuaishou | [Keye-VL source](https://github.com/Kwai-Keye/Keye), [Vanchin context caching docs](https://streamlake.com/document/WANQING/mkxypaeruepm2t9mp78) | **A+C**: model attention/long-video workload + public KV/prefix API, not an inspectable Vanchin scheduler. |
| JD.com / JD Cloud | [JoyMaaS](https://joymaas.jdcloud.com/) | **C**: inference API gateway, routing, tenancy and models; **no public kernel/runtime method established**. |
| iFLYTEK | [AICC platform](https://spark-aicc.iflytek.com/aicc-portal/), [official OSS](https://github.com/iFLYTEK) | **C**: heterogeneous inference service and platform, not a reproduced proprietary engine improvement. |
| Moore Threads | [vllm-musa](https://github.com/MooreThreads/vllm-musa), [MATE](https://github.com/MooreThreads/mate) | **A**: accelerator-specific backend/kernel port; version/device parity untested. |

### United States: selected sources and precise status

| Company | Primary evidence | Included on what basis / boundary |
|---|---|---|
| Anyscale | [Ray Serve LLM](https://github.com/ray-project/ray/blob/master/doc/source/serve/llm/index.md), [cookbook](https://github.com/anyscale/ai-infra-cookbook) | **A**: serving orchestration above vLLM/SGLang; shared Ray ownership acknowledged. |
| Baseten | [Truss](https://github.com/basetenlabs/truss) | **A**: packaging/deployment/engine integration; not exclusive TensorRT-LLM or SGLang ownership. |
| Databricks | [Joint production inference case study](https://www.databricks.com/blog/how-superhuman-and-databricks-built-200k-qps-inference-platform-together) | **B**: short-output grammar workload with FP8/CPU/kernel optimizations; not a long-response LLM baseline. |
| Red Hat | [llm-d v1.0](https://llm-d.ai/blog), [Red Hat release](https://www.redhat.com/en/about/press-releases/llm-d-1-advances-open-cost-efficient-ai-inference-production-scale) | **A+B**: distributed inference, QoS and day-2 operations; joint community project. |
| Cloudflare | [P/D service description](https://blog.cloudflare.com/high-performance-llms), [KV exposure remediation](https://blog.cloudflare.com/kv-cache-exposure-remediation/) | **B+C**: production P/D, KV ownership, failure-path and security contracts; credited SGLang upstream fixes. |
| Predibase | [LoRAX server](https://github.com/predibase/lorax) | **A**: heterogeneous adapter batching/preload/eviction; TGI heritage and kernel attribution stated. |
| CoreWeave | [Founding llm-d collaboration](https://www.coreweave.com/blog/the-next-chapter-for-ai-infrastructure-why-llm-ds-move-to-cncf-matters) | **B**: community co-founder and cloud operations; **not an exclusive inference engine release**. |

### Existing pages expanded, not new organizations

- [Meta KernelEvolve](https://engineering.fb.com/2026/04/02/developer-tools/kernelevolve-how-metas-ranking-engineer-agent-optimizes-ai-infrastructure/) (production kernel agent) and [LLM parallel inference](https://engineering.fb.com/2025/10/17/ai-research/scaling-llm-inference-innovations-tensor-parallelism-context-parallelism-expert-parallelism/). Ads recommendation results are not token-decoder E2E gains.
- [Google engineers' llm-d P/D topology contract](https://llm-d.ai/blog/topology-as-an-end-to-end-contract) (GKE, RDMA, router, GPU/NIC locality). The measured rail-affinity scorer was a **prototype**, so do not imply universal production 3.5x TTFT.
- [Alibaba RTP-LLM](https://github.com/alibaba/rtp-llm) (production-derived LLM serving across Alibaba business units); ecosystem implementation/credit is distinct from Qwen model families.

## Review exclusions and next checks

**Not promoted on this sweep:** Bilibili and Didi lacked a sufficiently direct, high-value, first-party 2025–26 LLM inference mechanism in the material reviewed. Other companies may own significant *private* infrastructure, but that cannot be inferred from product demand, headcount or job advertisements alone. iFLYTEK/JDCloud/Kuaishou product disclosures remain **platform-contract scope**, not claims of hidden implementations.

**Reproduction status:** not_attempted for all. Before performance claims become technical entries: pin source commits, model/checkpoint/tokenizer, device/driver/toolchain, precision and output equivalence; use real engine end-to-end TTFT/TPOT/Goodput and hidden workloads against strong contemporaneous baselines. A kernel, cluster controller, backend port, RL rollout engine and hosted model API are **different evidence units**.

**Editorial decision:** organizations directory expanded, **zero additional entries** in the eight canonical paper topics, **no change** to Frontier count. Review and deduplicate any later paper nominations separately.
