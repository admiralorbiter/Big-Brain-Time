# 05 — Safety, Permissions, and Threat Model

## 1. Security posture

Big Brain Time will eventually ingest private notes, external documents, web pages, email, calendar metadata, and model outputs. That makes it both a valuable personal system and an adversarial input processor. The safety design begins before agents are added.

## 2. Assets to protect

- canonical Markdown and Git history
- operational SQLite state
- backups and recovery keys
- health, relationship, schedule, and professional context
- external accounts and connector tokens
- Jonathan’s authentic decisions and writing voice
- action permissions and approval state
- provenance and audit trails
- evaluation data and known safety tests
- model-independent export capability

## 3. Threat actors and failure sources

1. Malicious external content author.
2. Compromised webpage, document, email, or connector result.
3. Model misinterpretation or hallucination.
4. Over-broad tool credentials.
5. Accidental user approval.
6. Buggy parser, migration, or automation.
7. Stale authority rule.
8. Multi-device conflict or partial sync.
9. Local malware or device loss.
10. Well-intentioned proactive behavior that becomes interruption spam.

## 4. Core trust boundaries

### Control plane — trusted

- explicit user request
- system policies
- installed command definitions
- typed tool schemas
- permission rules
- approved workflow templates
- signed/hashed application code and migrations

### Evidence plane — untrusted by default

- Markdown body content
- imported files
- email
- webpages
- search results
- connector responses
- model-generated summaries
- comments or instructions quoted inside sources

A canonical document can be authoritative evidence and still not be allowed to issue instructions to the runtime.

## 5. Prompt-injection controls

Indirect prompt injection research demonstrates that malicious instructions can be embedded in retrieved content and can manipulate tool-using systems. [R17] The architecture therefore uses layered controls:

1. **Structural separation:** Evidence is passed in delimited, typed fields; it cannot modify the system prompt or policy.
2. **Instruction provenance:** Only user/control-plane instructions are executable.
3. **Content labeling:** Every source carries trust, privacy, and authority classes.
4. **Least privilege:** Tools receive narrow scopes and short-lived credentials.
5. **Typed actions:** Models produce a structured proposal; no arbitrary shell/tool text is executed.
6. **Policy evaluation:** A deterministic engine validates domain, action, target, risk, and confirmation.
7. **Human review:** Consequential writes and external effects require explicit review.
8. **Output validation:** Tool arguments, file paths, recipients, and data exposure are checked.
9. **Canary tests:** Safety tests contain malicious source instructions and verify they are ignored.
10. **Audit and rollback:** Every action records before/after state and rollback information where possible.

## 6. Initiative and risk tiers

### Initiative levels

| Level | Name | Behavior |
|---|---|---|
| 0 | Silent | No use of the capability |
| 1 | Retrieve | Answer only when asked |
| 2 | Suggest | Surface an issue or option |
| 3 | Prepare | Draft context, patch, plan, or action graph |
| 4 | Act | Execute an authorized low-risk reversible action |
| 5 | Monitor | Watch for a defined trigger and notify |
| 6 | Negotiate | Challenge priorities or propose goal changes |

### Risk tiers

| Tier | Description | Examples | Default control |
|---|---|---|---|
| R0 | Read-only, no sensitive disclosure | local search, diagnostics | automatic |
| R1 | Local derived output | rebuild index, generate context pack | automatic with log |
| R2 | Reversible local canonical change | fix a broken link, update generated index | proposal or scoped authorization |
| R3 | Material personal/operational change | modify project status, create reminder | explicit review |
| R4 | External consequential action | send email, publish, schedule, delete, financial/health action | explicit confirmation each time; often out of scope |
| R5 | Forbidden | expose secrets, bypass controls, silent high-stakes decisions | never |

Initiative level cannot exceed the risk policy. “Monitor” is not automatically safer than “Act”; continuous access and interruption costs are separate risks.

## 7. Initial domain permission matrix

| Domain | Retrieve | Suggest | Prepare | Act | Monitor | Negotiate |
|---|---:|---:|---:|---:|---:|---:|
| Read-model rebuild / indexes | Yes | Yes | Yes | Yes, R1 | Yes | No |
| Repository diagnostics | Yes | Yes | Yes | Only approved mechanical fixes | Yes, bounded | No |
| Project context / transitions | Yes | Yes | Yes | Record only after review | Trigger-based | Yes, carefully |
| Tasks | Yes | Yes | Yes | Reversible local updates after pilot | Due/review triggers | Limited |
| Personal goals and identity | Yes | Yes | Draft only | No silent edits | No continuous inference | Human-led |
| Health | Yes, source-grounded | Cautious | Prep/questions only | No | Only explicit reminders | No |
| Finance/legal | Yes, source-grounded | Cautious | Draft/checklist only | No | Explicit reminders only | No |
| Email/publishing | Yes with connector policy | Yes | Draft | No autonomous send | No default monitoring | No |
| Calendar | Yes | Yes | Draft event/ICS | Explicit approval | Explicit triggers | No |
| Code/tooling | Yes | Yes | Yes | Scoped repo action when directed | CI monitoring | No |

