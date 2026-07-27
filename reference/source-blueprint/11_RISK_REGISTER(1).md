# 10 — Discovery and Requirements Worksheet

This worksheet converts the supplied documents into testable requirements while leaving genuinely personal choices visible. It is not a prerequisite to begin Sprints 0–2; unanswered items become explicit assumptions or observability gaps rather than hidden guesses.

## 1. Product framing

### Current source-backed framing

- **[SOURCE]** The system should help Jonathan resume accurately without rereading the corpus and warn when knowledge disagrees with itself.
- **[SOURCE]** The preferred long-term direction is a local-first Flask + SQLite personal operating system with subsystem-by-subsystem migration and Markdown exportability.
- **[SOURCE]** The unit of design is the joint cognitive system: Jonathan + AI + language + artifacts + methods + training.
- **[SOURCE]** Graceful re-entry, provenance, temporal truth, managed forgetting, explicit initiative levels, and low maintenance are already core values.

### Proposed one-sentence outcome

> When Jonathan opens Big Brain Time after an interruption, it should assemble the smallest trustworthy representation of what matters, explain why it believes it, reveal conflict or uncertainty, and help execute the next safe action.

**Decision:** accept / amend / reject  
**Notes:**

---

## 2. Ten high-value questions the system should answer

The first five are directly implied by the audit; the remainder are ambitious candidates. For each, supply one real example and describe what an unacceptable answer would look like.

| ID | Candidate question | Why it matters | Real example / notes |
|---|---|---|---|
| QCAP-01 | What should I work on next, and why now? | Tests operational prioritization and rationale | |
| QCAP-02 | I have been away from this project for 30–60 days. What changed, where did I stop, and what is the first physical action? | Core re-entry test | |
| QCAP-03 | What is the current decision on this issue, what did it supersede, and what would cause reconsideration? | Temporal truth and rationale | |
| QCAP-04 | Which documents disagree about this project, person, plan, or fact? | Contradiction and propagation detection | |
| QCAP-05 | Show the evidence for this answer and tell me what is missing. | Provenance and abstention | |
| QCAP-06 | Which commitments, review triggers, or dependencies are likely to become important in the next two weeks? | Prospective memory without alert overload | |
| QCAP-07 | What have I repeatedly postponed, abandoned, or reconstructed, and what system change might remove the friction? | Metacognitive and process improvement | |
| QCAP-08 | Across my projects, what themes, bottlenecks, and capability gaps are emerging? | Global sensemaking | |
| QCAP-09 | What did I believe at a specified past date, and when did the record change? | Bitemporal history | |
| QCAP-10 | Prepare a safe, cited context pack for another model or collaborator, with privacy and authority boundaries. | Interoperability and context engineering | |

### Acceptance template for each question

- **Authoritative sources:**
- **Time boundary:**
- **Required citations:**
- **Conflicts that must be disclosed:**
- **What should cause abstention:**
- **Maximum useful response length:**
- **Maximum acceptable retrieval time:**
- **Privacy class:**
- **Benchmark example:**

---

## 3. Five recurring actions the system should support

| ID | Candidate action | Default initiative | Consequence class | Human checkpoint |
|---|---|---|---|---|
| ACAP-01 | Capture a conversation, classify its contents, and propose canonical destinations | Prepare | Reversible draft | Before canonical write |
| ACAP-02 | Generate or refresh a project re-entry capsule | Prepare | Reversible draft | Review before replacing current capsule |
| ACAP-03 | Detect stale, broken, conflicting, or unpropagated state | Monitor in shadow mode | Read-only | User decides disposition |
| ACAP-04 | Prepare a patch set after a decision or project-state change | Prepare | Reversible proposal | Diff approval before execution |
| ACAP-05 | Assemble a daily/weekly exhibit from projects, tasks, time, and review triggers | Suggest/Prepare | Read-only or reversible view | User may pin, dismiss, or correct |

Optional later actions:

