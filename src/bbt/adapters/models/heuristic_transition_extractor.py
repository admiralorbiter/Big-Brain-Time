"""HeuristicTransitionExtractor rule-based baseline (non-LLM)."""

import hashlib
import re
from typing import Dict, List

from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ModelExtractionResult,
    ModelRunMetadata,
    TranscriptSpan,
)


class HeuristicTransitionExtractor:
    """Rule-based non-LLM extractor baseline using keyword matching and sentence splitters."""

    def extract(self, request: TransitionExtractionRequest) -> ModelExtractionResult:
        text = request.transcript
        sentences = [s.strip() for s in re.split(r"[.!?\n]", text) if s.strip()]

        extracted_fields: Dict[str, any] = {
            "session_purpose": None,
            "material_changes": [],
            "stop_point": None,
            "next_action": None,
            "open_loops": [],
        }

        spans: Dict[str, List[TranscriptSpan]] = {}

        for sentence in sentences:
            s_lower = sentence.lower()
            idx = text.find(sentence)
            span = TranscriptSpan(
                start_char=idx if idx >= 0 else 0,
                end_char=idx + len(sentence) if idx >= 0 else len(sentence),
                text_snippet=sentence,
            )

            # Heuristic keyword matching
            if any(k in s_lower for k in ("stop", "stopped", "stuck", "paused", "finished")):
                if not extracted_fields["stop_point"]:
                    extracted_fields["stop_point"] = sentence
                    spans["stop_point"] = [span]

            if any(k in s_lower for k in ("next", "need to", "action", "should do", "todo")):
                if not extracted_fields["next_action"]:
                    extracted_fields["next_action"] = sentence
                    spans["next_action"] = [span]

            if any(k in s_lower for k in ("learned", "changed", "identified", "decided")):
                extracted_fields["material_changes"].append(sentence)
                spans.setdefault("material_changes", []).append(span)

            if any(k in s_lower for k in ("open", "loop", "blocker", "unresolved", "issue")):
                extracted_fields["open_loops"].append(sentence)
                spans.setdefault("open_loops", []).append(span)

            if any(k in s_lower for k in ("purpose", "working on", "trying to")):
                if not extracted_fields["session_purpose"]:
                    extracted_fields["session_purpose"] = sentence
                    spans["session_purpose"] = [span]

        inp_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
        meta = ModelRunMetadata(
            provider="heuristic",
            model="regex-v1",
            adapter_version="0.1.0",
            prompt_contract_version="v1",
            input_hash=inp_hash,
            output_hash=hashlib.sha256(str(extracted_fields).encode("utf-8")).hexdigest()[:16],
            started_at="2026-07-27T19:00:00Z",
            completed_at="2026-07-27T19:00:00Z",
        )

        return ModelExtractionResult(
            raw_fields=extracted_fields,
            evidence_spans=spans,
            model_run=meta,
            raw_response_hash=meta.output_hash,
            diagnostics=(),
        )
