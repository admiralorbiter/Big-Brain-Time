"""Extraction and proposal models for Milestone C2 Conversational Closeout Harness."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Tuple

from bbt.packs.project_continuity.models import SourceSnapshot, ProjectTransition


class FieldStatus(Enum):
    MISSING = "missing"
    EXTRACTED = "extracted"
    USER_SUPPLIED = "user_supplied"
    USER_CONFIRMED = "user_confirmed"
    CONFLICTED = "conflicted"
    UNKNOWN = "unknown"


class ProposalStatus(Enum):
    DRAFT = "draft"
    NEEDS_CLARIFICATION = "needs_clarification"
    READY_FOR_REVIEW = "ready_for_review"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


@dataclass(frozen=True, slots=True)
class TranscriptSpan:
    """Locator span in raw transcript supporting an extracted field."""

    start_char: int
    end_char: int
    text_snippet: str


@dataclass(frozen=True)
class ProposedField:
    """Per-field state with transcript evidence and issue diagnostics."""

    value: Optional[Any]
    status: FieldStatus
    evidence_spans: Tuple[TranscriptSpan, ...] = field(default_factory=tuple)
    issues: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ModelRunMetadata:
    """Provenance metadata for an untrusted model extraction run."""

    provider: str
    model: str
    adapter_version: str
    prompt_contract_version: str
    input_hash: str
    output_hash: str
    started_at: str
    completed_at: str


@dataclass(frozen=True)
class TransitionExtractionRequest:
    """Request payload for model extraction."""

    project_id: str
    transcript: str
    project_context: str


@dataclass(frozen=True)
class ModelExtractionResult:
    """Raw, untrusted field extractions returned by a model provider."""

    raw_fields: Dict[str, Any]
    evidence_spans: Dict[str, List[TranscriptSpan]]
    model_run: ModelRunMetadata
    raw_response_hash: str
    diagnostics: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ProjectTransitionProposal:
    """Domain proposal object constructed by ProposalBuilder from extraction results."""

    schema: str = "bbt.project-transition-proposal/v1"
    proposal_id: str = ""
    project_id: str = ""
    status: ProposalStatus = ProposalStatus.DRAFT

    fields: Dict[str, ProposedField] = field(default_factory=dict)
    missing_required_fields: Tuple[str, ...] = field(default_factory=tuple)
    conflicts: Tuple[str, ...] = field(default_factory=tuple)

    source_snapshot: Optional[SourceSnapshot] = None
    transcript_hash: str = ""
    transcript_retention: str = "ephemeral"
    clarification_count: int = 0
    review_hash: str = ""

    extraction_run: Optional[ModelRunMetadata] = None
    created_at: str = ""
    expires_at: str = ""


@dataclass(frozen=True)
class ProposalAcceptance:
    """Command payload for accepting a proposal card."""

    proposal_id: str
    reviewed_hash: str
    accepted_by: str = "user"


@dataclass(frozen=True)
class AcceptedTransitionResult:
    """Result of executing AcceptTransitionProposal application service."""

    transition: ProjectTransition
    file_path: str
    committed: bool = True
