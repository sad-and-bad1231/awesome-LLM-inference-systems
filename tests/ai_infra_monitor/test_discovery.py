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


class FairnessFetcher:
    def fetch(self, source, cache):
        if source["id"] == "large":
            entries = "".join(
                f"""
                <entry>
                  <id>https://example.test/large/{index}</id>
                  <updated>2026-06-14T{index:02d}:00:00Z</updated>
                  <title>Generic Paper {index}</title>
                  <summary>LLM serving system.</summary>
                  <link href="https://example.test/large/{index}"/>
                </entry>
                """
                for index in range(6)
            )
        else:
            entries = """
            <entry>
              <id>https://example.test/small/1</id>
              <updated>2026-06-14T10:00:00Z</updated>
              <title>Small Source KV Cache Runtime</title>
              <summary>KV cache runtime for LLM inference.</summary>
              <link href="https://example.test/small/1"/>
            </entry>
            """
        return {
            "status": 200,
            "body": (
                b'''<?xml version="1.0"?>
                <feed xmlns="http://www.w3.org/2005/Atom">'''
                + entries.encode()
                + b"</feed>"
            ),
            "etag": "one",
            "last_modified": "today",
        }


class DiscoveryTests(unittest.TestCase):
    def test_source_batch_partitions_eligible_sources_deterministically(self):
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
                        "id": f"source-{index}",
                        "name": f"Source {index}",
                        "type": "feed",
                        "url": f"https://example.test/{index}",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["weekly"],
                    }
                    for index in range(4)
                ],
            }
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")

            first = DiscoveryEngine(root, config_path, fetcher=FakeFetcher()).discover(
                "weekly", source_batch_index=0, source_batch_count=2
            )
            second = DiscoveryEngine(root, config_path, fetcher=FakeFetcher()).discover(
                "weekly", source_batch_index=1, source_batch_count=2
            )

            self.assertEqual(
                [item["source_id"] for item in first["sources"]],
                ["source-0", "source-1"],
            )
            self.assertEqual(
                [item["source_id"] for item in second["sources"]],
                ["source-2", "source-3"],
            )

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

    def test_source_fairness_prevents_large_source_from_monopolizing_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "paper-list.md").write_text("# Papers\n", encoding="utf-8")
            (root / "industrial.md").write_text("# Industry\n", encoding="utf-8")
            config = {
                "version": 1,
                "settings": {
                    "daily_limit": 10,
                    "weekly_limit": 4,
                    "max_candidates_per_source": 2,
                    "core_serving_only": True,
                    "paper_file": "paper-list.md",
                    "industry_file": "industrial.md",
                    "candidate_file": "candidates.md",
                    "state_file": "state.json",
                    "runs_dir": "runs",
                    "weekly_reports_dir": "reports/weekly",
                },
                "topics": [
                    {"id": "serving", "keywords": ["llm serving", "kv cache"]}
                ],
                "sources": [
                    {
                        "id": "large",
                        "name": "Large",
                        "type": "feed",
                        "url": "https://example.test/large",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["weekly"],
                    },
                    {
                        "id": "small",
                        "name": "Small",
                        "type": "feed",
                        "url": "https://example.test/small",
                        "tier": "A",
                        "kind": "paper",
                        "modes": ["weekly"],
                    },
                ],
            }
            config_path = root / "config.yaml"
            config_path.write_text(json.dumps(config), encoding="utf-8")

            result = DiscoveryEngine(
                root, config_path, fetcher=FairnessFetcher()
            ).discover("weekly")

            self.assertEqual(result["candidate_count"], 3)
            self.assertEqual(
                {item["source_id"] for item in result["candidates"]},
                {"large", "small"},
            )
            self.assertEqual(
                sum(item["source_id"] == "large" for item in result["candidates"]),
                2,
            )
            self.assertEqual(result["suppressed_count"], 4)
            self.assertEqual(
                result["sources"][0]["selected"] + result["sources"][1]["selected"],
                3,
            )


if __name__ == "__main__":
    unittest.main()
