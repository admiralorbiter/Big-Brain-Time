# Sources and Traceability

## 1. Scope and research cutoff

**Package prepared:** 2026-07-27  
**Current-repository review:** static inspection of `admiralorbiter/bigbraintime` on 2026-07-27  
**External research review:** sources available through 2026-07-27

This package distinguishes four evidence layers:

1. **Current repository evidence** — live files, implementation, project history, and repository-reported tests.
2. **Supplied source package** — the uploaded Big Brain Time blueprint, charter, ADRs, roadmap, risk register, bibliography, and worksheets.
3. **External research and standards** — primary research, standards, and official technical documentation.
4. **New design proposals** — interpretations and recommendations introduced by the design studio.

The package does not claim that external research proves the proposed product architecture. Research is used to reveal distinctions, constraints, likely failure modes, and experiment designs.

## 2. Evidence labels used in the documents

- **`[CURRENT]`** — observed in the current repository or current project documentation.
- **`[SOURCE]`** — directly supported by the supplied Big Brain Time materials.
- **`[RESEARCH]`** — supported by external primary research, standards, or official documentation.
- **`[PROPOSAL]`** — a design recommendation introduced in the studio.
- **`[QUESTION]`** — unresolved.
- **`[EXPERIMENT]`** — proposed local evidence collection.
- **`[INFERENCE]`** — reasoned combination of evidence and design judgment.

A clear proposal is still a proposal.

## 3. Preserved supplied source package

Exact copies of the uploaded materials are preserved under `reference/source-blueprint/`.

Some uploaded filenames differ from the title inside the file. The table records both.

| Uploaded filename | Internal title / role |
|---|---|
| `00_EXECUTIVE_BLUEPRINT.md` | Repository audit and planning transcript; original problem evidence and research questions |
| `00_SPRINT_0_CHARTER.md` | Sprint 0 Program Charter, scope boundaries, initial defect fixtures |
| `01_RESEARCH_SYNTHESIS(1).md` | `00 — Executive Blueprint`; north star, capability tests, horizons, architecture laws |
| `02_TARGET_ARCHITECTURE.md` | `01 — Research Synthesis and Design Implications` |
| `03_DOMAIN_AND_DATA_MODEL(1).md` | `02 — Target Architecture` |
| `04_RETRIEVAL_CONTEXT_AND_MEMORY.md` | `03 — Domain and Data Model` |
| `05_SAFETY_PERMISSIONS_AND_THREAT_MODEL.md` | `04 — Retrieval, Context, and Long-Term Memory` |
| `06_ROADMAP_MILESTONES_AND_SPRINTS(1).md` | `05 — Safety, Permissions, and Threat Model` |
| `07_EVALUATION_AND_EXPERIMENTS.md` | `06 — Roadmap, Milestones, Tasks, and Sprints` |
| `08_ARCHITECTURE_DECISION_PROPOSALS.md` | `07 — Evaluation and Experiments` |
| `09_RESEARCH_BIBLIOGRAPHY(1).md` | `08 — Architecture Decision Proposals` |
| `10_DISCOVERY_AND_REQUIREMENTS_WORKSHEET(1).md` | `09 — Research Bibliography and Evidence Map` |
| `11_RISK_REGISTER(1).md` | `10 — Discovery and Requirements Worksheet` |
| `ARCHITECTURE_DECISION_RECORDS.md` | Locked ADRs for epistemic, retrieval, watcher, audit, handoff, and reconciliation design |
| `ARTIFACT_MANIFEST(1).md` | `11 — Risk Register` |
| `BIG_BRAIN_TIME_SYSTEM_BLUEPRINT(1).md` | Artifact Manifest for the earlier package |
| `README(3).md` | Product Backlog — 24 sprints / 120 tasks |

Because of these filename/title mismatches, this studio normally cites the internal document title and section rather than assuming the filename number is semantically correct.

## 4. Load-bearing source-derived ideas

The following ideas came from the supplied package and are preserved rather than silently replaced:

### Product and mission

- accurate resumption without rereading the corpus;
- contradiction and propagation detection;
- local-first, source-grounded, temporal capability platform;
- the “knowledge compiler” framing;
- joint human–AI capability rather than feature count.

### Architecture

- local-first modular monolith;
- ports and adapters;
- Markdown/Git narrative authority;
- disposable SQLite read model;
- selected operational SQLite aggregates only after gates;
- external systems remain authoritative in their domains;
- interfaces share domain services;
- evidence/control plane separation;
- deterministic behavior before model synthesis;
- one active writer per information type.

### Memory and retrieval

- explicit provenance and valid/recorded time;
- context-pack manifests;
- local versus global query strategies;
- contradiction disclosure and abstention;
- memory summaries as derived caches;
- managed forgetting as visibility control;
- Ready-to-Resume transitions.

