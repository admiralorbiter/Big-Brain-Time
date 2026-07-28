"""Closeout session repository port protocol for ephemeral interactions."""

from typing import Protocol, Optional
from bbt.packs.project_continuity.closeout_session import CloseoutSession


class CloseoutSessionRepository(Protocol):
    """Port for storing and retrieving ephemeral closeout sessions."""

    def save(self, session: CloseoutSession) -> None: ...
    def get(self, session_id: str) -> Optional[CloseoutSession]: ...
