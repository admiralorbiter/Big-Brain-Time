# 11 — Experiment Portfolio and Decision Gates

## 1. Portfolio purpose

The experiment portfolio translates the design studio into learnable action. It is not a promise to run every experiment. It provides a menu of small probes ordered by the decisions they can change.

The central rule is:

> Run the cheapest experiment that can invalidate an important assumption before investing in the architecture that assumes it is true.

## 2. Experiment principles

1. Begin with a baseline.
2. Name the decision the experiment can change.
3. Keep the intervention small and reversible.
4. Test the failure mode, not only the happy path.
5. Include maintenance and human correction costs.
6. Preserve raw results and confounders.
7. Predeclare a keep/revise/remove or adopt/defer rule.
8. Do not change multiple major variables at once.
9. Prefer real work when safety permits.
10. Limit concurrent experiments so the system remains usable.

## 3. Maturity gates

![Evaluation flywheel](diagrams/16_evaluation_flywheel.svg)

### Gate 0 — Concept

- problem and user capability are stated;
- current evidence and assumptions are visible;
- at least two options exist.

### Gate 1 — Prototype

- inspectable probe exists;
- scope and limitations are explicit;
- no product reliability claim.

### Gate 2 — Tested

- deterministic behavior passes unit/integration/fixture checks;
- recovery and failure behavior are included;
- semantic contract is not merely implied by test count.

### Gate 3 — Benchmarked

- declared evaluation cases and thresholds pass;
- simpler baseline is included;
- model/config/version is recorded;
- hard and negative cases are present.

### Gate 4 — Piloted

- used in real work over a meaningful period;
- corrections, maintenance, and subjective burden are recorded;
- the capability survives more than one ideal scenario.

### Gate 5 — Trusted

- sustained evidence supports reliance in a specific domain and consequence level;
- recovery and trust repair have been demonstrated;
- behavior remains understandable after change.

### Gate 6 — Authorized

- deterministic policy permits an effect in a declared scope;
- user comprehension and rollback are adequate;
- adversarial boundary tests pass.

## 4. Portfolio ordering

### Portfolio A — Semantic integrity first

These experiments address assumptions that affect almost every future subsystem.

### Portfolio B — Product value

These determine whether the strongest wedge actually improves real work.

### Portfolio C — Architecture alternatives

These compare representation and deployment choices.

### Portfolio D — Longer-horizon capability

These explore consolidation, personalization, proactivity, and productization after the kernel is clearer.

No more than three experiments should be active, and only one should materially alter the working prototype at a time.

---

## 5. Experiment E01 — Plural cognitive object model

### Question

Does separating object kind, source mode, stance, perspective, proposition, and resolution improve representation without unacceptable complexity?

### Decision affected

Whether to replace or supplement the current flat epistemic enums.

### Design

Select ten to twenty real examples covering fact, observation, interpretation, memory, preference, goal, plan, decision, question, procedure, and simulation. Represent each using:

- current marker/claim system;
- free-form source-only representation;
- proposed plural model.

### Measures

- ambiguous or forced classifications;
- number of fields required;
- time to capture/review;
- ability to answer factual, perspective, and decision questions;
- user comfort;
- migration complexity.

### Decision rule

Adopt a smaller version of the plural model if it resolves material ambiguities and improves query behavior without making ordinary capture feel like form completion. Otherwise retain source-first storage and add structure at retrieval.

---

## 6. Experiment E02 — Stable identity and temporal rebuild

### Question

Can the read model be rebuilt without changing semantic identities, recorded times, or applicable intervals?

### Decision affected

Whether the current derived projection is safe as a foundation for temporal truth.

### Design

Build the same corpus twice; insert a new earlier claim; rename a file; change importer build time; reimport. Compare semantic records.

### Measures

- stable IDs;
- unchanged recorded/valid times;
- alias behavior;
- logical fingerprint;
- visible diagnostics for collisions;
- round-trip preservation.

### Gate

Zero unexpected semantic differences before temporal answers rely on the projection.

---

## 7. Experiment E03 — Reconciliation invariants

### Question

Does pair adjudication behave correctly under time, scope, authority, argument order, and serialization?

### Decision affected

Whether reconciliation can automatically create relations or only review cards.

### Design

Property and fixture tests for:

- order inversion;
- interval overlap versus different start dates;
- same wording, different scope;
- different wording, equivalent proposition;
- perspective disagreement;
- decision versus observation;
- explicit authorized correction;
- full write/read round trip.

