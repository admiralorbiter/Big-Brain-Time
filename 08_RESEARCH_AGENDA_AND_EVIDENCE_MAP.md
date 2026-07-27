# 08 — Research Agenda and Evidence Map

## 1. Research posture

Research should help Big Brain Time make better design choices, not provide intellectual decoration or justify a preferred architecture after the fact.

For each thread, distinguish:

1. **Phenomenon:** what human, organizational, or technical behavior is being studied?
2. **Finding:** what does the source actually support?
3. **Boundary:** under what conditions was it observed?
4. **Design implication:** what constraint or option does it suggest?
5. **Product hypothesis:** what might be useful in Big Brain Time?
6. **Probe:** what local evidence could confirm or reject that hypothesis?

A primary paper, standard, or official technical source is preferred. Recent preprints are useful for mechanisms and benchmark ideas but receive lower design authority until replicated or locally demonstrated.

## 2. Priority model

Score research questions by:

```text
expected decision impact
× uncertainty reduced
× number of dependent design choices
× safety or privacy significance
÷ research and evaluation cost
```

The first priority is not the most novel topic. It is the question most likely to change a material product choice.

## 3. Research Thread A — Autobiographical memory and the changing self

### Central question

How should a personal system preserve experiences and self-understanding when autobiographical memory is constructive, purpose-sensitive, and connected to current goals?

### Why it matters

A secondary brain can become harmful if it treats past descriptions as immutable identity facts or “corrects” personal memory solely from external records.

### Evidence base

- Conway & Pleydell-Pearce’s self-memory system;
- autobiographical memory and working-self research;
- narrative identity and memory reconsolidation literature;
- source monitoring.

### Design implications to investigate

- retrieve an original artifact and a current reconstruction separately;
- represent “Jonathan then” and “Jonathan now” as perspectives;
- time-bound personal interpretations and preferences;
- retain authentic voice while allowing concise current views;
- show when later knowledge influenced a reconstruction.

### Research questions

1. Which autobiographical structures are useful without becoming invasive?
2. How does cue and current goal change a useful retrieval?
3. How can the system support narrative identity without fixing it?
4. What should be immutable: source artifact, memory claim, or neither?
5. What consent is required when memories include other people?

### Local probe

Select five journal or project episodes that Jonathan now interprets differently. Create source view, historical perspective, current perspective, and factual record view.

### Caution

Human-memory theories are explanatory frameworks, not direct software specifications.

### Starting sources

