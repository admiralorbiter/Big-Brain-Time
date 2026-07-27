# 10 — Generalization and Productization

## 1. The generalization challenge

Big Brain Time is powerful partly because it is grounded in Jonathan’s real corpus, habits, language, projects, and willingness to edit Markdown and inspect technical artifacts. Those conditions cannot be assumed for another user.

Productization should therefore not mean “make Jonathan’s entire system configurable.” It should identify which concepts are universal, which are profile-specific, which are capability-specific, and which are artifacts of the current prototype.

![Productization layers](diagrams/15_productization_layers.svg)

## 2. Product layers

### 2.1 Universal kernel

The kernel should remain small and domain-neutral.

Candidate contracts:

- `Agent`
- `Perspective`
- `SourceArtifact`
- `Activity`
- `MemoryItem`
- `Stance`
- `Assertion`
- `Commitment`
- `Relation`
- `LifecycleState`
- `AuthorityRule`
- `ContextContract`
- `Proposal`
- `PermissionGrant`
- `EvaluationCase`
- `RunEvidence`

Universal infrastructure:

- stable identity;
- time and provenance;
- privacy classification;
- source and model manifests;
- import/export;
- query and command envelopes;
- adapter interfaces;
- audit and evaluation;
- schema and policy versioning.

### 2.2 Profile and policy layer

A profile configures the kernel for a person, project, group, or organization.

It contains:

- vocabulary and aliases;
- life areas and project categories;
- authority priorities;
- privacy defaults;
- retention rules;
- initiative preferences;
- notification budgets;
- interaction and accessibility preferences;
- accepted personal constraints;
- allowed model destinations;
- explicit values relevant to decision support.

A profile is inspectable data, not hidden model weights.

### 2.3 Capability packs

A capability pack combines domain semantics, workflows, views, prompts, evaluation cases, and integrations.

Examples:

- project continuity;
- research and evidence synthesis;
- learning and practice;
- writing and publication;
- software engineering;
- health appointment preparation;
- home operations;
- media reflection;
- team decision memory.

A pack may define its own object payloads and policies while using kernel identity, provenance, time, lifecycle, context, permission, and evaluation contracts.

### 2.4 Workflow compositions

A product experience may combine several packs.

A “project brain” might use:

- project continuity;
- research;
- decisions;
- handoff;
- code/GitHub adapter;
- re-entry evaluation.

A “learning brain” might use:

- source ingestion;
- concept memory;
- practice and procedural memory;
- spaced prospective triggers;
- reflection;
- learning evaluation.

### 2.5 Interfaces and adapters

Interfaces remain thin over the same use cases. Packs should not create separate memory systems for voice, web, or agents.

### 2.6 Deployment envelope

The same product contracts may operate as:

- a local technical-user repository;
- a desktop/local web application;
- a portable project package;
- a private device-synced system;
- an organizational deployment with stricter governance.

Deployment changes security and social assumptions and must be explicit.

## 3. The most plausible reusable products

### Product A — Project Brain Package

A portable, local-first package that preserves project outcome, state, decisions, evidence, research, handoffs, transitions, and evaluation.

**Target user:** individuals or small technical teams managing long-lived complex projects.

**Core promise:** return after a gap or hand off to another person/model without reconstructing the project.

**Why promising:** bounded scope, measurable value, easier privacy and deletion, natural Git integration, directly grounded in the current prototype.

**Minimum capabilities:** source inventory, decision/rationale records, re-entry capsule, context pack, search, change impact, export.

### Product B — Research Memory Workbench

A local evidence and synthesis environment for papers, notes, experiments, competing hypotheses, and research questions.

**Core promise:** preserve evidence and perspective while producing purpose-bound, cited syntheses that can be updated rather than rewritten from scratch.

**Why promising:** strong differentiation from generic note apps; tests epistemic plurality and consolidation.

**Risks:** research source ingestion and citation fidelity; users may prefer established tools; synthesis value must exceed workflow overhead.

### Product C — Knowledge Assurance Layer

A CLI/library/workbench that audits a Markdown or document corpus for identity, links, staleness, temporal conflict, source gaps, and context-pack readiness.

**Core promise:** make an existing knowledge base trustworthy enough for human and AI use.

**Why promising:** narrow, technical, compatible with many existing systems, less invasive than replacing storage.

**Risks:** diagnostic precision and false-warning fatigue; difficult to generalize beyond opinionated conventions.

### Product D — Personal Capability Platform

