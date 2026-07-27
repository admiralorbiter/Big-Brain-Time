"""System clock adapter returning timezone-aware UTC datetime."""

from datetime import datetime, timezone


class SystemClock:
    """Returns current UTC time."""

    def now(self) -> datetime:
        return datetime.now(timezone.utc)
