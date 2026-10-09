# Personal Developer Settings on GitHub.com

Use with [github-administration.md](github-administration.md). Cover configuration and lifecycle, not implementation of App code or universal API automation. Account ownership and effective permissions must be verified; personal Developer Settings can be managed without a repository checkout. Organization-owned App registrations and organization token policies are outside personal administration, but may constrain repository integrations.

## Distinct resources

- **GitHub App registration**: owned App definition, permissions/events, callback and webhook configuration, distribution, credentials and lifecycle.
- **GitHub App installation**: access granted to an account/repository selection. Separate from registration and App user authorization; changes may require installation-owner/admin approval.
- **OAuth App registration**: owned application identity and callback configuration. Separate from user OAuth authorization/token grants and third-party applications.
- **PAT**: user credential bounded by the user's actual rights and applicable policy, not a way to acquire repository administration.

Before proposing App changes, explicitly distinguish registration, installation and user authorization in the inventory; mark a user authorization grant not applicable when no user access is requested. Audit safe metadata, permissions, repository selection, expiration, consumers and known usage before recommending changes. Prefer fine-grained PATs when current documented limitations permit; compare a GitHub App for durable automation rather than assuming a classic PAT is necessary. Explain permission and credential-lifetime tradeoffs. Never invent consumer usage or last-used evidence where unavailable.

## GitHub Apps

Inventory owned registrations, identity, URLs, callback/redirect settings, webhook enablement/events, permissions, installation scope and visibility/distribution options as exposed by current documentation. Identify which fields require UI, have a documented API, or are unverified. Treat permission expansion and installation selection as access changes, not routine metadata edits. Existing installations may require owner approval for updated permissions; configuration of the registration does not prove effective installation access.

Registration through the official UI or manifest flow includes human participation. A manifest may prefill reviewed non-secret configuration but is not blanket authorization. Do not implement the callback service as part of settings management. The manifest handshake returns credentials including a private key, webhook secret and client secret: do not call its conversion endpoint through a tool that displays responses. Let the user complete credential-producing steps through a secure channel. An App ID/client ID is not a secret, but it is not permission to retrieve other credentials.

Support modification, credential rotation/revocation, suspension/uninstallation where documented, and registration deletion as separately approved operations. Identify installations and consumers before removal. Key or secret rotation needs secure provisioning and verified replacement before old-credential revocation where possible; a webhook secret change can disrupt deliveries. Do not claim uninstalling an App deletes its registration or revokes every separate authorization grant.

## OAuth Apps

Inventory owned registration identity, homepage/callback URLs, documented optional settings and credential metadata. Propose creation or changes via the documented UI or specifically verified API, never infer a registration API from token exchange endpoints. Generating a new client secret is user-operated; existing secret values must not be read or displayed.

Separate registration modification/deletion from revoking user grants or tokens. Verify the target and documented lifecycle effect before claiming a particular action revokes consumers. Review callback changes and impacted users; use overlap for rotation only when supported. OAuth flow implementation, consent interception and automated capture of authorization codes/tokens are excluded.

## Fine-grained PATs

Guide official personal Settings > Developer settings > Personal access tokens creation/edit/revocation using verified current documentation. Describe token purpose/name, resource owner, repository selection, account/repository permissions, expiration and possible organization approval/SSO restrictions. A prefilled URL may encode only approved non-secret choices; it is not token creation. Generate it only as an approved artifact, and never embed credential values.

A pending organization approval is not effective access; do not automatically switch to a classic PAT to bypass policy. Respect current fine-grained feature limitations and explicitly explain unsupported operations. User generates, stores and provisions the token through a secure channel. Verify metadata and an explicitly authorized minimal consumer check, never inspect the token value. Rotation normally creates a replacement; use documented lifecycle options, not an assumed in-place refresh.

## Classic PATs

Guide creation, scopes, expiration, regeneration and deletion through current documented UI. Explain broader scope and organization/SSO constraints, and justify classic only when a verified requirement cannot use a safer compatible alternative. Regeneration may invalidate the existing value; do not call it zero-downtime rotation. Propose a separate replacement credential where necessary and supported. No invented generic PAT creation REST endpoint, credential printing, or automatic scope expansion.

## Secure human handoff

Present the approved non-secret parameters, official destination, expected safe metadata and affected consumers. Ask the user to complete credential-producing/revealing screens outside agent observation, then return only confirmation or non-secret identifiers. Do not capture those screens or ask for attachments of them. Browser automation may manage safe non-secret settings only after approval; uncertainty about a screen's secret contents requires handing that step to the user.

Never treat a manual instruction as executed. If verification is blocked, report pending/unverified and defer dependent revocation. Emergency revocation may precede replacement only with explicit acceptance of disruption. Tokens/private keys/client and webhook secrets never belong in skill examples, task records, PRs, screenshots or source control. Provisioning into a secret store remains user-operated or a separately approved secure workflow, not an invitation to paste a secret into a tool call.

## Official sources

Documentation researched on 2026-10-09; refresh relevant pages at use time. Context7 is a discovery aid, not authority for invented endpoint snippets.

- [Registering a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app)
- [GitHub App manifest flow](https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-from-a-manifest)
- [Modifying a GitHub App registration](https://docs.github.com/en/apps/maintaining-github-apps/modifying-a-github-app-registration)
- [Managing GitHub App private keys](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps)
- [Installing GitHub Apps](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app)
- [Creating an OAuth App](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)
- [Maintaining OAuth Apps](https://docs.github.com/en/apps/oauth-apps/maintaining-oauth-apps)
- [Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [Apps REST API](https://docs.github.com/en/rest/apps)
