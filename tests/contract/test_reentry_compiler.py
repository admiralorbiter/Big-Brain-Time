"""Contract tests for ReentryCompiler using domain ports."""

import tempfile
from pathlib import Path

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.adapters.markdown_narrative import MarkdownProjectNarrativeRepository
from bbt.adapters.git_source_state import GitSourceStateProvider
from bbt.adapters.system_clock import SystemClock
from bbt.packs.project_continuity.models import ProjectTransition, EvidenceAnchor, ReentryStatus
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler
from bbt.interfaces.renderers.reentry_markdown import render_reentry_markdown


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

        transitions = YAMLProjectTransitionRepository(tmp_path)
        narratives = MarkdownProjectNarrativeRepository(tmp_path)
        source_state = GitSourceStateProvider(tmp_path)
        clock = SystemClock()

        transitions.add(
            ProjectTransition(
                id="transition.fixture1",
                project_id="project.math-reconstruction",
                recorded_at="2026-07-27T17:30:00Z",
                session_purpose="Test continuity",
                stop_point="Finished the interval construction",
                next_action="Write the contradiction argument",
                open_loops=["Compare supremum proof"],
                evidence_anchors=[EvidenceAnchor(source_id="textbook.chapter.4", relative_path="section.4.2")],
            )
        )

        compiler = ReentryCompiler(
            project_id="project.math-reconstruction",
            transitions=transitions,
            narratives=narratives,
            source_state=source_state,
            clock=clock,
        )
        pack = compiler.compile()

        assert pack.status == ReentryStatus.READY
        assert pack.project_name == "Math Reconstruction"
        assert pack.latest_transition is not None
        assert "interval construction" in pack.latest_transition.stop_point
        assert "contradiction argument" in pack.latest_transition.next_action

        markdown_out = render_reentry_markdown(pack)
        assert "# Re-Entry Pack — Math Reconstruction" in markdown_out
        assert "## 1. Physical Next Action" in markdown_out
        assert "contradiction argument" in markdown_out
        assert "textbook.chapter.4" in markdown_out


def test_no_transition_recorded_status():
    """Verify explicit NO_TRANSITION_RECORDED status when directory is empty."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir(parents=True)
        (projects_dir / "test.md").write_text("# Test Project", encoding="utf-8")

        transitions = YAMLProjectTransitionRepository(tmp_path)
        narratives = MarkdownProjectNarrativeRepository(tmp_path)
        source_state = GitSourceStateProvider(tmp_path)
        clock = SystemClock()

        compiler = ReentryCompiler(
            project_id="project.test",
            transitions=transitions,
            narratives=narratives,
            source_state=source_state,
            clock=clock,
        )
        pack = compiler.compile()

        assert pack.status == ReentryStatus.NO_TRANSITION_RECORDED
        assert pack.latest_transition is None
        markdown_out = render_reentry_markdown(pack)
        assert "No accepted transition record exists" in markdown_out
