# Vindicta Foundation

> **Status:** reference implementation of the shared kernel (base models, constitution docs) for the Vindicta design record; maintained for reading, not for new features. Single maintainer.

> 📢 **Notice:** This repository is a Component Submodule of the Vindicta Platform Monorepo. For local development, testing, and dependency resolution, please clone the root [vindicta-platform](https://github.com/vindicta-platform/vindicta-platform) repository.


The **central hub** and **core pillar** of the [Vindicta Platform](https://github.com/vindicta-platform). This repository provides the axiomatic base models, shared kernel logic, and constitutional documentation that all other Vindicta microservices, agents, and clients depend upon.

---

## Installation

```bash
uv sync
```

## Features

- **VindictaModel**: Pydantic V2 base model for all entities.
- **EntropyProof**: Cryptographic verification for random events.
- **GasTankState**: Economic state tracking.

## Testing & Coverage

```bash
uv run pytest --cov
uv run behave
```
Coverage Mandate: ≥90%

## Docs

- [⚖️ The Constitution](docs/constitution.md): The supreme law and Zero-Order Axioms.
- [🏗️ ADRs](docs/architecture/adr/): Architectural Decision Records.
- [🗺️ C4 Models](docs/architecture/C4-Target-State.md): System architecture diagrams.
- [📚 Core Concepts](docs/concepts/): Deep dives into WARScribe and platform logic.

## Independence

This is a personal project by Brandon Fox, built on my own time and equipment. It is not affiliated with, endorsed by, or derived from the work of any employer, current or former, and does not represent their views, products or practices. Licensed under the MIT License; principles at [First-ADE/PRINCIPLES.md](https://github.com/First-ADE/.github/blob/main/PRINCIPLES.md).
