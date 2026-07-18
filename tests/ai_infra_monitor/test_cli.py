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
    def test_help_lists_core_commands(self):
        result = subprocess.run(
            [sys.executable, str(MONITOR), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("discover", "sweep", "migrate", "triage", "queue", "compact", "curate", "render", "publish", "validate", "finalize", "status"):
            self.assertIn(command, result.stdout)

    def test_discover_keeps_new_candidates_in_run_manifest_until_triage(self):
        from scripts.ai_infra_monitor.monitor import command_discover

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
            manifest = {
                "run_id": "run-1",
                "candidates": [
                    {
                        "title": "New Serving Candidate",
                        "url": "https://example.org/serving",
                        "source_id": "source",
                        "source_name": "Source",
                        "tier": "A",
                        "kind": "paper",
                        "topics": ["runtime-serving"],
                        "triage": {"verdict": "keep", "priority": "normal"},
                    }
                ],
            }
            args = SimpleNamespace(
                root=root,
                config=config,
                mode="weekly",
                source_id=[],
            )
            with patch("scripts.ai_infra_monitor.monitor.DiscoveryEngine") as engine:
                engine.return_value.discover.return_value = manifest
                self.assertEqual(command_discover(args), 0)

            self.assertFalse((root / "data" / "candidates.jsonl").exists())

    def test_sweep_processes_every_source_batch_through_lifecycle(self):
        from scripts.ai_infra_monitor import monitor

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = SimpleNamespace(
                root=root,
                config=root / "config.yaml",
                mode="weekly",
                source_id=[],
                source_batch_count=2,
                end_batch_index=None,
                tiers=["A", "B", "C"],
                report=True,
                no_commit=True,
            )
            manifests = [{"run_id": "run-1"}, {"run_id": "run-2"}]
            with patch.object(monitor, "DiscoveryEngine") as engine, patch.object(
                monitor, "command_triage"
            ) as triage, patch.object(monitor, "command_queue") as queue, patch.object(
                monitor, "command_report"
                ) as report, patch.object(monitor, "command_finalize") as finalize:
                engine.return_value.discover.side_effect = manifests
                for action in (triage, queue, report, finalize):
                    action.return_value = 0

                self.assertEqual(monitor.command_sweep(args), 0)

            self.assertEqual(engine.return_value.discover.call_count, 2)
            self.assertEqual([call.args[0].run_id for call in triage.call_args_list], ["run-1", "run-2"])
            self.assertEqual([call.args[0].run_id for call in queue.call_args_list], ["run-1", "run-2"])
            self.assertEqual([call.args[0].run_id for call in report.call_args_list], ["run-1", "run-2"])
            self.assertEqual([call.args[0].run_id for call in finalize.call_args_list], ["run-1", "run-2"])
            self.assertEqual([call.args[0].skip_render for call in finalize.call_args_list], [True, False])

    def test_sweep_can_resume_from_a_later_batch(self):
        from scripts.ai_infra_monitor import monitor

        args = SimpleNamespace(
            root=Path("."),
            config=Path("config.yaml"),
            mode="weekly",
            source_id=[],
            source_batch_count=6,
            start_batch_index=2,
            end_batch_index=5,
            tiers=["A"],
            report=False,
            no_commit=True,
        )
        manifests = [{"run_id": f"run-{index}"} for index in range(2, 6)]
        with patch.object(monitor, "DiscoveryEngine") as engine, patch.object(
            monitor, "command_triage", return_value=0
        ), patch.object(monitor, "command_queue", return_value=0), patch.object(
            monitor, "command_finalize", return_value=0
        ):
            engine.return_value.discover.side_effect = manifests
            self.assertEqual(monitor.command_sweep(args), 0)

        self.assertEqual(engine.return_value.discover.call_count, 4)
        self.assertEqual(
            [call.kwargs["source_batch_index"] for call in engine.return_value.discover.call_args_list],
            [2, 3, 4, 5],
        )

    def test_sweep_stops_batch_lifecycle_after_triage_failure(self):
        from scripts.ai_infra_monitor import monitor

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = SimpleNamespace(
                root=root,
                config=root / "config.yaml",
                mode="weekly",
                source_id=[],
                source_batch_count=1,
                end_batch_index=None,
                tiers=["A"],
                report=True,
                no_commit=True,
            )
            with patch.object(monitor, "DiscoveryEngine") as engine, patch.object(
                monitor, "command_triage", return_value=1
            ) as triage, patch.object(monitor, "command_queue") as queue, patch.object(
                monitor, "command_report"
            ) as report, patch.object(monitor, "command_finalize") as finalize:
                engine.return_value.discover.return_value = {"run_id": "run-1"}
                self.assertEqual(monitor.command_sweep(args), 1)

            triage.assert_called_once()
            queue.assert_not_called()
            report.assert_not_called()
            finalize.assert_not_called()

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
            with patch.object(monitor, "promote_candidates", return_value={"paper": 1, "industry": 0}):
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
                "scripts.ai_infra_monitor.monitor.triage_candidates",
                return_value=results,
            ), patch("scripts.ai_infra_monitor.monitor.write_records") as writer:
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
                "scripts.ai_infra_monitor.monitor.triage_candidates",
                return_value=[TriageResult(verdict="downrank", priority="low")],
            ):
                self.assertEqual(command_triage(args), 0)

            updated = load_records(root / "data" / "papers.jsonl")[0]
            self.assertEqual(updated["status"], "drop")
            self.assertEqual(updated["triage"]["verdict"], "downrank")
            self.assertEqual(load_records(root / "data" / "candidates.jsonl")[0]["status"], "drop")


if __name__ == "__main__":
    unittest.main()
