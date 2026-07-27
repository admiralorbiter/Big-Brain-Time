# 01 — Current Product and Proof of Concept

## 1. Review boundary

This document combines:

- the supplied architecture and planning package;
- a static review of the current `admiralorbiter/bigbraintime` repository on 2026-07-27;
- the current project history and claimed test milestones;
- design inferences about maturity and product direction.

The repository was not independently executed as part of this package. Statements about passing test counts are therefore treated as repository-reported evidence, not fresh verification.

## 2. What the current product is

The strongest source-backed framing is not “a second-brain app.” The supplied audit identified the immediate need as accurate resumption without rereading the corpus and detection of disagreements, stale state, broken propagation, and incomplete knowledge. The larger blueprint then framed Big Brain Time as a local-first, source-grounded, temporal capability platform and a kind of knowledge compiler.

The current proof of concept combines five product identities:

1. **Personal knowledge repository** — canonical Markdown, decisions, projects, records, ideas, and views.
2. **Knowledge assurance tool** — diagnostics, identity checks, link checks, temporal and contradiction concerns.
3. **Retrieval and context compiler** — FTS, hybrid retrieval, graph traversal, project packs, handoff packets.
4. **Operational continuity tool** — project state, Ready-to-Resume plans, briefings, re-entry reports.
5. **Human–AI change-control environment** — captured claims, proposals, patches, undo, staging, review, audit, and reconciliation.

This breadth is a strength as a research prototype: it exposes how the subsystems interact. It is also a risk: each name can imply a level of completeness that the underlying implementation has not yet earned.

## 3. Current north star

The original blueprint’s product mission remains a useful anchor:

> Big Brain Time is a local-first, source-grounded, temporal personal capability platform that helps a human–AI partnership remember, resume, decide, act, learn, and improve without losing provenance, history, privacy, or human authority.

For the design phase, that mission should be paired with a more concrete product kernel:

> Preserve enough trustworthy state, perspective, and rationale to resume meaningful work; compile only the context needed for the current purpose; expose uncertainty and change; and help convert understanding into safe commitments and actions.

## 4. Current capability inventory

The repository history reports rapid delivery across a wide set of modules. The following inventory treats the implementation as a proof-of-concept capability map.

| Capability | Current proof | Likely maturity | Key unresolved product question |
|---|---|---|---|
| Canonical Markdown corpus | Established repository structure, front matter, decisions, projects, records | Piloted for Jonathan’s use | Which information types should remain Markdown-canonical forever? |
| Backup command | Manifest-bearing archive and restore-oriented documentation | Tested, restore evidence should remain recurring | What counts as an independent recovery boundary? |
| `bbt doctor` diagnostics | Parser and registry rules for known defects | Tested on seeded cases | Does it remain precise enough in daily use to avoid alert fatigue? |
| Evaluation harness | Gold cases, answer-state concepts, metrics | Prototype/tested | Are benchmarks faithful to actual workflows or overfit to seeded defects? |
| Context packs | Project-scoped token-bounded compiler | Prototype/tested | Is selection purpose-driven and claim-complete enough for real handoffs? |
| SQLite read model | Documents, sections, links, claims, migrations | Tested as projection | Is rebuild semantically deterministic, especially for identity and time? |
| FTS5 and hybrid retrieval | Lexical search, embeddings, rank fusion | Prototype/tested | Which retrieval additions provide measured net value? |
| Graph traversal | Recursive CTE neighborhood and diagnostics | Prototype/tested | Which edges are meaningful, inferred, canonical, or merely retrieval aids? |
| Capture and patching | Smart target, patch generation, atomic apply, undo | Prototype/tested | Does capture processing reduce or increase maintenance and categorization burden? |
| Synthesis engine | Claim harvesting and generated knowledge notes | Prototype | What does synthesis mean beyond collation, and how is loss evaluated? |
| Daily briefing and re-entry | Structured project summaries and transition fields | Prototype | Do they reduce time to first productive action in live use? |
| Flask workbench | Local visual interface over search, graph, patches, audit | Prototype | Which workflows genuinely require a visual interaction surface? |
| File watcher | Background indexing and event handling | Prototype/tested | Is continuous operation worth complexity compared with explicit refresh? |
| Audit ledger | JSONL events, hash chain, projection | Prototype | Does the ledger actually preserve full-event integrity and remain privacy-minimized? |
| Staging | Threshold-based ephemeral candidates | Prototype | What constitutes readiness to synthesize, and how are unrelated claims prevented? |
| Handoff packets | Typed Markdown/JSON packet concept | Prototype/tested | Can a packet be compiled from live evidence rather than hardcoded state? |
| Reconciliation | Candidate retrieval, pair adjudication, Socratic review | Prototype | Is the ontology broad enough, and are temporal/scope/authority invariants correct? |

