# AI Infra Candidate Pool

This is the working queue. Daily automation should add candidates here first.
Main documents should change only after a small manual or weekly confirmation pass.

Status values:

- `new`: not reviewed.
- `keep`: worth tracking, but not ready for the main documents.
- `promote`: verified and ready for a small main-document update.
- `drop`: off-topic, duplicate, weak source, or too speculative.

## Current Keep Rationale（2026-06-27）

The queue is intentionally small after the weekly-quality pass. These entries are still worth watching, but the current public source does not yet justify moving them into the main index.

| Title | Keep reason | Next check |
|---|---|---|
| Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications | Enterprise multi-agent deployment is relevant, but the systems mechanism is still too application/framework-level for the main LLM inference index. | Re-check for a concrete runtime, scheduling, or state-management artifact. |
| Variable-Width Transformers | Potential inference efficiency implications, but it is primarily a model-architecture direction until systems evaluation is clearer. | Re-check for serving/runtime benchmarks or adoption by an inference engine. |
| CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference | KV compression is on-topic, but the arXiv page currently carries an admin note about text overlap, so promotion should wait. | Re-check arXiv status or an independent venue/source before promotion. |

## Daily Notes（2026-07-06, run 20260706T005509666159Z）

- `new`, likely P1: `Lynx` is a concrete disaggregated long-context serving mechanism centered on progressive KV transfer and speculative decode overlap.
- `new`, likely P1: `Moebius` is a strong MoE serving systems paper with runtime TP/EP switching and concrete H200 evaluation.
- `new`, likely P1: `MosaicKV` is a direct long-context inference systems contribution with two-dimensional KV compression and serving benchmarks.
- `new`, likely P1: `Omni-Flow` is a useful multimodal inference orchestration and distributed KV sharing system, though it is broader than text-only LLM serving.
- `new`, likely P2: `MxGLUT` is relevant as inference hardware support, but it is accelerator-centric rather than a serving/runtime system.
- `new`, likely P2: `OmniPilot` is useful cluster-level inference configuration work, but closer to advisor/evaluation infrastructure than core serving runtime.

