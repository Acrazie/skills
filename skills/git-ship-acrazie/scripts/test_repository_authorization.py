"""Policy eligibility tests, not live shipping or authorization-discovery tests."""

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("repository_authorization.py")
spec = importlib.util.spec_from_file_location("authorization", SCRIPT)
authorization = importlib.util.module_from_spec(spec)
spec.loader.exec_module(authorization)


class AuthorizationTests(unittest.TestCase):
    def setUp(self):
        self.policy = {
            "schema_version": 1, "source_revision": "a" * 40, "installer_version": "1.7.2",
            "hosts": ["codex", "claude-code"], "skills": ["git-ship-acrazie"], "policy_sources": {},
            "permissions": {name: {"mode": "confirm"} for name in authorization.ACTIONS},
        }
        self.policy["permissions"]["commit"] = {"mode": "preauthorized", "repository": "https://github.com/example/project", "branches": ["codex/search"], "destinations": ["local"], "checks": ["python3 -m unittest"]}
        self.observed = {"repository": "https://github.com/example/project", "branch": "codex/search", "destination": "local", "snapshot": "tree:123", "approval_evidenced": True, "policy_unchanged": True, "restrictions": [], "checks": {"python3 -m unittest": "tree:123"}}

    def mode(self, action="commit", policy=None, observed=None):
        return authorization.decision(self.policy if policy is None else policy, action, self.observed if observed is None else observed)["mode"]

    def test_no_policy_requires_confirmation(self):
        self.assertEqual(authorization.decision(None, "commit", self.observed)["mode"], "confirm")

    def test_valid_scoped_preauthorization(self):
        self.assertEqual(self.mode(), "preauthorized")

    def test_commit_does_not_bundle_stage_push_or_pr(self):
        for action in ("stage", "push", "pr_create", "pr_update", "merge", "deploy"):
            self.assertEqual(self.mode(action), "confirm")

    def test_forbidden_is_not_overridden_by_approval(self):
        self.policy["permissions"]["commit"] = {"mode": "forbidden"}
        self.assertEqual(self.mode(), "forbidden")

    def test_restrictive_current_instruction_prevails(self):
        self.observed["restrictions"] = ["commit"]
        self.assertEqual(self.mode(), "forbidden")

    def test_configuration_is_not_evidence_of_approval(self):
        self.observed["approval_evidenced"] = False
        self.policy["_managed"] = {"approval": "approved"}
        self.assertEqual(self.mode(), "confirm")

    def test_policy_drift_blocks_even_confirm_mode(self):
        self.observed["policy_unchanged"] = False
        self.assertEqual(self.mode(), "blocked")
        self.assertEqual(self.mode("push"), "blocked")

    def test_exact_identity_branch_destination_scope(self):
        for field in ("repository", "branch", "destination"):
            observed = copy.deepcopy(self.observed)
            observed[field] = "different"
            self.assertEqual(self.mode(observed=observed), "confirm")

    def test_snapshot_change_invalidates_check(self):
        self.observed["snapshot"] = "tree:456"
        self.assertEqual(self.mode(), "blocked")

    def test_missing_proof_blocks(self):
        for field in ("snapshot", "checks"):
            observed = copy.deepcopy(self.observed)
            del observed[field]
            self.assertEqual(self.mode(observed=observed), "blocked")

    def test_incomplete_invalid_or_unknown_policy_blocks(self):
        cases = [True, {"schema_version": 2}, {**self.policy, "allow_all": True}]
        bad = copy.deepcopy(self.policy)
        del bad["permissions"]["stage"]
        cases.append(bad)
        for bad in cases:
            self.assertEqual(self.mode(policy=bad), "blocked")

    def test_nonscalar_modes_and_restrictions_fail_closed(self):
        self.policy["permissions"]["commit"]["mode"] = {}
        self.assertEqual(self.mode(), "blocked")
        self.observed["restrictions"] = [{}]
        self.assertEqual(self.mode(), "blocked")

    def test_wildcard_conditions_block(self):
        self.policy["permissions"]["commit"]["branches"] = ["*"]
        self.assertEqual(self.mode(), "blocked")

    def test_observation_cannot_invent_action(self):
        self.assertEqual(self.mode(action="force_push"), "blocked")

    def test_duplicate_keys_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"permissions":{},"permissions":{}}', object_pairs_hook=authorization.no_duplicates)

    def test_cli_returns_eligibility_not_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            policy, observed = root / "policy.json", root / "observed.json"
            policy.write_text(json.dumps(self.policy))
            observed.write_text(json.dumps(self.observed))
            command = [sys.executable, str(SCRIPT), "--policy", str(policy), "--observation", str(observed), "--action", "commit"]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["mode"], "preauthorized")
            self.policy["permissions"]["commit"] = {"mode": "forbidden"}
            policy.write_text(json.dumps(self.policy))
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(set(p.name for p in root.iterdir()), {"policy.json", "observed.json"})


if __name__ == "__main__":
    unittest.main()
