# 01 — Research Synthesis and Design Implications

This synthesis starts from the problems evidenced in the supplied corpus and uses outside research only to constrain architecture choices.

## 1. Local-first ownership and incremental migration

### Evidence

**[SOURCE]** Big Brain Time explicitly values plain Markdown, Git history, portability, privacy, zero tool lock-in, canonical-versus-view separation, and graceful re-entry. [S1, Architecture; Philosophy; D-BBT-001–D-BBT-026]

**[RESEARCH]** Local-first software prioritizes local data as the primary copy and treats offline operation, multi-device use, longevity, privacy, and user control as first-class qualities. The same literature presents CRDTs as a promising foundation for collaboration, not a universal prerequisite. [R01]

**[RESEARCH]** Incremental legacy displacement research argues against big-bang replacement. It recommends breaking the system into parts, finding seams, maintaining a transitional architecture, and preserving the ability to reverse decisions. [R02][R03]

### Design implication

Adopt a **strangler migration around information authority**:

- Markdown/Git remains canonical for narrative knowledge and historical records.
- A read-only index is introduced without changing writers.
- One operational aggregate—projects/tasks/transitions—is migrated only after measured value.
- Old and new representations are not both writable. During each migration, one is authoritative and the other is an export or projection.
- Every migrated aggregate has a rollback procedure and a canonical export fixture.

### Architecture rejection

Reject long-lived application-level dual writes. They create split-brain state when one write succeeds and the other fails, and they obscure which representation is authoritative. If a transition needs temporary synchronization, use an outbox/change-log pattern with reconciliation and an explicit end date.

## 2. SQLite is appropriate—but only with operational discipline

### Evidence

**[RESEARCH]** SQLite provides built-in FTS5 for phrase, prefix, proximity, boolean, and ranked full-text retrieval. [R04] The online backup API creates a consistent snapshot of a live database; `VACUUM INTO` creates a compact copy. [R05][R06] STRICT tables provide per-table type enforcement and integrate with integrity checks. [R07]

### Design implication

Use SQLite for:

- Rebuildable documents, sections, links, typed records, diagnostics, provenance projections, and FTS5 indexes.
- Later, carefully selected operational aggregates with transactions and constraints.
- Local evaluation logs and action audit trails.

Do not treat copying the `.db` file as a complete backup strategy, especially under WAL. Use the backup API or `VACUUM INTO`, record checksums, and prove restore into an isolated directory. Run `PRAGMA integrity_check`, schema-version checks, row-count checks, and application-level invariants after restore.

Use:

- `PRAGMA foreign_keys = ON`
- STRICT tables where practical
- explicit schema migrations and `user_version`
- deterministic import order
- normalized timestamps
- idempotent rebuilds
- a database manifest containing corpus commit, importer version, schema version, and build time

## 3. Modular Flask, not a web-shaped architecture

### Evidence

**[SOURCE]** The proposed architecture places Flask, CLI, voice, and future agents over the same domain services. [S2, lines 61–85]

**[RESEARCH]** Flask’s application-factory and blueprint patterns make it possible to create multiple configured instances, support testing, and keep extensions unbound until app creation. [R08]

### Design implication

Build a **modular monolith**:

- `domain/` contains entities, policies, and invariants.
- `application/` contains use cases and commands.
- `adapters/` contains Markdown, SQLite, Git, calendar, model, and connector implementations.
- `interfaces/cli/`, `interfaces/web/`, `interfaces/voice/`, and `interfaces/api/` contain thin delivery code.

Every feature must work through a service or command before receiving a Flask screen. This keeps tests fast and prevents the browser from becoming the only usable interface.

## 4. Long context is not reliable memory

### Evidence

**[RESEARCH]** Lost in the Middle shows that models may perform substantially worse when relevant information appears in the middle of a long input. [R11] RULER shows that simple “needle” tests overstate effective context and that multi-hop and aggregation tasks degrade earlier. [R12] NoLiMa demonstrates sharper degradation when questions and evidence have limited literal overlap. [R13]

**[RESEARCH]** LongMemEval identifies long-term memory tasks including information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention; it reports substantial performance drops even for strong systems and finds gains from session decomposition, fact-oriented keys, and time-aware query expansion. [R14]

### Design implication

Do not send the entire handbook and assume the model “has the context.” Build an evaluated retrieval system with:

