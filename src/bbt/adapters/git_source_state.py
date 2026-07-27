"""Git and SHA-256 source state provider for project fingerprinting."""

import hashlib
from pathlib import Path
import subprocess
from typing import List, Optional, Tuple

from bbt.packs.project_continuity.models import SourceSnapshot, SourceState


class GitSourceStateProvider:
    """Calculates deterministic project fingerprint and git revision status."""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root).resolve()

    def get_git_head(self) -> Optional[str]:
        """Fetch current git commit hash."""
        try:
            res = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=True,
            )
            return res.stdout.strip()
        except Exception:
            return None

    def get_dirty_paths(self) -> Tuple[str, ...]:
        """Fetch list of uncommitted modified files."""
        try:
            res = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=True,
            )
            dirty = []
            for line in res.stdout.splitlines():
                if line.strip():
                    parts = line.strip().split(maxsplit=1)
                    if len(parts) == 2:
                        path_str = parts[1]
                        # Exclude transition records and projections from dirty list
                        if not path_str.startswith(".bbt/"):
                            dirty.append(path_str)
            return tuple(dirty)
        except Exception:
            return ()

    def calculate_project_fingerprint(self) -> str:
        """Compute deterministic SHA-256 hash of project inputs with LF line normalization."""
        hasher = hashlib.sha256()

        # Collect relevant canonical project files
        relevant_files: List[Path] = []

        projects_dir = self.project_root / "projects"
        if projects_dir.exists():
            relevant_files.extend(sorted(projects_dir.glob("*.md")))

        notes_dir = self.project_root / "notes"
        if notes_dir.exists():
            relevant_files.extend(sorted(notes_dir.glob("**/*.md")))

        readme = self.project_root / "README.md"
        if readme.exists():
            relevant_files.append(readme)

        if not relevant_files:
            # Fallback to hashing any non-.bbt markdown file
            relevant_files = sorted(
                [p for p in self.project_root.glob("*.md") if not p.name.startswith(".")]
            )

        for p in relevant_files:
            try:
                rel_path = str(p.relative_to(self.project_root)).replace("\\", "/")
                hasher.update(rel_path.encode("utf-8"))
                
                # Normalize CRLF -> LF for cross-platform fingerprinting
                content_bytes = p.read_bytes()
                normalized_bytes = content_bytes.replace(b"\r\n", b"\n")
                hasher.update(normalized_bytes)
            except Exception:
                pass

        return hasher.hexdigest()[:16]

    def snapshot(self, project_id: str) -> SourceSnapshot:
        """Construct a complete SourceSnapshot for the project."""
        head = self.get_git_head()
        dirty = self.get_dirty_paths()
        fingerprint = self.calculate_project_fingerprint()

        state = SourceState.CURRENT
        if dirty:
            state = SourceState.UNCOMMITTED_PROJECT_CHANGES

        return SourceSnapshot(
            repository_head=head,
            project_fingerprint=fingerprint,
            dirty_paths=dirty,
            state=state,
        )
