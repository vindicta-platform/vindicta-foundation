# Platform Evolution Tracker

> **Maturity status and health of every Vindicta Platform repository.**
> This document is validated by CI against the GitHub org API — staleness triggers build failure.

---

## Tech Radar Rings

| Ring         | Meaning                                      |
| ------------ | -------------------------------------------- |
| 🟢 **Adopt**  | Production-ready, actively used, stable API  |
| 🟡 **Trial**  | Under active development, API may change     |
| 🟠 **Assess** | Exploratory, evaluating fit for the platform |
| 🔴 **Hold**   | Frozen, deprecated, or archived              |

---

## Repository Status

### Meso-Repositories (Active)

| Repository                                                                      | Ring    | Language  | Status   | Notes                                  |
| ------------------------------------------------------------------------------- | ------- | --------- | -------- | -------------------------------------- |
| [vindicta-platform](https://github.com/vindicta-platform/vindicta-platform)     | 🟢 Adopt | Python/TS | ✅ Active | Orchestrator, Workspace root, UI & API |
| [vindicta-foundation](https://github.com/vindicta-platform/vindicta-foundation) | 🟢 Adopt | Python    | ✅ Active | Shared Kernel, Governance, Docs        |
| [vindicta-engine](https://github.com/vindicta-platform/vindicta-engine)         | 🟢 Adopt | Python    | ✅ Active | Physics Domain (Dice, AI)              |
| [warscribe-system](https://github.com/vindicta-platform/warscribe-system)       | 🟢 Adopt | Python    | ✅ Active | Scribe Domain (Notation, Parser)       |
| [vindicta-economy](https://github.com/vindicta-platform/vindicta-economy)       | 🟡 Trial | Python    | ✅ Active | Economy Domain (Ledger, Quotas)        |
| [vindicta-oracle](https://github.com/vindicta-platform/vindicta-oracle)         | 🟡 Trial | Python    | ✅ Active | Oracle Domain (AI Council)             |
| [vindicta-agents](https://github.com/vindicta-platform/vindicta-agents)         | 🟢 Adopt | Python    | ✅ Active | Agent SDK & Swarm Orchestration        |

### Archived & Superseded

| Repository                                                                | Ring   | Language | Status     | Notes                                   |
| ------------------------------------------------------------------------- | ------ | -------- | ---------- | --------------------------------------- |
| [Vindicta-Portal](https://github.com/vindicta-platform/Vindicta-Portal)   | 🔴 Hold | HTML/JS  | ☠ Archived | Consolidated into `vindicta-platform`   |
| [Vindicta-API](https://github.com/vindicta-platform/Vindicta-API)         | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-platform`   |
| [Vindicta-CLI](https://github.com/vindicta-platform/Vindicta-CLI)         | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-platform`   |
| [Dice-Engine](https://github.com/vindicta-platform/Dice-Engine)           | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-engine`     |
| [Entropy-Buffer](https://github.com/vindicta-platform/Entropy-Buffer)     | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-engine`     |
| [Primordia-AI](https://github.com/vindicta-platform/Primordia-AI)         | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-engine`     |
| [WARScribe-Core](https://github.com/vindicta-platform/WARScribe-Core)     | 🔴 Hold | Python   | ☠ Archived | Consolidated into `warscribe-system`    |
| [WARScribe-Parser](https://github.com/vindicta-platform/WARScribe-Parser) | 🔴 Hold | Python   | ☠ Archived | Consolidated into `warscribe-system`    |
| [Economy-Engine](https://github.com/vindicta-platform/Economy-Engine)     | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-economy`    |
| [Meta-Oracle](https://github.com/vindicta-platform/Meta-Oracle)           | 🔴 Hold | Python   | ☠ Archived | Consolidated into `vindicta-oracle`     |
| [Platform-Docs](https://github.com/vindicta-platform/Platform-Docs)       | 🔴 Hold | MkDocs   | ☠ Archived | Consolidated into `vindicta-foundation` |
| [platform-core](https://github.com/vindicta-platform/platform-core)       | 🔴 Hold | Python   | ☠ Archived | Superseded by modular architecture      |

---

## Planned Evolution

| Change               | Target Phase | Description                                                          |
| -------------------- | ------------ | -------------------------------------------------------------------- |
| Structurizr Lite     | V1.2         | Interactive local architecture exploration via Docker                |
| Auto-discovery CI    | V2           | GitHub API job auto-detects new repos and validates DSL completeness |
| GCP deployment views | V3           | C4 Level 4 code diagrams + Cloud Run / GCS deployment architecture   |

---

*Last updated: 2026-02-12 — Validated against GitHub org API via CI.*
