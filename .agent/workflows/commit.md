---
description: Standardized way to sign and execute commits locally.
---

1. **Local Pre-flight Checks**: Run `just prepush` (or explicitly run `uv run ruff format --check .`, `uv run ruff check .`, `uv run mypy src tests`, `uv run pytest`, and `uv run behave`). **Do not commit code that fails these tests.**
2. **Atomic Context**: Only stage files that you explicitly modified using `git add <file>`. **NEVER use `git add .` or commit everything**.
3. **Commit Signature**: Run `git commit -m "<Conventional Commit Message>"`
    - If configured correctly, commits will be auto-signed via SSH. 
    - Message format: `type(scope): subject`.
4. **Push Local Changes**: `git push`
