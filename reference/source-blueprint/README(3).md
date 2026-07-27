# Product Backlog — 24 Sprints / 120 Tasks

**Status at creation:** all tasks are proposed and queued. The backlog is evidence-gated; sprint assignment is a default sequence, not a mandate to continue when a milestone gate fails.

## Backlog conventions

- `P0`: privacy, recovery, authorization, or catastrophic-integrity work.
- `P1`: required for the first useful capability path.
- `P2`: valuable experiment or extension after its prerequisites.
- Acceptance tests are deliverables, not implementation notes.
- A task is `Done` only when its result is reflected in code, tests, runbooks, and canonical project state as applicable.

## Summary

- Tasks: **120**
- Sprints: **24**
- Milestones: **8**
- P0 tasks: **14**
- P1 tasks: **90**
- P2 tasks: **16**

## S0 — Program Baseline and Acceptance Freeze

**Milestone:** M0 — Trust Foundation  
**Goal:** Establish scope, source traceability, fixtures, and a reproducible development shell before feature work.  
**Sprint exit:** A versioned charter, baseline report, and known-defect fixtures exist.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0001 | P1 | Product architect | Write the program charter and scope boundary | Charter names mission, year-one capabilities, non-goals, authority assumptions, and milestone stop rules; it is versioned in Git. | None |
| T-BBT-0002 | P1 | Product architect | Create a source-to-requirement manifest | Every source-backed requirement links to a file, section or line span; proposals and research-derived constraints are labeled separately. | Program charter |
| T-BBT-0003 | P1 | Product architect | Freeze fixtures for every known repository defect | Fixtures reproduce live repository defects (5 broken decision links, stale language in views/now.md, missing status fields on 15 project pages, duplicate typed IDs, corrected experiment value, incomplete indexes). | Source manifest |
| T-BBT-0004 | P1 | Product architect | Create the Python package, CLI shell, test layout, and quality gates | `bbt --help`, test discovery, lint/format/type commands, and a read-only configuration all run on a clean checkout. | Program charter |
| T-BBT-0005 | P1 | Product architect | Capture baseline human and system measures | Record current re-entry time, repeated-explanation examples, maintenance time, search steps, and source-accuracy sample without changing workflow. | Capability questions |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S1 — Independent Backup and Restore Proof

**Milestone:** M0 — Trust Foundation  
**Goal:** Protect the corpus and prove that recovery works.  
**Sprint exit:** An isolated restore is verified and reproducible.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0006 | P0 | Recovery engineer + verifier | Select and document an independent backup target | Backup is separate from the primary device/repository credentials, encrypted as appropriate, and has a retention policy. | Program charter |
| T-BBT-0007 | P0 | Recovery engineer + verifier | Implement a reproducible canonical-corpus backup command | Command records source commit, file manifest, hashes, timestamp, tool version, and excludes secrets/derived data. | Backup target |
| T-BBT-0008 | P0 | Recovery engineer + verifier | Perform an isolated restore rehearsal | Restore occurs in a new directory or machine context with no dependency on the working copy; all expected files and Git history are present. | Backup command |
| T-BBT-0009 | P0 | Recovery engineer + verifier | Rebuild generated artifacts from the restored corpus | Handbook and any existing indexes are regenerated and compared to expected output; discrepancies are explained. | Isolated restore |
| T-BBT-0010 | P0 | Recovery engineer + verifier | Publish restore evidence and recovery runbook | Runbook includes RPO/RTO assumptions, commands, checks, failure escalation, and date of next rehearsal. | Restore and rebuild |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S2 — Read-Only Corpus Parser and `bbt doctor` Skeleton

**Milestone:** M1 — Observatory v1  
**Goal:** Parse the corpus without writes and report its structure.  
**Sprint exit:** The CLI inventories files, metadata, IDs, and parse failures.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0011 | P1 | Archivist/implementer | Discover corpus files deterministically | Scanner inventories included/excluded files in stable order and reports unsupported or unreadable inputs. | S0 package shell |
| T-BBT-0012 | P1 | Archivist/implementer | Parse YAML front matter, headings, links, and source spans | Parser preserves raw text and line ranges, tolerates unknown fields, and emits visible parse diagnostics rather than dropping content. | File discovery |
| T-BBT-0013 | P1 | Archivist/implementer | Build a global typed-ID registry | Registry detects duplicates, invalid formats, missing IDs where required, and aliases without auto-merging records. | Parser |
| T-BBT-0014 | P1 | Archivist/implementer | Implement the read-only `bbt doctor` command skeleton | CLI returns human-readable and JSON reports with severity, code, file, span, explanation, and remediation hint; no file writes occur. | Parser and registry |
| T-BBT-0015 | P1 | Archivist/implementer | Prove read-only behavior | Test snapshots corpus hashes before/after every doctor command and fails on any mutation outside a temporary output directory. | Doctor skeleton |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S3 — Known-Defect Diagnostic Rules

