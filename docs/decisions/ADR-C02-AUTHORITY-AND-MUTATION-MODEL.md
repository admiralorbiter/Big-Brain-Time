# ADR-C02 — Authority, Human Confirmation, & Proposal Boundaries

**Date:** 2026-07-27  
**Status:** PROVISIONAL  
**Supersedes:** None  
**Scope:** Human-AI control loop, permissions, and canonical mutation rules  

---

## Decision

1. **Human Authority for Canonical Mutations:** No LLM, agent, background task, or automated script may directly mutate or create canonical files (`projects/*.md`, `.bbt/records/*`) without explicit human acceptance.
2. **Models Operate in the Proposal Plane:** Model responses, voice synthesis extraction, context-pack proposals, and transition drafts are proposals (`Status: Draft / Proposed`). They are rendered into staging buffers or interactive approval prompts (`bbt transition review`).
3. **No Unconfirmed Deletes or Overwrites:** Canonical records and historical files can never be deleted or overwritten by automated processes. Corrections create new versioned transition records with explicit supersession links.

---

## Rationale

- **Preventing Hallucinated Authority:** Allowing generative models to write directly to canonical files risks corrupting historical facts and introducing unverified assumptions into the project baseline.
- **Enforcing Read-Propose-Review-Write:** Keeping model outputs in the proposal tier guarantees that the human user remains the final authority for commitments, decisions, and operational stop points.

---

## Consequences

- The application layer must strictly separate query (`READ`), proposal (`PROPOSE`), and canonical mutation (`SUPERSEDE` / `WRITE`) execution paths.
- The CLI/Voice harness must present explicit diffs or summary cards for human approval before committing files to disk.
