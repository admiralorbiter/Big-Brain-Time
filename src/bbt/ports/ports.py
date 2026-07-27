"""Core domain ports (protocols) for Big Brain Time."""

from datetime import datetime
from typing import Protocol, Tuple
from bbt.packs.project_continuity.models import (
    ProjectTransition,
    TransitionReadResult,
    SourceSnapshot,
    NarrativeDocument,
)


class ProjectTransitionRepository(Protocol):
    """Port for storing and retrieving canonical ProjectTransition records."""

    def add(self, transition: ProjectTransition) -> str: ...
    def read_current(self, project_id: str) -> TransitionReadResult: ...


class ProjectNarrativeRepository(Protocol):
    """Port for retrieving canonical project purpose and narrative documents."""

    def get_canonical_narrative(self, project_id: str) -> NarrativeDocument: ...


class SourceStateProvider(Protocol):
    """Port for calculating source snapshots, fingerprints, and uncommitted changes."""

    def snapshot(self, project_id: str) -> SourceSnapshot: ...


class Clock(Protocol):
    """Port for system time."""

    def now(self) -> datetime: ...
