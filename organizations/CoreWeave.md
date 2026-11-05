# CoreWeave

An AI cloud/infrastructure provider and **founding co-contributor** to distributed inference research infrastructure. Its documented role is in serving control planes and cluster deployment—not training its own frontier model.

[← Organizations](README.md)

## Primary sources

| Source | Engineering focus | Evidence boundary |
|---|---|---|
| [CoreWeave on llm-d and CNCF](https://www.coreweave.com/blog/the-next-chapter-for-ai-infrastructure-why-llm-ds-move-to-cncf-matters) (2026-03-24) | CoreWeave explicitly identifies itself as a founding contributor with Red Hat, IBM, Google and NVIDIA. Focus: distributed, interoperable production inference and cloud-native orchestration. | **Multi-organization community code**, not a privately owned CoreWeave engine or a product-specific speedup. |
| [llm-d source](https://github.com/llm-d/llm-d) | Prefix-aware request routing, P/D allocation, KV offloading, wide-EP and production SLO control across accelerator fleets. | These are **joint project capabilities**; do not attribute every commit to CoreWeave. |
| [Red Hat × CoreWeave validated deployment blueprint](https://www.redhat.com/en/blog/red-hat-ai-inference-brings-llm-d-any-managed-kubernetes-starting-coreweave-and-microsoft-azure) | Managed-Kubernetes llm-d deployment and operational recipe on CoreWeave Kubernetes Service. | Partnership/product packaging, not evidence of a new scheduling algorithm unless a separately audited design is published. |

## Research reading angle

This profile emphasizes **infrastructure repeatability, routing, accelerated networking, and the distinction between an engine's per-replica throughput and a cluster's production Goodput**. The public source set is narrower than the underlying cloud capability.

**Status:** official company/community sources. No independent performance receipt and no exclusive ownership claim.
