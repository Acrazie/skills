"""Static instruction regressions; no model or host evaluation."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
AUDIT = "audit-repository-acrazie"
MODERNIZER = "repo-modernizer-acrazie"


def read(name, relative="SKILL.md"):
    return (ROOT / "skills" / name / relative).read_text()


class EngineeringDecisionContractTests(unittest.TestCase):
    def contains(self, phrase, text):
        self.assertTrue(" ".join(phrase.split()) in " ".join(text.split()), phrase)

    def test_published_metadata_preserved(self):
        for name in (AUDIT, MODERNIZER):
            self.assertNotIn("disable-model-invocation:", read(name).split("---", 2)[1])
            self.contains("allow_implicit_invocation: true", read(name, "agents/openai.yaml"))

    def test_entry_loading_and_dependency_boundaries(self):
        for name in (AUDIT, MODERNIZER):
            text = read(name)
            for phrase in ("explicit project kit", "before reading its instructions",
                           "each dependency", "before reading or dispatching",
                           "not filesystem access controls", "Global homonyms"):
                self.contains(phrase, text)
            self.assertLess(text.index("## Project loading boundary"), text.index("## Entry and authorization")
                            if name == AUDIT else text.index("## 1. Entry"))

    def test_four_field_localized_questions(self):
        for name in (AUDIT, MODERNIZER):
            text = read(name)
            for phrase in ("display only Current state, numbered Options, Recommendation and Response",
                           "Translate labels/content", "preselect an answer as consent"):
                self.contains(phrase, text)
        ref = read(AUDIT, "references/interview-tree.md")
        labels = re.findall(r"^([A-Za-z ]+):", re.search(r"```text\n(.*?)\n```", ref, re.S)[1], re.M)
        self.assertEqual(labels, ["Current state", "Options", "Recommendation", "Response"])
        self.assertNotIn("one numbered round", ref)

    def test_audit_reuses_specialist_contract_without_new_dependency(self):
        text = read(AUDIT)
        for phrase in ("approval evidence beyond a status label", "reopen only affected decisions",
                       "retains its specialist interview", "does not automatically invoke another skill"):
            self.contains(phrase, text)
        self.assertNotIn("Interview is mandatory", text)
        self.contains("Do not require Interview", read(AUDIT, "references/interview-tree.md"))

    def test_record_status_not_consent(self):
        ref = read(AUDIT, "references/audit-record.md")
        for phrase in ("resolved", "not approval evidence", "immediately before writing",
                       "exact proposed record", "content and destination"):
            self.contains(phrase, ref)
        self.contains("only allowed write path", read(AUDIT))

    def test_modernizer_reuses_plan_not_validation(self):
        text = read(MODERNIZER)
        for phrase in ("approval evidence beyond a status label", "reopen only affected decisions",
                       "Revalidate repository facts and required checks", "not evidence of a green checkpoint"):
            self.contains(phrase, text)
        self.contains("ne dispense jamais de revalider", read(MODERNIZER, "references/execution-protocol.md"))

    def test_repo_init_brownfield_ownership_without_implicit_loading(self):
        text = read(MODERNIZER)
        self.contains("engineering activation in existing repositories", text)
        self.contains("not a mandatory skill dependency", text)
        self.assertNotIn("operates at **Day 0**", text)

    def test_modernizer_permissions_and_recovery_preserved(self):
        text = read(MODERNIZER)
        for phrase in ("Commit, push, and PR permissions remain distinct",
                       "obtain separate explicit confirmation before destructive rollback",
                       "Maximum 3 self-repair attempts allowed", "before validation and the corresponding commit"):
            self.contains(phrase, text)
        ref = read(MODERNIZER, "references/commit-strategy.md")
        self.contains("Un fichier de politique ne constitue pas une preuve de consentement", ref)
        self.contains("ne transforme pas l'accord de migration en permission de livraison", ref)

    def test_scenarios_defined_not_executed(self):
        for name in (AUDIT, MODERNIZER):
            data = json.loads(read(name, "evals/evals.json"))
            self.assertEqual(data["skill_name"], name)
            ids = [e["id"] for e in data["evals"]]
            self.assertEqual(len(ids), len(set(ids)))
            scenarios = [e for e in data["evals"] if e.get("name", "").startswith("engineering-decision-")]
            self.assertGreaterEqual(len(scenarios), 3)
            for scenario in scenarios:
                self.contains("Simulation only", scenario["prompt"])
                self.assertTrue(scenario["expectations"])

    def test_local_links(self):
        for name in (AUDIT, MODERNIZER):
            folder = ROOT / "skills" / name
            for path in (folder / "SKILL.md", *folder.glob("references/*.md")):
                for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text()):
                    if "://" not in target:
                        self.assertTrue((path.parent / target).exists(), (path, target))


if __name__ == "__main__":
    unittest.main()
