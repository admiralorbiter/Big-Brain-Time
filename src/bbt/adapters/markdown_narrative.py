"""Markdown adapter for canonical project narrative documents."""

from pathlib import Path
from typing import Optional
import yaml

from bbt.packs.project_continuity.models import NarrativeDocument


class NarrativeNotFoundError(Exception):
    """Raised when canonical narrative document cannot be unambiguously resolved."""
    pass


class AmbiguousNarrativeError(Exception):
    """Raised when multiple unmanifested narrative documents exist."""
    pass


class MarkdownProjectNarrativeRepository:
    """Loads canonical narrative document for a project."""

    def __init__(self, project_root: Path):
        self.project_root = Path(project_root).resolve()

    def get_canonical_narrative(self, project_id: str) -> NarrativeDocument:
        """Find and return canonical narrative document."""
        # 1. Check for explicit project manifest
        manifest_path = self.project_root / "project.manifest.yaml"
        if manifest_path.exists():
            try:
                with manifest_path.open("r", encoding="utf-8") as f:
                    mdata = yaml.safe_load(f)
                if isinstance(mdata, dict):
                    m_id = mdata.get("id")
                    narr_rel = mdata.get("canonical_narrative")
                    if m_id == project_id and narr_rel:
                        narr_path = self.project_root / narr_rel
                        if narr_path.exists():
                            return NarrativeDocument(
                                title=mdata.get("title", narr_path.stem.title()),
                                content=narr_path.read_text(encoding="utf-8"),
                                relative_path=narr_rel,
                            )
            except Exception as e:
                print(f"Warning reading manifest: {e}")

        # 2. Check projects/ directory for matching name
        projects_dir = self.project_root / "projects"
        if projects_dir.exists():
            slug = project_id.replace("project.", "")
            match_file = projects_dir / f"{slug}.md"
            if match_file.exists():
                return NarrativeDocument(
                    title=slug.replace("-", " ").title(),
                    content=match_file.read_text(encoding="utf-8"),
                    relative_path=str(match_file.relative_to(self.project_root)),
                )

            md_files = list(projects_dir.glob("*.md"))
            if len(md_files) == 1:
                target = md_files[0]
                return NarrativeDocument(
                    title=target.stem.replace("-", " ").title(),
                    content=target.read_text(encoding="utf-8"),
                    relative_path=str(target.relative_to(self.project_root)),
                )
            elif len(md_files) > 1:
                raise AmbiguousNarrativeError(
                    f"Multiple project narratives found in {projects_dir}. Add project.manifest.yaml to declare authority."
                )

        # 3. Check root README.md
        readme = self.project_root / "README.md"
        if readme.exists():
            return NarrativeDocument(
                title=self.project_root.name.replace("-", " ").title(),
                content=readme.read_text(encoding="utf-8"),
                relative_path="README.md",
            )

        raise NarrativeNotFoundError(
            f"No canonical narrative document found for project '{project_id}' at {self.project_root}."
        )
