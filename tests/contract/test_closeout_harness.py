"""Contract and integration tests for Milestone C2 Conversational Closeout Harness."""

import tempfile
from pathlib import Path
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
    ProposalHashMismatch,
)
from bbt.packs.project_continuity.reentry_compiler import ReentryCompiler
from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ProposalAcceptance,
    FieldStatus,
    ProposalStatus,
)


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


def test_missing_next_action_asks_next_action_question():
    """Verify that a transcript missing next_action prompts for next_action first."""
    with tempfile.TemporaryDirectory() as tmpdir:
        transcript = "I finished proving the upper bound."
        scripted = {
            "session_purpose": "Upper bound proof",
            "stop_point": "Finished proving upper bound",
            "next_action": None,
        }
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        request = TransitionExtractionRequest(project_id="project.test", transcript=transcript, project_context="")
        extraction = extractor.extract(request)

        builder = ProposalBuilder()
        proposal = builder.build_proposal(project_id="project.test", transcript=transcript, extraction=extraction)

        assert proposal.status == ProposalStatus.NEEDS_CLARIFICATION
        assert "next_action" in proposal.missing_required_fields

        policy = ClarificationPolicy()
        question = policy.choose_next_question(proposal)
        assert question is not None
        assert question.target_field == "next_action"


def test_bounded_followup_policy_max_three_questions():
    """Verify that follow-up engine strictly caps questions at 3."""
    with tempfile.TemporaryDirectory() as tmpdir:
        transcript = "Just did some work."
        scripted = {"session_purpose": None, "stop_point": None, "next_action": None}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        request = TransitionExtractionRequest(project_id="project.test", transcript=transcript, project_context="")
        extraction = extractor.extract(request)

        builder = ProposalBuilder()
        proposal = builder.build_proposal(project_id="project.test", transcript=transcript, extraction=extraction)

        policy = ClarificationPolicy()

        # Simulate 3 unanswered questions
        proposal = proposal.__class__(**{**proposal.__dict__, "clarification_count": 3})
        question = policy.choose_next_question(proposal)
        assert question is None


def test_proposal_hash_mismatch_rejection():
    """Verify that AcceptTransitionProposal rejects an altered proposal hash."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        repo = YAMLProjectTransitionRepository(path)
        service = AcceptTransitionProposal(repo)

        transcript = "Finished work. Next do testing."
        scripted = {"stop_point": "Finished work", "next_action": "Do testing"}
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.test", transcript, ""))

        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.test", transcript, extraction)

        invalid_acceptance = ProposalAcceptance(
            proposal_id=proposal.proposal_id,
            reviewed_hash="INVALID_HASH_123",
        )

        with pytest.raises(ProposalHashMismatch):
            service.execute(proposal, invalid_acceptance)


def test_end_to_end_closeout_to_reentry():
    """Verify full path: voice dump -> proposal -> acceptance -> canonical write -> reentry pack."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        (path / "projects").mkdir(parents=True)
        (path / "projects" / "math.md").write_text("# Math Lab\n\n**Purpose:** Analysis.", encoding="utf-8")

        repo = YAMLProjectTransitionRepository(path)
        service = AcceptTransitionProposal(repo)

        transcript = "I completed the IVT theorem proof. Next physical action is to write exercises."
        scripted = {
            "session_purpose": "IVT proof",
            "stop_point": "Completed IVT proof",
            "next_action": "Write exercises",
            "material_changes": ["IVT proof complete"],
        }
        extractor = FakeModelInferenceProvider(scripted_fields=scripted)
        extraction = extractor.extract(TransitionExtractionRequest("project.math", transcript, ""))

        source_state = GitSourceStateProvider(path)
        snapshot = source_state.snapshot("project.math")
        builder = ProposalBuilder()
        proposal = builder.build_proposal("project.math", transcript, extraction, source_snapshot=snapshot)

        acceptance = ProposalAcceptance(
            proposal_id=proposal.proposal_id,
            reviewed_hash=proposal.review_hash,
            accepted_by="user",
        )

        res = service.execute(proposal, acceptance)
        assert res.committed
        assert Path(res.file_path).exists()

        # Re-entry compiler verification
        narratives = MarkdownProjectNarrativeRepository(path)
        clock = SystemClock()
        compiler = ReentryCompiler("project.math", repo, narratives, source_state, clock)
        pack = compiler.compile()

        assert pack.latest_transition is not None
        assert pack.latest_transition.stop_point == "Completed IVT proof"
        assert pack.latest_transition.next_action == "Write exercises"
