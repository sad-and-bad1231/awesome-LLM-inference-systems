# BentoML

[← Organizations](README.md)

Open model-serving and deployment infrastructure with a published runtime/packaging implementation. **Not primarily a new CUDA attention or token scheduler design.**

| Source | Technical relevance | Evidence boundary |
|---|---|---|
| [BentoML](https://github.com/bentoml/BentoML) | Model service APIs, deployment artifacts, scalable execution processes, request handling and orchestration across model types. | Broader AI inference framework; LLM per-token scheduler is usually supplied by integrated engines. |
| [BentoML deployment documentation](https://docs.bentoml.com/) | Packaging, autoscaling, endpoint behavior, model load and observability. | First-party docs, not evidence of a proprietary faster attention kernel. |

**Research fit:** service API → model-worker lifecycle, cold start and orchestration overhead; measure independently of the integrated model engine. No local performance replication.
