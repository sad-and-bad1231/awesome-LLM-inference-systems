# JD.com / JD Cloud

A useful case of a major **inference-service operator with limited public low-level implementation disclosure**. Its cloud API and model products should be studied as service contracts, not mistaken for verified new CUDA/Ascend kernels.

[← Organizations](README.md)

## First-party service evidence

| Source | Executed or externally visible contract | What cannot be concluded |
|---|---|---|
| [JoyMaaS](https://joymaas.jdcloud.com/) · [model registry](https://joymaas.jdcloud.com/models) | Enterprise model-service gateway with a normalized API, authentication, rate limiting, routing, load balancing, fallback and usage/cost controls; serves JD-built models alongside third-party models. | A **published service/API surface**. Request-routing policy, internal P/D topology, kernel code and measured fleet utilization are **not publicly disclosed here**. |
| [JD JoyAI-VL-Interaction / LiveTTS](https://joymaas.jdcloud.com/models) | First-party multimodal interaction and streaming speech endpoints illustrate different execution and latency contracts in the same model gateway. | Endpoint inventory is not evidence of shared model architecture or internally optimized decode kernels. |
| [JD Cloud platform](https://www.jdcloud.com/) | Heterogeneous compute, GPU and enterprise model deployment product family; relevant infrastructure discovery source. | Broad vendor capability claims are not a benchmark or inspectable inference-engine mechanism. |

## Research reading angle

**MaaS at enterprise scale** brings service-level questions: dynamic provider/model routing, isolation, token-based usage and billing, fallback/error semantics, concurrency SLO, security and heterogeneous deployment. To turn this into a canonical systems paper or strong optimization entry, demand an official architecture disclosure, code, measured workload and strong baseline; **none are established by the service catalog alone**.

**Status:** first-party product documentation (**SERVICE-CONTRACT ONLY**) rather than code-level research admission. Do not claim private scheduling implementation from marketing text or recruitment descriptions.
