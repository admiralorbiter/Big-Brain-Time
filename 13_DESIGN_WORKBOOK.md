# 13 — Design Workbook

## How to use this workbook

The workbook is meant to be completed slowly. Copy a section into a dated working note for each session. Use concrete examples from real work. “Unknown” is a useful answer when it becomes a visible question rather than a hidden assumption.

---

# Session 1 — Proof-of-concept inventory

## A. What did the current prototype make possible?

| Capability | Real example | Before BBT | With BBT | Evidence or artifact |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## B. What required repeated correction or maintenance?

| Friction | Frequency | Consequence | Current workaround | Likely cause |
|---|---:|---|---|---|
| | | | | |
| | | | | |
| | | | | |

## C. Keep, question, retire

**Keep and strengthen:**

1.
2.
3.

**Keep as experiments:**

1.
2.
3.

**Redesign:**

1.
2.
3.

**Retire or simplify:**

1.
2.
3.

## D. Maturity claims

For each important capability, mark:

```text
concept | prototype | tested | benchmarked | piloted | trusted | authorized
```

What evidence would be required for the next label?

---

# Session 2 — Product promise

## A. Complete the sentence

> Big Brain Time helps ______________________________ when ______________________________ by ______________________________, while never ______________________________.

## B. Top five jobs

| Job | Trigger situation | Desired progress | Current alternative | Trust-destroying failure |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

## C. Anti-promises

What should the system explicitly not claim or attempt?

1.
2.
3.
4.
5.

## D. Transformative one-year test

> After one year, Big Brain Time would feel transformative if it reliably ______________________________, while requiring no more than ______________________________ of deliberate maintenance per week, and I trusted it enough to ______________________________.

---

# Session 3 — Capability and quality scenarios

## A. Capability scenario template

```text
User / actor:
Situation:
Trigger:
Current friction:
Desired system response:
Evidence required:
Maximum acceptable time:
Privacy boundary:
What must cause abstention:
Success measure:
Failure that destroys trust:
```

Write five scenarios:

1. Re-entry
2. Current/historical truth
3. Research or synthesis
4. Planning/commitment
5. Lifecycle or action safety

## B. Quality-attribute tree

Create a hierarchy for the three most important qualities.

```text
Quality:
├── Subquality:
│   ├── measurable scenario
│   └── measurable scenario
└── Subquality:
```

## C. Tradeoffs

Which two desirable qualities are in tension for each scenario?

| Scenario | Quality A | Quality B | What changes the balance? |
|---|---|---|---|
| | | | |
| | | | |

---

# Session 4 — System boundaries and authority

## A. External system map

| Information type | Current authority | Why | What BBT stores | What BBT may write | Failure if duplicated |
|---|---|---|---|---|---|
| Calendar | | | | | |
| Email | | | | | |
| GitHub/code | | | | | |
| Professional tasks | | | | | |
| Health records | | | | | |
| Research sources | | | | | |
| Personal projects | | | | | |

## B. Representation class

For each item, select:

```text
canonical narrative | canonical operational | external authority |
derived projection | compiled artifact | ephemeral staging | audit evidence
```

## C. Migration candidate

```text
Information fields to move:
Current authority:
Candidate new authority:
User value:
Dual-write risk:
Export format:
Rollback:
Cutover evidence:
Reconsider if:
```

## D. Joint cognitive control case

Choose one consequential workflow and complete:

```text
Values or identity constraints:
Goal and desired outcome:
Protected commitments:
Current purpose:
Open questions:
Active assumptions and contradictions:
Attention budget and interruption threshold:
Participants, roles, source sets, limitations, permissions:
Observation/source:
Interpretation or claim:
Authority for decision:
Predicted external change:
Authorized action:
Independent verification evidence:
Mismatch response:
Current system-health limits:
Degraded-mode behavior:
Recovery condition:
Method or policy that may need revision:
```

---

# Session 5 — Cognitive object model

Choose real examples and complete the matrix.

| Example | Item kind | Source mode | Stance | Perspective | Proposition needed? | Resolution/lifecycle |
|---|---|---|---|---|---|---|
| Objective record | | | | | | |
| First-person experience | | | | | | |
| Interpretation | | | | | | |
| Preference | | | | | | |
| Value | | | | | | |
| Decision | | | | | | |
| Plan | | | | | | |
| Procedure | | | | | | |
| Memory with conflicting record | | | | | | |
| Future simulation | | | | | | |

