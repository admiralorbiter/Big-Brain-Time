# Big Brain Time Design Studio

**Prepared:** 2026-07-27  
**Mode:** research, architecture, product design, and deliberate experimentation  
**Starting point:** the current Big Brain Time repository is treated as an instrumented proof of concept—not as a frozen product architecture.

## What this package is for

Big Brain Time has already crossed an important threshold: it is no longer only a collection of notes or a speculative architecture. It is a working prototype that exposes real questions about memory, truth, continuity, synthesis, planning, autonomy, and human–AI collaboration.

That is exactly the point at which building faster can become less useful than **designing more deliberately**.

This package creates a temporary “design studio” around the prototype. Its purpose is to let Jonathan:

1. Understand what has actually been built and what maturity claims are justified.
2. Separate the cognitive model, product model, technical architecture, and delivery process.
3. Explore multiple architectures without prematurely choosing one.
4. study relevant research as a source of constraints and experiments—not as a list of features to copy.
5. Turn broad ideas into explicit design questions, options, criteria, prototypes, and evidence.
6. Decide what belongs in a universal product kernel, what is Jonathan-specific, and what should remain external.
7. Resume implementation only when the next design risk is understood well enough to justify a small probe.

The package is intentionally larger than an implementation plan and smaller than a final specification. It is a **thinking environment**.

![Joint cognitive system](diagrams/01_joint_cognitive_system.svg)

## Central product hypothesis

> Big Brain Time can become a durable joint cognitive capability platform by preserving source and history, maintaining an explicit active frame, representing epistemic state and commitments, coordinating human and AI roles, compiling purpose-specific context, closing action through independent verification, and adapting its methods under explicit human authority.

The original blueprint correctly identified a narrower first opportunity: accurate resumption, conflict detection, and source-grounded context. The design studio keeps that practical kernel while exploring the larger ambition of a secondary cognitive system.

The joint cognitive system is organized through five functional planes: purpose, cognitive control, knowledge, governance, and adaptation. Its core loop is `attend → sense → frame → generate → challenge → decide → act → verify`. Participants and tools contribute across those planes; they are not themselves the operating model.

## Eight distinctions to keep visible

The package uses eight distinctions repeatedly because much of the architectural confusion comes from collapsing them:

### 1. Prototype versus product

A prototype proves that an interaction or mechanism can exist. A product must also be understandable, recoverable, governable, maintainable, and useful over time.

### 2. Cognitive object versus factual claim

Episodes, narratives, preferences, goals, plans, decisions, hypotheses, and simulations are all useful memory objects, but they do not all have the same truth conditions.

### 3. Canonical authority versus derived representation

A search index, graph, summary, context pack, or embedding may be useful without becoming the authoritative place where the underlying meaning lives.

### 4. Research result versus design decision

Research constrains what is plausible and reveals failure modes. It rarely determines a product choice without considering this system’s goals, users, scale, privacy, and maintenance burden.

### 5. Technical correctness versus joint-system improvement

A module can pass tests and still make Jonathan’s overall workflow slower, noisier, harder to trust, or more dependent on maintenance.

### 6. Available memory versus active attention

An artifact may be relevant without belonging in the current frame. Surfacing and interruption must be governed by purpose, commitment risk, consequence, uncertainty, reversibility, novelty, and attention cost—not model confidence alone.

### 7. Execution versus verified outcome

A successful tool response proves that an operation was attempted or accepted at one boundary. Consequential action is complete only when the intended external state is independently observed and reconciled with the prediction.

### 8. Tools versus autonomous people

Calendar and GitHub are instrumented external authorities. People and institutions have their own rights, interpretations, expectations, and capacity to disagree; they are not systems to query or modify.

## Recommended reading path

The documents can be read linearly, but the package is designed for repeated passes.

### Pass 1 — Orient to the proof of concept

