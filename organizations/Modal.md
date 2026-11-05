# Modal

A first-party **inference implementation and deployment systems** signal. Unlike a pure model API catalog, Modal publishes detailed engineering work on existing engines and kernels.

[← Organizations](README.md)

## Public technical sources

| Work | Inference mechanism | Evidence boundary |
|---|---|---|
| **[Making FlashAttention-4 faster for inference](https://modal.com/blog/flash-attention-4-faster)** (2026-06-11) | Decode-oriented, variable-sequence GPU attention optimizations and contributions building on the FlashAttention-4 implementation; useful for understanding kernel composition with serving. | **Engineering analysis/implementation contribution**; measured kernel behavior should not be silently promoted to universal end-to-end serving goodput. Credit core FlashAttention authors separately. |
| **[Achieve state-of-the-art inference latencies with speculative decoding](https://modal.com/blog/achieve-sota-specdec)** (2026-06-24) | Practical speculative decoding choices on Blackwell, SGLang runtime and low-overhead deployment for latency-oriented endpoints. | Vendor-reported end-to-end claims depend on model, hardware and prompt/response distribution; comparison baseline must be read in article. |
| **[Modal inference platform](https://modal.com/products/inference)** | Managed endpoints and low-level deploy/scale primitives, including asynchronous jobs. | Service feature documentation is **not** a disclosure of all underlying scheduler or kernel code. |

## Reading angle

Important at the **kernel → engine → deployment** boundary: small isolated kernel gains may not survive engine composition, while speculation and request shape often dominate observed interactive latency. Require correctness against reference outputs, matched workloads and P95 TTFT/TPOT versus serving throughput.

**Status:** first-party engineering blog and public product interface; not a distinct canonical paper count.
