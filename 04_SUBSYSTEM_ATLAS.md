# 04 — Subsystem Atlas

## 1. How to use the atlas

The atlas describes Big Brain Time as a set of cooperating responsibilities rather than a list of current Python packages. Each subsystem card includes:

- purpose;
- primary jobs;
- inputs and outputs;
- authority and lifecycle;
- deterministic versus model-driven behavior;
- major friction and failure modes;
- key design questions;
- smallest useful probe;
- likely reusable product role.

The boundaries are proposals. A studio exercise may merge, split, or remove them.

![Subsystem landscape](diagrams/06_subsystem_landscape.svg)

---

## 2. Capture and Ingestion

### Purpose

Accept low-friction raw material while preserving its original form, source, time, privacy, and context. Convert only useful portions into reviewable structured candidates.

### Primary jobs

- capture text, voice, conversations, files, links, events, and external records;
- preserve a source artifact before transformation;
- classify privacy and processing urgency;
- detect exact duplicates and known source identities;
- extract candidate episodes, assertions, decisions, questions, tasks, and entities;
- propose canonical destinations or leave material in an inbox;
- avoid turning every capture into permanent structure.

![Capture pipeline](diagrams/07_capture_to_memory.svg)

### Inputs

Raw text, audio transcription, Markdown, documents, email, webpages, connector records, application events.

### Outputs

Source artifact, capture event, extraction candidates, staging packet, discard/archive recommendation.

### Authority

The preserved source is authoritative for what was captured. Extracted objects are derived until reviewed or structurally trusted.

### Deterministic work

Hashing, source identity, timestamping, privacy policy, file parsing, exact duplicate detection, allowed destination checks.

### Model work

Candidate extraction, topic suggestions, ambiguity detection, suggested questions, semantic duplicate proposals.

### Major frictions

- capture becomes a backlog rather than usable memory;
- smart routing creates surprising destinations;
- voice produces ambiguous or sensitive noise;
- extraction loses tone and context;
- repeated captures create false authority through frequency;
- classification questions interrupt the moment of capture.

### Design questions

1. What is the minimum metadata required at capture time?
2. When is preserving the original enough?
3. Should a capture be processed synchronously, later, or only when retrieved?
4. Which sources can create trusted structured records automatically?
5. How should one capture contain multiple object types?
6. What is the expiration policy for unprocessed inbox material?

### Smallest probe

Collect twenty real captures through the current flow. For each, record capture time, processing time, eventual use, incorrect routing, sensitive content, and whether structure added value. Compare immediate extraction with delayed processing.

### Reusable role

Universal kernel service, but interaction and extraction policies belong in profiles and capability packs.

---

## 3. Memory and Cognitive Object Model

### Purpose

Represent useful mental and informational objects without forcing all of them into one factual claim taxonomy.

### Primary jobs

- preserve episodes and narratives;
- represent truth-apt assertions where needed;
- represent preferences, values, goals, plans, decisions, questions, and simulations distinctly;
- associate stances and perspectives with holders and time periods;
- preserve authentic wording and structured addressability together;
- support lifecycle, relation, retrieval, and evaluation.

### Proposed core object

```yaml
memory_item:
  id: M-...
  kind: episode | assertion | narrative | preference | value |
        goal | plan | decision | question | simulation | procedure
  content: ...
  source_artifact: ...
  created_or_experienced_at: ...
  recorded_at: ...
  privacy: ...
  lifecycle: ...
```

Optional attached structures include stance, proposition, commitment, and relations.

### Authority

Object kind does not determine authority. A remembered episode can be authentically Jonathan’s memory without establishing every external detail as fact. A decision can be binding without being empirically true.

### Deterministic work

Schema validation, identity, lifecycle, required fields by kind, source linkage, permission checks.

### Model work

Suggested kind, stance, proposition, relations, ambiguity, narrative summary—always reviewable.

### Major frictions

