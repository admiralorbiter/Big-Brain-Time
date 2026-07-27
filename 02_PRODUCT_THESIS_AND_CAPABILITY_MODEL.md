# 02 — Product Thesis and Capability Model

## 1. Product thesis

Big Brain Time should not be defined primarily by a storage medium, database, interface, or AI model. Those are replaceable mechanisms.

The product is a **joint cognitive control and continuity system**:

> It helps a person-plus-artifacts-plus-AI system maintain orientation, form warranted working beliefs, protect commitments, construct the smallest trustworthy context for the current purpose, act deliberately, verify real outcomes, and improve how the collaboration works.

This thesis retains the original assurance-and-context wedge while making room for the larger ambition of a secondary human brain. It also makes a crucial boundary explicit: Big Brain Time is not primarily a memory application with AI attached. Memory is one plane in a controlled process of attention, reasoning, judgment, action, and adaptation.

## 2. The unit of design

The unit is not “the AI assistant” or “the knowledge base.” It is the organized joint system:

```text
Jonathan and other autonomous people
+ AI collaborator roles
+ persistent artifacts and structured state
+ an active cognitive frame that allocates scarce attention
+ methods, policies, evaluation, and system-health controls
+ instrumented and uninstrumented environments
```

![Joint cognitive system](diagrams/01_joint_cognitive_system.svg)

A feature succeeds when the joint system can do something more reliably, safely, or creatively—not simply when the software has another function.

### 2.1 Five functional planes

The second-generation model organizes cognition by function rather than treating participants as the architecture:

1. **Purpose plane:** values and identity guide goals; goals justify commitments. Plans and tasks are means, not silent replacements for goals.
2. **Cognitive control loop:** attend → sense → frame → generate → challenge → decide → act → verify.
3. **Knowledge plane:** observations and sources become qualified claims, accepted working beliefs, decisions, plans, and history with provenance and scope.
4. **Governance plane:** authority, permissions, policies, review, rollback, and cognitive-immune responses bound what may influence belief or action.
5. **Adaptation plane:** predictions, outcomes, incidents, evaluations, and system health change methods and permitted behavior.

These are not five services or databases. Jonathan, AI collaborators, other people, artifacts, and tools participate in different portions of each plane.

### 2.2 Active cognitive frame

The active cognitive frame is the temporary control state that determines what matters now:

- current purpose and desired outcome;
- protected commitments and endangered obligations;
- open questions and decision points;
- active assumptions and unresolved contradictions;
- priority, consequence, novelty, and reversibility;
- attention budget and interruption threshold;
- current participants, roles, and shared understanding;
- known context gaps and degraded capabilities.

Shared artifacts may contain thousands of relevant items. The active frame selects the few that should guide the next cognitive move. It is inspectable, expires or revalidates after material change, and does not become durable personal memory automatically.

### 2.3 Control and adaptation

The loop is closed only when action is followed by observation and reconciliation. A successful API response is execution evidence, not proof that the intended real-world outcome occurred. Before consequential action the system records predicted changes, risks, and verification evidence; afterward it compares expectation with reality and either closes the action, rolls it back, or captures an incident.

The same rule applies to cognition itself. When context is stale, a dependency is unavailable, collaborators share a faulty premise, or the system cannot establish a trustworthy project state, system health must narrow permitted behavior. A degraded system may reconstruct and explain uncertainty while refusing to update canonical state or take external action.

## 3. Product promise

A mature Big Brain Time should make the following promise in a bounded form:

1. **Continuity:** You can return after an interruption and recover the important state without rereading everything.
2. **Grounding:** You can see where an answer, decision, memory, or recommendation came from.
3. **Change awareness:** You can distinguish current, historical, proposed, disputed, and unknown states.
4. **Perspective:** You can preserve different people’s or different-times’ views without forcing premature agreement.
5. **Compression with recourse:** You can use concise views while retaining access to underlying evidence and known omissions.
6. **Commitment:** You can connect understanding to goals, decisions, plans, next actions, and review triggers.
7. **Attention:** The system can explain why something is being surfaced now, defer it without losing it, and protect limited human attention from low-value interruption.
8. **Safety and agency:** The system proposes, explains, and prepares; consequential action remains governed by explicit authority and verified against real outcomes.
9. **Adaptability:** The system can change representation, model provider, interface, workflow, or method without losing the user’s durable meaning.
10. **Recovery:** Canonical information can be exported, restored, inspected, rebuilt, and used in an explicit degraded mode.
11. **Improvement:** The system measures whether it actually reduces cognitive and coordination burden.

