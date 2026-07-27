"""Deterministic Re-entry Pack compiler for Project Continuity."""

from datetime import datetime
from pathlib import Path
import subprocess
from typing import Dict, Any, Optional

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.packs.project_continuity.models import ProjectTransition, ReentryPack


class ReentryCompiler:
    """Compiles deterministic, cited Re-entry Packs from local project state."""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root).resolve()
        self.transition_repo = YAMLProjectTransitionRepository(self.project_root)

    def get_git_revision(self) -> str:
        """Fetch current git commit hash if in a git repository."""
        try:
            res = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=True,
            )
            return res.stdout.strip()
        except Exception:
            return "git:uncommitted-or-none"

    def find_project_narrative(self) -> tuple[str, str]:
        """Find primary project narrative markdown file under projects/."""
        projects_dir = self.project_root / "projects"
        if projects_dir.exists():
            md_files = list(projects_dir.glob("*.md"))
            if md_files:
                target = md_files[0]
                return target.stem.replace("-", " ").title(), target.read_text(encoding="utf-8")

        # Fallback to README.md at root
        readme = self.project_root / "README.md"
        if readme.exists():
            return self.project_root.name.replace("-", " ").title(), readme.read_text(encoding="utf-8")

        return self.project_root.name.replace("-", " ").title(), "# Project Baseline\nNo narrative file found."

    def compile(self) -> ReentryPack:
        """Compile a cited Re-entry Pack artifact."""
        project_name, narrative = self.find_project_narrative()
        latest_transition = self.transition_repo.get_latest()

        if not latest_transition:
            latest_transition = ProjectTransition(
                project_id=f"project.{self.project_root.name}",
                session_purpose="Initial baseline registration",
                stop_point="Project workspace initialized.",
                next_action="Review project narrative and record first transition.",
            )

        git_rev = self.get_git_revision()
        now_str = datetime.now().isoformat()

        manifest: Dict[str, Any] = {
            "compiler": "bbt.reentry-compiler/v0.1",
            "compiled_at": now_str,
            "project_root": str(self.project_root),
            "git_revision": git_rev,
            "latest_transition_id": latest_transition.id,
            "transition_recorded_at": latest_transition.recorded_at,
        }

        # Check for potential staleness if transition source_revision differs
        stale_warning: Optional[str] = None
        if latest_transition.source_revision and latest_transition.source_revision != f"git:{git_rev}":
            stale_warning = (
                f"Source code revision has changed since transition was recorded! "
                f"Recorded at `{latest_transition.source_revision}`, current is `{git_rev}`."
            )

        return ReentryPack(
            project_name=project_name,
            compiled_at=now_str,
            project_narrative=narrative,
            latest_transition=latest_transition,
            git_revision=git_rev,
            stale_warning=stale_warning,
            manifest=manifest,
        )