Questions:

1. Which fields felt natural?
2. Which felt artificial?
3. Which distinctions changed retrieval or reasoning?
4. Which could be inferred later?
5. Which personal inferences should never be automatic?

---

# Session 6 — Retrieval and context

## A. Real question set

Write ten questions you actually want to ask.

| Question | Mode | Time boundary | Authority | Expected evidence | Conflict/abstention condition |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |

Modes:

```text
factual | memory | perspective | exploration | decision | simulation | narrative
```

## B. Context contract

```yaml
purpose:
audience:
query:
as_of_valid_time:
as_of_recorded_time:
authority_policy:
privacy_ceiling:
required_sources:
protected_information:
conflicts_to_show:
allowed_omissions:
token_or_length_budget:
expiration:
```

Create two contracts for the same project: re-entry and architecture review. What changes?

## C. Retrieval ladder

For one difficult question, record results from:

- exact/path lookup;
- FTS;
- metadata/time/authority filters;
- links/relations;
- embeddings;
- global hierarchy.

Which addition changed the result enough to justify its cost?

---

# Session 7 — Synthesis, compression, and forgetting

## A. Synthesis purpose

```text
Source set:
Future task/question:
Audience:
What must survive:
What may be omitted:
What disagreement must remain visible:
What new interpretation may be proposed:
How will the result be tested:
When does it become stale:
```

## B. Compare artifact types

Create from the same sources:

1. extractive digest;
2. comparative synthesis;
3. abstractive summary;
4. reflection/hypothesis;
5. decision exhibit.

Which one is most useful for the declared purpose? Which one is most dangerous if treated as authority?

## C. Lifecycle cases

For each case choose the desired verb and explain why.

| Case | Hide | Suppress | Archive | Supersede | Retract | Redact | Purge |
|---|---:|---:|---:|---:|---:|---:|---:|
| Old completed task | | | | | | | |
| Incorrect research claim | | | | | | | |
| Earlier personal preference | | | | | | | |
| Accidentally captured secret | | | | | | | |
| Sensitive third-party detail | | | | | | | |
| Stale generated context pack | | | | | | | |

## D. Purge impact checklist

- [ ] canonical Markdown
- [ ] Git history/remotes
- [ ] operational database
- [ ] read model and FTS
- [ ] embeddings
- [ ] relation graph
- [ ] summaries/context packs
- [ ] handoffs/briefings
- [ ] staging/temp
- [ ] snapshots/undo
- [ ] audit payloads
- [ ] backups
- [ ] external model disclosures
- [ ] connector caches

---

# Session 8 — Design tension and QOC

Choose two tensions from `07_DESIGN_TENSIONS_AND_OPTION_SPACES.md`.

## QOC 1

```text
QUESTION:
Scenario:
Why now:

OPTION A:
OPTION B:
OPTION C:

CRITERIA:
1.
2.
3.
4.
5.

Evidence for/against each:

Preferred option today:
Confidence:
Missing evidence:
Cheapest discriminating probe:
```

## QOC 2

Repeat.

## Reflection

Did preserving alternatives change the preferred solution? Was the current implementation previously being treated as the only option?

---

# Session 9 — Research agenda

## A. Research-question selection

| Question | Decision impact | Uncertainty | Dependencies | Cost | Safety/privacy | Priority |
|---|---:|---:|---:|---:|---:|---:|
| | | | | | | |
| | | | | | | |
| | | | | | | |

## B. Research brief

```text
RESEARCH QUESTION:
Decision it can change:
Current assumption:

Primary sources:
Standards/official docs:
Current-system evidence:
Contrary evidence:

What the evidence supports:
What it does not support:
Boundary conditions:

Design implications:
Options remaining:
Local probe:
Reconsider date/trigger:
```

## C. Evidence hygiene

- [ ] primary sources for load-bearing claims
- [ ] publication/status recorded
- [ ] result boundary recorded
- [ ] external finding separated from product inference
- [ ] contrary evidence included
- [ ] no benchmark treated as universal product value
- [ ] no cognitive analogy treated as implementation proof

---

