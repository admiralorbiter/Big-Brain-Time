# 08 — Architecture Decision Proposals

These are proposed decision records, not silent edits to the existing decision log. Each should be accepted, amended, or rejected through Big Brain Time’s normal process.

## ADR-P01 — Define the product as a Knowledge Assurance and Context Engine

**Status:** Proposed  
**Choice:** The first product is an assurance, retrieval, temporal-truth, and context-compilation system—not a general second-brain UI.  
**Rationale:** Directly addresses the observed failures and the stated need for accurate resumption and contradiction warning.  
**Reconsider if:** Another workflow produces greater measured capability value.

## ADR-P02 — Supersede D-BBT-015 narrowly

**Status:** Proposed  
**Choice:** Permit SQLite now as a disposable read model because the concrete query/integrity threshold has been crossed; continue to defer broad SQLite-canonical migration.  
**Rationale:** Reconciles the earlier deferral with the later audit without abandoning Markdown/Git authority.  
**Reconsider if:** A text-only index meets all retrieval and diagnostic requirements with lower maintenance.

## ADR-P03 — Use explicit authority by information type

**Status:** Proposed  
**Choice:** Maintain a versioned authority matrix for narrative, operational, external, and derived data.  
**Rationale:** Prevents duplicate systems of record and makes migration tractable.  
**Reconsider if:** Authority rules become too granular to maintain; simplify by aggregate.

## ADR-P04 — Adopt a modular monolith with ports and adapters

**Status:** Proposed  
**Choice:** Domain/application services are independent of CLI, Flask, voice, models, and storage adapters.  
**Rationale:** Supports testing, local use, multiple interfaces, and incremental replacement without distributed-system overhead.  
**Reconsider if:** A subsystem requires independent scaling or a distinct security boundary.

## ADR-P05 — CLI-first, Flask second

**Status:** Proposed  
**Choice:** Every capability is proven through commands/services before receiving a web screen.  
**Rationale:** Keeps automation testable and prevents UI logic from becoming the architecture.  
**Reconsider if:** A workflow can only be meaningfully evaluated through interaction design.

## ADR-P06 — Treat the read database as compiler output

**Status:** Proposed  
**Choice:** Read-model SQLite may be deleted and rebuilt from canonical sources; its manifest binds corpus commit, schema, and importer version.  
**Rationale:** Preserves reversibility and makes stale projection state detectable.  
**Reconsider if:** Derived state becomes too expensive to rebuild; then add cache layers without changing authority.

## ADR-P07 — Use deterministic retrieval before model synthesis

**Status:** Proposed  
**Choice:** Exact lookup, FTS, time/authority filtering, structural expansion, and conflict scanning precede LLM use.  
**Rationale:** Long context alone is unreliable and opaque.  
**Reconsider if:** A future model can demonstrably meet the same evidence, temporal, and abstention gates without retrieval—but retain evaluation.

## ADR-P08 — Separate local and global query strategies

**Status:** Proposed  
**Choice:** Use targeted retrieval for local questions and hierarchical/graph-assisted sensemaking for corpus-wide questions.  
**Rationale:** Different query classes fail under different retrieval designs.  
**Reconsider if:** One measured strategy handles both with lower complexity.

## ADR-P09 — Use a minimal provenance and bitemporal claim model

**Status:** Proposed  
**Choice:** Store sources, agents, activities, claims, evidence, valid time, recorded time, and correction relations; do not implement full RDF PROV.  
**Rationale:** Supports current/historical truth and trust without ontology overhead.  
**Reconsider if:** Interoperability requires a fuller standard mapping.

## ADR-P10 — Reuse RFC 5545 recurrence semantics

**Status:** Proposed  
**Choice:** Store recurrence using RRULE-compatible definitions and explicit exceptions.  
**Rationale:** Avoids inventing subtle calendar behavior.  
**Reconsider if:** The operational model needs only a simpler strict subset; remain export-compatible.

## ADR-P11 — Never allow model-direct canonical writes

**Status:** Proposed  
**Choice:** Model outputs become typed proposals. Deterministic commands execute only after policy and required review.  
**Rationale:** Protects provenance, authority, privacy, and authentic voice.  
**Reconsider if:** Low-risk generated artifacts are proven safe; those can receive narrow scoped authorization.

## ADR-P12 — Separate evidence and control planes

**Status:** Proposed  
**Choice:** Retrieved content is untrusted evidence and cannot issue runtime instructions.  
**Rationale:** Mitigates indirect prompt injection and tool poisoning.  
**Reconsider if:** Never; implementation techniques may evolve, but the boundary remains.

## ADR-P13 — Introduce autonomy through shadow mode

**Status:** Proposed  
**Choice:** Proactive rules and actions begin as logged suggestions, then preparation, then narrowly reversible local actions.  
**Rationale:** Measures usefulness and false alerts before consequences.  
**Reconsider if:** A safety-critical reminder requires immediate behavior; handle as a separate explicit rule, not general autonomy.

## ADR-P14 — Make export and restore acceptance criteria

**Status:** Proposed  
**Choice:** Every canonical migration and release includes export, isolated restore, integrity checks, and rollback evidence.  
**Rationale:** Local-first ownership creates a responsibility to prove recovery.  
**Reconsider if:** Never; mechanisms may change.

## ADR-P15 — Evaluate coordination cost and human capability

**Status:** Proposed  
**Choice:** Score features on time-to-action, corrections, re-explanations, maintenance, cognitive burden, trust, and task outcomes alongside technical metrics.  
**Rationale:** The unit of design is the joint cognitive system.  
**Reconsider if:** Metrics create more burden than insight; reduce instrumentation rather than abandoning the principle.

## ADR-P16 — Do not adopt CRDTs until concurrent writing is observed

**Status:** Proposed  
**Choice:** Use a single-writer assumption and existing Git/file sync in year one; instrument multi-device conflicts.  
**Rationale:** CRDTs solve a real but currently unproven problem and add data-model complexity.  
**Reconsider if:** Measured concurrent offline edits become frequent or collaboration expands.

## ADR-P17 — Embeddings and graph indexes are benchmark-gated

**Status:** Proposed  
**Choice:** Add embeddings or generated knowledge graphs only if they materially improve the hard-case regression set.  
**Rationale:** Avoids novelty-driven infrastructure and model lock-in.  
**Reconsider if:** New requirements cannot be met lexically/structurally.

## ADR-P18 — Use append-oriented correction, not destructive truth replacement

**Status:** Proposed  
**Choice:** Preserve superseded claims and decisions with explicit correction links.  
**Rationale:** Enables as-of reasoning, trust repair, and explanation of change.  
**Reconsider if:** Privacy or legal deletion requirements mandate erasure; record a tombstone where permitted.

## ADR-P19 — Treat transition state as a core domain aggregate

**Status:** Proposed  
**Choice:** Stop point, restart cue, next micro-action, and resumption trigger are structured and versioned.  
**Rationale:** Graceful re-entry is the product’s primary capability, not a side note.  
**Reconsider if:** Live use shows a smaller or different field set predicts resumption better.

## ADR-P20 — Preserve model independence

**Status:** Proposed  
**Choice:** Canonical memory, context packs, evaluation cases, and proposals use provider-neutral Markdown/JSON formats.  
**Rationale:** Supports longevity, comparison, privacy routing, and future local models.  
**Reconsider if:** A provider-specific feature offers exceptional value; use it as a cache/adapter, never the sole canonical layer.


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