The full longitudinal personal brain across projects and life domains.

**Core promise:** continuity, personalized context, perspective, planning, and safe initiative across years.

**Why compelling:** largest augmentation potential.

**Why later:** privacy, identity modeling, lifecycle, maintenance, and domain boundaries require substantial evidence.

### Product E — Shared Team Brain

A multi-perspective project and organizational memory.

**Core promise:** preserve rationale, responsibility, disagreement, and handoff across team change.

**Why distinct:** requires consent, social authority, access control, speaker grounding, and organizational governance. It should be treated as a separate product line, not merely multi-user mode.

## 4. Product kernel test

A concept belongs in the universal kernel only if:

1. at least three materially different capability packs need it;
2. its meaning is stable across those packs;
3. implementing it once improves interoperability or safety;
4. the shared contract is simpler than duplicated domain versions;
5. its lifecycle and migration can be versioned;
6. users can understand or safely ignore it;
7. it does not smuggle Jonathan-specific values into all deployments.

Otherwise it belongs in a pack, profile, adapter, or experiment.

## 5. Progressive formalization

Another user should not need to understand the full cognitive ontology before receiving value.

### Stage 0 — Preserve

Import or create a project with files and a simple project page.

### Stage 1 — Orient

Generate inventory, search, source references, and a re-entry capsule.

### Stage 2 — Declare key objects

Add decisions, questions, transitions, and commitments where useful.

### Stage 3 — Add temporal/provenance structure

Introduce current/historical resolution for real changing information.

### Stage 4 — Consolidate and propagate

Add source-grounded syntheses and impact analysis.

### Stage 5 — Prepare and act

Add proposals, policies, and narrowly authorized actions.

The system should remain useful at every stage. This avoids requiring complete ontology adoption before first value.

## 6. Configuration versus customization

### Configuration

Uses stable product concepts:

- choose authority source;
- set privacy class;
- select context template;
- set notification budget;
- enable a capability pack;
- define aliases;
- choose model adapter;
- set retention period.

### Customization

Adds domain-specific concepts or code:

- new memory item payload;
- specialized authority resolver;
- connector;
- lifecycle policy;
- evaluation family;
- domain view;
- typed executor.

Customization should occur through versioned extension points rather than editing core logic.

## 7. Proposed capability-pack contract

```yaml
pack:
  id: capability.project-continuity
  version: 0.1.0
  title: Project Continuity
  requires_kernel: ">=0.3,<0.4"

object_types:
  - project
  - milestone
  - transition
  - project_decision

commands:
  - RecordTransition
  - AcceptProjectDecision

queries:
  - BuildReentryPack
  - ExplainCurrentProjectState

views:
  - project_home
  - reentry
  - decision_history

policies:
  authority: project-authority-v1
  privacy: private-default
  retention: project-history-v1

integrations:
  optional:
    - git
    - github
    - calendar_reference

exports:
  - markdown
  - json

fitness_functions:
  - project_reentry_fixture
  - export_reimport_equivalence
  - stale_transition_detection
```

## 8. Extension architecture

### Stable extension points

- object payload schemas;
- query planners;
- authority policies;
- context compilers;
- views;
- connectors;
- executors;
- evaluation cases;
- import/export adapters;
- privacy and retention policies.

### Forbidden extension behavior

A pack should not:

- bypass kernel permission checks;
- create hidden canonical storage;
- depend on provider memory as sole state;
- override global privacy ceilings;
- mutate another pack’s authority without an explicit command;
- store secrets in normal configuration;
- make unreviewed profile inferences globally active;
- define an incompatible identity or time system.

## 9. Onboarding another user

The product should learn through guided examples rather than a giant settings form.

### Step 1 — Choose bounded outcome

“What is one project or workflow you repeatedly reconstruct?”

### Step 2 — Import minimal sources

Only the current project page, key decisions, active tasks, and recent context—not the entire digital life.

### Step 3 — Establish authority

For each information type, identify current source of truth and what Big Brain Time may do.

### Step 4 — Create baseline questions

Ten real questions the user wants answered.

### Step 5 — Create first transition

Use the project; stop; record a capsule; resume later.

### Step 6 — Review corrections and burden

Adjust vocabulary, context, and workflow.

### Step 7 — Add one capability at a time

No bulk import until value and maintenance are demonstrated.

## 10. Portability contract

A reusable product must allow a user to leave.

Every deployment should export:

