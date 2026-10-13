# Modernization ADR Template

Use an ADR when repository policy requires it or an approved durable, non-obvious architectural trade-off among genuine alternatives needs recording. A tier number alone does not require an ADR. Obtain content/destination approval; when required, prepare the ADR before validation and include it in the corresponding authorized commit. Follow the repository's naming
convention; otherwise use `docs/adr/` with the next unused identifier. Record actual
approval, sources and outcomes; the template grants no consent and predeclares no
check successful. Apply [portable-practice.md](portable-practice.md).

```markdown
# <Identifier> — <Modernization decision>

- Date: <actual decision date>
- Status: <proposed or evidenced approval>
- Pillar / tier: <approved scope>

## Context
<Observed versions, constraints and demonstrated problem. Source locators,
version applicability and verification date for changing claims. Unknowns separate.>

## Decision and alternatives
<Approved source-to-target path, including maintaining the incumbent as an
alternative; reasons for choosing or rejecting each viable path. Approval evidence.>

## Consequences
<Expected benefits, costs, capability parity, compatibility constraints and risks.
Numerical benefits only if supported by representative project measurements.>

## Evidence
<Checks planned versus actually executed, commands, results and exact content
validated. Initially pending; do not prefill green checks or checkpoint SHAs.>

## Limits
<Unverified or contradictory facts, dependent steps blocked, residual risks,
checks not run and scope of local versus live evidence.>
```