“Maturity” here is intentionally conservative. Code and unit tests establish feasibility; they do not establish sustained usefulness, semantic completeness, or safe product behavior.

## 5. Strong foundations worth preserving

### 5.1 Local-first, inspectable sources

The system’s bias toward local operation, readable files, Git history, exportability, and replaceable models is a durable advantage. Even if some operational state migrates to SQLite, the user should retain the ability to inspect and recover meaningful information without a vendor or a particular model.

### 5.2 Canonical versus derived separation

The blueprint repeatedly distinguishes authoritative state from indexes, graphs, embeddings, context packs, and summaries. This is one of the most important architectural laws and should survive redesign.

### 5.3 Time and correction as first-class concerns

The insistence that current, historical, proposed, valid, recorded, superseded, and unresolved states differ is essential to a longitudinal personal system.

### 5.4 Re-entry as a product capability

The Ready-to-Resume protocol is unusually concrete and tied to a real cognitive friction. It gives Big Brain Time a clear user outcome rather than only a storage or search feature.

### 5.5 Human-reviewed mutation

The read → propose → review → write pattern creates a strong basis for safe AI participation. It should be refined, not discarded.

### 5.6 Evaluation and stop rules

The source package explicitly allows features to be dropped when they fail value or safety experiments. That is unusually healthy for an ambitious personal platform.

### 5.7 Shared foundations across interfaces

Keeping CLI, web, voice, API, and agents over common services is the right direction for durability and productization.

## 6. Current rough edges that matter for design

The static repository review found several issues that should be treated as **design evidence**, not merely bugs.

### 6.1 Epistemic taxonomy fragmentation

Different modules recognize different claim classes. Some distinguish interpretation, plan, and unknown; others introduce requirement, assumption, and open question. The normalized claim model currently risks defaulting unreviewed content to fully confident fact/user authority.

**Design implication:** the system needs a single conceptual model that separates object kind, source mode, stance, perspective, logical proposition, and resolution. One flat enum is unlikely to represent all of these safely.

### 6.2 Derived rebuilds may mutate epistemic meaning

The importer’s generated identities and timestamps can depend on rebuild time or line order. That means a projection rebuild can accidentally look like a new belief event.

**Design implication:** source identity, semantic identity, recorded time, build time, and database row identity must be distinct.

### 6.3 Reconciliation is not yet equivalent to reasoning

Pair adjudication can over-rely on normalized subject/predicate/object differences and simplified temporal checks. Scope, authority, population, environment, interval overlap, argument order, and evidence status need stronger invariants.

**Design implication:** candidate retrieval, logical relation, temporal resolution, authority resolution, and human review are separate stages.

### 6.4 Synthesis is currently closer to collection than compression

The current synthesis path harvests marked lines and emits a structured note. It does not yet establish semantic deduplication, information-loss boundaries, minority-view preservation, or purpose-specific evaluation. Repeated application can produce duplicated generated documents.

**Design implication:** synthesis needs its own artifact contract and idempotent lifecycle. It should not be treated as an append convenience.

### 6.5 Thresholds can create false coherence

The staging system uses claim counts as a major readiness signal and can fall back to broad claim collection. The richer source/session/duplicate/conflict criteria in the ADR are not fully reflected in the implementation.

**Design implication:** consolidation readiness is a semantic and use-driven question, not a raw volume threshold.

### 6.6 Assurance claims can be hardcoded

The handoff compiler contains repository-state claims and evidence references that can become stale. The audit hash covers only part of an event payload, and cross-process serialization requires stronger proof.

**Design implication:** Big Brain Time must apply its epistemic discipline to claims about itself. Test status, benchmark status, current revision, and evidence references should be compiled from artifacts.

### 6.7 Rapid milestone completion can hide maturity differences

The repository history reports many completed milestones in a short period. This shows remarkable prototyping throughput, but “implemented,” “tested,” “benchmarked,” “piloted,” “trusted,” and “authorized” are not interchangeable.

**Design implication:** the next phase should use maturity classes at the capability level rather than declaring broad milestones complete because their code exists.

## 7. Proof-of-concept architecture versus product architecture

The current repository is valuable partly because it compresses many experiments into one environment. A product architecture should be more selective.

### Proof-of-concept behavior

- Implement a module to make a concept tangible.
- Use a simplified schema to expose interactions.
- Optimize for fast feedback and inspectability.
- Accept hand-authored fixtures and placeholders.
- Place adjacent concerns together to learn where seams exist.

### Product architecture behavior

- Name the user outcome and quality attributes.
- Define authority and lifecycle per information type.
- Keep interfaces thin and contracts versioned.
- Distinguish generated artifacts from canonical decisions.
- Provide migration, recovery, privacy, and deletion behavior.
- Earn complexity through benchmarks and live use.
- Remove mechanisms that do not improve capability.

