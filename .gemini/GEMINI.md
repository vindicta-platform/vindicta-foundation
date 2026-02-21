### Vindicta Foundation Workspace Rules

1. **Dual Constitution Hierarchy**:
    - **Tier 1 (Foundation Law)**: All architectural models and universal definitions must adhere to the **Zero-Order Axioms** defined in `docs/constitution.md`.
    - **Tier 2 (Builder Law)**: Specification generation, implementation rules, and agent workflows strictly rely on `# Project Constitution` in `.specify/memory/constitution.md`, which inherently adheres to Tier 1.
2. **Structural Integrity**:
    - Every domain model MUST inherit from `VindictaModel` in `src/vindicta_foundation/models/base.py`.
    - New models must be explicitly exported in `src/vindicta_foundation/models/__init__.py`.
3. **Meso-Repo Consolidation**:
    - Follow the consolidation tactics in `docs/architecture/adr/0006-consolidation-tactics.md` when porting code from other repositories.
    - Legacy code must be audited against the **Vindicta Axioms** before integration.
4. **Architecture Documentation**:
    - Update the **C4 Model** in `docs/architecture/c4-model.md` when changing container boundaries.
    - Standardize new ADRs using the `docs/architecture/adr/_0000-template.md` and follow the `XXXX-title.md` naming convention.
    - Always verify documentation with `uv run mkdocs build --strict` after any change to the `docs/` directory.
5. **Quality Mandates**:
    - **Coverage**: Minimum 90% test coverage required. Verify with `uv run pytest`.
    - **Types**: Strict type checking with `mypy` is mandatory.
    - **Linting**: All code must pass `ruff` checks.
6. **Speckit Integration & Workflows**: Utilize the IDE slash commands defined in `.agent/workflows/` (e.g., `/speckit-plan`, `/speckit-tasks`) for complex tasks like task extraction, planning, and implementation. Do not attempt to manually reference or run `.gemini/commands/*.toml` configuration files.
7. **Workflow Namespacing**: The `speckit-` prefix in `.agent/workflows/` is a **strict namespace** reserved exclusively for Speckit configurations. Other workflows must either be namespace-free (e.g., `pr.md`) or use appropriate custom namespaces for logical grouping.
8. **Pull Request Formatting**: You must NEVER use inline `--body` flags with `gh pr create` or `gh pr edit`. You MUST ALWAYS generate a properly formatted markdown file (e.g., `PR_BODY.md`) and use the `--body-file` flag to ensure high-quality, template-driven documentation. Clean up the body file immediately after execution.