## 8. Safe action lifecycle

```text
READ -> PROPOSE -> SIMULATE -> POLICY CHECK -> REVIEW -> EXECUTE -> VERIFY -> AUDIT -> ROLLBACK/COMMIT
```

Every proposal includes:

- objective
- evidence basis
- affected resources
- action sequence
- permissions requested
- predicted side effects
- reversibility
- preconditions and hashes
- verification plan
- rollback plan
- expiration time

A stale proposal cannot execute if its precondition hash no longer matches current state.

## 9. Threat scenarios and controls

### Scenario A — malicious note tells the AI to exfiltrate data

**Control:** note is evidence only; proposal parser ignores embedded instructions; outbound tools are unavailable or require explicit recipient and user confirmation; privacy filter blocks unrelated data.

### Scenario B — stale decision causes wrong project guidance

**Control:** temporal resolver and supersession scan; current answers include conflicts; regression case; no “latest text wins.”

### Scenario C — model silently rewrites Jonathan’s authentic voice

**Control:** model output remains a proposal; semantic diff highlights tone/meaning changes; personal writing requires human acceptance; original preserved in Git.

### Scenario D — derived index hides a vital old record

**Control:** high-preservation records ignore buoyancy suppression; “show suppressed” mode; retrieval tests include hidden-old-but-critical cases.

### Scenario E — backup appears successful but cannot restore

**Control:** scheduled isolated restore drill; checksum and application invariants; evidence of last successful restore shown by `bbt doctor`.

### Scenario F — multi-device concurrent edits split state

**Control:** year-one single-writer assumption; device lease/write lock for SQLite-canonical state; Git conflict detection for Markdown; CRDT decision deferred until measured need.

### Scenario G — action graph mutates more than approved

**Control:** resource-scoped operations, before hashes, maximum affected-item count, dry run, postcondition checks, automatic stop on mismatch.

### Scenario H — proactive monitoring becomes noisy

**Control:** shadow mode; alert budget; batching; quiet hours; per-rule precision; disable rules above false-alert threshold.

## 10. Privacy architecture

- Classify at source, document, section/claim, and context-pack level where needed.
- Enforce “minimum necessary evidence” before model calls.
- Prefer local parsing and retrieval.
- Use provider adapters with explicit data-handling policy.
- Redact secrets and high-risk identifiers before remote inference.
- Record what evidence was sent to which model and when.
- Keep credentials outside the corpus and database.
- Encrypt devices and independent backups.
- Separate personal Big Brain Time from employer operational secrets.

## 11. Safety test suite

The safety suite includes:

- indirect injection in Markdown, HTML, email, and quoted model output
- tool-poisoning descriptions
- path traversal and unsafe file targets
- recipient substitution
- stale proposal/precondition mismatch
- authorization boundary tests
- privacy-class leakage tests
- high-risk domain action attempts
- prompt requesting hidden instructions or secrets
- malicious source requesting policy override
- rollback failure simulation

A new connector cannot ship until its threat model, permission scope, and adversarial fixtures exist.

## 12. Release gates for autonomy

### Gate A — Suggest

- no tool execution
- source and rationale displayed
- useful-suggestion rate measured
- dismissals captured without pressure

### Gate B — Prepare

- typed proposals
- deterministic policy classification
- complete affected-resource list
- dry-run diff

### Gate C — Reversible local act

- 100% pass on authorization fixtures
- rollback tested
- kill switch tested
- zero unintended resources in seeded scenarios
- action log complete

### Gate D — External act

Not a year-one goal. Requires separate threat model, explicit user decision, per-action confirmation, recipient/target verification, and a long successful shadow period.

## 13. Trust repair

When the system is wrong it should:

1. identify the exact unsupported or stale claim
2. show the evidence and policy that led to it
3. accept the correction without defensiveness
4. preserve the incorrect output in the run log
5. record a correction/supersession rather than overwrite history
6. add or update a regression case
7. explain what behavior will change
8. avoid inflating confidence after a correction


## Source conventions

This package distinguishes three kinds of statements:

- **[SOURCE]** — directly supported by the two supplied Big Brain Time documents.
- **[RESEARCH]** — supported by external primary literature or official technical documentation listed in `09_RESEARCH_BIBLIOGRAPHY.md`.
- **[PROPOSAL]** — a design recommendation, target, threshold, or inference introduced by this blueprint. It must be tested before being promoted into canonical Big Brain Time decisions.

Local source keys:

- **[S1]** `sources/handbook.md`, exact copy of the supplied Big Brain Time Handbook, compiled 2026-07-21.
- **[S2]** `sources/repository-audit-and-planning.txt`, exact copy of the supplied repository audit and architecture planning transcript.
