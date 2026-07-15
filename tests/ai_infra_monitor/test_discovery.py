import json
import tempfile
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.discovery import DiscoveryEngine


class FakeFetcher:
    def fetch(self, source, cache):
        return {
            "status": 200,
            "body": b"""<?xml version="1.0"?>
            <feed xmlns="http://www.w3.org/2005/Atom">
              <entry>
                <id>http://arxiv.org/abs/2606.12345v1</id>
                <updated>2026-06-14T10:00:00Z</updated>
                <title>Efficient LLM Serving with KV Cache Transfer</title>
                <summary>Disaggregated inference with RDMA.</summary>
                <link href="https://arxiv.org/abs/2606.12345v1"/>
              </entry>
            </feed>""",
            "etag": "one",
            "last_modified": "today",
        }


class BacklogFetcher:
    def fetch(self, source, cache):
        if cache:
            return {
                "status": 304,
                "body": b"",
                "etag": "one",
                "last_modified": "today",
            }
        return {
            "status": 200,
            "body": b"""<?xml version="1.0"?>
            <feed xmlns="http://www.w3.org/2005/Atom">
              <entry>
                <id>http://arxiv.org/abs/2606.10001v1</id>
                <updated>2026-06-14T10:00:00Z</updated>
                <title>First LLM Serving System</title>
                <summary>KV cache runtime.</summary>
                <link href="https://arxiv.org/abs/2606.10001v1"/>
              </entry>
              <entry>
                <id>http://arxiv.org/abs/2606.10002v1</id>
                <updated>2026-06-14T11:00:00Z</updated>
                <title>Second LLM Serving System</title>
                <summary>KV cache runtime.</summary>
                <link href="https://arxiv.org/abs/2606.10002v1"/>
              </entry>
            </feed>""",
            "etag": "one",
            "last_modified": "today",
        }


class DiscoveryTests(unittest.TestCase):
    def test_source_filter_limits_discovery_without_changing_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "paper-list.md").write_text("# Papers\n", encoding="utf-8")
            (root / "industrial.md").write_text("# Industry\n", encoding="utf-8")
            config = {
                "version": 1,
                "settings": {
                    "daily_limit": 10,
                    "weekly_limit": 20,
                    "paper_file": "paper-list.md",
                    "industry_file": "industrial.md",
                    "candidate_file": "candidates.md",
                    "state_file": "state.json",
                    "runs_dir": "runs",
                    "weekly_reports_dir": "reports",
                },
                "topics": [{"id": "serving", "keywords": ["llm serving"]}],
                "sources": [
                    {
                        "id": "selected",
                        "name": "Selected",
                        "type": "feed",
                        "url": "https://example.test/selected",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["weekly"],
                    },
                    {
                        "id": "skipped",
                        "name": "Skipped",
                        "type": "feed",
                        "url": "https://example.test/skipped",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["weekly"],
                    },
                ],
            }
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            result = DiscoveryEngine(root, config_path, fetcher=FakeFetcher()).discover(
                "weekly", source_ids={"selected"}
            )
            self.assertEqual([item["source_id"] for item in result["candidates"]], ["selected"])
            self.assertEqual([item["source_id"] for item in result["sources"]], ["selected"])

    def test_second_run_does_not_emit_duplicate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "paper-list.md").write_text(
                "# Papers\n| 题目 | 发表的会议 | 主要作者单位 | 一句话总结 |\n"
                "|---|---|---|---|\n",
                encoding="utf-8",
            )
            (root / "industrial.md").write_text("# Industry\n", encoding="utf-8")
            config = {
                "version": 1,
                "settings": {
                    "daily_limit": 10,
                    "weekly_limit": 20,
                    "paper_file": "paper-list.md",
                    "industry_file": "industrial.md",
                    "candidate_file": "candidates.md",
                    "state_file": "state.json",
                    "runs_dir": "runs",
                    "weekly_reports_dir": "reports",
                },
                "topics": [{"id": "serving", "keywords": ["llm serving", "kv cache"]}],
                "sources": [
                    {
                        "id": "fixture",
                        "name": "Fixture",
                        "type": "feed",
                        "url": "https://example.test/feed",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["daily"],
                    }
                ],
            }
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            first = DiscoveryEngine(root, config_path, fetcher=FakeFetcher()).discover("daily")
            self.assertEqual(first["candidate_count"], 1)
            second = DiscoveryEngine(root, config_path, fetcher=FakeFetcher()).discover("daily")
            self.assertEqual(second["candidate_count"], 0)

    def test_existing_industry_solution_is_not_reemitted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "paper-list.md").write_text("# Papers\n", encoding="utf-8")
            (root / "industrial.md").write_text(
                "# Industry\n"
                "| 企业/组织 | 方案/论文 | 年份 | 对应方向 | 核心做法 | 材料 |\n"
                "|---|---|---:|---|---|---|\n"
                "| Example | Efficient LLM Serving with KV Cache Transfer | 2026 | runtime | x | y |\n",
                encoding="utf-8",
            )
            config = {
                "version": 1,
                "settings": {
                    "daily_limit": 10,
                    "weekly_limit": 20,
                    "paper_file": "paper-list.md",
                    "industry_file": "industrial.md",
                    "candidate_file": "candidates.md",
                    "state_file": "state.json",
                    "runs_dir": "runs",
                    "weekly_reports_dir": "reports",
                },
                "topics": [{"id": "serving", "keywords": ["llm serving", "kv cache"]}],
                "sources": [
                    {
                        "id": "fixture",
                        "name": "Fixture",
                        "type": "feed",
                        "url": "https://example.test/feed",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["daily"],
                    }
                ],
            }
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            result = DiscoveryEngine(root, config_path, fetcher=FakeFetcher()).discover("daily")
            self.assertEqual(result["candidate_count"], 0)

    def test_deferred_backlog_bypasses_conditional_fetch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "paper-list.md").write_text("# Papers\n", encoding="utf-8")
            (root / "industrial.md").write_text("# Industry\n", encoding="utf-8")
            config = {
                "version": 1,
                "settings": {
                    "daily_limit": 1,
                    "weekly_limit": 1,
                    "paper_file": "paper-list.md",
                    "industry_file": "industrial.md",
                    "candidate_file": "candidates.md",
                    "state_file": "state.json",
                    "runs_dir": "runs",
                    "weekly_reports_dir": "reports",
                },
                "topics": [{"id": "serving", "keywords": ["llm serving", "kv cache"]}],
                "sources": [
                    {
                        "id": "fixture",
                        "name": "Fixture",
                        "type": "feed",
                        "url": "https://example.test/feed",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["daily"],
                    }
                ],
            }
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            first = DiscoveryEngine(
                root, config_path, fetcher=BacklogFetcher()
            ).discover("daily")
            second = DiscoveryEngine(
                root, config_path, fetcher=BacklogFetcher()
            ).discover("daily")
            self.assertEqual(first["candidate_count"], 1)
            self.assertEqual(second["candidate_count"], 1)
            self.assertNotEqual(
                first["candidates"][0]["identity"],
                second["candidates"][0]["identity"],
            )


if __name__ == "__main__":
    unittest.main()
