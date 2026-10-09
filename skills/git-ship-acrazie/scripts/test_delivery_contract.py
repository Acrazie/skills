"""Static instruction-contract checks, not live agent or GitHub behavior tests."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DeliveryContractTests(unittest.TestCase):
    def setUp(self):
        self.main = (ROOT / "SKILL.md").read_text()
        self.refs = {p.stem: p.read_text() for p in (ROOT / "references").glob("*.md")}

    def require(self, text, *terms):
        for term in terms:
            self.assertIn(term, text)

    def test_action_scope(self):
        self.require(self.main, "commit-only", "separate authorization", "Never include `Co-authored-by:`")

    def test_adaptive_policy(self):
        self.require(self.refs["inspection"], "inaccessible", "Conventional Commits only", "no mandatory initialization", "protected")
        self.assertNotIn("Emergency Fast-Path", self.refs["inspection"])

    def test_freshness_boundaries(self):
        self.require(self.refs["pre-flight"], "Before each mutation", "HEAD", "index", "remote", "configuration", "material")

    def test_exact_snapshot(self):
        self.require(self.refs["pre-flight"], "git diff --cached", "git write-tree", "unstaged", "hook", "third-party", "--no-verify")

    def test_secrets_are_content_aware(self):
        self.require(self.refs["pre-flight"], "content", "redact", "not a guarantee", "example")

    def test_delivery_and_recovery(self):
        self.require(self.refs["pr-delivery"], "commit-only", "existing PR", "head SHA", "base", "pending", "ambiguous", "--dry-run")

    def test_stack_lifecycle(self):
        self.require(self.refs["stacking"], "old parent", "squash", "rebase", "closed", "replacement", "shared", "conflict", "topological", "--onto", "--base")

    def test_explicit_rewrite_lease(self):
        self.require(self.refs["stacking"], "separate authorization", "--force-with-lease=refs/heads/<branch>:<expected-remote-SHA>", "background fetch", "do not refresh", "rollback")

    def test_links_and_invocation(self):
        for p in [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md")]:
            for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", p.read_text()):
                if "://" not in link:
                    self.assertTrue((p.parent / link).is_file(), (p, link))
        self.assertNotIn("disable-model-invocation: true", self.main)
        self.require((ROOT / "agents/openai.yaml").read_text(), "allow_implicit_invocation: true")
        self.assertLess(len(self.main.splitlines()), 500)

    def test_eval_coverage(self):
        data = json.loads((ROOT / "evals/evals.json").read_text())
        self.assertEqual(data["skill_name"], ROOT.name)
        ids = [e["id"] for e in data["evals"]]
        self.assertEqual(len(ids), len(set(ids)))
        categories = {e.get("category") for e in data["evals"]}
        self.assertTrue({"scope", "snapshot", "freshness", "stack", "recovery", "secrets", "policy"} <= categories)
        for e in data["evals"]:
            self.assertTrue(e["prompt"] and e["expected_output"] and e["assertions"])


if __name__ == "__main__":
    unittest.main()