**Milestone:** M1 — Observatory v1  
**Goal:** Turn the observed defects into executable tests.  
**Sprint exit:** All reported defects are detected by named, severity-ranked rules.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0016 | P1 | Assurance engineer | Implement local-link and anchor diagnostics | All five known broken decision links are detected; valid links and external references do not produce false positives. | S2 doctor |
| T-BBT-0017 | P1 | Assurance engineer | Implement required-metadata and project-status diagnostics | All known project pages missing documented status are detected with exact spans and accepted-status hints. | S2 parser |
| T-BBT-0018 | P1 | Assurance engineer | Implement stale relative-time and expired-view diagnostics | Seeded `today`, `tomorrow`, and dated-current language is flagged when its effective window has expired, with suppression options for historical quotes. | S2 parser |
| T-BBT-0019 | P1 | Assurance engineer | Implement duplicate-ID, index-omission, and stale-correction diagnostics | Known question-ID reuse, omitted index entries, and the stale zero-versus-25 experiment result are surfaced as separate diagnosable failures. | S2 registry/parser |
| T-BBT-0020 | P1 | Assurance engineer | Add severity, confidence, suppression, and regression snapshots | Rules have stable codes, documented false-positive tradeoffs, expiring suppressions, and golden reports for all known defects. | All S3 diagnostics |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S4 — Retrieval Gold Set, Bitemporal Benchmark, and Epistemic Answer Gate

**Milestone:** M1 — Observatory v1  
**Goal:** Freeze a rigorous evaluation benchmark and implement a deterministic 5-gate answer pipeline before optimizing retrieval.  
**Sprint exit:** ≥ 24 cases across all 8 required families exist with bitemporal evidence annotations; the 5-gate answer pipeline passes all 7 locked exit criteria. See `system/ARCHITECTURE_DECISION_RECORDS.md` for ADR-001 through ADR-004.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0021 | P1 | Evaluation lead | Define ≥ 24 retrieval regression cases across 8 required families | Cases cover: static recall, supersession, historical as-of, multi-session synthesis, workflow resumption, latent retrieval, abstention, and contradiction; each family has ≥ 3 cases with distractors (ADR-001). | S0 capability questions |
| T-BBT-0022 | P1 | Evaluation lead | Create bitemporal gold annotations | Each case carries: required evidence spans with `valid_from`/`valid_to`/`recorded_at`, stale/forbidden evidence IDs, supersession edges, abstention flag, and unacceptable-answer patterns (ADR-001). | Question set |
| T-BBT-0023 | P1 | Evaluation lead | Implement RequiredClaimPlanner and ClaimAdjudicator (Gates 2 & 3) | Planner decomposes each question into required claims C1…Cn; adjudicator assigns SUPPORT/REFUTE/INSUFFICIENT/CONFLICT per claim deterministically from evidence; no prose renderer is invoked (ADR-003). | Gold annotations |
| T-BBT-0024 | P1 | Evaluation lead | Implement deterministic answer-status state machine and post-generation verifier (Gates 4 & 5) | State machine selects ANSWERED/PARTIAL/UNKNOWN/CONFLICT before prose generation; verifier splits prose into atomic claims, requires evidence IDs for each, and runs entailment; 0 unsupported essential claims; citation entailment precision ≥ 0.95 (ADR-003). | Claim adjudicator |
| T-BBT-0025 | P1 | Evaluation lead | Build benchmark runner with 10 diagnostic metrics and freeze pre-index baseline | Runner scores retrieval evidence recall/precision, current-state accuracy, historical-state accuracy, stale-fact suppression rate, resumption completeness, contradiction disclosure recall, abstention F1, citation entailment precision, and unsupported-claim rate separately; prompt-injection fixture suite passes with 0 control escapes (ADR-004). | Benchmark runner; gold annotations |

**Sprint 4 exit criteria (locked — see ADR-003 & ADR-004):**  
Benchmark cases ≥ 24 · Contradiction disclosure recall = 1.00 · Abstention F1 ≥ 0.90 · Unsupported essential claims = 0 · Citation entailment precision ≥ 0.95 · Stale-state selection rate = 0 · Prompt-injection escapes = 0

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S5 — Citation-Bearing Context Packs With Reproducible Manifests

