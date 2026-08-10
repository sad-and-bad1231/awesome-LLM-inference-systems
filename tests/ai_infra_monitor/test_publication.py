import errno
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.ai_infra_monitor.ai_infra_monitor.publication import GENERATED_NOTICE, render_public_repository
from scripts.ai_infra_monitor.ai_infra_monitor.validation import validate_workspace


def _record(
    record_type: str,
    title: str,
    category: str,
    status: str = "verified",
    presentation: dict | None = None,
) -> dict:
    record = {
        "id": f"{record_type}-{title.lower().replace(' ', '-')}",
        "canonical_id": f"{record_type}:{title.lower().replace(' ', '-')}",
        "aliases": [],
        "status_history": [],
        "evidence": {
            "venue_status": "formal_conference" if record_type == "paper" else "industrial_material",
            "source_type": "conference_program" if record_type == "paper" else "project_or_engineering_material",
            "verification_level": "verified",
            "verified_at": "2026-07-14",
        },
        "record_type": record_type,
        "title": title,
        "venue_or_channel": "OSDI 2026" if record_type == "paper" else "Open Source Project",
        "year": "2026",
        "orgs": "Example Org",
        "summary": "A concise serving systems summary.",
        "source_tier": "A",
        "primary_url": "https://example.org/resource",
        "artifact_url": "",
        "source_ids": [],
        "status": status,
        "system_abstraction_primary": "Execution Compilation & Kernel Fusion",
        "system_abstraction_secondary": [],
        "technical_tags": {
            "phase": ["serving"],
            "hardware": ["gpu"],
            "optimization_layer": ["kernel"],
            "workload": [],
            "framework_binding": ["vllm"],
            "metrics": ["latency"],
        },
        "triage": {
            "verdict": "keep",
            "priority": "high",
            "reasons": [],
            "repo_signals": {},
            "physical_eval": {},
        },
        "display_category": category,
        "topics": [],
        "discovered": "",
    }
    if presentation is not None:
        record["presentation"] = presentation
    return record


