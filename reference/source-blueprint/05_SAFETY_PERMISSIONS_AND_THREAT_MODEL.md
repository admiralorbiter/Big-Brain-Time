# 04 — Retrieval, Context, and Long-Term Memory

## 1. Objective

The memory system must support temporally changing, source-backed personal knowledge across many sessions. It must retrieve not merely what is textually similar, but what is authoritative, current for the requested time, relevant to the task, and safe to expose.

## 2. Query taxonomy

Every query is classified into one or more families:

| Family | Example | Preferred strategy |
|---|---|---|
| Identifier/navigation | “Open D-BBT-018” | exact registry/path lookup |
| Local factual | “What is Roll Call’s next milestone?” | FTS + metadata + canonical-source filter |
| Current truth | “What is the current SQLite decision?” | temporal resolver + supersession graph |
| Historical/as-of | “What did we believe on July 20?” | bitemporal query + historical evidence |
| Contradiction | “Where does the corpus disagree about project status?” | diagnostics + claim conflict graph |
| Multi-hop | “Which decisions affect how a context pack may be generated?” | linked records + bounded graph expansion |
| Global sensemaking | “What failure patterns recur across projects?” | hierarchy/map-reduce/community summaries |
| Re-entry/action | “What should I do first on Polaris?” | project capsule + readiness/dependency filters |
| Negative/unknown | “What is the verified backup restore date?” | observability-gap lookup + abstention |
| Research synthesis | “What does the evidence imply for multi-device sync?” | source-quality filter + cross-source synthesis |

A query may be both temporal and global; the router emits a plan rather than one label.

## 3. Retrieval pipeline

```mermaid
flowchart LR
    Q[Question] --> N[Normalize entities, IDs, time]
    N --> C[Classify query family]
    C --> A[Apply authority/privacy/time policy]
    A --> L[Lexical + exact retrieval]
    L --> X[Metadata/link expansion]
    X --> E[Optional embedding retrieval]
    E --> R[Rerank]
    R --> D[Conflict/supersession scan]
    D --> B[Evidence bundle]
    B --> P[Context pack contract]
    P --> S[Synthesis]
    S --> V[Citation/faithfulness verifier]
    V --> O[Answer or abstention]
```

### Stage 1 — normalization

- resolve typed IDs, project names, aliases, and paths
- detect an explicit or implied as-of date
- identify requested domain and privacy class
- expand abbreviations only through the alias registry

### Stage 2 — policy filters

- restrict by user permission and model access policy
- prefer canonical or authoritative external sources
- apply valid-time and recorded-time windows
- exclude expired context packs
- retain contradicted evidence when the question requires disclosure

### Stage 3 — lexical retrieval

FTS5 is the first baseline because the corpus uses stable vocabulary, typed IDs, headings, and links. Index title, path, frontmatter, heading path, body, typed IDs, aliases, and canonical-for fields with weighted ranking.

### Stage 4 — structural expansion

Expand from a hit to:

- parent and child sections
- linked decision/question/experiment records
- current project transition plan
- superseding or conflicting claims
- source artifacts
- direct dependencies

Expansion has a strict budget to avoid graph explosion.

### Stage 5 — embeddings as an experiment

Embeddings are introduced only to address demonstrated low-overlap failures. Compare:

1. FTS only
2. FTS + metadata/time filters
3. FTS + links
4. Hybrid FTS + embeddings
5. Hybrid + reranker

Do not adopt embeddings unless they improve the gold set enough to justify privacy, model, index, and maintenance costs. Proposed stop rule: less than a 10% relative improvement in hard-case evidence recall after tuning means defer.

### Stage 6 — global retrieval

Start with simple corpus hierarchy:

```text
section summaries -> document summaries -> project/area summaries -> portfolio summary
```

For a global question, retrieve relevant summaries, map across units, and reduce into a synthesis with links back to raw evidence. Add an entity/community graph only after a benchmark shows a material gain over hierarchy plus existing links.

### Stage 7 — conflict scan

Before synthesis, inspect:

- duplicate current claims
- explicit `conflicts_with`
- superseded records still surfaced in current views
- stale view dates
- authority disagreements
- unresolved observability gaps
- source date newer than last review

A conflict is not buried in a confidence score. It appears in the context pack and answer.

## 4. Context pack contract

Every generated pack begins with a machine-readable and human-readable manifest.

```yaml
context_pack_id: cp.project.polaris.2026-07-26T20-30-00Z
purpose: resume_project
query: "Catch me up on Polaris after 45 days away"
as_of_valid_time: 2026-07-26T23:59:59-05:00
as_of_recorded_time: 2026-07-26T23:59:59-05:00
authority_policy: project-current-v1
privacy_ceiling: sensitive
sources:
  - source_id: project.polaris
    locator: projects/polaris.md
    content_hash: "..."
conflicts:
  - conflict_id: "..."
omissions:
  - "Raw student data excluded by policy"
compression:
  method: extractive-plus-section-summary
  lineage_preserved: true
token_budget: 12000
generated_by: bbt-context/0.3.0
index_manifest_hash: "..."
expires_after_material_change: true
```

