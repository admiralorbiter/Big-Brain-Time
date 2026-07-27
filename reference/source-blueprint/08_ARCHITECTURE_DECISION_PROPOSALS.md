# 07 — Evaluation and Experiments

## 1. Evaluation thesis

Big Brain Time succeeds when the joint system—Jonathan, AI, language, artifacts, methods, and training—can do something reliably that the parts could not do alone. Feature count, note count, token count, and model benchmark scores are secondary.

## 2. Scorecard

### Trust and recovery

| Metric | Definition | Baseline | Year-one proposal |
|---|---|---:|---:|
| Last verified restore age | Days since a successful isolated restore | Unknown | ≤ 30 days |
| Recovery time objective | Time to restore canonical corpus and rebuild projections | Measure in Sprint 1 | ≤ 30 minutes |
| Unexpected semantic loss | Missing/changed canonical records after restore/export cycle | Not measured | 0 |
| Unresolved P0 diagnostics | Data-loss/privacy/canonical-integrity findings | Audit reported issues | 0 |

### Retrieval and epistemic quality

| Metric | Definition | Proposed target |
|---|---|---:|
| Evidence recall@5 | Expected sources retrieved in top 5 | ≥ 0.92 |
| Evidence precision@10 | Relevant evidence among top 10 | ≥ 0.80 |
| Citation correctness | Cited source actually supports the claim | ≥ 0.98 |
| Citation coverage | Material claims with citations | 1.00 |
| Temporal selection accuracy | Correct current/historical claim selection | ≥ 0.95 |
| Contradiction disclosure recall | Seeded known conflicts disclosed | 1.00 |
| Abstention F1 | Correctly abstain when records do not support answer | ≥ 0.90 |
| Counterfactual resistance | Reject false statement embedded in retrieved evidence | ≥ 0.95 |

### Human capability and coordination

| Metric | Definition | Year-one proposal |
|---|---|---:|
| Time to first productive action | From opening a dormant project to meaningful work | 50% reduction |
| Re-explanation count | Times Jonathan must restate already-recorded context | 50% reduction |
| Correction count | Material AI assumptions corrected per session | 50% reduction |
| Weekly maintenance burden | Time spent keeping BBT operational | ≤ 30 minutes median |
| Capture-to-use conversion | Processed captures used in a decision/project/view | Establish baseline, improve |
| Decision comprehensibility | Later ability to explain why a decision was made | ≥ 4/5 review rubric |
| Long-gap resumption success | Projects resumed after 30+ days without full reread | ≥ 80% |
| Subjective cognitive burden | 1–7 rating after review/resumption | Downward trend |
| Trust calibration | User confidence matches measured correctness | No systematic overtrust |

### Proactivity and action safety

| Metric | Definition | Gate |
|---|---|---:|
| Useful suggestion rate | Suggestions accepted or acted upon | ≥ 60% before expansion |
| False-warning rate | Alerts judged unnecessary/wrong | ≤ 10% mature target |
| Interruptions per day | Proactive interruptions | User-configured budget |
| Unauthorized action rate | Action outside policy/scope | 0 |
| Rollback success | Reversible actions restored correctly | 100% in tests |
| Audit completeness | Action has actor, basis, before/after, result | 100% |

Targets are ambitious starting hypotheses. Baseline collection may require recalibration.

## 3. Evaluation case design

Each evaluation case contains:

- stable ID
- question/task
- query family
- valid and recorded as-of time
- expected evidence IDs/sections
- acceptable answer elements
- explicitly forbidden claims
- known conflicts
- whether abstention is expected
- privacy ceiling
- human rubric
- regression history

Cases are version-controlled. Any material failure that reaches the user becomes a new or updated case.

## 4. Experiment portfolio

### E1 — Full handbook versus project context pack

**Question:** Does scoped, citation-bearing context improve answer quality and reduce tokens compared with supplying the full handbook?

**Design:** Select 10 project questions. Run both conditions with the same model. Blind-rate correctness, citations, conflict disclosure, omissions, latency, and token use.

**Decision rule:** Adopt scoped packs as default if they improve correctness or conflict disclosure without meaningful loss of necessary context. Retain full handbook for global audit cases.

### E2 — FTS5 versus hybrid retrieval

**Question:** Do embeddings materially improve low-overlap retrieval beyond FTS + metadata + links?

