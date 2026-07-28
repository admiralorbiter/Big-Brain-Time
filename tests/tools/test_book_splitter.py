"""Contract & integration tests for book-split tool."""

import tempfile
from pathlib import Path
import pytest
import pymupdf

from tools.book_splitter.inspector import inspect_pdf, compute_sha256
from tools.book_splitter.detector import generate_plan_from_bookmarks, save_split_plan_yaml, load_split_plan_yaml
from tools.book_splitter.splitter import execute_split, validate_plan_boundaries
from tools.book_splitter.cli import cmd_verify


def create_synthetic_pdf(pdf_path: Path) -> None:
    """Create a 4-page synthetic PDF with embedded TOC bookmarks for testing."""
    doc = pymupdf.open()

    for i in range(1, 5):
        page = doc.new_page()
        page.insert_text((50, 50), f"Sample content for Page {i}. Chapter text line.\nSecond line of page {i}.")

    # Set TOC: Level 1 "Chapter 1" at page 1, Level 1 "Chapter 2" at page 3
    toc = [
        [1, "Chapter 1 Intro", 1],
        [1, "Chapter 2 Main", 3],
    ]
    doc.set_toc(toc)
    doc.save(str(pdf_path))
    doc.close()


def test_inspect_and_plan_generation():
    """Verify inspection and bookmark-based plan generation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / "test_book.pdf"
        create_synthetic_pdf(pdf_path)

        inspection = inspect_pdf(pdf_path)
        assert inspection.total_pages == 4
        assert inspection.text_readable_pages == 4
        assert inspection.embedded_bookmarks == 2

        plan = generate_plan_from_bookmarks(inspection)
        assert len(plan.chapters) == 2
        assert plan.chapters[0].title == "Chapter 1 Intro"
        assert plan.chapters[0].start_page == 0
        assert plan.chapters[0].end_page == 2
        assert plan.chapters[1].title == "Chapter 2 Main"
        assert plan.chapters[1].start_page == 2
        assert plan.chapters[1].end_page == 4


def test_yaml_plan_roundtrip():
    """Verify SplitPlan saves to 1-indexed YAML and reloads identically into internal 0-indexed representation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / "test_book.pdf"
        yaml_path = Path(tmpdir) / "plan.yaml"
        create_synthetic_pdf(pdf_path)

        inspection = inspect_pdf(pdf_path)
        plan1 = generate_plan_from_bookmarks(inspection)
        save_split_plan_yaml(plan1, yaml_path)

        assert yaml_path.exists()

        plan2 = load_split_plan_yaml(yaml_path)
        assert len(plan2.chapters) == len(plan1.chapters)
        assert plan2.chapters[0].chapter_id == plan1.chapters[0].chapter_id
        assert plan2.chapters[0].start_page == plan1.chapters[0].start_page
        assert plan2.chapters[0].end_page == plan1.chapters[0].end_page


def test_execute_split_dry_run_and_live():
    """Verify dry run and live chapter splitting producing PDF and TXT files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        pdf_path = tmp / "sample_book.pdf"
        create_synthetic_pdf(pdf_path)

        inspection = inspect_pdf(pdf_path)
        plan = generate_plan_from_bookmarks(inspection)

        # Dry run
        dry_artifacts = execute_split(plan, tmp, dry_run=True)
        assert len(dry_artifacts) == 2
        assert dry_artifacts[0].pdf_sha256 == "DRY_RUN_HASH"

        # Live run
        live_artifacts = execute_split(plan, tmp, dry_run=False)
        assert len(live_artifacts) == 2

        chap1_pdf = Path(live_artifacts[0].pdf_output_path)
        chap1_txt = Path(live_artifacts[0].text_output_path)

        assert chap1_pdf.exists()
        assert chap1_txt.exists()

        # Check PyMuPDF extracted page count on exported chapter 1 PDF
        ch1_doc = pymupdf.open(chap1_pdf)
        assert len(ch1_doc) == 2
        ch1_doc.close()

        # Check extracted text
        txt_content = chap1_txt.read_text(encoding="utf-8")
        assert "Sample content for Page 1" in txt_content
        assert "Sample content for Page 2" in txt_content

        # Verify manifest.json
        manifest_path = tmp / "chapters" / "sample_book" / "manifest.json"
        assert manifest_path.exists()


def test_boundary_validation_rejection():
    """Verify out-of-bound ranges or overlapping chapters raise validation errors."""
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / "test_book.pdf"
        create_synthetic_pdf(pdf_path)
        inspection = inspect_pdf(pdf_path)
        plan = generate_plan_from_bookmarks(inspection)

        # Create invalid plan with out-of-bounds page
        invalid_chapters = tuple(plan.chapters) + (
            plan.chapters[0].__class__(chapter_id="bad", title="Bad", start_page=10, end_page=20, include=True),
        )
        bad_plan = plan.__class__(**{**plan.__dict__, "chapters": invalid_chapters})

        errors = validate_plan_boundaries(bad_plan, total_source_pages=4)
        assert len(errors) > 0
        assert "exceeds total source pages" in errors[0]
