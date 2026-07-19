import copy
import unittest


def _industry_record(title, url, *, summary="Concise project summary.", year="2026", priority="frontier", themes=None):
    return {
        "record_type": "project",
        "title": title,
        "primary_url": url,
        "artifact_url": "",
        "canonical_id": f"url:{url}",
        "source_ids": ["example-releases"],
        "orgs": "Example Org",
        "venue_or_channel": "Official project material",
        "year": year,
        "summary": summary,
        "status": "queued",
        "source_tier": "A",
        "evidence": {
            "venue_status": "industrial_material",
            "source_type": "project_or_engineering_material",
            "verification_level": "verified",
            "verified_at": f"{year}-06-01",
        },
        "curation": {
            "version": "guide-2026-v6",
            "scope": "core",
            "priority": priority,
            "themes": themes or ["runtime-scheduling"],
            "project_key": "github:example/project",
            "reasons": ["test"],
        },
    }


class ReadingPresentationTests(unittest.TestCase):
    def test_display_summary_strips_html_truncates_and_preserves_source(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import display_summary

        record = _industry_record(
            "Project",
            "https://github.com/example/project",
            summary="<h2>Highlights</h2><p>" + ("Fast serving and KV transfer. " * 30) + "</p>",
        )
        before = copy.deepcopy(record)
        rendered = display_summary(record, max_chars=80)

        self.assertLessEqual(len(rendered), 80)
        self.assertNotIn("<h2>", rendered)
        self.assertEqual(record, before)

    def test_long_release_notes_use_structured_neutral_summary(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import display_summary

        record = _industry_record(
            "v1.2.3",
            "https://github.com/example/project/releases/tag/v1.2.3",
            summary="<ul><li>change</li></ul>" * 1000,
            themes=["kv-cache", "runtime-scheduling"],
        )
        rendered = display_summary(record)

        self.assertIn("官方发布记录", rendered)
        self.assertIn("KV Cache", rendered)
        self.assertNotIn("<li>", rendered)

    def test_project_key_prefers_github_repository_then_release_source(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import project_key_for

        github = _industry_record("v1", "https://github.com/Example/Project/releases/tag/v1")
        source = _industry_record("Release", "https://example.org/release")
        source["source_ids"] = ["tensor-runtime-releases"]

        self.assertEqual(project_key_for(github), "github:example/project")
        self.assertEqual(project_key_for(source), "source:tensor-runtime")

    def test_project_aggregation_prefers_non_release_anchor_and_distinct_milestones(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import aggregate_industry_records

        anchor = _industry_record("Example Project", "https://github.com/example/project")
        stable = _industry_record(
            "v2.0.0 KV Cache",
            "https://github.com/example/project/releases/tag/v2.0.0",
            themes=["kv-cache"],
        )
        rc = _industry_record(
            "v3.0.0rc1 Speculative Decoding",
            "https://github.com/example/project/releases/tag/v3.0.0rc1",
            themes=["speculative-decoding"],
        )
        duplicate_theme = _industry_record(
            "v2.1.0 KV Cache",
            "https://github.com/example/project/releases/tag/v2.1.0",
            themes=["kv-cache"],
        )
        groups = aggregate_industry_records([rc, duplicate_theme, anchor, stable], milestone_limit=3)

        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]["anchor"]["title"], "Example Project")
        self.assertEqual(len(groups[0]["milestones"]), 2)
        self.assertEqual(
            {item["curation"]["themes"][0] for item in groups[0]["milestones"]},
            {"kv-cache", "speculative-decoding"},
        )

    def test_project_aggregation_falls_back_to_latest_stable_before_prerelease(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import aggregate_industry_records

        stable = _industry_record("v2.0.0", "https://github.com/example/project/releases/tag/v2.0.0")
        stable["evidence"]["verified_at"] = "2026-05-01"
        rc = _industry_record("v3.0.0rc1", "https://github.com/example/project/releases/tag/v3.0.0rc1")
        rc["evidence"]["verified_at"] = "2026-07-01"

        group = aggregate_industry_records([rc, stable])[0]
        self.assertEqual(group["anchor"]["title"], "v2.0.0")


if __name__ == "__main__":
    unittest.main()
