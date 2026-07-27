# 03 — System Landscape and Architecture

## 1. Architectural stance

The supplied blueprint proposes a local-first modular monolith with ports and adapters, Markdown/Git narrative authority, a rebuildable SQLite read model, selected operational write models, and strict separation between evidence and control. That remains the strongest baseline architecture for the design studio.

The important change in this package is to distinguish **the product kernel** from **the current implementation modules**. The architecture should be organized around stable responsibilities and contracts, not around the order in which prototypes were built.

![Container architecture](diagrams/04_container_architecture.svg)

## 2. Architectural goals

The architecture must allow Big Brain Time to be:

- useful with or without generative synthesis;
- local and inspectable by default;
- source-grounded and temporally aware;
- able to preserve multiple perspectives;
- recoverable and exportable;
- incrementally migratable;
- model-provider independent;
- safe under untrusted retrieved content;
- testable beneath the interface layer;
- extensible across project, research, learning, and other capability packs;
- simple enough for one person to operate;
- capable of honest deletion and lifecycle reporting;
- measurable as part of a joint cognitive system.

## 3. System context

![System context](diagrams/03_system_context.svg)

### Jonathan

Jonathan is the owner, primary user, primary source of values and personal authority, and final approver of consequential changes. The system may learn explicit preferences and interaction patterns, but it does not silently become the authority on Jonathan’s identity.

### Big Brain Time

Big Brain Time owns the local product contracts, memory lifecycle, derived context, selected operational state, policies, evaluation artifacts, and user-facing continuity workflows.

### AI models

Models are replaceable reasoning and language services. Their outputs are proposals or derived artifacts unless explicitly accepted. Models do not own canonical memory, permissions, or action policy.

### External authorities

Calendars, email providers, GitHub, health portals, financial systems, and organizational tools remain authoritative for their own records unless a bounded migration decision says otherwise.

### Evidence sources

Files, web pages, email, conversations, connector results, and model outputs enter as evidence with source, time, privacy, and trust boundaries. They cannot issue runtime instructions.

### Recovery systems

Independent backups and restore procedures are part of the product architecture, not merely operations documentation.

## 4. Architectural layers

### 4.1 Interfaces

- CLI
- Flask/HTMX web workbench
- local API
- voice
- future agent or protocol adapters

Interfaces translate user interaction into application queries, commands, and proposals. They do not decide truth, authority, permission, or lifecycle.

### 4.2 Application layer

The application layer coordinates use cases:

- `CaptureArtifact`
- `BuildReentryPack`
- `ExplainCurrentState`
- `CompileContext`
- `ProposeSynthesis`
- `RecordDecision`
- `AnalyzePropagation`
- `RequestPurge`
- `EvaluateCapability`

It manages workflows and transactions but delegates domain rules to the kernel.

### 4.3 Domain kernel

The kernel contains stable concepts and policies:

- agents and perspectives;
- source artifacts and activities;
- memory items and assertions;
- valid time, recorded time, lifecycle state;
- authority rules;
- commitments and transitions;
- context contracts;
- proposal and permission rules;
- evaluation cases and maturity states.

The kernel should not import Flask, SQLAlchemy, GitHub, or model-provider types.

### 4.4 Ports

Ports express what the kernel needs without choosing implementation:

- artifact repository;
- operational repository;
- search index;
- graph/relationship query;
- model inference;
- clock and identity generation;
- policy store;
- audit writer;
- backup and export;
- connector/action executor.

### 4.5 Adapters

Adapters implement ports for Markdown, Git, SQLite, FTS5, embeddings, local or remote models, calendar, GitHub, email, filesystem, and other connectors.

### 4.6 Canonical authorities

Canonical authority is declared per information type. There is no single universal store.

### 4.7 Derived representations

Indexes, graph candidates, summaries, context packs, embeddings, dashboards, and compiled views are rebuildable or invalidatable. They carry manifests and lineage but are not sole authority for factual claims.

## 5. Authority and trust planes

![Authority and trust planes](diagrams/05_authority_and_trust_planes.svg)

Three questions must be answered independently:

1. **Where is this information stored?**
2. **Which representation is authoritative for this information type?**
3. **May this content influence control or action?**

A Markdown decision record may be authoritative evidence and still be unable to authorize a tool. A model output may be useful derived text but have no authority. A calendar event may be externally authoritative but represented locally only by a reference.