Human-readable sections:

1. Purpose and scope
2. Current outcome and definition of done
3. Current state
4. Latest decisions and rationale
5. Stop point and next micro-action
6. Blockers and dependencies
7. Changes since last session
8. Conflicts and stale claims
9. Unknowns/observability gaps
10. Evidence index
11. Explicit omissions

## 5. Re-entry capsule algorithm

A re-entry pack should deterministically gather:

- project canonical page
- status and milestone
- most recent material change
- latest transition plan
- unresolved work items and blockers
- decisions directly linked to the project
- open questions that can change action
- due/review triggers
- last retrospective or journal entries that mention the project
- conflicting current-state references

The model’s role is to organize and phrase the bundle. It does not invent the next action. If no valid next action exists, it says so and proposes one for review.

## 6. Memory layers

### Layer 0 — canonical evidence

Markdown/Git, operational SQLite, and external authoritative systems.

### Layer 1 — deterministic projections

Sections, links, typed records, claims, provenance, FTS, diagnostics.

### Layer 2 — semantic retrieval aids

Aliases, embeddings, graph edges, generated summaries, memory buoyancy scores. These are disposable and versioned.

### Layer 3 — episodic interaction records

Queries, context manifests, answers, corrections, accepted proposals, and user feedback. Retain selectively with privacy policy.

### Layer 4 — learned collaboration policy

Explicit preferences, initiative permissions, successful interaction patterns, and evaluation results. This layer is human-reviewable; it is not an opaque model profile.

## 7. Temporal retrieval behavior

For every claim-bearing answer:

- state the as-of date when time matters
- distinguish current state from historical state
- show a superseded claim only if useful or requested
- disclose when the newest source has not been reviewed
- avoid treating `last_reviewed` as proof every embedded claim was reverified
- allow “known now but not known then” queries by separating valid and recorded time

## 8. Abstention behavior

The system abstains when:

- no source meets the authority requirement
- sources conflict and policy says human resolution is required
- the requested date falls outside known validity
- a necessary external system has not been queried
- retrieval confidence is high but evidence does not support the requested conclusion
- the question asks for causal certainty from descriptive records
- privacy policy excludes necessary evidence

An abstention includes:

1. what cannot be concluded
2. evidence that was found
3. the missing source, field, event, or timestamp
4. why guessing would be unsafe
5. the minimum useful next step

This maps directly to the existing observability-gap model.

## 9. Regression corpus

Begin with 20 questions and grow to at least 60. Include:

- 5 exact/navigation questions
- 5 current-state questions
- 5 temporal/supersession questions
- 5 conflict/negative questions

Then add:

- multi-hop questions
- low lexical overlap paraphrases
- evidence positioned in long documents
- global synthesis questions
- counterfactual distractors
- poisoned/untrusted document content
- privacy-boundary questions
- re-entry questions after simulated 30/90/180-day gaps

Each case stores expected evidence, acceptable answer elements, forbidden claims, and whether abstention is required.

## 10. Proposed benchmark targets

These are **[PROPOSAL]** targets, not claims about current performance.

| Gate | Metric | Target |
|---|---|---|
| Context Pack v0 | Expected-source recall@5 | ≥ 0.85 on initial set |
| Context Pack v0 | Citation coverage of material claims | 100% |
| Context Pack v0 | Seeded contradiction disclosure | 100% |
| Read Model | Deterministic rebuild semantic diff | 0 unexpected differences |
| Retrieval v1 | Expected-source recall@5 | ≥ 0.92 |
| Retrieval v1 | Evidence precision@10 | ≥ 0.80 |
| Temporal | Correct current/historical selection | ≥ 0.95 |
| Abstention | Abstention F1 | ≥ 0.90 |
| Synthesis | Citation correctness | ≥ 0.98 |
| Global | Human rubric: comprehensiveness/relevance | ≥ 4/5 median |
| Re-entry | Median time to first productive action | 50% below baseline |

## 11. Retrieval explanations

Every search result and answer should expose:

- why the item matched
- authority and time filters applied
- whether it was expanded from another hit
- rank components
- content version/hash
- conflicts or supersession
- why a higher-ranked item was rejected

This creates coordination-grade understanding without overwhelming the user with model internals.

## 12. Managed forgetting in retrieval

Memory buoyancy is a ranking feature, not a truth filter. Low-buoyancy evidence can still be retrieved when:

- the query names it
- it is historically relevant
- it contradicts an active claim
- it carries high preservation value
- it is linked to the current task

Any suppressed item has an explanation and a “show all” path. The system never uses low activity alone as a deletion signal.

## 13. Model-independent context format

Store context packs as Markdown plus a JSON manifest. The body remains readable by any model or human; the manifest supports validation. Avoid provider-specific memory APIs as the canonical memory layer.


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