**Milestone:** M1 — Observatory v1  
**Goal:** Build a local-first context-pack compiler with auditable manifests and compare it against full-handbook prompting.  
**Sprint exit:** A pack manifest, evidence index, conflict section, coverage-gap section, and benchmark comparison report exist. Every pack is independently reproducible. See `system/ARCHITECTURE_DECISION_RECORDS.md` for ADR-002, ADR-005, and ADR-006.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0026 | P1 | Context engineer | Define the versioned context-pack manifest contract | Manifest includes: question interpretation, as-of basis, selected evidence with lineage and trust-boundary flags, applicable temporal state, supersession decisions, unresolved conflicts, coverage gaps, excluded-item reasons, and compiler/index versions (ADR-005). | S4 gold set |
| T-BBT-0027 | P1 | Context engineer | Implement trust-boundary normalization and instruction-like-content flagging (Gate 1) | Every evidence item carries `trust_boundary: untrusted` and `contains_instruction_like_content` flag; instruction-like spans are excluded from control logic and flagged in manifest exclusions (ADR-004). | Context schema |
| T-BBT-0028 | P1 | Context engineer | Implement local evidence pack compiler with token-budget selection | Given a question and project scope, collects: canonical page, linked decisions, transitions, referenced knowledge, conflicts, supersession edges, and stale markers deterministically within token budget; token-budget selection is deterministic for the same index version and configuration (ADR-005, ADR-006). | Evidence collector |
| T-BBT-0029 | P1 | Context engineer | Add citation and provenance rendering with claim-level lineage | Every included excerpt retains: source file, stable document ID, heading, line span, content hash, retrieval reason, valid-time interval, and claim ID; summary sentences retain source claim IDs; compression omissions are reported in manifest (ADR-002, ADR-005). | Pack compiler |
| T-BBT-0030 | P1 | Context engineer | Compare context packs with full handbook across all 8 benchmark families | Run gold set on lexical-only, semantic-only, hybrid, and local-graph-expansion retrieval modes; report Recall@5, Precision@10, citation entailment precision, and token cost per mode; identify cases requiring global community retrieval (ADR-006). | Pack renderer; benchmark runner |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S6 — SQLite Read-Model Schema

**Milestone:** M2 — Rebuildable Knowledge Read Model  
**Goal:** Introduce a disposable, strict, versioned projection.  
**Sprint exit:** Documents, sections, links, typed records, diagnostics, and manifest tables migrate cleanly.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0031 | P1 | Data architect | Design migration 001 for the rebuildable read model | Schema covers documents, sections, links, typed records, diagnostics, build metadata, and raw-source references using STRICT tables where practical. | M1 evidence |
| T-BBT-0032 | P1 | Data architect | Implement forward-only schema migration runner with test rollback strategy | Migrations are versioned, transactional where SQLite permits, and tested from an empty database and prior schema fixture. | Migration 001 |
| T-BBT-0033 | P1 | Data architect | Define stable identifiers and source keys | Document/section keys survive rebuilds when content location is stable and record aliases handle renames without identity reuse. | Parser + schema |
| T-BBT-0034 | P1 | Data architect | Enable foreign keys and integrity checks | Connection setup enforces foreign keys; CI runs `integrity_check`, `foreign_key_check`, uniqueness, and domain invariants. | Schema |
| T-BBT-0035 | P1 | Data architect | Write the derived-store deletion contract | Documentation and automated test prove the database may be deleted without canonical loss and identify which future tables would not be disposable. | Schema |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S7 — Deterministic Import, Rebuild, and Integrity

**Milestone:** M2 — Rebuildable Knowledge Read Model  
**Goal:** Make the read model safely deletable and reproducible.  
**Sprint exit:** Delete/rebuild/compare and integrity checks pass.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0036 | P1 | Data engineer | Implement deterministic corpus importer | Same corpus commit and importer version produce equivalent rows and source spans in stable order. | S6 schema |
| T-BBT-0037 | P1 | Data engineer | Make rebuild atomic | Build occurs in a temporary database and replaces the current projection only after all integrity and application checks pass. | Importer |
| T-BBT-0038 | P1 | Data engineer | Record a build fingerprint | Database stores corpus commit, source manifest hash, schema version, importer version, configuration, and completed timestamp. | Importer |
| T-BBT-0039 | P1 | Data engineer | Build semantic and structural comparison reports | Two rebuilds compare record counts, IDs, links, diagnostics, and normalized content hashes while ignoring allowed timestamps. | Atomic rebuild |
| T-BBT-0040 | P1 | Data engineer | Test corrupted and interrupted rebuild recovery | Injected crash or malformed source leaves last known-good read model available and exposes a clear failure report. | Atomic rebuild |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S8 — FTS5 Search and Explainability

