# GitHub administration skill update — approved contract

Approved on 2026-10-09 through the grill-with-docs interview. Owner: `github-repo-init-acrazie`.

## Scope and decisions

Add a third mode for GitHub.com repository settings and personal Developer Settings: GitHub Apps, OAuth Apps, fine-grained and classic PATs. Preserve initialization and engineering activation. Support inventory, contextual recommendations, creation/configuration, modification, credential rotation, revocation and deletion with documented automated or guided manual routes. Personal Developer Settings need no local repository. Organization-owned repositories are included within effective authority; organization-wide administration is excluded.

Invocation permits relevant read-only discovery. Every mutation, including ordinary settings, requires prior user approval of its exact action, target, proposed values and consequences. Approval may cover a finite enumerated batch, not permanent autonomy. Changed preconditions or new items require renewed approval. Credential-producing steps remain user-operated through a secure channel; no secrets in chat, documentation, logs, screenshots or Git. Reverify each operation and report partial or unverified results truthfully.

Exclude Enterprise Server, other personal settings, organization/enterprise-wide administration, continuous monitoring, App code implementation, Git shipping, merging and deployment. No real GitHub settings or credentials may be changed to validate this update.

## Acceptance and proof

1. Entry instructions and metadata route all three modes without forcing scaffolding.
2. Repository catalog covers all Settings families with dated official discovery sources, contextual relevance and explicit unknown/manual states; it does not claim every toggle is automated.
3. Developer Settings reference distinguishes registration, installation, authorization and credentials, with safe human handoff and lifecycle sequencing.
4. Exact prior approval covers every mutation; drift, costs, destructive effects and recovery cannot bypass that gate.
5. Glossary and boundary ADR capture the approved terminology and ownership tradeoff.
6. Structural checks, offline engineering activation regression tests and targeted simulated scenarios provide bounded evidence. No live account administration, PAT generation or browser integration is claimed.

## Delivery evidence

- Repository frontmatter and structure hooks: passed.
- YAML syntax and invocation metadata parity: passed using Ruby/Psych (PyYAML is not installed).
- Scenario JSON IDs, local links in changed Markdown and unchanged engineering helper/reference checks: passed.
- Existing offline engineering activation suite: 33 tests passed; no helper code changed.
- Three fresh-context simulated administration scenarios: initial new responses 12/13 assertions versus unchanged baseline 10/13; after clarifying user authorization and Planning/Copilot ownership, final responses 13/13. Initial baseline was not rerun. Grading is text-based, not live integration proof; no performance claim.
- Simulation outputs, grading and generated review viewer remain ignored under the worktree's `.skill-improver/admin-eval/`, not published skill artifacts.
- Site invocation test attempted but blocked before execution by missing `gray-matter` in this fresh worktree. No dependency installation or replacement parser was performed; targeted metadata checks do not replace that suite.
- No real GitHub settings, accounts, Apps or credentials were changed. Installed/global skill links remain unchanged; no live browser/account behavior is verified.
