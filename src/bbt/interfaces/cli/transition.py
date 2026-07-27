"""CLI commands for Project Continuity transitions with C1.1 safety guardrails."""

import json
from pathlib import Path
import sys
import uuid

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.adapters.markdown_narrative import MarkdownProjectNarrativeRepository
from bbt.adapters.git_source_state import GitSourceStateProvider
from bbt.adapters.system_clock import SystemClock
from bbt.packs.project_continuity.models import ProjectTransition
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler
from bbt.interfaces.renderers.reentry_markdown import render_reentry_markdown


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
    """Record a new project transition with explicit human confirmation."""
    path = Path(project_path).resolve()
    if not path.exists():
        print(f"Error: Project path does not exist: {path}")
        sys.exit(1)

    if interactive and not (stop_point and next_action):
        print("=== Big Brain Time — Record Project Transition ===")
        purpose = purpose or input("Session purpose [General progress]: ").strip() or "General progress"
        mat_changes_str = material_changes or input("What materially changed / was learned?: ").strip()
        stop_point = stop_point or input("Where did you physically/conceptually stop?: ").strip()
        next_action = next_action or input("What is the single next physical action?: ").strip()
        open_loops_str = open_loops or input("Open loops / blockers (comma separated): ").strip()
    else:
        mat_changes_str = material_changes
        open_loops_str = open_loops

    changes_list = [c.strip() for c in mat_changes_str.split(",") if c.strip()]
    loops_list = [l.strip() for l in open_loops_str.split(",") if l.strip()]

    clock = SystemClock()
    source_state = GitSourceStateProvider(path)

    snapshot = source_state.snapshot(f"project.{path.name}")
    now_iso = clock.now().isoformat().replace("+00:00", "Z")

    transition_id = f"transition.{uuid.uuid4().hex[:12]}"
    transition = ProjectTransition(
        schema="bbt.project-transition/v1",
        id=transition_id,
        project_id=f"project.{path.name}",
        recorded_at=now_iso,
        recorded_by="user",
        source_revision=f"git:{snapshot.repository_head or 'uncommitted'}",
        project_fingerprint=snapshot.project_fingerprint,
        session_purpose=purpose or "General progress",
        material_changes=changes_list,
        stop_point=stop_point or "Work paused.",
        next_action=next_action or "Review latest progress.",
        open_loops=loops_list,
    )

    print("\n--- Proposed Canonical Transition Record (ADR-C02 Proposal Plane) ---")
    print(json.dumps(transition.to_dict(), indent=2))
    print("---------------------------------------------------------------------\n")

    if not interactive and not accept:
        print("[PROPOSAL ONLY] Non-interactive mode without --accept. Written 0 files to disk.")
        return

    if interactive:
        confirm = input("Accept and write this canonical transition record? [y/N]: ").strip().lower()
        if confirm != "y":
            print("Operation cancelled. No changes written.")
            return

    repo = YAMLProjectTransitionRepository(path)
    saved_path = repo.add(transition)
    print(f"[OK] Canonical transition record written to working tree: {saved_path}")
