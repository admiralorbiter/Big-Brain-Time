# Big Brain Time Design Studio — Package Manifest

**Prepared:** 2026-07-27  
**Package purpose:** A durable design-and-research environment for stepping back from the current Big Brain Time proof of concept, examining the whole product and its subsystems, and making evidence-gated product decisions before further implementation.

## Package status

- Structural validation: **PASS**
- Principal design documents: **17** (`README`, documents `00`–`14`, source traceability, and this manifest)
- Combined editions: **2** (Markdown and standalone HTML)
- Diagrams: **20** rendered SVGs plus **20** editable Graphviz DOT sources
- Reusable design templates: **9**
- Preserved source-package files: **17**, plus a source-reference README
- Combined narrative length: approximately **42,071 words**
- Validation errors: **0**
- Validation warnings: **0**

The machine-readable file inventory and SHA-256 hashes are in [`manifest.json`](manifest.json). Structural checks are recorded in [`validation_report.json`](validation_report.json).

## Start here

1. Open [`BIG_BRAIN_TIME_DESIGN_STUDIO.html`](BIG_BRAIN_TIME_DESIGN_STUDIO.html) for the easiest browsable edition.
2. Read [`README.md`](README.md) for the paced reading path and working rules.
3. Read [`00_DESIGN_STUDIO_CHARTER.md`](00_DESIGN_STUDIO_CHARTER.md) and [`01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md`](01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md) before evaluating future architecture.
4. Use [`13_DESIGN_WORKBOOK.md`](13_DESIGN_WORKBOOK.md) to record decisions, tensions, questions, and experiments as the design evolves.
5. Treat the roadmap as an option map rather than an implementation commitment.

## Principal documents

| File | Purpose |
|---|---|
| [`README.md`](README.md) | Orientation, package map, paced reading path, and suggested design-studio cadence. |
| [`00_DESIGN_STUDIO_CHARTER.md`](00_DESIGN_STUDIO_CHARTER.md) | Defines the design phase, its boundaries, outputs, questions, evidence classes, and completion criteria. |
| [`01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md`](01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md) | Separates demonstrated capability, implemented mechanism, architectural aspiration, rough edges, and unverified claims in the current repository. |
| [`02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md`](02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md) | Defines the five-plane joint cognitive operating model, active frame, product thesis, durable kernel, capability model, product boundaries, and alternative product shapes. |
| [`03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md`](03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md) | Describes the closed cognitive control loop, whole-system landscape, authority boundaries, trust planes, verified action lifecycle, degraded modes, modular architecture, and quality attributes. |
| [`04_SUBSYSTEM_ATLAS.md`](04_SUBSYSTEM_ATLAS.md) | Gives a repeatable card for each major subsystem, including attention/coordination: purpose, inputs, outputs, state, invariants, failure modes, dependencies, friction, experiments, and open questions. |
| [`05_COGNITIVE_AND_MEMORY_MODEL.md`](05_COGNITIVE_AND_MEMORY_MODEL.md) | Defines the active cognitive frame, epistemic-state progression, transactive memory, cognitive immune response, plural cognitive objects, perspectives, and human–AI division of labor. |
| [`06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md`](06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md) | Separates indexing, deduplication, summarization, reflection, consolidation, suppression, archive, retraction, deletion, purge, and unlearning. |
| [`07_DESIGN_TENSIONS_AND_OPTION_SPACES.md`](07_DESIGN_TENSIONS_AND_OPTION_SPACES.md) | Preserves major unresolved architectural choices as explicit Question–Option–Criteria design spaces rather than premature decisions. |
| [`08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md`](08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md) | Organizes completed research, current evidence, targeted research threads, research packets, and evidence-to-decision traceability. |
| [`09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md`](09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md) | Provides the design-science, risk-driven, option-preserving, quality-attribute, and experiment-based method for turning ideas into governed product decisions. |
| [`10_GENERALIZATION_AND_PRODUCTIZATION.md`](10_GENERALIZATION_AND_PRODUCTIZATION.md) | Explores how the personal proof of concept could generalize into project brains, research workbenches, assurance tools, personal platforms, or collaborative systems. |
| [`11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md`](11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md) | Defines small probes for semantic foundations, retrieval, synthesis, re-entry, lifecycle, permissions, usability, and product value, with decision gates and stop rules. |
| [`12_DIAGRAM_ATLAS.md`](12_DIAGRAM_ATLAS.md) | Indexes and explains all twenty system and subsystem diagrams. |
| [`13_DESIGN_WORKBOOK.md`](13_DESIGN_WORKBOOK.md) | A working notebook for session-by-session reflection, product choices, tensions, risks, research pulls, and experiment outcomes. |
| [`14_GLOSSARY.md`](14_GLOSSARY.md) | Stabilizes important cognitive, epistemic, architectural, lifecycle, evaluation, and product terms. |
| [`SOURCES_AND_TRACEABILITY.md`](SOURCES_AND_TRACEABILITY.md) | Distinguishes source-derived material, repository observations, external research, and new proposals; maps the new package back to the supplied blueprint. |

