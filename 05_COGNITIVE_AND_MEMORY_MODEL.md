# 05 — Cognitive and Memory Model

## 1. Design objective

A system intended to function as a secondary human brain must represent more than retrievable factual statements. It must support experience, source, perspective, meaning, preference, imagination, commitment, procedural skill, future intention, and revision.

The goal is not to simulate the biological brain literally. It is to borrow distinctions that help the product avoid known failure modes:

- treating memories as recordings;
- confusing imagined, inferred, reported, and perceived content;
- forcing subjective meaning into factual truth categories;
- allowing repeated or recent content to become authority;
- losing episodic detail while extracting patterns;
- turning a temporary self-description into a permanent identity model;
- confusing belief with desire or intention;
- treating disagreement as a database error rather than a perspective or argument structure.

## 2. Research foundations and design implications

### 2.1 Autobiographical memory is constructed in relation to the self and current goals

Conway and Pleydell-Pearce’s self-memory system describes autobiographical memories as transitory constructions shaped by an autobiographical knowledge base and the current goals of a working self. This suggests that a retrieved memory is not simply a fixed file returned unchanged; the cue, current purpose, and self-context influence what becomes salient.

**Design implication:** Big Brain Time should preserve source artifacts and historical records while treating each retrieval or narrative reconstruction as a purpose- and perspective-bearing activity. A generated “memory” should not overwrite the evidence from which it was constructed.

