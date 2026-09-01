# Adaptive audit interview tree

Use this map as decision dependencies, not as a fixed questionnaire. Skip anything already explicit or discoverable from the repository.

## 1. Establish facts first

Inspect before asking:

- repository root, instructions, current commit and working-tree state;
- target subsystem and its call sites or integration boundaries;
- languages, runtimes, frameworks, manifests, lockfiles, and installed versions;
- relevant configuration, scripts, tests, CI, benchmarks, and operational paths;
- `docs/audits/` or equivalent records, especially related `pending` audits;
- evidence needed to determine whether the initial question is precise enough.

Unknown facts remain unknown. Do not turn them into user decisions.

## 2. Root decisions

Ask only unresolved items:

- **Audit question:** Which concrete decision, integration, tool, stack choice, or subsystem should the audit resolve?
- **Desired outcome:** What decision should the user be able to make afterward?
- **Scope boundary:** Which part of the single repository is central, and which adjacent parts may be needed to prove the answer?
- **Decision criteria:** Which project-specific constraints dominate, such as compatibility, performance, developer experience, operational simplicity, migration cost, or reversibility?
- **Change tolerance:** Is the user open to replacement, incremental improvement, or validation of the current choice?

Do not offer a general audit. If no focus exists, use preliminary inspection to propose a few concrete audit questions and wait for the user's selection.

## 3. Dependent decisions

Activate only after prerequisites settle:

- choose comparison dimensions after desired outcome and constraints are known;
- choose validations after the disputed behavior or claim is known;
- resolve a related pending Audit Record after overlap and evidence freshness are known;
- ask permission to enter another subsystem only after evidence shows it can materially change the answer;
- decide whether to resume, supersede, or link an old audit only after comparing its scope and repository state.

Do not ask the user which files, versions, commands, plugins, or framework capabilities exist when these can be inspected or researched.

## 4. Rounds

Ask the whole current frontier in one numbered round. Give a recommended answer and short repository-specific reason for every question.

Normally one round should settle the contract. A second round is warranted only when answers unblock a material dependent decision. Do not continue interviewing for completeness after the audit decision is clear.

## 5. Shared-understanding checkpoint

The frontier is empty when every relevant decision is settled, excluded, or blocked by a disclosed fact gap. Summarize:

1. verified facts;
2. audit question and intended decision;
3. central and adjacent scope;
4. comparison criteria;
5. exclusions;
6. related Audit Records and intended treatment;
7. permitted validations and forbidden side effects.

Wait for explicit confirmation before deep investigation.