- too little structure makes reasoning and retrieval weak;
- too much structure turns journaling into database administration;
- flat enums mix content type, source, confidence, and status;
- the model may psychologize or rigidly profile the user;
- structured extraction may appear more certain than source prose.

### Design questions

1. Which object kinds are universal?
2. Can object kind be inferred later rather than required at capture?
3. When does an assertion need proposition-level structure?
4. How should emotion and first-person experience be represented?
5. How do “Jonathan then” and “Jonathan now” coexist?
6. Which inferences about identity may never become durable without explicit acceptance?

### Smallest probe

Select ten real items: a fact, observation, interpretation, preference, value, decision, plan, memory, question, and imagined scenario. Model them using the current claim system and the plural object proposal. Compare ambiguity, retrieval, editing burden, and user comfort.

### Reusable role

Core kernel. This is the most consequential ontology decision and should remain deliberately small.

---

## 4. Provenance, Time, Perspective, and Resolution

### Purpose

Explain where information came from, when it applied, when it was known, who held it, and how the system’s position changed.

### Primary jobs

- track agents, source artifacts, and transformation activities;
- distinguish valid time, recorded time, observed time, generated time, and review time;
- represent source mode: perceived, measured, remembered, reported, inferred, generated, imagined;
- preserve perspective holders and stances;
- link corrections, supersession, support, attack, qualification, derivation, and dependency;
- answer current and as-of questions;
- expose unresolved conflict and authority policy.

### Inputs

Memory items, source artifacts, external records, accepted relations, correction events, authority rules.

### Outputs

Applicable-state result, alternatives, conflict set, evidence explanation, as-of history, observability gaps.

### Authority

The resolver does not create truth. It applies declared scope, time, source, and decision policies and reports the result.

### Deterministic work

Interval logic, explicit relation traversal, authority-rule application, retraction filtering, cycle detection, output state selection where policy is complete.

### Model work

Candidate proposition normalization, relation suggestions, scope questions, evidence relevance proposals.

### Major frictions

- timestamps are missing or ambiguous in ordinary notes;
- “latest” is not always most authoritative;
- different perspectives may be legitimate rather than contradictory;
- a remembered event can change during reconsolidation;
- detailed provenance can become visually overwhelming;
- silently swallowed parse failures create false confidence.

### Design questions

1. What is the minimum temporal model for ordinary users?
2. Which relations are canonical versus derived?
3. How is uncertain or approximate time represented?
4. Can source and perspective be shown progressively rather than always inline?
5. What authority policies are values or commitments rather than objective rules?
6. How are conflicts between policy and source handled?

### Smallest probe

Create five temporal cases from actual Big Brain Time history: correction, changing plan, historical preference, external authority update, and two legitimate perspectives. Manually produce current, as-known-then, and perspective-specific answers.

### Reusable role

Core kernel, with domain-specific authority policies supplied by profiles and capability packs.

---

## 5. Retrieval and Search

### Purpose

Find the evidence, objects, and relationships needed for a particular question—not merely similar text.

### Primary jobs

- exact ID, path, title, and alias lookup;
- lexical search with metadata and source filters;
- temporal, authority, privacy, and lifecycle filtering;
- bounded link and relationship expansion;
- optional semantic retrieval and reranking;
- local versus global query routing;
- explanation of why results were selected or rejected;
- negative retrieval and abstention support.

### Inputs

Query plan, read model, indexes, authority rules, source artifacts, lifecycle and privacy state.

### Outputs

Ranked evidence candidates, retrieval explanations, coverage gaps, conflict candidates, manifest.

### Authority

Retrieval returns candidates. It never decides that a claim is true, contradictory, superseding, or safe to act upon.

### Deterministic work

Exact lookup, FTS, filters, budgets, stable result contracts, graph caps, manifest generation.

### Model work

Query decomposition, paraphrase expansion, semantic reranking, global map/reduce synthesis—benchmarked and optional.

