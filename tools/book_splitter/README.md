# 📖 Book Splitter Utility (`book-split`)

Standalone study tool for inspecting, planning, splitting, and verifying PDF books into per-chapter `.pdf` and `.txt` files for AI study ingestion (Antigravity, Gemini, NotebookLM, etc.).

---

## 🏗️ Workflow Overview

```text
Inspect PDF ➔ Generate Split Plan YAML ➔ Human Review & Edit ➔ Split PDF & Export Text ➔ Verify Manifest
```

---

## 🛠️ Command Usage

### 1. Inspect PDF Book
Inspect PDF page count, extractable text availability, and embedded table of contents (TOC):
```bash
book-split inspect pilot/math-reconstruction/books/source/apostol-calculus-vol1.pdf
# or:
python tools/book_splitter/cli.py inspect pilot/math-reconstruction/books/source/apostol-calculus-vol1.pdf
```

### 2. Generate Proposed Split Plan (YAML)
Extract level-1 chapter bookmarks into a human-reviewable 1-indexed inclusive YAML plan:
```bash
book-split plan pilot/math-reconstruction/books/source/apostol-calculus-vol1.pdf \
  --output pilot/math-reconstruction/books/plans/apostol-calculus-vol1.chapters.yaml
```

### 3. Review & Edit YAML Plan
Edit `books/plans/apostol-calculus-vol1.chapters.yaml` in VS Code to adjust page numbers or exclude unwanted sections.

### 4. Preview / Dry-Run Split
Preview exported chapter ranges and filenames without writing files:
```bash
book-split split pilot/math-reconstruction/books/source/apostol-calculus-vol1.pdf \
  --plan pilot/math-reconstruction/books/plans/apostol-calculus-vol1.chapters.yaml \
  --dry-run
```

### 5. Execute Chapter Split & Text Extraction
Export chapter `.pdf` files, `.txt` files, and `manifest.json`:
```bash
book-split split pilot/math-reconstruction/books/source/apostol-calculus-vol1.pdf \
  --plan pilot/math-reconstruction/books/plans/apostol-calculus-vol1.chapters.yaml
```

### 6. Verify Manifest Hashes
Verify exported files against their SHA-256 manifest:
```bash
book-split verify \
  pilot/math-reconstruction/books/source/apostol-calculus-vol1.pdf \
  pilot/math-reconstruction/books/chapters/apostol-calculus-vol1/manifest.json
```

---

## 🔒 Gitignore Safety Guardrails

- **Copyrighted PDFs (`.pdf`) & raw chapter text (`.txt`):** Saved under `books/source/`, `books/chapters/`, and `books/text/` which are **strictly gitignored**.
- **Tracked Artifacts:** Split plan YAML files (`books/plans/*.yaml`) and manifest metadata (`books/chapters/**/manifest.json`) **are tracked in Git**.