**Milestone:** M2 — Rebuildable Knowledge Read Model  
**Goal:** Deliver fast local search with filters and explanations.  
**Sprint exit:** CLI search supports exact, phrase, prefix, metadata filters, and rank explanation.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0041 | P1 | Search engineer | Create weighted FTS5 indexes | Index title, aliases, headings, body, typed IDs, canonical subjects, and tags with documented field weights. | S7 importer |
| T-BBT-0042 | P1 | Search engineer | Implement exact, phrase, prefix, boolean, and ranked search modes | CLI exposes predictable query syntax and returns snippets, source spans, scores, and match reasons. | FTS indexes |
| T-BBT-0043 | P1 | Search engineer | Add metadata and authority filters | Search can constrain document type, project, status, privacy, maturity, current/historical state, and review date. | Search modes |
| T-BBT-0044 | P1 | Search engineer | Add explain-search output | Result explanation shows FTS contribution, filters, link/metadata expansion, suppression, and why higher-ranked items won. | Filtered search |
| T-BBT-0045 | P1 | Search engineer | Benchmark FTS5 against frozen baselines | Score the S4 set; identify failure classes and do not add semantic search until lexical/metadata baseline is tuned. | Search adapter |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S9 — Provenance, Claims, and Temporal Truth

**Milestone:** M2 — Rebuildable Knowledge Read Model  
**Goal:** Model source, correction, supersession, valid time, and recorded time.  
**Sprint exit:** Known corrected/conflicting examples answer current and as-of queries correctly.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0046 | P1 | Provenance/temporal engineer | Add agent, source-artifact, activity, claim, evidence-link, and claim-relation tables | Schema can represent direct user statements, source documents, imports, AI extraction, corrections, derivations, and responsibility. | S7 schema |
| T-BBT-0047 | P1 | Provenance/temporal engineer | Project selected epistemic claim markers into typed claims | Start with decisions, facts, unknowns, and corrections; preserve source wording and do not infer unlabeled claims silently. | Provenance schema |
| T-BBT-0048 | P1 | Provenance/temporal engineer | Implement supersession and correction resolution | Resolver follows explicit relations, preserves historical claims, detects cycles, and returns unresolved conflicts rather than choosing by recency alone. | Typed claims |
| T-BBT-0049 | P1 | Provenance/temporal engineer | Implement valid-time and recorded-time queries | API answers `current`, `as known on`, and `valid during` questions with tests where a later correction changes knowledge but not past valid time. | Claims/resolver |
| T-BBT-0050 | P1 | Provenance/temporal engineer | Create `bbt why` truth explanations | Command reports chosen claim, authority rule, source evidence, temporal basis, superseded alternatives, and unresolved conflicts. | Temporal query |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S10 — Query Router and Authority Policies

**Milestone:** M3 — Retrieval and Sensemaking Engine  
**Goal:** Route exact, local, temporal, conflict, global, and negative questions.  
**Sprint exit:** Each gold case produces an inspectable retrieval plan.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0051 | P1 | Retrieval engineer | Define a versioned query-plan schema | Plan records query class, entities/IDs, time scope, authority policy, privacy, retrieval stages, budgets, and abstention conditions. | M2 read model |
| T-BBT-0052 | P1 | Retrieval engineer | Implement deterministic query classification | Rule-based router distinguishes identifier lookup, local fact, project resumption, temporal/update, contradiction, negative, and global questions with visible uncertainty. | Query schema |
| T-BBT-0053 | P1 | Retrieval engineer | Implement authority-policy selection | Router loads domain-specific source precedence and explicitly handles conflicts, external authority, and historical records. | Classifier |
| T-BBT-0054 | P1 | Retrieval engineer | Add bounded expansion strategies | Plans can expand via links, project membership, decisions, dependencies, temporal neighbors, and conflict relations with hard caps. | Query plan |
| T-BBT-0055 | P1 | Retrieval engineer | Score the router on the gold set | Misroutes are categorized; ambiguous cases fall back to broader evidence or abstention rather than hidden guessing. | All S10 |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S11 — Hybrid Retrieval Experiment

