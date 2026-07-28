"""Deterministic proposal builder constructing and updating ProjectTransitionProposal objects."""

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

    def compute_review_hash(
        self,
        schema: str,
        proposal_id: str,
        project_id: str,
        fields: Dict[str, ProposedField],
        missing_required: Tuple[str, ...],
        conflicts: Tuple[str, ...],
        fingerprint: str,
    ) -> str:
        """Calculate comprehensive deterministic hash of displayed proposal fields & context."""
        serialized_fields = {}
        for k in sorted(fields.keys()):
            pf = fields[k]
            serialized_fields[k] = {
                "value": pf.value,
                "status": pf.status.value,
                "issues": list(pf.issues),
            }

        payload = {
            "schema": schema,
            "proposal_id": proposal_id,
            "project_id": project_id,
            "fields": serialized_fields,
            "missing_required_fields": list(missing_required),
            "conflicts": list(conflicts),
            "project_fingerprint": fingerprint,
        }
        hasher = hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8"))
        return hasher.hexdigest()

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

        # Preserve original expiration if updating existing proposal
        if existing_proposal and existing_proposal.expires_at:
            expires_iso = existing_proposal.expires_at
        else:
            expires_iso = (now_dt + timedelta(hours=24)).isoformat().replace("+00:00", "Z")

        transcript_hash = hashlib.sha256(transcript.encode("utf-8")).hexdigest()[:16]

        fields: Dict[str, ProposedField] = {}
        missing: List[str] = []
        conflicts: List[str] = []

        base_fields = existing_proposal.fields if existing_proposal else {}

        for key in ALLOWED_FIELDS:
            if key in base_fields and base_fields[key].status in (FieldStatus.USER_SUPPLIED, FieldStatus.USER_CONFIRMED, FieldStatus.UNKNOWN):
                fields[key] = base_fields[key]
                if key in REQUIRED_FIELDS and (base_fields[key].value is None or base_fields[key].status == FieldStatus.UNKNOWN):
                    missing.append(key)
                continue

            raw_val = extraction.raw_fields.get(key)
            spans = extraction.evidence_spans.get(key, ())

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

        proposal_id = existing_proposal.proposal_id if existing_proposal else f"proposal.{uuid.uuid4().hex[:12]}"
        fp = source_snapshot.project_fingerprint if source_snapshot else ""
        schema = "bbt.project-transition-proposal/v1"

        missing_tuple = tuple(missing)
        conflicts_tuple = tuple(conflicts)

        review_hash = self.compute_review_hash(
            schema=schema,
            proposal_id=proposal_id,
            project_id=project_id,
            fields=fields,
            missing_required=missing_tuple,
            conflicts=conflicts_tuple,
            fingerprint=fp,
        )

        status = ProposalStatus.READY_FOR_REVIEW if not missing else ProposalStatus.NEEDS_CLARIFICATION
        clar_count = existing_proposal.clarification_count if existing_proposal else 0
        asked_fields = existing_proposal.asked_fields if existing_proposal else ()

        return ProjectTransitionProposal(
            schema=schema,
            proposal_id=proposal_id,
            project_id=project_id,
            status=status,
            fields=fields,
            missing_required_fields=missing_tuple,
            conflicts=conflicts_tuple,
            source_snapshot=source_snapshot,
            transcript_hash=transcript_hash,
            transcript_retention="ephemeral",
            clarification_count=clar_count,
            asked_fields=asked_fields,
            review_hash=review_hash,
            extraction_run=extraction.model_run,
            created_at=existing_proposal.created_at if existing_proposal else now_iso,
            expires_at=expires_iso,
        )

    def apply_user_answer(
        self,
        proposal: ProjectTransitionProposal,
        target_field: str,
        answer: Optional[str],
    ) -> ProjectTransitionProposal:
        """Apply a user clarification answer without mutating model extraction results."""
        if target_field not in ALLOWED_FIELDS:
            return proposal

        new_fields = dict(proposal.fields)
        clean_ans = answer.strip() if answer else None

        if clean_ans:
            new_fields[target_field] = ProposedField(
                value=clean_ans,
                status=FieldStatus.USER_SUPPLIED,
                evidence_spans=(),
                issues=(),
            )
        else:
            # User skipped / blank answer -> set status UNKNOWN, value None (no fake filler text!)
            new_fields[target_field] = ProposedField(
                value=None,
                status=FieldStatus.UNKNOWN,
                evidence_spans=(),
                issues=(),
            )

        new_missing: List[str] = []
        for req in REQUIRED_FIELDS:
            pf = new_fields.get(req)
            if pf is None or pf.value is None or pf.status in (FieldStatus.MISSING, FieldStatus.UNKNOWN):
                new_missing.append(req)

        missing_tuple = tuple(new_missing)
        fp = proposal.source_snapshot.project_fingerprint if proposal.source_snapshot else ""

        review_hash = self.compute_review_hash(
            schema=proposal.schema,
            proposal_id=proposal.proposal_id,
            project_id=proposal.project_id,
            fields=new_fields,
            missing_required=missing_tuple,
            conflicts=proposal.conflicts,
            fingerprint=fp,
        )

        status = ProposalStatus.READY_FOR_REVIEW if not new_missing else ProposalStatus.NEEDS_CLARIFICATION
        new_asked = tuple(list(proposal.asked_fields) + [target_field]) if target_field not in proposal.asked_fields else proposal.asked_fields

        return ProjectTransitionProposal(
            schema=proposal.schema,
            proposal_id=proposal.proposal_id,
            project_id=proposal.project_id,
            status=status,
            fields=new_fields,
            missing_required_fields=missing_tuple,
            conflicts=proposal.conflicts,
            source_snapshot=proposal.source_snapshot,
            transcript_hash=proposal.transcript_hash,
            transcript_retention=proposal.transcript_retention,
            clarification_count=proposal.clarification_count + 1,
            asked_fields=new_asked,
            review_hash=review_hash,
            extraction_run=proposal.extraction_run,
            created_at=proposal.created_at,
            expires_at=proposal.expires_at,
        )