### Suggested representation classes

| Class | Meaning | Examples |
|---|---|---|
| Canonical narrative | Human-readable durable meaning | decisions, research notes, journal, rationale |
| Canonical operational | Transactional current state | selected tasks, transitions, permission grants |
| External authority | Another system owns current record | calendar, email, GitHub issue, health result |
| Derived projection | Rebuildable query structure | FTS, section table, entity candidates, embeddings |
| Compiled artifact | Purpose-specific, invalidatable output | context pack, briefing, handoff, synthesis |
| Ephemeral staging | Temporary proposal material | extraction candidates, review cards, draft relations |
| Audit evidence | Durable record of process and change | approvals, hashes, results, incidents |

## 6. One authority per information type

The source blueprint’s one-writer rule is crucial, but authority may be more granular than an entire document or database.

A project might be split as follows:

| Field or meaning | Authority |
|---|---|
| outcome and rationale | Markdown narrative |
| current operational status | SQLite aggregate after migration |
| external due date | calendar or work system |
| recent code state | GitHub repository |
| generated re-entry capsule | compiled artifact |
| AI interpretation of risk | proposal with source lineage |

This is safer than saying “the project is in SQLite” or “the project is in Markdown.”

### Authority migration contract

Any migration must state:

1. exact fields and invariants moving;
2. prior authority;
3. new authority;
4. transition period and synchronization mechanism;
5. export and rollback format;
6. conflict detection;
7. cutover evidence;
8. end date for temporary dual representation;
9. how hand-edited old representations are rejected or imported;
10. how the decision can be reversed.

## 7. Shared foundations

![Subsystem landscape](diagrams/06_subsystem_landscape.svg)

The following foundations should be implemented once and reused.

### Identity

Stable identifiers for agents, artifacts, memory items, claims, commitments, transitions, proposals, activities, and evaluation runs. IDs must survive rebuilds and not encode mutable status.

### Time

At minimum:

- event/experience time;
- source publication or occurrence time;
- valid-from and valid-to;
- recorded-at;
- build/generated-at;
- review-at;
- expiration/invalidation;
- timezone and original local representation where meaningful.

### Provenance

Who or what created, observed, reported, inferred, transformed, accepted, or executed an item; what inputs and software versions were involved; and how the output derives from source.

### Authority

Domain- and scope-specific source precedence, explicit decisions, perspective holders, and resolution behaviors such as choose, show both, abstain, or require review.

### Privacy

Classification, minimum-necessary disclosure, model destination, retention, redaction, and connector boundaries.

### Lifecycle

Draft, active, superseded, disputed, retracted, archived, suppressed, redacted, purged, expired, and invalidated are not interchangeable.

### Evaluation

Every significant behavior can be connected to fixtures, run evidence, baselines, user corrections, and maturity state.

## 8. Command, query, proposal, event

These four application concepts should remain distinct.

### Query

Requests information without changing canonical state.

Examples: `ExplainCurrentDecision`, `SearchEvidence`, `BuildPreviewContext`, `ListPurgeImpact`.

### Command

Requests a defined state change with validated intent and authority.

Examples: `RecordTransition`, `AcceptMemoryItem`, `SupersedeDecision`, `ArchiveProject`.

### Proposal

A reviewable possible set of commands, usually created by a human or model from evidence.

Examples: a patch set, a proposed relation, a synthesis draft, a reminder plan.

### Event

Records that an accepted command or external occurrence happened.

Examples: `TransitionRecorded`, `DecisionSuperseded`, `ProposalRejected`, `IndexRebuilt`.

The system does not require full event sourcing. Events are useful for projection, audit, and evaluation, while current aggregates may still be stored directly.

## 9. Core data flows

### Trusted answer

![Trusted answer pipeline](diagrams/08_trusted_answer_pipeline.svg)

A trusted answer is not a single model call. It is a pipeline with inspectable intermediate artifacts:

1. interpret query and mode;
2. determine time, authority, and privacy policy;
3. retrieve candidates;
4. expand structure within a budget;
5. resolve temporal and authority applicability;
6. expose conflicts and gaps;
7. compile a context contract;
8. generate prose or structured output;
9. verify material claims against included evidence;
10. answer, qualify, disclose conflict, or abstain.

### Proposed change

![Change propagation](diagrams/11_change_propagation.svg)

