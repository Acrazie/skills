"""Static adaptive-output regressions; not behavioral model or runtime proof."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def read(name, path='SKILL.md'):
    return (ROOT / 'skills' / name / path).read_text()


class AdaptiveCatalogueTests(unittest.TestCase):
    def contains(self, phrase, text):
        self.assertIn(' '.join(phrase.split()), ' '.join(text.split()))

    def test_readme_no_architecture_or_preview_quota(self):
        text = read('repository-readme-architect-acrazie')
        ref = read('repository-readme-architect-acrazie', 'references/readme-patterns.md')
        for phrase in ('no fixed option count', 'one fitting architecture',
                       'no required preview format', 'Do not create cosmetic variants'):
            self.contains(phrase, text)
        self.assertNotIn('offer two or three materially different README architectures', text)
        self.contains('A single fitting proposal is valid', ref)
        self.contains('not required syntax or headings', ref)

    def test_readme_write_and_reuse_guards(self):
        text = read('repository-readme-architect-acrazie')
        for phrase in ('Do not repropose architectures', 'Let the user select one option',
                       'explicit approval of the exact candidate and destination immediately before writing',
                       'Do not install dependencies', 'Do not commit changes'):
            self.contains(phrase, text)

    def test_critique_equivalent_layout_preserves_content(self):
        ref = read('product-critic-acrazie', 'references/critique-report.md')
        for phrase in ('not mandatory headings', 'Equivalent content in an existing report is valid',
                       'scope/revision, status and approval evidence',
                       'observations, declared needs and hypotheses', 'accepted/pending decisions',
                       'actual checks, evidence gaps', 'source/context, impact, confidence/limits',
                       'discriminating verification method', 'do not invent measurements',
                       'content and exact destination', 'Report approval is not implementation authorization'):
            self.contains(phrase, ref)

    def test_review_contextual_examples_not_weakened_proof(self):
        ref = read('adversarial-reviewer-acrazie', 'references/adversarial-rubric.md')
        for phrase in ('Assess relevance of each pillar', 'non-exhaustive investigation leads',
                       'Missing examples never exclude an actual defect',
                       'Do not skip affected authorization', 'Verify runtime, language, framework and version',
                       'syntax match alone never establishes', 'proof-of-flaw requirements',
                       "does not alter the caller's review/correction loops", 'concrete failure scenario',
                       'legitimate contract results and test doubles are not violations'):
            self.contains(phrase, ref)
        entry = read('adversarial-reviewer-acrazie')
        for phrase in ('fresh agent context without inherited author conversation',
                       'If its source changes during review', 'Never write replacement code',
                       'only to its snapshot'):
            self.contains(phrase, entry)

    def test_scenarios_and_links(self):
        for name in ('repository-readme-architect-acrazie', 'product-critic-acrazie',
                     'adversarial-reviewer-acrazie'):
            data = json.loads(read(name, 'evals/evals.json'))
            self.assertEqual(data['skill_name'], name)
            ids = [e['id'] for e in data['evals']]
            self.assertEqual(len(ids), len(set(ids)))
            scenarios = [e for e in data['evals'] if e['name'].startswith('adaptive-catalogue-')]
            self.assertEqual(len(scenarios), 1)
            self.assertIn('Simulation only', scenarios[0]['prompt'])
            self.assertTrue(scenarios[0]['expectations'])
            folder = ROOT / 'skills' / name
            for path in (folder / 'SKILL.md', *folder.glob('references/*.md')):
                for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', path.read_text()):
                    if '://' not in target:
                        self.assertTrue((path.parent / target).exists(), (path, target))


if __name__ == '__main__':
    unittest.main()
