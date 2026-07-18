import unittest


def _record(**overrides):
    record = {
        "record_type": "paper",
        "title": "Example LLM serving system",
        "summary": "A real GPU evaluation for inference serving.",
        "year": "2026",
        "venue_or_channel": "MLSys 2026",
        "source_tier": "A",
        "artifact_url": "",
        "system_abstraction_primary": "Program-Aware Scheduling",
        "technical_tags": {
            "phase": ["serving"],
            "hardware": ["gpu"],
            "optimization_layer": ["scheduler"],
            "workload": ["llm-inference"],
            "framework_binding": [],
            "metrics": ["latency"],
        },
        "triage": {
            "priority": "high",
            "physical_eval": {"has_physical_signal": True},
        },
    }
    record.update(overrides)
    return record


class CurationTests(unittest.TestCase):
    def test_guide_peripheral_record_is_archived(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import classify_record

        result = classify_record(
            _record(
                title="A Generic Vector Database for RAG Retrieval",
                summary="A database benchmark with no inference runtime or kernel path.",
                venue_or_channel="Systems Workshop 2026",
                technical_tags={
                    "phase": [],
                    "hardware": [],
                    "optimization_layer": [],
                    "workload": ["rag"],
                    "framework_binding": [],
                    "metrics": ["throughput"],
                },
                triage={"priority": "normal", "physical_eval": {}},
            )
        )

        self.assertEqual(result["scope"], "archive")
        self.assertEqual(result["priority"], "supporting")

    def test_foundational_kernel_record_precedes_frontier_work(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import (
            classify_record,
            curation_sort_key,
        )

        foundation = _record(
            title="FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness",
            summary="An IO-aware attention kernel that reduces HBM traffic.",
            year="2022",
            venue_or_channel="NeurIPS 2022",
            source_tier="legacy",
            triage={"priority": "normal", "physical_eval": {"has_physical_signal": True}},
        )
        frontier = _record(
            title="FlashAttention-4: Algorithm and Kernel Pipelining Co-Design",
            summary="A new GPU pipeline for long-sequence attention serving.",
            year="2026",
            venue_or_channel="MLSys 2026",
        )

        foundation["curation"] = classify_record(foundation)
        frontier["curation"] = classify_record(frontier)
        self.assertEqual(foundation["curation"]["priority"], "foundation")
        self.assertEqual(frontier["curation"]["priority"], "frontier")
        self.assertLess(curation_sort_key(foundation), curation_sort_key(frontier))

    def test_current_innovation_requires_mainline_and_system_evidence(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import classify_record

        result = classify_record(
            _record(
                title="Adaptive Fused Kernel for Prefill Decode and KV Transfer",
                summary="A CUDA LLM serving runtime evaluated on H100 with end-to-end TTFT and TPOT.",
                technical_tags={
                    "phase": ["prefill", "decode", "serving"],
                    "hardware": ["cuda", "hopper"],
                    "optimization_layer": ["kernel", "kv-cache"],
                    "workload": ["long-context"],
                    "framework_binding": ["vllm"],
                    "metrics": ["ttft", "tpot", "throughput"],
                },
            )
        )

        self.assertEqual(result["scope"], "core")
        self.assertEqual(result["priority"], "frontier")

    def test_curation_sort_key_puts_archived_scope_last(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import (
            classify_record,
            curation_sort_key,
        )

        core = _record()
        archive = _record(
            title="Non-LLM Hardware Benchmark",
            summary="A benchmark without an inference or serving path.",
            technical_tags={
                "phase": [],
                "hardware": ["gpu"],
                "optimization_layer": [],
                "workload": [],
                "framework_binding": [],
                "metrics": ["throughput"],
            },
            triage={"priority": "low", "physical_eval": {}},
        )
        core["curation"] = classify_record(core)
        archive["curation"] = classify_record(archive)

        self.assertLess(curation_sort_key(core), curation_sort_key(archive))


if __name__ == "__main__":
    unittest.main()
