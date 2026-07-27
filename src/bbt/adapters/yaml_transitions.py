"""YAML storage adapter for ProjectTransition records."""

from pathlib import Path
from typing import List, Optional
import yaml

from bbt.packs.project_continuity.models import ProjectTransition


class YAMLProjectTransitionRepository:
    """Manages append-only versioned YAML records under .bbt/records/project-transitions/."""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.records_dir = self.project_root / ".bbt" / "records" / "project-transitions"
        self.records_dir.mkdir(parents=True, exist_ok=True)

    def add(self, transition: ProjectTransition) -> Path:
        """Save a new transition record to YAML."""
        if not transition.id:
            import uuid
            transition.id = f"transition.{uuid.uuid4().hex[:12]}"

        target_file = self.records_dir / f"{transition.id}.yaml"
        data = transition.to_dict()

        with open(target_file, "w", encoding="utf-8") as f:
            yaml.dump(data, f, sort_keys=False, default_flow_style=False)

        return target_file

    def get_latest(self) -> Optional[ProjectTransition]:
        """Fetch the latest transition record by file modification time / recorded_at."""
        records = self.list_history()
        if not records:
            return None
        return records[-1]

    def list_history(self) -> List[ProjectTransition]:
        """List all historical transition records sorted by recorded time / filename."""
        if not self.records_dir.exists():
            return []

        yaml_files = sorted(self.records_dir.glob("*.yaml"))
        transitions = []

        for yf in yaml_files:
            try:
                with open(yf, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if isinstance(data, dict):
                        transitions.append(ProjectTransition.from_dict(data))
            except Exception as e:
                print(f"Warning: Failed to parse {yf}: {e}")

        # Sort by recorded_at timestamp if present, otherwise file order
        transitions.sort(key=lambda t: t.recorded_at or t.id)
        return transitions
