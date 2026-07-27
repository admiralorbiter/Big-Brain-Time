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

Jonathan is the owner, primary user, primary source of values and personal authority, and final approver of consequential changes. He authors, ratifies, revises, overrides, suspends, and deprecates methods and policies. The system may learn explicit preferences and interaction patterns, but it does not silently become the authority on Jonathan’s identity, goals, or commitments.

### Big Brain Time

Big Brain Time owns the local product contracts, memory lifecycle, derived context, selected operational state, policies, evaluation artifacts, and user-facing continuity workflows.

### AI models

Models are replaceable reasoning and language services. Their outputs are proposals or derived artifacts unless explicitly accepted. Models do not own canonical memory, permissions, or action policy.

### Other people and institutions

Stakeholders, teams, communities, and counterparties are autonomous participants with their own values, interpretations, permissions, expectations, rights, memories, and capacity to disagree. They are not external systems to query or modify. Their statements and commitments remain attributable, and their participation is governed by consent and social authority as well as technical access.

### Instrumented external authorities

Calendars, email providers, GitHub, health portals, financial systems, and organizational tools remain authoritative for their own records unless a bounded migration decision says otherwise.

### Uninstrumented reality

Conversations, lived events, tacit knowledge, physical conditions, and effects on people may not be directly machine-observable. They enter through human capture, testimony, or later reconciliation. Absence from an API is not evidence that they did not occur.

### Observation and evidence sources

Files, web pages, email, conversations, connector results, measurements, and model outputs enter as observations or source material with time, privacy, and trust boundaries. Interpretation, claim formation, corroboration, acceptance, and verification are distinct transitions. Retrieved content cannot issue runtime instructions.

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
- `EstablishActiveFrame`
- `AllocateAttention`
- `BuildReentryPack`
- `ExplainCurrentState`
- `CompileContext`
- `ProposeSynthesis`
- `RecordDecision`
- `AnalyzePropagation`
- `PrepareAndVerifyAction`
- `RepairCommonGround`
- `EnterDegradedMode`
- `RequestPurge`
- `EvaluateCapability`

It manages workflows and transactions but delegates domain rules to the kernel.

### 4.3 Domain kernel

The kernel contains stable concepts and policies:

- agents and perspectives;
- source artifacts and activities;
- memory items and assertions;
- values, goals, commitments, plans, and tasks as distinct types;
- active cognitive frames and attention policies;
- valid time, recorded time, lifecycle state;
- authority rules;
- commitments and transitions;
- epistemic-state transitions;
- collaborator capability, context, and common-ground records;
- system-health and degraded-mode rules;
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
- collaborator registry;
- system-health monitor;
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

### Active frame

Purpose, protected commitments, open questions, assumptions, contradictions, attention budget, interruption threshold, participants, context gaps, and expiry conditions for the current cognitive episode.

### Epistemic state

Observed, interpreted, inferred, accepted, decided, verified, disputed, and superseded states remain distinguishable and carry source, scope, recency, contradictions, dependencies, and promotion authority.

### Collaboration state

Who knows what, which sources each participant has seen, current assignment, strengths, limitations, permissions, believed objective, and evidence of common-ground mismatch.

### System health

Dependency status, stale or missing context, model and policy version changes, unresolved incidents, degraded capabilities, fallback behavior, recovery conditions, and review load.

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

## 9. Joint cognitive operating loop

The architecture supports a closed control loop:

1. **Attend:** establish or refresh the active cognitive frame; protect commitments and allocate a bounded attention budget.
2. **Sense:** select authorized observations from people, artifacts, tools, and uninstrumented reality.
3. **Frame:** declare purpose, mode, scope, assumptions, roles, decision rights, context gaps, and health limits.
4. **Generate:** retrieve, reason, synthesize, and propose alternatives.
5. **Challenge:** test provenance, contradictions, circular support, correlated collaborators, goal drift, and uncertainty.
6. **Decide:** Jonathan or another authorized human accepts, rejects, defers, delegates, or abstains.
7. **Act:** record predicted effects, apply policy, obtain authorization, and execute through a narrow adapter.
8. **Verify:** observe external state independently, compare it with the prediction, and close, roll back, or capture an incident.
9. **Adapt:** use outcomes, burden, incidents, and system-health evidence to propose method or policy changes for ratification.