## 4. Product anti-promise

Big Brain Time should explicitly not promise:

- perfect memory;
- a single objective model of the person;
- automatic truth from accumulated text;
- omniscient prioritization;
- frictionless capture with zero later processing;
- correct psychological inference;
- safe autonomy merely because an AI is confident;
- complete replacement of calendars, email, health portals, GitHub, or specialized tools;
- meaningful synthesis without a declared purpose;
- permanent retention of everything;
- general intelligence produced by adding more stored context;
- universal suitability for every user without configuration and discovery.

Explicit anti-promises protect trust and product focus.

## 5. Core jobs to be done

### Job 1 — Resume accurately

> When I return to a project, decision, or line of thought after an interruption, help me reconstruct what matters, what changed, where I stopped, and what physical action restarts progress.

Success is measured by time to first productive action, rereads, correction burden, and confidence.

### Job 2 — Explain the present through the past

> When I ask what is currently true, decided, planned, or believed, show the relevant history, source, time boundary, supersession, and unresolved alternatives.

Success is temporal correctness and understandable rationale—not maximal detail.

### Job 3 — Preserve experience without flattening it

> When I capture an event, reflection, preference, or idea, preserve the authentic source and make useful components addressable without pretending that the structured extraction exhausts the meaning.

Success is future usefulness with low capture and maintenance burden.

### Job 4 — Compile purpose-specific context

> When I or another model needs context, assemble the smallest evidence bundle that supports the current task, disclose omissions and conflicts, and remain reproducible.

Success is task performance per unit of context, not smallest token count alone.

### Job 5 — Think across time and scale

> When patterns, recurring constraints, or opportunities emerge across many episodes or projects, help me see them without erasing exceptions or turning generated themes into facts.

Success is useful sensemaking with source lineage and uncertainty.

### Job 6 — Convert understanding into commitments

> When an insight or decision should affect work, help identify consequences, dependencies, next actions, and review triggers.

Success is appropriate follow-through and visible rationale, not automatic activity generation.

### Job 7 — Protect agency while assisting proactively

> When the system notices something useful, surface or prepare it at the right time without becoming surveillance, interruption spam, or silent control.

Success is useful-suggestion rate, low nuisance, predictable permission boundaries, and easy correction.

### Job 8 — Learn how the collaboration works

> When a workflow succeeds or fails, preserve enough evidence to improve the method, not merely the content.

Success is measurable adaptation without an opaque, invasive profile.

## 6. Capability model

The product can be described through eleven capabilities rather than a feature list.

### C1. Preserve

Capture original artifacts, episodes, decisions, and operational events with source, time, privacy, and identity.

### C2. Structure

Make selected elements addressable as entities, assertions, stances, commitments, relations, tasks, and transitions.

### C3. Resolve

Determine which states apply for a requested time and authority policy while retaining conflict and perspective.

### C4. Attend

Maintain an inspectable active frame; allocate human and machine attention using purpose, consequence, uncertainty, reversibility, novelty, contradiction, value sensitivity, and interruption cost—not model confidence alone.

### C5. Retrieve

Find exact, local, temporal, multi-hop, global, and negative evidence with explanations.

### C6. Compile

Build purpose-bound context packs, briefings, re-entry capsules, handoffs, and decision exhibits.

### C7. Synthesize

Create summaries, patterns, alternatives, and proposed interpretations with explicit lineage and loss boundaries.

### C8. Commit

Represent goals, decisions, plans, tasks, dependencies, and review conditions without confusing them with factual truth.

### C9. Propagate

Identify which views, plans, summaries, questions, or actions are affected by a material change.

### C10. Govern

Apply privacy, permission, risk, retention, action, review, system-health, and degraded-mode policies.

### C11. Evaluate

Measure retrieval, correctness, resumption, attention burden, safety, trust, prediction calibration, and real-world outcomes; feed incidents back into method and policy evolution.

## 7. The product kernel

A reusable kernel should contain capabilities that every Big Brain Time deployment needs regardless of domain.

![Product kernel](diagrams/02_product_kernel.svg)

### Universal kernel candidates

- stable identity for agents, artifacts, memory items, and commitments;
- explicit values, goals, commitments, plans, and tasks as distinct object types;
- active-frame and attention-allocation contracts;
- epistemic-state transitions from observation through accepted working belief;
- collaborator capability, context, permission, and common-ground records;
- source and activity provenance;
- valid time, recorded time, and lifecycle state;
- authority and perspective;
- privacy classification;
- memory-item and relation contracts;
- retrieval and context contracts;
- proposal, permission, and audit contracts;
- prediction, verification, incident, degraded-mode, and recovery contracts;
- evaluation cases and run evidence;
- import/export and migration conventions;
- adapter interfaces;
- schema and policy versioning.

