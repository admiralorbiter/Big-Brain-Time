# 12 — Diagram Atlas

## 1. Purpose

The diagrams are alternate views of the written design, not separate sources of truth. Each rendered SVG has an editable Graphviz `.dot` source in `diagrams/`.

Use them to:

- orient to a subsystem before reading detail;
- compare current and proposed boundaries;
- identify missing arrows, authorities, or lifecycle steps;
- annotate design reviews;
- explain the system to another model or collaborator;
- create a smaller context pack for one architectural question.

Do not infer a contract solely from a box or arrow. The accompanying documents define the intended behavior and open questions.

## 2. Whole-system diagrams

### 2.1 Joint cognitive system

![Joint cognitive system](diagrams/01_joint_cognitive_system.svg)

**File:** `diagrams/01_joint_cognitive_system.svg`  
**Editable source:** `diagrams/01_joint_cognitive_system.dot`

Shows the second-generation joint cognitive operating model: purpose, cognitive control, knowledge, governance, and adaptation planes connected through an explicit `attend → sense → frame → generate → challenge → decide → act → verify` loop. Jonathan, AI collaborators, other people, artifacts, and tools participate across the planes rather than serving as the architecture themselves.

**Questions to ask:**

- What protects values, goals, and commitments from silent plan or priority drift?
- Why is an item inside the active frame, deferred, or allowed to interrupt?
- Which epistemic transition converted an observation or interpretation into an accepted working belief?
- Do collaborators share the same objective and source set, or merely appear to agree?
- Which observation verifies the intended real-world outcome after execution?
- How do incidents change methods, policies, calibration, or cognitive-immune responses?
- What becomes forbidden when a model, connector, context source, or human reviewer is degraded?

### 2.2 Product kernel

![Product kernel](diagrams/02_product_kernel.svg)

Shows the universal kernel, profile/policy, capability packs, adapters, and interfaces.

**Questions:**

- Which concept is truly universal?
- Is a Jonathan-specific rule leaking into the kernel?
- Can a capability pack be removed without corrupting other packs?
- Does a profile configure behavior or fork architecture?

### 2.3 System context

![System context](diagrams/03_system_context.svg)

Shows the responsibilities of Jonathan, Big Brain Time, AI models, external authorities, evidence sources, and recovery systems.

**Questions:**

- Which actor has final authority?
- Which external data should be referenced rather than copied?
- What leaves the local boundary?
- What recovery evidence exists?

### 2.4 Container architecture

![Container architecture](diagrams/04_container_architecture.svg)

Shows delivery interfaces, application orchestration, domain kernel, ports, adapters, and stores.

**Questions:**

- Is business logic leaking into an interface or adapter?
- Can the kernel be tested without Flask, SQLite, or a model?
- Which stores are canonical versus derived?
- What versioned contracts exist at each boundary?

## 3. Authority and subsystem diagrams

### 3.1 Authority and trust planes

![Authority and trust planes](diagrams/05_authority_and_trust_planes.svg)

Separates trusted control, untrusted evidence, canonical authorities, and disposable derived representations.

**Questions:**

- Can evidence influence action without a policy decision?
- Is a generated artifact being treated as authority?
- Does every write identify the active system of record?
- Can derived state be deleted safely?

### 3.2 Subsystem landscape

![Subsystem landscape](diagrams/06_subsystem_landscape.svg)

Shows cognitive, operational, and governance services over shared foundations.

**Questions:**

- Which subsystem owns each rule?
- Which seams carry the most trust risk?
- Which modules could be capability packs rather than core?
- Which foundation is duplicated today?

## 4. Cognitive and memory flows

### 4.1 Capture-to-memory pipeline

![Capture pipeline](diagrams/07_capture_to_memory.svg)

Shows preservation before triage and extraction, ephemeral staging, review, canonical acceptance, and projection rebuild.

**Use for:** voice capture, conversation ingestion, source imports, privacy review.

**Questions:**

- What is captured synchronously?
- What can remain source-only?
- When does extraction become authoritative?
- How does a capture expire or get discarded?

### 4.2 Trusted answer pipeline

![Trusted answer pipeline](diagrams/08_trusted_answer_pipeline.svg)

Shows query planning, retrieval, temporal/authority resolution, conflict scanning, context contracts, synthesis, and claim verification.

**Questions:**

- Where is abstention selected?
- What intermediate artifact explains a failure?
- Are authority and privacy applied before retrieval expansion?
- Can the user inspect omissions?

### 4.3 Conservative memory consolidation

![Memory consolidation](diagrams/09_memory_consolidation.svg)

Shows episodes, clusters, deduplication, alternatives, purpose-bound abstraction, retention tests, and consolidated semantic memory.

**Questions:**

- What purpose justifies consolidation?
- Which exceptions must survive?
- How is the summary invalidated?
- Does the result create new propositions?

### 4.4 Continuity and re-entry loop