1. [`00_DESIGN_STUDIO_CHARTER.md`](00_DESIGN_STUDIO_CHARTER.md)
2. [`01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md`](01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md)
3. [`02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md`](02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md)

**Output:** a one-page statement of what Big Brain Time is trying to make possible and which current capabilities should be preserved.

### Pass 2 — Understand the whole system

4. [`03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md`](03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md)
5. [`04_SUBSYSTEM_ATLAS.md`](04_SUBSYSTEM_ATLAS.md)
6. [`12_DIAGRAM_ATLAS.md`](12_DIAGRAM_ATLAS.md)

**Output:** mark each subsystem as `core`, `capability pack`, `adapter`, `external authority`, `derived`, or `not yet justified`.

### Pass 3 — Study the cognitive model

7. [`05_COGNITIVE_AND_MEMORY_MODEL.md`](05_COGNITIVE_AND_MEMORY_MODEL.md)
8. [`06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md`](06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md)

**Output:** work through three real memories, one changing belief, one preference, one decision, and one scenario using the proposed object model.

### Pass 4 — Preserve alternatives

9. [`07_DESIGN_TENSIONS_AND_OPTION_SPACES.md`](07_DESIGN_TENSIONS_AND_OPTION_SPACES.md)
10. [`08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md`](08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md)

**Output:** select no more than three design questions for deeper research or prototype work.

### Pass 5 — Establish the design method

11. [`09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md`](09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md)
12. [`11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md`](11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md)
13. the templates in [`templates/`](templates/)

**Output:** create one complete design-question packet and one experiment card before writing new production code.

### Pass 6 — Think beyond the personal prototype

14. [`10_GENERALIZATION_AND_PRODUCTIZATION.md`](10_GENERALIZATION_AND_PRODUCTIZATION.md)
15. [`13_DESIGN_WORKBOOK.md`](13_DESIGN_WORKBOOK.md)
16. [`14_GLOSSARY.md`](14_GLOSSARY.md)
17. [`SOURCES_AND_TRACEABILITY.md`](SOURCES_AND_TRACEABILITY.md)

**Output:** distinguish the universal kernel from Jonathan’s profile and choose the smallest reusable product surface worth testing.

## A paced twelve-session study plan

A “session” can be an hour, an evening, or a week. The sequence is deliberately slower than a sprint plan.

| Session | Focus | Concrete artifact |
|---|---|---|
| 1 | Current proof of concept | Keep / question / retire list |
| 2 | Product thesis | Product promise and anti-promise |
| 3 | Jobs and quality attributes | Top five capability scenarios |
| 4 | System boundaries | Authority and external-system map |
| 5 | Cognitive object model | Five worked memory examples |
| 6 | Retrieval and context | Two context-contract examples |
| 7 | Synthesis and forgetting | One compression contract and one purge case |
| 8 | Design tensions | Two QOC option maps |
| 9 | Research agenda | Three bounded research questions |
| 10 | Generalization | Kernel / profile / capability-pack split |
| 11 | Experiment design | Baseline, probe, measures, stop rule |
| 12 | Architecture review | Decision packet and next smallest build |

No session is required to end in a decision. An explicit unresolved question is a valid outcome.

## Document map