### Major frictions

- similarity retrieves related but non-answering text;
- current and historical evidence are mixed;
- semantic retrieval collapses negation or scope;
- graph expansion produces noise;
- hidden suppression removes important old evidence;
- a full-context answer looks confident even when evidence is missed.

### Design questions

1. What query families matter in real use?
2. Which hard failures remain after exact + FTS + metadata + links?
3. How should retrieval explain itself without overwhelming the user?
4. What is the right global-sensemaking baseline?
5. When should a query retrieve a narrative container as well as an atomic record?
6. What counts as enough evidence to stop searching?

### Smallest probe

Build a living set of thirty real questions. Compare exact/FTS, FTS+metadata, FTS+links, and hybrid retrieval. Record evidence recall, noise, latency, privacy, and correction burden.

### Reusable role

Core service with pluggable retrieval strategies and domain-specific query planners.

---

## 6. Context Compiler

### Purpose

Compile an inspectable, purpose-specific evidence package for a human, model, workflow, or handoff.

### Primary jobs

- declare purpose, audience, query, time, authority, privacy, and token budget;
- select and order evidence;
- include conflicts, unknowns, and omissions;
- preserve lineage and content hashes;
- externalize overflow to referenced appendices;
- invalidate after material source changes;
- render provider-neutral Markdown and machine-readable manifest.

### Inputs

Retrieval results, project/area configuration, privacy policy, time/authority resolution, context template.

### Outputs

Context manifest, human-readable body, evidence index, exclusions, staleness status.

### Authority

A context pack is a compiled view, never the sole authority for factual content.

### Deterministic work

Contract validation, source selection policy, token accounting, deduplication, manifests, expiration, rendering order.

### Model work

Compression, ordering suggestions, connective prose, task-specific explanation—only where loss is declared and lineage retained.

### Major frictions

- a fixed project priority list ignores the actual question;
- whole documents consume budget and hide relevant spans;
- omission reports are technically present but not useful;
- stale packs are reused because they look complete;
- generated summaries cite themselves rather than primary evidence;
- handoff packets can contain hardcoded status claims.

### Design questions

1. What purposes deserve distinct context contracts?
2. How are protected information units defined per purpose?
3. What should be extractive versus abstractive?
4. How does a recipient verify the pack quickly?
5. Which pack sections are universal versus capability-specific?
6. How should a pack represent a disagreement that cannot fit within budget?

### Smallest probe

Take one real project and build three packs: re-entry, architecture review, and external-model handoff. Use the same source corpus and compare what each must preserve and omit.

### Reusable role

Core kernel contract plus capability-specific compilers.

---

## 7. Synthesis and Consolidation

### Purpose

Create smaller or more general representations that improve future reasoning while preserving source lineage, exceptions, alternatives, and known loss.

### Primary jobs

- exact deduplication and normalization;
- cluster episodes and assertions by declared purpose;
- preserve conflicts and minority perspectives;
- produce extractive digests, abstractive summaries, thematic reflections, and proposed heuristics as distinct artifact types;
- test retained information and question-answer capability;
- invalidate or revise derived syntheses when sources change;
- promote only reviewed generalizations.

![Memory consolidation](diagrams/09_memory_consolidation.svg)

### Inputs

Source artifacts, memory items, relations, retrieval logs, task or question family, protected-content contract.

### Outputs

Derived synthesis artifact, lineage DAG, omission report, retention score, new hypothesis candidates, stale conditions.

### Authority

Syntheses are derived by default. A new interpretation or generalization is a proposal, not verified evidence.

### Deterministic work

Exact duplicates, manifests, source hashing, invalidation, protected-value tests, idempotent writes.

### Model work

Semantic clustering, abstraction, themes, candidate generalizations, counterexamples, compression.

### Major frictions