- query classification
- authority and time filtering
- lexical retrieval as the first baseline
- metadata and link expansion
- conflict and supersession scans
- bounded context packs
- source-level citations
- explicit abstention
- a regression suite that includes low lexical overlap and evidence in awkward positions

The full handbook remains useful for global audits and comparison, but it is not the default operational context.

## 5. Local questions and global questions require different retrieval

### Evidence

**[RESEARCH]** Conventional retrieval-augmented generation is well suited to local questions about specific facts but is weak at corpus-level sensemaking. GraphRAG uses entity/relationship extraction and hierarchical community summaries to answer global questions more comprehensively. [R15]

### Design implication

Route queries into at least two retrieval families:

- **Local evidence retrieval:** identifiers, project state, exact decisions, current tasks, source-grounded questions.
- **Global sensemaking:** themes, cross-project patterns, systemic drift, contradictions across areas, portfolio analysis.

Start global retrieval with deterministic hierarchy and map-reduce summaries. Add graph construction only if the benchmark shows it outperforms simpler section, link, and metadata aggregation. GraphRAG is a research direction, not a mandatory dependency.

## 6. Provenance and bitemporal truth are central—not metadata garnish

### Evidence

**[SOURCE]** The handbook distinguishes facts, observations, interpretations, hypotheses, decisions, plans, and unknowns; it treats dates as part of knowledge and preserves rationale and reconsideration triggers. [S1, How to Use; Architecture; Decision Log]

**[RESEARCH]** W3C PROV distinguishes entities, activities, and agents and supports derivation, versioning, responsibility, and trust judgments. [R09][R34] Temporal database research distinguishes **valid time**—when a claim applies in the modeled world—from **transaction/recorded time**—when the system learned or stored it. [R33]

### Design implication

Use a small provenance model, not full RDF:

- `source_artifact`: the record or external source.
- `activity`: import, extraction, synthesis, correction, decision, or migration.
- `agent`: Jonathan, an AI model, a script, or an external authority.
- `claim`: a typed assertion with valid-time and recorded-time ranges.
- `evidence_link`: how a source supports, contradicts, or qualifies a claim.
- `claim_relation`: supersedes, corrects, conflicts-with, depends-on, or derives-from.

“Current truth” becomes a query governed by authority, time, supersession, and unresolved conflict—not a mutable paragraph selected by recency alone.

## 7. Recurrence should reuse calendar semantics

### Evidence

**[RESEARCH]** iCalendar RFC 5545 defines recurrence rules, recurrence dates, exception dates, and instance identifiers. It already handles concepts such as “every second Tuesday,” finite counts, and exceptions. [R10]

### Design implication

Represent a recurring responsibility as:

- one series definition
- an RRULE-compatible recurrence expression
- generated occurrences in a bounded window
- explicit exception/cancellation/override records
- external calendar references where another system is authoritative

Do not store every future occurrence indefinitely, and do not invent a custom recurrence language.

## 8. Re-entry plans are a cognitive intervention

### Evidence

**[SOURCE]** Big Brain Time standardizes a 90-second Ready-to-Resume protocol with Stop Point, Restart Cue, Next Micro-Action, and Resumption Trigger. [S1, Cognitive Closure; D-BBT-018]

**[RESEARCH]** Research on attention residue shows that unfinished prior work can impair subsequent task performance. Ready-to-resume plans and specific plan-making can reduce intrusive goal activation and support later resumption. [R23][R24]

### Design implication

Treat transition state as a first-class operational entity. A project is not “resumable” merely because it has notes. It needs a current, timestamped transition record and a low-friction next action. Measure time from opening a project to the first productive action.

## 9. Saving information is not making it usable

### Evidence

**[SOURCE]** The handbook adopts Utility Before Storage and rejects raw link dumps. [S1, Principle 15; D-BBT-023]

**[RESEARCH]** Keeping Found Things Found research found that dedicated bookmarking often fails because saved items lack workflow integration, context, and reminding mechanisms. [R26]

### Design implication

Every processed capture should have:

- why it matters
- its claim or information type
- canonical destination or project link
- source/provenance
- a future retrieval or reminding condition
- a discard/archive decision if it has no use

The ingestion pipeline must optimize capture-to-use conversion, not volume.

## 10. Managed forgetting should control visibility, not destroy history

