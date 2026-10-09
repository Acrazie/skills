# Explicit project kits and evidence-bound action preauthorization

On 2026-10-09, host documentation exposed a trade-off between conversation-level
confirmation and native explicit-only invocation. The user chose explicit skill
commands for Codex and Claude Code, including each dependency. This supersedes
the single-confirmation chain choice in
[ADR 0007](0007-confirmed-skill-chains-and-repository-bootstrap.md), not its
specialist-first routing, ownership boundaries or Repo Init bootstrap decision.

Project activation adapts selected copies to explicit-only metadata and provides
a metadata catalog for natural-language proposals before activation. Published
library defaults and global installations are unchanged. We accept extra manual
handoffs rather than imply a runtime guarantee for “yes, load the whole chain”.
Flags are not filesystem authorization; unresolved implicit-enabled global
homonyms block a claim of a strict project gate. Live host behavior is not verified
in this delivery, as the user selected automated tests only.

One tracked canonical copy and relative Claude links avoid duplicate packages.
Repo Init uses the pinned existing Skills CLI in external staging, then an
ownership-aware, reviewed plan instead of allowing the installer to overwrite the
target. The project tracks `.acrazie/engineering.json`, selected packages and a
merged lock. We preserve source hashes separately from adapted installed hashes,
and reject conflict or unexpected layout rather than silently switching to copies,
overwriting personalization or drifting versions.

Git Ship keeps action/snapshot recaps and safety proof, but may recognize an
independently evidenced, exact-scoped repository preauthorization instead of
requiring duplicate approval. Configuration existence and an approval label do
not establish consent. Current restrictions, unresolved policy changes and failed
or stale checks still block action. Merge/deployment remain outside Git Ship.
See the [implementation contract](../specs/engineering-bootstrap-implementation.md).
