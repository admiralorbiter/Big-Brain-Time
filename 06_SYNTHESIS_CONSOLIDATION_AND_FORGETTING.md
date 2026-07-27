# 06 — Synthesis, Consolidation, Compression, and Forgetting

## 1. Core problem

As Big Brain Time grows, it cannot present every source artifact in every context. It needs smaller representations, but compression is never neutral. It changes what is easy to see, what appears important, which disagreements survive, and which future questions can still be answered.

The design goal is not maximum compression. It is:

> Reduce coordination and retrieval cost while preserving the information, alternatives, source access, and uncertainty needed for a declared future purpose.

## 2. There is no universally safe summary

The Information Bottleneck method formalizes compression relative to a relevance variable: preserve the information in one signal that matters for another objective while discarding other detail.

For Big Brain Time, the practical translation is:

> A lossy synthesis must name the question family, task, decision, audience, or capability it is optimized to support.

A project re-entry capsule, legal audit, research synthesis, emotional reflection, handoff packet, and executive brief have different protected information.

Reference: [Tishby, Pereira, & Bialek, “The Information Bottleneck Method”](https://arxiv.org/abs/physics/0004057).

## 3. Synthesis is a family of operations

The current prototype uses “synthesis” for a generated knowledge note. The product should distinguish several operations because their authority and loss differ.

| Operation | What it does | Loss risk | Default status |
|---|---|---:|---|
| Index | Makes source addressable | none semantically | derived projection |
| Exact deduplication | Collapses identical payloads while retaining locations | low | automatic with manifest |
| Normalization | Standardizes dates, names, propositions, formats | low–medium | derived/reviewable |
| Extractive digest | Selects source excerpts | omission | compiled view |
| Abstractive summary | Rephrases and combines | omission + distortion | derived, cited |
| Comparative synthesis | Organizes agreements, conflicts, scopes, and gaps | framing | derived/reviewable |
| Reflection | Proposes meaning or pattern | creates new propositions | hypothesis/proposal |
| Generalization | Forms a rule or semantic memory across episodes | exception loss | proposed, slowly promoted |
| Decision synthesis | Selects a commitment under evidence and values | alternative loss | human-authorized decision |
| Procedure compilation | Converts successful practice into reusable steps | context loss | versioned procedure |
| Context compilation | Builds task-specific working memory | bounded omission | expiring compiled artifact |
| Purge/compaction | Removes representations or payload | destructive | separate lifecycle operation |

Calling all of these “summary” hides important controls.

## 4. Multi-resolution architecture

![Multi-resolution memory](diagrams/18_multi_resolution_memory.svg)

### L0 — Originals

Verbatim episodes, documents, conversations, records, events, and source artifacts. Protected by retention and privacy policy.

### L1 — Addressable structures

Sections, entities, assertions, decisions, tasks, transition fields, quotes, timestamps.

### L2 — Relations and evidence

Support, attack, qualification, derivation, authority, scope, supersession, dependencies.

### L3 — Consolidated semantic structures

Themes, patterns, conceptual models, heuristics, community summaries. Derived and invalidatable.

### L4 — Purpose-bound contexts

Re-entry packs, briefings, handoffs, research exhibits, decision packets.

### L5 — Commitments and effects

Accepted decisions, plans, tasks, permissions, and actions.

The system should be able to answer from a higher layer and drill down to lower layers. It should never need to discard L0 merely because L3 exists.

## 5. The synthesis contract

Every meaningful lossy artifact should carry a contract.

```yaml
synthesis_id: syn.retrieval-architecture.2026-07-27
artifact_type: comparative_synthesis
purpose: decide_next_retrieval_experiment
audience: Jonathan
query_family: architecture_decision
as_of_valid_time: 2026-07-27T23:59:59-05:00
as_of_recorded_time: 2026-07-27T23:59:59-05:00

source_manifest:
  corpus_revision: ...
  items:
    - source_id: ...
      locator: ...
      content_hash: ...

method:
  stages:
    - exact_dedupe
    - extractive_evidence_units
    - conflict_preserving_abstraction
  model: ...
  template_version: ...

protected_content:
  - numerical_results
  - dates_and_effective_periods
  - decisions_and_rationale
  - unresolved_conflicts
  - minority_perspectives
  - negative_results
  - reconsideration_triggers

coverage:
  required_units: [...]
  preserved_units: [...]
  omitted_units: [...]
  unresolved_questions: [...]

loss:
  class: lossy
  known_risks:
    - wording_and_tone_reduction
    - omitted_low_relevance_examples

invalidation:
  stale_when_child_changes: true
  expires_at: null
```

The contract makes compression inspectable and testable.

## 6. Conservative consolidation pipeline

![Consolidation pipeline](diagrams/09_memory_consolidation.svg)

### Stage 1 — Declare purpose

No topic is consolidated merely because it has many notes. Name the future question, workflow, or decision.

### Stage 2 — Freeze source set

Record source IDs, versions, time boundaries, and privacy. A moving source set produces unstable evaluation.

### Stage 3 — Extract information units

Identify facts, observations, interpretations, alternatives, examples, decisions, exceptions, and open questions. Preserve source locators.

### Stage 4 — Exact and near-duplicate analysis

Exact deduplication may be automatic. Near-duplicate equivalence remains reviewable when scope, time, or perspective differs.

### Stage 5 — Conflict and exception preservation

Before abstraction, explicitly collect:

- incompatible applicable assertions;
- different perspectives;
- scope limitations;
- counterexamples;
- negative results;
- unresolved authority;
- temporal changes.

### Stage 6 — Produce artifact variants

Create one or more of:

- extractive digest;
- comparative table;
- abstractive summary;
- pattern proposal;
- decision exhibit.

Do not mix them invisibly.

### Stage 7 — Test retention

Ask whether protected units and representative future questions survive.

### Stage 8 — Human review and promotion

A reflection or generalization becomes durable only after acceptance. The source synthesis remains derived even when a resulting decision becomes canonical.

### Stage 9 — Invalidate and reconsolidate

When material children change, mark the artifact stale. Do not silently mutate it under the same identity.

## 7. When is consolidation appropriate?

A readiness score should be an explanation, not a magic number.

### Positive signals

- the same understanding is reconstructed repeatedly;
- multiple independent sources converge;
- source diversity and session diversity exist;
- retrieval repeatedly returns redundant evidence;
- a real decision or workflow needs a smaller representation;
- the material has become relatively stable;
- a defined regression set can test the result;
- maintenance cost of the raw set exceeds synthesis cost;
- users need a common vocabulary or model;
- the synthesis can preserve meaningful disagreements.

### Negative signals

- material is still rapidly evolving;
- only one episode or source exists;
- the topic is primarily narrative or emotionally contextual;
- the abstraction would create a sensitive personal inference;
- there is no declared future use;
- contradictions are not understood;
- the source set is already concise;
- generated summaries are the main sources;
- the system cannot evaluate information loss;
- the result would become a second canonical authority.

### Proposed readiness explanation

```text
Ready because:
- 14 candidate items from 5 sources and 4 sessions
- the same retrieval architecture explanation was reconstructed 6 times
- one architecture decision is pending
- source set has been stable for 10 days

Not fully ready because:
- one benchmark result is unreplicated
- the privacy implications of local embeddings remain unresolved
```

## 8. Protected information

Protected information depends on purpose, but certain categories deserve strong defaults.

### Usually protect

- exact names, dates, quantities, and units;
- active decisions and rationale;
- status and effective period;
- exceptions and counterexamples;
- unresolved conflicts;
- negative or null results;
- minority perspectives;
- safety and privacy constraints;
- source authority and uncertainty;
- next action and blocking condition;
- reconsideration triggers;
- content marked “do not summarize” or “preserve voice.”

### Often compressible

- repeated background;
- equivalent examples after at least one remains;
- boilerplate;
- low-value process chatter;
- redundant navigation language;
- formatting differences;
- generated connective prose;
- superseded operational detail when the purpose is current action—provided history remains reachable.

## 9. Synthesis evaluation

A good synthesis should be evaluated by retained capability, not aesthetic coherence.

### Structural checks

- deterministic manifest;
- valid source locators;
- no self-citation loops;
- idempotent rebuild;
- stale-child detection;
- privacy compliance;
- output type clearly declared.

### Information-unit checks

- protected unit recall;
- numerical/date/name preservation;
- conflict and minority-view retention;
- exception retention;
- unsupported generalization count;
- source-level citation correctness;
- omission disclosure.

### Task checks

- answers declared future questions;
- reduces context or retrieval cost;
- improves decision or re-entry time;
- does not increase corrections;
- supports drill-down;
- remains understandable after a time gap.

### Human checks

- authentic meaning preserved;
- confidence calibrated;
- result feels lighter than raw sources;
- omissions are acceptable;
- maintenance is justified;
- user can predict when it is stale.

## 10. Consolidation timing

Several timing strategies should remain open.

### Explicit request

Safest and easiest to understand. May miss recurring opportunities.

### Threshold notification

The system notices a possible cluster and asks whether synthesis would help. Requires good precision.

### Periodic “sleep” cycle

A scheduled process proposes deduplication, clusters, conflicts, and reflection candidates. Emerging agent-memory research explores sleep-like consolidation, but Big Brain Time should initially run this as a non-canonical report.

### Retrieval-time compilation

Create a temporary synthesis only when a question requires it. Reduces stored summaries but may be slower and less stable.

### Event-triggered invalidation

Material changes mark affected syntheses stale; regeneration remains explicit or scheduled.

A likely hybrid is: explicit or retrieval-time synthesis, with periodic candidate discovery and deterministic invalidation.

## 11. Forgetting is not deletion

Managed-forgetting research emphasizes reducing prominence and controlling retrieval rather than erasing all history. Big Brain Time should separate visibility from preservation.

### Memory buoyancy

A ranking or view signal based on current relevance, project membership, access, open dependencies, review dates, and explicit pinning.

**Rule:** buoyancy affects default visibility, never truth or retention by itself.

### Preservation value

A separate policy reflecting historical, legal, emotional, safety, explanatory, or recovery importance.

An old item can have low buoyancy and high preservation value.

### Cognitive metabolism

Every persistent artifact, rule, alert, task, collaborator record, and derived view consumes storage, review, retrieval, contradiction, dependency, privacy, and attention capacity. Creation therefore carries a future maintenance claim.

A useful default principle is:

> No persistent artifact without expected future retrieval, accountability, coordination, or learning value.

This is not an automatic deletion rule. It is a requirement to name why an artifact should remain cognitively alive, what may decay or be suppressed, who bears the review cost, and which event should trigger re-evaluation.

## 12. Lifecycle vocabulary

| Operation | Meaning | Reversible? | Payload retained? |
|---|---|---:|---:|
| Hide/filter | Exclude from one view | yes | yes |
| Suppress | Lower default retrieval/notification | yes | yes |
| Archive | Remove from active operation | yes | yes |
| Expire | Artifact no longer valid for reuse | regenerate | yes or policy-dependent |
| Supersede | Prefer a later applicable item | yes conceptually | yes |
| Retract | Withdraw endorsement | yes with history | yes |
| Redact | Remove protected payload but retain structure | partly | no for redacted portion |
| Delete representation | Remove one file/cache/row | depends | may exist elsewhere |
| Purge semantic item | Remove controlled canonical and derived copies | generally no | no in controlled active stores |
| Crypto-erase | Destroy access by destroying encryption key | generally no | ciphertext may remain |
| Unlearn | Remove influence from a trained model | difficult/uncertain | separate problem |

These terms should become product verbs, not implementation details.

## 13. Append-oriented correction versus purge

The current locked ADR says claims are never deleted or mutated. That is appropriate for ordinary epistemic correction but too absolute for privacy and user control.

Proposed revised law:

> Meaningful epistemic correction is append-oriented and never silently destroys history. Authorized redaction or purge is a separate, explicit, scope-limited lifecycle operation with impact enumeration and honest residual-copy reporting.

Use append-oriented correction for:

- corrected research results;
- superseded decisions;
- changing project state;
- historical beliefs and preferences;
- audit explanations.

Use purge or redaction for:

- accidentally captured secrets;
- highly sensitive personal material the owner chooses to remove;
- inappropriate third-party information;
- unlawful retention;
- harmful unreviewed psychographic inferences;
- corrupted generated artifacts with no historical value;
- expired ephemeral content under policy.

## 14. Purge transaction

![Lifecycle and purge](diagrams/13_lifecycle_and_purge.svg)

### 1. Request

Specify item, semantic scope, reason, and desired operation.

### 2. Classify

Determine authority, legal/ethical hold, privacy class, and whether suppression, retraction, redaction, or purge is appropriate.

### 3. Enumerate representations

Search:

- canonical Markdown and attachments;
- Git working history and remote references;
- operational SQLite;
- read models and FTS;
- embeddings and graph projections;
- context packs, summaries, briefings, and handoffs;
- staging and temporary files;
- patch snapshots and undo logs;
- audit payloads;
- backups;
- external model disclosures or connector caches.

### 4. Dry run

Show what will be removed, invalidated, retained, or left in expiring backups.

### 5. Approve

Destructive scope requires explicit, fresh approval. Retrieved evidence cannot authorize it.

### 6. Apply

Redact or purge canonical payload, then remove or invalidate derived copies.

### 7. Rebuild

Rebuild read models and summaries from remaining sources.

### 8. Verify

Search active stores for identifiers, hashes, and known fragments. Verification is evidence, not proof of universal erasure.

### 9. Receipt

Record who authorized the operation, scope, time, policy, and residual retention—without retaining the sensitive payload.

## 15. Git and backup realities

Deleting a working-tree file does not erase Git history or every clone. Sensitive-data removal may require history rewriting, remote coordination, and invalidating prior references. Backups may retain encrypted copies until expiration.

The product should never claim immediate universal deletion unless the storage and key architecture actually supports it.

Possible long-term mechanisms include:

- retention-aware backup manifests;
- domain-segmented encrypted archives;
- per-domain or per-item encryption keys for selected high-risk material;
- scheduled backup expiry and verification;
- external-disclosure logs;
- explicit “active stores clear; backup residual until date” reports.

## 16. Example synthesis contracts

### Re-entry synthesis

**Purpose:** restart a project.  
**Protect:** current milestone, recent decision, blocker, stop point, first action, changes while away.  
**May omit:** old completed tasks, broad background, superseded detail.  
**Must disclose:** stale transition and unresolved status conflicts.

### Research synthesis

**Purpose:** choose the next experiment.  
**Protect:** source quality, methods, effect boundaries, negative results, disagreements, assumptions, open gaps.  
**May omit:** repeated introductions and secondary descriptions.  
**Must not:** convert a preprint result into a universal architecture rule.

### Personal reflection

**Purpose:** understand a recurring experience.  
**Protect:** authentic voice, episode diversity, exceptions, emotional context, time.  
**May omit:** logistical repetition.  
**Must not:** create a stable personality fact without review.

### Handoff

**Purpose:** another model begins the correct work quickly.  
**Protect:** objective, current revision, verified state, open obligations, permitted paths, commands, stop conditions.  
**May omit:** transcript history and redundant rationale.  
**Must disclose:** staleness and unverified status.

## 17. Research hypotheses and experiments

1. Purpose-specific protected-unit contracts will reduce information-loss errors more than generic “summarize carefully” prompts.
2. Extractive-plus-comparative synthesis will be more trustworthy than immediate abstractive narrative for disputed topics.
3. Retrieval-time syntheses will reduce stale-cache maintenance for infrequently used topics.
4. A periodic non-canonical consolidation report will identify valuable deduplication without creating unwanted permanent summaries.
5. Separate buoyancy and preservation scores will reduce clutter without hiding critical history.
6. Explicit purge impact reports will be more understandable and trustworthy than a generic delete button.
7. Idempotence and stale-child tests will catch more practical synthesis defects than model-quality scores alone.
8. Recording expected future value and review cost at creation will reduce persistent low-value cognitive load.

## 18. Open questions

- What future question set is sufficient to evaluate a synthesis?
- How can protected information be selected without requiring extensive manual annotation?
- When should a thematic reflection be stored versus generated on demand?
- How should reconsolidation preserve earlier interpretations?
- What retention policy should apply to model prompts and outputs?
- Can semantic fragments be reliably found across summaries during purge?
- How should backup encryption be segmented without making recovery too complex?
- Which personal memories have intrinsic preservation value even when never retrieved?
- When is forgetting beneficial for learning or creativity rather than merely reducing clutter?
- How does a shared system negotiate one person’s deletion request against another person’s legitimate record?
- How should attention and maintenance cost enter preservation value?
- Which collaborator, alert, prediction, and system-health records justify persistent retention?