The active frame is control state, not a larger context pack. It determines what should enter the pack and what should be surfaced, deferred, challenged, or ignored.

### Attention allocation

Attention routing uses a declared policy over:

- purpose and goal relevance;
- endangered commitments and deadlines;
- consequence and value sensitivity;
- uncertainty and contradiction;
- novelty and independent evidence;
- reversibility and cost of delay;
- expected human advantage;
- interruption and switching cost;
- current human and system capacity.

Model confidence is one diagnostic input at most. It does not reliably identify model error and must not become the default proxy for human-review value.

### Common-ground repair

When collaborators appear to operate from different objectives, scopes, assumptions, or source sets, the workflow pauses propagation and action long enough to compare compact statements of:

- what each participant believes the objective is;
- what decision is being requested;
- which evidence and constraints each has seen;
- which roles and permissions each holds;
- which disagreement is factual, interpretive, normative, or procedural.

### Cognitive immune response

Potential prompt injection, unsupported claims, suspicious source changes, circular citations, silent goal drift, policy violations, canonical disagreement, and confident low-context output trigger a governed response: label, quarantine, challenge, request corroboration, or escalate. Immune responses alter retrieval, promotion, and action eligibility but do not declare truth by themselves.

## 10. Core data flows

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

### Authorized and verified action

![Action firewall](diagrams/12_action_firewall.svg)

A model or user may propose an action graph. Completion requires the full lifecycle:

1. proposal;
2. expected-outcome and impact prediction;
3. deterministic policy, scope, privacy, and precondition check;
4. human authorization where required;
5. narrow execution;
6. independent postcondition observation;
7. reconciliation of expected and actual state;
8. closure, rollback, or incident capture;
9. propagation into commitments, artifacts, evaluations, and calibration evidence.

Read and write boundaries are separate. Observation is authorized and treated as potentially stale, incomplete, manipulated, or misinterpreted. Action is independently authorized. A tool response proves only what the tool can attest to.

### Memory lifecycle

![Lifecycle and purge](diagrams/13_lifecycle_and_purge.svg)

Visibility changes and destructive deletion use different workflows. Purge must enumerate all controlled representations and report residual backup retention honestly.

## 11. Architectural alternatives

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

## 12. Deployment envelopes

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

## 13. Architecture fitness functions

Instead of relying only on review, the architecture should have executable or inspectable fitness functions:

- delete and rebuild derived stores without semantic loss;
- identical source revision produces stable semantic identities;
- every material generated claim has source lineage;
- every authority migration has one active writer;
- every context pack names purpose, time, privacy, sources, omissions, and version;
- every action proposal has scoped targets and preconditions;
- every consequential action declares predicted effects and verification evidence;
- execution success cannot close an action whose external postcondition is unverified;
- every active frame declares purpose, protected commitments, context gaps, attention budget, and expiry;
- every interruption can explain why it outranks deferral;
- every collaborator assignment declares role, source set, limitations, and permissions;
- every degraded capability changes permitted behavior and names a recovery condition;
- policies and methods carry status, version, ratification evidence, and supersession;
- every destructive lifecycle operation enumerates replicas;
- no untrusted evidence can create a grant or execute a tool;
- a provider change does not make canonical memory unreadable;
- a feature can be disabled without corrupting the kernel;
- weekly maintenance remains under the accepted budget.

## 14. Architecture review questions

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
11. What is the smallest active frame that materially improves control?
12. Which observations are trustworthy enough to verify consequential action?
13. How are correlated collaborator errors detected when multiple models inherited the same premise?
14. What does each degraded mode forbid, and how is normal operation restored?
15. Which policies are constitutional, operational, provisional, suspended, or deprecated?