### Gate

Zero false automatic supersessions; all uncertain cases route to review; every semantic field round-trips.

---

## 8. Experiment E04 — Purpose-bound synthesis

### Question

Does a synthesis contract preserve the information needed for a declared task better than a generic summary?

### Decision affected

The synthesis artifact model and evaluation requirements.

### Design

Use one source set to create:

- generic summary;
- re-entry synthesis;
- architecture-decision synthesis;
- research synthesis.

Predefine protected units and five future questions per purpose.

### Measures

- protected-unit recall;
- conflict/exception retention;
- citation correctness;
- future-question performance;
- token reduction;
- human usefulness;
- stale-child detection.

### Decision rule

No generic canonical summary. Adopt purpose contracts if they materially improve retained capability and make omissions understandable.

---

## 9. Experiment E05 — Stored versus on-demand consolidation

### Question

Which syntheses should be stored, and which should be generated when needed?

### Decision affected

Memory hierarchy, invalidation, and maintenance architecture.

### Design

Track one active topic and one infrequent topic for four weeks under:

- stored summary with invalidation;
- on-demand synthesis;
- stored structured units with on-demand prose.

### Measures

- stale artifacts;
- generation latency/cost;
- repeated corrections;
- reuse frequency;
- user editing value;
- provider dependence.

### Decision rule

Store only artifacts whose reuse or accepted human meaning justifies maintenance; otherwise retain structured units and generate views.

---

## 10. Experiment E06 — Ready-to-Resume field ablation

### Question

Which transition fields actually improve resumption?

### Decision affected

The transition aggregate and closeout workflow.

### Design

Across multiple interruptions, compare:

- no transition;
- stop point only;
- four-field current protocol;
- expanded capsule with open loops and mental model;
- system-generated draft reviewed by Jonathan.

### Measures

- closeout time;
- time to first productive action;
- rereads;
- wrong starts;
- correction burden;
- subjective relief or ceremony.

### Decision rule

Keep only fields that contribute to faster or more confident resumption. A shorter field set is a success if it performs as well.

---

## 11. Experiment E07 — Project context versus full history

### Question

Do purpose-bound project packs outperform whole-handbook or broad-history prompting?

### Decision affected

Default context architecture.

### Design

Ten real project questions under:

- full handbook/history;
- current project file only;
- deterministic project context pack;
- interactive evidence requests.

### Measures

- evidence recall;
- factual and temporal correctness;
- conflict disclosure;
- token use;
- startup time;
- follow-up questions;
- privacy exposure.

### Decision rule

Use the smallest method that meets correctness and conflict requirements. Retain full context as an audit baseline, not default.

---

## 12. Experiment E08 — Real-query retrieval ladder

### Question

Which retrieval mechanisms add net value after a tuned lexical/metadata/link baseline?

### Decision affected

Embeddings, reranking, and graph investment.

### Design

Maintain at least thirty real questions across exact, current, historical, conflict, low-overlap, multi-hop, global, and negative cases. Compare:

1. exact + FTS;
2. metadata/time/authority;
3. link expansion;
4. embeddings;
5. fusion/reranker;
6. hierarchy/global map-reduce.

### Measures

Recall, precision, latency, explanation, privacy, rebuild cost, maintenance, and false semantic matches.

### Stop rule

Remove or defer any complex method whose gain is small, unstable, or limited to synthetic cases.

---

## 13. Experiment E09 — Narrative plus projection versus atomization

### Question

Does preserving narrative originals with selective projections outperform document-only and atom-only representations?

### Decision affected

Core storage and object extraction strategy.

### Design

Use three complex artifacts: design conversation, personal reflection, and research note. Create document-only, atom-only, and combined representations.

### Measures

- future question coverage;
- authentic meaning;
- edit effort;
- propagation;
- deletion impact;
- user preference;
- schema maintenance.

### Decision rule

Adopt combined representation only for object types whose structured reuse is demonstrated.

---

## 14. Experiment E10 — Lifecycle comprehension and purge impact

### Question

Can users distinguish suppress, archive, supersede, retract, redact, delete, and purge, and does the system enumerate consequences accurately?

### Decision affected

Lifecycle vocabulary, UI, retention, and backup architecture.

### Design

Create synthetic cases and ask Jonathan to choose desired outcomes. Generate dry-run reports across Markdown, Git, DB, indexes, summaries, snapshots, audit, and backups.