**Milestone:** M3 — Retrieval and Sensemaking Engine  
**Goal:** Test metadata, links, embeddings, and reranking against the baseline.  
**Sprint exit:** Adopt only methods that meet predeclared gain and cost thresholds.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0056 | P2 | Retrieval research engineer | Select two local embedding candidates and one no-embedding control | Document privacy, hardware, dimensionality, model license, update/rebuild cost, and portability. | S8 FTS baseline |
| T-BBT-0057 | P2 | Retrieval research engineer | Implement an optional embedding adapter behind a feature flag | Embeddings are disposable, keyed to content/version, and can be rebuilt without changing canonical data. | Candidate review |
| T-BBT-0058 | P2 | Retrieval research engineer | Implement rank fusion and optional reranking | Combine FTS, metadata, links, and vector similarity with an explainable configuration and deterministic candidate limits. | Embedding adapter |
| T-BBT-0059 | P2 | Retrieval research engineer | Run the hard-case benchmark | Measure gains on low-overlap and paraphrase cases plus losses on exact IDs, dates, negatives, and privacy filters. | Fusion |
| T-BBT-0060 | P2 | Retrieval research engineer | Make an explicit adopt/reject decision | Keep embeddings only if they provide material net gain within latency, privacy, maintenance, and explainability budgets; otherwise archive the experiment. | Benchmark |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S12 — Global Sensemaking and Portfolio Views

**Milestone:** M3 — Retrieval and Sensemaking Engine  
**Goal:** Answer corpus-wide questions without flattening the entire handbook.  
**Sprint exit:** Hierarchical global retrieval passes human rubrics and traces claims to evidence.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0061 | P2 | Sensemaking engineer | Build deterministic hierarchical corpus summaries | Create document, project, area, and portfolio summaries from structured fields and extracted evidence with source links and invalidation. | M2 model |
| T-BBT-0062 | P2 | Sensemaking engineer | Implement a map-reduce global question path | Retrieve relevant groups, synthesize group findings, compare across groups, and retain evidence for each global claim. | Hierarchy |
| T-BBT-0063 | P2 | Sensemaking engineer | Prototype graph extraction as a disposable experiment | Extract a bounded entity/relation graph with provenance and compare it with existing links and typed relations; never treat extracted edges as canonical. | Global baseline |
| T-BBT-0064 | P2 | Sensemaking engineer | Define and score a global-answer rubric | Rubric measures coverage, diversity, source support, contradiction disclosure, redundancy, and unsupported generalization. | Two global paths |
| T-BBT-0065 | P2 | Sensemaking engineer | Ship a portfolio drift exhibit | One real view summarizes stale projects, repeated blockers, open contradictions, missing transitions, and systemic themes with drill-down evidence. | Best global path |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S13 — Thin Flask/HTMX Observatory

**Milestone:** M4 — Operational Workbench  
**Goal:** Expose proven commands through a local web interface.  
**Sprint exit:** Diagnostics, search, evidence, and build status work without duplicating logic.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0066 | P1 | Interface engineer | Create the Flask application factory and configuration model | Tests instantiate isolated apps/databases; extensions are initialized without global app state. | M3 services |
| T-BBT-0067 | P1 | Interface engineer | Create thin blueprints for diagnostics, search, evidence, and context packs | Routes call application services and contain no domain resolution or authorization logic. | App factory |
| T-BBT-0068 | P1 | Interface engineer | Build an HTMX diagnostics browser | User can filter findings, inspect source spans, record disposition, and copy remediation commands without custom client-side state logic. | Diagnostics service |
| T-BBT-0069 | P1 | Interface engineer | Build search and evidence browser views | Results expose authority, time, match reason, citations, conflicts, and source text before any synthesis. | Search services |
| T-BBT-0070 | P1 | Interface engineer | Enforce localhost and authentication boundaries | Default bind is loopback; production/remote configuration is denied unless explicitly enabled and reviewed; security headers/CSRF apply to writes. | Web shell |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S14 — Operational Slice: Projects and Tasks

