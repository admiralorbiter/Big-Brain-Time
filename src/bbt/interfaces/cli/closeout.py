"""CLI closeout command for Milestone C2.1 Conversational Harness."""

import json
from pathlib import Path
import sys

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.adapters.markdown_narrative import MarkdownProjectNarrativeRepository
from bbt.adapters.git_source_state import GitSourceStateProvider
from bbt.adapters.system_clock import SystemClock
from bbt.adapters.models.heuristic_transition_extractor import HeuristicTransitionExtractor
from bbt.packs.project_continuity.proposal_builder import ProposalBuilder
from bbt.packs.project_continuity.clarification_policy import ClarificationPolicy
from bbt.packs.project_continuity.closeout_session import CloseoutSession
from bbt.packs.project_continuity.accept_transition import AcceptTransitionProposal
from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ProposalAcceptance,
    ProposalStatus,
)
from bbt.interfaces.renderers.proposal_renderer import render_proposal_card


def cmd_closeout(
    project_path: str,
    dump: str = "",
    interactive: bool = True,
    accept: bool = False,
    proposal_only: bool = False,
) -> None:
    """Execute conversational voice/chat closeout workflow."""
    path = Path(project_path).resolve()
    if not path.exists():
        print(f"Error: Project path does not exist: {path}")
        sys.exit(1)

    project_id = f"project.{path.name}"

    if not dump:
        if interactive:
            print("=== Big Brain Time — Conversational Closeout ===")
            dump = input("Tell me about your session (where you stopped, next steps, learnings):\n> ").strip()
        else:
            print("Error: Voice dump text required when running non-interactively (--dump).")
            sys.exit(1)

    if not dump:
        print("Error: Empty session transcript provided.")
        sys.exit(1)

    # 1. Untrusted Model Extraction
    extractor = HeuristicTransitionExtractor()
    narratives = MarkdownProjectNarrativeRepository(path)
    try:
        narrative_doc = narratives.get_canonical_narrative(project_id)
        proj_context = narrative_doc.content
    except Exception:
        proj_context = ""

    request = TransitionExtractionRequest(
        project_id=project_id,
        transcript=dump,
        project_context=proj_context,
    )
    extraction_result = extractor.extract(request)

    # 2. Deterministic Proposal Builder
    source_state = GitSourceStateProvider(path)
    snapshot = source_state.snapshot(project_id)
    builder = ProposalBuilder()
    proposal = builder.build_proposal(
        project_id=project_id,
        transcript=dump,
        extraction=extraction_result,
        source_snapshot=snapshot,
    )

    # 3. Ephemeral Closeout Session
    session = CloseoutSession.create(
        project_id=project_id,
        transcript=dump,
        proposal=proposal,
    )

    # 4. Bounded Follow-Up Policy Engine
    policy = ClarificationPolicy()

    if interactive and proposal.status == ProposalStatus.NEEDS_CLARIFICATION:
        while True:
            question = policy.choose_next_question(proposal)
            if not question:
                break

            print(f"\n💬 Clarification [{proposal.clarification_count + 1} / 3]: {question.prompt}")
            user_answer = input("> ").strip()

            # Record exchange in session state machine
            session.record_exchange(question.target_field, question.prompt, user_answer)

            # Apply user answer directly to proposal without mutating model extraction result
            proposal = builder.apply_user_answer(
                proposal=proposal,
                target_field=question.target_field,
                answer=user_answer,
            )
            session.replace_proposal(proposal)

    # 5. Display Proposal Card Preview
    print("\n" + render_proposal_card(proposal))

    if proposal_only or (not interactive and not accept):
        print("[PROPOSAL ONLY] Non-interactive mode without --accept. Written 0 files to disk.")
        return

    # 6. Solicit Explicit Confirmation
    if interactive:
        confirm = input("Accept and write this canonical transition record? [y/N]: ").strip().lower()
        if confirm != "y":
            session.reject()
            print("Operation cancelled. No changes written.")
            return

    # 7. Unified AcceptTransitionProposal Service
    repo = YAMLProjectTransitionRepository(path)
    clock = SystemClock()
    service = AcceptTransitionProposal(repo, source_state=source_state, clock=clock)

    acceptance = ProposalAcceptance(
        proposal_id=proposal.proposal_id,
        reviewed_hash=proposal.review_hash,
        accepted_by="user",
        allow_incomplete=False,
    )

    result = service.execute(proposal, acceptance)
    session.accept()
    print(f"[OK] Canonical transition record written to working tree: {result.file_path}")
