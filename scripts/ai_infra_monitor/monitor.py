from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import date
from pathlib import Path
from types import SimpleNamespace

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.ai_infra_monitor.ai_infra_monitor.discovery import (  # noqa: E402
    DiscoveryEngine,
    load_config,
)
from scripts.ai_infra_monitor.ai_infra_monitor.git_ops import (  # noqa: E402
    commit_research_updates,
    is_repository,
)
from scripts.ai_infra_monitor.ai_infra_monitor.models import Candidate  # noqa: E402
from scripts.ai_infra_monitor.ai_infra_monitor.output import (  # noqa: E402
    append_candidate_records,
    load_manifest,
    write_weekly_report,
)
from scripts.ai_infra_monitor.ai_infra_monitor.publication import render_public_repository  # noqa: E402
from scripts.ai_infra_monitor.ai_infra_monitor.records import (  # noqa: E402
    candidate_to_record,
    compact_candidate_records,
    curate_record_stores,
    migrate_jsonl_to_split_stores,
    promote_candidates,
    render_markdown_views,
    validate_record_stores,
    load_records,
    normalize_record,
    write_records,
)
from scripts.ai_infra_monitor.ai_infra_monitor.state import (  # noqa: E402
    load_state,
    save_state,
)
from scripts.ai_infra_monitor.ai_infra_monitor.validation import (  # noqa: E402
    validate_workspace,
)
from scripts.ai_infra_monitor.ai_infra_monitor.triage import (  # noqa: E402
    triage_candidates,
)


ROOT = Path(__file__).resolve().parents[2]


def paths(root: Path, config: dict) -> dict[str, Path]:
    settings = config["settings"]
    defaults = {
        "paper_db_file": "data/papers.jsonl",
        "industry_db_file": "data/industry.jsonl",
        "candidate_db_file": "data/candidates.jsonl",
        "abstraction_file": "ai-infra-system-abstractions.md",
    }
    resolved = {
        key: root / settings[key]
        for key in (
            "paper_file",
            "industry_file",
            "candidate_file",
            "state_file",
            "runs_dir",
            "weekly_reports_dir",
        )
    }
    for key, value in defaults.items():
        resolved[key] = root / settings.get(key, value)
    return resolved


def manifest_path(root: Path, config: dict, run_id: str) -> Path:
    return paths(root, config)["runs_dir"] / run_id / "candidates.json"


