# BentoML

[← Organizations](README.md)

Open model-serving and deployment infrastructure with a published runtime/packaging implementation. **Not primarily a new CUDA attention or token scheduler design.**

| Source | Technical relevance | Evidence boundary |
|---|---|---|
| [BentoML](https://github.com/bentoml/BentoML) | Model service APIs, deployment artifacts, scalable execution processes, request handling and orchestration across model types. | Broader AI inference framework; LLM per-token scheduler is usually supplied by integrated engines. |
| [BentoML deployment documentation](https://docs.bentoml.com/) | Packaging, autoscaling, endpoint behavior, model load and observability. | First-party docs, not evidence of a proprietary faster attention kernel. |

## LLM-specific execution interface (first-party code and docs)

The [official vLLM deployment example](https://docs.bentoml.org/en/latest/examples/vllm.html) wraps the **existing vLLM engine** in a BentoML Service; it does *not* replace vLLM's Paged KV manager, speculative decoding kernels or per-token scheduler.

| Layer / source | What is actually implemented or controlled | Measure / do not infer |
|---|---|---|
| [BentoVLLM examples](https://github.com/bentoml/BentoVLLM) | Model reference, GPU/TP resource declaration, container runtime, launch of `vllm serve` and OpenAI-compatible endpoint | P/D and KV semantics are inherited from selected vLLM/version/backend |
| [Service workers and request concurrency](https://docs.bentoml.org/en/latest/build-with-bentoml/parallelize-requests.html) | Multi-process Service workers, traffic concurrency limits and endpoint execution orchestration | Worker count ≠ vLLM internal batch size or engine throughput |
| [Model packaging and lifecycle](https://docs.bentoml.org/en/latest/examples/vllm.html) | Service image, dependency pins, model handling and deployment resource configuration | Cold-start and model-load latency are separate from steady-state TPOT |
| [BentoCloud deployment scaling](https://docs.bentoml.org/en/bentocloud/examples/vllm.html) | Replica min/max scaling and resource quotas; deployment interface may require the hosted BentoCloud product | Product-level scale-up is **not** proof that a single GPU decodes faster |

**Engineering question:** what part of TTFT is API/process/queue/model loading versus core Engine Prefill? Compare fixed engine commit, weights, GPU, max concurrency and request trace before and after changing deployment controls. Inspect autoscaling under churn and record P95 cold-start, model-load-to-ready, queueing, streaming overhead and runtime GPU utilization.

**Research fit:** service API → model-worker lifecycle, cold start and orchestration overhead; measure independently of the integrated model engine. No local performance replication.
