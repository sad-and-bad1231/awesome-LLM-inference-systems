# Red Hat / llm-d

Red Hat is a **founding contributor and industrial distributor** of the community-governed llm-d distributed inference stack. This profile covers inference routing and reliability, not an exclusive claim to the vLLM/SGLang engine.

[← Organizations](README.md)

## Public stack and deployment

| Source | Systems mechanism | Attribution / scope |
|---|---|---|
| [llm-d v1.0](https://llm-d.ai/blog) · [project code](https://github.com/llm-d/llm-d) (2026-10-20) | Kubernetes-native distributed inference **above model-server replicas**: prefix/cache-aware routing, P/D separation, KV offloading, wide EP, agent-session affinity, multi-tenant QoS, high-availability routers and coordinated updates. | **CNCF community project**, jointly founded by Red Hat, Google Cloud, IBM Research, CoreWeave and NVIDIA. Neither the engine nor all components are Red-Hat-owned. |
| [llm-d Router](https://github.com/llm-d/llm-d-router) | Endpoint Picker, request scoring/flow control and L7 gateway integration; chooses among running model-server pods rather than replacing their attention kernels. | Distinguish endpoint routing from within-replica token scheduling. |
| [Red Hat AI Inference](https://www.redhat.com/en/blog/red-hat-ai-inference-brings-llm-d-any-managed-kubernetes-starting-coreweave-and-microsoft-azure) (2026-05-12) | Vendor-supported packaging of vLLM-based inference with llm-d distributed orchestration for managed Kubernetes. | **Product release** with versioned support matrix; cannot assume shipped versions track upstream llm-d tip. |
| [Red Hat v1.0 release](https://www.redhat.com/en/about/press-releases/llm-d-1-advances-open-cost-efficient-ai-inference-production-scale) | Production SLO, multi-tenant fairness, zero-downtime migration and agent-aware session handling. | Performance figures come from specified author/operator deployments and should not be generalized. |

## Engineering focus

**KV locality vs queueing**, **P/D topology and transfer**, **multi-tenant fairness**, **day-2 rollouts**, **routing safety**. For baselines compare model-server-alone versus llm-d with identical checkpoint, hardware and traffic. An llm-d orchestration improvement is not kernel speedup.

**Status:** open software and official shipped product references; no independent local benchmark.
