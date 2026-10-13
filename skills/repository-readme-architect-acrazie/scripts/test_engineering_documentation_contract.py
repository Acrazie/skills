"""Static instruction tests, not runtime recipe or host certification."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
README = "repository-readme-architect-acrazie"


def read(name, relative="SKILL.md"):
    return (ROOT / "skills" / name / relative).read_text()


class EngineeringDocumentationContractTests(unittest.TestCase):
    def contains(self, phrase, text):
        self.assertTrue(" ".join(phrase.split()) in " ".join(text.split()), phrase)

    def test_project_loading_boundary(self):
        for name in (README,):
            text = read(name)
            for phrase in ("explicit project kit", "before reading its instructions",
                           "each dependency", "before reading or dispatching",
                           "not filesystem access controls", "Global homonyms"):
                self.contains(phrase, text)

    def test_metadata_preserved(self):
        for name in (README,):
            self.assertNotIn("disable-model-invocation:", read(name).split("---", 2)[1])
            self.assertNotIn("allow_implicit_invocation: false", read(name, "agents/openai.yaml"))

    def test_question_format(self):
        for name in (README,):
            for phrase in ("display only Current state, numbered Options, Recommendation and Response",
                           "Translate labels/content", "preselect an answer as consent"):
                self.contains(phrase, read(name))
        ref = read(README, "references/interview-tree.md")
        match = re.search(r"```text\n(Current state:.*?)\n```", ref, re.S)
        self.assertIsNotNone(match)
        self.assertEqual(re.findall(r"^([A-Za-z ]+):", match[1], re.M),
                         ["Current state", "Options", "Recommendation", "Response"])

    def test_readme_reuses_current_architecture_not_write_permission(self):
        text = read(README)
        for phrase in ("approval evidence beyond a status label", "reopen only affected decisions",
                       "Do not repropose architectures", "exact candidate and destination immediately before writing"):
            self.contains(phrase, text)
        self.contains("current independently approved architecture", read(README, "references/readme-patterns.md"))

    def test_readme_scope_and_generated_boundary_preserved(self):
        text = read(README)
        for phrase in ("primary README", "never create or edit", "generated README",
                       "Do not commit changes", "Do not install dependencies"):
            self.contains(phrase, text)

    def test_model_gate_unchanged_against_port(self):
        def section(name):
            return read(name).split("## Subagent model selection\n")[1].split("\n## ")[0].strip()
        self.assertEqual(section(README), section("mechanical-port-acrazie"))
        self.contains("Before optional delegation", read(README))

    def test_scenarios_and_local_links(self):
        for name in (README,):
            data = json.loads(read(name, "evals/evals.json"))
            self.assertEqual(data["skill_name"], name)
            ids = [e["id"] for e in data["evals"]]
            self.assertEqual(len(ids), len(set(ids)))
            self.assertGreaterEqual(len(data["evals"]), 3)
            for scenario in data["evals"]:
                self.contains("Simulation only", scenario["prompt"])
                self.assertTrue(scenario["expectations"])
            folder = ROOT / "skills" / name
            for path in (folder / "SKILL.md", *folder.glob("references/*.md")):
                for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text()):
                    if "://" not in target:
                        self.assertTrue((path.parent / target).exists(), (path, target))


if __name__ == "__main__":
    unittest.main()
