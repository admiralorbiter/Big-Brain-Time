# 03 — Domain and Data Model

## 1. Modeling principles

1. Model **authority**, **time**, **provenance**, and **uncertainty** explicitly.
2. Preserve the existing typed-ID vocabulary and “one canonical home” rule.
3. Separate document representation from semantic records.
4. Separate current operational state from historical evidence.
5. Prefer small, inspectable schemas over ontologies that cannot be maintained.
6. Use derived relationships when they can be rebuilt; store only relationships that carry human meaning or authority.
7. Corrections supersede; they do not rewrite history.
8. The absence of evidence remains representable as an observability gap.

## 2. Core identity model

### `agent`

Represents an actor responsible for a claim or activity.

```text
agent_id                stable text ID
agent_type              person | ai_model | script | organization | external_system
name                    display name
version                 model/script version when relevant
trust_class             owner | trusted_tool | external_authority | untrusted_source
active_from / active_to optional
```

### `source_artifact`

A piece of evidence or canonical material.

```text
source_id
source_type              markdown | git_commit | email | webpage | calendar_event | file | conversation | database_record
canonical_uri            path, URL, connector ID, or stable reference
content_hash
captured_at
source_date
privacy_class            private | sensitive | shareable
trust_class              canonical | authoritative_external | corroborating | memory | unverified | hostile_possible
metadata_json
```

### `activity`

A provenance-producing process.

```text
activity_id
activity_type            capture | import | extraction | synthesis | decision | correction | migration | execution
started_at / ended_at
agent_id
input_manifest_hash
software_version
parameters_json
status
```

## 3. Document representation

### `document`

```text
document_id              existing frontmatter ID where present
path
relative_path
content_hash
frontmatter_json
maturity
state_described          current_state | proposed_state | historical_state
document_type
status
privacy
owner
created_at
last_reviewed_at
review_after
canonical_for_json
source_commit
```

### `document_version`

Stores projection metadata for a Git/blob version; raw history remains in Git.

```text
document_version_id
document_id
source_commit
content_hash
recorded_at
valid_from / valid_to    optional semantic period
change_summary
```

### `section`

```text
section_id               deterministic document_id + stable heading/path fingerprint
document_id
parent_section_id
heading
heading_path
ordinal
body_text
body_hash
line_start / line_end
claim_density
```

### `link_edge`

```text
link_id
from_document_id
from_section_id
to_kind                  document | section | typed_record | external
raw_target
resolved_target
link_text
status                    valid | broken | ambiguous | external_unchecked
```

## 4. Typed registry records

The existing decision, question, experiment, work-item, and observability-gap IDs should become a normalized projection.

### `typed_record`

```text
record_id                 e.g., D-BBT-015
record_type               decision | question | experiment | work_item | observability_gap | journal_entry
source_document_id
source_section_id
title
status
priority
owner
created_at
closed_at
review_at
payload_json
```

A validator enforces global uniqueness by type and prevents identifier reuse after deletion.

## 5. Claims and temporal truth

### `claim`

```text
claim_id
subject_ref               entity/record/document/topic
predicate                 controlled but extensible text
object_json               literal or entity reference
claim_type                fact | observation | interpretation | hypothesis | decision | plan | unknown
scope
confidence_label          optional, not a numeric truth score
valid_from
valid_to                  NULL means open-ended
recorded_at
retracted_at
status                    asserted | superseded | disputed | retracted | historical
asserting_agent_id
authority_domain
```

### `evidence_link`

```text
claim_id
source_id
source_locator            lines, section, page, record ID
relation                  supports | contradicts | qualifies | originated_from | merely_mentions
extraction_activity_id
review_status             unreviewed | human_reviewed | machine_verified
notes
```

### `claim_relation`

```text
from_claim_id
to_claim_id
relation                  supersedes | corrects | conflicts_with | depends_on | narrows | broadens | derived_from
created_at
agent_id
rationale
```

### Bitemporal rule

- `valid_from`/`valid_to`: when the claim is intended to apply.
- `recorded_at`: when Big Brain Time learned or recorded it.
- `retracted_at`/supersession: when the system changed its epistemic position.

Example:

```text
Claim A: experiment witness count = 0
valid_from: experiment date
recorded_at: initial log date
status: superseded

Claim B: experiment witness count = 25
valid_from: same experiment date
recorded_at: correction date
relation: corrects Claim A
```

An as-of-recorded-time query can show what was believed then; a current-valid-time query returns the corrected state while preserving the earlier record.

## 6. Authority resolution

A claim resolver must not choose “latest timestamp wins” universally. It applies an ordered policy:

1. Filter to the requested valid-time and recorded-time window.
2. Exclude retracted claims unless the query asks for history.
3. Apply explicit supersession/correction edges.
4. Apply authority rules by domain.
5. Prefer direct contemporaneous records over memory when the domain rule says so.
6. Preserve multiple claims when authorities legitimately differ.
7. Mark unresolved conflict rather than forcing a winner.
8. Return the selected claim, rejected alternatives, policy used, and evidence.

### `authority_rule`

```text
rule_id
domain
subject_pattern
preferred_source_type
preferred_agent_id
priority
valid_from / valid_to
resolution_behavior       choose | show_both | abstain | require_human
rationale
```

