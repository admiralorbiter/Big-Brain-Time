---
id: system.sprint-0-charter
title: Sprint 0 Program Charter, Scope Boundary & Baseline Fixture Plan
document_type: specification
maturity: working
describes: proposed_state
owner: Jonathan Lane
created: 2026-07-26
last_reviewed: 2026-07-26
canonical_for:
  - Sprint 0 charter
  - Initial defect fixtures
  - Python package shell specification
tags:
  - sprint-0
  - charter
  - bbt-cli
  - fixtures
---

# Sprint 0 Program Charter & System Baseline Plan

**Milestone:** M0 — Trust Foundation  
**Sprint:** S0 — Program Baseline and Acceptance Freeze  
**Prepared:** 2026-07-26  

---

## 1. Mission & Year-One Capabilities

Big Brain Time is transitioning from a static Markdown folder into an evolving **local-first Flask + SQLite + CLI personal operating system**. 

### Year-One Core Capabilities
1. **Context-Switching Resumption:** 90-Second Ready-to-Resume transition capsules (`Stop Point`, `Restart Cue`, `Next Micro-Action`, `Resumption Trigger`).
2. **Automated Diagnostics (`bbt doctor`):** Instant detection of broken links, stale relative-time language, missing front-matter metadata, duplicate question IDs, and index omissions.
3. **Citation-Bearing Context Packs:** Scoped evidence retrieval with explicit temporal validity and conflict disclosure.
4. **Local Operational Workbench:** Thin Flask/HTMX local web interface over single-writer SQLite operational aggregates with deterministic Markdown export.
5. **Data/Control Plane Safety Firewall:** Strict isolation of retrieved Markdown evidence from execution instructions to prevent indirect prompt injection.

---

## 2. Scope Boundaries & Stop Rules

### Non-Goals for Year One
- No multi-user concurrent editing or CRDT sync algorithms (single-user local-first authority model).
- No direct cloud-native backend dependencies (runs 100% locally on Windows/Powershell).
- No unverified AI mutation of canonical Markdown files without explicit human patch review.

### Milestone Stop Rules
- **Stop Rule M0:** Do not proceed to `bbt doctor` development until an independent, isolated backup and restore rehearsal is verified and documented (Sprint 1).
- **Stop Rule M1:** Do not implement SQLite read models until the full-handbook baseline and retrieval gold set are frozen (Sprint 4).
- **Stop Rule M4:** Do not enable local automated actions until permission policies pass 100% of adversarial boundary tests (Sprint 20).

---

## 3. Seeded Live Repository Defect Fixtures

To ensure `bbt doctor` targets real-world failures immediately, Sprint 0 freezes test fixtures for the following observed repository defects:

| Fixture ID | Defect Type | Live Repository Location | Expected Diagnostic Severity |
| :--- | :--- | :--- | :---: |
| `FIX-DEFECT-001` | Broken Decision Links | 5 decision links referencing non-existent anchors/files | **ERROR** |
| `FIX-DEFECT-002` | Expired Relative-Time Language | Dated "today" / "tomorrow" language in [`views/now.md`](file:///c:/Users/admir/Github/bigbraintime/views/now.md) | **WARNING** |
| `FIX-DEFECT-003` | Missing Project Status Fields | 15 project pages lacking documented `status:` field | **WARNING** |
| `FIX-DEFECT-004` | Duplicate Typed Question IDs | Reuse of typed question IDs across unrelated subjects | **ERROR** |
| `FIX-DEFECT-005` | Stale Experiment Result | Experiment log retaining zero-witness result corrected to 25 | **WARNING** |
| `FIX-DEFECT-006` | Incomplete Index Coverage | Project and knowledge indexes omitting newly added files | **INFO** |

---

## 4. Python Package & CLI Shell Specification (`bbt`)

The CLI shell will be developed as a local Python package under `src/bbt`:

```text
bigbraintime/
├── src/
│   └── bbt/
│       ├── __init__.py
│       ├── cli.py            # Click/Argparse CLI entrypoint (bbt --help)
│       ├── config.py         # Read-only configuration & path resolution
│       ├── diagnostics/      # Diagnostic rules engine (bbt doctor)
│       ├── domain/           # Core domain models & invariants
│       └── storage/          # SQLite read-model & Markdown exporters
├── tests/
│   ├── conftest.py
│   ├── test_cli.py           # CLI invocation & snapshot tests
│   └── test_fixtures.py      # Seeded repository defect tests
├── pyproject.toml            # Package metadata & entrypoints
└── system/
    └── 00_SPRINT_0_CHARTER.md
```

### Initial Commands Target (Sprint 0-2)
* `bbt --help`: Output version, commands, and options.
* `bbt doctor`: Execute read-only diagnostics against corpus without file mutation.
* `bbt doctor --json`: Output machine-readable diagnostic findings.

---

## 5. Reconciled Sprint 0 Trust Ledger

| Task | Classification | Status | Target Deliverable |
| :--- | :---: | :---: | :--- |
| `T-BBT-0001` | **A0** | **IN PROGRESS** | [`system/00_SPRINT_0_CHARTER.md`](file:///c:/Users/admir/Github/bigbraintime/system/00_SPRINT_0_CHARTER.md) |
| `T-BBT-0002` | **A0** | **QUEUED** | `system/SOURCE_REQUIREMENT_MANIFEST.md` |
| `T-BBT-0003` | **A2** | **QUEUED** | `tests/fixtures/defect_corpus/` |
| `T-BBT-0004` | **A1** | **QUEUED** | `pyproject.toml` + `src/bbt/cli.py` |
| `T-BBT-0005` | **D** | **QUEUED** | Baseline human-system timing log |
