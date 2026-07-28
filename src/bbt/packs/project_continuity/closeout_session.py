"""Closeout session state machine for ephemeral interactions."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional, Tuple
import uuid

from bbt.packs.project_continuity.extraction_models import (
    ProjectTransitionProposal,
    ProposalStatus,
)


class CloseoutStatus(Enum):
    CAPTURED = "captured"
    NEEDS_CLARIFICATION = "needs_clarification"
    READY_FOR_REVIEW = "ready_for_review"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


@dataclass(frozen=True)
class ClarificationExchange:
    """Record of a single clarification question and user answer."""

    target_field: str
    question_prompt: str
    user_answer: str
    answered_at: str


@dataclass
class CloseoutSession:
    """Ephemeral interaction state machine for closeout voice/chat dumps."""

    session_id: str
    project_id: str
    status: CloseoutStatus
    transcript: str
    proposal: ProjectTransitionProposal
    exchanges: List[ClarificationExchange] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))

    @classmethod
    def create(
        self,
        project_id: str,
        transcript: str,
        proposal: ProjectTransitionProposal,
    ) -> "CloseoutSession":
        session_id = f"session.{uuid.uuid4().hex[:12]}"
        status = (
            CloseoutStatus.READY_FOR_REVIEW
            if proposal.status == ProposalStatus.READY_FOR_REVIEW
            else CloseoutStatus.NEEDS_CLARIFICATION
        )
        return CloseoutSession(
            session_id=session_id,
            project_id=project_id,
            status=status,
            transcript=transcript,
            proposal=proposal,
            exchanges=[],
        )