Reference: [Conway & Pleydell-Pearce, 2000](https://pubmed.ncbi.nlm.nih.gov/10789197/).

### 2.2 Source monitoring is a distinct cognitive problem

Source-monitoring research examines how people attribute information to perception, memory, inference, imagination, or another source—and how these attributions can fail.

**Design implication:** provenance should distinguish source mode, not merely store a URL. The system should be able to say:

- Jonathan directly observed this;
- Jonathan remembers this but the original record is absent;
- a colleague reported this;
- a model inferred this;
- this appeared in a simulation;
- this summary was generated from specified sources.

Reference: [Johnson, Hashtroudi, & Lindsay, 1993](https://pubmed.ncbi.nlm.nih.gov/8346328/).

### 2.3 Episodic memory supports future simulation

Research on the constructive episodic simulation hypothesis connects remembering past events with imagining possible future events.

**Design implication:** a secondary brain should support prospective and counterfactual memory objects, not only historical retrieval. It should be able to compose scenarios from prior episodes while marking them explicitly as non-actual.

Reference: Schacter, Addis, and Buckner, “Remembering the past to imagine the future” and related constructive episodic simulation work.

### 2.4 Fast episodic learning and slower semantic integration have different jobs

Complementary Learning Systems theory distinguishes rapid learning of individual episodes from slower integration that extracts shared structure while reducing catastrophic interference.

**Design implication:** capture and consolidation should have different speeds and authority. One new episode can be stored immediately; it should not instantly rewrite a durable generalization about Jonathan, a project, or a domain.

Reference: [McClelland, McNaughton, & O’Reilly, 1995](https://pubmed.ncbi.nlm.nih.gov/7624455/).

### 2.5 Cognition can be distributed across people and artifacts

Distributed cognition and augmentation traditions emphasize that capability can belong to an organized system of people, representations, tools, and processes rather than to an isolated brain or computer.

**Design implication:** diagrams, checklists, context packs, decision records, prompts, and external tools are not merely storage. Their format and propagation affect the cognitive performance of the whole arrangement.

References include Hutchins’ *Cognition in the Wild*, Engelbart’s *Augmenting Human Intellect*, and Licklider’s *Man-Computer Symbiosis*.

### 2.6 Attention is a separate cognitive function

Human–AI teaming research distinguishes reasoning, memory, and attention as foundational functions connected by meta-coordination and governance. Memory makes information available; attention determines what receives scarce processing now. The two should not be collapsed.

**Design implication:** Big Brain Time needs an explicit active cognitive frame and an attention-allocation policy. Surfacing should consider consequence, uncertainty, reversibility, novelty, contradiction, value sensitivity, endangered commitments, interruption cost, and deferral cost. Model confidence alone is not a reliable allocation rule.

Reference: [Gonzalez et al., “Toward a science of human–AI teaming for decision making,” 2026](https://doi.org/10.1093/pnasnexus/pgag030).

### 2.7 Communication requires epistemic vigilance

People depend on communicated information and are therefore exposed to accidental error and intentional manipulation. Evaluating content without evaluating its source, context, plausibility, and supporting path is insufficient.

**Design implication:** observations, interpretations, claims, accepted working beliefs, decisions, and verified states must remain distinguishable. Suspicious sources, prompt injection, circular support, silent goal drift, and confident synthesis from inadequate context should trigger labeling, quarantine, corroboration, challenge, or escalation—not automatic acceptance.

Reference: [Sperber et al., “Epistemic Vigilance,” 2010](https://doi.org/10.1111/j.1468-0017.2010.01394.x).

### 2.8 Groups remember who knows what

Transactive-memory research shows that collective memory includes knowledge about who is responsible for which knowledge and how to retrieve it. A forced division of responsibility can disrupt an established coordination structure.

**Design implication:** Big Brain Time needs a capability and context registry for human and AI collaborators: strengths, known limitations, information seen, current assignment, permissions, and believed objective. It also needs common-ground repair: a collaborator should be able to state its understanding of the objective and request correction.

Reference: [Wegner, Erber, & Raymond, “Transactive Memory in Close Relationships,” 1991](https://doi.org/10.1037/0022-3514.61.6.923).

### 2.9 Belief revision and multiple assumption environments are useful computational analogies

Truth Maintenance Systems preserve reasons for beliefs and revise dependent conclusions when assumptions change. Assumption-Based TMS work supports multiple mutually inconsistent assumption sets without forcing one global state.

**Design implication:** Big Brain Time can represent alternative design worlds, hypotheses, or plans as environments:

```text
Environment: local single-writer system
assumptions: one primary workstation, no concurrent edits
implications: SQLite is practical; CRDT is unnecessary

Environment: collaborative project brain
assumptions: multiple offline writers, shared ownership
implications: conflict and replication semantics become core
```

This is more expressive than labeling one environment `FACT` and the other `UNKNOWN`.

References: Doyle’s Truth Maintenance System work and [de Kleer’s Assumption-Based TMS](https://www.sciencedirect.com/science/article/abs/pii/0004370286900809).

### 2.10 Beliefs, desires, and intentions should not be collapsed

BDI agent architectures separate informational state, motivational state, and committed action.

**Design implication:** Big Brain Time should distinguish:

- **belief/assertion:** how the world is represented;
- **desire/value/goal:** what is wanted or preferred;
- **intention/commitment:** what has been selected for action;
- **plan:** a proposed means;
- **decision:** an authority-bearing choice.

Reference: [Rao & Georgeff, 1995](https://aaai.org/papers/icmas95-042-bdi-agents-from-theory-to-practice/).

### 2.11 Arguments and attacks are different from claim labels

Formal argumentation represents arguments and attack relations and can yield more than one acceptable position depending on semantics.

**Design implication:** disagreement may require an argument graph: premises, conclusions, objections, undercutting evidence, assumptions, and accepted-under-policy status. A `CONTRADICTS` edge between two sentences is often insufficient.

Reference: Dung, “On the Acceptability of Arguments and Its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games” (1995).

### 2.12 Current agent-memory research is informative but immature

Recent work explores consolidation, forgetting, reconsolidation, knowledge graphs, multi-cue retrieval, dynamic organization, and memory safety. These papers are useful sources of mechanisms and test ideas, but they should not be treated as settled product architecture.

Examples:

- [Human-Inspired Memory Architecture for LLM Agents, 2026](https://www.microsoft.com/en-us/research/publication/human-inspired-memory-architecture-for-llm-agents/)
- [MemoryAgentBench, 2025](https://arxiv.org/abs/2507.05257)
- [MemEvoBench, 2026](https://arxiv.org/abs/2604.15774)
- [RHELM, 2026](https://www.microsoft.com/en-us/research/publication/beyond-static-dialogues-benchmarking-realistic-heterogeneous-and-evolving-long-term-memory/)

**Design implication:** evaluate retrieval, test-time learning, long-range understanding, selective forgetting, multi-source evolution, and adversarial memory contamination separately.

## 3. A plural cognitive object model

![Epistemic object model](diagrams/17_epistemic_object_model.svg)

The current claim taxonomies are trying to answer several questions with one label. A more durable model separates dimensions.

### 3.1 Memory item kind

What sort of thing is preserved?

- episode;
- assertion;
- narrative;
- interpretation;
- preference;
- value;
- goal;
- question;
- hypothesis;
- decision;
- plan;
- commitment;
- procedure;
- simulation;
- artifact reference.

### 3.2 Source mode

How did the content enter the system?

- perceived;
- measured;
- remembered;
- reported;
- imported;
- inferred;
- generated;
- imagined;
- accepted from a decision process.

### 3.3 Stance

How does an agent relate to the content?

- asserts;
- remembers;
- reports;
- accepts;
- doubts;
- denies;
- suspects;
- entertains;
- prefers;
- values;
- wants;
- fears;
- intends;
- explores.

### 3.4 Perspective holder

Whose stance is represented?

- Jonathan now;
- Jonathan at an earlier time;
- a collaborator;
- an organization;
- an external authority;
- a particular AI model/run;
- a simulated persona or scenario.

### 3.5 Proposition

Only truth-apt or logically comparable items need a normalized proposition:

```yaml
subject: retrieval_pipeline
predicate: default_method
object: fts5
polarity: positive
scope:
  project: big-brain-time
  component: search
  environment: local
  population: null
```

A preference or narrative may have no useful proposition until a query requires one.

### 3.6 Epistemic resolution

What is the system’s current relationship to the proposition?

- unclassified;
- unreviewed;
- supported;
- insufficient;
- disputed;
- contradicted;
- superseded;
- retracted;
- historical;
- unresolved.

This is not the same as object kind or confidence.

### 3.7 Authority and applicability

- who is entitled to decide or report in the domain;
- when and where the item applies;
- whether the authority binds action, evidence, or only perspective;
- what rule selected or preserved alternatives.

### 3.8 Purpose hierarchy

Motivational and operational objects form a typed chain:

```text
values and identity
        ↓ guide
goals and desired outcomes
        ↓ justify
commitments and obligations
        ↓ constrain
plans, tasks, and actions
```

An AI collaborator may optimize or challenge a plan without silently redefining the goal that justified it. A new opportunity does not automatically supersede an existing commitment. A commitment ledger should record who promised what, to whom, why, by when, its current risk, and the explicit condition that cancels or supersedes it.

### 3.9 Epistemic-state progression

The world does not deliver clean evidence. It supplies observations, messages, measurements, documents, tool results, claims, and interpretations. The system should preserve the stages through which these become action-guiding state:

```text
source or observation
    → interpretation
    → claim
    → corroboration or challenge
    → accepted working belief
    → decision to proceed
    → independent verification or supersession
```

Useful status distinctions include:

- **observed:** the source or tool produced this content;
- **inferred:** this interpretation was generated from declared inputs;
- **accepted:** an authorized actor adopted it as a working belief within a scope;
- **decided:** the system will proceed under an explicit choice;
- **verified:** an independent observation confirmed the material state;
- **superseded:** the item was previously applicable but is no longer current.

Confidence may accompany these states but cannot replace provenance, scope, contradiction, or authority.

## 4. Proposed minimal structures

The following is a conceptual model, not an immediate schema mandate.

```yaml
memory_item:
  id: M-204
  kind: episode
  content: "During the retrieval test, negation cases were easier to find with FTS5."
  source_artifact: run://retrieval/e17
  experienced_at: 2026-07-26T14:30:00-05:00
  recorded_at: 2026-07-26T15:05:00-05:00
  privacy: private
  lifecycle: active

stance:
  holder: agent.jonathan
  toward: M-204
  mode: interprets
  content: "Lexical retrieval may need to remain primary for contradiction work."
  valid_from: 2026-07-26

assertion:
  memory_item: M-204
  proposition:
    subject: contradiction_retrieval
    predicate: comparative_performance
    object: fts5_better_on_seeded_negation_cases
  resolution: supported_in_bounded_experiment
  evidence:
    - run://retrieval/e17

commitment:
  id: K-19
  kind: decision
  content: "Keep FTS5 as the default baseline pending broader evaluation."
  authority: agent.jonathan
  status: active
  reconsider_if:
    - hybrid retrieval improves hard-case recall by the declared threshold

active_frame:
  purpose: "Choose the next retrieval experiment."
  protected_commitments: [K-19]
  open_questions: ["Does hybrid retrieval improve the hard cases?"]
  active_assumptions: ["The seeded cases resemble real queries."]
  attention_budget: "one 45-minute review"
  interruption_threshold: "new evidence that threatens K-19"
  context_gaps: ["No longitudinal query sample yet."]
  expires_on:
    - material source-set change
    - experiment decision recorded

collaborator_context:
  collaborator: agent.retrieval_reviewer
  assignment: "Challenge the experiment interpretation."
  has_seen: [run://retrieval/e17, K-19]
  strengths: [evaluation_design, contradiction_analysis]
  limitations: [no_access_to_private_journal, no_lived_project_context]
  permissions: [read, propose]
  believed_objective: "Test whether FTS5 should remain the default baseline."
```

The episode, interpretation, assertion, decision, active frame, and collaborator context are related but not identical.

## 5. Memory families for product design

### 5.1 Episodic memory

Specific events and experiences situated in time and context.

**Examples:** a meeting, failed deployment, conversation, discovery, emotional response, experiment run.

**Product behavior:** preserve source and context; retrieve by cues; support reflection and future simulation; avoid immediate generalization.

### 5.2 Semantic memory

General concepts, definitions, patterns, and durable knowledge abstracted across episodes or sources.

**Examples:** how a system works, a learned heuristic, stable project architecture, a domain concept.

**Product behavior:** consolidate slowly; retain lineage and exceptions; invalidate after source change; distinguish accepted knowledge from proposed reflection.

### 5.3 Procedural memory

How to perform a task or coordinate a workflow.

**Examples:** restore procedure, release checklist, research workflow, how Jonathan likes to close a project session.

**Product behavior:** version procedures; connect to demonstrations and outcomes; retrieve at action time; treat repeated success as evidence but not infallibility.

### 5.4 Prospective memory

Remembering to perform an intended action when a time, event, context, or state occurs.

**Examples:** review a decision after a benchmark, prepare for a meeting, resume a project when a dependency clears.

**Product behavior:** connect commitments to triggers; preserve why the trigger matters; avoid notification overload; distinguish reminders from calendar authority.

### 5.5 Active cognitive frame

The temporary, bounded control state needed for the current task.

**Examples:** current purpose, protected commitments, open questions, active assumptions, salient contradictions, attention budget, interruption threshold, context gaps, current roles.

**Product behavior:** compile purpose-specific views; explain surfacing and deferral; protect endangered commitments; expire or revalidate after material change; do not treat active context as durable memory automatically.

### 5.6 Social and perspective memory

Who said, believed, preferred, promised, or understood what—and for which audience.

**Examples:** a partner’s preference, a team decision, an AI auditor’s concern, Jonathan’s earlier position.

**Product behavior:** retain speaker and audience; enforce consent and privacy; do not merge viewpoints into an artificial consensus.

### 5.7 Metacognitive memory

Knowledge about how Jonathan and the system work together.

**Examples:** which explanation formats help, which alerts are intrusive, which closeout fields improve resumption, which tasks are repeatedly reconstructed.

**Product behavior:** human-reviewable, evidence-linked, time-bound, and easy to correct; never an opaque personality dossier.

### 5.8 Transactive and common-ground memory

Knowledge about who knows what, what each participant has seen, what each believes the objective is, and how to repair divergent understanding.

**Examples:** a researcher has read corpus A but not the decision history; an adversarial reviewer has read-only permission; two collaborators disagree about whether the goal is exploration or selection.

**Product behavior:** maintain explicit capability, context, assignment, limitation, and permission records; prefer independent context when correlated error is a concern; surface a compact “my understanding of the objective” repair when common ground appears broken.

### 5.9 System-health memory

Current and historical knowledge about the reliability and availability of the joint system itself.

**Examples:** stale index, changed model version, unavailable connector, corrupted canonical document, unresolved policy conflict, overloaded human reviewer.

**Product behavior:** bind health state to allowed behavior; name degraded capability and recovery path; prevent uncertain reconstruction from silently updating canonical records or taking external action.

## 6. Memory layers

![Multi-resolution memory](diagrams/18_multi_resolution_memory.svg)

### L0 — Original artifacts and episodes

Verbatim source, durable within retention policy.

### L1 — Addressable spans and records

Sections, entities, assertions, decisions, tasks, transition fields.

### L2 — Evidence and relationship structures

Sources, provenance, support/attack, dependencies, scope, temporal relations.

### L3 — Consolidated reflections

Patterns, themes, heuristics, conceptual models. Derived and invalidatable.

### L4 — Purpose-bound views

Context packs, briefings, handoffs, re-entry capsules, decision exhibits.

### L5 — Commitments and actions

Accepted decisions, active plans, tasks, permissions, and executed outcomes.

Information flows both upward and downward. A decision creates new experience; a view must allow drill-down; a new episode may challenge a reflection without deleting it immediately.

## 7. Query modes and cognitive policy

A brain-like system should not use one universal “truth mode.”

### Factual mode

Purpose: determine a world-state assertion.  
Policy: strict source, scope, time, authority, conflict disclosure, and abstention.

### Memory mode

Purpose: reconstruct what was experienced or remembered.  
Policy: preserve first-person source, distinguish memory from external verification, show later reconstruction where relevant.

### Perspective mode

Purpose: understand how different agents interpreted or valued something.  
Policy: retain holders and audience; do not force one winner.

### Exploration mode

Purpose: consider hypotheses or design alternatives.  
Policy: maintain assumption environments, evidence for/against, and uncertainty.

### Decision mode

Purpose: select a commitment under evidence, values, and constraints.  
Policy: make values, alternatives, authority, and reconsideration triggers explicit.

### Simulation mode

Purpose: explore a possible future or counterfactual.  
Policy: mark assumptions and non-actual status; allow creative composition; exclude from factual retrieval unless explicitly requested.

### Narrative mode

Purpose: preserve meaning, voice, and temporal self-understanding.  
Policy: minimal structural intrusion; source and privacy remain, but not every sentence requires classification.

## 8. The self model

A personal cognitive system inevitably contains a model of its user. The design must prevent that model from becoming rigid or invasive.

### Permitted categories

- explicit preferences;
- accepted values and constraints;
- declared goals;
- interaction settings;
- observed workflow patterns with evidence;
- temporary hypotheses marked as such;
- time-bounded past preferences;
- user-corrected descriptions.

### Prohibited or high-friction categories

- unreviewed psychological diagnoses;
- permanent identity claims inferred from a small sample;
- hidden persuasion profiles;
- sensitive inferences retained without purpose;
- claims that a temporary mood reflects a stable trait;
- model-generated “insights” that influence recommendations without disclosure;
- identity conclusions that cannot be inspected, corrected, or deleted.

### Proposed self-model contract

Every durable personal inference should include:

```yaml
statement: ...
source_examples: [...]
created_by: ...
created_at: ...
validity: temporary | review_date | open-ended
status: proposed | accepted | rejected | superseded
uses_allowed: [...]
uses_prohibited: [...]
confidence_or_uncertainty: ...
reconsider_if: ...
```

## 9. Memory evolution and contamination

Persistent memory creates a longitudinal attack and error surface. Repetition, biased feedback, noisy tools, or generated summaries can gradually reshape later behavior.

MemEvoBench and related emerging research call attention to “memory misevolution”: long-run drift from contaminated updates.

Big Brain Time should test:

- a false assertion repeated in many captures;
- one generated summary citing another generated summary;
- a scope-limited observation generalized globally;
- a model preference becoming attributed to Jonathan;
- a temporary project rule persisting after its environment changes;
- an adversarial source accumulating links and retrieval frequency;
- a social majority overwriting a minority or historical perspective.

Frequency, recency, and graph centrality must not become authority by accident.

### Cognitive immune response

The system should not pretend to decide truth autonomously. It should provide bounded responses to epistemic and control hazards:

- **label** unsupported or low-context material;
- **quarantine** content from canonical promotion or control paths;
- **challenge** provenance, scope, circular support, or goal alignment;
- **corroborate** through an independent source or independently framed collaborator;
- **escalate** when consequence, contradiction, privacy, or value sensitivity exceeds policy;
- **repair** affected views and commitments after a bad premise is found.

This mechanism belongs across ingestion, retrieval, synthesis, collaboration, and action—not in one “safety model.”

## 10. Worked examples

### Example A — Subjective experience

> “The meeting felt unproductive.”

- kind: episode or observation of subjective experience;
- source mode: experienced;
- holder: Jonathan;
- stance: reports/feels;
- externally factual conclusion: none implied;
- possible interpretation: meeting lacked a decision structure;
- possible action: test an agenda template;

The feeling is real as an experience. The explanation remains an interpretation or hypothesis.

### Example B — Changing preference

> “I prefer CLI tools.”

Store as a time-bounded preference, not a universal fact. Later evidence might show a preference for CLI during debugging and visual workbench during review. The narrower pattern qualifies the earlier generalization.

### Example C — Decision versus observation

Decision: “FTS5 is the default retrieval baseline.”  
Observation: “Hybrid retrieval improved three low-overlap cases.”

The observation does not automatically contradict or supersede the decision. It may support a reconsideration trigger or a domain-specific hybrid policy.

### Example D — Future simulation

> “Suppose Big Brain Time becomes a shared project brain for a nonprofit team.”

Create a simulation environment with assumptions, stakeholders, access rules, and predicted tensions. Do not let simulated participants or policies surface in current personal-system answers.

### Example E — Reconstructed autobiographical memory

Jonathan remembers choosing a design because of privacy. A contemporaneous ADR says the primary rationale was reversibility. Preserve the remembered narrative and the record; do not silently “correct” the personal memory. A perspective answer can explain the difference.

## 11. Design hypotheses

1. Separating kind, source mode, stance, perspective, and resolution will reduce false factualization.
2. Most captures do not need full proposition normalization at ingestion.
3. Narrative originals plus derived structured objects provide a better maintenance/value balance than either pure prose or total atomization.
4. Explicit simulation environments will increase creative planning without contaminating current-state memory.
5. Slow, reviewed self-model updates will improve personalization more safely than continuous opaque profile inference.
6. Argument structures will be useful for architecture and research decisions but excessive for ordinary facts.
7. A small set of cognitive modes will be easier to understand than dozens of inline epistemic markers.
8. An explicit active frame will improve resumption and reduce irrelevant context more than adding undifferentiated long-term memory.
9. Attention allocation using consequence, commitment risk, uncertainty, reversibility, novelty, and interruption cost will outperform model-confidence routing.
10. Capability/context records and common-ground repair will reduce correlated collaborator errors and repeated explanation.
11. Prediction-and-verification records will expose technically successful but practically incorrect actions.

## 12. Open research and design questions

- How should retrieval of autobiographical material change with current purpose without rewriting the source?
- What is the minimum useful perspective model for a single user and multiple AI collaborators?
- Can source mode be captured reliably without interrupting ordinary capture?
- Which object kinds need stable schemas, and which should remain extensible tags?
- How should reconsolidation be represented when a memory changes after retrieval?
- What distinctions are understandable to non-expert users?
- Which parts of procedural memory should be inferred from repeated actions versus explicitly authored?
- How does the system preserve skill and judgment rather than encourage excessive cognitive offloading?
- How are consent and deletion handled when memory concerns other people?
- When should the system intentionally surface a past self rather than current interpretation?
- What is the minimum active frame that changes behavior without becoming another maintenance burden?
- Which attention-allocation factors are observable and understandable enough for daily use?
- When should collaborators share context, and when should they reason independently to avoid inherited-premise failures?
- Which health failures require abstention, read-only fallback, or a ban on canonical mutation?
