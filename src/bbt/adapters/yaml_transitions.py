"""YAML storage adapter for ProjectTransition records with C1.1 safety invariants."""

import os
from pathlib import Path
import re
from typing import List, Optional, Tuple
from datetime import datetime, timezone
import yaml

from bbt.packs.project_continuity.models import (
    ProjectTransition,
    TransitionReadResult,
    TransitionDiagnostic,
)


TRANSITION_ID_PATTERN = re.compile(r"^transition\.[a-zA-Z0-9_-]+$")
SUPPORTED_SCHEMAS = {"bbt.project-transition/v1"}


class TransitionStorageError(Exception):
    """Base exception for transition storage operations."""
    pass


class InvalidTransitionId(TransitionStorageError):
    """Raised when a transition ID fails pattern or safety validation."""
    pass


class TransitionAlreadyExists(TransitionStorageError):
    """Raised when an attempt is made to overwrite an existing canonical record."""
    pass


def parse_utc_timestamp(ts_str: str) -> Optional[datetime]:
    """Parse ISO 8601 string into a timezone-aware UTC datetime."""
    if not ts_str:
        return None
    try:
        if ts_str.endswith("Z"):
            ts_str = ts_str[:-1] + "+00:00"
        dt = datetime.fromisoformat(ts_str)
        if dt.tzinfo is None:
            # Reject timezone-naive timestamps
            return None
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


class YAMLProjectTransitionRepository:
    """Manages append-only versioned YAML records under .bbt/records/project-transitions/."""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root).resolve()
        self.records_dir = self.project_root / ".bbt" / "records" / "project-transitions"
        self.records_dir.mkdir(parents=True, exist_ok=True)

    def add(self, transition: ProjectTransition) -> str:
        """Save a new transition record using exclusive creation and atomic flush."""
        if not transition.id:
            raise InvalidTransitionId("Transition ID cannot be empty.")

        if not TRANSITION_ID_PATTERN.fullmatch(transition.id):
            raise InvalidTransitionId(
                f"Invalid transition ID '{transition.id}'. Must match pattern ^transition\\.[a-zA-Z0-9_-]+$"
            )

        target_file = self.records_dir / f"{transition.id}.yaml"
        
        # Path safety check
        if not target_file.resolve().is_relative_to(self.records_dir.resolve()):
            raise InvalidTransitionId(f"Path traversal detected in ID '{transition.id}'.")

        data = transition.to_dict()

        try:
            with target_file.open("x", encoding="utf-8") as stream:
                yaml.safe_dump(data, stream, sort_keys=False, default_flow_style=False)
                stream.flush()
                os.fsync(stream.fileno())
        except FileExistsError:
            raise TransitionAlreadyExists(
                f"Canonical transition record '{transition.id}' already exists at {target_file}."
            )
        except Exception as e:
            raise TransitionStorageError(f"Failed to write transition record: {e}") from e

        return str(target_file)

    def read_current(self, project_id: str) -> TransitionReadResult:
        """Read all canonical transitions for a project with fail-closed diagnostics."""
        if not self.records_dir.exists():
            return TransitionReadResult(transitions=(), diagnostics=(), degraded=False)

        yaml_files = sorted(self.records_dir.glob("*.yaml"))
        transitions: List[Tuple[datetime, ProjectTransition]] = []
        diagnostics: List[TransitionDiagnostic] = []
        degraded = False

        for yf in yaml_files:
            rel_path = str(yf.relative_to(self.project_root))
            try:
                with yf.open("r", encoding="utf-8") as stream:
                    data = yaml.safe_load(stream)

                if not isinstance(data, dict):
                    diagnostics.append(
                        TransitionDiagnostic(file_path=rel_path, message="File does not contain a YAML mapping.")
                    )
                    degraded = True
                    continue

                schema = data.get("schema")
                if schema not in SUPPORTED_SCHEMAS:
                    diagnostics.append(
                        TransitionDiagnostic(
                            file_path=rel_path,
                            message=f"Unsupported schema '{schema}'. Expected one of {SUPPORTED_SCHEMAS}.",
                        )
                    )
                    degraded = True
                    continue

                rec_project = data.get("project_id")
                if rec_project and rec_project != project_id:
                    # Belongs to another project — ignore without degrading this project
                    continue

                recorded_at_str = str(data.get("recorded_at", ""))
                dt_instant = parse_utc_timestamp(recorded_at_str)

                if dt_instant is None:
                    diagnostics.append(
                        TransitionDiagnostic(
                            file_path=rel_path,
                            message=f"Invalid or timezone-naive recorded_at timestamp '{recorded_at_str}'. Must be UTC ISO 8601.",
                        )
                    )
                    degraded = True
                    continue

                transition = ProjectTransition.from_dict(data)
                transitions.append((dt_instant, transition))

            except Exception as e:
                diagnostics.append(
                    TransitionDiagnostic(file_path=rel_path, message=f"Failed to parse YAML: {e}")
                )
                degraded = True

        # Sort strictly by UTC instant, then ID for deterministic tie-breaking
        transitions.sort(key=lambda item: (item[0], item[1].id))
        sorted_transitions = tuple(t for _, t in transitions)

        return TransitionReadResult(
            transitions=sorted_transitions,
            diagnostics=tuple(diagnostics),
            degraded=degraded,
        )