![Re-entry loop](diagrams/10_reentry_loop.svg)

Shows work, interruption, transition capsule, elapsed change, re-entry compilation, first action, and protocol reflection.

**Questions:**

- What information exists only in the worker’s head at stop time?
- Which fields predict resumption?
- What changed while away?
- How is a wrong first action detected?

### 4.5 Epistemic object model

![Epistemic object model](diagrams/17_epistemic_object_model.svg)

Shows memory item, source/activity, stance, perspective, optional proposition, resolution, and relations.

**Questions:**

- Is this object truth-apt?
- Whose stance is represented?
- Is the source perceived, remembered, reported, inferred, or generated?
- Does it need a proposition now, later, or never?

### 4.6 Multi-resolution memory

![Multi-resolution memory](diagrams/18_multi_resolution_memory.svg)

Shows originals, addressable records, evidence relations, reflections, views, and commitments/actions.

**Questions:**

- At which layer is this artifact authoritative?
- Can a higher-level view drill down?
- What happens when a lower-level source changes?
- Which layer is being deleted or hidden?

## 5. Change, safety, and lifecycle diagrams

### 5.1 Change propagation

![Change propagation](diagrams/11_change_propagation.svg)

Shows semantic diff, dependency graph, impact set, granular proposals, review, execution, projection invalidation, and audit.

**Questions:**

- Does a dependency mean display, derivation, or semantic reliance?
- What can be invalidated automatically?
- What is the maximum proposal scope?
- How is a false dependency corrected?

### 5.2 Action firewall

![Action firewall](diagrams/12_action_firewall.svg)

Shows typed action graphs, deterministic policy, simulation, confirmation, scoped execution, verification, audit, and denial.

**Questions:**

- Can the user predict the outcome?
- Is the action genuinely reversible?
- What precondition makes the proposal stale?
- Which arguments came from untrusted evidence?

### 5.3 Lifecycle and purge

![Lifecycle and purge](diagrams/13_lifecycle_and_purge.svg)

Shows semantic request, policy classification, representation enumeration, dry run, approval, application, rebuild, verification, and receipt.

**Questions:**

- Is the desired outcome suppression, retraction, redaction, or purge?
- Which backups or external disclosures remain?
- Can audit retain process without payload?
- What proof of absence is actually possible?

## 6. Design and productization diagrams

### 6.1 Design spiral

![Design spiral](diagrams/14_design_spiral.svg)

Shows observation, question framing, research, probe, pilot, measurement, decision, and documentation.

**Use for:** choosing the next work, resisting feature-roadmap inertia.

### 6.2 Productization layers

![Productization layers](diagrams/15_productization_layers.svg)

Shows universal kernel, profile, capability packs, workflow compositions, interfaces, and deployment envelope.

**Questions:**

- Does a pack use stable contracts?
- What personal context may enter a shared workflow?
- Which deployment assumptions change safety?
- Can a capability be installed and removed independently?

### 6.3 Evaluation flywheel

![Evaluation flywheel](diagrams/16_evaluation_flywheel.svg)

Shows baseline, regression cases, prototype, tests, pilot, incidents, maturity gate, and keep/simplify/remove decision.

**Questions:**

- Which evidence supports the current maturity label?
- Has a real incident become a regression case?
- Does the feature improve joint-system outcomes?
- When does evidence expire?

### 6.4 QOC design space

![QOC design space](diagrams/19_qoc_design_space.svg)

Illustrates a design question, alternative authority models, and criteria.

**Use for:** poorly understood or difficult-to-reverse design questions.

### 6.5 Quality-attribute map

![Quality attribute map](diagrams/20_quality_attribute_map.svg)

Shows recurring architectural qualities and selected tensions.

**Use for:** architecture reviews and scenario prioritization.

## 7. Diagram review protocol

For a major design review:

1. Start with system context.
2. Mark canonical, external, derived, and ephemeral stores.
3. Follow one user scenario through the relevant data-flow diagram.
4. Follow one failure or deletion scenario in reverse.
5. Mark every model judgment and deterministic policy.
6. Mark every authority transition.
7. Identify where source, time, privacy, or perspective can be lost.
8. Identify the quality attributes affected.
9. Update the `.dot` source and the written contract together.
10. Record unresolved disagreements rather than drawing an artificial consensus arrow.

## 8. Creating additional diagrams

Use the same numbering and include:

- title;
- purpose;
- boundaries;
- legend if colors or line styles carry meaning;
- editable `.dot` source;
- rendered `.svg`;
- reference from the defining document;
- date or version when the diagram represents a changing architecture.

Suggested future diagrams:

- state machine for commitments and plans;
- bitemporal claim examples;
- context-pack schema map;
- shared/team-brain access and perspective boundaries;
- backup and restore topology;
- model-routing and privacy decision tree;
- capability-pack dependency graph;
- multi-device single-writer lease flow;
- self-model review and expiration flow.
