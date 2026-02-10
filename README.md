> **Part of the [Vindicta Platform](https://github.com/vindicta-platform)**

# Vindicta Foundation

Shared core models, constitutional axioms, and architectural documentation for the Vindicta Platform.

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

- [ADRs](docs/architecture/adr/): Architectural Decision Records.
- [C4 Models](docs/architecture/C4-Target-State.md): System architecture diagrams.
