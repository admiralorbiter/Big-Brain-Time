"""Extraction and proposal models for Milestone C2.1 Continuity & Closeout Hardening."""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from types import MappingProxyType
from typing import Any, Dict, List, Mapping, Optional, Tuple

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


class ProposalAcceptanceError(Exception):
    """Base exception for proposal acceptance failures."""
    pass


class ProposalIdentityMismatch(ProposalAcceptanceError):
    """Raised when acceptance proposal_id does not match the proposal's ID."""
    pass


class ProposalHashMismatch(ProposalAcceptanceError):
    """Raised when the reviewed hash does not match the proposal's review hash."""
    pass


class ProposalNotReviewable(ProposalAcceptanceError):
    """Raised when an incomplete or conflicted proposal is submitted for acceptance."""
    pass


class ProposalExpired(ProposalAcceptanceError):
    """Raised when an expired proposal is submitted for acceptance."""
    pass


class ProposalSourceChanged(ProposalAcceptanceError):
    """Raised when the underlying project source fingerprint changed during review."""
    pass


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
    """Raw, untrusted field extractions returned by a model provider (immutable)."""

    raw_fields: Mapping[str, Any]
    evidence_spans: Mapping[str, Tuple[TranscriptSpan, ...]]
    model_run: ModelRunMetadata
    raw_response_hash: str
    diagnostics: Tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self):
        # Guarantee immutability of raw_fields mapping
        if isinstance(self.raw_fields, dict):
            object.__setattr__(self, "raw_fields", MappingProxyType(dict(self.raw_fields)))
        if isinstance(self.evidence_spans, dict):
            frozen_spans = {k: tuple(v) for k, v in self.evidence_spans.items()}
            object.__setattr__(self, "evidence_spans", MappingProxyType(frozen_spans))


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
    asked_fields: Tuple[str, ...] = field(default_factory=tuple)
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
    allow_incomplete: bool = False


@dataclass(frozen=True)
class AcceptedTransitionResult:
    """Result of executing AcceptTransitionProposal application service."""

    transition: ProjectTransition
    file_path: str
    committed: bool = True
