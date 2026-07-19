from __future__ import annotations

import gzip
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.maintenance import (
    archive_candidates,
    compact_state_data,
    maintain_data,
)
from scripts.ai_infra_monitor.ai_infra_monitor.records import load_records, write_records


def _candidate(identity: str, status: str, discovered: str) -> dict:
    return {
        "id": identity,
        "canonical_id": f"candidate:{identity}",
        "record_type": "candidate",
        "title": identity,
        "status": status,
        "discovered": discovered,
    }


def _load_gzip_jsonl(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in gzip.decompress(path.read_bytes()).decode("utf-8").splitlines()
        if line.strip()
    ]


class CandidateArchiveTests(unittest.TestCase):
    def test_archive_moves_only_old_terminal_candidates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            hot_path = root / "data" / "candidates.jsonl"
            archive_dir = root / "data" / "archive" / "candidates"
            write_records(
                hot_path,
                [
                    _candidate("old-drop", "drop", "2025-12-01"),
                    _candidate("old-promote", "promote", "2025-12-15"),
                    _candidate("recent-drop", "drop", "2026-07-01"),
                    _candidate("old-active", "new", "2025-10-01"),
                    _candidate("undated-drop", "drop", ""),
                ],
            )

            result = archive_candidates(
                hot_path,
                archive_dir,
                hot_window_days=180,
                today=date(2026, 7, 19),
            )

            self.assertEqual(result["archived"], 2)
            self.assertEqual(result["hot_records"], 3)
            self.assertEqual(result["skipped_undated"], 1)
            self.assertEqual(
                [record["id"] for record in load_records(hot_path)],
                ["recent-drop", "old-active", "undated-drop"],
            )
            shard = archive_dir / "candidates-2025-12.jsonl.gz"
            self.assertEqual(
                [record["id"] for record in _load_gzip_jsonl(shard)],
                ["old-drop", "old-promote"],
            )

    def test_archive_is_deterministic_deduplicated_and_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            hot_path = root / "candidates.jsonl"
            archive_dir = root / "archive"
            duplicate = _candidate("same", "drop", "2025-01-10")
            write_records(hot_path, [duplicate, dict(duplicate)])

            first = archive_candidates(
                hot_path,
                archive_dir,
                hot_window_days=180,
                today=date(2026, 7, 19),
            )
            shard = archive_dir / "candidates-2025-01.jsonl.gz"
            first_bytes = shard.read_bytes()
            second = archive_candidates(
                hot_path,
                archive_dir,
                hot_window_days=180,
                today=date(2026, 7, 19),
            )

            self.assertEqual(first["archived"], 2)
            self.assertEqual(first["archive_records"], 1)
            self.assertEqual(second["archived"], 0)
            self.assertEqual(second["changed_shards"], 0)
            self.assertEqual(shard.read_bytes(), first_bytes)
            self.assertEqual(len(_load_gzip_jsonl(shard)), 1)

    def test_terminal_hot_limit_archives_overflow_without_touching_active_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            hot_path = root / "candidates.jsonl"
            archive_dir = root / "archive"
            write_records(
                hot_path,
                [
                    _candidate("drop-a", "drop", "2026-07-18"),
                    _candidate("drop-b", "drop", "2026-07-18"),
                    _candidate("drop-c", "drop", "2026-07-18"),
                    _candidate("active", "new", "2025-01-01"),
                ],
            )

            result = archive_candidates(
                hot_path,
                archive_dir,
                hot_window_days=180,
                hot_terminal_limit=2,
                today=date(2026, 7, 19),
            )

            self.assertEqual(result["archived"], 1)
            hot_ids = {record["id"] for record in load_records(hot_path)}
            self.assertIn("active", hot_ids)
            self.assertEqual(len(hot_ids & {"drop-a", "drop-b", "drop-c"}), 2)

    def test_corrupt_existing_archive_does_not_partially_rotate_hot_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            hot_path = root / "candidates.jsonl"
            archive_dir = root / "archive"
            archive_dir.mkdir()
            corrupt = archive_dir / "candidates-2024-01.jsonl.gz"
            corrupt.write_bytes(b"not-gzip")
            write_records(
                hot_path,
                [_candidate("old", "drop", "2025-01-10")],
            )
            before = hot_path.read_bytes()

            with self.assertRaises((gzip.BadGzipFile, EOFError)):
                archive_candidates(
                    hot_path,
                    archive_dir,
                    hot_window_days=180,
                    today=date(2026, 7, 19),
                )

            self.assertEqual(hot_path.read_bytes(), before)
            self.assertFalse((archive_dir / "candidates-2025-01.jsonl.gz").exists())


class StateCompactionTests(unittest.TestCase):
    def test_compacts_only_old_terminal_state_rows(self):
        state = {
            "records": {
                "old": {
                    "fingerprint": "fp-old",
                    "status": "processed",
                    "source_id": "source-a",
                    "last_seen": "2025-01-01T00:00:00+00:00",
                    "title": "Old title",
                    "url": "https://example.org/old",
                    "run_id": "run-old",
                },
                "recent": {
                    "fingerprint": "fp-recent",
                    "status": "indexed",
                    "source_id": "source-b",
                    "last_seen": "2026-07-01T00:00:00+00:00",
                    "title": "Recent title",
                    "url": "https://example.org/recent",
                    "run_id": "run-recent",
                },
                "deferred": {
                    "fingerprint": "fp-deferred",
                    "status": "deferred",
                    "source_id": "source-c",
                    "last_seen": "2025-01-01T00:00:00+00:00",
                    "title": "Deferred title",
                    "url": "https://example.org/deferred",
                    "run_id": "run-deferred",
                },
            }
        }

        changed = compact_state_data(state, 180, today=date(2026, 7, 19))

        self.assertEqual(changed, 1)
        self.assertEqual(
            state["records"]["old"],
            {
                "fingerprint": "fp-old",
                "status": "processed",
                "source_id": "source-a",
                "last_seen": "2025-01-01T00:00:00+00:00",
            },
        )
        self.assertIn("title", state["records"]["recent"])
        self.assertIn("title", state["records"]["deferred"])

    def test_maintenance_rewrites_existing_state_as_compact_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            state_path = root / "state.json"
            state_path.write_text(
                json.dumps(
                    {"version": 1, "sources": {}, "records": {}, "runs": []},
                    indent=2,
                ),
                encoding="utf-8",
            )

            maintain_data(
                root / "candidates.jsonl",
                root / "archive",
                state_path,
                180,
                today=date(2026, 7, 19),
            )

            text = state_path.read_text(encoding="utf-8")
            self.assertEqual(
                text,
                '{"records":{},"runs":[],"sources":{},"version":1}\n',
            )


if __name__ == "__main__":
    unittest.main()
