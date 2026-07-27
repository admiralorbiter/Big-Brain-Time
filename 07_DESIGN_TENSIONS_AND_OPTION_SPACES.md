# 07 — Design Tensions and Option Spaces

## 1. Why preserve tensions

Big Brain Time’s most consequential choices are not simple feature decisions. They are tensions among desirable qualities. Choosing one side too early can create an architecture that works beautifully for one interpretation of the product and poorly for another.

This document uses **Questions–Options–Criteria (QOC)** to keep design spaces visible. QOC represents:

- **Question:** the design issue;
- **Options:** plausible responses;
- **Criteria:** values and evidence used to compare options;
- **Assessment:** how each option supports or conflicts with criteria.

The original QOC work argues that design rationale should be constructed alongside the artifact so that later redesign and reuse can understand not only what was selected but what alternatives existed.

Reference: [MacLean, Young, Bellotti, & Moran, 1991](https://www.tandfonline.com/doi/abs/10.1080/07370024.1991.9667168).

![QOC example](diagrams/19_qoc_design_space.svg)

The goal is not to produce a diagram for every minor choice. Use QOC where a decision is poorly understood, value-laden, difficult to reverse, or likely to recur.

## 2. Tension 1 — Truth discipline versus cognitive plurality

### Question

How strict should Big Brain Time be about classifying and verifying stored material?

### Options

**A. Universal epistemic claim system**  
Every durable statement receives a claim type and resolution status.

**B. Free-form memory with factual checks only at answer time**  
Store authentic material with source and time; extract claims when needed.

**C. Plural object model with mode-specific gates**  
Represent episodes, narratives, preferences, goals, plans, decisions, assertions, and simulations separately; apply strict adjudication only to truth-apt answers and actions.

### Criteria

- factual reliability;
- capture friction;
- preservation of voice and meaning;
- ability to represent perspective;
- maintainability;
- explainability;
- migration from current markers.

### Current assessment

Option A supports assurance but risks over-classification and ontology drift. Option B preserves authenticity but weakens proactive contradiction and temporal reasoning. Option C best matches the larger product thesis but requires a carefully bounded kernel.

### Proposed direction

Prototype C while preserving current source text. Do not migrate every old marker until real examples establish the model.

### Discriminating probe

Model ten heterogeneous real items with A, B, and C; compare ambiguity, capture effort, query quality, and user comfort.

---

## 3. Tension 2 — Narrative wholeness versus atomic addressability

### Question

Should knowledge be decomposed into small semantic units or preserved as documents and narratives?

### Options

- **A. Document-first:** structure is mostly metadata and headings.
- **B. Atom-first:** all meaningful content becomes claims/entities/relations.
- **C. Narrative originals with derived addressable projections.**

### Criteria

- authentic context;
- exact retrieval;
- temporal and relation queries;
- maintenance cost;
- deletion behavior;
- model independence;
- ability to reconstruct meaning.

### Current assessment

Total atomization loses framing, ambiguity, and voice. Pure document storage makes propagation and precise reasoning difficult. Option C is the strongest baseline: originals remain authoritative; structured projections are selectively created and always link back.

### Risk

Option C can quietly become dual authority if structured edits and prose edits both change the same meaning.

### Discriminating probe

Choose one complex design conversation. Preserve the transcript, create a narrative summary, and extract atomic objects. Test future questions using each representation alone and in combination.

---

## 4. Tension 3 — Markdown authority versus SQLite authority

### Question

Where should durable state be canonical?

### Options

- **A. Markdown/Git for all durable state.**
- **B. Split authority by information type or field.**
- **C. SQLite/event records as primary; Markdown as export.**
- **D. Federated project packages, each with their own local authority contract.**

### Criteria

- portability;
- transactional integrity;
- hand editability;
- schema enforcement;
- temporal history;
- backup and recovery;
- multi-interface behavior;
- maintenance;
- product usability for non-developers.

### Current assessment

The source blueprint already recommends A as the starting point and B as a likely evolution. The design studio should also evaluate D because project brains may be more reusable and deletable than one monolithic personal corpus.

### Design rule

Do not decide by storage technology. Decide per capability scenario and exact semantic fields.

### Discriminating probe

Run one project aggregate under A and a separate copy under B for two review cycles. Measure edits, drift, export, recovery, and understanding.

---

## 5. Tension 4 — Append-oriented history versus the right to erase

### Question

Should meaningful records ever be deleted?

### Options

- **A. Absolute immutability:** corrections only append.
- **B. Mutable current state with version history.**
- **C. Append-oriented correction plus explicit redaction/purge lifecycle.**
- **D. Retention-limited memory by default.**

### Criteria

- temporal explanation;
- privacy and consent;
- user control;
- legal/ethical deletion;
- audit integrity;
- backup complexity;
- trust.

### Current assessment

C is the most defensible. Ordinary correction preserves history; destructive operations remain separate, explicit, scoped, and honestly limited by backup realities.

### Discriminating probe

Walk one correction, one obsolete task, one sensitive accidental capture, and one third-party record through all four policies.

---

## 6. Tension 5 — Frictionless capture versus usable memory

### Question

How much processing should occur at capture time?

### Options

- **A. Zero-friction append to inbox.**
- **B. Required structured intake.**
- **C. Preserve immediately, process later through suggestions.**
- **D. Process only when retrieval reveals value.**

### Criteria

- capture completion;
- sensitive-data risk;
- backlog growth;
- capture-to-use conversion;
- source quality;
- interruption cost;
- classification accuracy.

### Current assessment

A and B represent familiar failure modes: forgotten inboxes and burdensome forms. A C/D hybrid is promising: preserve a safe minimum, triage cheaply, and invest in structure only when a future use or repeated pattern justifies it.

### Discriminating probe

Collect twenty captures under immediate structured processing and twenty under delayed/on-demand processing.

---

## 7. Tension 6 — Complete context versus bounded context

### Question

How much information should be supplied to a human or model?

### Options

- **A. Full history or handbook.**
- **B. Top-ranked excerpts only.**
- **C. Purpose-bound context contract with evidence, conflicts, omissions, and appendices.**
- **D. Interactive retrieval where the model requests more evidence.**

### Criteria

- evidence recall;
- distractor resistance;
- token and latency cost;
- conflict preservation;
- auditability;
- recipient startup time;
- privacy minimization.

### Current assessment

C is the current architectural center. D may improve difficult workflows but introduces iterative tool and policy complexity. A remains useful as a global audit baseline, not normal memory.

### Discriminating probe

Compare C and D on ten questions where relevant evidence is distributed or weakly lexical.

---

## 8. Tension 7 — Stored summaries versus synthesis on demand

### Question

Should consolidated summaries be durable artifacts?

### Options

- **A. Store summaries at every hierarchy level.**
- **B. Generate all synthesis at query time.**
- **C. Store only high-use or expensive syntheses with invalidation.**
- **D. Store structured information units, generate prose on demand.**

### Criteria

- freshness;
- latency;
- maintenance;
- reproducibility;
- user editing;
- provider dependence;
- ability to compare changing interpretations.

### Current assessment

C and D deserve comparison. Durable prose is useful when it embodies accepted human understanding or is repeatedly used. Generated orientation text should usually be reconstructible.

### Discriminating probe

Track one topic for a month under stored and on-demand synthesis. Measure stale artifacts, repeated generation cost, corrections, and reuse.

---

## 9. Tension 8 — Deterministic systems versus model judgment

### Question

Where should generative or probabilistic reasoning enter the pipeline?

### Options

- **A. Model-first orchestration.**
- **B. Deterministic parsing/retrieval/policy, model only for synthesis.**
- **C. Models propose at every stage; deterministic components validate and constrain.**
- **D. Multiple models deliberate and vote.**

### Criteria

- adaptability;
- factual and action safety;
- maintenance;
- explainability;
- error localization;
- performance;
- provider independence.

### Current assessment

C best fits the ambition if “propose” remains literal. B is a strong baseline and safe fallback. D may improve critique but can multiply cost and shared biases; it must be benchmarked against a single well-prompted model plus deterministic checks.

### Discriminating probe

Use the same ambiguous reconciliation cases with B, C, and D. Compare false resolutions, review time, and explanation quality.

---

## 10. Tension 9 — Local-first simplicity versus multi-device convenience

### Question

How should Big Brain Time operate across devices?

### Options

- **A. One trusted workstation.**
- **B. Multiple capture devices, one processing/writer node.**
- **C. Replicated append log or database.**
- **D. Cloud-hosted canonical service.**

### Criteria

- privacy;
- availability;
- concurrent editing;
- recovery;
- setup and support burden;
- mobile value;
- product distribution.

### Current assessment

B may provide most practical value without committing to concurrent writes. Instrument actual device conflicts before selecting C. D is a different trust and business model.

### Discriminating probe

Run a three-month multi-device need log: capture urgency, offline use, concurrent edits, conflicts, and missed opportunities.

---

## 11. Tension 10 — Personalization versus identity rigidity

### Question

How should the system learn about the user?

### Options

- **A. Explicit settings only.**
- **B. Continuous inferred profile.**
- **C. Evidence-backed, reviewable, time-bounded personal hypotheses.**
- **D. Context-specific profiles with no global synthesis.**

### Criteria

- usefulness;
- privacy;
- correction;
- adaptation;
- user comfort;
- cross-context transfer;
- risk of stereotyping or manipulation.

### Current assessment

C with some D is the preferred direction. Global inferences should be rare; context-specific behavior may be safer and more accurate.

### Discriminating probe

Take ten proposed personalization claims. Ask whether Jonathan recognizes them, wants them stored, and permits each intended use.

---

## 12. Tension 11 — Proactivity versus nonintrusion

### Question

When should the system initiate?

### Options

- **A. Respond only when asked.**
- **B. Batch suggestions in review or re-entry.**
- **C. Triggered notifications with budgets and quiet hours.**
- **D. Active-frame allocation using commitment risk, consequence, uncertainty, reversibility, novelty, value sensitivity, deferral cost, and interruption cost.**
- **E. Continuous adaptive monitoring and negotiation.**

### Criteria

- timeliness;
- interruption cost;
- useful-suggestion rate;
- privacy;
- predictability;
- missed commitments;
- goal and commitment alignment;
- explainability of surfacing and deferral;
- sensitivity to degraded system or human capacity;
- trust.

### Current assessment

Start with B and shadow-mode C, while using D to explain candidate ranking inside the batch. Confidence-only routing is not an acceptable baseline: a model may be highly confident on exactly the cases where human attention is most valuable. E requires mature consent, policy, common-ground repair, health-aware behavior, and evaluation and may never be appropriate for some domains.

### Discriminating probe

Generate candidate alerts silently for four weeks. Compare recency-, confidence-, and active-frame-based ranking. Label each useful, late, redundant, wrong, intrusive, already known, goal-drifting, or commitment-protecting; record both missed commitments and attention cost.

---

## 13. Tension 12 — One personal brain versus federated project brains

### Question

Should Big Brain Time be one longitudinal system or a federation of bounded brains?

### Options

- **A. One personal corpus and kernel instance.**
- **B. Independent project brains with shared tooling.**
- **C. Personal identity/profile layer plus federated project/capability packages.**
- **D. External project systems with only personal context links.**

### Criteria

- cross-project learning;
- privacy separation;
- portability;
- product reuse;
- deletion;
- context boundaries;
- complexity;
- collaboration.

### Current assessment

C is a strong long-term hypothesis. It allows projects to be portable and shareable while a personal layer holds values, preferences, and cross-project continuity. The boundary must prevent private personal context from leaking into shared packages.

### Discriminating probe

Package one project as if another person must use it without access to Jonathan’s private corpus. Record which kernel/profile dependencies appear.

---

## 14. Tension 13 — Universal kernel versus domain-specific semantics

### Question

How much should all capability packs share?

### Options

- **A. Large universal ontology.**
- **B. Minimal common kernel with domain schemas.**
- **C. Unstructured documents plus plugin code.**
- **D. Schema-on-read for every capability.**

### Criteria

- interoperability;
- extensibility;
- maintainability;
- cross-domain queries;
- user understanding;
- plugin isolation;
- migration.

### Current assessment

B is the preferred hypothesis: identity, source, time, authority, privacy, lifecycle, memory items, commitments, proposals, and evaluation are shared; domain meaning remains in capability packs.

### Discriminating probe

Model one research workflow, one project workflow, and one learning workflow. Identify only fields and rules genuinely common to all three.

---

## 15. Tension 14 — Fixed schema versus evolving meaning

### Question

How rigid should the data model be?

### Options

- **A. Strict normalized schema.**
- **B. Flexible JSON payloads and tags.**
- **C. Stable envelope with typed extensible payloads.**
- **D. Narrative-only source with derived schema-on-read.**

### Criteria

- constraints;
- evolvability;
- queryability;
- migrations;
- interoperability;
- preservation of unknown fields;
- developer experience.

### Current assessment

C is likely for canonical structured objects; D remains valuable for narrative source. Strictness belongs at stable boundaries, not every exploratory idea.

### Discriminating probe

Evolve the same sample objects through three requirement changes under A, B, and C; compare migrations, lost meaning, and validation.

---

## 16. Tension 15 — Transparency versus cognitive load

### Question

How much provenance, uncertainty, and policy should the interface show?

### Options

- **A. Always display full evidence and metadata.**
- **B. Show a clean answer with optional details.**
- **C. Progressive disclosure based on risk and conflict.**
- **D. Multiple dedicated views for answer, evidence, and audit.**

### Criteria

- trust calibration;
- usability;
- error detection;
- speed;
- accessibility;
- high-stakes safety;
- attention and maintenance burden;
- learning curve.

### Current assessment

C plus D: concise default output, visible status and key caveats, one-step evidence drill-down, and specialized audit views when needed. The active frame should expose why an item is salient now without requiring the user to inspect the entire epistemic ledger.

### Discriminating probe

Mock the same answer in all four styles and test comprehension, confidence, time, and correction detection.

---

## 17. Tension 16 — General product versus personal research instrument

### Question

Is the primary goal to optimize Jonathan’s system or to build a reusable product?

### Options

- **A. Personal system only.**
- **B. Build a generic platform immediately.**
- **C. Optimize personal use while extracting stable kernel contracts through deliberate productization probes.**
- **D. Open-source framework for technical users rather than end-user product.**

### Criteria

- learning speed;
- authentic need;
- architecture cleanliness;
- distribution/support;
- generalization evidence;
- time and motivation;
- privacy.

### Current assessment

C preserves the living laboratory while preventing Jonathan-specific assumptions from silently becoming universal. D may be a viable intermediate surface.

### Discriminating probe

Give one bounded project-brain package and setup guide to another technically comfortable user. Observe what they understand, change, and reject.

## 18. How to select a tension for work

Score each tension 1–5 on:

- impact on product identity;
- irreversibility;
- current uncertainty;
- evidence from real friction;
- dependency breadth;
- ease of a discriminating probe;
- safety/privacy significance.

Prioritize high-impact, high-uncertainty tensions with cheap probes. Do not prioritize a tension merely because its technology is interesting.

## 19. QOC worksheet

```text
QUESTION:
Why does it matter now?
What scenario exposes it?

OPTIONS:
A.
B.
C.
Current implementation as an explicit option:

CRITERIA:
- user capability
- reliability
- privacy
- reversibility
- maintenance
- explainability
- adaptability
- cost

EVIDENCE:
Current-system observations:
Research:
Assumptions:

ASSESSMENT:
Which criteria does each option support or challenge?
What evidence is missing?

PROBE:
What is the smallest experiment that can change our preference?

DECISION STATUS:
open | exploring | provisional | accepted | rejected | superseded
```
