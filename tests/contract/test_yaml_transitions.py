"""Contract tests for YAMLProjectTransitionRepository."""

import tempfile
from pathlib import Path
from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.packs.project_continuity.models import ProjectTransition, EvidenceAnchor


def test_yaml_roundtrip():
    """Verify that ProjectTransition saves and reloads without loss of meaning."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))

        transition = ProjectTransition(
            project_id="project.test",
            recorded_at="2026-07-27T18:00:00Z",
            session_purpose="Test serialization",
            stop_point="Line 42 of test file",
            next_action="Run pytest",
            open_loops=["Loop 1", "Loop 2"],
            evidence_anchors=[EvidenceAnchor(source="test.md", locator="line 42")],
        )

        saved_path = repo.add(transition)
        assert saved_path.exists()

        latest = repo.get_latest()
        assert latest is not None
        assert latest.project_id == "project.test"
        assert latest.stop_point == "Line 42 of test file"
        assert latest.next_action == "Run pytest"
        assert latest.open_loops == ["Loop 1", "Loop 2"]
        assert len(latest.evidence_anchors) == 1
        assert latest.evidence_anchors[0].source == "test.md"


def test_history_sorting():
    """Verify transitions are returned in temporal order."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))

        t1 = ProjectTransition(recorded_at="2026-07-27T10:00:00Z", stop_point="First")
        t2 = ProjectTransition(recorded_at="2026-07-27T12:00:00Z", stop_point="Second")

        repo.add(t1)
        repo.add(t2)

        history = repo.list_history()
        assert len(history) == 2
        assert history[0].stop_point == "First"
        assert history[1].stop_point == "Second"
        assert repo.get_latest().stop_point == "Second"