def command_init(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    resolved["runs_dir"].mkdir(parents=True, exist_ok=True)
    resolved["weekly_reports_dir"].mkdir(parents=True, exist_ok=True)
    for key in ("paper_db_file", "industry_db_file", "candidate_db_file"):
        resolved[key].parent.mkdir(parents=True, exist_ok=True)
    if not resolved["state_file"].exists():
        example = args.root / "ai-infra-state.example.json"
        if example.exists():
            shutil.copyfile(example, resolved["state_file"])
        else:
            save_state(
                resolved["state_file"],
                {"version": 1, "sources": {}, "records": {}, "runs": []},
            )
    print(json.dumps({"initialized": True, "root": str(args.root)}, ensure_ascii=False))
    return 0


def command_discover(args) -> int:
    source_ids = set(args.source_id) if args.source_id else None
    manifest = DiscoveryEngine(args.root, args.config).discover(
        args.mode,
        source_ids=source_ids,
        source_batch_index=getattr(args, "source_batch_index", 0),
        source_batch_count=getattr(args, "source_batch_count", 1),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


def command_sweep(args) -> int:
    """Run bounded discovery batches through triage, queue, report, and finalize."""
    source_ids = set(args.source_id) if args.source_id else None
    batch_count = max(1, int(args.source_batch_count))
    start_index = max(0, int(getattr(args, "start_batch_index", 0)))
    requested_end = getattr(args, "end_batch_index", None)
    end_index = batch_count - 1 if requested_end is None else int(requested_end)
    if start_index >= batch_count or end_index < start_index or end_index >= batch_count:
        print("invalid sweep batch range", file=sys.stderr)
        return 1
    run_ids: list[str] = []
    failures: list[dict[str, object]] = []
    engine = DiscoveryEngine(args.root, args.config)
    for batch_index in range(start_index, end_index + 1):
        manifest = engine.discover(
            args.mode,
            source_ids=source_ids,
            source_batch_index=batch_index,
            source_batch_count=batch_count,
        )
        run_id = str(manifest["run_id"])
        run_ids.append(run_id)
        lifecycle = SimpleNamespace(root=args.root, config=args.config, run_id=run_id)
        batch_failed = False
        for name, command in (("triage", command_triage), ("queue", command_queue)):
            if name == "queue":
                lifecycle.tiers = args.tiers
            if command(lifecycle) != 0:
                failures.append({"run_id": run_id, "step": name})
                batch_failed = True
                break
        if batch_failed:
            continue
        if args.report:
            if command_report(lifecycle) != 0:
                failures.append({"run_id": run_id, "step": "report"})
                continue
        lifecycle.no_commit = args.no_commit
        # Rendering the whole public repository is global work; defer it until the last batch.
        lifecycle.skip_render = batch_index != end_index
        if command_finalize(lifecycle) != 0:
            failures.append({"run_id": run_id, "step": "finalize"})
    print(
        json.dumps(
            {
                "mode": args.mode,
                "batches": len(run_ids),
                "source_batch_count": batch_count,
                "start_batch_index": start_index,
                "end_batch_index": end_index,
                "run_ids": run_ids,
                "failures": failures,
            },
            ensure_ascii=False,
        )
    )
    return 1 if failures else 0


def command_queue(args) -> int:
    config = load_config(args.config)
    manifest = load_manifest(manifest_path(args.root, config, args.run_id))
    selected = [
        Candidate.from_dict(item)
        for item in manifest["candidates"]
        if item.get("tier") in set(args.tiers)
        and str(item.get("triage", {}).get("priority", "normal")) in {"high", "normal"}
        and str(item.get("triage", {}).get("verdict", "keep")) == "keep"
    ]
    resolved = paths(args.root, config)
    counts = promote_candidates(resolved["paper_db_file"], resolved["industry_db_file"], selected)
    candidate_records = load_records(resolved["candidate_db_file"])
    promoted_ids = {candidate_to_record(item)["canonical_id"] for item in selected}
    for record in candidate_records:
        if record.get("canonical_id") in promoted_ids:
            record["status"] = "promote"
            normalized = normalize_record(record)
            record.clear()
            record.update(normalized)
    write_records(resolved["candidate_db_file"], candidate_records)
    print(json.dumps({"queued": sum(counts.values()), "counts": counts, "run_id": args.run_id}))
    return 0


def command_compact(args) -> int:
    config = load_config(args.config)
    candidate_path = paths(args.root, config)["candidate_db_file"]
    changed = compact_candidate_records(candidate_path)
    print(json.dumps({"compacted": changed, "candidate_db_file": str(candidate_path)}))
    return 0


def command_triage(args) -> int:
    config = load_config(args.config)
    path = manifest_path(args.root, config, args.run_id)
    manifest = load_manifest(path)
    candidates = manifest.get("candidates", [])
    triage_results = triage_candidates(
        [Candidate.from_dict(item) for item in candidates],
        inspect_repo=bool(config["settings"].get("github_repo_inspection", False)),
        repo_timeout_seconds=int(config["settings"].get("github_repo_timeout_seconds", 6)),
        core_only=bool(config["settings"].get("core_serving_only", False)),
        max_workers=int(config["settings"].get("max_parallel_triage", 1)),
    )
    for item, result in zip(candidates, triage_results):
        item["triage"] = result.to_dict()
    priority_rank = {"high": 0, "normal": 1, "low": 2}
    manifest["candidates"] = sorted(
        candidates,
        key=lambda item: (
            priority_rank.get(str(item.get("triage", {}).get("priority", "normal")), 1),
            item.get("tier") != "A",
            item.get("source_id", ""),
            item.get("title", ""),
        ),
    )
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    candidate_records = load_records(paths(args.root, config)["candidate_db_file"])
    by_identity = {candidate_to_record(Candidate.from_dict(item))["canonical_id"]: item for item in manifest.get("candidates", [])}
    changed_existing = False
    for record in candidate_records:
        item = by_identity.get(record.get("canonical_id"))
        if item:
            new_triage = item["triage"]
            if record.get("triage") != new_triage:
                record["triage"] = new_triage
                changed_existing = True
            if (
                record.get("status") in {"new", "keep", "promote"}
                and not (
                    new_triage.get("verdict") == "keep"
                    and new_triage.get("priority") in {"high", "normal"}
                )
            ):
                record["status"] = "drop"
                normalize_record(record)
                changed_existing = True
    if changed_existing:
        write_records(paths(args.root, config)["candidate_db_file"], candidate_records)
    for store_key in ("paper_db_file", "industry_db_file"):
        store_path = paths(args.root, config)[store_key]
        main_records = load_records(store_path)
        changed_main = False
        for record in main_records:
            item = by_identity.get(record.get("canonical_id"))
            if not item:
                continue
            new_triage = item["triage"]
            if record.get("triage") != new_triage:
                record["triage"] = new_triage
                changed_main = True
            if (
                record.get("status") in {"queued", "new", "keep", "promote"}
                and not (
                    new_triage.get("verdict") == "keep"
                    and new_triage.get("priority") in {"high", "normal"}
                )
            ):
                record["status"] = "drop"
                normalize_record(record)
                changed_main = True
        if changed_main:
            write_records(store_path, main_records)
    append_candidate_records(
        paths(args.root, config)["candidate_db_file"],
        [Candidate.from_dict(item) for item in candidates],
    )
    print(json.dumps({"triaged": len(candidates), "run_id": args.run_id}))
    return 0


def command_migrate(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    source = args.source.resolve()
    if not source.exists():
        print(f"migration source does not exist: {source}", file=sys.stderr)
        return 1
    counts = migrate_jsonl_to_split_stores(
        source,
        resolved["paper_db_file"],
        resolved["industry_db_file"],
        resolved["candidate_db_file"],
    )
    print(json.dumps({"migrated": counts, "source": str(source)}))
    return 0


def command_render(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    curate_record_stores(
        resolved["paper_db_file"], resolved["industry_db_file"], resolved["candidate_db_file"]
    )
    render_markdown_views(
        resolved["paper_db_file"],
        resolved["industry_db_file"],
        resolved["candidate_db_file"],
        resolved["paper_file"],
        resolved["industry_file"],
        resolved["candidate_file"],
        resolved["abstraction_file"],
    )
    render_public_repository(
        resolved["paper_db_file"],
        resolved["industry_db_file"],
        args.root,
    )
    print(json.dumps({"rendered": True, "paper_db_file": str(resolved["paper_db_file"]), "industry_db_file": str(resolved["industry_db_file"])}))
    return 0


def command_publish(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    render_public_repository(
        resolved["paper_db_file"],
        resolved["industry_db_file"],
        args.root,
    )
    print(json.dumps({"published_views": ["README.md", "papers/README.md", "industry/README.md", "archive/README.md"]}))
    return 0


def command_curate(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    counts = curate_record_stores(
        resolved["paper_db_file"], resolved["industry_db_file"], resolved["candidate_db_file"]
    )
    print(json.dumps({"curated": counts}, ensure_ascii=False))
    return 0


def command_report(args) -> int:
    config = load_config(args.config)
    manifest = load_manifest(manifest_path(args.root, config, args.run_id))
    report = (
        paths(args.root, config)["weekly_reports_dir"]
        / f"{date.today().isoformat()}-{args.run_id}.md"
    )
    write_weekly_report(manifest, report)
    print(json.dumps({"report": str(report), "run_id": args.run_id}))
    return 0


def command_validate(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    errors = validate_workspace(
        resolved["paper_file"],
        resolved["industry_file"],
        resolved["candidate_file"],
        resolved["paper_db_file"],
        resolved["industry_db_file"],
        resolved["candidate_db_file"],
        args.root,
    )
    if errors:
        for error in errors:
            print(f"{error.path}:{error.line}: {error.message}", file=sys.stderr)
        return 1
    print("validation passed")
    return 0


def command_finalize(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    curate_record_stores(
        resolved["paper_db_file"], resolved["industry_db_file"], resolved["candidate_db_file"]
    )
    jsonl_errors = validate_record_stores(
        resolved["paper_db_file"], resolved["industry_db_file"], resolved["candidate_db_file"]
    )
    if jsonl_errors:
        for error in jsonl_errors:
            print(f"{error.path}:{error.line}: {error.message}", file=sys.stderr)
        return 1
    skip_render = bool(getattr(args, "skip_render", False))
    if not skip_render:
        render_markdown_views(
            resolved["paper_db_file"],
            resolved["industry_db_file"],
            resolved["candidate_db_file"],
            resolved["paper_file"],
            resolved["industry_file"],
            resolved["candidate_file"],
            resolved["abstraction_file"],
        )
        render_public_repository(
            resolved["paper_db_file"],
            resolved["industry_db_file"],
            args.root,
        )
        if command_validate(args):
            return 1
    manifest = load_manifest(manifest_path(args.root, config, args.run_id))
    state = load_state(resolved["state_file"])
    for item in manifest.get("candidates", []):
        identity = item.get("identity")
        if identity in state["records"]:
            state["records"][identity]["status"] = "processed"
    for run in state["runs"]:
        if run["run_id"] == args.run_id:
            run["status"] = "finalized"
    save_state(resolved["state_file"], state)

    commit_output = ""
    if not args.no_commit:
        if not is_repository(args.root):
            print("not a Git repository", file=sys.stderr)
            return 1
        tracked = [
            resolved["paper_db_file"],
            resolved["industry_db_file"],
            resolved["candidate_db_file"],
            resolved["abstraction_file"],
            resolved["paper_file"],
            resolved["industry_file"],
            resolved["candidate_file"],
            args.root / "README.md",
            args.root / "papers" / "README.md",
            args.root / "industry" / "README.md",
        ]
        report_dir = resolved["weekly_reports_dir"]
        if report_dir.exists():
            tracked.extend(report_dir.glob("*.md"))
        commit_output = commit_research_updates(
            args.root,
            f"research: update ai infra index ({args.run_id})",
            tracked,
        )
    print(
        json.dumps(
            {
                "finalized": True,
                "run_id": args.run_id,
                "rendered": not skip_render,
                "committed": bool(commit_output),
            }
        )
    )
    return 0


def command_status(args) -> int:
    config = load_config(args.config)
    state = load_state(paths(args.root, config)["state_file"])
    pending = sum(
        record.get("status") in {"pending", "deferred"}
        for record in state["records"].values()
    )
    print(
        json.dumps(
            {
                "records": len(state["records"]),
                "pending": pending,
                "runs": state["runs"][-10:],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI infrastructure research monitor")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--config", type=Path, default=ROOT / "ai-infra-sources.yaml"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("init").set_defaults(func=command_init)
    discover = subparsers.add_parser("discover")
    discover.add_argument("--mode", choices=("daily", "weekly"), required=True)
    discover.add_argument(
        "--source-id",
        action="append",
        help="limit discovery to one or more configured source IDs; repeatable",
    )
    discover.add_argument(
        "--source-batch-index",
        type=int,
        default=0,
        help="zero-based batch index for partitioning eligible sources",
    )
    discover.add_argument(
        "--source-batch-count",
        type=int,
        default=1,
        help="number of deterministic source batches to run",
    )
    discover.set_defaults(func=command_discover)
    sweep = subparsers.add_parser(
        "sweep",
        help="discover all source batches and process each through triage, queue, and finalize",
    )
    sweep.add_argument("--mode", choices=("daily", "weekly"), required=True)
    sweep.add_argument(
        "--source-id",
        action="append",
        help="limit discovery to one or more configured source IDs; repeatable",
    )
    sweep.add_argument(
        "--source-batch-count",
        type=int,
        default=1,
        help="number of deterministic source batches to process",
    )
    sweep.add_argument(
        "--start-batch-index",
        type=int,
        default=0,
        help="first batch index to process when resuming a sweep",
    )
    sweep.add_argument(
        "--end-batch-index",
        type=int,
        help="last batch index to process when resuming a sweep",
    )
    sweep.add_argument("--tiers", nargs="+", default=["A", "B", "C"])
    sweep.add_argument("--report", action="store_true", help="write a report for every batch")
    sweep.add_argument(
        "--no-commit",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="keep finalize local without creating a Git commit (default: true)",
    )
    sweep.set_defaults(func=command_sweep)
    migrate = subparsers.add_parser("migrate")
    migrate.add_argument("--source", type=Path, required=True, help="legacy unified JSONL source to split")
    migrate.set_defaults(func=command_migrate)
    subparsers.add_parser("curate", help="backfill guide-based reading scope and priority metadata").set_defaults(func=command_curate)
    render = subparsers.add_parser("render")
    render.set_defaults(func=command_render)
    publish = subparsers.add_parser("publish")
    publish.set_defaults(func=command_publish)
    triage = subparsers.add_parser("triage")
    triage.add_argument("--run-id", required=True)
    triage.set_defaults(func=command_triage)
    queue = subparsers.add_parser("queue")
    queue.add_argument("--run-id", required=True)
    queue.add_argument("--tiers", nargs="+", default=["B", "C"])
    queue.set_defaults(func=command_queue)
    subparsers.add_parser("compact").set_defaults(func=command_compact)
    report = subparsers.add_parser("report")
    report.add_argument("--run-id", required=True)
    report.set_defaults(func=command_report)
    subparsers.add_parser("validate").set_defaults(func=command_validate)
    finalize = subparsers.add_parser("finalize")
    finalize.add_argument("--run-id", required=True)
    finalize.add_argument("--no-commit", action="store_true")
    finalize.set_defaults(func=command_finalize)
    subparsers.add_parser("status").set_defaults(func=command_status)
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = build_parser()
    args = parser.parse_args(argv)
    args.root = args.root.resolve()
    args.config = args.config.resolve()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
