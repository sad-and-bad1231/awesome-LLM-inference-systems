import json
import tempfile
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.publication import render_public_repository


def _record(record_type: str, title: str, category: str, status: str = "verified") -> dict:
    return {
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


class PublicationTests(unittest.TestCase):
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
            self.assertIn("Awesome AI Inference Systems", readme)
            self.assertIn("papers/README.md", readme)
            self.assertIn("industry/README.md", readme)
            self.assertIn("Serving Paper", papers_view)
            self.assertNotIn("Hidden Candidate", papers_view)
            self.assertNotIn("Training Only", papers_view)
            self.assertIn("Formal Conference", papers_view)
            self.assertIn("Serving Project", industry_view)
            self.assertIn("generated from data/papers.jsonl", papers_view)


if __name__ == "__main__":
    unittest.main()
