# Git/GitHub capability and settings discovery

A remote URL, governance files and workflow YAML do not configure GitHub access or repository settings. Inventory the relevant configuration families before the interview and include useful available choices in the blueprint. This is not authority to administer an organization or perform a general security audit.

## Establish context and available operations

Inspect repository identity/host, owner type, visibility, default branch, applicable instructions and effective organization/repository rules. Discover installed versions and supported commands with `git --version`, `git help config`, `gh --version`, `gh repo edit --help`, `gh api --help` and relevant subcommand help. Consult current official API schemas as well: CLI flags are not the entire GitHub settings surface. Verify host/API version compatibility, particularly on GitHub Enterprise Server. Prefer available purpose-built connectors when they expose the needed reads/settings.

Use read-only discovery. Inspect only relevant Git config keys with their origin/scope; never dump credentials, credential-bearing remote URLs, all config, tokens, secrets or variable values. Local choices may include initial branch, line-ending policy, signing requirements, hooks path and fetch/push behavior. Explain repository-local vs global config: do not alter user-global/system config or generate signing credentials by implication. Inspect the repository's effective caller role/permissions; authentication, collaborator access, API authorization and `GITHUB_TOKEN` scopes are separate layers. Do not print `gh auth token` or fetch credential values.

For an existing GitHub repository, verified read-only GET examples after resolving the actual owner/repository/host:

```bash
gh api --method GET repos/OWNER/REPO
gh api --method GET repos/OWNER/REPO/actions/permissions
gh api --method GET repos/OWNER/REPO/actions/permissions/workflow
gh api --method GET repos/OWNER/REPO/rulesets --paginate
```

Use the actual configured GitHub host (`--hostname` when needed), current documented endpoints and only necessary fields. Paginate list endpoints; inspect selected ruleset details, inherited rules and applicable branch protection rather than assuming a list is the full effective policy. Request other family-specific reads only when applicable and authorized. `gh api` is not read-only by default when fields imply POST: specify GET for discovery. GraphQL queries must be read-only queries, never mutations. Do not automatically request broader token scopes or bypass a denied read.

For a new remote, document prospective options and prerequisites before approval; actual settings/caller access remain pending until creation. For local-only mode, remote settings are not applicable. Missing `gh`/connector access does not prevent local discovery, but limits remote verification.

## Configuration coverage map

Inspect each family for relevance; expand details only where they apply. Discover additional relevant settings from current CLI/API documentation rather than treating this map as exhaustive.

| Family | Relevant options and dependencies |
|---|---|
| Identity/features | Visibility, default branch, description/topics/homepage, template mode, Issues, Discussions, Wiki, Projects, fork policy; implications and plan/owner limits |
| Human/app access | Effective caller role, collaborators/teams and inherited access, GitHub Apps, least privilege; separate read access from administrative mutation authority |
| Actions execution | Enablement, allowed actions/reusable workflows, fork PR policy, runner policies and retention; inherited org constraints, untrusted PRs and resource/billing implications |
| Workflow permissions | Repository/org token defaults, YAML workflow/job scopes, Actions PR creation/approval toggle; selected release automation prerequisites |
| Branch/tag governance | Effective rulesets and legacy protection, required checks/reviews, CODEOWNERS enforcement, signed commits, linear history, push/force-push/delete restrictions, bypass actors; feature/plan availability |
| Merge controls | Merge/rebase/squash availability, message defaults, auto-merge, merge queue, branch update and deletion controls; required reviews/checks remain enforced |
| Security/dependencies | Dependency graph, Dependabot alerts/security updates vs version-update configuration, code scanning, secret scanning/push protection and private reporting; availability, authority and possible paid licensing |
| Environments/deployment | Environments, required reviewers/wait rules/branch restrictions, runner or OIDC requirements, secrets/variables names and scopes only; no values, credentials or deployment without specific approval |
| Local Git | Scoped config and sources, initial branch, line endings, signing/hooks and fetch/push policy; keep repository policy portable, never change global config silently |

Prefer least-privilege Actions defaults and explicit job grants. CI generally needs `contents: read`; a release job may need `contents: write` and `pull-requests: write`. The repository API field `can_approve_pull_request_reviews` corresponds to allowing Actions to create and approve PRs; assess whether the selected automation needs it, not every workflow. Repository settings cannot loosen enforced organization restrictions. Fork and Dependabot events can further restrict tokens/secrets. Do not use `pull_request_target` with untrusted checkout to work around missing write permissions.

## Evidence and proposal

Record family/setting, observed value and source, availability, required authority/plan, recommendation and rationale, user's desired value or preserve/defer choice, mutation surface and readback proof. Keep these states distinct:

- **Inspected**: effective value verified, including enabled/disabled or inherited constraints.
- **Unavailable**: confirmed unsupported for this host/plan/context.
- **Inaccessible/unverified**: cannot read or availability is unknown. A 403/404, omitted field or missing endpoint does not prove disabled or unavailable; a 404 can mask insufficient access.
- **Deferred/not applicable**: intentionally not changed, including local-only or post-creation inspection.

Offer grouped relevant recommendations rather than an exhaustive toggle questionnaire. Keep unknowns visible; never promise all options were checked when evidence is incomplete. If a required setting cannot be established, mark the affected automation/configuration blocked while completing independent approved local work.

## Apply and verify only approved settings

The blueprint identifies proposed local and remote changes separately. Remote publication still requires its own approval. Immediately before sensitive changes, show exact repository, current/proposed values, required rights, access/security consequences and cost; obtain explicit approval. This includes visibility, collaborator/team/App access, protection/security changes, fork/Actions trust policy and paid features. Do not modify organization policy, expand credentials or add secret values by implication. For ordinary settings, execute only the precise changes already approved in the blueprint; newly discovered differences require renewed approval.

Use verified `gh repo edit` flags or documented API methods/payloads; do not invent writable counterparts for GET fields. Apply in dependency order (publish/inspect, required settings, automation), preserve unrelated values, and re-read effective settings after each mutation. On failure, stop dependent actions, report partial state and safe recovery; do not broaden privileges, weaken checks, retry different security settings or revert user changes without authorization. Avoid generating a privileged catch-all setup script.

Report remote settings applied-and-verified, unchanged, deferred and failed separately from local validation and actual CI/release execution. Local YAML and readback are not proof that a workflow ran successfully.

## Official discovery sources

- [Git config](https://git-scm.com/docs/git-config)
- [gh repo edit](https://cli.github.com/manual/gh_repo_edit), [gh api](https://cli.github.com/manual/gh_api)
- [Repository REST API](https://docs.github.com/en/rest/repos/repos)
- [Actions permissions REST API](https://docs.github.com/en/rest/actions/permissions)
- [Rulesets REST API](https://docs.github.com/en/rest/repos/rules)
- [GITHUB_TOKEN](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)

Repository and Actions permission documentation consulted on 2026-10-01. Re-verify documentation and effective host/plan behavior at use time.
