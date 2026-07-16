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
        for command in ("discover", "migrate", "triage", "queue", "compact", "render", "publish", "validate", "finalize", "status"):
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


if __name__ == "__main__":
    unittest.main()
