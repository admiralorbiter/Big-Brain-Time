# 11 — Risk Register

**Review mode:** event-driven and at every milestone gate. Probability and impact are initial planning judgments, not measured facts.

## 1. Risk scoring

- **Probability:** Low / Medium / High.
- **Impact:** Medium / High / Critical.
- A risk is **accepted** only with a named owner, observable trigger, mitigation, and contingency.
- Any Critical risk with a failed control blocks the related milestone.

## 2. Register

| ID | Category | Risk | Probability | Impact | Early signal | Preventive control | Contingency | Gate |
|---|---|---|---|---|---|---|---|---|
| RISK-001 | Recovery | Independent backup exists in name but restore is unproven | Medium | Critical | No dated restore artifact; backup cannot reconstruct exact commit | Sprint 1 isolated restore, checksums, handbook rebuild, documented RTO/RPO | Freeze writes; restore from last verified Git commit and reconstruct derived stores | M0 |
| RISK-002 | Canonical authority | Markdown and SQLite become co-equal writers | Medium | Critical | Same field differs; reconciliation scripts appear permanent | One-writer-per-information-type matrix; projections are read-only; migration end dates | Rollback aggregate to former authority using export and append-only change log | M2/M4 |
| RISK-003 | Migration | A big-bang rewrite stalls or corrupts working practices | Medium | High | Large schema/UI work before real capability test | Strangler slices; milestone gates; keep old workflow usable | Abandon incomplete slice and retain canonical Markdown | All |
| RISK-004 | Epistemic integrity | Old or corrected claim is presented as current | High | Critical | Answers lack as-of basis or supersession scan | Bitemporal claims, authority policy, contradiction checks, regression fixtures | Retract answer, show history, create incident and missing-rule test | M2/M5 |
| RISK-005 | Provenance | Generated synthesis loses source granularity | High | High | Paragraph-level citations cannot support individual claims | Claim-evidence links; citation verifier; sentence/claim mapping | Abstain or return evidence-only result | M5 |
| RISK-006 | Retrieval | Full-handbook prompting creates false confidence | High | High | Good answers on obvious questions but failures on dispersed evidence | Gold set, low-overlap/distractor tests, bounded packs, compare baselines | Use deterministic evidence browser without synthesis | M1/M3 |
| RISK-007 | Retrieval | Embeddings add complexity without measurable gain | Medium | Medium | Operational dependency appears before lexical baseline | Feature flag; hard benchmark; adopt only if material improvement | Remove embedding index; retain FTS5 and metadata retrieval | M3 |
| RISK-008 | Global sensemaking | Graph extraction amplifies model errors | Medium | High | Entity/relationship graph treated as truth | Derived graph with provenance and confidence; compare deterministic hierarchy | Delete graph projection and rebuild; use section/link aggregation | M3 |
| RISK-009 | Temporal model | Valid time and recorded time are conflated | Medium | High | As-of answers change incorrectly after corrections | Explicit fields and query tests; temporal examples in fixtures | Mark temporal answer unsupported until data is repaired | M2 |
| RISK-010 | IDs | Stable typed IDs remain duplicated or get reassigned | High | High | Import collisions; one ID points to unrelated records | Global registry, uniqueness constraint, alias/migration records | Quarantine collisions; never auto-merge by ID alone | M1/M2 |
| RISK-011 | Parsing | Markdown diversity breaks deterministic import | High | Medium | Silent skipped sections or malformed front matter | Loss-tolerant parser with errors as diagnostics; source spans; fixture corpus | Keep raw document index and exclude failed structured projections | M1/M2 |
| RISK-012 | Drift diagnostics | Warnings become noisy and are ignored | High | High | High dismissal/suppression rate; repeated false positives | Severity, confidence, suppression with expiry, benchmark precision target | Disable rule, preserve incident examples, redesign before re-enable | M1/M6 |
| RISK-013 | Managed forgetting | Vital context is suppressed from active views | Medium | Critical | User discovers relevant item only after harm or delay | Preservation class, explanation, 'show suppressed', vital-context tests | Disable automatic suppression; restore neutral ranking | M3/M6 |
| RISK-014 | Task management | System becomes another brittle task manager | Medium | High | More maintenance than execution; duplicate professional tasks | Migrate one narrow aggregate; preserve external authority; measure burden | Export and return task authority to Markdown/external system | M4 |
| RISK-015 | Recurrence | Custom recurrence semantics create edge-case failures | Medium | High | Ad hoc fields for every exception | RRULE-compatible subset; bounded generation; ICS round-trip tests | Keep calendar authoritative and store only rules/context | M4 |
| RISK-016 | Flask | UI drives domain logic and blocks CLI/voice reuse | Medium | Medium | Business rules appear in route handlers/templates | Application services first; contract tests; thin blueprints | Refactor route logic before adding new screens | M4 |
| RISK-017 | Security | Indirect prompt injection controls a tool or policy decision | Medium | Critical | Retrieved text appears in action arguments/instructions | Evidence/control plane separation, typed tools, action firewall, adversarial tests | Kill switch, revoke connector, inspect audit log, repair policy/test | M5/M6 |
| RISK-018 | Privacy | Sensitive context is sent to an external model | Medium | Critical | Pack has no privacy label or destination manifest | Classification before model access; minimization; allowlists; local redaction | Revoke access, incident log, rotate exposed secrets if any | All |
| RISK-019 | Authorization | A broad grant authorizes unintended targets | Medium | Critical | Permission says 'edit files' without path/action limits | Capability-style grants scoped by domain/action/target/time; deny by default | Revoke grant; restore from Git; add boundary fixture | M6 |
| RISK-020 | External action | System sends/publishes/schedules unintended content | Low | Critical | Action path bypasses proposal/review | No external actions in year-one default; explicit confirmation and preview | Cancel/retract if possible; incident; disable connector | Post-v1 |
| RISK-021 | Audit | Action history is incomplete or mutable | Medium | High | Cannot reconstruct who/what/why after a change | Append-oriented audit events, checksums, Git commit links, retention policy | Freeze action subsystem until audit integrity restored | M5/M6 |
| RISK-022 | Model dependence | A model update silently changes behavior | High | High | Benchmark regression after provider/model change | Record model/version/prompts; continuous regression suite; deterministic fallbacks | Pin/rollback model or disable synthesis | M3+ |
| RISK-023 | Vendor lock-in | Critical memory exists only in model-specific format | Medium | High | Prompts, embeddings, or conversations cannot export | Model-independent Markdown/JSON contracts and adapter interfaces | Rebuild derived artifacts with another provider/local model | All |
| RISK-024 | Performance | Rebuild/search latency makes the system feel heavy | Medium | Medium | Doctor/rebuild exceeds targets; UI waits on model | Profile deterministic pipeline, incremental indexes, bounded context | Use last valid projection; schedule full rebuild manually | M2/M3 |
| RISK-025 | Scope | Ambitious subsystem map causes endless platform work | High | High | No real daily workflow improves after several sprints | Every milestone tied to one user capability and stop rule | Pause platform expansion; ship smallest proven workflow | All |
| RISK-026 | Adoption | Maintenance exceeds perceived benefit | Medium | Critical | Weekly review skipped; captures accumulate; manual correction rises | Measure maintenance minutes and capture-to-use; simplify aggressively | Retire low-value structure and revert to simpler Markdown workflow | All |
| RISK-027 | Human model | System freezes changing preferences or identity into permanent facts | Medium | Critical | Old personal inference influences current recommendations | Temporal claims, explicit review, no unreviewed psychographic facts | Remove/supersede model, disclose influence, add prohibited inference rule | M5/M6 |
| RISK-028 | Coordination | AI produces more text but not lower coordination cost | High | Medium | Re-prompts, verification, and mental load do not fall | Measure time/corrections; strategy-aware concise exhibits; templates | Disable verbose synthesis; return structured evidence/action options | All |
| RISK-029 | Evaluation | Benchmarks overfit seeded defects and miss real failures | Medium | High | Perfect gold-set score but user still corrects common answers | Add live incidents, holdout cases, mutation testing, periodic benchmark refresh | Lower autonomy; expand evaluation before shipping | All |
| RISK-030 | Data sensitivity | Professional or third-party data crosses repository boundaries | Medium | Critical | Raw student/client/internal data appears in BBT | Boundary scanner, source-system references, minimization, explicit exclusions | Remove from history where feasible, notify relevant authority, review process | All |
| RISK-031 | Concurrency | Multi-device writes create conflicts before sync model is ready | Low | High | Simultaneous edits or DB copies diverge | Year-one single-writer rule; Git-based handoff; no shared live DB | Select one authoritative copy; manual merge with audit | Pre-M4 |
| RISK-032 | Backups | Git remote is mistaken for an independent backup | Medium | Critical | Same credentials/device compromise all copies | Separate encrypted backup and restore proof; retention and offline copy | Use independent backup; rotate credentials; investigate compromise | M0 |
| RISK-033 | Schema | Migration destroys round-trip Markdown fidelity | Medium | High | Export diffs lose wording, comments, unknown front matter | Preserve raw source spans; canonical export fixtures; semantic + textual diff | Abort migration and return authority to Markdown | M4 |
| RISK-034 | Proactivity | Monitoring becomes surveillance-like or intrusive | Medium | High | Unexpected inferences/alerts; user discomfort | Explicit monitored signals, shadow mode, pause controls, data minimization | Disable monitor and delete derived observations per retention rule | M6 |
| RISK-035 | Safety process | Confirmation fatigue causes blind approvals | Medium | High | High-volume prompts accepted without reading | Batch low-risk proposals, reserve interruption for consequence, improve scopes | Lower initiative; remove repeated confirmation source | M6 |

