from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import date
from pathlib import Path

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
    append_candidates,
    load_manifest,
    write_weekly_report,
)
from scripts.ai_infra_monitor.ai_infra_monitor.state import (  # noqa: E402
    load_state,
    save_state,
)
from scripts.ai_infra_monitor.ai_infra_monitor.validation import (  # noqa: E402
    validate_workspace,
)


ROOT = Path(__file__).resolve().parents[2]


def paths(root: Path, config: dict) -> dict[str, Path]:
    settings = config["settings"]
    return {
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


def manifest_path(root: Path, config: dict, run_id: str) -> Path:
    return paths(root, config)["runs_dir"] / run_id / "candidates.json"


def command_init(args) -> int:
    config = load_config(args.config)
    resolved = paths(args.root, config)
    resolved["runs_dir"].mkdir(parents=True, exist_ok=True)
    resolved["weekly_reports_dir"].mkdir(parents=True, exist_ok=True)
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
    manifest = DiscoveryEngine(args.root, args.config).discover(args.mode)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


def command_queue(args) -> int:
    config = load_config(args.config)
    manifest = load_manifest(manifest_path(args.root, config, args.run_id))
    selected = [
        Candidate.from_dict(item)
        for item in manifest["candidates"]
        if item.get("tier") in set(args.tiers)
    ]
    count = append_candidates(paths(args.root, config)["candidate_file"], selected)
    print(json.dumps({"queued": count, "run_id": args.run_id}))
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
        resolved["paper_file"], resolved["industry_file"], resolved["candidate_file"]
    )
    if errors:
        for error in errors:
            print(f"{error.path}:{error.line}: {error.message}", file=sys.stderr)
        return 1
    print("validation passed")
    return 0


def command_finalize(args) -> int:
    if command_validate(args):
        return 1
    config = load_config(args.config)
    resolved = paths(args.root, config)
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
            resolved["paper_file"],
            resolved["industry_file"],
            resolved["candidate_file"],
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
    discover.set_defaults(func=command_discover)
    queue = subparsers.add_parser("queue")
    queue.add_argument("--run-id", required=True)
    queue.add_argument("--tiers", nargs="+", default=["B", "C"])
    queue.set_defaults(func=command_queue)
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
    parser = build_parser()
    args = parser.parse_args(argv)
    args.root = args.root.resolve()
    args.config = args.config.resolve()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
