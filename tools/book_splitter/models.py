"""Domain models for book inspection, split planning, and artifact generation."""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class ChapterRange:
    """Internal half-open range [start_page, end_page) represented 0-indexed internally."""

    chapter_id: str
    title: str
    start_page: int  # 0-indexed, inclusive
    end_page: int    # 0-indexed, exclusive
    include: bool = True

    @property
    def page_count(self) -> int:
        return max(0, self.end_page - self.start_page)

    @property
    def start_page_1based(self) -> int:
        return self.start_page + 1

    @property
    def end_page_1based(self) -> int:
        return self.end_page  # exclusive 0-indexed == inclusive 1-indexed end page


@dataclass(frozen=True)
class SplitPlan:
    """Structured plan for splitting a source PDF into chapter files."""

    schema: str
    book_id: str
    title: str
    source_path: str
    source_sha256: str
    chapters: Tuple[ChapterRange, ...]


@dataclass(frozen=True)
class ChapterArtifact:
    """Metadata for an exported chapter PDF & text artifact."""

    chapter_id: str
    title: str
    pdf_output_path: str
    text_output_path: str
    start_page_1based: int
    end_page_1based: int
    page_count: int
    pdf_sha256: str


@dataclass(frozen=True)
class BookInspectionResult:
    """Inspection summary for a source PDF file."""

    file_path: str
    file_sha256: str
    total_pages: int
    text_readable_pages: int
    embedded_bookmarks: int
    toc_entries: Tuple[Tuple[int, str, int], ...] = field(default_factory=tuple)  # (level, title, 1-based page)
