# 09 — Research Bibliography and Evidence Map

**Research review date:** 2026-07-26

This bibliography privileges primary research, standards, and official technical documentation. The annotations state how each source constrains the blueprint; they do not imply that every research idea should be implemented.

## 1. Evidence map

| ID | Theme | Source | Architectural use |
|---|---|---|---|
| R01 | Local-first | [Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). *Local-First Software: You Own Your Data, in Spite of the Cloud*. Onward! 2019.](https://www.inkandswitch.com/local-first/) | Defines ownership, offline operation, longevity, privacy, and multi-device ideals; supports local authority and exportability without making CRDTs mandatory. |
| R02 | Migration | [Fowler, M. (2021). *Patterns of Legacy Displacement*.](https://martinfowler.com/articles/patterns-legacy-displacement/) | Supports incremental displacement, seams, transitional architecture, and outcome-oriented migration. |
| R03 | Migration | [Fowler, M. (2004). *Strangler Fig Application*.](https://martinfowler.com/bliki/StranglerFigApplication.html) | Supports replacing capability slices around an existing system rather than a big-bang rewrite. |
| R04 | SQLite | [SQLite Project. *SQLite FTS5 Extension*.](https://www.sqlite.org/fts5.html) | Primary technical basis for lexical full-text retrieval, phrase/prefix/NEAR queries, ranking, and tokenization. |
| R05 | SQLite | [SQLite Project. *Online Backup API*.](https://www.sqlite.org/backup.html) | Primary basis for transactionally consistent snapshots and tested recovery workflows. |
| R06 | SQLite | [SQLite Project. *VACUUM — VACUUM INTO*.](https://www.sqlite.org/lang_vacuum.html) | Alternative way to create compact database copies; relevant to portable local backups. |
| R07 | SQLite | [SQLite Project. *STRICT Tables*.](https://www.sqlite.org/stricttables.html) | Supports stronger type guarantees while retaining SQLite portability. |
| R08 | Application architecture | [Pallets Projects. *Flask Application Factories*.](https://flask.palletsprojects.com/en/stable/patterns/appfactories/) | Supports testable app construction, unbound extensions, multiple configurations, and thin interfaces over domain services. |
| R09 | Provenance | [W3C. (2013). *PROV-O: The PROV Ontology* and *PROV Overview*.](https://www.w3.org/TR/prov-overview/) | Conceptual basis for entities, activities, agents, derivation, attribution, and responsibility; blueprint adopts a deliberately small relational subset. |
| R10 | Time and recurrence | [IETF. (2009). *RFC 5545: Internet Calendaring and Scheduling Core Object Specification (iCalendar)*.](https://www.rfc-editor.org/rfc/rfc5545) | Authoritative recurrence, recurrence-date, exception-date, and occurrence identity semantics. |
| R11 | Long context | [Liu, N. F., et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts*. arXiv:2307.03172.](https://arxiv.org/abs/2307.03172) | Shows that relevant-position effects make nominal context length an unreliable proxy for usable memory. |
| R12 | Long context | [Hsieh, C.-P., et al. (2024). *RULER: What's the Real Context Size of Your Long-Context Language Models?* arXiv:2404.06654.](https://arxiv.org/abs/2404.06654) | Motivates multi-hop, aggregation, and distractor-heavy retrieval tests rather than needle-only evaluation. |
| R13 | Long context | [Modarressi, A., et al. (2025). *NoLiMa: Long-Context Evaluation Beyond Literal Matching*. arXiv:2502.05167.](https://arxiv.org/abs/2502.05167) | Motivates low-lexical-overlap cases and semantic bridging in the retrieval regression set. |
| R14 | Long-term memory | [Wu, D., et al. (2024). *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*. arXiv:2410.10813.](https://arxiv.org/abs/2410.10813) | Provides memory task families: extraction, multi-session reasoning, temporal reasoning, updates, and abstention. |
| R15 | Global sensemaking | [Edge, D., et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. arXiv:2404.16130.](https://arxiv.org/abs/2404.16130) | Supports separating targeted fact retrieval from corpus-wide sensemaking; graph construction remains benchmark-gated. |
| R16 | Global sensemaking | [Microsoft Research. *GraphRAG project and documentation*.](https://www.microsoft.com/en-us/research/project/graphrag/) | Implementation reference for hierarchical community summaries and global queries. |
| R17 | Security | [Greshake, K., et al. (2023). *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. arXiv:2302.12173.](https://arxiv.org/abs/2302.12173) | Primary basis for treating retrieved documents, email, and web content as untrusted evidence rather than executable instructions. |
| R18 | Risk management | [NIST. (2024). *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)*.](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | Lifecycle risk-management frame for governance, measurement, and incident response. |
| R19 | Security | [OWASP Cheat Sheet Series. *LLM Prompt Injection Prevention Cheat Sheet*.](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Operational controls: privilege isolation, input boundaries, monitoring, output validation, and human approval for consequential actions. |
| R20 | Mixed initiative | [Horvitz, E. (1999). *Principles of Mixed-Initiative User Interfaces*. CHI '99.](https://www.microsoft.com/en-us/research/publication/principles-mixed-initiative-user-interfaces/) | Supports balancing automation and direct manipulation using uncertainty, timing, goals, and interruption costs. |
| R21 | Human–AI interaction | [Amershi, S., et al. (2019). *Guidelines for Human-AI Interaction*. CHI 2019.](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) | Design guidance across initial interaction, regular use, error handling, and adaptation. |
| R22 | Automation | [Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). *A Model for Types and Levels of Human Interaction with Automation*. IEEE Transactions on Systems, Man, and Cybernetics—Part A, 30(3), 286–297.](https://doi.org/10.1109/3468.844354) | Supports different autonomy levels for acquisition, analysis, decision selection, and action rather than one global automation level. |
| R23 | Resumption | [Leroy, S., & Glomb, T. M. (2018). *Tasks Interrupted: How Anticipating Time Pressure on Resumption of an Interrupted Task Causes Attention Residue and Low Performance on Interrupting Tasks and How a “Ready-to-Resume” Plan Mitigates the Effects*. Organization Science.](https://doi.org/10.1287/orsc.2017.1184) | Empirical basis for explicit transition records and re-entry plans. |
| R24 | Prospective closure | [Masicampo, E. J., & Baumeister, R. F. (2011). *Consider It Done! Plan Making Can Eliminate the Cognitive Effects of Unfulfilled Goals*. Journal of Personality and Social Psychology.](https://doi.org/10.1037/a0024192) | Supports specific future plans as a way to reduce intrusive activation of unfinished goals. |
| R25 | Cognitive offloading | [Risko, E. F., & Gilbert, S. J. (2016). *Cognitive Offloading*. Trends in Cognitive Sciences, 20(9), 676–688.](https://doi.org/10.1016/j.tics.2016.07.002) | Supports explicit allocation of volatile details to tools while protecting internal judgment and skill. |
| R26 | Personal information management | [Jones, W., Bruce, H., & Dumais, S. (2001). *Keeping Found Things Found on the Web*. CIKM '01.](https://www.microsoft.com/en-us/research/publication/keeping-found-things-found-web/) | Shows why reminding, context, and workflow integration matter more than merely saving links. |
| R27 | Managed forgetting | [Jilek, C., Runge, Y., Niederée, C., Maus, H., Tempel, T., Dengel, A., & Frings, C. (2019). *Managed Forgetting to Support Information Management and Knowledge Work*. KI—Künstliche Intelligenz, 33(1), 45–55.](https://doi.org/10.1007/s13218-018-00568-9) | Basis for memory buoyancy, preservation value, inhibition, condensation, and gradual reversible reduction of prominence. |
| R27B | Managed forgetting | [Jilek, C., Maus, H., Tempel, T., Frings, C., Niederée, C., & Dengel, A. (2026). *Self-(re)organizing and Especially Forgetful Personal Knowledge Assistants to Support Information Management and Knowledge Work*. In *Intentional Forgetting with Intelligent Systems*, pp. 101–128.](https://doi.org/10.1007/978-3-032-17621-9_6) | Recent synthesis extending managed-forgetting work toward self-organizing personal knowledge assistants and context spaces. |
| R28 | Human–computer symbiosis | [Licklider, J. C. R. (1960). *Man-Computer Symbiosis*. IRE Transactions on Human Factors in Electronics.](https://groups.csail.mit.edu/medg/people/psz/Licklider.html) | Frames complementary division of labor and reduction of clerical/executive friction. |
| R29 | Augmentation | [Engelbart, D. C. (1962). *Augmenting Human Intellect: A Conceptual Framework*. SRI Report AFOSR-3223.](https://www.dougengelbart.org/content/view/138/) | Basis for evaluating the H-LAM/T joint system and bootstrapping capability rather than isolated tool features. |
| R30 | Distributed cognition | [Hutchins, E. (1995). *Cognition in the Wild*. MIT Press.](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/) | Supports analyzing representation propagation, artifacts, people, and time as one cognitive system. |
| R31 | RAG evaluation | [Es, S., et al. (2023). *RAGAS: Automated Evaluation of Retrieval Augmented Generation*. arXiv:2309.15217.](https://arxiv.org/abs/2309.15217) | Reference for separating retrieval context quality, answer faithfulness, and answer relevance. |
| R32 | RAG evaluation | [Saad-Falcon, J., Khattab, O., Potts, C., & Zaharia, M. (2023). *ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems*. arXiv:2311.09476.](https://arxiv.org/abs/2311.09476) | Reference for evaluation with lightweight judges calibrated by a smaller human-labeled set. |
| R33 | Temporal databases | [Snodgrass, R. T. (1999). *Developing Time-Oriented Database Applications in SQL*. Morgan Kaufmann.](https://shop.elsevier.com/books/developing-time-oriented-database-applications-in-sql/snodgrass/978-0-08-050422-3) | Foundational treatment of valid time, transaction time, bitemporal tables, temporal keys, and current/prior-state queries. |
| R34 | Provenance | [W3C. (2013). *PROV-DM: The PROV Data Model*.](https://www.w3.org/TR/prov-dm/) | Formal conceptual reference for derivations and responsibility; used selectively, not implemented wholesale. |
| R35 | Agent safety | [OWASP Cheat Sheet Series. *AI Agent Security Cheat Sheet*.](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) | Reference for tool authorization, action validation, observability, memory safety, and human control. |

## 2. Research-to-delivery traceability

| Research cluster | Decisions influenced | Delivery evidence required |
|---|---|---|
| Local-first and legacy displacement | ADR-P01–ADR-P05; Markdown/Git authority; disposable read model; no big-bang migration | Restore test, deterministic rebuild, export/re-import test, authority matrix |
| SQLite and Flask | ADR-P04–ADR-P06; FTS5, STRICT tables, application factory, thin interface | Integrity checks, schema migrations, idempotent importer, CLI parity before web UI |
| Long context and long-term memory | ADR-P07–ADR-P08; context packs, query router, regression set, abstention | Gold questions, distractor cases, low-overlap cases, as-of/update cases, full-handbook comparison |
| Global sensemaking | ADR-P08; two-stage local/global retrieval; graph is optional | Deterministic hierarchy baseline and benchmark evidence before adding graph extraction |
| Provenance and temporal databases | ADR-P09; claims, evidence links, supersession, bitemporal queries | Correction scenarios, authority conflicts, valid-time vs recorded-time tests |
| Recurrence and resumption | ADR-P10; RRULE compatibility; transition aggregate | Recurrence edge cases, exception round-trip, time-to-first-productive-action experiment |
| PIM, offloading, and managed forgetting | Contextual ingestion; retrieval reminders; reversible suppression | Capture-to-use rate, hidden-vital-context test, maintenance burden |
| Mixed initiative and automation | Domain/action permission matrix; shadow mode; progressive autonomy | Suggestion utility, false-alert and interruption rates, authorization boundary tests |
| Prompt injection and agent security | Evidence/control plane separation; typed tools; action firewall | Adversarial fixture suite, least-privilege test, audit completeness, kill switch |
| Joint cognitive systems | Human coordination cost and capability scorecard | Re-entry, correction burden, repeated-explanation rate, trust and cognitive-load measures |

## 3. Evidence quality rules for future research ingestion

1. Prefer a primary paper, standard, or official project documentation over a secondary summary.
2. Preserve the exact claim supported by a source; do not upgrade suggestive evidence into a universal design law.
3. Record publication date, access date, version, and whether the source is peer reviewed, a preprint, a standard, or documentation.
4. Separate empirical findings from the blueprint’s interpretation and proposed implementation.
5. Store quotations sparingly; preserve page/section location when a precise claim matters.
6. Add a `reconsider_if` condition when a research-derived decision depends on model, corpus-size, or deployment assumptions.
7. Re-run benchmark evidence when models, retrieval algorithms, or corpus characteristics materially change.

## 4. Research gaps still worth targeted investigation

- Longitudinal field evidence on solo human–AI co-adaptation over months or years.
- Practical bitemporal claim-resolution patterns for personal knowledge systems rather than enterprise databases.
- Evaluation of contradiction disclosure and abstention as trust-repair mechanisms.
- Low-maintenance, user-legible methods for memory buoyancy that do not hide essential context.
- Voice-first interruption and resumption design for a local personal operating system.
- Multi-device sync options that preserve a simple single-writer model until collaboration truly requires CRDT complexity.
- Privacy-preserving local embeddings and model routing under consumer hardware constraints.
- How proactive systems can negotiate priorities without increasing interruption cost or undermining agency.

## 5. Local source basis

- **S1:** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **S2:** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