### Measures

- user-policy agreement;
- missed representations;
- residual disclosure comprehension;
- accidental over-deletion or under-deletion;
- report burden.

### Gate

No destructive implementation until the semantic verbs and dry-run scope are predictable.

---

## 15. Experiment E11 — Personal inference review

### Question

Which inferred preferences or patterns are useful, acceptable to store, and safe to apply?

### Decision affected

Self-model and personalization policy.

### Design

Generate ten evidence-backed candidate inferences from real use. For each, show examples, uncertainty, intended uses, expiration, and correction controls.

### Measures

- recognition and acceptance;
- discomfort;
- desired retention;
- permitted uses;
- changes after one month;
- recommendation improvement.

### Stop rule

No durable inference class with low acceptance, high discomfort, or unclear utility. Never store sensitive psychological inferences by default.

---

## 16. Experiment E12 — Shadow-mode proactivity

### Question

Which proactive suggestions are useful enough to surface?

### Decision affected

Monitoring, interruption, and initiative policy.

### Design

Run two or three read-only monitors silently for four weeks: stale transitions, broken links, review due, or changed external reference. Present one digest for labeling.

### Measures

- useful, late, redundant, wrong, intrusive, already-known;
- action taken;
- preferred delivery time;
- false-warning rate;
- review burden.

### Decision rule

Only rules with sustained utility and acceptable nuisance leave shadow mode; default to batching.

---

## 17. Experiment E13 — Permission comprehension

### Question

Can Jonathan predict what Big Brain Time may do before it acts?

### Decision affected

Permission vocabulary and action firewall.

### Design

Twenty scenarios across read, suggest, prepare, local write, delete, calendar draft, email draft/send, health, code, and monitoring. Compare expected and policy result.

### Measures

- agreement;
- explanation time;
- overbroad grants;
- confirmation fatigue;
- target/path comprehension.

### Gate

At least 90% comprehension on enabled action types; confusing rules are redesigned, not explained away.

---

## 18. Experiment E14 — Portable project brain

### Question

Can a project be understood and resumed outside Jonathan’s full personal corpus?

### Decision affected

Productization around federated project packages.

### Design

Export one project into a package containing sources, decisions, state, context contract, re-entry, evaluation, and manifests. Give it to another model or collaborator with no prior context.

### Measures

- startup questions;
- correct first action;
- missing private assumptions;
- unnecessary personal data;
- package size;
- source verification;
- portability.

### Decision rule

Pursue project-brain productization if bounded packages can support accurate resumption without hidden personal dependencies.

---

## 19. Experiment E15 — Second-user design probe

### Question

Which concepts generalize beyond Jonathan?

### Decision affected

Kernel, profile, capability packs, and interface assumptions.

### Design

A second user creates a small project brain through guided onboarding and uses it for two weeks.

### Measures

- setup time;
- terminology confusion;
- fields ignored or reinvented;
- value achieved;
- maintenance;
- desired integrations;
- privacy concerns;
- export understanding.

### Decision rule

Only promote concepts to universal kernel after they survive materially different use.

---

## 20. Experiment E16 — Audit integrity and usefulness

### Question

Can the audit prove event integrity and support trust repair without storing sensitive excess?

### Decision affected

Audit schema, hashing, locking, retention, and UI.

### Design

- mutate every event field and verify detection;
- simulate concurrent writers;
- redact sensitive payloads;
- reconstruct one failed proposal and one successful action;
- test causal-trace interface versus chronological log.

### Gate

Full canonicalized event payload integrity, unique sequence under concurrency, reconstruction of actor/basis/result, and no forbidden sensitive payload.

---

## 21. Experiment E17 — Handoff evidence compilation

### Question

Can handoff packets be generated entirely from current evidence and support correct action without setup questions?

### Decision affected

Cross-model continuity and handoff compiler.

### Design

Compile packets at multiple revisions; introduce repository changes; compare current/stale behavior; give packets to different models.

### Measures

- time to identify first action;
- setup questions;
- stale-state detection;
- false completion claims;
- evidence resolution;
- token efficiency;
- correct handback.

### Gate

No hardcoded repository-state assertions; every factual status links to current run evidence or is marked unverified.

---

## 22. Experiment E18 — System-without-model fallback

### Question

Which capabilities remain useful and safe when generative models are unavailable?

