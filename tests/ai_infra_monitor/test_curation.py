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
    def test_v6_classifies_each_guide_theme_from_structured_signals(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import classify_record

        cases = {
            "FlashAttention-4 Attention Kernel": "attention-kernel",
            "Paged KV Cache Compression for LLM Inference": "kv-cache",
            "Disaggregated Prefill Decode KV Transfer": "prefill-decode-transfer",
            "Fused Speculative Decoding Draft Verify": "speculative-decoding",
            "Expert Routing for MoE Inference": "moe",
            "Wave DSL Compiler for LLM Kernels": "compiler-dsl",
            "Continuous Batching Scheduler for LLM Serving": "runtime-scheduling",
        }
        for title, expected in cases.items():
            with self.subTest(title=title):
                result = classify_record(_record(title=title))
                self.assertEqual(result["version"], "guide-2026-v6")
                self.assertIn(expected, result["themes"])
                self.assertEqual(result["scope"], "core")

    def test_release_html_does_not_create_mainline_signal(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import classify_record

        result = classify_record(
            _record(
                record_type="project",
                title="v1.92.0",
                venue_or_channel="Official releases",
                summary="<h2>LLM inference</h2>" + " kernel serving compiler" * 1000,
                technical_tags={key: [] for key in _record()["technical_tags"]},
                evidence={
                    "venue_status": "industrial_material",
                    "source_type": "project_or_engineering_material",
                    "verification_level": "verified",
                    "verified_at": "2026-07-01",
                },
            )
        )

        self.assertNotEqual(result["scope"], "core")
        self.assertEqual(result["themes"], [])

    def test_broad_batch_tags_do_not_promote_generic_dnn_inference(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import classify_record

        result = classify_record(
            _record(
                title="Coordinated Resource Management for Energy-Efficient DNN Inference on Edge Devices",
                venue_or_channel="Euro-Par 2026",
                technical_tags={
                    "phase": ["serving"],
                    "hardware": [],
                    "optimization_layer": ["compiler", "compression", "kernel", "moe"],
                    "workload": ["agent", "edge", "moe", "multimodal", "rag"],
                    "framework_binding": [],
                    "metrics": [],
                },
                evidence={
                    "venue_status": "formal_conference",
                    "source_type": "conference_program",
                    "verification_level": "verified",
                    "verified_at": "2026-06-01",
                },
            )
        )

        self.assertNotEqual(result["scope"], "core")
        self.assertEqual(result["themes"], [])

    def test_evidenced_comic_generation_inference_is_exploration(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import classify_record

        result = classify_record(
            _record(
                title="Context-Aware Comic Generation Inference Enhancement",
                venue_or_channel="ACM Multimedia 2026",
                technical_tags={
                    "phase": ["inference"],
                    "hardware": ["gpu"],
                    "optimization_layer": ["pipeline"],
                    "workload": ["multimodal", "comic-generation"],
                    "framework_binding": [],
                    "metrics": ["latency"],
                },
                evidence={
                    "venue_status": "formal_conference",
                    "source_type": "conference_program",
                    "verification_level": "verified",
                    "verified_at": "2026-06-10",
                },
            )
        )

        self.assertEqual(result["scope"], "adjacent")
        self.assertEqual(result["themes"], [])

    def test_exploration_selection_is_windowed_capped_and_deterministic(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.curation import select_exploration

        records = []
        for index in range(25):
            record = _record(
                title=f"Multimodal Comic Inference Study {index:02d}",
                venue_or_channel="ACM Multimedia 2026",
                technical_tags={
                    "phase": ["inference"],
                    "hardware": ["gpu"],
                    "optimization_layer": ["pipeline"],
                    "workload": ["multimodal"],
                    "framework_binding": [],
                    "metrics": ["latency"],
                },
                evidence={
                    "venue_status": "formal_conference",
                    "source_type": "conference_program",
                    "verification_level": "verified",
                    "verified_at": f"2026-06-{(index % 20) + 1:02d}",
                },
            )
            records.append(record)
        records.append(
            _record(
                title="Old Multimodal Inference Study",
                technical_tags={
                    "phase": ["inference"], "hardware": ["gpu"],
                    "optimization_layer": ["pipeline"], "workload": ["multimodal"],
                    "framework_binding": [], "metrics": ["latency"],
                },
                evidence={
                    "venue_status": "formal_conference",
                    "source_type": "conference_program",
                    "verification_level": "verified",
                    "verified_at": "2025-01-01",
                },
            )
        )

        first = select_exploration(records, window_days=180, limit=20)
        second = select_exploration(list(reversed(records)), window_days=180, limit=20)
        self.assertEqual(len(first), 20)
        self.assertEqual([item["title"] for item in first], [item["title"] for item in second])
        self.assertNotIn("Old Multimodal Inference Study", {item["title"] for item in first})

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