### Likely profile-specific material

- vocabulary and aliases;
- life areas and project types;
- source-authority priorities;
- privacy defaults;
- initiative preferences;
- preferred interaction style;
- personal values and constraints;
- preservation and forgetting policies;
- notification budgets;
- models of what “productive,” “important,” or “transformative” means.

### Capability-pack material

- research workflow;
- project management;
- learning and practice;
- writing and creative work;
- health preparation;
- household operations;
- media reflection;
- relationship/contact context;
- software engineering;
- organizational/team memory.

The kernel should not contain Jonathan’s categories as universal product ontology.

## 8. Three product scales

### 8.1 Project Brain

A bounded memory and continuity system for one finite or long-lived project.

**Primary jobs:** resumption, decisions, context, dependencies, handoff, research, experiments, change propagation.

**Advantages:** clear boundary, limited privacy scope, easier evaluation, portable artifact, plausible first reusable product.

**Risks:** may become another project wiki; difficult cross-project learning; identity and personal preferences remain external.

### 8.2 Personal Brain

A longitudinal system across projects, life areas, learning, preferences, experiences, and personal operations.

**Primary jobs:** cross-domain continuity, prospective memory, identity/perspective over time, portfolio sensemaking, personalized collaboration.

**Advantages:** highest potential augmentation value and continuity.

**Risks:** privacy, psychological over-modeling, maintenance, context collapse, rigid identity, unclear authority boundaries.

### 8.3 Shared or Team Brain

A multi-perspective system for a team, household, organization, or collaboration.

**Primary jobs:** shared decisions, handoffs, rationale, conflicting viewpoints, responsibilities, institutional memory.

**Advantages:** high coordination value; clearer economic product.

**Risks:** access control, consent, speaker grounding, disputed authority, surveillance, deletion rights, concurrent editing, organizational politics.

These scales should share contracts where possible, but they are not merely deployment sizes. They have different social and epistemic requirements.

## 9. Product wedges

Several focused wedges could validate the kernel without requiring the entire vision.

### Wedge A — Project Re-entry and Handoff

Input: project artifacts and recent activity.  
Output: cited re-entry capsule, changes while away, next action, handoff packet.  
Kernel tested: identity, time, provenance, retrieval, context, commitments, evaluation.

### Wedge B — Decision and Rationale Explorer

Input: decisions, evidence, alternatives, corrections.  
Output: current decision, history, conflicts, reconsideration triggers, impact.  
Kernel tested: epistemic objects, authority, bitemporality, argumentation, propagation.

### Wedge C — Research Memory Laboratory

Input: papers, notes, experiments, questions, interpretations.  
Output: evidence maps, competing hypotheses, purpose-bound syntheses, research gaps.  
Kernel tested: source monitoring, perspectives, synthesis, consolidation, citation verification.

### Wedge D — Knowledge Assurance Observatory

Input: Markdown/Git corpus.  
Output: integrity, staleness, identity, propagation, conflict, recovery status.  
Kernel tested: parsing, lineage, derived projections, diagnostics, evaluation.

The proof of concept suggests all four. Product discovery should determine which one produces the strongest recurring value and best platform learning.

## 10. Quality-attribute scenarios

A product architecture becomes concrete when quality attributes are expressed as scenarios.

### Reliability

After a failed derived-store rebuild, the prior valid index remains available, canonical sources remain unchanged, and the failure can be diagnosed from a manifest.

### Temporal correctness

When an experiment result is corrected, a current query returns the corrected result, an as-known-then query returns the earlier belief, and the system shows when and why the correction was recorded.

### Perspective preservation

When Jonathan and a collaborator interpret the same event differently, both stances remain attributable; a factual answer does not silently merge the perspectives.

### Reversibility

When one project’s task state is migrated to SQLite, it can be exported and semantically reimported into an empty system, and authority can return to Markdown without losing history.

### Privacy

When a context pack is sent to a remote model, it contains only sources permitted for that destination, records the disclosure manifest, and excludes secrets and unrelated sensitive sections.

### Low friction

When stopping work, recording a useful transition takes under a minute and improves later resumption enough to justify the closeout cost.

### Explainability

When the system suppresses an old item from a default view, Jonathan can see why, reveal it, and change the policy.

### Attention integrity