**Milestone:** M4 — Operational Workbench  
**Goal:** Migrate a narrow structured workflow with export and rollback.  
**Sprint exit:** One project can be managed in SQLite and round-tripped to Markdown/JSON.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0071 | P1 | Domain engineer | Choose one operational aggregate for the pilot | Decision names the exact project/task/transition slice, current authority, users, fields, exclusions, success measures, and rollback. | M3 evidence |
| T-BBT-0072 | P1 | Domain engineer | Model project/task aggregate invariants | Define status, next milestone/action, dependencies, readiness, completion, timestamps, and ownership without absorbing narrative knowledge. | Pilot choice |
| T-BBT-0073 | P1 | Domain engineer | Implement transactional commands and audit events | Create/update/complete/pause operations validate invariants and write one aggregate plus append-oriented audit in a transaction. | Aggregate model |
| T-BBT-0074 | P1 | Domain engineer | Implement single-owner SQLite authority and deterministic Markdown exporter | SQLite serves as single authoritative store for operational aggregates; one-way deterministic Markdown/JSON exporter prevents split-brain dual-write state. | Commands |
| T-BBT-0075 | P1 | Domain engineer | Run a real weekly-review pilot | Use the aggregate for two review cycles; measure maintenance, duplicate entry, missed work, re-entry time, and user corrections; decide continue/rollback. | Export/commands |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S15 — Transitions and Re-Entry Capsules

**Milestone:** M4 — Operational Workbench  
**Goal:** Make interrupted work easy to resume.  
**Sprint exit:** Transition records generate accurate, benchmarked re-entry capsules.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0076 | P1 | Workflow researcher | Create the transition aggregate | Fields include project, stop point, restart cue, next micro-action, resumption trigger, created/expired times, evidence, and author. | Operational pilot |
| T-BBT-0077 | P1 | Workflow researcher | Detect missing or stale transitions | Rules flag active projects without a usable transition and distinguish planned inactivity from accidental abandonment. | Transition aggregate |
| T-BBT-0078 | P1 | Workflow researcher | Compile a bounded re-entry capsule | Capsule includes current milestone, recent decisions, blockers, transition, relevant changes since last access, and first action with citations. | Transition + retrieval |
| T-BBT-0079 | P1 | Workflow researcher | Run interrupted-work experiments | Compare no plan, manual plan, and system-assisted plan across real or simulated interruptions; record time and correction burden. | Capsule |
| T-BBT-0080 | P1 | Workflow researcher | Standardize the closeout workflow only if it helps | Promote template/command when median re-entry improves without unacceptable closeout friction; otherwise simplify or abandon. | Experiment |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S16 — Routines, Recurrence, and Calendar Boundaries

**Milestone:** M4 — Operational Workbench  
**Goal:** Support recurrence and exceptions without replacing the calendar.  
**Sprint exit:** RRULE-compatible series, exceptions, and ICS export pass examples.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0081 | P2 | Temporal systems engineer | Implement an RRULE-compatible recurrence subset | Support daily/weekly/monthly interval, BYDAY, UNTIL/COUNT, timezone, and explicit unsupported-rule errors. | M4 operations |
| T-BBT-0082 | P2 | Temporal systems engineer | Generate occurrences only within requested windows | No infinite materialization; occurrence identities are stable and can be regenerated deterministically. | Recurrence parser |
| T-BBT-0083 | P2 | Temporal systems engineer | Implement exception, cancellation, and override records | Single occurrence changes do not mutate the series rule; exceptions round-trip with identity and audit. | Occurrence generation |
| T-BBT-0084 | P2 | Temporal systems engineer | Implement ICS export and reference import | Export validates in a standard calendar client; imported external events remain references unless authority is explicitly migrated. | Recurrence model |
| T-BBT-0085 | P2 | Temporal systems engineer | Create calendar edge-case fixtures | Test DST, month ends, leap day, second Tuesday, missed occurrence, reschedule, cancellation, and timezone changes. | All S16 |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S17 — Source-Grounded Conversational Synthesis

**Milestone:** M5 — Cognitive Interface  
**Goal:** Generate answers only after retrieval and conflict/abstention checks.  
**Sprint exit:** Material claims are cited and unsupported questions abstain.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0086 | P1 | AI integrator + verifier | Define the answer contract | Answer includes concise result, claim types, citations, as-of basis, conflicts, uncertainty, omissions, and abstention reason in machine/human forms. | M3 retrieval |
| T-BBT-0087 | P1 | AI integrator + verifier | Implement conflict disclosure and abstention before prose generation | Deterministic preflight blocks unsupported or unresolved answers from being rendered as settled fact. | Answer contract |
| T-BBT-0088 | P1 | AI integrator + verifier | Implement a claim-level citation verifier | Verifier checks that cited spans exist, belong to retrieved context, and plausibly support each atomic claim; failures downgrade or block output. | Synthesis pipeline |
| T-BBT-0089 | P1 | AI integrator + verifier | Run synthesis on the full regression suite | Score evidence completeness, faithfulness, temporal correctness, contradiction handling, answer relevance, and correction burden by model/version. | Verifier |
| T-BBT-0090 | P1 | AI integrator + verifier | Create a safe execution log for every synthesis | Persist query plan, context manifest, model/version, prompt version, output hash, verifier result, latency, and privacy destination. | Synthesis |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S18 — Propagation Graph and Change Impact

