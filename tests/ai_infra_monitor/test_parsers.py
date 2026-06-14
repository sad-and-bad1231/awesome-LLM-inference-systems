import json
import unittest
from pathlib import Path

from scripts.ai_infra_monitor.ai_infra_monitor.parsers import (
    parse_feed,
    parse_github_releases,
    parse_html_index,
)


FIXTURES = Path(__file__).parent / "fixtures"


class ParserTests(unittest.TestCase):
    def test_parse_atom_feed(self):
        items = parse_feed((FIXTURES / "feed.xml").read_bytes(), "fixture")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Efficient LLM Serving with KV Cache Transfer")
        self.assertEqual(items[0]["published"], "2026-06-14T10:00:00Z")

    def test_parse_html_index_resolves_links(self):
        items = parse_html_index(
            (FIXTURES / "index.html").read_bytes(),
            "https://conference.example/program/",
        )
        self.assertEqual(items[0]["url"], "https://conference.example/paper/one")
        self.assertEqual(items[1]["url"], "https://conference.example/about")

    def test_parse_github_releases(self):
        payload = json.dumps(
            [
                {
                    "name": "v1.2.0",
                    "tag_name": "v1.2.0",
                    "html_url": "https://github.com/org/repo/releases/tag/v1.2.0",
                    "published_at": "2026-06-14T01:00:00Z",
                    "body": "Adds KV cache transfer.",
                    "draft": False,
                    "prerelease": False,
                }
            ]
        ).encode()
        items = parse_github_releases(payload)
        self.assertEqual(items[0]["title"], "v1.2.0")
        self.assertIn("KV cache", items[0]["summary"])


if __name__ == "__main__":
    unittest.main()