## 3. Highest-priority compound failure modes

### A. Epistemic failure chain

`parser omission → incomplete retrieval → confident synthesis → canonical patch → propagated error`

Controls must exist at every boundary: visible parse errors, benchmarked retrieval, abstention, claim-level citation checks, proposal diffs, and reversible execution. A good final answer cannot compensate for an invisible ingestion failure.

### B. Migration failure chain

`dual authority → divergent writes → reconciliation heuristics → unclear truth → irreversible cleanup`

The prevention is architectural: one active writer per information type, explicit projections, finite transitional architecture, exports, and rollback rehearsals.

### C. Agentic security failure chain

`malicious retrieved content → model treats evidence as instruction → broad tool grant → external consequence`

The prevention is separation of the evidence and control planes, narrow typed tools, deterministic authorization, target-scoped grants, previews, and a kill switch. Model self-restraint is not a security boundary.

### D. Adoption failure chain

`ambitious schema → capture friction → stale corpus → poor retrieval → more automation → higher maintenance`

The response is simplification, not another layer. Track maintenance minutes, skipped reviews, unprocessed captures, and re-entry time. Stop or remove features that do not improve a real capability.

## 4. Risk review protocol

At each milestone:

1. Re-score probability and impact using incidents and measurements.
2. Close risks only when the failure mode is impossible, transferred, or evidenced below an accepted threshold.
3. Convert every significant incident into a regression fixture or control test.
4. Check whether one mitigation created a new maintenance, privacy, or usability risk.
5. Review all permissions, connector scopes, model versions, and backup evidence.
6. Record a Ready-to-Resume state for unresolved high risks.

## 5. Stop-the-line conditions

Immediately pause affected writes/actions when any of these occurs:

- failed restore or integrity check
- unexplained loss of canonical content
- duplicate identity/typed-ID collision with ambiguous merge
- citation verifier accepts unsupported claims
- model output bypasses the action firewall
- permission boundary test fails
- sensitive data reaches an unauthorized service
- external action occurs without the required approval
- audit history is missing or alterable
- managed forgetting hides a designated vital item
- benchmark regression exceeds the accepted threshold after a model or schema change

Restart only after the incident is explained, the control is repaired, a regression test exists, and the relevant milestone gate is re-run.

## 6. Risk ownership proposal

| Risk family | Proposed owner role | Independent reviewer role |
|---|---|---|
| Recovery, schema, imports | Implementer | Verifier |
| Retrieval and temporal truth | Retrieval engineer / archivist | Adversarial evaluator |
| Privacy and permissions | System owner | Security reviewer |
| User experience and maintenance | Jonathan | Retrospective facilitator |
| Model behavior | AI integrator | Benchmark/audit role |
| External connectors | Connector owner | Least-privilege reviewer |

One person may hold several roles in a single-user project, but the review *mode* should remain distinct: the implementation session should not be the only audit of its own work.
