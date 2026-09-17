# Repository Governance & Rule Inspection

This document defines how `git-ship-acrazie` inspects the repository to discover delivery rules, branch policies, commit standards, and when to trigger the fallback to `github-repo-init-acrazie`.

---

## 1. Governance Discovery Order

When invoked, the skill inspects the repository in the following cascade:

1. **Authoritative Workflow Document**:
   - Check if `docs/git-workflow.md` exists.
   - If present, parse:
     - Default branch name (`main`, `master`).
     - Allowed branch prefixes (`feat/`, `fix/`, `chore/`, `docs/`, `refactor/`).
     - Commit format requirements (Conventional Commits, scope rules).
     - Co-author prohibition invariant.
     - Pre-commit quality gate command (e.g. `lefthook run pre-commit`, `pnpm test`, `uv run ruff check`).
     - PR template location and default state (`--draft`).
     - Autonomy boundaries.

2. **Agent Guidelines Entrypoint**:
   - If `docs/git-workflow.md` is not in the default location, check `AGENTS.md` (or `CLAUDE.md`).
   - Look for a link to an alternate workflow document (e.g. `docs/delivery.md`, `docs/development-workflow.md`).
   - If found, read that referenced document.

3. **Contribution Guidelines**:
   - If still not found, inspect `CONTRIBUTING.md` for documented git rules, branch models, and commit conventions.

---

## 2. Fallback to `github-repo-init-acrazie`

If neither `docs/git-workflow.md` nor equivalent documented rules exist on the repository:

1. **Do NOT guess or invent arbitrary rules**:
   - Do not assume branch naming conventions or commit formats without documented consensus.
2. **Halt and propose setup**:
   - Stop execution cleanly.
   - Inform the user:
     ```text
     ⚠️ Aucune règle de gouvernance Git trouvée sur ce dépôt (docs/git-workflow.md introuvable).

     Pour standardiser les branches, les conventions de commit, les quality gates et le template de PR, vous pouvez invoquer le skill parent :
     👉 /github-repo-init-acrazie
     ```
3. **Offer an Emergency Fast-Path (if user insists on shipping without full init)**:
   - If the user explicitly asks to bypass setup ("force commit", "just commit anyway"):
     - Apply minimal safe defaults:
       - Ensure not on `main`.
       - Conventional Commits without co-author.
       - Stage only modified tracked files.
       - Open Draft PR with a generic summary.
