"""Contract tests for ReentryCompiler."""

import tempfile
from pathlib import Path
from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.packs.project_continuity.models import ProjectTransition, EvidenceAnchor
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler


def test_reentry_compiler_with_fixture():
    """Test deterministic compilation against an isolated fixture."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir(parents=True)
        (projects_dir / "math-reconstruction.md").write_text(
            "# Math Reconstruction\n\n**Purpose:** Rebuild calculus foundation.",
            encoding="utf-8",
        )

        repo = YAMLProjectTransitionRepository(tmp_path)
        repo.add(
            ProjectTransition(
                project_id="project.math-reconstruction",
                recorded_at="2026-07-27T17:30:00Z",
                session_purpose="Test continuity",
                stop_point="Finished the interval construction",
                next_action="Write the contradiction argument",
                open_loops=["Compare supremum proof"],
                evidence_anchors=[EvidenceAnchor(source="textbook.chapter.4", locator="section.4.2")],
            )
        )

        compiler = ReentryCompiler(tmp_path)
        pack = compiler.compile()

        assert pack.project_name == "Math Reconstruction"
        assert pack.latest_transition is not None
        assert "interval construction" in pack.latest_transition.stop_point
        assert "contradiction argument" in pack.latest_transition.next_action

        markdown_out = pack.render_markdown()
        assert "# Re-Entry Pack — Math Reconstruction" in markdown_out
        assert "## 1. Physical Next Action" in markdown_out
        assert "contradiction argument" in markdown_out
        assert "textbook.chapter.4" in markdown_out