**Design:** Use exact, paraphrase, low-overlap, temporal, and multi-hop cases. Compare recall, precision, latency, privacy/cost, and maintenance.

**Stop rule:** Defer embeddings if relative hard-case recall improves less than 10% or if gains disappear under human relevance review.

### E3 — Temporal truth resolver

**Question:** Can the system correctly distinguish what was true, what was believed, and when a correction was recorded?

**Design:** Seed corrected experiment results, superseded decisions, expired “today” language, and project-status changes.

**Gate:** 100% on small deterministic fixtures before model synthesis uses temporal answers.

### E4 — Ready-to-resume capsule

**Question:** Does a structured transition record reduce time and friction when resuming work?

**Design:** Alternate projects/sessions with and without a capsule; measure time to first productive action, rereads, confusion, and subjective burden.

**Decision rule:** Keep fields that predict faster resumption; remove ceremonial fields that are rarely useful.

### E5 — Propagation detection

**Question:** When a decision changes, does the system identify all dependent artifacts?

**Design:** Create 10 seeded change scenarios with known downstream views, records, questions, and indexes.

**Gate:** 100% recall on P0/P1 dependencies; precision can be tuned later.

### E6 — Shadow proactive monitoring

**Question:** Which warnings are useful enough to interrupt or batch?

**Design:** For four weeks, generate but do not send/act on candidate alerts. Jonathan reviews a daily/weekly digest and labels useful, late, redundant, wrong, or intrusive.

**Stop rule:** Disable any rule with persistent false-warning rate above 20% or no observed action value.

### E7 — Managed forgetting ranking

**Question:** Can buoyancy reduce clutter without hiding critical history?

**Design:** Compare search and weekly-review views with and without buoyancy. Include old but high-preservation evidence.

**Gate:** No critical-evidence misses; clutter reduction must be subjectively noticeable.

### E8 — Permission comprehension

**Question:** Can Jonathan predict what the system will do before it acts?

**Design:** Present action scenarios and ask for expected behavior; compare with actual policy outcome.

**Gate:** ≥ 90% agreement before enabling local actions; confusing policies are redesigned.

### E9 — Voice capture transfer

**Question:** Does voice reduce capture friction without creating unprocessable noise?

**Design:** Pilot a narrow voice inbox. Measure captures, processing time, ambiguity, privacy mistakes, and capture-to-use conversion.

**Stop rule:** Do not expand voice interfaces if they increase backlog or sensitive accidental capture.

### E10 — Multi-device need test

**Question:** Is concurrent-write complexity actually justified?

**Design:** Instrument device use for three months: number of devices, offline edits, conflicts, and urgency.

**Decision rule:** Adopt CRDT/replication complexity only if meaningful concurrent edits occur often enough that a single-writer or Git-sync model is materially harmful.

## 5. Experiment lifecycle

```text
Friction observed
  -> hypothesis
  -> smallest reversible intervention
  -> baseline and measures
  -> live use
  -> result and confounders
  -> retain, revise, or remove
  -> update canonical decision and regression set
```

## 6. Release confidence classes

- **Prototype:** useful artifact exists; no reliability claim.
- **Tested:** deterministic unit/integration tests pass.
- **Benchmarked:** evaluation suite meets stated threshold.
- **Piloted:** used in real workflows with logged feedback.
- **Trusted:** sustained performance, recovery, and safety evidence.
- **Authorized:** permission policy allows action in a defined scope.

A feature can be Trusted for retrieval but not Authorized for action.

## 7. Failure and stop criteria

Pause or remove a feature when:

- it creates a second source of truth
- it increases weekly maintenance without measurable benefit
- it cannot explain its evidence or time policy
- it hides critical context
- it fails restore/export tests
- its alerts are mostly dismissed or wrong
- users cannot predict its action boundary
- it requires model/vendor lock-in for canonical access
- it encourages over-offloading of judgment or learning
- it treats absence of evidence as evidence of absence
- it turns exploratory hypotheses into confident canonical claims

## 8. Baseline collection during Sprints 0–5

Record:

- time to find five known facts
- time to resume three projects
- current number of broken/stale/duplicate diagnostics
- full-handbook answer performance on 20 questions
- number of corrections and re-explanations in normal sessions
- weekly maintenance time
- subjective trust and cognitive burden

Without baseline data, year-one improvement claims remain speculative.


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
