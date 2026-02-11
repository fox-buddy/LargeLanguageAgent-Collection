# AGENTS.md

Project-level operating guide for coding agents working in this repository.

## Scope
- Applies to the entire repository unless a deeper AGENTS.md overrides sections for a subdirectory.
- Direct user instructions always take precedence over this file.

## Mission
- Make the smallest safe change that solves the requested task.
- Preserve current behavior unless a behavior change is explicitly requested.
- Prefer maintainability and readability over cleverness.

## Environment
- OS/Shell: Windows + PowerShell.
- Keep paths Windows-compatible unless the task explicitly targets another platform.
- Do not assume network access; degrade gracefully if offline.

## Workflow
1. Read the request and restate assumptions briefly in your own words.
2. Inspect only the files needed to complete the task.
3. Implement minimal edits with clear intent.
4. Run targeted checks/tests for touched areas when available.
5. Report what changed, why, and any risks or follow-up actions.
6. Document a changeloc for each edit under /agentChangelog

## Code Change Standards
- Match existing style, naming, and architecture patterns.
- Avoid broad refactors unless requested or required for correctness.
- Add comments only when non-obvious logic needs explanation.
- Keep new dependencies to a minimum and justify them.
- Never include secrets, tokens, or machine-local credentials.

## File Editing Rules
- Modify only files relevant to the task.
- Do not rewrite generated files manually unless asked.
- Keep diffs focused; avoid unrelated formatting churn.
- If a file has ongoing unrelated edits, do not revert or clean them up unless asked.

## Review Expectations
When asked for a review:
- Prioritize bugs, regressions, correctness, security
- Provide findings ordered by severity with file and line references.
- Keep summaries short

## Communication Format
- Be concise and concrete.
- State assumptions and constraints explicitly.
- For substantial changes: provide a short summary, then key implementation details, then validation results.
- Include actionable next steps only when they are natural and useful.

## Escalation / Clarification
- Ask before destructive actions (e.g., deleting files, hard resets, schema drops).
- Ask when requirements are ambiguous and materially affect implementation.
- If blocked, provide best fallback and clearly state what is needed to proceed.

## Optional Repo-Specific Section (Customize Me)
Replace this section with project specifics:
- Build command:
- Test command:
- Lint/format command:
- Key directories:
- Definition of done:

