"""Static engineering-core instruction regressions, not host/model execution."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NAMES = ("interview-acrazie", "test-retrofitter-acrazie")


def read(name, relative="SKILL.md"):
    return (ROOT / "skills" / name / relative).read_text()


class EngineeringCoreContractTests(unittest.TestCase):
    def contains(self, phrase, text):
        self.assertTrue(" ".join(phrase.split()) in " ".join(text.split()), phrase)

    def test_published_defaults_unchanged(self):
        for name in NAMES:
            self.assertNotIn("disable-model-invocation:", read(name).split("---", 2)[1])
            self.contains("allow_implicit_invocation: true", read(name, "agents/openai.yaml"))

    def test_each_entry_obeys_project_loading_rules(self):
        for name in NAMES:
            text = read(name)
            self.contains("explicit project kit", text)
            self.contains("before reading its instructions", text)
            self.contains("each dependency", text)
            self.contains("not filesystem access controls", text)

    def test_question_fields_exact(self):
        text = read("interview-acrazie")
        match = re.search(r"```text\n(Current state:.*?)\n```", text, re.S)
        self.assertIsNotNone(match)
        labels = re.findall(r"^([A-Za-z ]+):", match[1], re.M)
        self.assertEqual(labels, ["Current state", "Options", "Recommendation", "Response"])
        self.contains("1. ", match[1])
        self.contains("2. ", match[1])
        self.contains("Translate the four labels", text)
        self.contains("Do not add question IDs", text)

    def test_executor_questions_use_four_fields(self):
        for name in NAMES[1:]:
            text = read(name)
            self.contains("display only Current state, numbered Options, Recommendation and Response", text)
            self.contains("Translate labels/content", text)
            self.contains("preselect an answer as consent", text)

    def test_executor_contract_reuse_precedes_interview(self):
        for name in NAMES[1:]:
            text = read(name)
            self.assertLess(text.index("Reuse an explicitly approved Task Contract"), text.index("Interview is mandatory"))
            self.contains("approval evidence beyond a status label", text)
            self.contains("reopen only affected", text.lower())
        self.assertNotIn("on every invocation", read("test-retrofitter-acrazie"))

    def test_retained_test_oracles(self):
        text = read("test-retrofitter-acrazie")
        for phrase in ("**Characterization:**", "**Conformance:**", "oracle for each", "Functional fixes remain out", "No implementation begins without applicable explicit approval evidence"):
            self.contains(phrase, text)

    def test_dependency_activation_before_body_read(self):
        for name in NAMES[1:]:
            text = read(name)
            self.contains("mandatory only when", text)
            self.contains("unavailable or not activated", text)
            self.contains("Do not install silently", text)
            self.contains("project's pinned selection", text)

    def test_handoff_is_not_execution_authority(self):
        text = read("interview-acrazie")
        self.contains("Stop here", text)
        self.contains("request a new explicit invocation", text)
        ref = read("interview-acrazie", "references/task-contract.md")
        for phrase in ("loading approval", "execution authorization", "same contract", "not activate a dependency"):
            self.contains(phrase, ref)

    def test_executor_acceptance_obligations(self):
        ref = read("interview-acrazie", "references/task-contract.md")
        for phrase in ("execution authorization", "criterion mappings", "final task snapshot",
                       "Always offer independent review", "explicit user choice",
                       "Repository policy requires review", "final-snapshot `ACCEPT`",
                       "fresh context without inherited author conversation",
                       "including new files", "authoritative criteria", "reviewer does not implement",
                       "explicitly approved bounded correction/re-review budget",
                       "Never silently reset", "user arbitration", "explicit inheritance approval",
                       "changed role, scope, risk or model", "pre-existing/out-of-scope",
                       "withdrawal of optional review must be explicit"):
            self.contains(phrase, ref)
        self.contains("this skill never implements", read("interview-acrazie"))
        self.contains("capable harness executor", read("interview-acrazie"))

    def test_no_fallback_self_interview(self):
        for name in NAMES[1:]:
            text = read(name)
            self.contains("do not embed", text)
            self.contains("npx skills add Acrazie/skills@interview-acrazie", text)

    def test_project_override_is_not_library_default_change(self):
        text = (ROOT / ".agents/invocation.md").read_text()
        for phrase in ("Published-library defaults", "explicit project kit", "before reading", "each dependency", "homonyms"):
            self.contains(phrase, text)

    def test_local_markdown_links(self):
        paths = [ROOT / ".agents/invocation.md"]
        for name in NAMES:
            folder = ROOT / "skills" / name
            paths.extend([folder / "SKILL.md", *folder.glob("references/*.md")])
        for path in paths:
            for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text()):
                if "://" not in link:
                    self.assertTrue((path.parent / link).exists(), (path, link))

    def test_scenarios_defined_not_claimed_executed(self):
        for name in NAMES:
            data = json.loads(read(name, "evals/evals.json"))
            self.assertEqual(data["skill_name"], name)
            ids = [e["id"] for e in data["evals"]]
            self.assertEqual(len(ids), len(set(ids)))
            scenarios = [e for e in data["evals"] if e.get("name", "").startswith("engineering-core-")]
            self.assertGreaterEqual(len(scenarios), 2)
            for scenario in scenarios:
                self.contains("Simulation only", scenario["prompt"])
                self.assertTrue(scenario["expectations"])


if __name__ == "__main__":
    unittest.main()
