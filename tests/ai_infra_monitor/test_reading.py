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
        "status": "verified",
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
    def test_public_selector_applies_theme_budget_and_stable_priority_order(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import select_public_mainline

        supporting = _industry_record(
            "Supporting Runtime", "https://example.org/supporting", priority="supporting"
        )
        frontier = _industry_record(
            "Frontier Runtime", "https://example.org/frontier", priority="frontier"
        )
        foundation = _industry_record(
            "Foundation Runtime", "https://example.org/foundation", priority="foundation"
        )
        multi_theme = _industry_record(
            "Multi Theme",
            "https://example.org/multi",
            priority="foundation",
            themes=["runtime-scheduling", "kv-cache"],
        )

        first = select_public_mainline(
            [supporting, frontier, multi_theme, foundation], limit_per_theme=2
        )
        second = select_public_mainline(
            [foundation, multi_theme, frontier, supporting], limit_per_theme=2
        )

        self.assertEqual(
            [record["title"] for record in first],
            ["Multi Theme", "Foundation Runtime", "Frontier Runtime"],
        )
        self.assertEqual(first[0]["_reading_themes"][0], "kv-cache")
        self.assertEqual(
            [record["title"] for record in first],
            [record["title"] for record in second],
        )
        self.assertEqual(sum(record["title"] == "Multi Theme" for record in first), 1)

    def test_configured_industry_topics_render_in_fixed_order(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import render_industry_topics

        moonshot = _industry_record("Mooncake", "https://github.com/kvcache-ai/Mooncake")
        moonshot["curation"]["project_key"] = "github:kvcache-ai/mooncake"
        moonshot["presentation"] = {
            "topic": "moonshot-ai-systems",
            "topic_group": "inference-systems",
        }
        minimax = _industry_record("MiniMax-M3", "https://github.com/MiniMax-AI/MiniMax-M3")
        minimax["curation"]["project_key"] = "github:minimax-ai/minimax-m3"
        minimax["presentation"] = {
            "topic": "minimax-ai-systems",
            "topic_group": "models-architecture",
        }
        third_party = _industry_record(
            "Unofficial MiniMax runtime", "https://github.com/example/minimax-runtime"
        )

        rendered = render_industry_topics([third_party, minimax, moonshot])

        self.assertLess(rendered.index("## Kimi / Moonshot AI 系统专题"), rendered.index("## MiniMax AI 系统专题"))
        self.assertIn("Mooncake", rendered)
        self.assertIn("MiniMax-M3", rendered)
        self.assertNotIn("Unofficial MiniMax runtime", rendered)

    def test_industry_topic_is_explicit_deduplicated_and_group_sorted(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import select_industry_topic

        storage = _industry_record("3FS", "https://github.com/deepseek-ai/3FS")
        storage["curation"]["project_key"] = "github:deepseek-ai/3fs"
        storage["presentation"] = {
            "topic": "deepseek-ai-systems",
            "topic_group": "storage",
        }
        kernel = _industry_record("FlashMLA", "https://github.com/deepseek-ai/FlashMLA")
        kernel["curation"]["project_key"] = "github:deepseek-ai/flashmla"
        kernel["presentation"] = {
            "topic": "deepseek-ai-systems",
            "topic_group": "kernels",
        }
        release = _industry_record(
            "v1.0.0", "https://github.com/deepseek-ai/FlashMLA/releases/tag/v1.0.0"
        )
        release["curation"]["project_key"] = "github:deepseek-ai/flashmla"
        release["presentation"] = {
            "topic": "deepseek-ai-systems",
            "topic_group": "kernels",
        }
        third_party = _industry_record(
            "DeepSeek-compatible runtime", "https://github.com/example/deepseek-runtime"
        )

        selected = select_industry_topic(
            [storage, third_party, release, kernel], "deepseek-ai-systems"
        )

        self.assertEqual([item["title"] for item in selected], ["FlashMLA", "3FS"])

    def test_industry_topic_applies_a_deterministic_project_budget(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import select_industry_topic

        records = []
        for index in range(4):
            record = _industry_record(
                f"Kernel {index}", f"https://github.com/deepseek-ai/kernel-{index}"
            )
            record["curation"]["project_key"] = f"github:deepseek-ai/kernel-{index}"
            record["presentation"] = {
                "topic": "deepseek-ai-systems",
                "topic_group": "kernels",
            }
            records.append(record)

        selected = select_industry_topic(records, "deepseek-ai-systems", limit=2)

        self.assertEqual([record["title"] for record in selected], ["Kernel 0", "Kernel 1"])

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
        source["curation"]["project_key"] = "source:tensor-runtime"

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

    def test_unpromoted_releases_do_not_expand_project_themes_or_milestones(self):
        from scripts.ai_infra_monitor.ai_infra_monitor.reading import aggregate_industry_records

        anchor = _industry_record(
            "Transfer Library",
            "https://github.com/example/project",
            themes=["prefill-decode-transfer"],
        )
        queued_release = _industry_record(
            "v2.0.0 MoE compiler release",
            "https://github.com/example/project/releases/tag/v2.0.0",
            themes=["moe", "compiler-dsl"],
        )
        queued_release["status"] = "queued"

        project = aggregate_industry_records([anchor, queued_release])[0]

        self.assertEqual(project["themes"], ["prefill-decode-transfer"])
        self.assertEqual(project["milestones"], [])


if __name__ == "__main__":
    unittest.main()
