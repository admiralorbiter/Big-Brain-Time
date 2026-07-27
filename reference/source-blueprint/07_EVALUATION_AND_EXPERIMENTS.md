# 06 — Roadmap, Milestones, Tasks, and Sprints

## 1. Delivery philosophy

The destination is large; the increments are deliberately small. A sprint is a default two-week planning container, not a promise to ship unsafe work on a date. A milestone completes only when its evidence gate passes.

Rules:

1. Acceptance tests are written before implementation.
2. Every sprint must produce an inspectable artifact.
3. Read-only capability precedes write capability.
4. Deterministic behavior precedes model behavior.
5. A feature can be dropped if it fails a value or safety experiment.
6. No milestone is complete merely because code exists.
7. Each sprint ends with a Ready-to-Resume record.

## 2. Milestone map

| ID | Milestone | Sprints | Evidence gate |
|---|---|---|---|
| M0 | Trust Foundation | Sprints 0–1 | Corpus can be recovered; scope and baseline are frozen. |
| M1 | Observatory v1 | Sprints 2–5 | Known defects are executable tests; context packs beat or clarify the full-handbook baseline. |
| M2 | Rebuildable Knowledge Read Model | Sprints 6–9 | SQLite can be deleted/rebuilt and can answer temporal/provenance questions. |
| M3 | Retrieval and Sensemaking Engine | Sprints 10–12 | Local, temporal, negative, and global queries meet benchmark gates. |
| M4 | Operational Workbench | Sprints 13–16 | A narrow structured workflow reduces real friction and exports cleanly. |
| M5 | Cognitive Interface | Sprints 17–19 | Cited synthesis and propagation patches are safe and reviewable. |
| M6 | Adaptive Partner — Bounded | Sprints 20–22 | Policy enforcement works; proactive behavior is useful; only reversible local actions are authorized. |
| M7 | Capability Platform v1 | Sprint 23 | Reusable foundations and measured year-two priorities exist. |

## 3. Critical path

```text
Backup/restore
  -> read-only parser
  -> known-defect diagnostics
  -> evaluation set
  -> context packs
  -> SQLite read model
  -> temporal/provenance resolver
  -> retrieval router
  -> synthesis
  -> propagation proposals
  -> policy engine
  -> shadow monitoring
  -> reversible local action
```

Flask is intentionally off the critical path until commands and tests work.

## 4. Sprint catalog

### Sprint 0 — Program Baseline and Acceptance Freeze

**Goal:** Establish scope, source traceability, fixtures, and a reproducible development shell before feature work.  
**Exit condition:** A versioned charter, baseline report, and known-defect fixtures exist.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 1 — Independent Backup and Restore Proof

**Goal:** Protect the corpus and prove that recovery works.  
**Exit condition:** An isolated restore is verified and reproducible.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 2 — Read-Only Corpus Parser and `bbt doctor` Skeleton

**Goal:** Parse the corpus without writes and report its structure.  
**Exit condition:** The CLI inventories files, metadata, IDs, and parse failures.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 3 — Known-Defect Diagnostic Rules

**Goal:** Turn the observed defects into executable tests.  
**Exit condition:** All reported defects are detected by named, severity-ranked rules.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 4 — Retrieval Gold Set and Full-Handbook Baseline

**Goal:** Freeze evaluation before optimizing retrieval.  
**Exit condition:** At least 20 cases with expected evidence, conflicts, and abstention labels exist.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 5 — Citation-Bearing Context Packs v0

**Goal:** Generate project-scoped context and compare it with whole-handbook prompting.  
**Exit condition:** A pack manifest, evidence index, conflict section, and benchmark report exist.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 6 — SQLite Read-Model Schema

**Goal:** Introduce a disposable, strict, versioned projection.  
**Exit condition:** Documents, sections, links, typed records, diagnostics, and manifest tables migrate cleanly.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 7 — Deterministic Import, Rebuild, and Integrity

