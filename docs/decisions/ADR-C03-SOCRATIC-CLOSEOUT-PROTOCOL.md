# ADR-C03 — Conversational Closeout & Re-entry Pack Protocol

**Date:** 2026-07-27  
**Status:** PROVISIONAL  
**Supersedes:** None  
**Scope:** Conversational closeout harness and deterministic re-entry pack generation  

---

## Decision

1. **Conversational Voice/Chat Dump Intake:** The closeout ceremony begins with an open, conversational voice or text summary from the human user answering: *"What were you trying to do, what got decided/changed, where did you stop, and what comes next?"*
2. **Targeted Follow-Ups (0–3 max):** The system extracts candidate fields for `ProjectTransition/v1`. If required fields (`stop_point`, `next_action`) are missing or ambiguous, it asks up to 3 brief, targeted follow-up questions.
3. **Deterministic Re-entry Compiler (No-Model Fallback):** Re-entry pack compilation (`BuildReentryPack`) must be buildable deterministically without relying on LLM synthesis. LLM enhancement (e.g. connective prose) is an optional derived layer over deterministic evidence sources.
4. **Scannable & Dense Output:** All generated re-entry artifacts must prioritize structural density, bullet points, source citations, and immediate physical restart actions over long-form prose.

---

## Rationale

- **Low Cognitive Overhead:** Forcing a user to fill out multi-field web forms at the end of a session creates high friction. A 2-minute voice dump with targeted follow-ups captures complete operational state with minimal effort.
- **Fail-Safe Reliability:** If model API providers are offline or degraded, deterministic compilation guarantees that the user can still generate trusted, cited re-entry packs from raw canonical files.

---

## Consequences

- Closeout tools must support single-prompt voice transcript parsing into `ProjectTransition/v1`.
- Every re-entry pack must state its inputs, source commit hash, manifest, and whether generative synthesis was used.
