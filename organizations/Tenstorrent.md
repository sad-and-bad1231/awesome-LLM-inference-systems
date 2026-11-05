# Tenstorrent

[← Organizations](README.md)

An accelerator vendor with a substantial open **programming model, kernel/runtime stack and multi-chip LLM execution documentation**; useful as a non-CUDA architectural comparison.

| Source | Implementation scope | Critical limitation |
|---|---|---|
| [TT-Metal / TT-NN](https://github.com/tenstorrent/tt-metal) | Low-level TT-Metalium kernels, TT-NN tensor operations, multi-chip device programming and model integration. | Specific Tenstorrent chip generation and firmware determine supported kernel paths. |
| [LLM bring-up technical guide](https://github.com/tenstorrent/tt-metal/blob/main/tech_reports/LLMs/llms.md) | Prefill versus decode, multi-chip mapping, memory layout and transformer-specific engineering pitfalls. | An engineering guide, not an independently controlled LLM serving speedup. |
| [TT-LLK archive/migration](https://github.com/tenstorrent/tt-llk) | Previous low-level-kernel repo, now **frozen**, moved to `tt-metal/tt_metal/tt-llk`. | Do **not** recommend the old TT-LLK repository as the active development branch. |

**Research fit:** compute tile orchestration, hierarchical memory and communication, deterministic profiling and mapping; vendor and GPU/NPU performance cannot be compared without matching model/quality/budget.
