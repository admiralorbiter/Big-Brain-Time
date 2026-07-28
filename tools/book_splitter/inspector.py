"""PDF Inspection engine using PyMuPDF."""

hashlib_sha256 = None
import hashlib
from pathlib import Path
from typing import Tuple
import pymupdf

from tools.book_splitter.models import BookInspectionResult


def compute_sha256(file_path: Path) -> str:
    """Calculate SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def inspect_pdf(pdf_path: Path) -> BookInspectionResult:
    """Inspect PDF page count, extractable text pages, and embedded bookmarks."""
    pdf_path = Path(pdf_path).resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    sha256_hash = compute_sha256(pdf_path)

    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)

    text_pages = 0
    for page in doc:
        text = page.get_text()
        if text and len(text.strip()) > 10:
            text_pages += 1

    raw_toc = doc.get_toc()
    doc.close()

    toc_entries: List[Tuple[int, str, int]] = []
    for entry in raw_toc:
        level, title, page_num = entry[0], entry[1], entry[2]
        toc_entries.append((int(level), str(title).strip(), int(page_num)))

    return BookInspectionResult(
        file_path=str(pdf_path),
        file_sha256=sha256_hash,
        total_pages=total_pages,
        text_readable_pages=text_pages,
        embedded_bookmarks=len(toc_entries),
        toc_entries=tuple(toc_entries),
    )
