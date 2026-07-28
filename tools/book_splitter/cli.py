"""CLI entry point for book-split utility."""

import argparse
import json
from pathlib import Path
import sys

from tools.book_splitter.inspector import inspect_pdf, compute_sha256
from tools.book_splitter.detector import generate_plan_from_bookmarks, save_split_plan_yaml, load_split_plan_yaml
from tools.book_splitter.splitter import execute_split


def cmd_inspect(pdf_path: str) -> None:
    """Inspect a PDF file and display summary statistics and TOC entries."""
    path = Path(pdf_path).resolve()
    result = inspect_pdf(path)

    print("=== Book Splitter — PDF Inspection ===")
    print(f"File                 : {result.file_path}")
    print(f"SHA-256              : {result.file_sha256}")
    print(f"Total Pages          : {result.total_pages}")
    print(f"Text-Readable Pages  : {result.text_readable_pages} / {result.total_pages}")
    print(f"Embedded Bookmarks   : {result.embedded_bookmarks}")
    print("-" * 50)

    if result.toc_entries:
        print("Candidate Bookmark Structure (Top Level):")
        for level, title, page_1based in result.toc_entries:
            indent = "  " * (level - 1)
            print(f"{indent}[L{level}] {title:<40} (Page {page_1based})")
    else:
        print("No embedded TOC bookmarks found. Text scanning or manual split plan required.")


def cmd_plan(pdf_path: str, strategy: str = "bookmarks", output_path: str = "") -> None:
    """Generate a candidate SplitPlan YAML file from inspection."""
    path = Path(pdf_path).resolve()
    inspection = inspect_pdf(path)
    plan = generate_plan_from_bookmarks(inspection)

    if not output_path:
        out_name = f"{path.stem}.chapters.yaml"
        out_file = path.parent / out_name
    else:
        out_file = Path(output_path).resolve()

    save_split_plan_yaml(plan, out_file)
    print(f"[OK] Generated reviewable split plan YAML: {out_file}")
    print(f"Plan contains {len(plan.chapters)} chapter ranges. Edit file to adjust boundaries before splitting.")


def cmd_split(source_path: str, plan_path: str, output_dir: str = "", dry_run: bool = False, overwrite: bool = False) -> None:
    """Execute chapter splitting into PDFs and text files based on a YAML plan."""
    plan_file = Path(plan_path).resolve()
    plan = load_split_plan_yaml(plan_file)

    if not output_dir:
        # Default output directory: parent of books/source -> books/
        out_path = Path(source_path).resolve().parent.parent
    else:
        out_path = Path(output_dir).resolve()

    mode_tag = "[DRY-RUN] " if dry_run else ""
    print(f"{mode_tag}Executing chapter split for '{plan.title}'...")

    artifacts = execute_split(plan, out_path, dry_run=dry_run, overwrite=overwrite)

    print("-" * 50)
    print(f"{mode_tag}Processed {len(artifacts)} chapter artifacts:")
    for a in artifacts:
        print(f"  - {a.chapter_id:<25} Pages {a.start_page_1based:>3}..{a.end_page_1based:<3} ({a.page_count} pgs) -> {Path(a.pdf_output_path).name}")

    if not dry_run:
        print(f"[OK] Split complete. Chapter PDFs & text written under: {out_path}")


def cmd_verify(source_path: str, manifest_path: str) -> None:
    """Verify exported chapter artifacts against their manifest and source PDF."""
    manifest_file = Path(manifest_path).resolve()
    source_file = Path(source_path).resolve()

    if not manifest_file.exists():
        print(f"Error: Manifest file not found: {manifest_file}")
        sys.exit(1)

    with manifest_file.open("r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    current_src_hash = compute_sha256(source_file)
    stored_src_hash = manifest_data.get("source_sha256")

    print("=== Book Splitter — Manifest Verification ===")
    print(f"Manifest File : {manifest_file}")
    print(f"Source Match  : {'[OK]' if current_src_hash == stored_src_hash else '[FAIL] Source Hash Mismatch'}")

    chapters_dir = manifest_file.parent
    chapters = manifest_data.get("chapters", [])
    valid_count = 0

    for ch in chapters:
        pdf_rel = ch.get("pdf_path")
        pdf_full = chapters_dir / pdf_rel
        if not pdf_full.exists():
            print(f"  [MISSING] {pdf_rel}")
            continue

        calc_hash = compute_sha256(pdf_full)
        expected_hash = ch.get("sha256")
        if calc_hash == expected_hash:
            valid_count += 1
        else:
            print(f"  [CORRUPT] {pdf_rel} (hash mismatch)")

    print("-" * 50)
    print(f"Verified {valid_count} / {len(chapters)} chapter files match manifest hashes cleanly.")


def main():
    parser = argparse.ArgumentParser(description="Book Splitter CLI for Big Brain Time study materials.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Inspect
    inspect_parser = subparsers.add_parser("inspect", help="Inspect PDF page count, text, and TOC bookmarks.")
    inspect_parser.add_argument("pdf_path", help="Path to source PDF file.")

    # Plan
    plan_parser = subparsers.add_parser("plan", help="Generate reviewable YAML split plan from PDF.")
    plan_parser.add_argument("pdf_path", help="Path to source PDF file.")
    plan_parser.add_argument("--strategy", default="bookmarks", help="Detection strategy (bookmarks)")
    plan_parser.add_argument("--output", "-o", default="", help="Output YAML plan file path.")

    # Split
    split_parser = subparsers.add_parser("split", help="Split PDF into chapter PDFs and text files using YAML plan.")
    split_parser.add_argument("source_path", help="Path to source PDF file.")
    split_parser.add_argument("--plan", "-p", required=True, help="Path to YAML split plan file.")
    split_parser.add_argument("--output-dir", "-o", default="", help="Root books/ directory path.")
    split_parser.add_argument("--dry-run", action="store_true", help="Preview split plan without writing files.")
    split_parser.add_argument("--overwrite", action="store_true", help="Overwrite existing chapter files.")

    # Verify
    verify_parser = subparsers.add_parser("verify", help="Verify exported chapter files against manifest.json.")
    verify_parser.add_argument("source_path", help="Path to source PDF file.")
    verify_parser.add_argument("manifest_path", help="Path to manifest.json file.")

    args = parser.parse_args()

    if args.command == "inspect":
        cmd_inspect(args.pdf_path)
    elif args.command == "plan":
        cmd_plan(args.pdf_path, strategy=args.strategy, output_path=args.output)
    elif args.command == "split":
        cmd_split(
            source_path=args.source_path,
            plan_path=args.plan,
            output_dir=args.output_dir,
            dry_run=args.dry_run,
            overwrite=args.overwrite,
        )
    elif args.command == "verify":
        cmd_verify(args.source_path, args.manifest_path)


if __name__ == "__main__":
    main()