- [Conway & Pleydell-Pearce, 2000](https://pubmed.ncbi.nlm.nih.gov/10789197/)
- [Johnson, Hashtroudi, & Lindsay, 1993](https://pubmed.ncbi.nlm.nih.gov/8346328/)

---

## 4. Research Thread B — Episodic, semantic, and procedural consolidation

### Central question

How should Big Brain Time learn general patterns from experiences without allowing one event or one generated summary to rewrite durable understanding?

### Why it matters

This is the foundation for synthesis, personalization, learned procedures, and long-term memory growth.

### Evidence base

- Complementary Learning Systems;
- systems consolidation and gist/detail tradeoffs;
- memory reconsolidation;
- emerging agent-memory consolidation research.

### Design implications to investigate

- fast episode storage, slow generalization;
- replay/interleaving across diverse episodes;
- source diversity and exception preservation;
- separate procedural memory from semantic facts;
- review and regression before promoting a heuristic.

### Research questions

1. What triggers consolidation: time, use, diversity, or task need?
2. How are outliers preserved?
3. Should procedures mature through successful executions?
4. When should a generalization decay or be reopened?
5. How is reconsolidation represented without rewriting history?

### Local probe

Take one recurring workflow with six episodes. Build a proposed procedure after episode one and after all six. Compare errors and exceptions.

### Starting sources

- [McClelland, McNaughton, & O’Reilly, 1995](https://pubmed.ncbi.nlm.nih.gov/7624455/)
- [Human-Inspired Memory Architecture for LLM Agents, 2026](https://www.microsoft.com/en-us/research/publication/human-inspired-memory-architecture-for-llm-agents/)

---

## 5. Research Thread C — Source monitoring, provenance, and temporal truth

### Central question

How can the system distinguish what happened, what was perceived, what was remembered, what was reported, what was inferred, and what was generated—across valid and recorded time?

### Why it matters

Most trust failures in a longitudinal AI system are source/time failures before they are language-generation failures.

### Evidence base

- source-monitoring psychology;
- W3C PROV concepts;
- bitemporal database research;
- archival provenance and event sourcing practices.

### Design implications to investigate

- source mode and agent attribution;
- valid time versus recorded time;
- transformation activity and software version;
- current-state selection policies;
- explicit observability gaps;
- provenance display through progressive disclosure.

### Research questions

1. What provenance is useful to users versus only auditors?
2. How is approximate or uncertain time represented?
3. What authority rules should choose, show both, or abstain?
4. How should a generated summary inherit source lineage?
5. How can rebuild metadata avoid changing epistemic time?

### Local probe

Build a five-case temporal/provenance fixture from real repository history and hand-check current, historical, and source-specific answers.

### Starting sources

- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/)
- Snodgrass, *Developing Time-Oriented Database Applications in SQL*
- existing Big Brain Time bibliography R09, R33, R34.

---

## 6. Research Thread D — Belief revision, assumption environments, and argumentation

### Central question

How should Big Brain Time preserve alternatives, revise dependent conclusions, and explain disagreement without pretending that every conflict has one immediate winner?

### Why it matters

Architecture, research, personal interpretation, and group decisions frequently contain assumptions and competing arguments rather than isolated factual claims.

### Evidence base

- Truth Maintenance Systems;
- Assumption-Based TMS;
- nonmonotonic reasoning;
- Dung-style argumentation;
- design rationale and QOC.

### Design implications to investigate

- assumption environments for scenarios and architecture options;
- justifications for derived conclusions;
- argument, premise, conclusion, attack, and undercut relations;
- accepted-under-policy rather than universally true;
- dependency invalidation after assumption change.

### Research questions

1. Which reasoning structures are understandable and maintainable?
2. When is an argument graph worth the cost?
3. How are factual contradiction and value disagreement distinguished?
4. Can QOC and argumentation share a common design-rationale model?
5. How does an AI explain why a conclusion changed after one premise was withdrawn?

### Local probe

Model one contested architecture decision using flat claims, an ATMS-like assumption environment, and QOC/argument structure. Compare explanation and change impact.

### Starting sources

- Doyle, “A Truth Maintenance System”
- [de Kleer, “An Assumption-Based TMS”](https://www.sciencedirect.com/science/article/abs/pii/0004370286900809)
- Dung, 1995
- [MacLean et al., 1991](https://www.tandfonline.com/doi/abs/10.1080/07370024.1991.9667168)

---

## 7. Research Thread E — Long-term agent memory and memory safety

### Central question

Which competencies and failure modes should be used to evaluate a persistent AI memory system?

### Why it matters

Static retrieval accuracy is not enough. A useful memory system must update, understand long-range interactions, forget selectively, apply memory to action, and resist gradual contamination.

### Evidence base

- LongMemEval;
- MemoryAgentBench;
- RHELM;
- MemEvoBench;
- multi-session agent memory and action benchmarks;
- emerging memory architectures.

### Competencies to separate

- accurate retrieval;
- temporal update and supersession;
- test-time learning;
- long-range and multi-session understanding;
- selective forgetting;
- speaker and perspective grounding;
- multi-source aggregation;
- memory-to-action transfer;
- resistance to misleading repetition, noisy tools, and biased feedback.

### Research questions

1. Which benchmark families map to Jonathan’s real use?
2. How should incremental memory updates be evaluated?
3. What safety tests detect memory contamination?
4. Can simple lexical or structured baselines outperform complex memory agents?
5. How should memory repair be triggered by downstream failures?

### Local probe

Create a streaming benchmark of twenty interactions where facts, preferences, decisions, and sources change. Include misleading repetitions and tool noise.

### Starting sources

- [LongMemEval](https://arxiv.org/abs/2410.10813)
- [MemoryAgentBench](https://arxiv.org/abs/2507.05257)
- [MemEvoBench](https://arxiv.org/abs/2604.15774)
- [RHELM](https://www.microsoft.com/en-us/research/publication/beyond-static-dialogues-benchmarking-realistic-heterogeneous-and-evolving-long-term-memory/)

### Caution

These benchmarks are new and often preprint-stage. Use them to broaden evaluation, not to select an architecture by leaderboard.

---

## 8. Research Thread F — Purpose-bound compression and information loss

### Central question

How can the system reduce information while preserving the capability needed for a declared task?

### Why it matters

Synthesis and context compression are central to scale, but they can create false coherence, hidden omissions, and stale authority.

### Evidence base

- Information Bottleneck;
- summarization content-unit and pyramid evaluation;
- hierarchical retrieval such as RAPTOR and GraphRAG;
- cognitive gist/detail research;
- memory consolidation.

### Design implications to investigate

- relevance variable or purpose contract;
- protected information units;
- extractive before abstractive stages;
- alternative and conflict preservation;
- source lineage and invalidation;
- task-performance evaluation after compression.

### Research questions

1. How are protected units selected cheaply?
2. Which summary levels should be stored?
3. What loss should be shown to users?
4. How can summary parents be invalidated after child change?
5. Can a summary be evaluated by future question performance?

### Local probe

Use one source set to produce re-entry, decision, research, and public-sharing syntheses. Compare protected units and omissions.

### Starting sources

- [Tishby et al., 2000](https://arxiv.org/abs/physics/0004057)
- Nenkova & Passonneau, Pyramid Method
- RAPTOR and GraphRAG research in the existing bibliography.

---

## 9. Research Thread G — Retrieval, local/global sensemaking, and context construction

### Central question

What retrieval architecture works for exact, temporal, multi-hop, global, and low-overlap questions at different corpus sizes?

### Why it matters

A long context window is not a reliable substitute for memory. Retrieval failure can produce confident synthesis failure.

### Evidence base

- Lost in the Middle;
- RULER;
- NoLiMa;
- LongMemEval;
- RAG and RAG evaluation;
- GraphRAG/global query research;
- FTS5 official behavior.

### Research questions

1. Which query taxonomy best matches use?
2. What is the tuned lexical/metadata/link baseline?
3. Which low-overlap cases justify embeddings?
4. How should global synthesis be evaluated?
5. When should narrative parent context be retrieved?
6. What retrieval explanations help correction?

### Local probe

Maintain an evolving real-question set and benchmark exact/FTS, metadata, links, embeddings, and hierarchy at 100, 1,000, and simulated 10,000 documents.

### Starting sources

Use R04, R11–R16, R31–R32 in the supplied bibliography.

---

## 10. Research Thread H — Prospective memory, interruption, and cognitive offloading

### Central question

How can Big Brain Time help remember and resume intentions without weakening judgment, skill, or attention?

### Why it matters

Re-entry is the product’s strongest practical wedge, and prospective memory connects stored context to future action.

### Evidence base

- attention residue and ready-to-resume plans;
- implementation intentions and prospective closure;
- cognitive offloading;
- interruption and notification research;
- personal information management.

### Research questions

1. Which transition fields produce actual resumption gains?
2. What closeout cost is acceptable?
3. When should a reminder be time-, event-, state-, or context-triggered?
4. Which knowledge should remain internal to preserve learning and judgment?
5. How does the system distinguish useful preparation from interruption?

### Local probe

Run a within-person interrupted-work study comparing no capsule, manual capsule, and system-assisted capsule.

### Starting sources

Use R23–R26 in the supplied bibliography.

---

## 11. Research Thread I — Distributed cognition and longitudinal co-adaptation

### Central question

How does the whole human–AI-artifact system change over time, and which representations improve or damage coordination?

### Why it matters

A local metric such as answer accuracy can improve while overall maintenance, verification, or dependence worsens.

### Evidence base

- Licklider and Engelbart augmentation;
- distributed cognition;
- joint cognitive systems;
- human–AI interaction guidelines;
- longitudinal HCI and co-adaptation research.

### Research questions

1. What work moves from Jonathan to the system, and what new coordination work appears?
2. Which skills should the system reinforce rather than replace?
3. How does trust calibrate after errors?
4. Which artifacts become shared mental-model anchors?
5. How can adaptation remain explicit and reversible?

### Local probe

Track one workflow for eight weeks: time, corrections, repeated explanation, maintenance, reliance, satisfaction, and what Jonathan stops remembering internally.

### Starting sources

Use R20–R22 and R28–R30 in the supplied bibliography.

---

## 12. Research Thread J — Managed forgetting, lifecycle, and privacy-preserving deletion

### Central question

How should visibility, retention, retraction, redaction, purge, backup expiry, and model influence differ?

### Why it matters

A system intended to remember for years must also support user control and prevent old or sensitive material from exerting unwanted influence.

### Evidence base

- managed forgetting and memory buoyancy;
- records retention and archival practice;
- secure deletion and media sanitization;
- Git history removal;
- machine unlearning as a distinct future issue.

### Research questions

1. What preservation-value model is understandable?
2. How is vital old context protected from suppression?
3. What can be honestly guaranteed about backups?
4. Can sensitive domains use segmented encryption?
5. How are derived summaries and prompts included in purge?
6. When does a retracted item remain discoverable?

### Local probe

Build lifecycle impact plans for synthetic ordinary, historical, sensitive, and shared records.

### Starting sources

Use R27/R27B in the supplied bibliography, NIST media-sanitization guidance, and GitHub’s sensitive-data removal documentation.

---

## 13. Research Thread K — Mixed initiative, action safety, and human control

### Central question

How can the system move from retrieval to suggestion, preparation, monitoring, negotiation, and limited action without becoming unsafe or intrusive?

### Why it matters

Proactivity is a major source of potential value and a major threat to agency, privacy, attention, and trust.

### Evidence base

- mixed-initiative interaction;
- levels of automation;
- human–AI interaction guidelines;
- indirect prompt injection;
- least privilege and capability security;
- NIST/OWASP agent risk guidance.

### Research questions

1. How should initiative vary by domain and cognitive stage?
2. What actions are genuinely reversible?
3. Can users predict permission outcomes?
4. How should alert budgets and quiet modes work?
5. What does trust repair require after an action error?
6. How are evidence and control separated end to end?

### Local probe

Run two read-only monitors in shadow mode and twenty permission-comprehension scenarios before enabling any new action.

### Starting sources

Use R17–R22, R35, and the supplied safety document.

---

## 14. Research Thread L — Product architecture and design rationale

### Central question

What process best supports a complex, long-lived design whose requirements emerge through use?

### Why it matters

The project can fail through endless platform work, rapid code accumulation, or undocumented alternatives even when individual modules are technically sound.

### Evidence base

- Design Science Research Methodology;
- Spiral Model’s risk-driven iteration;
- QOC design rationale;
- Architecture Tradeoff Analysis Method;
- evolutionary and strangler migration;
- architecture fitness functions.

### Design implications to investigate

- design questions before feature tasks;
- risk-driven probes;
- quality-attribute scenarios;
- explicit alternatives and criteria;
- evidence gates and stop rules;
- architecture decisions as scoped, revisable contracts;
- removal and simplification as normal outcomes.

### Local probe

Take one subsystem decision through the full design-studio method and compare it with the previous rapid milestone process.

### Starting sources

- [Peffers et al., 2007](https://www.jmis-web.org/articles/765)
- [Boehm, 1988](https://ieeexplore.ieee.org/document/59)
- [MacLean et al., 1991](https://www.tandfonline.com/doi/abs/10.1080/07370024.1991.9667168)
- [SEI ATAM](https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/)

---

## 15. Research Thread M — Multi-party and shared memory

### Central question

What changes when memory belongs to a project, team, household, or organization rather than one person?

### Why it matters

Productization toward shared brains introduces speaker grounding, audience sensitivity, access, consent, authority, and social conflict—not merely more users.

### Evidence base

- transactive memory systems;
- organizational memory;
- common ground and shared mental models;
- distributed cognition;
- emerging multi-party agent-memory benchmarks such as GroupMemBench.

### Research questions

1. Who owns a shared memory item?
2. How are private and shared perspectives separated?
3. Who may correct, retract, or delete?
4. How does the system represent disagreement without organizational coercion?
5. What context may be shared with an AI on behalf of a group?
6. How are audience-specific terms and prior knowledge preserved?

### Local probe

Package one real project for another collaborator. Include separate personal, shared, and externally authoritative layers.

### Caution

Multi-user support is a social-governance redesign, not a database scaling feature.

## 16. Suggested research sequence

### Tier 1 — Directly shapes the next architecture

1. plural cognitive object model;
2. purpose-bound synthesis and information-loss evaluation;
3. stable provenance/time/source identity;
4. design method and quality-attribute scenarios;
5. lifecycle and purge semantics.

### Tier 2 — Shapes the next product wedge

6. re-entry and prospective memory;
7. project brain versus personal brain;
8. real-query retrieval benchmark;
9. personalization and self-model governance;
10. shared foundations across capability packs.

### Tier 3 — Contingent or longer horizon

11. multi-device replication;
12. multi-party shared memory;
13. advanced agent-memory architectures;
14. procedural-memory learning;
15. broad proactive negotiation;
16. machine unlearning.

## 17. Research brief template

```text
RESEARCH QUESTION:
Decision(s) it can change:
Current assumption:

SOURCE SET:
Primary research:
Standards/official documentation:
Current-system evidence:
Contrary evidence:

SUPPORTED FINDINGS:
1.
2.

BOUNDARIES AND UNCERTAINTY:

DESIGN IMPLICATIONS:

OPTIONS STILL OPEN:

LOCAL PROBE:

RECONSIDER WHEN:
```

## 18. Evidence-quality reminders

- A cognitive analogy does not prove a software mechanism will help.
- A benchmark result does not establish long-term user value.
- A preprint result is not a locked architecture decision.
- An official standard can define interoperability without requiring full implementation.
- A model-generated literature synthesis should be checked against primary sources for load-bearing claims.
- A locally successful prototype may be more decision-relevant than a broad average result—but only for the scope actually tested.
- Negative results and failed probes should remain part of the research memory.