### Safety and governance

- graduated initiative;
- permission and risk tiers;
- read → propose → review → write;
- human control of consequential action;
- recovery, export, and rollback as acceptance criteria;
- shadow mode before proactive behavior;
- model independence.

### Evaluation

- capability and coordination measures;
- baseline before optimization;
- explicit stop rules;
- prototype/tested/benchmarked/piloted/trusted/authorized distinctions;
- keep/simplify/remove decisions.

## 5. Current repository review basis

The design studio’s `01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md` also draws on a static review of the current repository, including:

- `README.md` and project state;
- `AGENTS.md`;
- current CLI and module structure;
- synthesis harvester/engine;
- reconciliation models, candidate retrieval, adjudicator, graph, and tests;
- patch applicator and undo;
- audit schema/writer;
- handoff compiler;
- SQLite importer and models;
- context compiler;
- recent commit history.

Important limitation: the studio did not independently execute the repository test suite. Repository-reported test counts are therefore treated as implementation claims that should be bound to run artifacts in a future self-audit.

## 6. Traceability from studio documents

| Studio document | Primary supplied basis | Additional research/proposal introduced |
|---|---|---|
| `00_DESIGN_STUDIO_CHARTER.md` | source roadmap rules, evaluation gates, risk register | DSRM, Spiral, QOC, ATAM; design-mode governance |
| `01_CURRENT_PRODUCT_AND_PROOF_OF_CONCEPT.md` | source blueprint and live repo | conservative maturity map and freeze strategy |
| `02_PRODUCT_THESIS_AND_CAPABILITY_MODEL.md` | executive blueprint, jobs and horizons | five-plane joint cognitive operating model, active frame, product kernel, project/personal/shared scales |
| `03_SYSTEM_LANDSCAPE_AND_ARCHITECTURE.md` | target architecture, authority matrix, safety | closed cognitive control loop, verified action lifecycle, degraded modes, federated project-brain alternative, and fitness functions |
| `04_SUBSYSTEM_ATLAS.md` | all architecture and domain documents | attention/coordination subsystem, responsibility cards, subsystem probes, seam map |
| `05_COGNITIVE_AND_MEMORY_MODEL.md` | epistemic markers, temporal truth, joint system | active frame, epistemic-state progression, transactive memory, cognitive immune response, plural object model, source mode, stance, perspective, cognitive modes |
| `06_SYNTHESIS_CONSOLIDATION_AND_FORGETTING.md` | context contracts, summaries-as-caches, managed forgetting | information-bottleneck framing, synthesis contract, purge transaction |
| `07_DESIGN_TENSIONS_AND_OPTION_SPACES.md` | ADRs, risks, architecture alternatives | QOC option maps and additional macro alternatives |
| `08_RESEARCH_AGENDA_AND_EVIDENCE_MAP.md` | supplied bibliography and research gaps | 2025–2026 memory benchmarks and prioritized local probes |
| `09_PRODUCT_DESIGN_METHOD_AND_GOVERNANCE.md` | roadmap gates and evaluation process | evolvable method/policy jurisprudence, collaborator context, four backlogs, risk-driven studio workflow, decision packets |
| `10_GENERALIZATION_AND_PRODUCTIZATION.md` | capability-platform horizon | active-frame, health, verification, and kernel/profile/pack productization model |
| `11_EXPERIMENT_PORTFOLIO_AND_DECISION_GATES.md` | existing ten experiments and scorecard | semantic-foundation and productization experiments |
| `12_DIAGRAM_ATLAS.md` | supplied Mermaid diagrams | rendered cross-level architecture and cognitive diagrams |
| `13_DESIGN_WORKBOOK.md` | discovery worksheet and roadmap | paced studio exercises |
| `14_GLOSSARY.md` | existing terminology | reconciled vocabulary for plural cognition and product design |

## 7. Foundational external research and standards

### Human memory, cognition, and augmentation

