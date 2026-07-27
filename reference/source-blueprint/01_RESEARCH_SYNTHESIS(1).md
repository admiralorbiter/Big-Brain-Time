# 00 — Executive Blueprint

**Research cutoff:** 2026-07-26

## 1. The north star

**[SOURCE]** The clearest opportunity identified by the repository audit is not to build another generic “second brain.” It is to let Jonathan **resume accurately without rereading the corpus and detect when the knowledge base disagrees with itself**. The audit reports 91 source Markdown files, roughly 109K tokens, stale active views, broken decision links, missing project status fields, reused typed IDs, a stale corrected experiment result, incomplete indexes, and no verified independent restore test. It concludes that the automation threshold has been crossed because propagation and epistemic integrity—not storage speed—are failing. [S2, lines 1–24]

**[PROPOSAL] Product mission:**

> Big Brain Time is a local-first, source-grounded, temporal personal capability platform that helps a human–AI partnership remember, resume, decide, act, learn, and improve without losing provenance, history, privacy, or human authority.

The product should behave less like a warehouse of notes and more like a **knowledge compiler**:

1. Parse canonical records and external references.
2. Validate their structure and epistemic consistency.
3. Build disposable search and relationship projections.
4. Compile task-specific “exhibits” or context packs.
5. Show conflicts, uncertainty, omissions, and time boundaries.
6. Produce proposed changes or actions.
7. Require review or policy authorization before mutation.
8. Measure whether the joint system actually improved.

## 2. What the system should make possible

By the end of the first year, the system should reliably answer or perform these capability tests:

1. **Resume a project:** “I have not touched Polaris for 45 days. What changed, why did it matter, where did I stop, and what is the first physical action?”
2. **Explain current truth:** “What is the current decision on SQLite, what did it supersede, and what conditions would reopen it?”
3. **Disclose conflict:** “Which active views, project pages, decisions, or records disagree about current status?”
4. **Answer as-of questions:** “What did the system believe on July 20, and when was that belief corrected?”
5. **Build context for another AI:** Produce a bounded, cited, project-scoped packet with authority rules, unresolved conflicts, omitted material, and token budget.
6. **Identify propagation work:** When a decision changes, show every dependent artifact and prepare a reviewable patch set.
7. **Plan the day without becoming a brittle task manager:** Combine active projects, task readiness, review triggers, recurrence, interruption state, and external calendar boundaries.
8. **Abstain correctly:** Say that available records cannot support an answer, name what evidence is missing, and avoid plausible invention.
9. **Recover:** Restore the canonical corpus and rebuild every derived artifact from a tested backup.
10. **Improve itself:** Run experiments on retrieval, re-entry, interruption handling, alerting, and coordination cost; promote only measured improvements.

## 3. Strategic architecture choice

The source documents contain a productive tension:

- **Earlier decision:** defer SQLite until roughly 100 files or a concrete query need appears. [S1, D-BBT-015]
- **Later audit:** the corpus is already at 91 files and has concrete propagation, integrity, link, identifier, and retrieval defects. [S2, lines 4–23]

**[PROPOSAL] Reconcile the tension by splitting the decision:**

- **Now:** permit SQLite only as a **disposable, deterministic, rebuildable read model**.
- **Later:** move one operational domain at a time into SQLite-canonical state only after export fidelity, restore, rollback, and user-value gates pass.

This is not a silent reversal of the Markdown-first philosophy. It is a narrower supersession that distinguishes **derived indexing** from **source-of-truth migration**.

## 4. Three candidate migration architectures

| Candidate | Canonical authority | Advantages | Failure modes | Recommended use |
|---|---|---|---|---|
| **A. Markdown canonical + SQLite projection** | Markdown/Git for all durable state; SQLite rebuilt from files | Maximum reversibility, readable history, low lock-in, easiest audit | Structured operations remain awkward; write workflows can become fragile; parser complexity | **Year 1 starting architecture** |
| **B. Split authority by information type** | Markdown for narrative knowledge; SQLite for projects/tasks/time/transitions; external systems for their own records | Matches data to its natural form; strong operations; preserves portable narrative | Authority ambiguity unless every entity type has an explicit owner; migration requires care | **Year 1–2 target** |
| **C. SQLite canonical + continuous exports** | SQLite/event history primary; Markdown/JSON/ICS generated | Strong constraints, queries, multi-interface behavior, transaction safety | Export drift, loss of hand-editability, migration lock-in, harder Git review | Consider only for mature operational domains; **not the corpus-wide target** |

The local-first literature emphasizes offline use, longevity, privacy, user control, and ownership. It also makes clear that multi-device concurrency is a distinct problem; CRDTs are a possible foundation, not a requirement for a single-user, mostly single-writer first version. [R01]

