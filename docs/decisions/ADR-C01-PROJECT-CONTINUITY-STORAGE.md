# ADR-C01 — Project Continuity Storage & Representation Architecture

**Date:** 2026-07-27  
**Status:** PROVISIONAL  
**Supersedes:** None  
**Scope:** Project Continuity capability pack & kernel storage model  

---

## Decision

The storage architecture for Project Continuity capability pack v0.1 divides data into three explicit tiers:

1. **Canonical Project Narrative (`projects/<project>.md`):** Human-authored Markdown files remain the sole authority for project purpose, scope, rationale, accepted decisions, and background context.
2. **Canonical Operational Transition Records (`.bbt/records/project-transitions/<transition-id>.yaml`):** Versioned, structured YAML files remain the sole authority for operational transition state (stop points, restart cues, next physical actions, open loops, evidence references).
3. **Rebuildable Read Projections (`.bbt/projections/read-model.sqlite`):** SQLite databases, vector stores, graph indexes, and generated re-entry packs (`.bbt/artifacts/reentry/`) are derived, disposable projections that can be completely deleted and verifiably rebuilt from canonical files at any time.

---

## Rationale

- **No Split-Brain Dual Writes:** Mixing operational transition fields into canonical Markdown files creates fragile regex parsing and implicit schema changes. Separating structured records into versioned YAML files isolates machine-readable operational data while keeping it plain-text, Git-controlled, and diffable.
- **Local-First & Exportable:** Plain Markdown and YAML files allow any tool or text editor to inspect, backup, edit, or migrate project state without vendor lock-in or database corruption risks.
- **Rebuild Integrity:** Treating SQLite as a pure read projection ensures that database corruption or schema migration never destroys underlying historical truth.

---

## Consequences

- All transition records must carry a schema version (`schema: bbt.project-transition/v1`).
- Direct mutation of `.sqlite` projection tables is prohibited; projections update only via canonical file events or explicit rebuild commands.
- Deleting `.bbt/projections/` must leave the system fully functional and recoverable via `bbt rebuild`.