| Source | Status | Design use |
|---|---|---|
| Conway, M. A., & Pleydell-Pearce, C. W. (2000). *The construction of autobiographical memories in the self-memory system*. | Peer-reviewed | Memories as constructed in relation to autobiographical knowledge and current goals; supports perspective/purpose-aware retrieval. |
| Johnson, M. K., Hashtroudi, S., & Lindsay, D. S. (1993). *Source monitoring*. | Peer-reviewed review | Distinguishes perceived, remembered, imagined, and reported sources; motivates source mode. |
| McClelland, J. L., McNaughton, B. L., & O’Reilly, R. C. (1995). *Why there are complementary learning systems in the hippocampus and neocortex*. | Peer-reviewed | Fast episodic capture versus slower semantic integration. |
| Schacter, D. L., Addis, D. R., & Buckner, R. L. (2007). Constructive episodic simulation work. | Peer-reviewed | Memory supports future simulation; motivates explicit scenario objects. |
| Risko, E. F., & Gilbert, S. J. (2016). *Cognitive Offloading*. | Peer-reviewed review | External tools can redistribute cognitive work; motivates measuring skill and dependence. |
| Licklider (1960), Engelbart (1962), Hutchins (1995). | Foundational | Human–computer symbiosis, augmentation, and distributed cognition. |
| Gonzalez, C., et al. (2026). *Toward a science of human–AI teaming for decision making: A complementarity framework*. PNAS Nexus. DOI: 10.1093/pnasnexus/pgag030. | Peer-reviewed | Treats reasoning, memory, and attention as foundational functions joined by meta-coordination; motivates the active frame and role-aware control loop. |
| Wegner, D. M., Erber, R., & Raymond, P. (1991). *Transactive Memory in Close Relationships*. | Peer-reviewed | Collective memory includes knowledge of who knows what; motivates capability/context registries and cautions against imposed role structures. |
| Sperber, D., et al. (2010). *Epistemic Vigilance*. | Peer-reviewed review | Communication creates exposure to accidental and intentional misinformation; motivates source, context, plausibility, corroboration, and cognitive-immune responses. |
| Horvitz, E. (1999). *Principles of Mixed-Initiative User Interfaces* and *Mixed-Initiative Interaction*. | Peer-reviewed conference/journal | Initiative depends on uncertainty, timing, value, and user control; motivates interruption thresholds, deferral, and role negotiation. |
| Woods, D. D. (2018). *The Theory of Graceful Extensibility*. | Peer-reviewed | Sustained adaptability requires extending adaptive capacity under surprise; motivates visible degraded modes and recovery paths. |
| Leroy & Glomb (2018); Masicampo & Baumeister (2011). | Peer-reviewed | Ready-to-resume and prospective closure. |
| Jilek et al. (2019; 2026). Managed forgetting. | Peer-reviewed/book chapter | Buoyancy, reversible suppression, preservation value. |

### Formal knowledge, belief revision, and action

| Source | Status | Design use |
|---|---|---|
| Doyle, J. (1979). *A Truth Maintenance System*. | Peer-reviewed/classic | Preserve justifications and revise dependent conclusions. |
| de Kleer, J. (1986). *An Assumption-Based TMS*. | Peer-reviewed | Multiple inconsistent assumption environments and alternatives. |
| Dung, P. M. (1995). Argumentation framework. | Peer-reviewed | Arguments, attacks, and multiple acceptable positions. |
| Rao, A. S., & Georgeff, M. P. (1995). *BDI Agents: From Theory to Practice*. | Conference paper | Separate beliefs, desires, and intentions. |
| Tishby, N., Pereira, F. C., & Bialek, W. (2000). *The Information Bottleneck Method*. | Primary paper/preprint | Compression is relative to a relevance objective. |
| W3C PROV Overview / PROV-DM. | W3C standard | Agents, entities, activities, derivation, attribution. |
| Snodgrass (1999). Temporal database applications. | Foundational book | Valid time, transaction/recorded time, bitemporal queries. |
| RFC 5545 iCalendar. | IETF standard | Recurrence and exception semantics. |

### Product, architecture, and design method

| Source | Status | Design use |
|---|---|---|
| Kleppmann et al. (2019). *Local-First Software*. | Peer-reviewed/conference essay | Ownership, offline capability, longevity, privacy, multi-device ideals. |
| Fowler. *Strangler Fig Application* and *Patterns of Legacy Displacement*. | Practitioner primary source | Incremental migration and seams rather than big-bang rewrite. |
| Peffers et al. (2007). DSRM. | Peer-reviewed | Problem → objective → artifact → demonstration → evaluation → communication. |
| Boehm (1988). Spiral Model. | Peer-reviewed/classic | Risk-driven iteration. |
| MacLean et al. (1991). QOC. | Peer-reviewed | Questions, options, criteria, and preserved design rationale. |
| Kazman et al. (1998). ATAM. | SEI technical report | Quality-attribute scenarios and architecture tradeoffs. |
| Flask application factory documentation. | Official documentation | Thin, testable interfaces and modular app construction. |
| SQLite FTS5, backup API, `VACUUM INTO`, STRICT tables. | Official documentation | Local search, recovery, and constrained data model. |

### Retrieval, context, and safety

