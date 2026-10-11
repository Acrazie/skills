# CI/CD Decision Frontier

Reuse current independently approved decisions. Display only localized Current
state, numbered Options, Recommendation and Response. Discover facts yourself;
ask only decisions with settled prerequisites. No fixed questionnaire.

1. Determine create/modernize/diagnose and CI-only/publication/delivery/deployment.
2. Establish event/source trust, commands with provenance and verified runners.
3. For publication: immutable identity, output/registry, provenance and overwrite rules.
4. For delivery: requested environments, same-artifact promotion and interfaces.
5. For deployment: environment authority, approver, verification, known-good rollback,
   concurrency/staleness and timeout policy; data-changing rollback needs its own effects.
6. For remote work: exact target, submitted data, effects, validation/read-back and
   validity of the separately approved envelope. Plan approval never activates it.

Unknown tool-specific facts require actual configuration/docs, not a Jenkins-like
assumption. Non-applicable branches stay absent. If one branch is blocked, independent
safe discovery may continue. Summarize exact edits and allowed checks before realization.