- Create calendar drafts from an approved operational record.
- Open a scoped project workspace and suppress unrelated context.
- Generate a research ingestion packet with source traceability.
- Run a retrospective and propose one experiment.
- Export a project or domain into Markdown/JSON/ICS.

---

## 4. Propagation scenarios

Document five real examples where one change should update or challenge dependent representations.

| ID | Trigger change | Dependent artifacts | Desired system behavior | What must not happen |
|---|---|---|---|---|
| PROP-01 | A decision is superseded | Project plan, now view, context packs, open questions | Flag dependents; prepare reviewable changes | Silently rewrite historical rationale |
| PROP-02 | A project becomes paused or complete | Task board, dashboard, reminders, portfolio view | Remove from active focus while preserving history | Delete or lose re-entry state |
| PROP-03 | A factual result is corrected | Experiment log, synthesis, index, answers | Preserve old claim as corrected; prefer current claim | Continue presenting old result as current |
| PROP-04 | An external authority changes | Local interpretation, preparation checklist, linked project | Mark local claim stale; request review | Treat external content as an instruction |
| PROP-05 | A personal constraint changes | Routines, schedules, plans, recommendations | Show affected commitments and alternatives | Infer sensitive facts or make external changes |

For each scenario, specify:

- trigger source
- authority
- valid date
- recorded date
- relation (`supersedes`, `corrects`, `conflicts_with`, `depends_on`)
- expected proposal
- approval rule
- rollback rule

---

## 5. Three non-negotiable prohibitions

The source material strongly implies the first three. Confirm or amend them.

1. **Never silently destroy or overwrite meaningful history.**
2. **Never present old, inferred, or conflicting information as settled current truth.**
3. **Never send, publish, schedule, purchase, disclose, or mutate consequential external state without explicit scoped authorization.**

Additional candidates:

- Never place secrets, authenticators, government IDs, or raw financial tokens in the corpus.
- Never let instructions inside retrieved evidence authorize tools.
- Never hide uncertainty merely to produce a smooth answer.
- Never make a high-stakes health, legal, or financial decision on Jonathan’s behalf.
- Never preserve a psychological inference as a durable personal fact without explicit review.

---

## 6. Typical-week narrative

Narrate one recent week using the prompts below. Concrete interruptions and handoffs are more useful than an idealized routine.

### Monday–Friday

- How does work begin?
- Which repositories, calendars, email accounts, task systems, and AI tools are opened?
- What creates a new task or project?
- How are meetings and interruptions handled?
- Which work tends to be reconstructed?
- What gets captured but never reused?
- What decisions change multiple artifacts?
- What happens when a task is blocked?
- How does work end?
- What must be remembered for tomorrow?

### Evenings and weekends

- When are personal projects, learning, health logistics, hobbies, and planning handled?
- When is voice interaction valuable?
- Which activities can coexist, and which require protected focus?
- What kinds of reminders help versus annoy?
- Which information should deliberately disappear from active focus?
- How is a long-neglected project resumed?

### Irregular events

- Travel or loss of normal transportation
- Medical appointments or health preparation
- A production incident
- A new research idea
- A major external deadline
- A multi-week gap
- Loss of network access
- A model/tool becoming unavailable

---

## 7. Authority-by-information-type worksheet

Use one active writer per information type. A secondary representation is a projection, cache, export, or reference—not a co-equal source of truth.