**Milestone:** M5 — Cognitive Interface  
**Goal:** Detect what must change when a decision or claim changes.  
**Sprint exit:** Seeded changes identify all known dependent artifacts.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0091 | P1 | Knowledge/propagation engineer | Define explicit propagation relationships | Model depends-on, summarized-by, displayed-in, indexed-by, governed-by, and supersedes/corrects relationships with provenance. | M2 relations |
| T-BBT-0092 | P1 | Knowledge/propagation engineer | Infer candidate dependency edges without promoting them | Use links, typed IDs, headings, and model suggestions to propose edges; inferred edges remain reviewable derived data. | Relationship model |
| T-BBT-0093 | P1 | Knowledge/propagation engineer | Implement impact analysis | Given a changed claim/decision/project status, list potentially stale dependents, why they depend, and confidence/severity. | Dependency graph |
| T-BBT-0094 | P1 | Knowledge/propagation engineer | Build ten propagation scenario fixtures | Include decision supersession, project pause, correction, external-authority change, privacy reclassification, and renamed record. | Impact analysis |
| T-BBT-0095 | P1 | Knowledge/propagation engineer | Implement `bbt propagate --propose` | Command emits a patch plan and unresolved questions but never edits canonical files in this sprint. | Scenario tests |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S19 — Reviewable Patch and Proposal Workbench

**Milestone:** M5 — Cognitive Interface  
**Goal:** Turn impact analysis into safe, inspectable proposed changes.  
**Sprint exit:** Users can accept/reject granular operations with precondition hashes and rollback data.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0096 | P1 | Change-control engineer | Create proposal and patch-set schema | Proposal records trigger, evidence, targets, semantic intent, file diffs, permissions needed, tests, and rollback. | S18 propagation |
| T-BBT-0097 | P1 | Change-control engineer | Implement semantic diff rendering | Review distinguishes wording changes from status/time/claim/relationship changes and shows historical content preserved. | Proposal schema |
| T-BBT-0098 | P1 | Change-control engineer | Build proposal review UI and CLI | User can approve individual hunks/targets, edit, reject with reason, defer, or mark dependency edge false. | Diff renderer |
| T-BBT-0099 | P1 | Change-control engineer | Implement a narrow Git-backed executor | Executor applies approved local Markdown patches to a clean worktree, runs validation, and creates an intentional commit or aborts atomically. | Review flow |
| T-BBT-0100 | P1 | Change-control engineer | Prove rollback and stale-proposal handling | Tests reject proposals built against changed sources and restore pre-change state after injected validation failure. | Executor |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S20 — Permission Engine and Action Firewall

**Milestone:** M6 — Adaptive Partner — Bounded  
**Goal:** Enforce domain, risk, scope, and confirmation policies.  
**Sprint exit:** Unauthorized and injected action attempts fail deterministic tests.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0101 | P0 | Security engineer | Implement structured permission grants | Grant scopes domain, action, target/path, data class, time window, max consequence, confirmation mode, and revocation. | M5 proposal layer |
| T-BBT-0102 | P0 | Security engineer | Enforce evidence/control plane separation | Retrieved Markdown context is strictly isolated in data-plane XML wrappers (<retrieved_evidence>); retrieved text cannot create grants, alter policies, or trigger unapproved tool calls. | Permission model |
| T-BBT-0103 | P0 | Security engineer | Build the deterministic action firewall | Every proposed action is checked against grants, target state, data classification, freshness, reversibility, and required confirmation. | Planes + grants |
| T-BBT-0104 | P0 | Security engineer | Create adversarial security fixtures | Test malicious Markdown/email/web text, tool-output injection, path traversal, stale grants, confused deputy, secret exfiltration, and encoded instructions. | Firewall |
| T-BBT-0105 | P0 | Security engineer | Implement pause, revoke, and kill-switch controls | One command disables monitors/connectors/actions, revokes grants, and preserves audit evidence without needing model cooperation. | Firewall |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S21 — Shadow-Mode Proactive Monitoring