## Combined editions

- [`BIG_BRAIN_TIME_DESIGN_STUDIO.md`](BIG_BRAIN_TIME_DESIGN_STUDIO.md) — one searchable Markdown document containing the complete design studio.
- [`BIG_BRAIN_TIME_DESIGN_STUDIO.html`](BIG_BRAIN_TIME_DESIGN_STUDIO.html) — a standalone styled HTML edition with embedded navigation and rendered diagrams.

## Diagram library

The [`diagrams/`](diagrams/) directory contains editable `.dot` sources and rendered `.svg` outputs for:

1. Joint cognitive system
2. Product kernel
3. System context
4. Container architecture
5. Authority and trust planes
6. Subsystem landscape
7. Capture-to-memory flow
8. Trusted-answer pipeline
9. Memory consolidation
10. Re-entry loop
11. Change propagation
12. Action firewall
13. Lifecycle and purge
14. Design spiral
15. Productization layers
16. Evaluation flywheel
17. Epistemic object model
18. Multi-resolution memory
19. QOC design space
20. Quality-attribute map

Use [`12_DIAGRAM_ATLAS.md`](12_DIAGRAM_ATLAS.md) to read the diagrams in sequence and understand what each one intentionally includes or omits.

## Reusable templates

The [`templates/`](templates/) directory contains:

- `CONTEXT_CONTRACT.md`
- `DECISION_PACKET.md`
- `DESIGN_QUESTION_PACKET.md`
- `EXPERIMENT_CARD.md`
- `FRICTION_RECORD.md`
- `LIFECYCLE_IMPACT_PACKET.md`
- `QUALITY_ATTRIBUTE_SCENARIO.md`
- `RESEARCH_BRIEF.md`
- `SUBSYSTEM_CARD.md`

These are intended to become the stable working language of the design phase. They are deliberately provider-neutral and implementation-neutral.

## Preserved source material

The [`reference/source-blueprint/`](reference/source-blueprint/) directory contains exact copies of the uploaded planning and architecture documents used as the package’s local source basis. The reference README records filename/title differences and source-copy handling.

The new design-studio package does not silently replace or reconcile those documents. It treats them as a preserved prior design layer and distinguishes:

- statements directly supported by the supplied documents;
- observations from the current repository review;
- external research constraints;
- new design proposals and hypotheses;
- unresolved questions that require experiments or user decisions.

## Validation performed

The package was checked for:

- required-file presence;
- UTF-8-readable Markdown;
- balanced Markdown code fences;
- resolution of relative links in the new documentation;
- XML parsing of all rendered SVG diagrams;
- complete diagram-atlas coverage;
- presence of all reusable templates;
- SHA-256 identity of all seventeen preserved uploaded source files;
- successful generation of the combined Markdown and standalone HTML editions.

See [`validation_report.json`](validation_report.json) for the machine-readable result.

## Recommended first design session

Read the charter and current-product review, then write three lists in the workbook:

1. **Keep:** mechanisms or principles that have already demonstrated value.
2. **Question:** mechanisms that may be useful but need a sharper model or experiment.
3. **Retire or simplify:** mechanisms whose complexity currently exceeds their demonstrated value.

Do not begin by choosing a final architecture. Begin by deciding what the current proof of concept has actually taught you.
