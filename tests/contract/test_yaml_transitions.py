"""Contract tests for YAMLProjectTransitionRepository with C1.1 safety invariants."""

import tempfile
from pathlib import Path
import pytest

from bbt.adapters.yaml_transitions import (
    YAMLProjectTransitionRepository,
    TransitionAlreadyExists,
    InvalidTransitionId,
)
from bbt.packs.project_continuity.models import ProjectTransition, EvidenceAnchor


def test_yaml_roundtrip():
    """Verify that ProjectTransition saves and reloads without loss of meaning."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))

        transition = ProjectTransition(
            id="transition.test12345",
            project_id="project.test",
            recorded_at="2026-07-27T18:00:00Z",
            session_purpose="Test serialization",
            stop_point="Line 42 of test file",
            next_action="Run pytest",
            open_loops=["Loop 1", "Loop 2"],
            evidence_anchors=[EvidenceAnchor(source_id="test.md", relative_path="line 42")],
        )

        saved_path = repo.add(transition)
        assert Path(saved_path).exists()

        result = repo.read_current("project.test")
        assert not result.degraded
        latest = result.latest
        assert latest is not None
        assert latest.id == "transition.test12345"
        assert latest.project_id == "project.test"
        assert latest.stop_point == "Line 42 of test file"
        assert latest.next_action == "Run pytest"
        assert latest.open_loops == ["Loop 1", "Loop 2"]
        assert len(latest.evidence_anchors) == 1
        assert latest.evidence_anchors[0].source_id == "test.md"


def test_duplicate_id_rejection():
    """Verify that exclusive creation prevents silent overwrites."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))
        t1 = ProjectTransition(id="transition.duplicate1", project_id="project.test", recorded_at="2026-07-27T18:00:00Z")
        repo.add(t1)

        t2 = ProjectTransition(id="transition.duplicate1", project_id="project.test", recorded_at="2026-07-27T19:00:00Z")
        with pytest.raises(TransitionAlreadyExists):
            repo.add(t2)


def test_invalid_id_path_traversal_rejection():
    """Verify that invalid or path-traversal IDs are rejected."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))
        
        with pytest.raises(InvalidTransitionId):
            repo.add(ProjectTransition(id="../invalid_id", recorded_at="2026-07-27T18:00:00Z"))

        with pytest.raises(InvalidTransitionId):
            repo.add(ProjectTransition(id="transition.bad/slash", recorded_at="2026-07-27T18:00:00Z"))


def test_corrupt_file_degraded_mode():
    """Verify that corrupt YAML files produce fail-closed degraded status."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        repo = YAMLProjectTransitionRepository(tmp_path)

        t1 = ProjectTransition(id="transition.valid1", project_id="project.test", recorded_at="2026-07-27T18:00:00Z")
        repo.add(t1)

        # Inject corrupt YAML record
        corrupt_file = tmp_path / ".bbt" / "records" / "project-transitions" / "transition.corrupt.yaml"
        corrupt_file.write_text("schema: bbt.project-transition/v1\nrecorded_at: INVALID_TIMESTAMP\n", encoding="utf-8")

        result = repo.read_current("project.test")
        assert result.degraded
        assert len(result.diagnostics) >= 1
        assert "Invalid or timezone-naive" in result.diagnostics[0].message


def test_utc_timestamp_instant_sorting():
    """Verify transitions with offsets sort by actual UTC instant."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))

        # 12:00 UTC == 07:00 -05:00
        t1 = ProjectTransition(id="transition.t1", project_id="project.test", recorded_at="2026-07-27T12:00:00Z", stop_point="First")
        # 11:00 UTC == 06:00 -05:00 (Earlier instant)
        t2 = ProjectTransition(id="transition.t2", project_id="project.test", recorded_at="2026-07-27T06:00:00-05:00", stop_point="Second (Earlier)")

        repo.add(t1)
        repo.add(t2)

        result = repo.read_current("project.test")
        assert len(result.transitions) == 2
        assert result.transitions[0].stop_point == "Second (Earlier)"
        assert result.transitions[1].stop_point == "First"