**Goal:** Make the read model safely deletable and reproducible.  
**Exit condition:** Delete/rebuild/compare and integrity checks pass.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 8 — FTS5 Search and Explainability

**Goal:** Deliver fast local search with filters and explanations.  
**Exit condition:** CLI search supports exact, phrase, prefix, metadata filters, and rank explanation.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 9 — Provenance, Claims, and Temporal Truth

**Goal:** Model source, correction, supersession, valid time, and recorded time.  
**Exit condition:** Known corrected/conflicting examples answer current and as-of queries correctly.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 10 — Query Router and Authority Policies

**Goal:** Route exact, local, temporal, conflict, global, and negative questions.  
**Exit condition:** Each gold case produces an inspectable retrieval plan.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 11 — Hybrid Retrieval Experiment

**Goal:** Test metadata, links, embeddings, and reranking against the baseline.  
**Exit condition:** Adopt only methods that meet predeclared gain and cost thresholds.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 12 — Global Sensemaking and Portfolio Views

**Goal:** Answer corpus-wide questions without flattening the entire handbook.  
**Exit condition:** Hierarchical global retrieval passes human rubrics and traces claims to evidence.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 13 — Thin Flask/HTMX Observatory

**Goal:** Expose proven commands through a local web interface.  
**Exit condition:** Diagnostics, search, evidence, and build status work without duplicating logic.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 14 — Operational Slice: Projects and Tasks

**Goal:** Migrate a narrow structured workflow with export and rollback.  
**Exit condition:** One project can be managed in SQLite and round-tripped to Markdown/JSON.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 15 — Transitions and Re-Entry Capsules

**Goal:** Make interrupted work easy to resume.  
**Exit condition:** Transition records generate accurate, benchmarked re-entry capsules.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 16 — Routines, Recurrence, and Calendar Boundaries

**Goal:** Support recurrence and exceptions without replacing the calendar.  
**Exit condition:** RRULE-compatible series, exceptions, and ICS export pass examples.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 17 — Source-Grounded Conversational Synthesis

**Goal:** Generate answers only after retrieval and conflict/abstention checks.  
**Exit condition:** Material claims are cited and unsupported questions abstain.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 18 — Propagation Graph and Change Impact

**Goal:** Detect what must change when a decision or claim changes.  
**Exit condition:** Seeded changes identify all known dependent artifacts.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 19 — Reviewable Patch and Proposal Workbench

**Goal:** Turn impact analysis into safe, inspectable proposed changes.  
**Exit condition:** Users can accept/reject granular operations with precondition hashes and rollback data.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 20 — Permission Engine and Action Firewall

**Goal:** Enforce domain, risk, scope, and confirmation policies.  
**Exit condition:** Unauthorized and injected action attempts fail deterministic tests.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 21 — Shadow-Mode Proactive Monitoring

**Goal:** Learn which warnings and preparations are useful without acting.  
**Exit condition:** Alert precision, dismissals, interruption cost, and trust are measured.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 22 — Limited Reversible Local Actions

**Goal:** Authorize a tiny set of low-risk operations after safety gates.  
**Exit condition:** Scoped actions execute, verify, audit, and roll back with zero seeded boundary violations.

See `product_backlog.csv` for implementation tasks and acceptance tests.

### Sprint 23 — Year-One Capability Audit and Platformization

**Goal:** Evaluate the joint system, stabilize shared infrastructure, and choose year-two bets.  
**Exit condition:** Capability scorecard, architecture review, deprecation plan, and year-two roadmap are approved.

See `product_backlog.csv` for implementation tasks and acceptance tests.


## 5. Milestone detail and gates

### M0 — Trust Foundation

**Must be true:**

- The exact canonical corpus and exclusions are listed.
- A second independent backup exists.
- A restore into an isolated path completes successfully.
- Recovered files match expected hashes or semantic manifest.
- Git history and sensitive-data boundaries are checked.
- The development environment can be recreated from documented steps.