- original source artifacts where licensing and privacy permit;
- Markdown narrative;
- normalized JSON objects and relations;
- authority and lifecycle rules;
- context and proposal manifests;
- evaluation cases and run summaries;
- schema versions;
- attachment manifest and hashes;
- human-readable explanation of the export;
- instructions for reconstruction without the original app.

Derived embeddings or model-specific caches need not export if they can be rebuilt.

## 11. Product ethics and social boundaries

### Personal systems

- no hidden psychological profiling;
- explicit data/model destinations;
- user-controlled deletion and retention;
- no silent consequential action;
- preserve authentic voice and historical self-perspective;
- do not turn absence of records into negative judgments.

### Shared systems

- speaker and audience grounding;
- consent for personal material;
- role and item-level access;
- right to challenge or annotate shared memory;
- transparent authority and conflict handling;
- clear ownership and deletion rules;
- no workplace surveillance disguised as productivity memory;
- no model-generated consensus presented as team agreement.

## 12. Business and distribution options

This package does not choose a business model, but architecture consequences should be visible.

### Open-source technical framework

**Fit:** current repository and technical audience.  
**Architecture:** local, extensible, file-friendly.  
**Risk:** support burden and fragmented configurations.

### Paid local desktop application

**Fit:** users wanting privacy and polished workflows.  
**Architecture:** installer, migrations, encrypted local storage, reliable backup, constrained extensions.  
**Risk:** cross-platform packaging and support.

### Hosted service

**Fit:** convenience and collaboration.  
**Architecture:** multi-tenant security, remote canonical storage, data governance, billing, uptime.  
**Risk:** conflicts with local-first trust thesis and greatly increases security obligations.

### Hybrid local core with optional sync/service

**Fit:** preserve local ownership while offering connectors, model routing, or encrypted sync.  
**Architecture:** clear local canonical state, provider-neutral contracts, optional services.  
**Risk:** complex product explanation and conflict semantics.

### Consulting/template methodology

**Fit:** organizations or projects adopting a design approach rather than software.  
**Architecture:** portable project-brain packages, templates, evaluation methods.  
**Risk:** less scalable but may reveal real user needs.

## 13. Generalization experiments

### G1 — Portable project brain

Export one project into a self-contained package. Ask another person/model to resume it using only the package. Record missing private assumptions and unnecessary Jonathan-specific structure.

### G2 — Second-user onboarding

Have another technically comfortable user create a bounded project brain. Observe terminology, capture, authority, and maintenance failures.

### G3 — Capability-pack extraction

Extract re-entry as a pack that uses only declared kernel contracts. Count imports from current app-specific modules; every hidden dependency is a kernel or design smell.

### G4 — No-Markdown interface

Mock onboarding and daily use for a user who never edits Markdown directly. Determine whether readable export can remain without direct-file interaction.

### G5 — Shared project boundary

Split one project into personal context, shared project memory, and external authority. Test accidental disclosure and perspective conflict.

### G6 — Provider replacement

Run the same context and evaluation pack through two model providers or a local model. Measure contract portability and behavior drift.

## 14. Suggested productization sequence

### Phase 1 — Jonathan’s design laboratory

- stabilize kernel concepts through real examples;
- measure re-entry, synthesis, and maintenance;
- preserve proof-of-concept baseline;
- create versioned pack contracts.

### Phase 2 — Portable project brain

- self-contained project package;
- clear authority and exports;
- re-entry and handoff;
- no global personal profile dependency.

### Phase 3 — Research or knowledge-assurance pack

- validate a second distinct capability against the same kernel;
- revise shared contracts based on real reuse.

### Phase 4 — Technical preview for another user

- onboarding, installation, error recovery, documentation, and portability;
- measure setup and maintenance, not only feature usefulness.

### Phase 5 — Choose product form

Use evidence to decide framework, desktop app, hybrid product, or continued personal research system.

### Phase 6 — Personal platform expansion

Only after the kernel has survived at least two capability packs and another user’s workflow.

## 15. Productization decision questions

1. Which current capability would another person seek independently?
2. What requires Jonathan’s tacit knowledge to operate?
3. Which concepts are impossible to explain without the current corpus?
4. What is the smallest installable and recoverable artifact?
5. Does the system create value before importing large amounts of data?
6. Can another user disagree with the ontology and still use the kernel?
7. What support burden does local-first shift to the product?
8. What data or behavior would make a hosted model unacceptable?
9. Which social assumptions change in a shared deployment?
10. Would the product still be worthwhile if it never became a business?
