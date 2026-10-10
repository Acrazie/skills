"""Static complement instruction regressions; not host/model execution."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NAMES = ("product-critic-acrazie", "adversarial-reviewer-acrazie")


def read(name, relative="SKILL.md"):
    return (ROOT / "skills" / name / relative).read_text()


class EngineeringComplementsContractTests(unittest.TestCase):
    def contains(self, phrase, text):
        self.assertTrue(" ".join(phrase.split()) in " ".join(text.split()), phrase)

    def test_published_defaults_preserved(self):
        for name in NAMES:
            self.assertNotIn("disable-model-invocation:", read(name).split("---", 2)[1])
            self.contains("allow_implicit_invocation: true", read(name, "agents/openai.yaml"))

    def test_each_entry_obeys_project_loading_boundary(self):
        for name in NAMES:
            text = read(name)
            for phrase in ("explicit project kit", "before reading its instructions",
                           "each dependency", "before reading or dispatching",
                           "not filesystem access controls", "Global homonyms"):
                self.contains(phrase, text)
            self.assertLess(text.index("## Project loading boundary"),
                            text.index("## Entry and boundaries") if name == NAMES[0]
                            else text.index("## Core stance"))

    def test_questions_use_localized_four_fields(self):
        for name in NAMES:
            text = read(name)
            self.contains("display only Current state, numbered Options, Recommendation and Response", text)
            self.contains("Translate labels/content", text)
            self.contains("preselect an answer as consent", text)

    def test_critic_contract_reuse_before_conditional_interview(self):
        text = read(NAMES[0])
        self.assertLess(text.index("Reuse an explicitly approved"), text.index("Interview is mandatory only"))
        for phrase in ("approval evidence beyond a status label", "reopen only affected",
                       "without installing or loading Interview", "do not duplicate its interview"):
            self.contains(phrase, text)

    def test_critic_missing_dependency_blocks_only_dependent_step(self):
        text = read(NAMES[0])
        for phrase in ("unavailable or not activated", "block only the dependent step",
                       "before reading or invoking", "project's pinned selection",
                       "separately approved installation", "Do not silently install or copy",
                       "npx skills add Acrazie/skills@interview-acrazie"):
            self.contains(phrase, text)

    def test_critic_return_and_feature_handoff_have_separate_authority(self):
        text = read(NAMES[0])
        for phrase in ("new explicit invocation of Product Critic", "Report approval never authorizes implementation",
                       "separate explicit activation of Feature Builder", "not a skill command",
                       "not implement the feature itself", "Bug fixes, behavior-preserving refactors"):
            self.contains(phrase, text)

    def test_critic_report_acceptance_remains_separate(self):
        self.contains("Report acceptance and option acceptance are separate", read(NAMES[0]))
        ref = read(NAMES[0], "references/critique-report.md")
        for phrase in ("approval evidence beyond a status label", "loading and execution permissions",
                       "Report approval is not implementation authorization"):
            self.contains(phrase, ref)

    def test_reviewer_does_not_force_interview_for_read_only_review(self):
        text = read(NAMES[1])
        for phrase in ("explicit objective and review scope", "Task Contract is not universally required",
                       "Do not require Interview", "authoritative requirements"):
            self.contains(phrase, text)

    def test_reviewer_isolation_and_spawn_permissions_preserved(self):
        text = read(NAMES[1])
        for phrase in ("fresh agent context without inherited author conversation", "report review as blocked",
                       "spawning and model choice", "new reviewer activation", "does not activate the returning implementer",
                       "review required by repository policy"):
            self.contains(phrase, text)

    def test_reviewer_snapshot_and_no_fix_invariants_preserved(self):
        text = read(NAMES[1])
        for phrase in ("If its source changes during review", "Never write replacement code",
                       "do not implement, commit, or ship", "only to its snapshot"):
            self.contains(phrase, text)
        ref = read(NAMES[1], "references/adversarial-rubric.md")
        self.contains("does not grant activation, spawning, installation or implementation permission", ref)

    def test_scenarios_defined_not_claimed_executed(self):
        for name in NAMES:
            data = json.loads(read(name, "evals/evals.json"))
            self.assertEqual(data["skill_name"], name)
            ids = [e["id"] for e in data["evals"]]
            self.assertEqual(len(ids), len(set(ids)))
            scenarios = [e for e in data["evals"] if e.get("name", "").startswith("engineering-complements-")]
            self.assertGreaterEqual(len(scenarios), 3)
            for scenario in scenarios:
                self.contains("Simulation only", scenario["prompt"])
                self.assertTrue(scenario["expectations"])

    def test_local_markdown_links(self):
        for name in NAMES:
            folder = ROOT / "skills" / name
            for path in (folder / "SKILL.md", *folder.glob("references/*.md")):
                for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text()):
                    if "://" not in link:
                        self.assertTrue((path.parent / link).exists(), (path, link))


if __name__ == "__main__":
    unittest.main()