A meaningful change is represented semantically before being rendered as file or database operations. This prevents the implementation representation from hiding the intent.

### Authorized action

![Action firewall](diagrams/12_action_firewall.svg)

A model or user may propose an action graph. A deterministic policy engine evaluates risk, scope, privacy, preconditions, and confirmation. Only narrow executors perform effects.

### Memory lifecycle

![Lifecycle and purge](diagrams/13_lifecycle_and_purge.svg)

Visibility changes and destructive deletion use different workflows. Purge must enumerate all controlled representations and report residual backup retention honestly.

## 10. Architectural alternatives

The design studio should preserve at least four plausible macro-architectures.

### Option A — Markdown-centric knowledge compiler

**Description:** Markdown/Git remains canonical for nearly everything; SQLite and AI are derived tools.

**Strengths:** maximum readability, portability, simple recovery, Git review.

**Weaknesses:** transactional operations, identity, concurrency, and structured lifecycle become awkward; parsing rules can become an implicit database schema.

**Best fit:** knowledge assurance, research, project context, single technical user.

### Option B — Split-authority modular monolith

**Description:** narrative and rationale remain Markdown; selected operational aggregates and policies are SQLite-canonical; external systems remain authoritative for their domains.

**Strengths:** matches representation to use, supports transactions, preserves narrative.

**Weaknesses:** authority matrix and export discipline become essential; users can be confused about where to edit.

**Best fit:** likely near-term target for Jonathan’s personal platform.

### Option C — Event-log-centered local platform

**Description:** durable semantic events and object records are canonical; Markdown becomes a projection/export for narrative views.

**Strengths:** strong temporal history, propagation, audit, multiple interfaces.

**Weaknesses:** high implementation and migration cost, loss of direct hand editability, complex deletion and compaction.

**Best fit:** only if operational breadth and multi-interface needs clearly exceed Markdown-centric approaches.

### Option D — Federated project brains

**Description:** each project or capability pack has a bounded local memory package; a portfolio layer indexes and compiles across packages.

**Strengths:** portable, privacy-scoped, reusable, easier productization and deletion.

**Weaknesses:** cross-project identity and learning are harder; duplicated kernel metadata; global personal continuity becomes a federation problem.

**Best fit:** promising productization path and useful comparison to one monolithic personal brain.

No option should be selected globally before scenario and quality-attribute analysis.

## 11. Deployment envelopes

### Envelope 1 — Single trusted workstation

- one writer;
- localhost interfaces;
- private Git remote;
- independent encrypted backup;
- local SQLite;
- explicit context export to remote models.

This remains the simplest and safest studio baseline.

### Envelope 2 — Multiple personal devices, single active writer

- capture inboxes from multiple devices;
- one authoritative processing node;
- explicit lease or ownership transfer;
- no live copied SQLite database;
- synchronization evidence and conflict reporting.

### Envelope 3 — Private multi-device replication

Requires measured need, identity and conflict semantics, encrypted transport, schema migration coordination, and recovery testing. CRDTs or append-log replication are options, not defaults.

### Envelope 4 — Multiple people

Requires consent, role-based and item-level access, speaker-grounded perspectives, deletion rights, organizational authority, and social conflict governance. This is a distinct product architecture.

## 12. Architecture fitness functions

Instead of relying only on review, the architecture should have executable or inspectable fitness functions:

- delete and rebuild derived stores without semantic loss;
- identical source revision produces stable semantic identities;
- every material generated claim has source lineage;
- every authority migration has one active writer;
- every context pack names purpose, time, privacy, sources, omissions, and version;
- every action proposal has scoped targets and preconditions;
- every destructive lifecycle operation enumerates replicas;
- no untrusted evidence can create a grant or execute a tool;
- a provider change does not make canonical memory unreadable;
- a feature can be disabled without corrupting the kernel;
- weekly maintenance remains under the accepted budget.

## 13. Architecture review questions

1. Which domain concepts are genuinely stable enough for the kernel?
2. Which current modules are experiments rather than permanent services?
3. Which quality attributes dominate the next product wedge?
4. Where does a narrative need to remain whole?
5. Which authority boundaries are understandable to a non-developer?
6. What is the smallest useful deployment envelope?
7. What fails when AI synthesis is unavailable?
8. What fails when the read model is stale or absent?
9. What can be exported and understood ten years later?
10. How does the system tell Jonathan that its own architecture claim is stale?
