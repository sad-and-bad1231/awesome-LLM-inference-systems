from __future__ import annotations

import json
import re
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path

from .fetch import HttpFetcher
from .identity import candidate_fingerprint, candidate_identity, normalize_title
from .models import Candidate
from .parsers import parse_source
from .records import load_records
from .state import load_state, save_state
from .triage import triage_candidate


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _document_titles(path: Path) -> set[str]:
    if not path.exists():
        return set()
    titles = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*-", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not cells:
            continue
        if cells[0] == "题目":
            continue
        if cells[0] == "企业/组织":
            continue
        title = cells[1] if len(cells) >= 6 else cells[0]
        titles.add(normalize_title(title))
    return titles


def _record_titles(path: Path) -> set[str]:
    return {
        normalize_title(record.get("title", ""))
        for record in load_records(path)
        if record.get("title")
    }


def _matched_topics(text: str, topics: list[dict]) -> tuple[str, ...]:
    lowered = text.lower()
    return tuple(
        topic["id"]
        for topic in topics
        if any(keyword.lower() in lowered for keyword in topic.get("keywords", []))
    )


class DiscoveryEngine:
    def __init__(self, root: Path, config_path: Path, fetcher=None):
        self.root = Path(root)
        self.config_path = Path(config_path)
        self.config = load_config(self.config_path)
        settings = self.config["settings"]
        self.state_path = self.root / settings["state_file"]
        self.fetcher = fetcher or HttpFetcher(
            settings.get("user_agent", "ai-infra-monitor/1.0"),
            int(settings.get("request_timeout_seconds", 25)),
        )

    def discover(self, mode: str) -> dict:
        if mode not in {"daily", "weekly"}:
            raise ValueError("mode must be daily or weekly")
        now = datetime.now(timezone.utc)
        run_id = now.strftime("%Y%m%dT%H%M%S%fZ")
        settings = self.config["settings"]
        state = load_state(self.state_path)
        existing_titles = set()
        for key in ("paper_db_file", "industry_db_file", "candidate_db_file"):
            if settings.get(key):
                existing_titles.update(_record_titles(self.root / settings[key]))
        for key in ("paper_file", "industry_file"):
            existing_titles.update(_document_titles(self.root / settings[key]))

        candidates: list[Candidate] = []
        errors: list[dict[str, str]] = []
        source_stats: list[dict[str, object]] = []
        for source in self.config["sources"]:
            if mode not in source.get("modes", []):
                continue
            has_deferred = any(
                record.get("status") == "deferred"
                and record.get("source_id") == source["id"]
                for record in state["records"].values()
            )
            cache = {} if has_deferred else state["sources"].get(source["id"], {})
            emitted = 0
            try:
                response = self.fetcher.fetch(source, cache)
                status = int(response.get("status", 200))
                if status == 304:
                    source_stats.append(
                        {"source_id": source["id"], "status": 304, "emitted": 0}
                    )
                    continue
                raw_items = parse_source(source, response["body"])
                for raw in raw_items:
                    haystack = " ".join(
                        (raw.get("title", ""), raw.get("summary", ""), source["name"])
                    )
                    topics = tuple(
                        dict.fromkeys(
                            (
                                *source.get("topics", []),
                                *_matched_topics(haystack, self.config["topics"]),
                            )
                        )
                    )
                    if not topics:
                        continue
                    candidate = Candidate(
                        title=raw["title"].strip(),
                        url=raw["url"].strip(),
                        source_id=source["id"],
                        source_name=source["name"],
                        tier=source.get("tier", "B"),
                        kind=source.get("kind", "paper"),
                        published=raw.get("published", ""),
                        discovered=now.date().isoformat(),
                        topics=topics,
                        summary=raw.get("summary", ""),
                        venue=raw.get("venue", ""),
                    )
                    candidate = replace(
                        candidate,
                        triage=triage_candidate(
                            candidate,
                            inspect_repo=bool(settings.get("discovery_repo_inspection", False)),
                            repo_timeout_seconds=int(settings.get("github_repo_timeout_seconds", 6)),
                            core_only=bool(settings.get("core_serving_only", False)),
                        ).to_dict(),
                    )
                    identity = candidate_identity(candidate)
                    fingerprint = candidate_fingerprint(candidate)
                    previous = state["records"].get(identity)
                    known_title = normalize_title(candidate.title) in existing_titles
                    if (
                        previous
                        and previous.get("fingerprint") == fingerprint
                        and previous.get("status") != "deferred"
                    ):
                        continue
                    if known_title and not previous:
                        state["records"][identity] = {
                            "status": "indexed",
                            "fingerprint": fingerprint,
                            "title": candidate.title,
                            "url": candidate.url,
                            "source_id": source["id"],
                            "last_seen": now.isoformat(),
                        }
                        continue
                    update = bool(previous and previous.get("fingerprint") != fingerprint)
                    candidate = replace(
                        candidate,
                        identity=identity,
                        fingerprint=fingerprint,
                        update=update,
                    )
                    candidates.append(candidate)
                    state["records"][identity] = {
                        "status": "pending",
                        "fingerprint": fingerprint,
                        "title": candidate.title,
                        "url": candidate.url,
                        "source_id": source["id"],
                        "last_seen": now.isoformat(),
                        "run_id": run_id,
                    }
                    emitted += 1
                state["sources"][source["id"]] = {
                    "etag": response.get("etag", ""),
                    "last_modified": response.get("last_modified", ""),
                    "last_checked": now.isoformat(),
                }
                source_stats.append(
                    {"source_id": source["id"], "status": status, "emitted": emitted}
                )
            except Exception as error:
                errors.append(
                    {
                        "source_id": source["id"],
                        "source_name": source["name"],
                        "error": f"{type(error).__name__}: {error}",
                    }
                )
                source_stats.append(
                    {"source_id": source["id"], "status": "error", "emitted": 0}
                )

        limit = int(settings[f"{mode}_limit"])
        priority_rank = {"high": 0, "normal": 1, "low": 2}
        candidates.sort(
            key=lambda item: (
                priority_rank.get(str(item.triage.get("priority", "normal")), 1),
                item.tier != "A",
                item.source_id,
                item.title,
            )
        )
        candidates = candidates[:limit]
        selected_identities = {item.identity for item in candidates}
        for identity, record in state["records"].items():
            if record.get("run_id") == run_id and identity not in selected_identities:
                record["status"] = "deferred"

        run_dir = self.root / settings["runs_dir"] / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        manifest = {
            "version": 1,
            "run_id": run_id,
            "mode": mode,
            "created_at": now.isoformat(),
            "candidate_count": len(candidates),
            "candidates": [item.to_dict() for item in candidates],
            "errors": errors,
            "sources": source_stats,
        }
        (run_dir / "candidates.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        state["runs"].append(
            {
                "run_id": run_id,
                "mode": mode,
                "created_at": now.isoformat(),
                "candidate_count": len(candidates),
                "error_count": len(errors),
                "status": "discovered",
            }
        )
        state["runs"] = state["runs"][-100:]
        save_state(self.state_path, state)
        return manifest
