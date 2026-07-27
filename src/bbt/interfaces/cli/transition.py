"""CLI commands for Project Continuity transitions."""

from datetime import datetime
from pathlib import Path
import sys

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.packs.project_continuity.models import ProjectTransition
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler


def cmd_show(project_path: str) -> None:
    """Compile and display the cited Re-entry Pack for a project."""
    path = Path(project_path).resolve()
    if not path.exists():
        print(f"Error: Project path does not exist: {path}")
        sys.exit(1)

    compiler = ReentryCompiler(path)
    pack = compiler.compile()
    print(pack.render_markdown())


def cmd_record(
    project_path: str,
    stop_point: str = "",
    next_action: str = "",
    purpose: str = "",
    open_loops: str = "",
    interactive: bool = True,
) -> None:
    """Record a new project transition with explicit human confirmation."""
    path = Path(project_path).resolve()
    if not path.exists():
        print(f"Error: Project path does not exist: {path}")
        sys.exit(1)

    if interactive and not (stop_point and next_action):
        print("=== Big Brain Time — Record Project Transition ===")
        purpose = purpose or input("Session purpose [General progress]: ").strip() or "General progress"
        stop_point = stop_point or input("Where did you physically/conceptually stop?: ").strip()
        next_action = next_action or input("What is the single next physical action?: ").strip()
        open_loops_str = open_loops or input("Open loops / blockers (comma separated): ").strip()
    else:
        open_loops_str = open_loops

    loops_list = [l.strip() for l in open_loops_str.split(",") if l.strip()]

    compiler = ReentryCompiler(path)
    git_rev = compiler.get_git_revision()
    now_str = datetime.now().isoformat()

    transition = ProjectTransition(
        project_id=f"project.{path.name}",
        recorded_at=now_str,
        recorded_by="user",
        source_revision=f"git:{git_rev}",
        session_purpose=purpose or "General progress",
        stop_point=stop_point or "Work paused.",
        next_action=next_action or "Review latest progress.",
        open_loops=loops_list,
    )

    print("\n--- Proposed Canonical Transition Record (ADR-C02 Proposal Plane) ---")
    print(f"Project ID: {transition.project_id}")
    print(f"Recorded At: {transition.recorded_at}")
    print(f"Stop Point: {transition.stop_point}")
    print(f"Next Action: {transition.next_action}")
    print(f"Open Loops: {transition.open_loops}")
    print("---------------------------------------------------------------------\n")

    if interactive:
        confirm = input("Accept and save this canonical transition record? [Y/n]: ").strip().lower()
        if confirm and confirm not in ("y", "yes"):
            print("Operation cancelled. No changes written.")
            return

    repo = YAMLProjectTransitionRepository(path)
    saved_path = repo.add(transition)
    print(f"[OK] Canonical transition record committed to: {saved_path}")