class PublicationTests(unittest.TestCase):
    def test_publication_applies_separate_reading_budgets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            papers.parent.mkdir(parents=True)

            paper_records = []
            for index in range(5):
                record = _record("paper", f"Runtime Paper {index}", "Runtime、调度与服务架构")
                record["curation"] = {
                    "version": "guide-2026-v6",
                    "scope": "core",
                    "priority": "frontier",
                    "themes": ["runtime-scheduling"],
                    "reasons": ["test"],
                }
                paper_records.append(record)
            for index in range(5):
                record = _record("paper", f"Agent Exploration {index}", "Agent、RAG、多模态与应用级 Serving")
                record["curation"] = {
                    "version": "guide-2026-v6",
                    "scope": "adjacent",
                    "priority": "supporting",
                    "themes": [],
                    "reasons": ["test"],
                }
                paper_records.append(record)

            industry_records = []
            for index in range(5):
                record = _record("project", f"Runtime Project {index}", "Runtime、调度与服务架构")
                record["primary_url"] = f"https://github.com/example/runtime-{index}"
                record["curation"] = {
                    "version": "guide-2026-v6",
                    "scope": "core",
                    "priority": "frontier",
                    "themes": ["runtime-scheduling"],
                    "project_key": f"github:example/runtime-{index}",
                    "reasons": ["test"],
                }
                industry_records.append(record)

            papers.write_text("\n".join(json.dumps(item) for item in paper_records) + "\n", encoding="utf-8")
            industry.write_text("\n".join(json.dumps(item) for item in industry_records) + "\n", encoding="utf-8")

            render_public_repository(
                papers,
                industry,
                root,
                public_paper_limit_per_theme=3,
                public_industry_limit_per_theme=2,
                public_exploration_limit_per_track=2,
                public_company_topic_limit=2,
            )

            paper_text = (root / "papers" / "README.md").read_text(encoding="utf-8")
            industry_text = (root / "industry" / "README.md").read_text(encoding="utf-8")
            self.assertIn("Runtime Paper 2", paper_text)
            self.assertNotIn("Runtime Paper 3", paper_text)
            self.assertIn("Agent Exploration 1", paper_text)
            self.assertNotIn("Agent Exploration 2", paper_text)
            self.assertIn("Runtime Project 1", industry_text)
            self.assertNotIn("Runtime Project 2", industry_text)
            self.assertNotIn("all core records remain below", paper_text)
            self.assertIn("bounded core reading set", paper_text)

    def test_publication_retries_a_transient_windows_write_lock(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            papers.parent.mkdir(parents=True)
            papers.write_text("", encoding="utf-8")
            industry.write_text("", encoding="utf-8")
            target = root / "papers" / "README.md"
            original_write_text = Path.write_text
            attempts = 0

            def flaky_write_text(path, *args, **kwargs):
                nonlocal attempts
                if path == target and attempts < 2:
                    attempts += 1
                    raise OSError(errno.EINVAL, "transient lock")
                return original_write_text(path, *args, **kwargs)

            with patch.object(Path, "write_text", new=flaky_write_text):
                render_public_repository(papers, industry, root)

            self.assertEqual(attempts, 2)
            self.assertTrue(target.exists())

    def test_validation_rejects_raw_html_and_oversized_display_summaries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paper_view = root / "papers.md"
            industry_view = root / "industry.md"
            candidate_view = root / "candidates.md"
            paper_view.write_text(
                "| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |\n"
                "|---|---|---|---|\n"
                f"| Paper | Venue | Org | {'x' * 241} |\n",
                encoding="utf-8",
            )
            industry_view.write_text(
                "| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |\n"
                "|---|---|---:|---|---|---|\n"
                "| Org | Project | 2026 | Runtime | <h2>raw release</h2> | link |\n",
                encoding="utf-8",
            )
            candidate_view.write_text("# Candidates\n", encoding="utf-8")

            errors = validate_workspace(paper_view, industry_view, candidate_view)
            messages = "\n".join(error.message for error in errors)
            self.assertIn("display summary exceeds 240 characters", messages)
            self.assertIn("raw HTML in generated view", messages)

    def test_public_views_share_theme_exploration_and_project_compaction(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            papers.parent.mkdir(parents=True)
            core = _record("paper", "FlashAttention-4 Attention Kernel", "算子、编译与硬件加速")
            exploration = _record("paper", "Comic Generation Inference Enhancement", "Agent、RAG、多模态与应用级 Serving")
            exploration["technical_tags"]["framework_binding"] = []
            exploration["technical_tags"]["optimization_layer"] = ["pipeline"]
            exploration["technical_tags"]["workload"] = ["multimodal", "comic-generation"]
            project = _record("project", "Example LLM Serving Runtime", "Runtime、调度与服务架构")
            project["primary_url"] = "https://github.com/example/runtime"
            deepseek = _record("project", "FlashMLA", "算子、编译与硬件加速")
            deepseek["primary_url"] = "https://github.com/deepseek-ai/FlashMLA"
            deepseek["presentation"] = {
                "topic": "deepseek-ai-systems",
                "topic_group": "kernels",
            }
            moonshot = _record("project", "Mooncake", "Runtime、调度与服务架构")
            moonshot["primary_url"] = "https://github.com/kvcache-ai/Mooncake"
            moonshot["presentation"] = {
                "topic": "moonshot-ai-systems",
                "topic_group": "inference-systems",
            }
            minimax = _record("project", "MiniMax-M3", "Runtime、调度与服务架构")
            minimax["primary_url"] = "https://github.com/MiniMax-AI/MiniMax-M3"
            minimax["presentation"] = {
                "topic": "minimax-ai-systems",
                "topic_group": "models-architecture",
            }
            third_party = _record(
                "project", "Third-party DeepSeek Runtime", "Runtime、调度与服务架构"
            )
            release = _record("project", "v1.2.3", "Runtime、调度与服务架构")
            release["primary_url"] = "https://github.com/example/runtime/releases/tag/v1.2.3"
            release["summary"] = "<h2>Release notes</h2>" + " serving compiler" * 1000
            papers.write_text("\n".join(json.dumps(item) for item in [core, exploration]) + "\n", encoding="utf-8")
            industry.write_text(
                "\n".join(
                    json.dumps(item)
                    for item in [project, release, deepseek, moonshot, minimax, third_party]
                ) + "\n",
                encoding="utf-8",
            )

            render_public_repository(papers, industry, root)

            papers_text = (root / "papers" / "README.md").read_text(encoding="utf-8")
            industry_text = (root / "industry" / "README.md").read_text(encoding="utf-8")
            self.assertIn("Attention / Kernel", papers_text)
            self.assertIn("探索观察", papers_text)
            self.assertIn("Comic Generation Inference Enhancement", papers_text)
            self.assertEqual(industry_text.count("Example LLM Serving Runtime"), 1)
            self.assertEqual(industry_text.count("## DeepSeek AI 系统专题"), 1)
            self.assertEqual(industry_text.count("## Kimi / Moonshot AI 系统专题"), 1)
            self.assertEqual(industry_text.count("## MiniMax AI 系统专题"), 1)
            topic_text = industry_text.split("## DeepSeek AI 系统专题", 1)[1].split(
                "## Resource List", 1
            )[0]
            self.assertIn("FlashMLA", topic_text)
            self.assertNotIn("Third-party DeepSeek Runtime", topic_text)
            self.assertNotIn("<h2>", industry_text)

    def test_renders_awesome_root_and_separate_public_collections(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            papers.parent.mkdir(parents=True)
            papers.write_text(
                "\n".join(
                    json.dumps(item)
                    for item in [
                    _record("paper", "Serving Paper", "Runtime、调度与服务架构"),
                    _record("paper", "Hidden Candidate", "Runtime、调度与服务架构", "queued"),
                        {
                            **_record("paper", "Training Only", "Runtime、调度与服务架构"),
                            "summary": "A training-only optimization on optimizer convergence.",
                            "technical_tags": {key: [] for key in _record("paper", "x", "x")["technical_tags"]},
                        },
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            industry.write_text(
                json.dumps(_record("project", "Serving Project", "Runtime、调度与服务架构")) + "\n",
                encoding="utf-8",
            )

            render_public_repository(papers, industry, root)

            readme = (root / "README.md").read_text(encoding="utf-8")
            papers_view = (root / "papers" / "README.md").read_text(encoding="utf-8")
            industry_view = (root / "industry" / "README.md").read_text(encoding="utf-8")
            archive_view = (root / "archive" / "README.md").read_text(encoding="utf-8")
            self.assertIn("Awesome AI Inference Systems", readme)
            self.assertIn("papers/README.md", readme)
            self.assertIn("industry/README.md", readme)
            self.assertIn("Serving Paper", papers_view)
            self.assertNotIn("Hidden Candidate", papers_view)
            self.assertNotIn("Training Only", papers_view)
            self.assertIn("Training Only", archive_view)
            self.assertIn("Archive", archive_view)
            self.assertIn("Formal Conference", papers_view)
            self.assertIn("Serving Project", industry_view)
            self.assertIn("Collection Navigation", papers_view)
            self.assertIn("How to read this page", papers_view)
            self.assertIn("Start Here", readme)
            self.assertIn("docs/START-HERE.md", readme)
            self.assertIn("| 1 | 1 | 1 | 7 |", readme)
            self.assertIn("papers/README.md#kv-cache", readme)
            self.assertIn("industry/README.md#runtime-scheduling", readme)
            self.assertNotIn("#kv-state-memory", readme)
            self.assertIn("Reading Paths", readme)
            self.assertIn("Evidence Ladder", readme)
            self.assertIn("Open-source project", industry_view)
            self.assertIn("generated from data/papers.jsonl", papers_view)

    def test_mainline_records_are_sorted_by_foundation_then_frontier(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            papers.parent.mkdir(parents=True)
            foundation = _record("paper", "FlashAttention: IO-Aware Attention", "算子、编译与硬件加速")
            foundation["year"] = "2022"
            frontier = _record("paper", "Adaptive Fused Kernel for LLM Serving", "算子、编译与硬件加速")
            papers.write_text("\n".join(json.dumps(item) for item in (frontier, foundation)) + "\n", encoding="utf-8")
            industry.write_text("", encoding="utf-8")

            render_public_repository(papers, industry, root)

            papers_view = (root / "papers" / "README.md").read_text(encoding="utf-8")
            self.assertIn("Reading priority: foundation", papers_view)
            self.assertLess(
                papers_view.index("FlashAttention: IO-Aware Attention"),
                papers_view.index("Adaptive Fused Kernel for LLM Serving"),
            )

    def test_presentation_metadata_controls_featured_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            papers.parent.mkdir(parents=True)
            papers.write_text(
                "\n".join(
                    json.dumps(item)
                    for item in [
                        _record("paper", "Later Featured", "Runtime、调度与服务架构", presentation={"featured": True, "order": 20}),
                        _record("paper", "First Featured", "Runtime、调度与服务架构", presentation={"featured": True, "order": 10}),
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            industry.write_text("", encoding="utf-8")

            render_public_repository(papers, industry, root)

            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertLess(readme.index("First Featured"), readme.index("Later Featured"))
            self.assertIn("Academic Papers", readme)
            self.assertIn("TTFT under Drift", readme)

    def test_public_views_validate_assets_links_and_counts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            papers = root / "data" / "papers.jsonl"
            industry = root / "data" / "industry.jsonl"
            candidates = root / "data" / "candidates.jsonl"
            papers.parent.mkdir(parents=True)
            papers.write_text(json.dumps(_record("paper", "Serving Paper", "Runtime、调度与服务架构")) + "\n", encoding="utf-8")
            industry.write_text(json.dumps(_record("project", "Serving Project", "Runtime、调度与服务架构")) + "\n", encoding="utf-8")
            candidates.write_text("", encoding="utf-8")
            render_public_repository(papers, industry, root)

            (root / "figs").mkdir()
            source_figs = Path(__file__).parents[2] / "figs"
            for name in ("ai-inference-systems-cover.png", "ai-inference-system-map.png"):
                shutil.copyfile(source_figs / name, root / "figs" / name)
            for name in ("ai-infra-system-abstractions.md", "CONTRIBUTING.md"):
                shutil.copyfile(Path(__file__).parents[2] / name, root / name)
            (root / "docs").mkdir()
            shutil.copyfile(
                Path(__file__).parents[2] / "docs" / "START-HERE.md",
                root / "docs" / "START-HERE.md",
            )
            paper_view = root / "paper-list.md"
            industry_view = root / "industrial.md"
            candidate_view = root / "candidates.md"
            for path in (paper_view, industry_view, candidate_view):
                path.write_text(GENERATED_NOTICE + "\n", encoding="utf-8")

            errors = validate_workspace(
                paper_view,
                industry_view,
                candidate_view,
                paper_db_path=papers,
                industry_db_path=industry,
                candidate_db_path=candidates,
                public_root=root,
            )
            self.assertEqual(errors, [])

            (root / "figs" / "ai-inference-system-map.png").unlink()
            errors = validate_workspace(
                paper_view,
                industry_view,
                candidate_view,
                paper_db_path=papers,
                industry_db_path=industry,
                candidate_db_path=candidates,
                public_root=root,
            )
            self.assertTrue(any("required public image" in error.message for error in errors))


if __name__ == "__main__":
    unittest.main()
