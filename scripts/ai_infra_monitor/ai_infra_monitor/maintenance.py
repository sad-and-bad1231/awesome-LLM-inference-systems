from __future__ import annotations

import gzip
import json
import os
import tempfile
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any


TERMINAL_CANDIDATE_STATUSES = {"drop", "promote"}
TERMINAL_STATE_STATUSES = {"processed", "indexed", "suppressed"}


def _record_date(record: dict[str, Any]) -> date | None:
    values = (
        record.get("discovered"),
        record.get("evidence", {}).get("verified_at")
        if isinstance(record.get("evidence"), dict)
        else "",
    )
    for value in values:
        text = str(value or "").strip()
        if not text:
            continue
        try:
            return date.fromisoformat(text[:10])
        except ValueError:
            continue
    return None


def _identity(record: dict[str, Any]) -> str:
    for key in ("canonical_id", "id"):
        value = str(record.get(key, "")).strip()
        if value:
            return value
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _jsonl_bytes(records: list[dict[str, Any]]) -> bytes:
    lines = [
        json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        for record in records
    ]
    return ("\n".join(lines) + ("\n" if lines else "")).encode("utf-8")


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _load_gzip_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    text = gzip.decompress(path.read_bytes()).decode("utf-8")
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def candidate_archive_summary(archive_dir: Path | None) -> list[tuple[Path, int]]:
    """Count archive rows without parsing or returning archived record bodies."""
    if archive_dir is None or not archive_dir.exists():
        return []
    summary: list[tuple[Path, int]] = []
    for path in sorted(archive_dir.glob("candidates-*.jsonl.gz")):
        text = gzip.decompress(path.read_bytes()).decode("utf-8")
        summary.append((path, sum(bool(line.strip()) for line in text.splitlines())))
    return summary


def _atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(handle, "wb") as stream:
            stream.write(payload)
        os.replace(temporary_name, path)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def archive_candidates(
    candidate_path: Path,
    archive_dir: Path,
    hot_window_days: int,
    *,
    hot_terminal_limit: int | None = None,
    today: date | None = None,
) -> dict[str, int]:
    """Move old terminal candidates into deterministic monthly gzip shards."""
    reference_date = today or datetime.now().astimezone().date()
    cutoff = reference_date - timedelta(days=max(0, hot_window_days))
    existing_shards = (
        sorted(archive_dir.glob("candidates-*.jsonl.gz"))
        if archive_dir.exists()
        else []
    )
    archive_contents = {path: _load_gzip_jsonl(path) for path in existing_shards}
    hot: list[dict[str, Any]] = []
    moving: dict[str, list[dict[str, Any]]] = {}
    skipped_undated = 0
    records = _load_jsonl(candidate_path)
    dated_terminal: list[tuple[date, str, int]] = []
    for index, record in enumerate(records):
        record_date = _record_date(record)
        if (
            str(record.get("status", "")) in TERMINAL_CANDIDATE_STATUSES
            and record_date is not None
            and record_date >= cutoff
        ):
            dated_terminal.append((record_date, _identity(record), index))
    keep_recent_indexes = {index for _day, _identity_key, index in dated_terminal}
    if hot_terminal_limit is not None:
        limit = max(0, hot_terminal_limit)
        ranked = sorted(dated_terminal, key=lambda item: (-item[0].toordinal(), item[1]))
        keep_recent_indexes = {index for _day, _identity_key, index in ranked[:limit]}

    for index, record in enumerate(records):
        record_date = _record_date(record)
        is_terminal = str(record.get("status", "")) in TERMINAL_CANDIDATE_STATUSES
        if is_terminal and record_date is None:
            skipped_undated += 1
        should_archive = bool(
            is_terminal
            and record_date is not None
            and (record_date < cutoff or index not in keep_recent_indexes)
        )
        if not should_archive:
            hot.append(record)
            continue
        month = record_date.strftime("%Y-%m")
        moving.setdefault(month, []).append(record)

    changed_shards = 0
    for month, additions in sorted(moving.items()):
        shard = archive_dir / f"candidates-{month}.jsonl.gz"
        merged = {
            _identity(record): record
            for record in archive_contents.get(shard, [])
        }
        for record in additions:
            merged.setdefault(_identity(record), record)
        ordered = [merged[key] for key in sorted(merged)]
        payload = gzip.compress(_jsonl_bytes(ordered), mtime=0)
        if not shard.exists() or shard.read_bytes() != payload:
            _atomic_write(shard, payload)
            changed_shards += 1
        archive_contents[shard] = ordered

    if moving:
        _atomic_write(candidate_path, _jsonl_bytes(hot))

    shard_paths = sorted(archive_contents)
    archive_records = sum(len(records) for records in archive_contents.values())
    return {
        "archived": sum(len(items) for items in moving.values()),
        "hot_records": len(hot),
        "archive_records": archive_records,
        "archive_shards": len(shard_paths),
        "changed_shards": changed_shards,
        "skipped_undated": skipped_undated,
    }


def compact_state_data(
    state: dict[str, Any],
    hot_window_days: int,
    *,
    today: date | None = None,
) -> int:
    """Drop redundant diagnostic fields from old terminal deduplication rows."""
    reference_date = today or datetime.now().astimezone().date()
    cutoff = reference_date - timedelta(days=max(0, hot_window_days))
    changed = 0
    for record in state.get("records", {}).values():
        if str(record.get("status", "")) not in TERMINAL_STATE_STATUSES:
            continue
        try:
            last_seen = date.fromisoformat(str(record.get("last_seen", ""))[:10])
        except ValueError:
            continue
        if last_seen >= cutoff:
            continue
        before = len(record)
        for key in ("title", "url", "run_id"):
            record.pop(key, None)
        if len(record) != before:
            changed += 1
    return changed


def maintain_data(
    candidate_path: Path,
    archive_dir: Path,
    state_path: Path,
    hot_window_days: int,
    *,
    hot_terminal_limit: int | None = None,
    today: date | None = None,
) -> dict[str, int]:
    """Run bounded candidate rotation and local-state compaction."""
    from .state import load_state, save_state

    result = archive_candidates(
        candidate_path,
        archive_dir,
        hot_window_days,
        hot_terminal_limit=hot_terminal_limit,
        today=today,
    )
    state = load_state(state_path)
    state_compacted = compact_state_data(
        state,
        hot_window_days,
        today=today,
    )
    if state_path.exists() or state_compacted:
        save_state(state_path, state)
    result["state_compacted"] = state_compacted
    return result