## 5. The seven horizons

The five horizons in the planning transcript are retained and expanded into implementation milestones:

1. **Trust Foundation:** backups, restore, canonical inventory, program charter, no data loss.
2. **Observatory:** inspect, validate, search, cite, detect drift, run epistemic CI, compile context packs.
3. **Workbench:** manage structured projects, tasks, transitions, time, decisions, and experiments through a common service layer.
4. **Cognitive Interface:** conversational retrieval, bounded synthesis, voice capture, re-entry guidance, proposed propagation patches.
5. **Adaptive Partner:** permission-scoped monitoring, proactive preparation, calibrated suggestions, shadow-mode learning.
6. **Personal Capability Platform:** specialized subsystems reuse identity, provenance, time, authority, permissions, evaluation, and interface infrastructure.
7. **Longitudinal Co-Adaptation Laboratory:** measure how Jonathan, AI, representations, methods, and training change one another over years.

## 6. Ten architectural laws

1. **One authority per information type.** Every class of state has one declared canonical system.
2. **Canonical writes are explicit; projections are disposable.** Deleting the read database must never lose knowledge.
3. **Deterministic before generative.** Parse, validate, filter, and disclose conflicts before asking a model to synthesize.
4. **Evidence is not instruction.** Retrieved documents, emails, webpages, and connectors are untrusted evidence inputs.
5. **Time is part of truth.** Current, historical, proposed, valid-from, recorded-at, and superseded states remain distinguishable.
6. **History is append-oriented.** Corrections supersede claims; they do not erase why the earlier state existed.
7. **Interfaces do not own business logic.** CLI, Flask, voice, API, and agents call the same domain services.
8. **Autonomy is earned by benchmark.** The system moves from retrieve → suggest → prepare → act only when measured safety and value justify it.
9. **Every irreversible choice needs an exit.** Export, rollback, rebuild, and recovery are acceptance criteria, not later operations work.
10. **Optimize the joint cognitive system.** Evaluate time-to-action, corrections, coordination burden, trust, and capability—not feature count.

## 7. Product bets that are ambitious and distinctive

### 7.1 Epistemic CI

A local test suite for knowledge: duplicate IDs, invalid metadata, stale views, broken links, impossible time ranges, unresolved supersession, orphaned decisions, contradictory current claims, and missing authority declarations fail with machine-readable diagnostics.

### 7.2 Temporal truth debugger

A user can ask “What was believed as of date T?”, inspect the evidence available then, see when a correction was recorded, and distinguish **valid time** from **recorded time**.

### 7.3 Propagation graph and patch compiler

When a project, decision, or claim changes, the system identifies dependent views, indexes, questions, context templates, and operational plans. It generates a patch bundle with rationale and impact, never a silent rewrite.

### 7.4 Re-entry capsules

Each active project receives a compact, cited capsule: outcome, current status, latest decisions, blockers, last meaningful work, stop point, restart cue, next micro-action, risks, and “what changed while away.”

### 7.5 Context contracts

Every context pack declares its purpose, as-of time, authority policy, included evidence, known conflicts, excluded sources, compression methods, token budget, and confidence limits. A pack is inspectable input, not an opaque prompt.

### 7.6 Memory buoyancy without destructive forgetting

Current relevance affects ranking and visibility, while preservation value governs retention. The system may suppress or archive low-buoyancy material but does not automatically delete durable records.

### 7.7 Action firewall

A model may propose an action graph, but a deterministic policy engine decides which tools, scopes, targets, and confirmation requirements are permitted. Consequential external actions remain human-controlled.

### 7.8 Capability laboratory

Every major feature ships with a short experiment: baseline, hypothesis, intervention, measures, confounders, result, decision, and stop rule. Big Brain Time must improve Big Brain Time through observed use, not aesthetic architecture.

## 8. Deliberate non-goals for year one

- No bulk import of all historical material.
- No corpus-wide SQLite-canonical migration.
- No microservice architecture.
- No vector database before lexical/metadata/link baselines are measured.
- No CRDT or custom sync protocol before real concurrent-edit conflicts justify it.
- No full RDF or complete W3C PROV implementation.
- No full event-sourcing framework.
- No silent model writes to canonical files or operational tables.
- No autonomous health, finance, legal, publishing, email, or scheduling actions.
- No dashboard whose definitions have not stabilized.
- No “AI memory” that cannot show its source, time boundary, and correction path.

## 9. Year-one outcome

A successful year-one system is not the one with the most screens. It is the one that can be deleted, restored, rebuilt, audited, queried, contradicted, corrected, and resumed—with lower cognitive burden than the current corpus.


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