When several items could interrupt Jonathan, the system explains their consequence, uncertainty, reversibility, novelty, commitment risk, and deferral cost; it does not use model confidence as the sole routing signal.

### Verified action

When an authorized action executes successfully at the tool boundary but the expected external state does not appear, the system reports the mismatch, preserves the prediction and observation, and initiates rollback or incident handling rather than declaring success.

### Adaptability

When a model provider changes, canonical memory and evaluation cases remain usable, and the new model can be benchmarked without data migration.

### Graceful degradation

When a provider, connector, index, or trusted context source is unavailable, the system names the missing capability, narrows permitted behavior, offers a bounded fallback, and records the recovery condition.

## 11. Product principles

1. **Continuity before completeness.** Preserve what is needed to resume and reason; do not capture everything.
2. **Plural cognition, strict boundaries.** Represent perspectives and simulations freely; enforce grounding for factual claims and actions.
3. **Originals remain reachable.** Structured or compressed representations link back to source.
4. **Purpose precedes compression.** A lossy synthesis declares what it is for.
5. **Commitments are not beliefs.** Decisions, plans, and requirements have authority and status, not truth scores.
6. **One writer per information type.** Projections and exports do not become co-equal authorities.
7. **Models propose; policies authorize.** Model confidence is not permission.
8. **Execution is not completion.** Consequential action ends with verified external state or an explicit unresolved incident.
9. **Attention is governed.** Surfacing, deferral, interruption, and escalation consume a finite budget and must be explainable.
10. **Methods are versioned commitments.** Jonathan may propose, test, ratify, amend, suspend, override, or deprecate them.
11. **Use generates evidence.** Features mature through real workflows, not only architecture reasoning.
12. **Maintenance is part of usability.** Every persistent artifact and alert must justify its carrying cost.
13. **The user can leave.** Export, restore, delete, and provider replacement are product capabilities.

## 12. Transformative outcomes

A mature system might feel transformative when Jonathan can:

- resume any important active project after a month in less than five minutes;
- ask why the system believes something and receive a comprehensible evidence and change history;
- move between AI models without reconstructing project context;
- preserve a complex line of thought without prematurely forcing it into settled claims;
- notice recurring constraints across work and personal projects without manually rereading journals;
- safely explore multiple future scenarios while keeping them distinct from current reality;
- allow the system to prepare useful work without fearing silent external action;
- remove or purge sensitive information with a truthful report of residual copies;
- understand how the system’s model of him changed and correct it;
- spend less time maintaining the system than the coordination effort it saves.

## 13. Product hypotheses to test

1. Re-entry is the most valuable recurring wedge.
2. A plural cognitive object model reduces false factualization without making capture too complex.
3. Purpose-bound context packs outperform full-history prompting on correctness and coordination cost.
4. Narrative originals plus structured projections outperform either pure prose or total atomization.
5. Explicit transition state is more useful than broad conversation history for resumption.
6. A small authority/time/provenance kernel generalizes across project, research, and learning domains.
7. Consolidation improves retrieval only when it preserves exceptions and source lineage.
8. Users value a visible design rationale and correction path enough to tolerate some additional structure.
9. Shadow-mode proactivity can reveal useful rules without creating surveillance or notification fatigue.
10. A project-brain product can teach the kernel enough to later support a personal brain.
11. Consequence- and commitment-aware attention allocation outperforms confidence-only routing on joint-system benefit and interruption cost.
12. Prediction-and-verification receipts improve calibration and catch technically successful but practically wrong actions.
13. Explicit degraded modes preserve usefulness while preventing uncertain reconstruction from silently changing canonical state.

## 14. Product questions that remain open

- Is Big Brain Time fundamentally a personal tool, a framework, a developer platform, or a product for broader users?
- Should other users edit Markdown directly, or should Markdown become an export/internal format?
- How much epistemic structure can ordinary users understand and maintain?
- Which parts of a personal profile may be inferred, and which require explicit declaration?
- Can a reusable kernel stay small, or does every domain require specialized semantics?
- What is the right economic or distribution model for a local-first product?
- How much model independence is worth the adapter and evaluation burden?
- At what point does multi-user collaboration require a different product rather than an extension?
- Which fields belong in the smallest useful active cognitive frame?
- What evidence is strong enough to interrupt Jonathan, and what should always wait for review?
- How should common-ground disagreement be detected and repaired without constant restatement?
- Which degraded modes permit read, synthesis, proposal, canonical mutation, or external action?

These questions belong in the design studio, not in premature implementation commitments.