- compression creates false coherence;
- summaries grow into a second canonical corpus;
- repeated synthesis duplicates content;
- patterns become identity claims;
- one purpose’s summary is reused for another;
- exceptions disappear because they are rare;
- source changes do not invalidate parents.

### Design questions

1. Which synthesis artifact types are needed?
2. What makes a topic “ready” for consolidation?
3. What information is protected for each purpose?
4. How are minority views represented compactly?
5. Should consolidation occur on a schedule, at retrieval, or by explicit request?
6. When may a derived reflection become a canonical decision or heuristic?

### Smallest probe

Select one topic with ten to twenty heterogeneous sources. Produce an extractive digest, abstractive summary, and reflection. Test each against five future questions and a list of protected facts, disagreements, and exceptions.

### Reusable role

Core contracts and evaluation; algorithms and prompts remain replaceable adapters.

---

## 8. Attention, Active Frame, and Collaboration Coordination

### Purpose

Maintain orientation for the current cognitive episode and allocate scarce human and machine attention without turning every stored item into an interruption.

### Primary jobs

- establish current purpose, scope, and desired outcome;
- protect commitments and surface endangered obligations;
- track open questions, active assumptions, and salient contradictions;
- allocate attention using consequence, uncertainty, reversibility, novelty, value sensitivity, and interruption cost;
- compile the smallest relevant context from shared artifacts;
- record participants, roles, information seen, permissions, and known limitations;
- detect and repair common-ground mismatch;
- expire or revalidate the frame after material change;
- narrow permitted behavior when system health is degraded.

### Inputs

Values, goals, commitments, project state, epistemic ledger, source changes, context manifests, collaborator registry, health state, calendar references, interruption policy.

### Outputs

Inspectable active frame, ranked surfacing candidates, deferral record, context request, common-ground repair prompt, escalation, abstention, degraded-mode notice.

### Authority

Jonathan controls goals, protected commitments, attention preferences, and interruption thresholds. Deterministic policies enforce declared hard constraints. Models may propose salience and explain tradeoffs but may not silently reprioritize goals or cancel commitments.

### Deterministic work

Expiry, deadline calculation, policy thresholds, source-set comparison, permission filtering, frame versioning, deferral persistence, health gates, and audit.

### Model work

Propose relevance, identify possible contradiction or novelty, estimate missing context, draft common-ground summaries, and suggest attention tradeoffs.

### Major frictions

- the active frame becomes another status document to maintain;
- urgency proxies crowd out important but quiet goals;
- model confidence is mistaken for human-review value;
- alerts create attention residue and blind dismissal;
- collaborators inherit the same bad premise and appear independently confident;
- “helpful” reprioritization silently changes the user’s goal;
- stale frames keep controlling work after the environment changes;
- system overload or missing context is hidden instead of changing behavior.

### Design questions

1. What is the minimum active-frame schema that materially improves behavior?
2. Which factors justify interruption rather than review-queue placement?
3. How are quiet long-term commitments protected from urgent noise?
4. What evidence shows that collaborators no longer share the same objective or source set?
5. When should collaborators receive independent context to reduce correlated error?
6. Which frame changes require Jonathan’s acceptance?
7. What is the carrying cost of each alert, frame field, and registry record?
8. Which degraded states permit reading, synthesis, proposal, canonical mutation, or action?

### Smallest probe

For two weeks, maintain one compact active frame for a real project. Run every surfacing candidate through consequence, uncertainty, reversibility, novelty, commitment risk, deferral cost, and interruption cost. Compare it with recency- or confidence-based routing on useful-suggestion rate, missed commitments, correction burden, and unwanted interruptions.

### Reusable role

Universal control-loop capability built on purpose, commitment, epistemic, collaboration, policy, and health contracts.

---

## 9. Projects, Commitments, and Planning

### Purpose

Represent what the user or system has committed to doing, why, under what constraints, and with what current state—without turning Big Brain Time into a brittle universal task manager.

### Primary jobs

