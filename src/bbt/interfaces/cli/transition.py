"""CLI commands for Project Continuity transitions with unified acceptance service."""

from pathlib import Path
import sys

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.adapters.markdown_narrative import MarkdownProjectNarrativeRepository
from bbt.adapters.git_source_state import GitSourceStateProvider
from bbt.adapters.system_clock import SystemClock
from bbt.adapters.models.fake_transition_extractor import FakeModelInferenceProvider
from bbt.packs.project_continuity.proposal_builder import ProposalBuilder
from bbt.packs.project_continuity.accept_transition import AcceptTransitionProposal
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler
from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ProposalAcceptance,
)
from bbt.interfaces.renderers.reentry_markdown import render_reentry_markdown
from bbt.interfaces.renderers.proposal_renderer import render_proposal_card


def cmd_show(project_path: str) -> None:
    """Compile and display the cited Re-entry Pack for a project."""
    path = Path(project_path).resolve()
    if not path.exists():
        print(f"Error: Project path does not exist: {path}")
        sys.exit(1)

    project_id = f"project.{path.name}"
    transitions = YAMLProjectTransitionRepository(path)
    narratives = MarkdownProjectNarrativeRepository(path)
    source_state = GitSourceStateProvider(path)
    clock = SystemClock()

    compiler = ReentryCompiler(
        project_id=project_id,
        transitions=transitions,
        narratives=narratives,
        source_state=source_state,
        clock=clock,
    )
    pack = compiler.compile()
    print(render_reentry_markdown(pack))


def cmd_record(
    project_path: str,
    stop_point: str = "",
    next_action: str = "",
    purpose: str = "",
    material_changes: str = "",
    open_loops: str = "",
    interactive: bool = True,
    accept: bool = False,
) -> None:
    """Record a new project transition using AcceptTransitionProposal application service."""
    path = Path(project_path).resolve()
    if not path.exists():
        print(f"Error: Project path does not exist: {path}")
        sys.exit(1)

    project_id = f"project.{path.name}"

    if interactive and not (stop_point and next_action):
        print("=== Big Brain Time — Record Project Transition ===")
        purpose = purpose or input("Session purpose [General progress]: ").strip() or "General progress"
        material_changes = material_changes or input("What materially changed / was learned?: ").strip()
        stop_point = stop_point or input("Where did you physically/conceptually stop?: ").strip()
        next_action = next_action or input("What is the single next physical action?: ").strip()
        open_loops = open_loops or input("Open loops / blockers (comma separated): ").strip()

    changes_list = [c.strip() for c in material_changes.split(",") if c.strip()]
    loops_list = [l.strip() for l in open_loops.split(",") if l.strip()]

    scripted_fields = {
        "session_purpose": purpose or "General progress",
        "material_changes": changes_list,
        "stop_point": stop_point or "Work paused.",
        "next_action": next_action or "Review latest progress.",
        "open_loops": loops_list,
    }

    extractor = FakeModelInferenceProvider(scripted_fields=scripted_fields)
    request = TransitionExtractionRequest(
        project_id=project_id,
        transcript="",
        project_context="",
    )
    extraction_result = extractor.extract(request)

    source_state = GitSourceStateProvider(path)
    snapshot = source_state.snapshot(project_id)
    builder = ProposalBuilder()
    proposal = builder.build_proposal(
        project_id=project_id,
        transcript="",
        extraction=extraction_result,
        source_snapshot=snapshot,
    )

    print("\n" + render_proposal_card(proposal))

    if not interactive and not accept:
        print("[PROPOSAL ONLY] Non-interactive mode without --accept. Written 0 files to disk.")
        return

    if interactive:
        confirm = input("Accept and write this canonical transition record? [y/N]: ").strip().lower()
        if confirm != "y":
            print("Operation cancelled. No changes written.")
            return

    repo = YAMLProjectTransitionRepository(path)
    service = AcceptTransitionProposal(repo)
    acceptance = ProposalAcceptance(
        proposal_id=proposal.proposal_id,
        reviewed_hash=proposal.review_hash,
        accepted_by="user",
    )

    result = service.execute(proposal, acceptance)
    print(f"[OK] Canonical transition record written to working tree: {result.file_path}")
