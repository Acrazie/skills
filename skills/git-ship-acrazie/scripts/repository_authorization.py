"""Evaluate repository action policy against independently established evidence.

This helper never executes Git/check commands or establishes consent itself.
Observation inputs must come from the caller's real approval and snapshot proof.
"""

import argparse
import json
from pathlib import Path

ACTIONS = {"stage", "commit", "push", "pr_create", "pr_update", "merge", "deploy"}


def no_duplicates(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("Duplicate JSON key")
        value[key] = item
    return value


def decision(policy, action, observed):
    def result(mode, reason):
        return {"mode": mode, "reason": reason}

    if not isinstance(action, str) or action not in ACTIONS or not isinstance(observed, dict):
        return result("blocked", "Invalid action or observation")
    restrictions = observed.get("restrictions", [])
    if not isinstance(restrictions, list) or any(not isinstance(x, str) or x not in ACTIONS for x in restrictions):
        return result("blocked", "Invalid current restrictions")
    if action in restrictions:
        return result("forbidden", "Current restrictive instruction prevails")
    if policy is None:
        return result("confirm", "No repository action configuration")
    if not isinstance(policy, dict) or type(policy.get("schema_version")) is not int or policy["schema_version"] != 1:
        return result("blocked", "Unsupported policy schema")
    fields = {"schema_version", "source_revision", "installer_version", "hosts", "skills", "permissions", "policy_sources"}
    if set(policy) not in (fields, fields | {"_managed"}):
        return result("blocked", "Unknown or incomplete policy fields")
    rules = policy.get("permissions")
    if not isinstance(rules, dict) or set(rules) != ACTIONS:
        return result("blocked", "Incomplete action policy")
    for rule in rules.values():
        if not isinstance(rule, dict) or not isinstance(rule.get("mode"), str) or rule["mode"] not in {"forbidden", "confirm", "preauthorized"}:
            return result("blocked", "Invalid action mode")
        if rule["mode"] != "preauthorized":
            if set(rule) != {"mode"}:
                return result("blocked", "Unknown action fields")
            continue
        if set(rule) != {"mode", "repository", "branches", "destinations", "checks"} or not isinstance(rule["repository"], str) or not rule["repository"].strip():
            return result("blocked", "Incomplete preauthorization scope")
        for field in ("branches", "destinations", "checks"):
            values = rule[field]
            if not isinstance(values, list) or not values or any(not isinstance(x, str) or not x.strip() or "\n" in x or "\x00" in x for x in values) or len(values) != len(set(values)):
                return result("blocked", "Invalid preauthorization conditions")
        if any(any(c in x for c in "*?[") for x in rule["branches"] + rule["destinations"]):
            return result("blocked", "Wildcard preauthorization is unsupported")
    rule = rules[action]
    if rule["mode"] == "forbidden":
        return result("forbidden", "Repository forbids this action")
    if observed.get("policy_unchanged") is not True:
        return result("blocked", "Policy drift or governance conflict unresolved")
    if rule["mode"] == "confirm" or observed.get("approval_evidenced") is not True:
        return result("confirm", "Explicit operation approval required")
    if (observed.get("repository") != rule["repository"] or
            observed.get("branch") not in rule["branches"] or
            observed.get("destination") not in rule["destinations"]):
        return result("confirm", "Operation falls outside the approved exact scope")
    snapshot, checks = observed.get("snapshot"), observed.get("checks")
    if not isinstance(snapshot, str) or not snapshot or not isinstance(checks, dict) or any(checks.get(command) != snapshot for command in rule["checks"]):
        return result("blocked", "Required proof is missing or belongs to another snapshot")
    return result("preauthorized", "Independent approval and scoped current proof supplied; no action executed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    parser.add_argument("--observation", type=Path, required=True)
    parser.add_argument("--action", choices=sorted(ACTIONS), required=True)
    args = parser.parse_args()
    try:
        if args.policy.is_symlink():
            raise ValueError("Policy symlinks are not an authoritative local source")
        policy = json.loads(args.policy.read_text(), object_pairs_hook=no_duplicates) if args.policy.exists() else None
        observed = json.loads(args.observation.read_text(), object_pairs_hook=no_duplicates)
        result = decision(policy, args.action, observed)
    except (OSError, ValueError) as error:
        result = {"mode": "blocked", "reason": str(error)}
    print(json.dumps(result))
    return 1 if result["mode"] in {"blocked", "forbidden"} else 0


if __name__ == "__main__":
    raise SystemExit(main())
