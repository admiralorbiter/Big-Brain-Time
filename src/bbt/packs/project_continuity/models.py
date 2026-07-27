"""Domain models for Project Continuity capability pack."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class EvidenceAnchor:
    """Locator reference for source evidence."""

    source: str
    locator: str

    def to_dict(self) -> Dict[str, str]:
        return {"source": self.source, "locator": self.locator}

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "EvidenceAnchor":
        return cls(source=d.get("source", ""), locator=d.get("locator", ""))


@dataclass
class ProjectTransition:
    """Canonical operational record of a project transition/stop point."""

    schema: str = "bbt.project-transition/v1"
    id: str = ""
    project_id: str = ""
    recorded_at: str = ""
    recorded_by: str = ""
    source_revision: str = "git:unknown"
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
        evidence_anchors = [
            EvidenceAnchor.from_dict(ea) if isinstance(ea, dict) else EvidenceAnchor(source=str(ea), locator="")
            for ea in evidence_raw
        ]

        return cls(
            schema=data.get("schema", "bbt.project-transition/v1"),
            id=data.get("id", ""),
            project_id=data.get("project_id", ""),
            recorded_at=str(data.get("recorded_at", "")) if data.get("recorded_at") else "",
            recorded_by=data.get("recorded_by", ""),
            source_revision=data.get("source_revision", "git:unknown"),
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


@dataclass
class ReentryPack:
    """Compiled, cited artifact for resuming project work."""

    project_name: str
    compiled_at: str
    project_narrative: str
    latest_transition: ProjectTransition
    git_revision: str
    stale_warning: Optional[str] = None
    manifest: Dict[str, Any] = field(default_factory=dict)

    def render_markdown(self) -> str:
        """Render deterministic cited Markdown Re-entry Pack."""
        lines = [
            f"# Re-Entry Pack — {self.project_name}",
            f"*Compiled at: {self.compiled_at} | Git Revision: `{self.git_revision}`*",
            "",
        ]

        if self.stale_warning:
            lines.extend([
                "> [!WARNING]",
                f"> {self.stale_warning}",
                "",
            ])

        lines.extend([
            "## 1. Physical Next Action (Restart Progress Here)",
            f"**Action:** {self.latest_transition.next_action or 'None specified'}",
            "",
            "## 2. Last Known Stop Point",
            f"{self.latest_transition.stop_point or 'None specified'}",
            "",
            "## 3. Session Purpose & Recent Changes",
            f"**Session Purpose:** {self.latest_transition.session_purpose or 'General progress'}",
            "",
            "**Material Changes:**",
        ])

        if self.latest_transition.material_changes:
            for change in self.latest_transition.material_changes:
                lines.append(f"- {change}")
        else:
            lines.append("- No material changes recorded.")

        lines.extend([
            "",
            "## 4. Open Loops & Blockers",
        ])
        if self.latest_transition.open_loops:
            for loop in self.latest_transition.open_loops:
                lines.append(f"- {loop}")
        else:
            lines.append("- No open loops recorded.")

        if self.latest_transition.resumption_warnings:
            lines.extend([
                "",
                "## 5. Resumption Warnings",
            ])
            for warn in self.latest_transition.resumption_warnings:
                lines.append(f"- [WARNING] {warn}")

        if self.latest_transition.evidence_anchors:
            lines.extend([
                "",
                "## 6. Cited Evidence Anchors",
            ])
            for ea in self.latest_transition.evidence_anchors:
                lines.append(f"- `{ea.source}` ({ea.locator})")

        lines.extend([
            "",
            "---",
            "### Project Baseline Narrative",
            self.project_narrative.strip(),
        ])

        return "\n".join(lines)