| Source | Status | Design use |
|---|---|---|
| Lost in the Middle | Peer-reviewed/preprint lineage | Long context position effects. |
| RULER | Research benchmark | Effective context under multi-hop/aggregation. |
| NoLiMa | Research benchmark | Low lexical overlap and semantic bridging. |
| LongMemEval | Research benchmark | Multi-session extraction, temporal updates, abstention. |
| GraphRAG research and documentation | Research/official project | Separate local retrieval from global sensemaking. |
| RAGAS and ARES | Research frameworks | Separate context, faithfulness, and answer relevance. |
| Greshake et al. (2023). Indirect prompt injection. | Primary security research | Evidence/control separation and least privilege. |
| NIST AI RMF 1.0 Core and NIST AI 600-1 | Official guidance | Human oversight, lifecycle monitoring, independent evaluation, incident response, recovery, change management, and safe decommissioning. |
| OWASP prompt-injection and agent-security guidance | Official community guidance | Privilege, output validation, monitoring, and human approval. |

## 8. Emerging 2025–2026 agent-memory evidence

These sources are recent and should be treated as **research directions and benchmark ideas**, not settled architecture laws.

| Source | Date/status | Main relevance |
|---|---|---|
| [MemoryAgentBench](https://arxiv.org/abs/2507.05257) | 2025 preprint | Evaluates accurate retrieval, test-time learning, long-range understanding, and selective forgetting; current systems do not master all. |
| [Human-Inspired Memory Architecture for LLM Agents](https://www.microsoft.com/en-us/research/publication/human-inspired-memory-architecture-for-llm-agents/) | May 2026 preprint/MSR | Consolidation, interference-based forgetting, maturation, reconsolidation, graphs, multi-cue retrieval; useful mechanisms and tradeoff curves. |
| [MemEvoBench](https://arxiv.org/abs/2604.15774) | April 2026 preprint | Long-horizon memory safety under adversarial injection, noisy tools, and biased feedback. |
| [RHELM](https://www.microsoft.com/en-us/research/publication/beyond-static-dialogues-benchmarking-realistic-heterogeneous-and-evolving-long-term-memory/) | May 2026 preprint/MSR | Heterogeneous, evolving, multi-source memory and contextual reasoning. |
| [Toward Human-AI Complementarity Across Diverse Tasks](https://arxiv.org/abs/2605.04070) | May 2026 preprint | Confidence-based routing does not reliably identify AI errors; motivates richer allocation of scarce human attention and independent evaluation. |
| GroupMemBench | May 2026 preprint/MSR | Speaker-grounded memory, multi-party beliefs, and audience-sensitive language. |
| A-MEM | 2025 preprint | Dynamic note linking and memory evolution inspired by Zettelkasten. |
| Recent memory-to-action and interdependent-session benchmarks | 2026 emerging | Evaluate whether stored memory supports coherent tool use and continued tasks, not only recall. |

### Local use of emerging evidence

- expand evaluation families;
- create adversarial memory-update tests;
- compare simple and complex memory systems;
- test streaming and multi-source change;
- avoid static “memory retrieval accuracy” as the only score;
- do not import biologically named mechanisms without a local design question.

## 9. Research gaps that remain genuinely open for Big Brain Time

1. Low-maintenance plural epistemic modeling for ordinary personal use.
2. Purpose-specific synthesis evaluation without extensive manual annotation.
3. Longitudinal field evidence for one person and AI co-adapting over years.
4. Personal-memory deletion across Git, summaries, prompts, and backups.
5. Speaker- and audience-grounded memory in a shared project brain.
6. Measurement of cognitive offloading that preserves learning and judgment.
7. User-legible authority and temporal policies.
8. Nonintrusive proactive negotiation of priorities.
9. Portable local-first productization for nontechnical users.
10. How to distinguish valuable semantic consolidation from invasive profiling.

## 10. Claim promotion rules

A research-derived idea may become an accepted Big Brain Time decision only when:

- the source claim is accurately represented;
- relevant boundaries and contrary evidence are recorded;
- the product inference is explicit;
- a current capability scenario requires the decision;
- at least one alternative is considered;
- local evidence or a strong safety rationale supports the choice;
- reconsideration conditions are named.

A recent benchmark result alone does not promote an architecture.

## 11. Citation practice for future documents

For load-bearing research claims, record:

```yaml
citation_key:
full_citation:
url_or_doi:
publication_date:
accessed_at:
status: peer_reviewed | preprint | standard | official_docs | practitioner
exact_supported_claim:
boundary_conditions:
design_interpretation:
decisions_influenced:
reconsider_if:
```

Quote sparingly. Prefer an accurate paraphrase and location/DOI.

## 12. Provenance of the diagrams

All diagrams in `diagrams/` were created for this design studio from the combined current-system review, supplied blueprint, and new proposals. They are not copied figures from external publications.

Each `.svg` is generated from the adjacent `.dot` source. The diagrams are proposal views and should be versioned with the written model.
