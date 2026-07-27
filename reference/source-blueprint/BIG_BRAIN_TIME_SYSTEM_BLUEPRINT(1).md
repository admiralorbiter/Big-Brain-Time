# Artifact Manifest

**Package:** Big Brain Time — Research and Delivery Blueprint  
**Prepared:** 2026-07-26  
**Canonical output directory:** `/mnt/data/big-brain-time-blueprint`

## Package summary

- Principal numbered documents: **12**
- Combined blueprint: **1**
- Backlog tasks: **120 across 24 sprints**
- Milestones: **8**
- Proposed ADRs: **20**
- Risks: **35**
- Bibliography entries: **36**
- Included exact source copies: **2**
- Validation status: **PASS** (`validation_report.json`)

## Files

| Path | Bytes | Lines | SHA-256 | Purpose |
|---|---:|---:|---|---|
| `00_EXECUTIVE_BLUEPRINT.md` | 11549 | 152 | `d2865e90618d3f4cca8b0bc4a5dafb67baa8e8af9c80e25ca6ae9a43a9cbfb39` | Mission, capability tests, migration strategy, horizons, architectural laws, innovative bets, and non-goals. |
| `01_RESEARCH_SYNTHESIS.md` | 15842 | 297 | `11cf74837b51572fca43aebacc0f826fd6ec9476c66f9199dbcc9ae97e89ca5f` | Research findings translated into architectural constraints and rejection criteria. |
| `02_TARGET_ARCHITECTURE.md` | 14083 | 419 | `f6ae46d8f4c3129b11ca6401a1b3c69789d5941a8949ce779b03e6230aa94ab7` | Modular-monolith architecture, boundaries, modules, deployment, and migration path. |
| `03_DOMAIN_AND_DATA_MODEL.md` | 12688 | 553 | `911487d1e3e2fce952f28d4db3b0719a1789dceb10e8e14d81578b0094a375f1` | Authority matrix, provenance, bitemporal claims, operational aggregates, permissions, and audit schema. |
| `04_RETRIEVAL_CONTEXT_AND_MEMORY.md` | 11498 | 310 | `ad21983858f7de85d89ab4dd8f2a631838ecf062ea960d2f8d863f2c771d285e` | Query taxonomy, retrieval pipeline, context contracts, local/global sensemaking, and memory evaluation. |
| `05_SAFETY_PERMISSIONS_AND_THREAT_MODEL.md` | 10875 | 254 | `5afe098b96b161cd2f01daa900529cbc3636f0b6aaf2d55d04b38e5fb75d3989` | Trust boundaries, initiative levels, permission matrix, action firewall, threats, and safety gates. |
| `06_ROADMAP_MILESTONES_AND_SPRINTS.md` | 15021 | 361 | `41ebb6d42ac023a97a2f837b58061694bc7eaabdb763b5255e2f78954a7e4d0d` | Eight milestones, 24 sprint goals, critical path, evidence gates, and multi-year horizons. |
| `07_EVALUATION_AND_EXPERIMENTS.md` | 10056 | 225 | `00a277e8af4ddba3cf1ee34980a66bc485178a48d5504e0ac9dcf173f5bbd581` | Capability scorecard, benchmark design, ten experiments, baselines, and stop rules. |
| `08_ARCHITECTURE_DECISION_PROPOSALS.md` | 8874 | 157 | `15103fed2f5cb369f5e0880515dc76a9643a35579279e0b9337262bacf87d835` | Twenty proposed ADRs for explicit acceptance, amendment, or rejection. |
| `09_RESEARCH_BIBLIOGRAPHY.md` | 15091 | 87 | `f1ac29f702c889cbd45c960db9166f21b787eb1ca1cc050753f931eb36b30048` | Thirty-six primary/official research references and research-to-delivery traceability. |
| `10_DISCOVERY_AND_REQUIREMENTS_WORKSHEET.md` | 17344 | 383 | `30d12ba8dc8ce5b63786011d6077fb8e7e73289517c0b4fb94d64c76bfb820d1` | User-specific requirements, authority, initiative, privacy, typical-week, and traceability worksheets. |
| `11_RISK_REGISTER.md` | 14338 | 118 | `a55b25e98799849acf67bdfdb71f4a5afb301649e2909299a3f29aa12ac556c3` | Thirty-five risks, compound failure chains, review protocol, stop-the-line criteria, and ownership. |
| `BIG_BRAIN_TIME_SYSTEM_BLUEPRINT.md` | 200162 | 3813 | `bf67156d53f955c578bc615eed5c26f84b4812764a172d34b27e97cae011c5be` | Combined narrative blueprint containing all principal planning documents and the readable backlog. |
| `README.md` | 4429 | 59 | `22413439a568596b751a2b3b1661f3d81968320ba43d922e1028bfcb4719620d` | Package overview, reading order, and immediate execution guidance. |
| `product_backlog.csv` | 39207 | 121 | `8f45f56fab4a440bca1b71a84ceee8b4b57c2bbbba3049cbe311c57fe9b454fa` | Importable UTF-8-with-BOM backlog with tasks, acceptance tests, dependencies, owner roles, evidence basis, and risk. |
| `product_backlog.md` | 40879 | 404 | `50a521fc1ee6831e0f0e71275de1b988a2f015b8e8f10e60ae01d089c86d420e` | Human-readable 120-task backlog grouped into 24 sprints. |
| `sources/handbook.md` | 248269 | 4309 | `d0913c9573dc1538b1525014d8ca95f6bcd890d2e10d58117a1f276be5f75b15` | Exact copy of the supplied Big Brain Time handbook. |
| `sources/repository-audit-and-planning.txt` | 15524 | 277 | `453965a7668122be8eb341385240c743d441090fa7a554a49ddb2a357679ba55` | Exact copy of the supplied audit and architecture-planning transcript. |
| `validation_report.json` | 4483 | 201 | `003734927f2617adaebd12488f7bf84dc991794b8874a0093c17c89aca14029d` | Machine-readable structural validation results. |

## Validation performed

- All required generated files are present.
- All text artifacts decode as UTF-8/UTF-8-BOM.
- Generated Markdown code fences are balanced.
- Generated relative Markdown links resolve; exact source copies intentionally preserve their original workspace links.
- All research IDs used by the blueprint resolve to bibliography entries.
- Included source copies match the uploaded originals by SHA-256.
- The CSV contains 120 unique tasks, exactly five for each of S0–S23, with non-empty acceptance tests.
- The roadmap contains all 24 sprints.
- The ADR document contains 20 unique proposed decisions.
- The risk register contains 35 unique risks.
- The combined blueprint contains all principal narrative sections and the readable backlog.

## Reproducibility note

The package separates source-derived content, outside research, and design proposals. The two supplied source files are preserved verbatim under `sources/`. The generated plan is not a silent mutation of the user’s canonical repository; proposed ADRs and requirements must be accepted through the project’s own governance process.
