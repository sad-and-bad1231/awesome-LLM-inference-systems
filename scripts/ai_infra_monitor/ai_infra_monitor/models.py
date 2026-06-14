from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class Candidate:
    title: str
    url: str
    source_id: str = ""
    source_name: str = ""
    tier: str = "A"
    kind: str = "paper"
    published: str = ""
    discovered: str = ""
    topics: tuple[str, ...] = field(default_factory=tuple)
    summary: str = ""
    venue: str = ""
    identity: str = ""
    fingerprint: str = ""
    update: bool = False

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["topics"] = list(self.topics)
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Candidate":
        values = dict(data)
        values["topics"] = tuple(values.get("topics", ()))
        allowed = cls.__dataclass_fields__
        return cls(**{key: value for key, value in values.items() if key in allowed})
