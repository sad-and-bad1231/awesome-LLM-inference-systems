import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.ai_infra_monitor.ai_infra_monitor.records import (
    load_records,
    migrate_jsonl_to_split_stores,
    render_markdown_views,
    validate_record_stores,
    validate_record_store,
)
from scripts.ai_infra_monitor.ai_infra_monitor.triage import triage_candidate
from scripts.ai_infra_monitor.ai_infra_monitor.models import Candidate


class RecordStoreTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