## 7. Entities and relationships

A lightweight entity graph supports retrieval without forcing all prose into structured triples.

### `entity`

```text
entity_id
entity_type               person | organization | project | area | system | concept | place | artifact
canonical_name
status
privacy
valid_from / valid_to
```

### `entity_alias`

```text
entity_id
alias
alias_type                abbreviation | old_name | nickname | external_id
valid_from / valid_to
```

### `relationship`

```text
relationship_id
from_entity_id
to_entity_id
relationship_type
valid_from / valid_to
recorded_at
source_claim_id
status
```

Entity extraction from prose is derived and reviewable. Human-authored relationships become canonical only after acceptance.

## 8. Projects, tasks, and transitions

### `project`

```text
project_id                preserve `project.*` IDs
name
outcome
definition_of_done
status                    active | maintenance | waiting | incubating | paused | complete | archived
area_id
reason_now
current_milestone_id
priority
valid_from / valid_to
narrative_document_id
```

### `milestone`

```text
milestone_id
project_id
name
outcome
status
target_date
completed_at
acceptance_json
```

### `task`

```text
task_id
project_id
milestone_id
name
description
status                    backlog | ready | active | blocked | waiting | done | dropped
priority
start_after
due_at
review_at
effort_hint
next_physical_action      boolean or separate field
source_ref
created_at / completed_at
```

### `task_dependency`

```text
predecessor_task_id
successor_task_id
relation                  blocks | informs | must_follow | optional
```

### `transition_plan`

```text
transition_id
project_id
session_id
created_at
stop_point
restart_cue
next_micro_action
resumption_trigger
open_loops_json
active_context_json
superseded_by
quality_status            complete | missing_fields | stale
```

A project cannot be marked “ready to resume” unless the latest transition plan passes required-field validation and is newer than the last material project change.

## 9. Time, routines, and recurrence

### `recurrence_series`

```text
series_id
name
domain
rrule                     RFC 5545-compatible
start_datetime
timezone
duration
external_authority_ref
review_policy
active_from / active_to
```

### `occurrence_exception`

```text
exception_id
series_id
recurrence_id             original occurrence identifier
action                    cancel | reschedule | modify | complete | skip
replacement_start
payload_json
recorded_at
```

### `reminder_policy`

```text
policy_id
target_ref
trigger_type              time | state | dependency | location | context | review_due
trigger_json
channel
initiative_level
quiet_hours_policy
status
```

The first version should generate occurrences only for bounded query windows and export ICS rather than becoming a complete calendar server.

## 10. Proposals, permissions, and audit

### `change_proposal`

```text
proposal_id
proposal_type             patch | structured_update | reminder | action_graph | decision
created_by_agent
created_at
basis_manifest_hash
risk_tier
summary
status                    draft | pending_review | approved | rejected | expired | executed | failed
expires_at
```

### `change_operation`

```text
operation_id
proposal_id
sequence
operation_type            add | update | supersede | move | archive | call_tool
resource_ref
precondition_hash
payload_json
rollback_json
```

### `permission_rule`

```text
permission_id
domain
action
max_initiative_level
risk_ceiling
resource_scope
confirmation_mode
valid_from / valid_to
rationale
```

### `action_audit`

```text
audit_id
proposal_id
operation_id
requested_by
approved_by
executed_by
started_at / ended_at
result
before_hash / after_hash
rollback_status
error_json
```

## 11. Retrieval and evaluation records

### `evaluation_case`

```text
case_id
case_type                 exact | temporal | conflict | multi_hop | global | abstention | action
question
as_of_valid_time
as_of_recorded_time
expected_evidence_json
forbidden_claims_json
abstention_expected
rubric_json
```

### `retrieval_run`

```text
run_id
case_id
query_text
router_version
index_manifest_hash
started_at
latency_ms
hits_json
metrics_json
```

### `answer_run`

```text
answer_run_id
retrieval_run_id
model_id
prompt_template_version
context_manifest_hash
answer_text
claim_citation_map_json
verifier_result_json
human_correction_json
```

## 12. Minimal schema for the first read model

Do not implement the full target schema in Sprint 6. Start with:

1. `document`
2. `section`
3. `link_edge`
4. `typed_record`
5. `diagnostic`
6. `build_manifest`
7. FTS5 virtual tables

Add `claim`, `source_artifact`, `evidence_link`, and `claim_relation` during the provenance milestone. Add operational tables only after the workbench gate.

## 13. Round-trip and export guarantees

For every SQLite-canonical aggregate:

- Export a complete Markdown representation and normalized JSON.
- Preserve stable IDs, timestamps, rationale, and history.
- Reimport the export into an empty database.
- Compare semantic equivalence, not row IDs.
- Keep versioned JSON Schema for exports.
- Include an `EXPORT_MANIFEST.json` with schema version, count, hashes, and generation time.
- Test that a future user can understand the data without the application.

## 14. Model boundaries

Not everything should become a claim or entity. Keep prose when:

- meaning depends on narrative context
- the structure is not reused operationally
- a schema would create more maintenance than retrieval value
- the information is exploratory or evolving

Promote prose into structured records only when repeated queries, automation, constraints, or temporal reasoning justify the cost.


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
