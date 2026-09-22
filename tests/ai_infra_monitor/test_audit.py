import unittest

from scripts.ai_infra_monitor.ai_infra_monitor.audit import build_audit


def _record(title, *, record_type="paper", scope="core", theme="runtime-scheduling"):
    return {
        "title": title,
        "canonical_id": f"id:{title}",
        "record_type": record_type,
        "year": "2026",
        "discovered": "2026-08-01",
        "summary": "summary",
        "orgs": "Org",
        "artifact_url": "",
        "evidence": {
            "verified_at": "2026-08-10",
            "venue_status": "formal_conference" if record_type == "paper" else "industrial_material",
            "affiliation_status": "verified",
            "artifact_status": "not_found",
            "metadata_checked_at": "2026-08-10",
            "metadata_sources": ["https://example.org/source"],
        },
        "curation": {
            "version": "guide-2026-v6",
            "scope": scope,
            "priority": "frontier",
            "themes": [theme] if scope == "core" else [],
            "project_key": f"project:{title}" if record_type != "paper" else "",
            "reasons": ["test"],
        },
    }


class AuditTests(unittest.TestCase):
    def test_audit_reports_compact_quality_and_public_projection_counts(self):
        papers = [_record("Paper A"), _record("Paper B")]
        papers[1]["canonical_id"] = papers[0]["canonical_id"]
        papers[1]["evidence"]["affiliation_status"] = "not_checked"
        papers[1]["summary"] = "x" * 5001
        adjacent = _record("Exploration", scope="adjacent")
        industry = [_record("Project A", record_type="project")]

        result = build_audit(
            papers + [adjacent],
            industry,
            [],
            paper_limit_per_theme=1,
            industry_limit_per_theme=1,
            exploration_limit_per_track=1,
            company_topic_limit=1,
        )

        self.assertEqual(result["stores"]["papers"]["records"], 3)
        self.assertEqual(result["stores"]["papers"]["scopes"]["core"], 2)
        self.assertEqual(result["stores"]["papers"]["duplicate_canonical_ids"], 1)
        self.assertEqual(result["stores"]["papers"]["long_summaries"], 1)
        self.assertEqual(result["stores"]["papers"]["core_affiliation_status"]["not_checked"], 1)
        self.assertEqual(result["public_projection"]["papers"], 1)
        self.assertEqual(result["public_projection"]["industry_projects"], 1)
        self.assertEqual(result["public_projection"]["paper_exploration"], 1)

    def test_industry_exploration_projection_counts_projects_not_release_records(self):
        first = _record("Project Release 1", record_type="project", scope="adjacent")
        second = _record("Project Release 2", record_type="project", scope="adjacent")
        # head 侧 project_key 由 primary_url / source_ids 派生（不再读取 curation.project_key
        # 缓存），所以让两条记录共享同一仓库 URL 来落进同一个 project。
        first["primary_url"] = "https://github.com/example/project"
        second["primary_url"] = "https://github.com/example/project"

        result = build_audit(
            [],
            [first, second],
            [],
            exploration_limit_per_track=5,
        )

        self.assertEqual(result["public_projection"]["industry_exploration"], 1)

    def test_public_projection_excludes_unpromoted_workflow_statuses(self):
        published = _record("Published")
        published["status"] = "verified"
        queued = _record("Queued")
        queued["status"] = "queued"

        result = build_audit([published, queued], [], [])

        self.assertEqual(result["public_projection"]["papers"], 1)


if __name__ == "__main__":
    unittest.main()
