"""Deterministic proposal builder constructing ProjectTransitionProposal objects."""

import hashlib
import json
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple
import uuid

from bbt.packs.project_continuity.extraction_models import (
    ModelExtractionResult,
    ProjectTransitionProposal,
    ProposedField,
    FieldStatus,
    ProposalStatus,
    TranscriptSpan,
)
from bbt.packs.project_continuity.models import SourceSnapshot

ALLOWED_FIELDS = {
    "session_purpose",
    "material_changes",
    "stop_point",
    "next_action",
    "open_loops",
}

REQUIRED_FIELDS = ("stop_point", "next_action")


class ProposalBuilder:
    """Validates raw extractions and builds typed, review-hashed proposals."""

    def compute_review_hash(self, fields: Dict[str, ProposedField]) -> str:
        """Calculate deterministic hash of displayed proposal fields."""
        serialized = {}
        for k in sorted(fields.keys()):
            pf = fields[k]
            serialized[k] = {
                "value": pf.value,
                "status": pf.status.value,
                "issues": list(pf.issues),
            }
        hasher = hashlib.sha256(json.dumps(serialized, sort_keys=True).encode("utf-8"))
        return hasher.hexdigest()[:16]

    def build_proposal(
        self,
        project_id: str,
        transcript: str,
        extraction: ModelExtractionResult,
        source_snapshot: Optional[SourceSnapshot] = None,
        existing_proposal: Optional[ProjectTransitionProposal] = None,
    ) -> ProjectTransitionProposal:
        """Construct a validated ProjectTransitionProposal from an untrusted extraction."""
        now_dt = datetime.now(timezone.utc)
        now_iso = now_dt.isoformat().replace("+00:00", "Z")
        expires_iso = (now_dt + timedelta(hours=24)).isoformat().replace("+00:00", "Z")

        transcript_hash = hashlib.sha256(transcript.encode("utf-8")).hexdigest()[:16]

        fields: Dict[str, ProposedField] = {}
        missing: List[str] = []
        conflicts: List[str] = []

        # Merge existing fields if updating
        base_fields = existing_proposal.fields if existing_proposal else {}

        for key in ALLOWED_FIELDS:
            if key in base_fields and base_fields[key].status in (FieldStatus.USER_SUPPLIED, FieldStatus.USER_CONFIRMED):
                # Preserve user-confirmed or user-supplied fields
                fields[key] = base_fields[key]
                continue

            raw_val = extraction.raw_fields.get(key)
            spans = extraction.evidence_spans.get(key, [])

            if raw_val is None or (isinstance(raw_val, (list, str)) and not raw_val):
                status = FieldStatus.MISSING
                val = None
                if key in REQUIRED_FIELDS:
                    missing.append(key)
            else:
                status = FieldStatus.EXTRACTED
                val = raw_val

            fields[key] = ProposedField(
                value=val,
                status=status,
                evidence_spans=tuple(spans),
                issues=(),
            )

        review_hash = self.compute_review_hash(fields)

        status = ProposalStatus.READY_FOR_REVIEW if not missing else ProposalStatus.NEEDS_CLARIFICATION

        proposal_id = existing_proposal.proposal_id if existing_proposal else f"proposal.{uuid.uuid4().hex[:12]}"
        clar_count = (existing_proposal.clarification_count + 1) if existing_proposal else 0

        return ProjectTransitionProposal(
            schema="bbt.project-transition-proposal/v1",
            proposal_id=proposal_id,
            project_id=project_id,
            status=status,
            fields=fields,
            missing_required_fields=tuple(missing),
            conflicts=tuple(conflicts),
            source_snapshot=source_snapshot,
            transcript_hash=transcript_hash,
            transcript_retention="ephemeral",
            clarification_count=clar_count,
            review_hash=review_hash,
            extraction_run=extraction.model_run,
            created_at=existing_proposal.created_at if existing_proposal else now_iso,
            expires_at=expires_iso,
        )