### Evidence

**[SOURCE]** Big Brain Time distinguishes Delete, Archive, Suppress, and Supersede and separates operational relevance from preservation value. [S1, Principle 17; D-BBT-025]

**[RESEARCH]** Managed Forgetting and memory buoyancy research models gradual reduction of prominence while retaining long-term availability and context-sensitive resurfacing. [R27]

### Design implication

Ranking can incorporate:

- current project membership
- explicit pinning
- access and update history
- review dates
- open dependencies
- recency decay
- preservation class
- semantic or link proximity to active work

But automatic low-buoyancy suppression must be reversible, explainable, and testable for hidden-vital-context failures.

## 11. Human–AI systems require mixed initiative and shared mental models

### Evidence

**[SOURCE]** The handbook defines six initiative levels—Retrieve, Suggest, Prepare, Act, Monitor, Negotiate—and argues that the unit of improvement is Jonathan + AI + language + artifacts + methods + training. [S1, Mixed-Initiative; Philosophy]

**[RESEARCH]** Mixed-initiative research emphasizes timing, uncertainty, user goals, and the cost of interruption. Human–AI interaction guidelines distinguish behavior across initial use, normal use, error, and adaptation. Levels-of-automation research shows that automation can apply differently to information acquisition, analysis, decision selection, and action implementation. [R20][R21][R22]

### Design implication

Initiative is not one global switch. Define permission by:

- domain
- action type
- reversibility
- target scope
- evidence confidence
- urgency
- interruption cost
- external consequence
- current user mode

Start every proactive feature in shadow mode. Measure useful suggestion rate, false-alert rate, dismissals, interruption cost, and trust repair after error.

## 12. Retrieved content is an attack surface

### Evidence

**[RESEARCH]** Indirect prompt injection can place malicious instructions inside webpages, documents, or other retrieved content and manipulate tool-using models. [R17] NIST’s generative-AI risk profile recommends lifecycle risk management, and OWASP guidance stresses prompt injection, privilege control, monitoring, and separation of trusted instructions from untrusted content. [R18][R19][R35]

### Design implication

Implement two planes:

- **Evidence plane:** documents, email, web pages, notes, search results, attachments. Never executable as instructions.
- **Control plane:** user request, system policy, approved workflow, tool schemas, and deterministic authorization.

The model may read evidence and propose an action graph. A policy engine validates every node. Canonical writes and external effects are executed by narrow commands with typed arguments, not by free-form instructions extracted from content.

## 13. Evaluation must extend beyond answer accuracy

### Evidence

**[SOURCE]** Proposed measures include time to first productive action, corrections, source accuracy, contradiction recall, false-warning rate, maintenance time, repeated explanations, capture-to-use conversion, reminders acted upon, decisions understood, long-gap resumption, cognitive burden, and trust. [S2, lines 237–258]

**[RESEARCH]** RAG evaluation work commonly separates context relevance, answer faithfulness, and answer relevance. [R31][R32] Joint cognitive systems research argues that system properties belong to the organized human-artifact arrangement rather than an isolated component. [R28][R29][R30]

### Design implication

The primary scorecard should combine:

- retrieval/evidence quality
- temporal and contradiction handling
- action safety
- recovery and reversibility
- human coordination cost
- real task resumption
- maintenance burden
- subjective trust

A feature that improves benchmark accuracy but increases weekly maintenance or user corrections may be a net regression.

## 14. Research-derived architecture summary

| Evidence cluster | Constraint placed on the system |
|---|---|
| Local-first + incremental displacement | Local ownership, exports, seams, reversible migration, no big bang |
| Long-context evaluation | Retrieval and compression must be benchmarked; full corpus is not memory |
| Graph/global RAG | Separate local fact retrieval from corpus-wide sensemaking |
| Provenance + temporal DBs | Claims need source, agent, derivation, valid time, recorded time, and correction |
| iCalendar | Reuse recurrence and exception semantics |
| Attention residue | Store explicit transition state and measure re-entry |
| PIM + managed forgetting | Optimize contextual use and selective visibility, not capture volume |
| Mixed initiative | Domain-scoped, risk-scoped autonomy; shadow mode before action |
| Prompt injection | Separate evidence/control planes; least privilege and policy checks |
| Joint cognitive systems | Evaluate the full human–AI workflow and coordination burden |


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
