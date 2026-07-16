import errno
import tempfile
import unittest
from pathlib import Path
from threading import Lock
from time import sleep
from unittest.mock import patch

from scripts.ai_infra_monitor.ai_infra_monitor.records import (
    candidate_to_record,
    compact_candidate_records,
    load_records,
    migrate_jsonl_to_split_stores,
    normalize_record,
    render_markdown_views,
    validate_record_stores,
    validate_record_store,
    write_records,
)
from scripts.ai_infra_monitor.ai_infra_monitor.triage import (
    triage_candidate,
    triage_candidates,
)
from scripts.ai_infra_monitor.ai_infra_monitor.models import Candidate


class RecordStoreTests(unittest.TestCase):
    def test_write_records_retries_transient_windows_file_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "records.jsonl"
            original = Path.write_text
            calls = []

            def flaky_write(*args, **kwargs):
                calls.append(path)
                if len(calls) < 3:
                    raise OSError(errno.EINVAL, "transient file lock")
                return original(path, *args, **kwargs)

            with patch.object(Path, "write_text", side_effect=flaky_write):
                write_records(path, [{"id": "one", "title": "One"}])

            self.assertEqual(len(calls), 3)
            self.assertIn('"id": "one"', path.read_text(encoding="utf-8"))

    def test_splits_existing_store_and_merges_known_title_aliases(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "infra-db.jsonl"
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            candidates = root / "data" / "candidates.jsonl"
            source.write_text(
                "\n".join(
                    [
                        '{"record_type":"paper","title":"Prism: Unleashing GPU Sharing for Cost-Efficient Multi-LLM Serving","venue_or_channel":"OSDI 2026","year":"2026","orgs":"UCLA","summary":"GPU memory ballooning for serving.","source_tier":"legacy","primary_url":"","artifact_url":"","source_ids":[],"status":"verified_legacy","system_abstraction_primary":"Memory Topology & Virtualization","system_abstraction_secondary":[],"technical_tags":{"phase":["serving"],"hardware":["gpu"],"optimization_layer":["memory"],"workload":[],"framework_binding":[],"metrics":[]},"triage":{"verdict":"keep","priority":"normal","reasons":[],"repo_signals":{},"physical_eval":{}}}',
                        '{"record_type":"paper","title":"Chimera: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning","venue_or_channel":"OSDI 2026","year":"2026","orgs":"UCLA","summary":"GPU memory ballooning for serving.","source_tier":"legacy","primary_url":"","artifact_url":"","source_ids":[],"status":"verified_legacy","system_abstraction_primary":"Memory Topology & Virtualization","system_abstraction_secondary":[],"technical_tags":{"phase":["serving"],"hardware":["gpu"],"optimization_layer":["memory"],"workload":[],"framework_binding":[],"metrics":[]},"triage":{"verdict":"keep","priority":"normal","reasons":[],"repo_signals":{},"physical_eval":{}}}',
                        '{"record_type":"industry","title":"AITER","venue_or_channel":"ROCm","year":"2026","orgs":"AMD","summary":"ROCm kernels for vLLM.","source_tier":"A","primary_url":"https://github.com/ROCm/AITER","artifact_url":"https://github.com/ROCm/AITER","source_ids":[],"status":"verified","system_abstraction_primary":"Execution Compilation & Kernel Fusion","system_abstraction_secondary":[],"technical_tags":{"phase":["serving"],"hardware":["rocm"],"optimization_layer":["kernel"],"workload":[],"framework_binding":["vllm"],"metrics":[]},"triage":{"verdict":"keep","priority":"high","reasons":[],"repo_signals":{},"physical_eval":{}}}',
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            counts = migrate_jsonl_to_split_stores(source, papers, industry, candidates)
            self.assertEqual(counts, {"papers": 1, "industry": 1, "candidates": 0})
            records = load_records(papers)
            self.assertEqual(records[0]["title"], "Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning")
            self.assertIn("Prism: Unleashing GPU Sharing for Cost-Efficient Multi-LLM Serving", records[0]["aliases"])
            self.assertIn("canonical_id", records[0])
            self.assertIn("evidence", records[0])
            self.assertFalse(validate_record_stores(papers, industry, candidates))

            paper_view = root / "paper-list.md"
            industry_view = root / "industrial.md"
            candidate_view = root / "candidates.md"
            render_markdown_views(papers, industry, candidates, paper_view, industry_view, candidate_view, root / "abstractions.md")
            self.assertIn("generated from data/papers.jsonl", paper_view.read_text(encoding="utf-8"))
            self.assertIn("AITER", industry_view.read_text(encoding="utf-8"))
            abstraction_text = (root / "abstractions.md").read_text(encoding="utf-8")
            self.assertIn("Memory Topology & Virtualization", abstraction_text)
            self.assertIn("Reading Entry Points", abstraction_text)
            self.assertIn("Representative Items", abstraction_text)
            self.assertNotIn("| Title | Type | Channel | Summary | Technical Tags |", abstraction_text)

    def test_promotion_routes_papers_and_industry_to_different_stores(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.records import promote_candidates

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "papers.jsonl"
            industry = root / "industry.jsonl"
            candidates = [
                Candidate(title="Serving Paper", url="https://arxiv.org/abs/2607.00001", kind="paper"),
                Candidate(title="Serving Runtime", url="https://github.com/example/runtime", kind="project"),
            ]
            self.assertEqual(promote_candidates(papers, industry, candidates), {"papers": 1, "industry": 1})
            self.assertEqual(load_records(papers)[0]["record_type"], "paper")
            self.assertEqual(load_records(industry)[0]["record_type"], "project")

    def test_promotion_merges_official_evidence_into_legacy_record(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.records import promote_candidates

        with tempfile.TemporaryDirectory() as tmp:
            papers = Path(tmp) / "papers.jsonl"
            industry = Path(tmp) / "industry.jsonl"
            legacy = candidate_to_record(
                Candidate(title="FastServe", url="", summary="Legacy summary"),
                "paper",
                "verified_legacy",
            )
            write_records(papers, [legacy])
            incoming = Candidate(
                title="FastServe",
                url="https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang",
                source_id="usenix-nsdi26-spring-accepted",
                source_name="USENIX NSDI 2026 spring accepted papers",
                tier="A",
                summary="Official abstract with vLLM baseline and GPU evaluation.",
                topics=("runtime-serving",),
            )

            self.assertEqual(promote_candidates(papers, industry, [incoming]), {"papers": 0, "industry": 0})
            merged = load_records(papers)[0]
            self.assertEqual(merged["primary_url"], incoming.url)
            self.assertIn("usenix-nsdi26-spring-accepted", merged["source_ids"])
            self.assertEqual(merged["summary"], incoming.summary)
        self.assertEqual(merged["evidence"]["verification_level"], "official_source")

    def test_promotion_merges_known_title_aliases(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.records import promote_candidates

        with tempfile.TemporaryDirectory() as tmp:
            papers = Path(tmp) / "papers.jsonl"
            industry = Path(tmp) / "industry.jsonl"
            legacy = candidate_to_record(
                Candidate(
                    title="Cascadia: A Cascade Serving System for Large Language Models",
                    url="",
                    summary="Legacy Cascadia summary",
                ),
                "paper",
                "verified_legacy",
            )
            write_records(papers, [legacy])
            incoming = Candidate(
                title="Cascadia: An Efficient Cascade Serving System for Large Language Models",
                url="https://iclr.cc/virtual/2026/poster/10006705",
                source_id="iclr26-virtual",
                source_name="ICLR 2026 official virtual papers",
                tier="A",
                summary="Official ICLR abstract for Cascadia.",
                topics=("runtime-serving",),
            )

            self.assertEqual(promote_candidates(papers, industry, [incoming]), {"papers": 0, "industry": 0})
            merged = load_records(papers)
            self.assertEqual(len(merged), 1)
            self.assertEqual(merged[0]["title"], incoming.title)
            self.assertIn("iclr26-virtual", merged[0]["source_ids"])
            self.assertIn("Cascadia: A Cascade Serving System for Large Language Models", merged[0]["aliases"])

    def test_known_osdi_title_aliases_share_canonical_ids(self):
        old_opentela = normalize_record(
            candidate_to_record(Candidate(title="OpenTela", url=""), "paper", "verified_legacy")
        )
        new_opentela = normalize_record(
            candidate_to_record(
                Candidate(
                    title="OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving",
                    url="https://example.org/opentela",
                ),
                "paper",
                "queued",
            )
        )
        self.assertEqual(old_opentela["canonical_id"], "paper:osdi-2026-opentela")
        self.assertEqual(old_opentela["canonical_id"], new_opentela["canonical_id"])

    def test_official_venue_replaces_stale_preprint_evidence(self):
        record = candidate_to_record(
            Candidate(
                title="Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning",
                url="https://www.usenix.org/conference/osdi26/presentation/yu-shan",
                source_id="osdi26-usenix",
                tier="A",
                venue="OSDI 2026",
            ),
            "paper",
            "verified_legacy",
        )
        record["evidence"] = {
            "source_type": "arxiv",
            "venue_status": "preprint",
            "verification_level": "official_source",
            "verified_at": "",
        }

        normalized = normalize_record(record)

        self.assertEqual(normalized["evidence"]["source_type"], "conference_program")
        self.assertEqual(normalized["evidence"]["venue_status"], "formal_conference")

    def test_compact_candidate_records_marks_non_actionable_items_as_drop(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "candidates.jsonl"
            records = [
                candidate_to_record(
                    Candidate(
                        title="Keep Candidate",
                        url="https://example.org/keep",
                        triage={
                            "verdict": "keep",
                            "priority": "normal",
                            "reasons": [],
                            "repo_signals": {},
                            "physical_eval": {},
                        },
                    )
                ),
                candidate_to_record(
                    Candidate(
                        title="Noise Candidate",
                        url="https://example.org/noise",
                        triage={
                            "verdict": "downrank",
                            "priority": "low",
                            "reasons": [],
                            "repo_signals": {},
                            "physical_eval": {},
                        },
                    )
                ),
            ]
            write_records(path, records)

            self.assertEqual(compact_candidate_records(path), 1)
            compacted = load_records(path)
            self.assertEqual(compacted[0]["status"], "new")
            self.assertEqual(compacted[1]["status"], "drop")

    def test_render_candidate_view_excludes_promoted_records_from_active_table(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = candidate_to_record(
                Candidate(
                    title="Promoted Candidate",
                    url="https://example.org/promoted",
                    triage={
                        "verdict": "keep",
                        "priority": "normal",
                        "reasons": [],
                        "repo_signals": {},
                        "physical_eval": {},
                    },
                ),
                status="promote",
            )
            candidates = root / "candidates.jsonl"
            write_records(candidates, [candidate])
            candidate_view = root / "candidates.md"

            render_markdown_views(
                root / "papers.jsonl",
                root / "industry.jsonl",
                candidates,
                root / "papers.md",
                root / "industry.md",
                candidate_view,
                root / "abstractions.md",
            )

            text = candidate_view.read_text(encoding="utf-8")
            self.assertIn("Active candidates: 0.", text)
            self.assertIn("Promoted Candidate", text)

    def test_validation_rejects_duplicate_titles_and_new_record_without_url(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "infra-db.jsonl"
            db.parent.mkdir(parents=True, exist_ok=True)
            db.write_text(
                '{"id":"one","record_type":"candidate","title":"Same","venue_or_channel":"arXiv","year":"2026","orgs":"","summary":"x","source_tier":"A","primary_url":"https://example.org/one","artifact_url":"","source_ids":[],"status":"new","system_abstraction_primary":"Execution Compilation & Kernel Fusion","system_abstraction_secondary":[],"technical_tags":{"phase":[],"hardware":[],"optimization_layer":[],"workload":[],"framework_binding":[],"metrics":[]},"triage":{"verdict":"keep","priority":"normal","reasons":[],"repo_signals":{},"physical_eval":{},"llm_review":{}},"presentation":{"featured":"yes","order":-1}}\n'
                '{"id":"two","record_type":"candidate","title":"Same","venue_or_channel":"arXiv","year":"2026","orgs":"","summary":"x","source_tier":"A","primary_url":"","artifact_url":"","source_ids":[],"status":"new","system_abstraction_primary":"Execution Compilation & Kernel Fusion","system_abstraction_secondary":[],"technical_tags":{"phase":[],"hardware":[],"optimization_layer":[],"workload":[],"framework_binding":[],"metrics":[]},"triage":{"verdict":"keep","priority":"normal","reasons":[],"repo_signals":{},"physical_eval":{},"llm_review":{}}}\n',
                encoding="utf-8",
            )
            messages = "\n".join(error.message for error in validate_record_store(db))
            self.assertIn("duplicate title", messages)
            self.assertIn("missing primary_url", messages)
            self.assertIn("presentation.featured must be boolean", messages)
            self.assertIn("presentation.order must be a non-negative integer", messages)

    def test_triage_downranks_algorithm_only_and_promotes_framework_bindings(self):
        algorithmic = Candidate(
            title="A Mathematical Proof for New Sampling",
            url="https://example.org/proof",
            summary="We provide a theorem and simulation on synthesized datasets.",
            topics=("reliability-evaluation",),
        )
        bound = Candidate(
            title="AITER Kernels for ROCm LLM Serving",
            url="https://github.com/ROCm/AITER",
            summary="Optimized Triton and C++ kernels integrated with vLLM, SGLang, Kubernetes, and Docker.",
            topics=("kernel-compiler",),
        )
        self.assertEqual(triage_candidate(algorithmic).verdict, "downrank")
        self.assertEqual(triage_candidate(bound).priority, "high")

    def test_triage_downranks_peripheral_work_without_serving_signal(self):
        peripheral = Candidate(
            title="A General Vector Database",
            url="https://example.org/vector-db",
            summary="A vector database benchmark for generic retrieval.",
            topics=("agent-rag",),
        )
        self.assertEqual(triage_candidate(peripheral, core_only=True).priority, "low")

    def test_core_triage_downranks_non_llm_inference_systems(self):
        candidate = Candidate(
            title="FENIX: In-Network DNN Inference with FPGA-Enhanced Programmable Switches",
            url="https://example.org/fenix",
            summary="A programmable-switch system for low-latency DNN inference.",
            topics=("runtime-serving", "kernel-compiler"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.verdict, "downrank")
        self.assertEqual(result.priority, "low")

    def test_triage_downranks_generic_attention_and_training_titles(self):
        generic_attention = Candidate(
            title="A Unified Sparse Attention Method",
            url="https://example.org/attention",
            topics=("kernel-compiler",),
        )
        moe_training = Candidate(
            title="Load Balancing for Mixture-of-Experts Training",
            url="https://example.org/moe-training",
            topics=("moe",),
        )
        self.assertEqual(triage_candidate(generic_attention, core_only=True).priority, "low")
        self.assertEqual(triage_candidate(moe_training, core_only=True).priority, "low")

    def test_triage_downranks_quantum_decoder_even_when_decoding_matches(self):
        quantum_decoder = Candidate(
            title="Quantum Error Correction Decoder",
            url="https://example.org/quantum",
            topics=("kernel-compiler",),
        )
        self.assertEqual(triage_candidate(quantum_decoder, core_only=True).priority, "low")

    def test_triage_keeps_moe_serving_title(self):
        moe_serving = Candidate(
            title="System-Hardware Co-design for Efficient MoE Serving",
            url="https://example.org/moe",
            topics=("runtime-serving", "moe"),
        )
        self.assertEqual(triage_candidate(moe_serving, core_only=True).priority, "normal")

    def test_triage_downranks_generic_moe_kernel_without_serving_evidence(self):
        generic_moe = Candidate(
            title="Understanding Mixture-of-Experts with a Kernel Method",
            url="https://example.org/paper",
            topics=("moe", "kernel-compiler"),
        )
        result = triage_candidate(generic_moe, core_only=True)
        self.assertEqual(result.verdict, "downrank")
        self.assertEqual(result.priority, "low")

    def test_triage_downranks_security_attack_with_moe_inference_wording(self):
        attack = Candidate(
            title="A Membership Inference Attack on MoE Routing",
            url="https://example.org/paper",
            topics=("moe", "runtime-serving"),
        )
        result = triage_candidate(attack, core_only=True)
        self.assertEqual(result.verdict, "downrank")
        self.assertEqual(result.priority, "low")

    def test_triage_downranks_inference_time_model_method(self):
        candidate = Candidate(
            title="Evolving Contextual Safety in Multi-Modal Large Language Models via Inference-Time Self-Reflective Memory",
            url="https://example.org/paper",
            topics=("runtime-serving", "compression-cost"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "low")

    def test_triage_keeps_inference_optimization_title(self):
        candidate = Candidate(
            title="Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding",
            url="https://example.org/paper",
            topics=("runtime-serving", "compression-cost"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_keeps_foundation_model_inference_title(self):
        candidate = Candidate(
            title="Accelerating Foundation Model Inference on Memory-Constrained GPUs",
            url="https://example.org/paper",
            topics=("runtime-serving", "hardware-edge"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_keeps_generative_inference_system_title(self):
        candidate = Candidate(
            title="Harmonia: QoS-Aware and High-Throughput Generative Inference with a Single GPU",
            url="https://example.org/paper",
            topics=("runtime-serving",),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_keeps_kernel_system_with_llm_evidence_in_summary(self):
        candidate = Candidate(
            title="MPK: A Compiler and Runtime for Mega-Kernelizing Tensor Programs",
            url="https://example.org/mpk",
            summary="A compiler and runtime for multi-GPU LLM inference with persistent kernel execution.",
            topics=("kernel-compiler", "runtime-serving"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_does_not_promote_generic_kubernetes_title(self):
        candidate = Candidate(
            title="Kubernetes Packing Heuristics for Multi-Tenant Clusters",
            url="https://example.org/paper",
            topics=("program-scheduling",),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "low")

    def test_triage_promotes_kubernetes_llm_inference_title(self):
        candidate = Candidate(
            title="Kubernetes-Native Predictive Autoscaling for SLO-Aware AI Inference",
            url="https://example.org/paper",
            topics=("runtime-serving", "reliability-evaluation"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "high")

    def test_candidate_record_preserves_official_source_evidence(self):
        candidate = Candidate(
            title="PTStore: Distributed Prefix Caching",
            url="https://2026.euro-par.org/paper#ptstore",
            source_id="europar26-accepted",
            source_name="Euro-Par 2026 official accepted papers",
            tier="A",
            topics=("state-kv", "runtime-serving"),
        )
        record = candidate_to_record(candidate, "paper", "queued")
        self.assertEqual(record["evidence"]["source_type"], "conference_program")
        self.assertEqual(record["evidence"]["venue_status"], "formal_conference")
        self.assertEqual(record["evidence"]["verification_level"], "official_source")

    def test_triage_keeps_kv_cache_scheduler_title_without_llm_token(self):
        candidate = Candidate(
            title="PKAS: Predictive KVCache-Aware Scheduling",
            url="https://example.org/paper",
            topics=("state-kv", "runtime-serving"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_keeps_lora_serving_title(self):
        candidate = Candidate(
            title="M-LoRA: Efficient Serving for Concurrent LoRA Adapters with Memory-Aware Speculative Scheduler",
            url="https://example.org/paper",
            topics=("runtime-serving", "state-kv"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_keeps_edge_rag_system_title(self):
        candidate = Candidate(
            title="SRAG: A Lightweight and Specialized Retrieval-augmented Generation System at the Edge",
            url="https://example.org/paper",
            topics=("agent-rag", "runtime-serving", "hardware-edge"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.priority, "normal")

    def test_triage_does_not_treat_source_topics_as_physical_evidence(self):
        generic_gpu = Candidate(
            title="Adaptive GPU Memory Oversubscription",
            url="https://example.org/gpu",
            topics=("runtime-serving", "moe", "hardware-edge"),
        )
        self.assertEqual(triage_candidate(generic_gpu, core_only=True).priority, "low")

    def test_triage_does_not_promote_nonserving_release_from_repo_structure(self):
        candidate = Candidate(
            title="AITER v0.1.17",
            url="https://github.com/ROCm/aiter/releases/tag/v0.1.17",
            summary="Release notes for CUDA and ROCm kernels.",
            topics=("kernel-compiler", "hardware-edge"),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.verdict, "downrank")
        self.assertEqual(result.priority, "low")

    def test_decoder_word_does_not_trigger_decode_serving_signal(self):
        candidate = Candidate(
            title="Foundation Models with Traditional Decoders",
            url="https://example.org/paper",
            topics=("runtime-serving",),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertEqual(result.verdict, "downrank")
        self.assertEqual(result.priority, "low")

    def test_llm_driven_does_not_trigger_llm_d_binding(self):
        candidate = Candidate(
            title="LLM-Driven Agent Planning",
            url="https://example.org/paper",
            topics=("agent-rag",),
        )
        result = triage_candidate(candidate, core_only=True)
        self.assertFalse(result.physical_eval["has_framework_binding"])
        self.assertEqual(result.priority, "low")

    def test_triage_records_unavailable_github_metadata_without_rejecting(self):
        candidate = Candidate(
            title="Kernel Project",
            url="https://github.com/example/kernel-project",
            summary="CUDA kernel implementation for inference serving.",
        )
        with patch(
            "scripts.ai_infra_monitor.ai_infra_monitor.triage.inspect_github_repository",
            return_value={"repository": "example/kernel-project", "unavailable": "HTTPError: rate limited"},
        ):
            result = triage_candidate(candidate, inspect_repo=True)
        self.assertEqual(result.verdict, "keep")
        self.assertIn("unavailable", result.repo_signals)

    def test_triage_candidates_uses_bounded_parallelism_and_preserves_order(self):
        candidates = [
            Candidate(title=f"Serving Runtime {index}", url=f"https://example.org/{index}")
            for index in range(6)
        ]
        lock = Lock()
        state = {"active": 0, "maximum": 0}

        def fake_triage(candidate, **_kwargs):
            with lock:
                state["active"] += 1
                state["maximum"] = max(state["maximum"], state["active"])
            sleep(0.02)
            with lock:
                state["active"] -= 1
            return candidate.title

        with patch(
            "scripts.ai_infra_monitor.ai_infra_monitor.triage.triage_candidate",
            side_effect=fake_triage,
        ):
            results = triage_candidates(candidates, max_workers=3)

        self.assertGreaterEqual(state["maximum"], 2)
        self.assertEqual(results, [candidate.title for candidate in candidates])


if __name__ == "__main__":
    unittest.main()