- preserve the chain from values to goals to commitments to plans and tasks;
- project outcomes and definitions of done;
- goals, decisions, plans, tasks, dependencies, and blockers;
- promises and obligations: to whom, why, by when, and under what authority;
- explicit cancellation and supersession conditions;
- endangered-commitment detection;
- status and readiness;
- temporal constraints and review triggers;
- recurrence references and calendar boundaries;
- rationale and reconsideration conditions;
- portfolio views and prioritization explanations.

### Inputs

Accepted decisions, user commitments, external dates, project narratives, transitions, review policies.

### Outputs

Current operational state, next-action candidates, dependency graph, planning views, exports, external drafts.

### Authority

Selected operational fields may become SQLite-canonical after a bounded migration. Narrative rationale and external events may remain elsewhere.

### Deterministic work

State transitions, constraints, dependencies, recurrence calculations, export, audit.

### Model work

Task decomposition, prioritization alternatives, blocker interpretation, plan proposals, negotiation prompts.

### Major frictions

- duplicate task systems;
- excessive status maintenance;
- model-generated tasks that create work rather than progress;
- plans treated as facts;
- priorities inferred from incomplete values;
- plans silently redefine their parent goals;
- new opportunities displace existing obligations without a supersession decision;
- external dates copied locally and become stale.

### Design questions

1. Which operational aggregate provides enough value to justify migration?
2. What is the difference between goal, project, commitment, plan, task, and reminder?
3. Which professional tasks should remain external references?
4. How should the system challenge priorities without taking control?
5. What planning state is essential for re-entry?
6. How are abandoned or intentionally paused commitments represented?
7. Which commitments are promises to other people and therefore require social, not merely technical, reconciliation?
8. How does an attention policy protect important quiet commitments from urgent low-value activity?

### Smallest probe

Choose one project for two real review cycles. Compare the current Markdown workflow with a minimal structured aggregate containing only outcome, status, milestone, next action, blockers, and transition.

### Reusable role

Capability pack built on kernel commitments, time, identity, and policy.

---

## 10. Re-entry and Continuity

### Purpose

Make interrupted or dormant work resumable with minimal cognitive startup cost.

### Primary jobs

- record stop point, restart cue, next micro-action, and resumption trigger;
- detect stale or missing transitions;
- gather changes since last meaningful access;
- compile current decisions, blockers, dependencies, and conflicts;
- distinguish project state from conversation history;
- measure resumption performance.

![Re-entry loop](diagrams/10_reentry_loop.svg)

### Inputs

Project state, transition records, recent changes, decisions, tasks, external events, journal/retro references.

### Outputs

Re-entry capsule, stale-transition warning, first-action proposal, resumption measurement.

### Authority

The recorded transition is authoritative for where the user intended to stop. The compiled capsule is derived and may need correction if the world changed.

### Deterministic work

Required-field validation, material-change detection, change window, source selection, expiration.

### Model work

Concise phrasing, comparison of changes, open-loop summary, candidate next action when none exists.

### Major frictions

- closeout ceremony costs more than resumption benefit;
- a capsule records activity but not the unresolved mental model;
- restart cue points to stale lines or missing files;
- a micro-action is easy but not strategically correct;
- automated briefings become repetitive.

### Design questions

1. Which fields actually predict successful resumption?
2. What counts as a material project change?
3. Should the system generate a capsule continuously or only at transition?
4. How does re-entry work for conceptual research rather than executable tasks?
5. What is the right balance between narrative and structured fields?
6. How is elapsed-time change distinguished from forgotten context?

### Smallest probe

Alternate manual and system-assisted transition records across six interruptions. Measure closeout time, resumption time, rereads, wrong first actions, and subjective burden.

### Reusable role

Strong candidate for the first reusable project-brain capability.

---

## 11. Propagation and Change Control

### Purpose

Identify what a material change affects and prepare safe, understandable updates without silently rewriting history.