### Decision affected

Product resilience and kernel boundaries.

### Design

Operate diagnostics, search, re-entry, context browsing, planning, and lifecycle without model synthesis.

### Measures

- task completion;
- degraded interactions;
- missing explanations;
- recovery behavior;
- provider lock-in;
- user acceptance.

### Decision rule

Core memory, retrieval, recovery, permission, and lifecycle functions must not require a specific model. Model-dependent capabilities declare degraded mode.

## 23. Experiment E19 — Active-frame control and verified action

### Question

Does an explicit active cognitive frame allocate attention and close consequential actions better than recency-, confidence-, or task-list-based control?

### Decision affected

Whether active-frame, collaborator-context, prediction, verification, and degraded-mode contracts belong in the product kernel.

### Design

For one real project over two weeks:

1. maintain a compact frame containing purpose, protected commitments, open questions, assumptions, contradictions, attention budget, interruption threshold, context gaps, participants, and health limits;
2. rank candidate surfacing events under recency, model confidence, and active-frame policy;
3. give one reviewer shared context and another independently framed context for selected high-consequence claims;
4. run five reversible shadow actions with predicted state, simulated execution result, independent observation, and reconciliation;
5. inject one stale-context and one unavailable-dependency condition and verify that permitted behavior narrows.

### Measures

- useful-suggestion rate and missed important items;
- unwanted interruptions and switching cost;
- protected versus silently displaced commitments;
- common-ground failures and correlated-reviewer errors;
- prediction–outcome mismatch detection;
- false completion claims;
- degraded-mode comprehension and compliance;
- maintenance minutes for the frame and registries.

### Decision rule

Keep the smallest subset of fields that improves commitment protection, error detection, or interruption cost over simpler baselines. Reject any field whose carrying cost exceeds observed control value. No action path advances if execution success can close the action without independent postcondition evidence.

## 24. Baseline packet

Before the next major probe, record:

- time to resume three projects;
- time to find ten known pieces of evidence;
- current corrections and re-explanations per session;
- weekly maintenance minutes;
- number of unprocessed captures;
- active/stale generated artifacts;
- subjective trust and cognitive burden;
- storage and rebuild size/time;
- current model/provider dependencies;
- current permission and deletion comprehension.

Without a baseline, “improvement” becomes a narrative.

## 25. Experiment selection matrix

| Experiment | Impact | Uncertainty | Cost | Safety relevance | Suggested order |
|---|---:|---:|---:|---:|---:|
| E01 plural model | very high | high | low–medium | high | 1 |
| E02 identity/time rebuild | very high | medium | medium | high | 1 |
| E04 synthesis contract | very high | high | medium | high | 1 |
| E06 re-entry ablation | high | medium | low | medium | 1 |
| E10 lifecycle comprehension | high | high | low | very high | 1 |
| E08 retrieval ladder | high | medium | medium | high | 2 |
| E09 narrative/projection | high | high | medium | medium | 2 |
| E11 personal inference | high | high | low | very high | 2 |
| E14 portable project brain | high | high | medium | medium | 2 |
| E03 reconciliation | medium–high | medium | medium | high | 2 |
| E12 proactivity | medium | high | low but time-based | high | 3 |
| E13 permissions | medium | medium | low | very high | before action |
| E15 second user | very high | high | high | medium | after kernel probe |
| E16 audit | medium | medium | medium | high | before action |
| E17 handoff | high | medium | low–medium | medium | 2 |
| E18 no-model fallback | high | medium | low | high | 2 |
| E19 active frame / verified action | very high | high | low–medium | very high | 1 |

## 26. Portfolio stop rules

Pause the experiment program when:

- instrumentation makes normal use substantially heavier;
- more than three probes are active;
- experiments alter the same subsystem so results cannot be attributed;
- the current proof of concept becomes unstable as a baseline;
- privacy or recovery evidence is missing;
- a probe lacks a decision rule;
- findings are not being turned into decisions or removals;
- the portfolio becomes a substitute for simply using the system.

## 27. Experiment card

Use `templates/EXPERIMENT_CARD.md` for each selected experiment. A complete card should state:

- problem and decision;
- hypothesis and alternatives;
- baseline;
- intervention;
- scenarios and failure cases;
- measures;
- privacy and safety;
- expected duration or sample;
- confounders;
- decision and stop rules;
- results;
- resulting design change;
- regression or follow-up evidence.
