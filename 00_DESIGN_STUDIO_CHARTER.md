# 00 — Design Studio Charter

## 1. Purpose

Big Brain Time has a credible proof of concept, a substantial architecture package, and multiple working mechanisms. The next phase is not primarily an implementation phase. It is a period of **design inquiry** intended to clarify the product, cognitive model, subsystem boundaries, architectural tradeoffs, and evidence required before deeper commitment.

The studio exists to answer a different question from a normal sprint:

> What must be understood, represented, compared, and tested so that Big Brain Time can grow into a durable secondary cognitive system without hardening prototype assumptions into permanent constraints?

## 2. Why step back now

The supplied audit and blueprint identified accurate resumption and contradiction detection as the clearest immediate opportunity. It also documented concrete propagation, identity, temporal, retrieval, and recovery failures. The subsequent prototype demonstrates that many proposed capabilities can be implemented, but it also reveals that implementation names can outrun semantic guarantees.

This creates a productive moment:

- There is enough software to expose real rough edges.
- There is enough architecture to see the intended whole.
- There is not yet so much product adoption that redesign is prohibitively expensive.
- Jonathan is still the primary user, making close observation and rapid qualitative learning possible.
- The larger ambition—another brain or capability platform—requires conceptual foundations beyond a collection of features.

The studio treats the repository as a **research instrument**. Its purpose is not to prove the current design correct. Its purpose is to make important assumptions observable.

## 3. Studio mission

> Develop a coherent, evidence-backed design language and product architecture for a local-first human–AI cognitive system that can preserve experience and knowledge, support accurate resumption and action, represent changing perspectives, synthesize without hiding loss, and remain recoverable, governable, and adaptable.

## 4. Scope

The studio covers four connected but distinct layers.

### Layer A — Human and cognitive model

Questions include:

- What types of memory and mental object matter?
- How do facts, observations, interpretations, preferences, values, goals, decisions, plans, narratives, and simulations differ?
- How should source, perspective, confidence, time, and revision be represented?
- What should remain embodied in Jonathan rather than offloaded?
- How should the system help construct futures, not merely reconstruct the past?

### Layer B — Product capability model

Questions include:

- What jobs should Big Brain Time perform?
- Which capabilities form the product kernel?
- What makes a “project brain,” “personal brain,” or “team brain” meaningfully different?
- Which experiences should feel transformative?
- What must the system explicitly refuse to promise?

### Layer C — Technical architecture

Questions include:

- What is canonical, derived, external, or ephemeral?
- Which modules share universal infrastructure?
- Where do Markdown, SQLite, Git, models, graphs, and external systems belong?
- How do retrieval, synthesis, planning, propagation, permissions, and lifecycle interact?
- What must be deterministic, and where is model judgment useful?

### Layer D — Design and evaluation process

Questions include:

- How are alternatives preserved and compared?
- What is the smallest useful probe for a design risk?
- Which measures reflect joint-system improvement?
- When should a feature be simplified or removed?
- What evidence justifies movement from prototype to trusted or authorized behavior?

## 5. Out of scope for the studio phase

The studio does not require:

- a complete rewrite of the current repository;
- implementation of every proposed schema;
- choosing a final mobile, sync, hosting, or model-provider strategy;
- designing for hypothetical scale before a use case requires it;
- turning the personal prototype into a public SaaS product;
- adopting a complete cognitive theory, ontology, graph database, or agent framework;
- producing a final five-year roadmap with fixed dates;
- treating all research findings as product requirements;
- maximizing documentation volume.

Implementation is allowed only when it is the cheapest way to test a material design question.

## 6. Operating principles

### 6.1 Preserve the prototype; do not worship it

The current system contains valuable learned structure. Preserve the repository and record its behavior, but allow any module, schema, taxonomy, or workflow to be redesigned if evidence warrants it.

### 6.2 Separate representation levels

Do not solve a cognitive-model question by immediately adding a database column. First clarify the concept and examples; then decide whether the concept needs durable structure, derived structure, or prose.

### 6.3 Keep alternatives alive long enough to learn

A design question should normally have at least two credible options. A single proposed solution is often an unexamined assumption.

### 6.4 Work from scenarios

Every important architectural property should be grounded in a concrete scenario:

- a project resumed after 90 days;
- a belief corrected after new evidence;
- a preference that changes gradually;
- a summary that hides an exception;
- a private memory that must be purged;
- a model output that is useful but not authoritative;
- a collaborator who disagrees with Jonathan;
- a device or provider that becomes unavailable.

### 6.5 Design for correction

The system will be wrong. The product should make the location, cause, influence, and repair of an error understandable.

### 6.6 Treat maintenance as a product cost

Every schema, marker, relation, prompt, policy, view, and workflow creates ongoing cognitive and technical cost. A concept is not free because it is stored in Markdown.

### 6.7 Preserve authentic human meaning

Formalization should improve addressability and reasoning without erasing narrative, ambiguity, voice, emotion, or historical perspective.

### 6.8 Earn complexity

A more sophisticated method must outperform a simpler baseline on a declared problem. This applies to embeddings, graphs, multi-agent orchestration, formal epistemic systems, CRDTs, complex ontologies, and proactive automation.

### 6.9 Evaluate the joint system

The unit of improvement is not the model or database alone. It is Jonathan + AI + artifacts + language + methods + environment over time.

### 6.10 Preserve exits

Every major commitment needs a way to export, rollback, rebuild, replace, archive, or retire it.

## 7. Studio workflow

