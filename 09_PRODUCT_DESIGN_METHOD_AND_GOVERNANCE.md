# 09 — Product Design Method and Governance

## 1. Why a separate method is needed

Big Brain Time combines product discovery, cognitive modeling, information architecture, software architecture, AI evaluation, personal knowledge management, privacy, and experimental self-use. A normal feature backlog is not enough to govern that complexity.

The source roadmap already contains strong delivery principles: acceptance tests before implementation, read-only before write, deterministic before model-driven, inspectable artifacts, evidence gates, and permission-scoped autonomy. The design studio adds methods for preserving alternatives, selecting risks, and learning from real use before hardening the architecture.

The proposed method combines four traditions:

1. **Design Science Research Methodology (DSRM):** identify problem, define objectives, design artifact, demonstrate, evaluate, communicate.
2. **Spiral development:** choose the next cycle according to the most consequential unresolved risk.
3. **Questions–Options–Criteria:** preserve design alternatives and rationale.
4. **Architecture Tradeoff Analysis:** evaluate candidate architectures through quality-attribute scenarios, risks, sensitivity points, and tradeoffs.

References:

- [Peffers et al., 2007](https://www.jmis-web.org/articles/765)
- [Boehm, 1988](https://ieeexplore.ieee.org/document/59)
- [MacLean et al., 1991](https://www.tandfonline.com/doi/abs/10.1080/07370024.1991.9667168)
- [SEI Architecture Tradeoff Analysis Method](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/)

## 2. Four backlogs, not one

The current project history demonstrates how quickly implementation tasks can dominate. The design phase should maintain four connected backlogs.

### 2.1 Friction and observation backlog

Raw evidence from real use:

- confusion;
- repeated reconstruction;
- slow re-entry;
- incorrect answer;
- stale view;
- awkward capture;
- excessive maintenance;
- useful surprise;
- privacy discomfort;
- feature not used;
- action not trusted.

An observation is not immediately a requirement.

### 2.2 Design-question backlog

Questions about product meaning, architecture, interaction, or policy.

Example:

> When a user expresses a personal preference, should the system store the exact episode, a generalized preference, or both, and how does that preference expire or change?

### 2.3 Experiment backlog

Probes capable of changing a design preference.

Example:

> Compare episode-only, generalized-preference, and context-specific-preference representations across ten real preference queries.

### 2.4 Implementation backlog

Production or prototype work that executes an accepted design or experiment.

Implementation items should name the question or decision they serve. Orphan implementation tasks are a scope smell.

## 3. The design cycle

![Design spiral](diagrams/14_design_spiral.svg)

### Stage 1 — Observe and preserve

Record what happened before interpreting it.

```yaml
observation_id: OBS-BBT-...
date:
workflow:
context:
what_happened:
expected:
actual:
source_artifacts:
impact:
initial_interpretations: []
```

### Stage 2 — Frame the problem

Define the friction, affected users, capability, and consequence. Separate symptom from cause.

Questions:

- What job was the user trying to perform?
- What evidence shows this is recurring or important?
- Is this a product problem, implementation bug, content issue, or training problem?
- What happens if nothing changes?
- Which assumptions make it a problem?

### Stage 3 — Define objectives and quality scenarios

Turn broad desires into scenarios.

```text
Source: Jonathan returning to a project after 60 days
Stimulus: asks for the fastest trustworthy re-entry
Environment: repository changed in the interval
Artifact: re-entry and context subsystems
Response: compiles current state, changes, conflicts, first action
Measure: under 5 minutes to productive work; no stale decision presented as current
```

Quality scenarios prevent terms such as “robust,” “brain-like,” or “safe” from remaining aesthetic.

### Stage 4 — Research and option mapping

Review current system evidence, relevant research, standards, and comparable designs. Produce at least two credible options and criteria.

Do not ask research to choose values that belong to Jonathan. Research can show likely effects; it cannot decide how much capture friction or privacy risk he accepts.

### Stage 5 — Risk selection

Identify the uncertainty most likely to invalidate the design.

Examples:

- semantic model too complex to maintain;
- synthesis hides exceptions;
- re-entry protocol adds more closure work than it saves;
- split authority confuses editing;
- personalization feels invasive;
- derived graph misses critical propagation;
- multi-device need is too weak to justify replication.

The next probe should address this risk, not implement the most visible screen.

### Stage 6 — Design the smallest discriminating probe

A probe should be:

- small enough to discard;
- realistic enough to expose the risk;
- instrumented enough to compare options;
- bounded in privacy and consequence;
- reversible;
- clear about what result would change the design.

Possible probes:

- paper or HTML mock;
- sample data model with worked examples;
- command-line spike;
- synthetic fixture suite;
- manual concierge workflow;
- alternative context packs;
- shadow-mode monitor;
- throwaway database migration;
- user comprehension test;
- structured retrospective.

### Stage 7 — Demonstrate in context

Run the probe on real or representative work. Do not demonstrate only the happy path.

Include:

- stale source;
- conflicting evidence;
- missing field;
- sensitive item;
- long time gap;
- user correction;
- provider or network outage;
- deletion request;
- unexpected but legitimate workflow.

### Stage 8 — Evaluate the joint system

Measure technical and human effects.

Technical:

- correctness;
- determinism;
- latency;
- recovery;
- security;
- compatibility;
- information loss.

Human/system:

- time to productive action;
- correction and re-explanation;
- maintenance;
- comprehension;
- trust calibration;
- cognitive burden;
- authentic voice;
- interruption cost;
- behavior change.

### Stage 9 — Decide

Possible outcomes:

- accept a bounded design;
- revise and rerun;
- retain multiple options under different scenarios;
- defer with a trigger;
- reject;
- retire the current implementation;
- change the problem framing.

### Stage 10 — Communicate and propagate

Update:

- design rationale;
- accepted requirements;
- architecture diagrams;
- risk register;
- regression cases;
- migration notes;
- implementation backlog;
- current product thesis if necessary;
- Ready-to-Resume state.

## 4. Decision packet

Before a major implementation commitment, create a short packet.

```yaml
decision_id: ADR-BBT-...
title:
status: proposed | provisional | accepted | rejected | superseded
scope:
owner:
date:

problem:
capability_scenario:
current_implementation:

options:
  - id: A
    description:
  - id: B
    description:

criteria:
  - value
  - reliability
  - privacy
  - reversibility
  - maintenance
  - adaptability

research_basis: []
current_system_evidence: []
experiment_evidence: []

choice:
rationale:
tradeoffs:
risks:
non_goals:
migration_effect:
acceptance_or_fitness_functions: []
reconsider_if: []
```

The packet should fit in a few pages. Supporting research and experiment reports can remain separate.

## 5. Decision states

### Open

A question exists; options may not yet be complete.

### Exploring

Research or probes are active. No production commitment.

### Provisional

A bounded direction is preferred for the current scenario, but evidence is limited.

### Accepted

The direction governs implementation in a declared scope.

### Trusted

Sustained use supports reliance in a declared scope.

### Authorized

Policy permits the design to perform a declared effect.

### Rejected

An option is not selected; preserve rationale and reconsideration conditions.

### Superseded

A later decision replaces or narrows an earlier decision while preserving history.

“Locked” should be rare and mean process protection, not immunity from new evidence.

### Method and policy jurisprudence

Methods and policies are evolvable governance artifacts, not a fixed constitution handed to Jonathan by the system. Their hierarchy should distinguish:

- **constitutional principles:** stable values and nondelegable authority boundaries;
- **operational policies:** current rules for attention, privacy, action, retention, verification, and review;
- **case records:** decisions, exceptions, incidents, appeals, and trust repairs that show how rules behaved;
- **experiments:** bounded tests of a proposed rule or amendment.

Jonathan may author, grant provisional status, ratify, amend, override, suspend, or deprecate a method. Incidents challenge it; evaluations support or weaken it. Every method record should name scope, status, author/authority, version, evidence, exceptions, supersession, review date, and fallback.

No policy may modify its own authority or convert a model proposal into ratification.

## 6. Architecture review through quality attributes

At major boundaries, run a small ATAM-inspired workshop—even if Jonathan and AI occupy multiple roles.

### Step 1 — Present the business/product drivers

- product wedge;
- primary users;
- transformative outcome;
- non-goals;
- deployment envelope;
- privacy and maintenance budget.

### Step 2 — Present candidate architecture

Use context, container, authority, data-flow, and lifecycle views.

### Step 3 — Build a quality-attribute tree

Example:

```text
Trustworthiness
├── temporal correctness
├── source/citation correctness
├── epistemic-state integrity
├── verified external outcomes
├── recoverability
└── predictable action boundary

Usability
├── capture friction
├── time to re-entry
├── interruption and attention cost
├── correction effort
└── maintenance burden

Resilience
├── visible dependency and context health
├── behaviorally enforced degraded modes
├── bounded fallback
└── explicit recovery path
```

### Step 4 — Prioritize scenarios

Rank by importance and architectural difficulty.

### Step 5 — Analyze approaches

Identify:

- sensitivity points: a parameter or decision strongly affects a quality;
- tradeoff points: one decision affects multiple qualities differently;
- risks: evidence suggests failure;
- non-risks: the approach has adequate evidence;
- unknowns: need a probe.

### Step 6 — Produce next probes

Do not convert every risk into a large implementation task.

## 7. Roles and review modes

A single-person project still benefits from role separation.

### Product owner / lived-experience authority — Jonathan

- determines values, goals, acceptable burden, and personal boundaries;
- supplies real scenarios and corrections;
- approves personal inferences and consequential decisions;
- decides what feels useful or invasive.

### Product/design facilitator — AI collaborator

- organizes questions and alternatives;
- translates research into bounded implications;
- creates diagrams, prototypes, and evaluation plans;
- detects inconsistencies and missing scenarios;
- does not treat its own proposal as acceptance.

Every collaborator assignment should also declare:

- current role and bounded assignment;
- source set and context already seen;
- believed objective and requested decision;
- strengths and known limitations;
- permissions and prohibited effects;
- whether independence from other collaborators is part of the assignment.

When the objective, scope, or source set appears inconsistent, the collaborator initiates common-ground repair before propagating a decision or taking action.

### Implementer

- builds the bounded probe or accepted capability;
- reports actual commands, changes, and limitations;
- avoids weakening tests to fit the design.

### Verifier / adversarial reviewer

- checks source claims, test evidence, edge cases, privacy, and overconfidence;
- attempts to falsify the preferred option;
- receives independently framed context when inherited-premise or correlated-model error is a material risk;
- verifies real postconditions through an observation path appropriate to the action, not merely the executor’s success response;
- may be a separate model session, test harness, or deliberate review mode.

### Archivist / change-control role

- ensures rationale, source, decision status, migration, and supersession remain clear.

One person or model can hold multiple roles, but not invisibly in the same reasoning step.

## 8. Documentation architecture

Documents should be organized by responsibility.

### Stable product documents

- product thesis and principles;
- architecture views;
- kernel contracts;
- authority matrix;
- safety and lifecycle policy;
- evaluation/maturity definitions.

### Evolving design documents

- design questions;
- QOC maps;
- research briefs;
- prototypes;
- experiment reports;
- decision proposals.

### Operational documents

- current project state;
- Ready-to-Resume plans;
- active risks;
- current experiments;
- implementation tasks.

### Historical evidence

- prior decisions;
- rejected options;
- experiment results;
- incidents;
- migrations;
- archived prototypes.

Do not use a single combined blueprint as the only editable artifact. A combined document is a compiled reading view.

## 9. Traceability without bureaucracy

Use a lightweight chain:

```text
observation
  -> design question
  -> capability/quality scenario
  -> option space
  -> research and probe
  -> decision
  -> requirement/fitness function
  -> implementation
  -> run evidence and live feedback
```

Not every minor change needs the entire chain. Use it for high-impact, unclear, or hard-to-reverse choices.

## 10. Managing research debt and design debt

### Research debt

A decision depends on an unverified or outdated claim.

Record:

- claim;
- source status;
- decision affected;
- date to revisit;
- acceptable temporary assumption.

### Design debt

A prototype shortcut obscures the intended responsibility or creates a second authority.

Record:

- shortcut;
- current value;
- failure mode;
- trigger for redesign;
- maximum allowed lifetime.

### Documentation debt

The current artifact cannot explain its own status, source, or relationship to implementation.

The response is not automatically more documentation. It may be deletion, consolidation, or a better generated view.

## 11. Cadence

A suggested cadence during the design phase:

### Weekly

- one real-use friction review;
- one active design question;
- no more than one small probe;
- update Ready-to-Resume state;
- note any new trust-destroying failure.

### Every four weeks

- architecture and product-thesis check;
- keep/simplify/remove review;
- active-frame and attention-policy burden review;
- system-health, degraded-mode, and recovery review;
- method and policy ratify/amend/suspend/deprecate review;
- research agenda reprioritization;
- measurement burden check;
- documentation navigation test.

### At every accepted decision

- update decision packet;
- identify affected diagrams and contracts;
- create or update evaluation cases;
- state migration and rollback;
- close or supersede the question.

## 12. Implementation restart gate

Resume substantial implementation only when all are true:

1. A concrete capability scenario exists.
2. The user or project value is plausible and observable.
3. The current prototype’s failure or limitation is documented.
4. At least two options were considered.
5. The highest-risk assumption is named.
6. A probe or evidence supports the selected option.
7. Authority, privacy, lifecycle, and recovery are understood for the slice.
8. Acceptance tests or a manual evaluation protocol exist.
9. The change is small enough to reverse.
10. The design packet names what remains deliberately out of scope.
11. The active frame and attention cost for the workflow are understood.
12. Observation, prediction, execution, verification, and incident closure are distinct where action is involved.
13. A degraded-mode behavior and recovery condition are named for required dependencies.

## 13. Method anti-patterns

- using sprint completion as proof of product maturity;
- asking a panel of models to create artificial certainty;
- treating agreement among collaborators with the same premise and source set as independent verification;
- generating a giant research review without a decision it can change;
- coding the first plausible schema before modeling real examples;
- turning every prototype field into a universal kernel concept;
- using architectural elegance as a substitute for user value;
- documenting only the selected option;
- treating an ADR as permanently locked despite changed assumptions;
- measuring everything and making the system a self-tracking burden;
- treating API success as verified real-world completion;
- allowing degraded capability to remain merely an error banner instead of narrowing behavior;
- allowing a provisional method to become permanent through inertia;
- allowing the design studio itself to become another unprocessed corpus.

## 14. Design phase definition of done

The design phase can close when Jonathan can answer:

- What is the next product wedge?
- What is the minimum product kernel needed for it?
- Which cognitive objects and memory layers does it require?
- What remains narrative, operational, external, derived, or ephemeral?
- What are the dominant quality attributes and risks?
- What alternatives were rejected or deferred, and why?
- What experiment evidence supports the choice?
- How will success, burden, safety, and reversibility be measured?
- What exact small implementation begins next?
