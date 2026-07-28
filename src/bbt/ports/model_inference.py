"""Model inference provider port protocol."""

from typing import Protocol
from bbt.packs.project_continuity.extraction_models import (
    TransitionExtractionRequest,
    ModelExtractionResult,
)


class ModelInferenceProvider(Protocol):
    """Port for untrusted model extraction of candidate transition fields."""

    def extract(self, request: TransitionExtractionRequest) -> ModelExtractionResult: ...