### Primary jobs

- represent explicit and inferred dependencies;
- detect semantic differences, not merely textual diffs;
- find stale views, summaries, plans, questions, and actions;
- prioritize impacts by severity and confidence;
- prepare granular proposals with preconditions;
- accept, edit, reject, or mark false dependencies;
- invalidate and rebuild derived artifacts;
- preserve audit and rollback evidence.

### Inputs

Accepted change, dependency graph, source links, displays, summaries, indexes, policy and authority rules.

### Outputs

Impact report, proposal bundle, unresolved questions, invalidation events, audit evidence.

### Authority

Explicit human-authored dependencies may be canonical. Inferred edges remain derived until accepted.

### Deterministic work

Exact links, typed references, manifest dependencies, precondition hashes, affected-store invalidation.

### Model work

Semantic dependency suggestions, impact explanations, proposed wording, missing-link detection.

### Major frictions

- graph false positives create review fatigue;
- hidden dependencies remain undetected;
- a wording edit is mistaken for a semantic change;
- derived summaries are updated but source decisions are not;
- broad patch acceptance hides granular meaning changes.

### Design questions

1. Which dependency types are worth maintaining?
2. How is propagation recall evaluated when the full dependency set is unknown?
3. What changes can be auto-invalidated versus human-updated?
4. Can the system distinguish “displayed in” from “semantically depends on”?
5. How are external dependencies represented?
6. What is the maximum reasonable proposal size?

### Smallest probe

Create ten seeded material changes across real documents and manually define expected impacts. Compare explicit links, textual references, typed IDs, and model suggestions.

### Reusable role

Core change-control service with domain-specific dependency rules.

---

## 12. Memory Lifecycle, Forgetting, and Deletion

### Purpose

Control visibility, relevance, retention, correction, redaction, and destruction without confusing them.

### Primary jobs

- suppress low-relevance items reversibly;
- archive inactive material;
- supersede or retract endorsed assertions;
- redact protected payload while retaining lawful structure;
- purge selected meaning across controlled representations;
- expire ephemeral staging and context packs;
- apply preservation classes and legal/ethical holds;
- disclose residual backup retention.

### Inputs

Lifecycle request, item identity, retention policy, dependency graph, backups, authority and privacy rules.

### Outputs

Impact plan, approval requirement, updated lifecycle state, projection rebuild, deletion receipt, residual-copy report.

### Authority

Only an authorized lifecycle operation changes or destroys canonical material. Low retrieval rank is never deletion authority.

### Deterministic work

Policy classification, representation enumeration, deletion transactions, projection invalidation, receipt and verification.

### Model work

Candidate archive/suppression suggestions, preservation-value questions, semantic replica discovery—never autonomous purge.

### Major frictions

- append-only rules conflict with privacy and user control;
- Git and backups retain historical copies;
- summaries and model prompts contain derived fragments;
- suppression hides vital old context;
- deletion receipts accidentally preserve sensitive payload;
- users expect universal erasure that cannot be guaranteed.

### Design questions

1. Which retention classes apply to each domain?
2. What must be deleted versus merely hidden or retracted?
3. How should Git history and backup expiration be handled?
4. Can per-domain encryption make cryptographic erase practical?
5. What derived outputs must be searched during purge?
6. What proof of deletion is honest and useful?

### Smallest probe

Choose three synthetic items: ordinary obsolete note, retracted belief, and highly sensitive accidental capture. Walk each through suppress, archive, retract, redact, and purge impact plans.

### Reusable role

Core kernel and governance service. Essential before broad personal or multi-user deployment.

---

## 13. Permissions and Action Firewall

### Purpose

Allow increasingly useful initiative without allowing evidence, model confidence, or broad credentials to become authority.

### Primary jobs

