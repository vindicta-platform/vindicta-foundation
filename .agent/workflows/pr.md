---
description: Generate a standardized Pull Request description and submit or update it via GitHub CLI.
---
1. **Local Pre-flight Checks**: Run `just prepush` (or explicitly run `uv run ruff format --check .`, `uv run ruff check .`, `uv run mypy src tests`, `uv run pytest`, and `uv run behave`) to assert that the PR will not fail CI checks. **Do not create a PR if these fail.**
2. **Analyze Diff**: Run `git log <base>..<head>` or `git diff <base>...<head>` to understand the full scope of changes made in the branch.
3. **Draft PR Body**: Create a local file named `PR_BODY.md`. It MUST contain the following sections formatted in Markdown:
    *   **Summary**: A high-level overview of the entire PR.
    *   **Changes**: A bulleted list of the specific files changed and what was done.
    *   **Why**: The root cause, business value, or technical reason for the change.
    *   **Verification**: How the changes were verified locally (e.g., test commands, manual inspections).
3. **Submit/Edit**: 
    *   If creating a new PR, run: `gh pr create --title "<Title>" --body-file PR_BODY.md`
    *   If updating an existing PR, run: `gh pr edit <PR_NUMBER> --title "<Title>" --body-file PR_BODY.md`
4. **Cleanup**: Remove the temporary `PR_BODY.md` file using native OS commands (e.g., `Remove-Item PR_BODY.md -Force`).
**CRITICAL RULE**: NEVER use the inline `--body` flag. Always use `--body-file`.
