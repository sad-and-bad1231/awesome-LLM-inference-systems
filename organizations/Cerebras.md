# Cerebras

First-party **wafer-scale inference hardware and systems execution** signals. Models provided as hosted endpoints are not necessarily Cerebras-designed or trained.

[← Organizations](README.md)

## Hardware–runtime co-design

| Work | System relevance | Evidence boundary |
|---|---|---|
| **[CS-4 / Nexus](https://www.cerebras.ai/blog/introducing-cerebras-cs-4)** (2026-08-18) | Fourth-generation wafer-scale inference system combining three wafer-scale engines with a redesigned rack/power/cooling/I/O architecture; targets interactive token generation at scale. | Product architecture and **vendor-reported performance**, not independent apples-to-apples comparison against GPU servers. Claimed maximum speedups are conditional on models, precision and deployment. |
| **[Hot Chips 2026 technical overview](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026)** | Public discussion of CS-4 packaging, system architecture, inference scalability and a forward roadmap. | **Engineering conference presentation**, not evidence that every projected future generation is shipping. |
| **[Disaggregated inference](https://www.cerebras.ai/blog)** (2026-10-01 article in official blog index) | Follow the role of cross-device placement and system-level resource mapping in wafer-scale inference. | Discovery pointer; verify the detailed implementation and baseline before making a specific architectural or acceleration claim. |

## Why it belongs here

Cerebras addresses the **device-memory-communication topology** of inference through purpose-built hardware. It is a distinct systems dimension from generic LLM APIs and from agent-assisted software optimization. Compare real workloads and latency/throughput/cost jointly; do not present operator-level or vendor-selected token-rate claims as universal goodput improvements.

**Status:** company-owned hardware and first-party architectural disclosures; no independent local reproduction.