- define domain/action/target/time/privacy grants;
- classify risk and reversibility;
- validate typed action graphs;
- record predicted changes, failure conditions, and verification evidence before execution;
- require previews and confirmations;
- authorize observation separately from mutation;
- enforce preconditions, scope, and maximum affected items;
- execute through narrow adapters;
- observe and verify external postconditions independently;
- reconcile expected and actual outcomes;
- provide kill switch, safe mode, rollback, and trust repair.

### Inputs

User request, proposal, grants, resource state, privacy class, tool schema, evidence manifest.

### Outputs

Allow/deny decision, required confirmation, prediction record, executed result, external observation, reconciliation status, verification, incident, audit, and rollback status.

### Authority

Only the control plane creates grants. Retrieved content and model output cannot modify policy.

### Deterministic work

All authorization, target validation, risk ceiling, confirmation mode, path and recipient checks, action execution boundary, postcondition matching, and closure gate.

### Model work

Propose and explain actions; never decide its own permission.

### Major frictions

- confirmation fatigue leads to blind approval;
- grants are too broad or hard to understand;
- monitoring feels more invasive than one-time action;
- model output smuggles unapproved arguments;
- rollback exists technically but cannot undo external consequences.
- an API success is reported as outcome success without external verification;
- read access admits stale or manipulated tool output into the control path;
- verification repeats the same faulty observation path and is not independent;
- degraded system health fails to narrow action permissions.

### Design questions

1. Can Jonathan predict policy outcomes?
2. What permission concepts are understandable in daily use?
3. Which low-risk actions actually save enough effort?
4. How are model/data destinations part of permission?
5. What changes require per-action confirmation forever?
6. How should “negotiate” initiative be bounded for goals and identity?
7. What independent observation is sufficient to verify each action class?
8. When must a prediction mismatch trigger rollback, incident capture, or human reconciliation?
9. Which system-health states force safe mode or prohibit action?

### Smallest probe

Create twenty action scenarios and ask Jonathan to predict allow, deny, or confirm. For each allowed scenario, record the expected external change and verification evidence; simulate technical success with a wrong real-world result. Redesign policy and closure language until expected and actual outcomes align.

### Reusable role

Universal governance kernel, with domain-specific grants and executors.

---

## 14. Evaluation, Experiments, Audit, and Observability

### Purpose

Determine whether the system is correct, useful, safe, understandable, and worth maintaining; preserve enough evidence to repair failures and improve design.

### Primary jobs

- maintain regression cases and seeded defects;
- capture baselines and live workflow measures;
- record model, prompt, context, policy, and software versions;
- distinguish prototype, tested, benchmarked, piloted, trusted, and authorized;
- track human corrections, burden, trust, and task outcomes;
- compare predicted and actual effects for actions, collaborators, and methods;
- monitor dependency, context, model, policy, and human-review health;
- convert incidents into tests;
- preserve causal audit without sensitive payload excess;
- support keep/simplify/remove decisions.

### Inputs

Test fixtures, run manifests, active-frame history, prediction and outcome records, health transitions, user feedback, action events, incidents, metrics, retrospectives.

### Outputs

Scorecards, benchmark reports, maturity evidence, incident records, design decisions, deprecation recommendations.

### Authority

Evaluation evidence supports decisions but does not replace human value judgments. Metrics must remain interpretable and revisable.

### Deterministic work

Fixture execution, integrity checks, metrics, version binding, hash verification, audit-chain validation.

### Model work

Rubric assistance, failure clustering, qualitative synthesis, candidate regression cases—reviewed and calibrated.

### Major frictions

- seeded benchmarks are overfit;
- model judges agree with model errors;
- instrumentation creates privacy or maintenance burden;
- test count becomes a proxy for product maturity;
- audit logs are technically complete but unusable;
- success metrics optimize behavior users do not value.
- human attention is treated as free evaluation capacity;
- correlated model reviewers repeat the same premise and simulate independent assurance;
- health degradation is visible in logs but does not alter permitted behavior.

### Design questions

