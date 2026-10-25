# Tencent

Tencent's public LLM model releases and inference-oriented systems work. The index separates Tencent-owned projects from broader multi-company collaborations.

[← Organizations](README.md) · [← Home](../README.md)

| Public work | Inference relevance | Primary source |
|---|---|---|
| **Hunyuan-A13B** | Efficient MoE model architecture with a low active-parameter footprint; inference-related architecture, not a serving scheduler. | [Official source](https://github.com/Tencent-Hunyuan/Hunyuan-A13B) |
| **Hy3** (2026) | 295B MoE / 21B activated, GQA, expert routing and native MTP head. Public vLLM/SGLang deployment guidance informs real serving compatibility; quality ranking is not a systems measurement. | [Official repository](https://github.com/Tencent-Hunyuan/Hy3) |
| **Hy4-preview** (2026) | 770B MoE / 49B activated; **Gated DeepSeek Sparse Attention** with cross-layer **IndexCache** reuse, iHC residual branches and an MTP head. Interesting for indexer reuse, sparsity, KV layout and expert placement; **preview model**, not independent engine/kernel evidence. | [Official repository](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| **Hunyuan-Large** | Technical report and code for Tencent's large MoE model; inspect model architecture and sparse expert execution. | [Official source](https://github.com/Tencent/Hunyuan-Large) |
| **Angel** | Tencent's distributed ML systems toolkit; useful background but predominantly broader than LLM inference. | [Official source](https://github.com/Tencent/Angel) |

**Scope:** Model architectures and first-party components only. The reused DSA/IndexCache principles are attributed as such, not claimed as newly invented by Tencent; do not infer full-serving acceleration or Ascend support from model release claims.
