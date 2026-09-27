import subprocess
import sys
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
MONITOR = ROOT / "scripts" / "ai_infra_monitor" / "monitor.py"


class CliTests(unittest.TestCase):
    def test_public_reading_options_use_bounded_defaults(self):
        from scripts.ai_infra_monitor.monitor import public_reading_options

        options = public_reading_options({"settings": {}})

        self.assertEqual(
            options,
            {
                "public_paper_limit_per_theme": 8,
                "public_industry_limit_per_theme": 5,
                "public_exploration_limit_per_track": 15,
                "public_company_topic_limit": 8,
            },
        )

    def test_help_lists_core_commands(self):
        result = subprocess.run(
            [sys.executable, str(MONITOR), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("discover", "sweep", "migrate", "triage", "queue", "compact", "maintain", "curate", "render", "publish", "validate", "audit", "finalize", "status"):
            self.assertIn(command, result.stdout)

    def test_maintain_outputs_one_compact_summary_line(self):
        from scripts.ai_infra_monitor import monitor

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "config.json"
            config.write_text(
                json.dumps(
                    {
                        "settings": {
                            "paper_file": "papers.md",
                            "industry_file": "industry.md",
                            "candidate_file": "candidates.md",
                            "state_file": "state.json",
                            "runs_dir": "runs",
                            "weekly_reports_dir": "reports",
                            "candidate_db_file": "data/candidates.jsonl",
                            "candidate_archive_dir": "data/archive/candidates",
                            "candidate_hot_window_days": 180,
                        },
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            args = SimpleNamespace(root=root, config=config)
            result = {
                "archived": 2,
                "hot_records": 3,
                "archive_records": 2,
                "archive_shards": 1,
                "changed_shards": 1,
                "skipped_undated": 0,
                "state_compacted": 4,
            }
            with patch("scripts.ai_infra_monitor.ai_infra_monitor.maintenance.maintain_data", return_value=result), patch(
                "builtins.print"
            ) as printer:
                self.assertEqual(monitor.command_maintain(args), 0)

            printer.assert_called_once()
            self.assertNotIn("\n", printer.call_args.args[0])

    def test_sweep_no_commit_flag_keeps_finalization_local(self):
        from scripts.ai_infra_monitor.monitor import build_parser

        args = build_parser().parse_args(
            ["sweep", "--mode", "weekly", "--no-commit"]
        )

        self.assertTrue(args.no_commit)

    def test_queue_preserves_promote_status_history(self):
        from scripts.ai_infra_monitor import monitor

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "config.json"
            config.write_text(
                json.dumps(
                    {
                        "settings": {
                            "paper_file": "paper-list.md",
                            "industry_file": "industry.md",
                            "candidate_file": "candidates.md",
                            "state_file": "state.json",
                            "runs_dir": "runs",
                            "weekly_reports_dir": "reports",
                            "candidate_db_file": "data/candidates.jsonl",
                        },
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            run_dir = root / "runs" / "run-1"
            run_dir.mkdir(parents=True)
            (run_dir / "candidates.json").write_text(
                json.dumps(
                    {
                        "run_id": "run-1",
                        "candidates": [
                            {
                                "title": "Queue Candidate",
                                "url": "https://example.org/queue",
                                "kind": "paper",
                                "tier": "A",
                                "triage": {"verdict": "keep", "priority": "high"},
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            candidate_path = root / "data" / "candidates.jsonl"
            candidate_path.parent.mkdir(parents=True)
            candidate_path.write_text(
                json.dumps(
                    {
                        "id": "candidate_queue",
                        "canonical_id": "url:https://example.org/queue",
                        "record_type": "candidate",
                        "title": "Queue Candidate",
                        "venue_or_channel": "source",
                        "year": 2026,
                        "orgs": [],
                        "summary": "candidate",
                        "source_tier": "A",
                        "primary_url": "https://example.org/queue",
                        "artifact_url": "",
                        "source_ids": [],
                        "status": "new",
                        "status_history": [],
                        "system_abstraction_primary": "Execution Compilation & Kernel Fusion",
                        "system_abstraction_secondary": [],
                        "technical_tags": {
                            "phase": "decode",
                            "hardware": "cuda",
                            "optimization_layer": "runtime",
                            "workload": "llm-inference",
                            "framework_binding": [],
                            "metrics": [],
                        },
                        "triage": {
                            "verdict": "keep",
                            "priority": "high",
                            "reasons": [],
                            "repo_signals": {},
                            "physical_eval": {},
                        },
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            args = SimpleNamespace(root=root, config=config, run_id="run-1", tiers=["A"])
            with patch("scripts.ai_infra_monitor.ai_infra_monitor.records.promote_candidates", return_value={"paper": 1, "industry": 0}):
                self.assertEqual(monitor.command_queue(args), 0)

            record = json.loads(candidate_path.read_text(encoding="utf-8").strip())
            self.assertEqual(record["status"], "promote")
            self.assertEqual(record["status_history"][-1]["status"], "promote")

    def test_triage_persists_only_keep_candidates_with_actionable_priority(self):
        from scripts.ai_infra_monitor.monitor import command_triage
        from scripts.ai_infra_monitor.ai_infra_monitor.triage import TriageResult

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "config.json"
            config.write_text(
                json.dumps(
                    {
                        "settings": {
                            "paper_file": "paper-list.md",
                            "industry_file": "industry.md",
                            "candidate_file": "candidates.md",
                            "state_file": "state.json",
                            "runs_dir": "runs",
                            "weekly_reports_dir": "reports",
                            "candidate_db_file": "data/candidates.jsonl",
                        },
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            run_dir = root / "runs" / "run-1"
            run_dir.mkdir(parents=True)
            (run_dir / "candidates.json").write_text(
                json.dumps(
                    {
                        "run_id": "run-1",
                        "candidates": [
                            {"title": "Keep Candidate", "url": "https://example.org/keep", "kind": "paper"},
                            {"title": "Noise Candidate", "url": "https://example.org/noise", "kind": "paper"},
                        ],
                    }
                ),
                encoding="utf-8",
            )
            args = SimpleNamespace(root=root, config=config, run_id="run-1")
            results = [
                TriageResult(verdict="keep", priority="normal"),
                TriageResult(verdict="downrank", priority="low"),
            ]
            with patch(
                "scripts.ai_infra_monitor.ai_infra_monitor.triage.triage_candidates",
                return_value=results,
            ), patch("scripts.ai_infra_monitor.ai_infra_monitor.records.write_records") as writer:
                self.assertEqual(command_triage(args), 0)

            writer.assert_not_called()

            records = [
                json.loads(line)
                for line in (root / "data" / "candidates.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual([record["title"] for record in records], ["Keep Candidate"])

    def test_triage_demotes_a_promoted_record_when_revalidation_rejects_it(self):
        from scripts.ai_infra_monitor.monitor import command_triage
        from scripts.ai_infra_monitor.ai_infra_monitor.records import candidate_to_record, load_records, write_records
        from scripts.ai_infra_monitor.ai_infra_monitor.models import Candidate
        from scripts.ai_infra_monitor.ai_infra_monitor.triage import TriageResult

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = root / "config.json"
            config.write_text(
                json.dumps(
                    {
                        "settings": {
                            "paper_file": "paper-list.md",
                            "industry_file": "industry.md",
                            "candidate_file": "candidates.md",
                            "state_file": "state.json",
                            "runs_dir": "runs",
                            "weekly_reports_dir": "reports",
                            "candidate_db_file": "data/candidates.jsonl",
                            "paper_db_file": "data/papers.jsonl",
                            "industry_db_file": "data/industry.jsonl",
                        },
                        "sources": [],
                    }
                ),
                encoding="utf-8",
            )
            candidate = Candidate(title="Revalidated Paper", url="https://example.org/revalidate", kind="paper")
            paper = candidate_to_record(candidate, "paper", "queued")
            write_records(root / "data" / "papers.jsonl", [paper])
            candidate_record = candidate_to_record(candidate, "candidate", "promote")
            write_records(root / "data" / "candidates.jsonl", [candidate_record])
            run_dir = root / "runs" / "run-1"
            run_dir.mkdir(parents=True)
            (run_dir / "candidates.json").write_text(
                json.dumps({"run_id": "run-1", "candidates": [candidate.to_dict()]}),
                encoding="utf-8",
            )
            args = SimpleNamespace(root=root, config=config, run_id="run-1")
            with patch(
                "scripts.ai_infra_monitor.ai_infra_monitor.triage.triage_candidates",
                return_value=[TriageResult(verdict="downrank", priority="low")],
            ):
                self.assertEqual(command_triage(args), 0)

            updated = load_records(root / "data" / "papers.jsonl")[0]
            self.assertEqual(updated["status"], "drop")
            self.assertEqual(updated["triage"]["verdict"], "downrank")
            self.assertEqual(load_records(root / "data" / "candidates.jsonl")[0]["status"], "drop")


if __name__ == "__main__":
    unittest.main()
