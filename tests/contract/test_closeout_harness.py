"""Contract and integration tests for Milestone C2.1 Continuity & Closeout Hardening."""

import tempfile
from pathlib import Path
from datetime import datetime, timedelta, timezone
import pytest

from bbt.adapters.yaml_transitions import YAMLProjectTransitionRepository
from bbt.adapters.markdown_narrative import MarkdownProjectNarrativeRepository
from bbt.adapters.git_source_state import GitSourceStateProvider
from bbt.adapters.system_clock import SystemClock
from bbt.adapters.models.fake_transition_extractor import FakeModelInferenceProvider
from bbt.packs.project_continuity.proposal_builder import ProposalBuilder
from bbt.packs.project_continuity.clarification_policy import ClarificationPolicy
from bbt.packs.project_continuity.closeout_session import CloseoutSession
from bbt.packs.project_continuity.accept_transition import (
    AcceptTransitionProposal,
    ProposalIdentityMismatch,
    ProposalHashMismatch,
    ProposalNotReviewable,
    ProposalExpired,
    ProposalSourceChanged,
)
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler
from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ProposalAcceptance,
    FieldStatus,
    ProposalStatus,
)
from bbt.packs.project_continuity.models import ProjectTransition, ReentryStatus, SourceSnapshot, SourceState


class FakeClock:
    def __init__(self, current_time: datetime):
        self._current_time = current_time

    def now(self) -> datetime:
        return self._current_time


def test_complete_voice_dump_requires_zero_followups():
    """Verify that a complete transcript produces READY_FOR_REVIEW proposal with zero follow-ups."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "projects").mkdir(parents=True)
        (path / "projects" / "test.md").write_text("# Test Project", encoding="utf-8")

        transcript = "I finished the IVT proof on case f(c)>0. Next action is to write the contradiction case f(c)<0."
        scripted = {
            "session_purpose": "IVT proof",
            "stop_point": "Finished IVT proof on case f(c)>0",
            "next_action": "Write contradiction case f(c)<0",
            "material_changes": ["Understood interval completeness"],
        }
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        request = TransitionExtractionRequest(project_id="project.test", transcript=transcript, project_context="")
        extraction = extractor.extract(request)

        builder = ProposalBuilder()
        proposal = builder.build_proposal(project_id="project.test", transcript=transcript, extraction=extraction)

        assert proposal.status == ProposalStatus.READY_FOR_REVIEW
        assert len(proposal.missing_required_fields) == 0

        policy = ClarificationPolicy()
        question = policy.choose_next_question(proposal)
        assert question is None


def test_blank_answer_consumes_followup_budget():
    """Verify that submitting blank answers increments clarification_count and sets FieldStatus.UNKNOWN without infinite looping."""
    with tempfile.TemporaryDirectory() as tmpdir:
        transcript = "Just worked a bit."
        scripted = {"session_purpose": "Work", "stop_point": None, "next_action": None}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.test", transcript, ""))

        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.test", transcript, extraction)

        policy = ClarificationPolicy()
        q1 = policy.choose_next_question(proposal)
        assert q1 is not None
        assert q1.target_field == "next_action"

        # Apply blank answer
        proposal = builder.apply_user_answer(proposal, q1.target_field, "")
        assert proposal.clarification_count == 1
        assert proposal.fields["next_action"].status == FieldStatus.UNKNOWN
        assert proposal.fields["next_action"].value is None

        # Next question should be stop_point, NOT next_action again!
        q2 = policy.choose_next_question(proposal)
        assert q2 is not None
        assert q2.target_field == "stop_point"

        # Apply second blank answer
        proposal = builder.apply_user_answer(proposal, q2.target_field, "")
        assert proposal.clarification_count == 2
        assert proposal.fields["stop_point"].status == FieldStatus.UNKNOWN

        # Budget consumed / asked_fields full -> returns None
        q3 = policy.choose_next_question(proposal)
        assert q3 is None


def test_user_answer_remains_user_supplied():
    """Verify user answers are labeled USER_SUPPLIED without mutating model extraction result."""
    with tempfile.TemporaryDirectory() as tmpdir:
        transcript = "Worked on analysis."
        scripted = {"stop_point": "Finished lemma 1", "next_action": None}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.test", transcript, ""))

        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.test", transcript, extraction)

        # Apply user answer
        proposal = builder.apply_user_answer(proposal, "next_action", "Write lemma 2")
        assert proposal.fields["next_action"].status == FieldStatus.USER_SUPPLIED
        assert proposal.fields["next_action"].value == "Write lemma 2"

        # Verify model extraction result was NOT mutated
        assert extraction.raw_fields["next_action"] is None


def test_wrong_proposal_id_is_rejected():
    """Verify proposal ID mismatch raises ProposalIdentityMismatch FIRST."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))
        service = AcceptTransitionProposal(repo)

        transcript = "Finished work. Next do testing."
        scripted = {"stop_point": "Finished work", "next_action": "Do testing"}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.test", transcript, ""))

        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.test", transcript, extraction)

        acceptance = ProposalAcceptance(
            proposal_id="proposal.WRONG_ID",
            reviewed_hash=proposal.review_hash,
        )

        with pytest.raises(ProposalIdentityMismatch):
            service.execute(proposal, acceptance)


