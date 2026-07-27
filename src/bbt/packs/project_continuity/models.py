"""Domain models for Project Continuity capability pack."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple


class SourceState(Enum):
    CURRENT = auto()
    REPOSITORY_ADVANCED_PROJECT_UNCHANGED = auto()
    PROJECT_CHANGED = auto()
    UNCOMMITTED_PROJECT_CHANGES = auto()
    SOURCE_STATE_UNKNOWN = auto()


class ReentryStatus(Enum):
    READY = auto()
    NO_TRANSITION_RECORDED = auto()
    DEGRADED = auto()
    STALE = auto()


@dataclass(frozen=True, slots=True)
class SourceSnapshot:
    """Snapshot of source repository state and project fingerprint."""

    repository_head: Optional[str]
    project_fingerprint: str
    dirty_paths: Tuple[str, ...]
    state: SourceState = SourceState.CURRENT


@dataclass(frozen=True, slots=True)
class NarrativeDocument:
    """Canonical project narrative document."""

    title: str
    content: str
    relative_path: str


@dataclass(frozen=True, slots=True)
class TransitionDiagnostic:
    """Diagnostic detail for corrupt or invalid canonical transition files."""

    file_path: str
    message: str
    severity: str = "ERROR"


@dataclass(frozen=True)
class EvidenceAnchor:
    """Verifiable locator reference for source evidence."""

    source_id: str
    relative_path: str
    revision: str = "git:unknown"
    line_start: Optional[int] = None
    line_end: Optional[int] = None
    content_sha256: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "source_id": self.source_id,
            "relative_path": self.relative_path,
            "revision": self.revision,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "content_sha256": self.content_sha256,
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "EvidenceAnchor":
        if not isinstance(d, dict):
            return cls(source_id=str(d), relative_path="")
        return cls(
            source_id=d.get("source_id", d.get("source", "")),
            relative_path=d.get("relative_path", d.get("locator", "")),
            revision=d.get("revision", "git:unknown"),
            line_start=d.get("line_start"),
            line_end=d.get("line_end"),
            content_sha256=d.get("content_sha256"),
        )


@dataclass
class ProjectTransition:
    """Canonical operational record of a project transition/stop point."""

    schema: str = "bbt.project-transition/v1"
    id: str = ""
    project_id: str = ""
    recorded_at: str = ""
    recorded_by: str = ""
    source_revision: str = "git:unknown"
    project_fingerprint: str = ""
    lifecycle: str = "active"
    privacy: str = "private"

    session_purpose: str = ""
    material_changes: List[str] = field(default_factory=list)
    stop_point: str = ""
    next_action: str = ""
    open_loops: List[str] = field(default_factory=list)
    evidence_anchors: List[EvidenceAnchor] = field(default_factory=list)
    protected_commitments: List[str] = field(default_factory=list)
    resumption_warnings: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema": self.schema,
            "id": self.id,
            "project_id": self.project_id,
            "recorded_at": self.recorded_at,
            "recorded_by": self.recorded_by,
            "source_revision": self.source_revision,
            "project_fingerprint": self.project_fingerprint,
            "lifecycle": self.lifecycle,
            "privacy": self.privacy,
            "session": {"purpose": self.session_purpose},
            "transition": {
                "material_changes": self.material_changes,
                "stop_point": self.stop_point,
                "next_action": self.next_action,
                "open_loops": self.open_loops,
                "evidence_anchors": [ea.to_dict() for ea in self.evidence_anchors],
                "protected_commitments": self.protected_commitments,
                "resumption_warnings": self.resumption_warnings,
            },
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProjectTransition":
        session = data.get("session", {})
        transition = data.get("transition", {})
        
        evidence_raw = transition.get("evidence_anchors", transition.get("evidence", []))
        evidence_anchors = [EvidenceAnchor.from_dict(ea) for ea in evidence_raw]

        rec_at = data.get("recorded_at", "")
        if isinstance(rec_at, datetime):
            rec_at = rec_at.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
        else:
            rec_at = str(rec_at)

        return cls(
            schema=data.get("schema", "bbt.project-transition/v1"),
            id=data.get("id", ""),
            project_id=data.get("project_id", ""),
            recorded_at=rec_at,
            recorded_by=data.get("recorded_by", ""),
            source_revision=data.get("source_revision", "git:unknown"),
            project_fingerprint=data.get("project_fingerprint", ""),
            lifecycle=data.get("lifecycle", "active"),
            privacy=data.get("privacy", "private"),
            session_purpose=session.get("purpose", "") if isinstance(session, dict) else str(session),
            material_changes=transition.get("material_changes", []),
            stop_point=transition.get("stop_point", ""),
            next_action=transition.get("next_action", ""),
            open_loops=transition.get("open_loops", []),
            evidence_anchors=evidence_anchors,
            protected_commitments=transition.get("protected_commitments", []),
            resumption_warnings=transition.get("resumption_warnings", []),
        )


@dataclass(frozen=True)
class TransitionReadResult:
    """Result of loading transitions from canonical storage with fail-closed diagnostics."""

    transitions: Tuple[ProjectTransition, ...]
    diagnostics: Tuple[TransitionDiagnostic, ...]
    degraded: bool

    @property
    def latest(self) -> Optional[ProjectTransition]:
        if not self.transitions:
            return None
        return self.transitions[-1]


@dataclass(frozen=True)
class ReentryManifest:
    """Typed manifest for compiled Re-entry Pack."""

    compiler: str
    compiled_at: str
    project_id: str
    git_revision: str
    project_fingerprint: str
    latest_transition_id: Optional[str]
    transition_recorded_at: Optional[str]


@dataclass(frozen=True)
class ReentryPack:
    """Compiled, cited artifact for resuming project work."""

    status: ReentryStatus
    project_name: str
    compiled_at: str
    project_narrative: str
    latest_transition: Optional[ProjectTransition]
    source_snapshot: SourceSnapshot
    manifest: ReentryManifest
    diagnostics: Tuple[TransitionDiagnostic, ...] = field(default_factory=tuple)