The design studio should not try to “clean up” the proof of concept into production one module at a time. It should first decide which modules belong in the product at all.

## 8. What to freeze during the design phase

Freeze means “preserve as a baseline,” not “declare correct.”

1. Tag or branch the current proof of concept.
2. Capture its command list, repository map, schema versions, and reported test results.
3. Preserve representative output artifacts: a briefing, context pack, handoff, synthesis note, reconciliation card, audit trace, search result, and patch flow.
4. Record current friction using the system for at least two normal weeks.
5. Avoid broad refactors that make before/after comparison impossible.
6. Allow only maintenance, recovery, and small design probes on the main line.
7. Keep new design documents separate from locked decisions until explicitly accepted.

## 9. Product surfaces visible in the prototype

The proof of concept already suggests several possible products. They should not all be assumed to be one product.

### A. Knowledge observatory

Inspect corpus state, integrity, temporal drift, conflict, provenance, search, and evidence.

### B. Project continuity workbench

Capture transition state, compile re-entry capsules, track commitments, and resume work.

### C. Research and synthesis laboratory

Ingest sources, preserve claims and perspectives, compare evidence, synthesize purpose-bound understanding, and record open questions.

### D. AI collaboration and handoff layer

Compile context and trust state for another model or collaborator; receive structured handback evidence.

### E. Personal operations platform

Projects, tasks, reminders, routines, calendar boundaries, and review triggers.

### F. Cognitive operating system

A shared kernel supporting memory, reasoning, identity, planning, learning, simulation, and action across domains.

The first four may share a near-term kernel. The last two require much more product discovery and should not be assumed to follow automatically.

## 10. Maturity map

Use this table as an editable hypothesis.

| Domain | Concept | Prototype | Tested | Benchmarked | Piloted | Trusted | Authorized |
|---|---:|---:|---:|---:|---:|---:|---:|
| Canonical Markdown practice | ✓ | ✓ | — | — | ✓ | partial | n/a |
| Recovery | ✓ | ✓ | ✓ | — | limited | unknown | n/a |
| Diagnostics | ✓ | ✓ | ✓ | limited | limited | no | read-only |
| Search | ✓ | ✓ | ✓ | limited | unknown | no | read-only |
| Temporal truth | ✓ | ✓ | partial | fixture-only | no | no | read-only |
| Context packs | ✓ | ✓ | ✓ | partial | limited | no | read-only |
| Re-entry | ✓ | ✓ | ✓ | not established | limited | no | proposal |
| Synthesis | ✓ | ✓ | partial | no | no | no | proposal only |
| Reconciliation | ✓ | ✓ | partial | narrow | no | no | review only |
| Audit | ✓ | ✓ | partial | no | no | no | internal |
| Patch/write workflow | ✓ | ✓ | ✓ | narrow | limited | no | explicit review |
| Proactive monitoring | ✓ | prototype | partial | no | no | no | shadow only |
| External action | concept | no | no | no | no | no | prohibited/default deny |

The purpose is not to criticize the prototype. It is to prevent “working code” from carrying product trust that has not yet been measured.

## 11. Keep, question, retire worksheet

Complete this after using the proof of concept rather than from memory alone.

### Keep and strengthen

| Capability or principle | Evidence it helps | What must remain true |
|---|---|---|
| | | |
| | | |
| | | |

### Keep as an experiment

| Capability | Question still being tested | Cheapest next probe |
|---|---|---|
| | | |
| | | |
| | | |

### Redesign

| Current mechanism | Rough edge | Alternative worth exploring |
|---|---|---|
| | | |
| | | |
| | | |

### Retire or simplify

| Capability or structure | Cost it creates | What simpler behavior replaces it |
|---|---|---|
| | | |
| | | |
| | | |

## 12. Design questions exposed by the prototype

1. Is accurate resumption still the strongest product wedge after live use?
2. Which classes of information need structured semantics, and which benefit from remaining narrative?
3. What is the smallest plural epistemic model that supports perspective without becoming an ontology project?
4. Can the system maintain source and time correctly without requiring every sentence to be manually classified?
5. Which summaries improve work, and which merely create more artifacts?
6. What does Jonathan actually want the system to forget, hide, archive, retract, or delete?
7. Which capabilities would still be valuable without an LLM?
8. Which capabilities should fail closed when a model or index is unavailable?
9. How much daily or weekly maintenance does the current prototype require?
10. Which subsystem would another user adopt independently of the whole platform?

## 13. Current conclusion

The current repository has achieved what a strong proof of concept should: it has turned abstract ideas into inspectable mechanisms and exposed where the real design problems are.

The right next step is not to abandon it, nor to treat it as the target. It is to preserve it as **Prototype A**, design alternative architectures and cognitive models around it, and use small experiments to determine which concepts deserve to become durable product contracts.