# Session 10 — Kernel and productization

## A. Kernel test

For each candidate concept, answer whether at least three different packs need it.

| Concept | Project pack | Research pack | Learning pack | Stable meaning? | Kernel / pack / profile |
|---|---:|---:|---:|---:|---|
| identity | | | | | |
| provenance | | | | | |
| time | | | | | |
| authority | | | | | |
| memory item | | | | | |
| commitment | | | | | |
| context contract | | | | | |
| permissions | | | | | |
| evaluation | | | | | |
| current taxonomy item | | | | | |

## B. Product form comparison

| Product | Primary user | Core job | Minimum capability | Biggest risk | Evidence needed |
|---|---|---|---|---|---|
| Project brain | | | | | |
| Research workbench | | | | | |
| Assurance layer | | | | | |
| Personal platform | | | | | |
| Team brain | | | | | |

## C. Portable project package

What must be included so another person or model can use a project without private personal context?

What should be excluded?

Which hidden assumptions are currently in Jonathan’s head or global corpus?

---

# Session 11 — Experiment design

Use `templates/EXPERIMENT_CARD.md`.

Minimum fields:

```text
Experiment ID:
Decision affected:
Hypothesis:
Alternatives:
Baseline:
Probe:
Failure cases:
Measures:
Privacy/safety:
Decision rule:
Stop rule:
Raw evidence location:
```

## Pre-mortem

Imagine the experiment produced a convincing but misleading result. How might that happen?

- novelty effect;
- handpicked examples;
- model/version dependence;
- measurement changed behavior;
- too-short pilot;
- preferred option received better tuning;
- user already knew expected answer;
- maintenance cost omitted;
- negative cases absent;
- data leakage from benchmark into design.

## Post-experiment decision

- [ ] adopt bounded design
- [ ] revise and rerun
- [ ] preserve multiple options
- [ ] defer with trigger
- [ ] reject
- [ ] retire current implementation
- [ ] reframe problem

---

# Session 12 — Architecture synthesis

## A. One-page product architecture

```text
PRODUCT WEDGE:
PRIMARY USER:
TRANSFORMATIVE OUTCOME:

KERNEL CAPABILITIES:

PROFILE/POLICY:

CAPABILITY PACKS:

CANONICAL AUTHORITIES:

DERIVED REPRESENTATIONS:

EXTERNAL AUTHORITIES:

ACTIVE FRAME AND ATTENTION POLICY:

COLLABORATOR CONTEXT AND COMMON GROUND:

ACTION PREDICTION AND VERIFICATION:

SYSTEM HEALTH, DEGRADED MODES, AND RECOVERY:

DOMINANT QUALITY ATTRIBUTES:

TOP RISKS:

EVIDENCE SUPPORTING THIS ARCHITECTURE:

OPEN ALTERNATIVES:

NEXT SMALLEST BUILD:
```

## B. Implementation restart gate

- [ ] concrete capability scenario
- [ ] real value/friction evidence
- [ ] current prototype limitation documented
- [ ] at least two options considered
- [ ] highest-risk assumption named
- [ ] research/probe supports choice
- [ ] authority and lifecycle understood
- [ ] privacy and recovery understood
- [ ] tests or evaluation protocol exist
- [ ] attention cost and active-frame behavior understood
- [ ] prediction, execution, and independent verification separated
- [ ] degraded-mode behavior and recovery condition named
- [ ] slice is reversible
- [ ] out-of-scope is explicit

## C. Ready-to-Resume plan

**Stop point:**  
**Restart cue:**  
**Next micro-action:**  
**Resumption trigger:**

---

# Ongoing friction log

| ID | Date | Workflow | Observation | Consequence | Source artifact | Design question created? |
|---|---|---|---|---|---|---|
| | | | | | | |

# Ongoing design-question register

| ID | Question | Status | Impact | Current options | Next evidence | Decision link |
|---|---|---|---:|---|---|---|
| | | | | | | |

# Ongoing experiment register

| ID | Decision | Status | Baseline | Probe | Result | Next action |
|---|---|---|---|---|---|---|
| | | | | | | |

# Ongoing simplification register

| Structure/feature | Why it exists | Evidence of use | Maintenance cost | Keep / simplify / remove |
|---|---|---|---|---|
| | | | | |