| Information type | Current authority | Year-one proposed authority | External source? | Export requirement | Migration gate |
|---|---|---|---|---|---|
| Narrative knowledge | Markdown/Git | Markdown/Git | Sometimes | Lossless Markdown | None |
| Decisions and rationale | Markdown/Git | Markdown/Git initially; structured projection | No | Markdown + JSON | Proven correction/supersession model |
| Claims and provenance | Mixed prose | SQLite projection + source Markdown | Yes | JSON/Markdown report | Deterministic extraction and review |
| Projects | Markdown | Pilot one aggregate in SQLite after M3 | Work systems for professional detail | Markdown | Round-trip and rollback |
| Tasks | Markdown view | SQLite for selected personal/system tasks | Professional backlog external | Markdown/CSV | Weekly pilot reduces burden |
| Transitions/re-entry | Markdown sections | SQLite operational aggregate + Markdown export | No | Markdown | Re-entry experiment passes |
| Calendar events | External calendar | External calendar | Yes | ICS draft/reference | Explicit authority boundary |
| Recurring responsibilities | Markdown | SQLite RRULE-compatible series | Sometimes | ICS + Markdown | Exception tests pass |
| Journal | Markdown/Git | Markdown/Git | No | Markdown | No migration planned |
| Research sources | Files/links/Markdown | Source registry + original references | Yes | Bibliography/JSON | Provenance parser |
| Search indexes | None/generated | Disposable SQLite/FTS5 | No | Rebuild only | Deterministic rebuild |
| Context packs | Generated | Disposable generated artifacts | No | Markdown/JSON | Benchmark and invalidation |
| Embeddings/graphs | None | Optional disposable projection | No | Rebuild only | Must beat simpler baseline |
| Permissions | Rules in prose | Structured policy + signed/recorded grants | No | Human-readable report | Action firewall tests |
| Audit events | Git/logs | Append-oriented SQLite + export | Connector logs external | JSON/Markdown | Integrity and retention design |

---

## 8. Usage and deployment choices

Mark the expected year-one and long-term target.

| Question | Year one | Long term | Decision notes |
|---|---|---|---|
| One Windows computer? | | | |
| Multiple personal computers? | | | |
| Phone read access? | | | |
| Phone capture? | | | |
| Remote web access? | | | |
| Fully offline core? | | | |
| Voice while gaming/away from keyboard? | | | |
| Single user only? | | | |
| Shared projects or household access? | | | |
| Local model use? | | | |
| Cloud model use for selected context? | | | |
| Encrypted attachment store? | | | |

### Proposed default assumption for year one

Single primary writer on one trusted Windows machine; private Git remote as versioned backup/sync; localhost Flask; external models receive only explicitly prepared context packs; no unattended internet-facing service; no CRDT layer.

This is a proposal, not a source-backed fact. Revisit it before M4.

---

## 9. Domain initiative matrix

For each domain, select the maximum permitted level:

1. Retrieve
2. Suggest
3. Prepare
4. Act
5. Monitor
6. Negotiate

| Domain | Max level | Permitted actions | Prohibited actions | Review cadence |
|---|---:|---|---|---|
| Repository diagnostics | | | | |
| Generated indexes/context packs | | | | |
| Project plans | | | | |
| Personal goals | | | | |
| Calendar | | | | |
| Email | | | | |
| Health | | | | |
| Finance | | | | |
| Professional systems | | | | |
| Code repositories | | | | |
| Research ingestion | | | | |
| Media/hobbies | | | | |

Also classify each action by reversibility and external consequence. A high domain level does not automatically authorize every action within that domain.

---

## 10. Trust-destroying failures

Rank each 1–5 for severity and add missing cases.

| Failure | Severity | Detectability | Recovery requirement |
|---|---:|---:|---|
| Data loss or failed restore | | | |
| Old belief presented as current | | | |
| Fabricated or missing citation | | | |
| Conflict hidden from the answer | | | |
| Private data sent to the wrong model/service | | | |
| Retrieved prompt injection causes an action | | | |
| Unintended email, post, calendar event, or external mutation | | | |
| Too many alerts or repeated false warnings | | | |
| Vital context suppressed by “managed forgetting” | | | |
| Authentic writing voice overwritten | | | |
| Irreversible schema migration | | | |
| System maintenance becomes a second job | | | |
| AI model of Jonathan becomes rigid or invasive | | | |
| A wrong automation is repeated at scale | | | |

---