![Design spiral](diagrams/14_design_spiral.svg)

Each design cycle follows eight stages.

### 1. Observe

Capture a real friction, surprise, failure, repeated reconstruction, or emerging opportunity. Preserve the raw example.

### 2. Frame

Convert the observation into a design question. Avoid framing that assumes a solution.

Poor framing:

> How should we add vector search to memory?

Better framing:

> Which retrieval failures remain after exact, lexical, temporal, and link-based retrieval, and what additional mechanism addresses them with acceptable privacy and maintenance cost?

### 3. Research

Review current system evidence, comparable systems, primary literature, standards, and implementation constraints. Record what the evidence supports and what remains an inference.

### 4. Map options

Use Questions–Options–Criteria or an equivalent design-space map. Include the current design as one option, not the default winner.

### 5. Build a probe

Create the smallest artifact that can discriminate among options. A probe may be a paper model, mock interaction, schema example, benchmark fixture, command-line prototype, diagram, or throwaway script.

### 6. Pilot

Use the probe in a real or faithfully simulated workflow. Record confusion, workarounds, maintenance, emotional response, and unexpected use—not only task success.

### 7. Evaluate

Compare results with a baseline and stop rule. Distinguish technical correctness from practical value.

### 8. Decide and communicate

Keep, revise, defer, or remove the design. Record rationale, scope, confidence, reconsideration trigger, and the next unresolved risk.

## 8. Core studio artifacts

Every major investigation should produce a small set of durable artifacts:

1. **Friction record** — what happened in real use.
2. **Design question** — what is genuinely unresolved.
3. **Scenario set** — where the design must work or fail safely.
4. **Option map** — plausible choices and criteria.
5. **Research brief** — relevant evidence and limitations.
6. **Probe** — smallest discriminating artifact.
7. **Evaluation record** — measures, observations, confounders.
8. **Decision record** — choice, rationale, scope, reconsideration trigger.
9. **Migration note** — impact on current implementation, if any.
10. **Ready-to-Resume note** — the next micro-action for the design inquiry.

Templates are provided in `templates/`.

## 9. Quality attributes to reason about

The original blueprint already prioritizes reliability, provenance, privacy, reversibility, low maintenance, and human authority. The studio will make tradeoffs among these attributes explicit.

![Quality attribute map](diagrams/20_quality_attribute_map.svg)

For each architecture question, consider at least:

- usefulness;
- cognitive friction;
- fidelity to source and authentic voice;
- temporal correctness;
- explainability;
- recoverability;
- privacy;
- security;
- adaptability;
- portability;
- performance;
- maintainability;
- interoperability;
- accessibility;
- autonomy and predictability;
- generalizability;
- cost of correction.

No design maximizes all of them.

## 10. Decision discipline

A studio finding may have one of five outcomes:

- **Adopt now** — enough evidence exists for a bounded commitment.
- **Prototype next** — the question is important and can be tested cheaply.
- **Research next** — evidence is too weak or conflicting for a meaningful probe.
- **Defer with trigger** — not currently important; name what would reopen it.
- **Reject or retire** — evidence indicates the complexity or behavior is not worthwhile.

A decision must state its scope. “Use SQLite” is not a sufficient decision. “Use SQLite as a disposable local projection for sections and FTS under a deterministic rebuild contract” is closer.

## 11. Stop rules

Pause a design line when:

- the question cannot be connected to a real capability or risk;
- the documentation required to maintain it exceeds its likely value;
- the probe cannot distinguish among options;
- the result depends entirely on imagined future scale;
- the design creates a second source of truth without a migration boundary;
- the system cannot explain or reverse the consequence;
- the proposal rigidly models Jonathan from sparse evidence;
- a simpler representation supports the observed workflow;
- the work becomes architecture theater rather than learning.

## 12. Studio success criteria

The studio phase is successful when:

1. The current prototype has an honest maturity map.
2. The product kernel and product boundaries are understandable without referring to implementation packages.
3. The cognitive model can represent several real examples without forcing all content into factual claims.
4. Major subsystems have clear responsibilities, inputs, outputs, authority, failure modes, and evaluation plans.
5. At least five significant design tensions have credible option spaces.
6. The research agenda is prioritized by expected decision impact.
7. A repeatable design-question-to-experiment workflow exists.
8. Jonathan can identify the next smallest build and explain which uncertainty it tests.
9. The design package is easier to navigate than the collection of ideas it organizes.
10. It remains acceptable to simplify or discard parts of the prototype.

## 13. Initial studio backlog

The first ten design inquiries should be treated as candidates, not a fixed sequence:

1. What kinds of cognitive objects belong in the kernel?
2. What does “current truth” mean across facts, memories, perspectives, and commitments?
3. What should remain Markdown-canonical, become operationally structured, or remain external?
4. What is the minimum useful synthesis contract?
5. Which information must never be compressed away?
6. How should memory visibility, archive, retraction, redaction, and purge differ?
7. Which project/re-entry workflow produces the most measurable daily value?
8. Which shared foundations are genuinely reusable across domains?
9. What aspects of Jonathan’s profile may be learned, and only under what review?
10. What would make a reusable “project brain” valuable to another person without requiring them to adopt Jonathan’s ontology?

## 14. Current phase statement

**Current status:** Design Studio Open  
**Implementation posture:** maintenance and narrow probes only  
**Primary output:** design understanding and experiment-ready decisions  
**Reconsider implementation mode when:** one design question has a bounded option space, discriminating probe, acceptance criteria, and recovery path.
