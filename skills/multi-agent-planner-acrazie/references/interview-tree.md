# Interview tree

Use this map as decision dependencies, not as a fixed questionnaire. Skip anything already explicit or discoverable from the environment.

## 1. Establish facts first (never ask)

Inspect before asking:

- repository roots, languages, manifests, test setups, current Git state;
- approximate file counts and subsystem boundaries;
- existing central specs, ADRs, or shared conventions;
- whether the current platform supports workers at all.

Unknown facts remain unknown. Do not turn them into user decisions.

## 2. Root decisions (round 1)

Ask only unresolved items. Each question carries 2-3 options plus one recommendation with its reason.

- **Goal:** What decision or artifact should exist afterward?
- **Perimeters:** Which repos, subsystems, or file sets are central, and which are adjacent?
- **Independence:** Can slices run without reading each other's output, or do they share contracts?
- **Risk and budget:** What dominates — token cost, speed, coherence, or reversibility?

Round 1 normally suffices to rule single vs multi. Propose the verdict as one of the options where it helps.

## 3. Dependent decisions (round 2, only when unblocked)

- Worker split: by repository, by module, or by independent lead — only after independence is known.
- Coherence mechanism: central spec first, reconnaissance first, or direct fan-out — only after dependencies are known.
- Verification path: which handle proves each worker's success — only after the split is known.
- Platform target: where the workflow will run — only when spawn syntax matters.

## 4. Rounds

Ask the whole current frontier in one numbered round. Every question: 2-3 labelled options, then exactly one recommendation and why it fits this case.

A second round is warranted only when round-1 answers unblock a material dependent decision. Do not interview past the stop criterion in SKILL.md.

## 5. Shared-understanding checkpoint

The frontier is empty when verdict, split, and contracts are settled, excluded, or blocked by a disclosed fact gap. Summarize:

1. verified facts;
2. verdict and rejected alternative;
3. workflow architecture and phases;
4. worker split and contracts;
5. coherence mechanism when needed;
6. assumptions under fast path.

Wait for explicit confirmation before presenting the final deliverable as done.
