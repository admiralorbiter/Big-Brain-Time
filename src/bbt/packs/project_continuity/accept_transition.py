"""Unified AcceptTransitionProposal application service."""

from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from bbt.ports.ports import ProjectTransitionRepository
from bbt.packs.project_continuity.models import ProjectTransition
from bbt.packs.project_continuity.extraction_models import (
    ProjectTransitionProposal,
    ProposalAcceptance,
    AcceptedTransitionResult,
    ProposalStatus,
    FieldStatus,
)


class ProposalAcceptanceError(Exception):
    """Base exception for proposal acceptance failures."""
    pass


class ProposalHashMismatch(ProposalAcceptanceError):
    """Raised when the reviewed hash does not match the proposal's review hash."""
    pass


class ProposalExpired(ProposalAcceptanceError):
    """Raised when an expired proposal is submitted for acceptance."""
    pass


class AcceptTransitionProposal:
    """Unified application use case for converting reviewed proposals into canonical transitions."""

    def __init__(self, repository: ProjectTransitionRepository):
        self.repository = repository

    def execute(
        self,
        proposal: ProjectTransitionProposal,
        acceptance: ProposalAcceptance,
    ) -> AcceptedTransitionResult:
        """Validate review hash and commit canonical ProjectTransition record."""
        if acceptance.reviewed_hash != proposal.review_hash:
            raise ProposalHashMismatch(
                f"Proposal hash mismatch! Displayed hash '{acceptance.reviewed_hash}' "
                f"differs from proposal hash '{proposal.review_hash}'."
            )

        if proposal.expires_at:
            try:
                exp_dt = datetime.fromisoformat(proposal.expires_at.replace("Z", "+00:00"))
                if datetime.now(timezone.utc) > exp_dt:
                    raise ProposalExpired("Proposal has expired and cannot be accepted.")
            except Exception:
                pass

        # Extract values from proposed fields
        f = proposal.fields

        session_purpose = str(f["session_purpose"].value) if f.get("session_purpose") and f["session_purpose"].value else "General progress"
        stop_point = str(f["stop_point"].value) if f.get("stop_point") and f["stop_point"].value else "Work paused."
        next_action = str(f["next_action"].value) if f.get("next_action") and f["next_action"].value else "Review latest progress."

        mat_changes_val = f["material_changes"].value if f.get("material_changes") else []
        if isinstance(mat_changes_val, str):
            material_changes = [mat_changes_val]
        elif isinstance(mat_changes_val, list):
            material_changes = [str(x) for x in mat_changes_val]
        else:
            material_changes = []

        open_loops_val = f["open_loops"].value if f.get("open_loops") else []
        if isinstance(open_loops_val, str):
            open_loops = [open_loops_val]
        elif isinstance(open_loops_val, list):
            open_loops = [str(x) for x in open_loops_val]
        else:
            open_loops = []

        now_iso = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        # Generate canonical ProjectTransition ID
        import uuid
        transition_id = f"transition.{uuid.uuid4().hex[:12]}"

        transition = ProjectTransition(
            schema="bbt.project-transition/v1",
            id=transition_id,
            project_id=proposal.project_id,
            recorded_at=now_iso,
            recorded_by=acceptance.accepted_by,
            source_revision=f"git:{proposal.source_snapshot.repository_head}" if proposal.source_snapshot and proposal.source_snapshot.repository_head else "git:unknown",
            project_fingerprint=proposal.source_snapshot.project_fingerprint if proposal.source_snapshot else "",
            lifecycle="active",
            privacy="private",
            session_purpose=session_purpose,
            material_changes=material_changes,
            stop_point=stop_point,
            next_action=next_action,
            open_loops=open_loops,
        )

        saved_path = self.repository.add(transition)

        return AcceptedTransitionResult(
            transition=transition,
            file_path=saved_path,
            committed=True,
        )
