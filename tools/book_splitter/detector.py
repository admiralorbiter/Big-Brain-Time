"""Chapter boundary detection and YAML split plan generation."""

from pathlib import Path
import re
from typing import List, Optional, Dict, Any
import yaml

from tools.book_splitter.models import (
    BookInspectionResult,
    ChapterRange,
    SplitPlan,
)
from tools.book_splitter.inspector import inspect_pdf


def sanitize_id(text: str) -> str:
    """Convert title to clean lowercase slug ID."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "chapter"


def generate_plan_from_bookmarks(inspection: BookInspectionResult) -> SplitPlan:
    """Generate a candidate SplitPlan from level-1 embedded TOC bookmarks."""
    toc = inspection.toc_entries
    book_name = Path(inspection.file_path).stem
    book_id = f"book.{sanitize_id(book_name)}"

    if not toc:
        # Fallback: Single chapter covering whole book
        chapters = (
            ChapterRange(
                chapter_id="full-book",
                title=book_name,
                start_page=0,
                end_page=inspection.total_pages,
                include=True,
            ),
        )
        return SplitPlan(
            schema="bbt.book-split-plan/v1",
            book_id=book_id,
            title=book_name,
            source_path=inspection.file_path,
            source_sha256=inspection.file_sha256,
            chapters=chapters,
        )

    # Filter to Level-1 TOC entries
    level1_entries = [entry for entry in toc if entry[0] == 1]
    if not level1_entries:
        level1_entries = list(toc)

    # Sort level 1 entries by page number
    level1_entries.sort(key=lambda x: x[2])

    chapter_ranges: List[ChapterRange] = []

    # 1. Front Matter (if chapter 1 starts after page 1)
    first_page_1based = level1_entries[0][2]
    if first_page_1based > 1:
        chapter_ranges.append(
            ChapterRange(
                chapter_id="00-front-matter",
                title="Front Matter",
                start_page=0,
                end_page=first_page_1based - 1,  # 0-indexed exclusive
                include=True,
            )
        )

    # 2. Level-1 Chapters
    for i, (level, title, page_1based) in enumerate(level1_entries):
        start_0indexed = max(0, page_1based - 1)

        if i + 1 < len(level1_entries):
            next_page_1based = level1_entries[i + 1][2]
            end_0indexed = max(start_0indexed + 1, next_page_1based - 1)
        else:
            end_0indexed = inspection.total_pages

        chap_slug = sanitize_id(title)
        chap_id = f"{i+1:02d}-{chap_slug}"

        chapter_ranges.append(
            ChapterRange(
                chapter_id=chap_id,
                title=title,
                start_page=start_0indexed,
                end_page=end_0indexed,
                include=True,
            )
        )

    return SplitPlan(
        schema="bbt.book-split-plan/v1",
        book_id=book_id,
        title=book_name,
        source_path=inspection.file_path,
        source_sha256=inspection.file_sha256,
        chapters=tuple(chapter_ranges),
    )


def save_split_plan_yaml(plan: SplitPlan, output_yaml_path: Path) -> None:
    """Save SplitPlan to human-editable 1-indexed inclusive YAML format."""
    dict_repr: Dict[str, Any] = {
        "schema": plan.schema,
        "book": {
            "id": plan.book_id,
            "title": plan.title,
            "source": plan.source_path,
            "source_sha256": plan.source_sha256,
        },
        "page_numbering": {
            "basis": "pdf_index_1based",
            "inclusive": True,
        },
        "chapters": [],
    }

    for ch in plan.chapters:
        dict_repr["chapters"].append(
            {
                "id": ch.chapter_id,
                "title": ch.title,
                "start_page": ch.start_page_1based,
                "end_page": ch.end_page_1based,
                "include": ch.include,
            }
        )

    output_yaml_path = Path(output_yaml_path).resolve()
    output_yaml_path.parent.mkdir(parents=True, exist_ok=True)

    with output_yaml_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(dict_repr, f, sort_keys=False, default_flow_style=False)


def load_split_plan_yaml(yaml_path: Path) -> SplitPlan:
    """Load and parse human-edited 1-indexed inclusive YAML into internal SplitPlan."""
    yaml_path = Path(yaml_path).resolve()
    if not yaml_path.exists():
        raise FileNotFoundError(f"Split plan YAML not found: {yaml_path}")

    with yaml_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML structure in {yaml_path}")

    schema = data.get("schema", "bbt.book-split-plan/v1")
    book_info = data.get("book", {})
    book_id = book_info.get("id", "book.unknown")
    title = book_info.get("title", "Unknown Book")
    source_path = book_info.get("source", "")
    source_sha256 = book_info.get("source_sha256", "")

    chapters_data = data.get("chapters", [])
    chapters: List[ChapterRange] = []

    for cdata in chapters_data:
        start_1based = int(cdata["start_page"])
        end_1based = int(cdata["end_page"])

        start_0indexed = max(0, start_1based - 1)
        end_0indexed = max(start_0indexed, end_1based)

        chapters.append(
            ChapterRange(
                chapter_id=str(cdata["id"]),
                title=str(cdata["title"]),
                start_page=start_0indexed,
                end_page=end_0indexed,
                include=bool(cdata.get("include", True)),
            )
        )

    return SplitPlan(
        schema=schema,
        book_id=book_id,
        title=title,
        source_path=source_path,
        source_sha256=source_sha256,
        chapters=tuple(chapters),
    )
