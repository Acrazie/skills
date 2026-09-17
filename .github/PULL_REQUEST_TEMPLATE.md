## Summary

Briefly explain the intent of this pull request, the target skill(s) involved, and any non-obvious design choices.

## Related Issue / Context

Closes #

## Type of Change

- [ ] New skill (`feat(<skill>): add ...`)
- [ ] Skill enhancement / behavior update (`feat(<skill>): update ...`)
- [ ] Bug fix / prompt correction (`fix(<skill>): ...`)
- [ ] Documentation / reference update (`docs(<skill>): ...`)
- [ ] Repository maintenance / tooling (`chore: ...`)

## Checklist & Invariants

- [ ] **Worktree Isolation**: All changes were developed and committed from an isolated worktree (`.worktrees/<branch>`).
- [ ] **Naming**: Skill directory and identifier end with `-acrazie`.
- [ ] **Hooks & Structure**: Changes pass `./scripts/hooks/validate-skills.sh` and `./scripts/hooks/check-skill-structure.sh`.
- [ ] **Hygiene**: No forbidden files staged (checked via `./scripts/hooks/check-forbidden-files.sh`).
- [ ] **Conventional Commits**: Commit messages follow Conventional Commits without co-author attributions.
