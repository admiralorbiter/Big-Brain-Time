"""Unified AcceptTransitionProposal application service for Milestone C2.1."""

from datetime import datetime, timezone
from typing import Optional

from bbt.ports.ports import ProjectTransitionRepository, SourceStateProvider, Clock
from bbt.packs.project_continuity.models import ProjectTransition
from bbt.packs.project_continuity.extraction_models import (
    ProjectTransitionProposal,
    ProposalAcceptance,
    AcceptedTransitionResult,
    ProposalStatus,
    ProposalIdentityMismatch,
    ProposalHashMismatch,
    ProposalNotReviewable,
    ProposalExpired,
    ProposalSourceChanged,
)


class AcceptTransitionProposal:
    """Unified application use case for converting reviewed proposals into canonical transitions."""

    def __init__(
        self,
        repository: ProjectTransitionRepository,
        source_state: Optional[SourceStateProvider] = None,
        clock: Optional[Clock] = None,
    ):
        self.repository = repository
        self.source_state = source_state
        self.clock = clock

    def execute(
        self,
        proposal: ProjectTransitionProposal,
        acceptance: ProposalAcceptance,
    ) -> AcceptedTransitionResult:
        """Validate identity, review hash, expiration, reviewability, and source snapshot before writing."""
        # 1. Identity Check FIRST
        if acceptance.proposal_id != proposal.proposal_id:
            raise ProposalIdentityMismatch(
                f"Proposal ID mismatch! Acceptance specifies '{acceptance.proposal_id}' "
                f"but proposal is '{proposal.proposal_id}'."
            )

        # 2. Review Hash Check
        if acceptance.reviewed_hash != proposal.review_hash:
            raise ProposalHashMismatch(
                f"Proposal hash mismatch! Displayed hash '{acceptance.reviewed_hash}' "
                f"differs from proposal hash '{proposal.review_hash}'."
            )

        # 3. Expiration Check (Clean ISO parsing, no broad try-except swallowing)
        if proposal.expires_at:
            try:
                exp_clean = proposal.expires_at[:-1] + "+00:00" if proposal.expires_at.endswith("Z") else proposal.expires_at
                exp_dt = datetime.fromisoformat(exp_clean)
            except ValueError as exc:
                raise ProposalExpired(f"Proposal has an invalid expiration timestamp '{proposal.expires_at}'.") from exc

            current_now = self.clock.now() if self.clock else datetime.now(timezone.utc)
            if current_now > exp_dt:
                raise ProposalExpired("Proposal has expired and cannot be accepted.")

        # 4. Reviewability & Incomplete Proposal Check
        if not acceptance.allow_incomplete:
            if proposal.status != ProposalStatus.READY_FOR_REVIEW or proposal.missing_required_fields or proposal.conflicts:
                raise ProposalNotReviewable(
                    f"Proposal '{proposal.proposal_id}' is not ready for review. "
                    f"Status: {proposal.status.value}, Missing required: {proposal.missing_required_fields}, Conflicts: {proposal.conflicts}."
                )

        # 5. Source State Revalidation at Acceptance
        if self.source_state and proposal.source_snapshot:
            current_snapshot = self.source_state.snapshot(proposal.project_id)
            if current_snapshot.project_fingerprint != proposal.source_snapshot.project_fingerprint:
                raise ProposalSourceChanged(
                    f"Project source fingerprint changed during review! "
                    f"Reviewed fingerprint '{proposal.source_snapshot.project_fingerprint}', "
                    f"current is '{current_snapshot.project_fingerprint}'."
                )

        # Extract values from proposed fields (NO fake filler content!)
        f = proposal.fields

        session_purpose = str(f["session_purpose"].value) if f.get("session_purpose") and f["session_purpose"].value is not None else ""
        stop_point = str(f["stop_point"].value) if f.get("stop_point") and f["stop_point"].value is not None else ""
        next_action = str(f["next_action"].value) if f.get("next_action") and f["next_action"].value is not None else ""

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

        now_dt = self.clock.now() if self.clock else datetime.now(timezone.utc)
        now_iso = now_dt.isoformat().replace("+00:00", "Z")

        import uuid
        transition_id = f"transition.{uuid.uuid4().hex[:12]}"

        head_rev = proposal.source_snapshot.repository_head if proposal.source_snapshot else "unknown"

        transition = ProjectTransition(
            schema="bbt.project-transition/v1",
            id=transition_id,
            project_id=proposal.project_id,
            recorded_at=now_iso,
            recorded_by=acceptance.accepted_by,
            source_revision=f"git:{head_rev}",
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