**Stop condition:** no indexing or migration work if recovery is not proven.

### M1 — Observatory v1

**Must be true:**

- `bbt doctor` is read-only by design and test.
- Every known defect from the audit has a fixture and diagnostic code.
- Diagnostic suppression requires rationale and expiration.
- At least 20 retrieval cases exist before optimization.
- Project context packs include citations, conflicts, unknowns, as-of time, and omissions.
- Full-handbook versus scoped-pack comparison is recorded.

**Proposed gate:** all known seeded defects detected; no false “clean” result when a fixture is corrupted.

### M2 — Rebuildable Knowledge Read Model

**Must be true:**

- `rm read-model.sqlite3 && bbt index` is safe.
- Schema and importer versions appear in the manifest.
- The logical build fingerprint is stable.
- FTS and exact lookup work offline.
- Current and historical truth queries distinguish corrections.
- Backup/restore procedures cover any new operational store separately.

**Stop condition:** no SQLite-canonical domain if export/reimport semantic equivalence is not 100% on its fixture set.

### M3 — Retrieval and Sensemaking Engine

**Must be true:**

- Query plans are inspectable.
- Authority and time filters are visible.
- Hard low-overlap and multi-hop cases are in the test set.
- Negative questions abstain rather than hallucinate.
- Global synthesis traces every material statement to lower-level evidence.
- Embeddings or graph features are adopted only if they beat simpler methods.

### M4 — Operational Workbench

**Must be true:**

- One selected project is managed end-to-end.
- Markdown/JSON exports remain understandable without the app.
- Task and transition updates have an audit history.
- Recurrence reuses RFC 5545 concepts and handles exceptions.
- A real weekly review is faster or more reliable than baseline.

**Stop condition:** revert the migration if maintenance cost or duplicate authority increases.

### M5 — Cognitive Interface

**Must be true:**

- Synthesis cannot bypass retrieval.
- Material claims are citation-mapped.
- Conflicts and unknowns are visible before an answer becomes a patch.
- Propagation analysis catches seeded dependent artifacts.
- Canonical changes are proposals with semantic diffs and preconditions.

### M6 — Adaptive Partner — Bounded

**Must be true:**

- A deterministic permission matrix governs action.
- Prompt-injection and privacy tests pass.
- Shadow monitoring demonstrates acceptable precision and interruption cost.
- Only explicitly selected reversible local actions are enabled.
- Kill switch, safe mode, rollback, and audit logs are tested.

### M7 — Capability Platform v1

**Must be true:**

- Shared services have stable contracts.
- Deprecated experiments and unused complexity are removed.
- The year-one capability scorecard is compared with baseline.
- User trust and cognitive burden are assessed.
- Year-two work is chosen from measured bottlenecks, not novelty.

## 6. Year-two horizon

Potential goals, contingent on year-one evidence:

- broader SQLite-canonical operations
- mobile/voice capture with privacy controls
- private remote access
- email/calendar/GitHub context adapters
- richer global graph sensemaking
- personalized retrieval and buoyancy policies
- a local tool/plugin SDK for specialized subsystems
- limited automated maintenance of generated artifacts
- longitudinal co-adaptation experiments

## 7. Five-year horizon

Big Brain Time could become a personal capability platform with specialized domains—learning, research, health preparation, creative work, home operations, media, professional growth—sharing:

- identity and stable IDs
- provenance and temporal truth
- authority declarations
- project/task/time semantics
- context contracts
- permissions and action audit
- evaluation infrastructure
- user interaction patterns
- export and recovery guarantees

The five-year test is not whether every life domain is captured. It is whether the platform helps the user develop capabilities, preserve autonomy, and change direction without corrupting its model of the person.

## 8. Backlog use

`product_backlog.csv` contains five implementation tasks per sprint—120 tasks total—with acceptance criteria, dependencies, risk, and evidence basis. The backlog should be imported into the current task workflow only one milestone at a time. Future sprint detail is a map, not an obligation.


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
