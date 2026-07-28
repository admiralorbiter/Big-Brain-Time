"""Deterministic PDF chapter splitter and text extractor using PyMuPDF."""

import json
from pathlib import Path
from typing import List, Tuple
import pymupdf

from tools.book_splitter.models import (
    SplitPlan,
    ChapterArtifact,
)
from tools.book_splitter.inspector import compute_sha256


def validate_plan_boundaries(plan: SplitPlan, total_source_pages: int) -> List[str]:
    """Validate plan for page range errors, overlaps, or out-of-bound errors."""
    errors: List[str] = []
    included = [ch for ch in plan.chapters if ch.include]

    for ch in included:
        if ch.start_page < 0:
            errors.append(f"Chapter '{ch.chapter_id}' has negative start page {ch.start_page_1based}.")
        if ch.end_page > total_source_pages:
            errors.append(
                f"Chapter '{ch.chapter_id}' end page {ch.end_page_1based} exceeds total source pages ({total_source_pages})."
            )
        if ch.start_page >= ch.end_page:
            errors.append(
                f"Chapter '{ch.chapter_id}' start page {ch.start_page_1based} >= end page {ch.end_page_1based}."
            )

    # Check overlaps
    sorted_chaps = sorted(included, key=lambda c: c.start_page)
    for i in range(len(sorted_chaps) - 1):
        c1 = sorted_chaps[i]
        c2 = sorted_chaps[i + 1]
        if c1.end_page > c2.start_page:
            errors.append(
                f"Overlap detected between '{c1.chapter_id}' (ends page {c1.end_page_1based}) and '{c2.chapter_id}' (starts page {c2.start_page_1based})."
            )

    return errors


def execute_split(
    plan: SplitPlan,
    output_dir: Path,
    dry_run: bool = False,
    overwrite: bool = False,
) -> Tuple[ChapterArtifact, ...]:
    """Execute chapter splitting and text extraction based on a SplitPlan."""
    source_pdf = Path(plan.source_path).resolve()
    if not source_pdf.exists():
        raise FileNotFoundError(f"Source PDF does not exist: {source_pdf}")

    src_doc = pymupdf.open(source_pdf)
    total_pages = len(src_doc)

    errors = validate_plan_boundaries(plan, total_pages)
    if errors:
        src_doc.close()
        raise ValueError(f"Split plan validation failed:\n" + "\n".join(f"- {e}" for e in errors))

    book_slug = Path(plan.source_path).stem
    chapters_dir = output_dir / "chapters" / book_slug
    text_dir = output_dir / "text" / book_slug

    if not dry_run:
        chapters_dir.mkdir(parents=True, exist_ok=True)
        text_dir.mkdir(parents=True, exist_ok=True)

    artifacts: List[ChapterArtifact] = []

    for ch in plan.chapters:
        if not ch.include:
            continue

        pdf_filename = f"{ch.chapter_id}.pdf"
        txt_filename = f"{ch.chapter_id}.txt"

        pdf_dest = chapters_dir / pdf_filename
        txt_dest = text_dir / txt_filename

        if dry_run:
            artifacts.append(
                ChapterArtifact(
                    chapter_id=ch.chapter_id,
                    title=ch.title,
                    pdf_output_path=str(pdf_dest),
                    text_output_path=str(txt_dest),
                    start_page_1based=ch.start_page_1based,
                    end_page_1based=ch.end_page_1based,
                    page_count=ch.page_count,
                    pdf_sha256="DRY_RUN_HASH",
                )
            )
            continue

        if pdf_dest.exists() and not overwrite:
            src_doc.close()
            raise FileExistsError(f"Chapter PDF already exists: {pdf_dest}. Use --overwrite to replace.")

        # Create Chapter PDF
        out_doc = pymupdf.open()
        out_doc.insert_pdf(
            src_doc,
            from_page=ch.start_page,
            to_page=ch.end_page - 1,
        )
        out_doc.save(str(pdf_dest))
        out_doc.close()

        # Extract Chapter Text
        text_content: List[str] = []
        for p_idx in range(ch.start_page, ch.end_page):
            text_content.append(f"--- PAGE {p_idx + 1} ---\n")
            text_content.append(src_doc[p_idx].get_text())

        txt_dest.write_text("\n".join(text_content), encoding="utf-8")

        pdf_sha256 = compute_sha256(pdf_dest)

        artifacts.append(
            ChapterArtifact(
                chapter_id=ch.chapter_id,
                title=ch.title,
                pdf_output_path=str(pdf_dest),
                text_output_path=str(txt_dest),
                start_page_1based=ch.start_page_1based,
                end_page_1based=ch.end_page_1based,
                page_count=ch.page_count,
                pdf_sha256=pdf_sha256,
            )
        )

    src_doc.close()

    # Save manifest.json
    if not dry_run:
        manifest_path = chapters_dir / "manifest.json"
        manifest_data = {
            "schema": "bbt.book-split-manifest/v1",
            "book_id": plan.book_id,
            "source_path": str(source_pdf),
            "source_sha256": plan.source_sha256,
            "chapter_count": len(artifacts),
            "chapters": [
                {
                    "id": a.chapter_id,
                    "title": a.title,
                    "pdf_path": str(Path(a.pdf_output_path).relative_to(chapters_dir)),
                    "text_path": str(Path(a.text_output_path).relative_to(text_dir.parent)),
                    "start_page": a.start_page_1based,
                    "end_page": a.end_page_1based,
                    "page_count": a.page_count,
                    "sha256": a.pdf_sha256,
                }
                for a in artifacts
            ],
        }
        with manifest_path.open("w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2)

    return tuple(artifacts)
