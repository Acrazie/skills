# GitHub.com administration

Use this mode for repository settings or personal Developer Settings, not project scaffolding. Read [github-settings.md](github-settings.md) for the repository coverage catalog and [developer-settings.md](developer-settings.md) for App and PAT lifecycles. These rules also govern remote settings changed during initialization. Engineering activation remains a separate, preservation-focused workflow.

## 1. Resolve the target and discover read-only

Identify GitHub.com, the authenticated acting user, resource owner and exact repository, App registration, installation or token metadata. Personal Developer Settings need no local checkout. A repository may belong to an organization, but organization-wide changes are excluded. Confirm ambiguous identities before reads; never infer that the authenticated account owns the resource. Reject Enterprise Server in this mode; do not silently switch hosts or accounts.

Discover only facts relevant to the request using available purpose-built connectors, verified CLI/API reads or a connected browser. Use explicit GET requests and read-only GraphQL queries. Do not execute mutations, install tools, reauthenticate, expand scopes, write reports/configuration files or create resources during discovery. An invocation or matching task authorizes scoped reads, not a permanent account-wide audit. Never dump credentials, tokens, secret/variable values, private keys, credential-bearing URLs, raw configuration or unfiltered API responses. Select safe metadata fields before displaying tool output; if a read cannot avoid exposing secrets, use user-operated inspection instead. Redact sensitive webhook/callback URLs.

Establish role, credential type and effective permissions without revealing credentials. Explicitly distinguish App registration, installation and user authorization grants before proposing App changes; a grant not needed for the requested flow is not applicable, not silently conflated with installation. Distinguish registration ownership, repository administration, App installation permissions, user authorization and workflow token permissions. Organization policies and managed-account restrictions may constrain a personal action without granting authority to change them. Denied access is a blocker, not consent to request broader access.

Refresh each relevant settings family's current official GitHub.com documentation at use time. Use Context7 for documentation discovery when available and verify API methods/payloads against the official endpoint documentation, not generated examples. A GET field does not imply a writable field. Record source/date, host, available method and prerequisites. New or renamed UI families must enter the inventory as documented, manual or unverified rather than disappear from coverage. Do not hardcode token lengths, endpoint availability or assumptions from screenshots.

## 2. Inventory and interview only unresolved decisions

Use a compact inventory with one row per relevant setting/resource:

| Field | Required evidence |
|---|---|
| Target | Host, acting account, resource owner, stable resource identity |
| Current state | Safe observed metadata and source, or inaccessible/unverified |
| Proposed action | Exact create/update/rotate/revoke/delete operation and desired non-secret values, or preserve/defer |
| Capability | Verified connector/CLI/API, guided manual step, unavailable, or inaccessible/unverified |
| Prerequisites | Authority, plan, inherited constraints, dependency and possible cost |
| Consequences | Access, exposure, disruption, consumers and irreversible effects |
| Verification | Safe readback or user-operated observation, separate from runtime proof |

Survey the coverage catalog for relevance without interrogating the user about every toggle. Ask the whole current decision frontier, with numbered options and one contextual recommendation; prune choices already explicitly supplied. Preserve unrelated configuration. Never equate a 403/404, omitted field or unsupported connector with a disabled feature. Confirmed unavailable requires evidence about host/plan/context; manual means a documented human route exists, not that it has been completed.

## 3. Obtain approval before every mutation

Present an enumerated action plan and stop. Each item identifies exact target, current/proposed state, operation, prerequisites, cost, consequences, dependencies and verification. Include local artifact writes or external setup if needed; generating a manifest is not implicit permission to register an App. Separate recommendations from executable actions.

The user may approve individual items or a finite, explicitly listed batch. Blueprint approval counts only if it explicitly covers that precise batch; a generic request to configure, a recommendation, a permission label, available credentials or a repository's delivery preauthorization does not authorize mutations. No permanent grant or new action can be inferred. Resolve ambiguous acceptance rather than selecting an alternative silently. Sensitive and destructive effects must be clearly disclosed in the approved item; approval of creation never covers later deletion.

Before each approved operation, recheck target identity and relevant preconditions. Use conditional updates where the documented surface supports them. If an observed value, permission, consumer set or cost materially differs, pause the affected action and obtain renewed approval. Never overwrite concurrent changes by replaying a stale batch. Approval does not bypass platform permissions or organization restrictions.

## 4. Execute the bounded batch and verify

Use only documented methods and approved fields in dependency order. Preserve unrelated values; never generate a catch-all privileged setup script. Browser actions obey the same gates as API actions. Credential-producing/revealing steps are user-operated in the official UI or an approved secure channel, never captured in agent screenshots, tool output, files, logs or chat. Do not ask users to paste secrets. The skill documents destinations and secret names, not values; it does not collect or copy secrets.

After each operation, read back effective non-secret state. A response code, a YAML file or a browser click alone is not proof of applied configuration. For write-only secrets, verify only metadata and separately authorized consumer checks; a secret cannot be recovered for comparison. Manual actions remain pending until safely confirmed by the user or observed metadata. Label user-reported evidence as such.

For credential rotation, identify affected consumers and sequence creation, secure provisioning, verification and revocation where supported. Do not revoke the old credential before the approved replacement is verified unless the user explicitly chooses emergency revocation and accepts disruption. Never run a production test or deployment by implication. If safe verification requires additional authority or an external mutation, request its own approval.

On failure, stop dependent operations and report completed, failed, unverified and not-attempted items. Continue only independent actions still covered by the batch and unchanged preconditions. No silent retries with broader scopes, weakened protections, rollback over concurrent edits or compensating mutations. Recovery/rollback is another proposed action unless already explicitly enumerated and approved. Irreversible deletion and immutable release effects must not be presented as recoverable.

## 5. Report without overclaiming

Report exact non-secret targets and approved items, applied-and-verified, applied-but-unverified, preserved, failed, manual-pending and deferred states. Separate documentation research, settings readback, user-reported evidence, local tests and actual consumer/workflow execution. Include remaining user/admin actions and capability gaps. Do not claim all settings were inspected or all integrations work from an incomplete inventory.

## Boundaries

Exclude Enterprise Server; personal profile, login/2FA, billing and unrelated account settings; organization/enterprise-wide administration; continuous monitoring; App/backend implementation; unsolicited stack/governance changes; Git shipping, merging and deployment. Repository settings with billing consequences may be discussed but cannot cause a plan purchase or account billing change by implication. Installed third-party Apps are not owned registrations. OAuth authorization grants are not OAuth App registrations. Changing either resource requires its own identified target and approval.
