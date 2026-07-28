"""Proposal card presentation renderer for ProjectTransitionProposal."""

from bbt.packs.project_continuity.extraction_models import ProjectTransitionProposal, FieldStatus


def render_proposal_card(proposal: ProjectTransitionProposal) -> str:
    """Render a ProjectTransitionProposal as a formatted proposal card."""
    lines = [
        "--- Proposed Canonical Transition Record (ADR-C02 Proposal Plane) ---",
        f"Proposal ID : {proposal.proposal_id}",
        f"Project ID  : {proposal.project_id}",
        f"Status      : {proposal.status.value.upper()}",
        f"Review Hash : {proposal.review_hash}",
        f"Clarifications Used: {proposal.clarification_count} / 3",
        "---------------------------------------------------------------------",
        "Field Details:",
    ]

    for key, pf in proposal.fields.items():
        val_str = str(pf.value) if pf.value is not None else "[UNSET / UNKNOWN]"
        status_tag = f"[{pf.status.value.upper()}]"
        lines.append(f"  - {key:<18} {status_tag:<18} : {val_str}")
        if pf.evidence_spans:
            for span in pf.evidence_spans:
                lines.append(f"      -> Evidence: \"{span.text_snippet}\"")

    if proposal.missing_required_fields:
        lines.extend([
            "",
            "[WARNING] Missing Required Fields:",
            f"  {', '.join(proposal.missing_required_fields)}",
        ])

    lines.append("---------------------------------------------------------------------\n")
    return "\n".join(lines)