## 11. Nonfunctional requirements

### Portability

- Canonical narrative remains human-readable without the application.
- Every SQLite-canonical aggregate has a documented export.
- Derived stores can be deleted and rebuilt.
- Stable IDs do not encode mutable status or dates.

### Reliability

- Independent backup and restore are tested.
- Imports are idempotent and atomic.
- Integrity checks include database constraints and domain invariants.
- Every consequential operation has a durable audit record.

### Performance

Proposed initial targets, to be validated:

- `bbt doctor` on the current corpus: under 5 seconds on the primary machine.
- Typical local search: under 500 ms before model synthesis.
- Context-pack compilation: under 3 seconds for deterministic retrieval.
- Flask first render for common local pages: under 1 second.
- Complete derived-store rebuild at 1,000 documents: under 60 seconds.
- No requirement to optimize for 10,000 documents until benchmark data exists.

### Privacy

- Data classification is enforced before context leaves the machine.
- Context packs name their privacy class and model destination.
- Secrets are excluded by rule and scanner.
- External connectors are least-privilege and domain-scoped.

### Explainability

- Every answer exposes evidence, authority, time basis, conflicts, and omissions.
- Every ranking or suppression decision can show its major contributing signals.
- Every action proposal shows target, arguments, permissions, and rollback.

### Accessibility and interaction

- Core workflows work via keyboard and text.
- Voice is an interface over the same commands, not a separate state machine.
- The system remains usable without AI synthesis.
- Dense dashboards are avoided when a focused exhibit is more useful.

---

## 12. Data classification worksheet

| Class | Examples | Local storage | Git | External model | Logging |
|---|---|---|---|---|---|
| Shareable | Public research notes, published writing | Yes | Yes | Allowed | Full |
| Private | Personal plans, ordinary journal, project notes | Yes | Private only | Explicit pack | Metadata + scoped content |
| Sensitive | Health observations, relationship details, work-sensitive summaries | Encrypted trusted device | Only per accepted policy | Default deny; explicit exception | Minimized |
| Secret | Passwords, tokens, recovery codes, government IDs | Password manager only | Never | Never | Never store value |

Add organization-specific and connector-specific classes as needed.

---

## 13. Transformative one-year test

Complete this sentence:

> After one year, Big Brain Time would feel transformative if it reliably ________________________________, while requiring no more than __________________ of deliberate maintenance per week, and I trusted it enough to ________________________________.

Candidate measurable outcome:

- Resume any active project after a 30-day gap in under 5 minutes.
- Cut repeated explanations to AI by at least 50%.
- Detect at least 90% of seeded contradiction/propagation defects with fewer than 10% nuisance warnings.
- Produce source-complete context packs that outperform the full-handbook baseline.
- Keep weekly maintenance at or below 30 minutes.
- Authorize only a small set of reversible local actions after zero policy-boundary failures in the red-team suite.

These are proposed targets; baseline them before adoption.

---

## 14. Requirement traceability record

For every accepted requirement, create:

```yaml
id: REQ-BBT-###
title:
source:
  - user_statement:
  - local_document:
  - research:
type: functional | nonfunctional | safety | governance
priority: must | should | could | not_now
acceptance_test:
owner:
status: proposed | accepted | implemented | verified | retired
depends_on: []
reconsider_if: []
privacy:
```

A requirement is not complete until its acceptance test is executable or a documented manual protocol exists.

---

## 15. Decisions that do not need to block the first two sprints

The following can remain open while backup, parsing, diagnostics, and benchmark fixtures are built:

- Final mobile strategy
- CRDT or multi-writer sync
- Embedding model
- Graph database or GraphRAG
- Voice technology
- Remote hosting
- Exact long-term task schema
- Contact/relationship subsystem
- Health subsystem depth
- Automated proactive monitoring
- External sending or publishing
- Whether most narrative knowledge ever leaves Markdown

This prevents ambitious discovery from delaying the trust foundation.
