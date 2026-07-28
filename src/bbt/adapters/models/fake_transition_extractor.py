"""FakeModelInferenceProvider test double for deterministic testing."""

import hashlib

from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ModelExtractionResult,
    ModelRunMetadata,
    TranscriptSpan,
)


class FakeModelInferenceProvider:
    """Test double with scripted extraction results for deterministic testing."""

    def __init__(self, scripted_fields: dict = None, diagnostics: tuple = ()):
        self.scripted_fields = scripted_fields or {}
        self.diagnostics = diagnostics

    def extract(self, request: TransitionExtractionRequest) -> ModelExtractionResult:
        inp_hash = hashlib.sha256(request.transcript.encode("utf-8")).hexdigest()[:16]
        meta = ModelRunMetadata(
            provider="fake",
            model="fake-v1",
            adapter_version="0.1.0",
            prompt_contract_version="v1",
            input_hash=inp_hash,
            output_hash="fake_out_hash",
            started_at="2026-07-27T19:00:00Z",
            completed_at="2026-07-27T19:00:01Z",
        )

        spans = {}
        for k, v in self.scripted_fields.items():
            if v and isinstance(v, str):
                spans[k] = [TranscriptSpan(start_char=0, end_char=len(v), text_snippet=v)]

        return ModelExtractionResult(
            raw_fields=self.scripted_fields,
            evidence_spans=spans,
            model_run=meta,
            raw_response_hash="fake_resp_hash",
            diagnostics=self.diagnostics,
        )