| Document | Primary question |
|---|---|
| [`00_DESIGN_STUDIO_CHARTER.md`](00_DESIGN_STUDIO_CHARTER.md) | How should this design phase operate? |
| [`01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md`](01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md) | What exists now, and how mature is it? |
| [`02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md`](02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md) | What product is being designed? |
| [`03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md`](03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md) | What are the system boundaries and major layers? |
| [`04_SUBSYSTEM_ATLAS.md`](04_SUBSYSTEM_ATLAS.md) | What does each subsystem do, depend on, and risk? |
| [`05_COGNITIVE_AND_MEMORY_MODEL.md`](05_COGNITIVE_AND_MEMORY_MODEL.md) | What kinds of memory and mental objects must be represented? |
| [`06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md`](06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md) | When and how may information be compressed or removed? |
| [`07_DESIGN_TENSIONS_AND_OPTION_SPACES.md`](07_DESIGN_TENSIONS_AND_OPTION_SPACES.md) | Which choices should remain open, and how can they be compared? |
| [`08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md`](08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md) | Which research threads can materially change the design? |
| [`09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md`](09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md) | How are questions converted into evidence-backed decisions? |
| [`10_GENERALIZATION_AND_PRODUCTIZATION.md`](10_GENERALIZATION_AND_PRODUCTIZATION.md) | How can a personal prototype become a reusable platform? |
| [`11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md`](11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md) | Which probes should be run, in what order, with what stop rules? |
| [`12_DIAGRAM_ATLAS.md`](12_DIAGRAM_ATLAS.md) | How can the product and subsystems be inspected visually? |
| [`13_DESIGN_WORKBOOK.md`](13_DESIGN_WORKBOOK.md) | What should Jonathan fill out while studying the system? |
| [`14_GLOSSARY.md`](14_GLOSSARY.md) | What does the package mean by its recurring terms? |
| [`SOURCES_AND_TRACEABILITY.md`](SOURCES_AND_TRACEABILITY.md) | Which ideas came from the current system, prior blueprint, research, or new proposals? |

## Evidence labels

The documents preserve the source package’s practice of distinguishing evidence from proposals, with a few additional labels:

- **`[CURRENT]`** — observed in the current repository or its current documentation.
- **`[SOURCE]`** — supported by the supplied Big Brain Time blueprint and planning materials.
- **`[RESEARCH]`** — supported by cited external primary research, standards, or official documentation.
- **`[PROPOSAL]`** — a design recommendation introduced in this package.
- **`[QUESTION]`** — a deliberately unresolved design issue.
- **`[EXPERIMENT]`** — a proposed probe, benchmark, or field study.
- **`[INFERENCE]`** — a conclusion drawn by combining current evidence and design reasoning.

A proposal does not become an architectural commitment merely because it is written clearly.

## Maturity vocabulary

The package uses the following ladder:

1. **Concept** — a reasoned idea exists.
2. **Prototype** — an inspectable artifact demonstrates feasibility.
3. **Tested** — deterministic tests pass for the stated scope.
4. **Benchmarked** — a declared evaluation suite meets its threshold.
5. **Piloted** — used in real work with recorded feedback.
6. **Trusted** — sustained evidence supports reliance in a defined scope.
7. **Authorized** — policy allows the capability to take a defined action.

These are independent of marketing language. A feature can be technically tested but not productively piloted, or trusted for retrieval but not authorized for mutation.

## Package layout

```text
big-brain-time-design-studio/
├── README.md
├── 00_... through 14_...       # principal design documents
├── SOURCES_AND_TRACEABILITY.md
├── BIG_BRAIN_TIME_DESIGN_STUDIO.md
├── diagrams/                   # Graphviz source and rendered SVGs
├── templates/                  # reusable design and experiment packets
└── reference/source-blueprint/ # preserved copies of supplied planning material
```

## How to edit this package

- Add a dated annotation instead of silently replacing an important unresolved tension.
- Keep design alternatives visible until evidence or an explicit value choice selects one.
- When changing an architectural recommendation, record the scenario or finding that changed it.
- Do not turn every sentence into a requirement.
- Keep diagrams as views over the written model; do not let a diagram become the only definition.
- Prefer one complete worked example over ten abstract fields.
- Remove sections that do not help a decision. The design studio must not become another archive that is hard to use.

## First action

Read [`00_DESIGN_STUDIO_CHARTER.md`](00_DESIGN_STUDIO_CHARTER.md), then spend one session on the “keep, question, retire” worksheet at the end of [`01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md`](01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md). Do not begin with the roadmap. The next build should emerge from the design risk that matters most, not from the next numbered sprint.