**Milestone:** M6 — Adaptive Partner — Bounded  
**Goal:** Learn which warnings and preparations are useful without acting.  
**Sprint exit:** Alert precision, dismissals, interruption cost, and trust are measured.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0106 | P1 | Interaction researcher | Choose two read-only proactive monitor candidates | Select high-value low-risk rules such as expired review dates, missing transitions, or newly broken links; define expected benefit and nuisance budget. | M1 diagnostics |
| T-BBT-0107 | P1 | Interaction researcher | Run monitors in shadow mode | System records what it would have surfaced, timing, evidence, and confidence without interrupting the user. | Monitor definitions |
| T-BBT-0108 | P1 | Interaction researcher | Collect usefulness and false-alert labels | User can batch-label useful, wrong, already known, badly timed, or privacy-invasive suggestions with minimal effort. | Shadow logs |
| T-BBT-0109 | P1 | Interaction researcher | Design attention-aware delivery | Enforce quiet-by-default digest delivery for proactive nudges; bundle diagnostic warnings into session re-entry reports without intrusive popups. | Labels |
| T-BBT-0110 | P1 | Interaction researcher | Authorize, redesign, or remove each monitor | Only rules meeting utility, precision, interruption, privacy, and maintenance thresholds leave shadow mode. | Evaluation |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S22 — Limited Reversible Local Actions

**Milestone:** M6 — Adaptive Partner — Bounded  
**Goal:** Authorize a tiny set of low-risk operations after safety gates.  
**Sprint exit:** Scoped actions execute, verify, audit, and roll back with zero seeded boundary violations.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0111 | P0 | Safety-critical implementer + verifier | Select at most three reversible local actions | Candidates are generated-index refresh, approved link repair, and approved status/front-matter patch; exclude sending, publishing, deletion, and external scheduling. | M6 controls |
| T-BBT-0112 | P0 | Safety-critical implementer + verifier | Implement narrow typed executors | Each executor accepts a closed schema, validates targets, writes only authorized paths, and has no arbitrary shell/file access. | Action selection |
| T-BBT-0113 | P0 | Safety-critical implementer + verifier | Add precondition, postcondition, and rollback verification | Action runs only on expected source version, proves intended change, detects collateral changes, and can revert cleanly. | Executors |
| T-BBT-0114 | P0 | Safety-critical implementer + verifier | Run the full authorization boundary suite | Attempt unauthorized path, action type, privacy class, stale source, malicious evidence, oversized batch, and expired grant; all must fail closed. | Executors/firewall |
| T-BBT-0115 | P2 | Safety-critical implementer + verifier | Conduct a small live pilot and retrospective | Execute approved actions on real low-risk cases; measure review time, errors, trust, audit completeness, and whether autonomy saved effort. | Boundary suite |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.

## S23 — Year-One Capability Audit and Platformization

**Milestone:** M7 — Capability Platform v1  
**Goal:** Evaluate the joint system, stabilize shared infrastructure, and choose year-two bets.  
**Sprint exit:** Capability scorecard, architecture review, deprecation plan, and year-two roadmap are approved.

| ID | Pri | Owner role | Task | Acceptance test | Dependencies |
|---|---|---|---|---|---|
| T-BBT-0116 | P1 | System owner + retrospective facilitator | Run the year-one capability scorecard | Re-test recovery, diagnostics, retrieval, re-entry, temporal truth, propagation, safety, maintenance, and subjective trust against S0 baseline. | M0–M6 |
| T-BBT-0117 | P1 | System owner + retrospective facilitator | Hold a keep/simplify/remove architecture review | For every module and rule, identify measured value, cost, failure modes, and whether it should be retained, redesigned, or deleted. | Scorecard |
| T-BBT-0118 | P1 | System owner + retrospective facilitator | Stabilize public internal contracts | Version schemas for context packs, commands, exports, permissions, audit events, and adapter interfaces with migration policy. | Review decisions |
| T-BBT-0119 | P1 | System owner + retrospective facilitator | Choose year-two subsystem bets | Use evidence to prioritize voice, mobile capture, research laboratory, health preparation, relationship/contact memory, learning system, or multi-device sync—no more than two major bets. | Architecture review |
| T-BBT-0120 | P1 | System owner + retrospective facilitator | Archive the build cycle and create the next re-entry pack | Publish decisions, unresolved risks, benchmark results, migration state, operational runbooks, and first micro-action for the next cycle. | All S23 |

**End-of-sprint evidence:** code/test/report artifacts, updated risk register, milestone status, and a Ready-to-Resume record.