def test_incomplete_proposal_is_rejected():
    """Verify that accepting an incomplete proposal raises ProposalNotReviewable."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))
        service = AcceptTransitionProposal(repo)

        transcript = "Finished work."
        scripted = {"stop_point": "Finished work", "next_action": None}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.test", transcript, ""))

        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.test", transcript, extraction)
        assert proposal.status == ProposalStatus.NEEDS_CLARIFICATION

        acceptance = ProposalAcceptance(
            proposal_id=proposal.proposal_id,
            reviewed_hash=proposal.review_hash,
        )

        with pytest.raises(ProposalNotReviewable):
            service.execute(proposal, acceptance)


def test_expired_proposal_is_rejected():
    """Verify that expired proposals are rejected cleanly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo = YAMLProjectTransitionRepository(Path(tmpdir))
        past_time = datetime.now(timezone.utc) - timedelta(hours=48)
        future_clock = FakeClock(datetime.now(timezone.utc))

        service = AcceptTransitionProposal(repo, clock=future_clock)

        transcript = "Finished work. Next do testing."
        scripted = {"stop_point": "Finished work", "next_action": "Do testing"}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.test", transcript, ""))

        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.test", transcript, extraction)
        
        # Override expiration to past
        proposal = proposal.__class__(**{**proposal.__dict__, "expires_at": past_time.isoformat().replace("+00:00", "Z")})

        acceptance = ProposalAcceptance(
            proposal_id=proposal.proposal_id,
            reviewed_hash=proposal.review_hash,
        )

        with pytest.raises(ProposalExpired):
            service.execute(proposal, acceptance)


def test_committed_project_change_marks_reentry_stale():
    """Verify that changing project fingerprint marks ReentryStatus STALE even when working tree is clean."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "projects").mkdir(parents=True)
        narrative_file = path / "projects" / "test.md"
        narrative_file.write_text("# Test Project v1", encoding="utf-8")

        transitions = YAMLProjectTransitionRepository(path)
        narratives = MarkdownProjectNarrativeRepository(path)
        source_state = GitSourceStateProvider(path)
        clock = SystemClock()

        # Record transition with current fingerprint
        snap1 = source_state.snapshot("project.test")
        t1 = ProjectTransition(
            id="transition.t1",
            project_id="project.test",
            recorded_at="2026-07-27T18:00:00Z",
            stop_point="Step 1",
            next_action="Step 2",
            project_fingerprint=snap1.project_fingerprint,
        )
        transitions.add(t1)

        compiler = ReentryCompiler("project.test", transitions, narratives, source_state, clock)
        pack1 = compiler.compile()
        assert pack1.status == ReentryStatus.READY

        # Modify project narrative (committed project change)
        narrative_file.write_text("# Test Project v2 — Material Narrative Edit", encoding="utf-8")

        pack2 = compiler.compile()
        assert pack2.status == ReentryStatus.STALE
        assert pack2.source_snapshot.state == SourceState.PROJECT_CHANGED


def test_retracted_transition_is_not_current():
    """Verify that retracted transitions are ignored in favor of active ones."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        repo = YAMLProjectTransitionRepository(path)

        t1 = ProjectTransition(id="transition.t1", project_id="project.test", recorded_at="2026-07-27T10:00:00Z", stop_point="Active 1")
        t2 = ProjectTransition(id="transition.t2", project_id="project.test", recorded_at="2026-07-27T12:00:00Z", stop_point="Retracted 2", lifecycle="retracted")

        repo.add(t1)
        repo.add(t2)

        result = repo.read_current("project.test")
        assert len(result.transitions) == 1
        assert result.latest.stop_point == "Active 1"