| Discovered | Tier | Kind | Source | Title | Topics | URL | Status |
|---|---|---|---|---|---|---|---|
| 2026-06-18 | A | paper | arXiv AI infrastructure query | Towards Scalable Customization and Deployment of Multi-Agent Systems for Enterprise Applications | compression-cost, agent-rag | [primary](https://arxiv.org/abs/2606.18502v1) | keep |
| 2026-06-18 | A | paper | arXiv AI infrastructure query | Variable-Width Transformers | runtime-serving, state-kv, agent-rag | [primary](https://arxiv.org/abs/2606.18246v1) | keep |
| 2026-06-24 | A | paper | arXiv AI infrastructure query | CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference | state-kv, compression-cost, kernel-compiler, agent-rag | [primary](https://arxiv.org/abs/2606.24467v1) | keep |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | 3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving | runtime-serving, state-kv, network-disaggregation | [primary](https://arxiv.org/abs/2607.01617v1) | promote |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | BaseRT: Best-in-Class LLM Inference on Apple Silicon via Native Metal | runtime-serving, kernel-compiler, moe | [primary](https://arxiv.org/abs/2607.00501v1) | promote |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference | kernel-compiler, reliability-evaluation | [primary](https://arxiv.org/abs/2606.31903v1) | keep |
| 2026-07-04 | A | paper | arXiv AI infrastructure query | BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding | runtime-serving, hardware-edge | [primary](https://arxiv.org/abs/2606.31315v1) | drop |
| 2026-07-04 | B | paper | MLSys 2026 official papers page | Learning from Less: Measuring the Effectiveness of RLVR in Low Data and Compute Regimes | reliability-evaluation, training-systems | [primary](https://mlsys.org/virtual/2026/papers.html) | keep |
| 2026-07-04 | B | paper | MLSys 2026 official papers page | CAGE: Curvature-Aware Gradient Estimation For Accurate Quantization-Aware Training | compression-cost, training-systems | [primary](https://mlsys.org/virtual/2026/papers.html) | keep |
| 2026-07-04 | B | paper | MLSys 2026 official papers page | REPARO: LOSS-RESILIENT GENERATIVE CODEC FOR VIDEO CONFERENCING | multimodal-diffusion, reliability-evaluation | [primary](https://mlsys.org/virtual/2026/papers.html) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | CSD: Content-aware Speculative Decoding for Efficient Image Generation | kernel-compiler, agent-rag | [primary](https://arxiv.org/abs/2606.27829v1) | drop |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Cache Merging as a Convergent Replicated State for Multi-Agent Latent Reasoning | runtime-serving, kernel-compiler, agent-rag, hardware-edge, reliability-evaluation | [primary](https://arxiv.org/abs/2607.01308v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Can LLMs Rank? A Tale of Triads and Triage | reliability-evaluation | [primary](https://arxiv.org/abs/2606.30412v1) | drop |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Cascaded Multi-Granularity Pruning for On-Device LLM Inference in Industrial IoT | compression-cost, kernel-compiler, hardware-edge | [primary](https://arxiv.org/abs/2606.26861v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving | runtime-serving, kernel-compiler | [primary](https://arxiv.org/abs/2606.27457v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Coverage-Driven KV Cache Eviction for Efficient and Improved Inference of LLM | state-kv, kernel-compiler, agent-rag, hardware-edge | [primary](https://arxiv.org/abs/2606.29563v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Cross-lingual Relation Extraction with Large Language Models: Zero-Shot, Few-Shot, and Fine-Tuned Evaluation on Romanian | kernel-compiler, reliability-evaluation | [primary](https://arxiv.org/abs/2606.31718v1) | drop |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving | runtime-serving, compression-cost | [primary](https://arxiv.org/abs/2606.29708v2) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | DiLaServe: High SLO Attainment Serving for Diffusion Language Models | reliability-evaluation | [primary](https://arxiv.org/abs/2606.29094v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation | hardware-edge | [primary](https://arxiv.org/abs/2607.01208v1) | drop |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving | runtime-serving, state-kv, kernel-compiler, network-disaggregation, moe | [primary](https://arxiv.org/abs/2607.00466v2) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | EcoTable: Cost-effective Table Integration in Data Lakes for Natural Language Queries | agent-rag, reliability-evaluation | [primary](https://arxiv.org/abs/2606.26613v1) | drop |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference | hardware-edge | [primary](https://arxiv.org/abs/2606.27743v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs | runtime-serving, reliability-evaluation | [primary](https://arxiv.org/abs/2606.30391v1) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction | runtime-serving, kernel-compiler, reliability-evaluation | [primary](https://arxiv.org/abs/2606.27550v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | GSRQ: Gain-Shape Residual Quantization for Sub-1-bit KV Cache | state-kv, compression-cost, agent-rag | [primary](https://arxiv.org/abs/2607.01065v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression | runtime-serving, compression-cost, kernel-compiler, agent-rag, reliability-evaluation | [primary](https://arxiv.org/abs/2606.28831v1) | keep |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators | runtime-serving, state-kv, compression-cost, network-disaggregation, reliability-evaluation | [primary](https://arxiv.org/abs/2606.29986v1) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching | runtime-serving, state-kv, kernel-compiler, agent-rag | [primary](https://arxiv.org/abs/2607.01299v1) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | HyperDFlash: Hyper-Connection-Aligned Block Speculative Decoding with Gated Residual Reduction | agent-rag, hardware-edge, reliability-evaluation | [primary](https://arxiv.org/abs/2606.26744v2) | drop |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Information-Aware KV Cache Compression for Long Reasoning | runtime-serving, state-kv, compression-cost, kernel-compiler, reliability-evaluation | [primary](https://arxiv.org/abs/2606.26875v1) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding | runtime-serving, kernel-compiler, agent-rag | [primary](https://arxiv.org/abs/2606.29207v1) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | KernelSight-LM: A Kernel-Level LLM Inference Simulator | runtime-serving, kernel-compiler, reliability-evaluation | [primary](https://arxiv.org/abs/2606.28565v2) | promote |
| 2026-07-05 | A | paper | arXiv AI infrastructure query | Labeling Training Data for Entity Matching Using Large Language Models | reliability-evaluation | [primary](https://arxiv.org/abs/2606.28823v1) | drop |
| 2026-07-06 | A | paper | arXiv AI infrastructure query | Lynx: Progressive Speculative Quantization for accelerating KV Transfer in Long-Context Inference | state-kv, compression-cost, kernel-compiler, network-disaggregation, agent-rag | [primary](https://arxiv.org/abs/2607.01831v1) | new |
| 2026-07-06 | A | paper | arXiv AI infrastructure query | Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch | runtime-serving, state-kv, kernel-compiler, moe, agent-rag | [primary](https://arxiv.org/abs/2606.26607v1) | new |
| 2026-07-06 | A | paper | arXiv AI infrastructure query | MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression | runtime-serving, state-kv, compression-cost, kernel-compiler, agent-rag | [primary](https://arxiv.org/abs/2607.00760v1) | new |
| 2026-07-06 | A | paper | arXiv AI infrastructure query | MxGLUT: A Reconfigurable LUT-Centric Broadcast Dataflow Accelerator for Mixed-Precision GEMM | runtime-serving, compression-cost, kernel-compiler | [primary](https://arxiv.org/abs/2607.01607v1) | new |
| 2026-07-06 | A | paper | arXiv AI infrastructure query | Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference | runtime-serving, state-kv, agent-rag | [primary](https://arxiv.org/abs/2606.31093v1) | new |
| 2026-07-06 | A | paper | arXiv AI infrastructure query | OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters | compression-cost, reliability-evaluation | [primary](https://arxiv.org/abs/2607.01579v1) | new |
