"""Deterministic clarification policy for bounded follow-up questions."""

from dataclasses import dataclass
from typing import Optional, Tuple
from bbt.packs.project_continuity.extraction_models import (
    ProjectTransitionProposal,
    FieldStatus,
)


@dataclass(frozen=True)
class ClarificationQuestion:
    """Targeted follow-up question for missing proposal fields."""

    target_field: str
    prompt: str
    priority: int


class ClarificationPolicy:
    """Enforces Bounded Follow-Up Policy with a hard cap of max 3 questions."""

    MAX_FOLLOWUPS = 3

    # Re-entry value priorities (1 = highest priority)
    FIELD_PROMPTS = [
        ("next_action", "What is the single next physical action to restart progress?", 1),
        ("stop_point", "Where did you physically or conceptually stop?", 2),
    ]

    def choose_next_question(
        self,
        proposal: ProjectTransitionProposal,
    ) -> Optional[ClarificationQuestion]:
        """Select the highest-priority missing question if follow-up budget remains."""
        if proposal.clarification_count >= self.MAX_FOLLOWUPS:
            # Hard cap reached — return None to stop asking questions
            return None

        for field_name, prompt_text, priority in self.FIELD_PROMPTS:
            pf = proposal.fields.get(field_name)
            if pf is None or pf.status in (FieldStatus.MISSING, FieldStatus.UNKNOWN) or pf.value is None:
                return ClarificationQuestion(
                    target_field=field_name,
                    prompt=prompt_text,
                    priority=priority,
                )

        return None