1. What baseline is cheap enough to sustain?
2. Which incidents should become regression cases?
3. How is joint-system benefit measured without constant self-tracking?
4. Which maturity claims expire after code/model/data changes?
5. What audit detail is needed for trust repair?
6. What is the removal threshold for a feature?
7. How is attention cost included in joint-system benefit?
8. How is evaluator independence established at the premise and source-set level?
9. Which prediction mismatches should recalibrate a collaborator or method?

### Smallest probe

For one capability, create a complete evidence packet: baseline, deterministic tests, benchmark, two-week pilot, corrections, burden, and a keep/revise/remove decision.

### Reusable role

Universal kernel and design-process infrastructure.

---

## 15. Integrations, Interfaces, and Runtime

### Purpose

Connect the kernel to storage, external systems, models, and user interaction without letting an adapter become the architecture.

### Primary jobs

- Markdown/Git persistence and export;
- SQLite operational and read models;
- search and embedding adapters;
- model routing and privacy policy;
- calendar, GitHub, email, drive, and file connectors;
- CLI, web, voice, and API delivery;
- configuration, secrets, local runtime, and health checks;
- provider replacement and compatibility tests.

### Authority

Adapters inherit authority from the information type and policy. A connector does not become authoritative merely because it can write.

### Deterministic work

Serialization, validation, migrations, retries, idempotency, authentication boundaries, connector scopes.

### Model work

Provider-specific inference only; no canonical state hidden in provider memory.

### Major frictions

- Flask routes accumulate domain logic;
- model provider features create lock-in;
- local-first becomes “local server requiring constant care”;
- connectors import more data than needed;
- multi-device convenience undermines single-writer assumptions;
- voice creates a parallel state machine.

### Design questions

1. Which interface is needed to evaluate each workflow?
2. What contracts must remain provider-neutral?
3. When is remote access worth its security boundary?
4. Which connector data should be indexed versus referenced on demand?
5. How does the app remain useful when a provider or network is down?
6. What is the supportable deployment story for another user?

### Smallest probe

Implement one use case through application services, CLI, and a thin web page. Confirm equivalent behavior and no domain logic in interface code.

### Reusable role

Adapters and product surfaces around the kernel; deliberately replaceable.

---

## 16. Cross-subsystem friction map

| Interaction | Typical failure |
|---|---|
| Capture → memory model | extraction turns ambiguity into certainty |
| Memory model → provenance | object kind and source mode are conflated |
| Provenance → retrieval | authority/time policy is applied after ranking instead of before |
| Retrieval → context | token budget hides necessary conflict or scope |
| Context → synthesis | summary becomes authority or loses exceptions |
| Commitments → active frame | urgency displaces a quiet obligation without explicit supersession |
| Artifacts → active frame | retrieval availability is confused with present salience |
| Active frame → collaborator | role, source set, or objective mismatch creates false agreement |
| Synthesis → planning | interpretation creates tasks without an accepted decision |
| Planning → re-entry | current status exists but restart cognition is missing |
| Change → propagation | dependency graph is noisy or incomplete |
| Propagation → action | proposal scope exceeds what the user understood |
| Execution → verification | tool success is mistaken for intended real-world outcome |
| Health → governance | degraded capability is reported but does not narrow permission |
| Incidents → methods | failure evidence accumulates without policy revision |
| Lifecycle → audit | deletion process retains the sensitive payload in logs |
| Evaluation → design | metrics reward feature behavior rather than capability value |
| Integrations → privacy | convenient connector imports exceed minimum necessary evidence |

These seams should receive more design attention than isolated module internals.

## 17. Atlas exercise

For each subsystem, mark:

- `must exist in kernel`;
- `capability pack`;
- `adapter`;
- `derived experiment`;
- `external authority`;
- `not yet justified`.

Then identify the **three seams** whose failure would most damage trust. Those seams should define the first architecture probes after the design phase.
