#!/usr/bin/env python3
"""Static contracts/fixture integrity, not live CI provider or agent evaluation."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / 'skills/ci-cd-acrazie'

def read(path='SKILL.md'):
    return (SKILL / path).read_text()

def flat(text):
    return ' '.join(text.split())

class CICDContract(unittest.TestCase):
    def assertRules(self, text, rules):
        for rule in rules:
            self.assertIn(rule, flat(text))

    def test_single_owner(self):
        self.assertTrue(SKILL.is_dir())
        self.assertFalse(list((ROOT/'skills').glob('jenkins-*-acrazie')))
        self.assertRules(read(), ['one repository', 'internal references', 'not separately invocable', 'No closed provider list'])

    def test_loading_boundary(self):
        self.assertRules(read(), ['explicit project kit', 'before reading or dispatching', 'each dependency', 'returning specialist', 'Never read or delegate', 'not filesystem controls'])

    def test_contract_and_decision_reuse(self):
        self.assertRules(read(), ['independent approval evidence', 'reopen only invalidated decisions', 'Current state, numbered Options, Recommendation and Response', 'No question IDs', 'Obtain scoped realization approval', 'Reports default to chat'])

    def test_action_separation(self):
        self.assertRules(read(), ['Installation/lockfile changes', 'remote reads', 'spawning/model', 'No implicit staging, commit, push, PR, merge, auto-merge, deployment or rollback', 'proposed policy is not consent'])

    def test_tool_agnostic_but_evidence_bound(self):
        self.assertRules(read(), ['current documentation', 'actual tool/version', 'Never invent build', 'Conventional commands are candidates', 'Missing required execution facts block runnable generation', 'not Jenkins syntax translated by analogy'])

    def test_ci_only_not_forced_delivery(self):
        self.assertRules(read(), ['CI-only', 'Non-requested capabilities are not applicable', 'CI-only work does not need production decisions'])

    def test_secret_and_contribution_trust(self):
        self.assertRules(read(), ['Never request, display or persist secret values', 'Masking is not isolation', 'Called tests/scripts may be attacker-controlled', 'untrusted code must not receive privileged'])

    def test_artifacts_and_runner(self):
        self.assertRules(read(), ['host-equivalent access', 'Build once and promote the same immutable artifact identity', 'environment authorization separately', 'stale/concurrent deployment'])

    def test_no_admin_expansion(self):
        self.assertRules(read(), ['global runner administration', 'cloud provisioning remain outside scope', 'Missing capabilities block dependent execution', 'not permission to provision infrastructure'])

    def test_remote_envelope(self):
        self.assertRules(read('references/remote-operations.md'), ['exact provider/registry/environment target', 'submitted data', 'One bounded approval', 'expiry', 'Pipeline edits do not authorize', 'read exact run/artifact/environment state', 'inspect state before retry'])

    def test_data_rollback_not_implied(self):
        self.assertRules(read('references/remote-operations.md'), ['environment authority', 'known-good target', 'database restore, data deletion', 'stop instead of blindly duplicating'])

    def test_proof_layers(self):
        self.assertRules(read('references/validation.md'), ['YAML parsing is not a workflow schema check', 'Groovy parsing is not Jenkins DSL/CPS', 'snapshot', 'CI run', 'Published artifact', 'rollback unexercised', 'REJECT/INCOMPLETE'])

    def test_review_not_self_acceptance(self):
        self.assertRules(read(), ['Offer independent review', 'required reviewer blocks acceptance', 'never substitute implementer self-review', 'exact candidate snapshot'])

    def test_stacks_are_evidence_not_commands(self):
        self.assertRules(read('references/stack-evidence.md'), ['not separately invocable skills', 'discovery hint', 'Go', 'JavaScript / TypeScript', 'Python', 'Rust', 'Symfony / PHP', 'module checksums', 'never assume reverting application code reverses a database migration'])

    def test_jenkins_conditional(self):
        self.assertRules(read(), ['only for Jenkins-specific'])
        self.assertRules(read('references/jenkins.md'), ['Read only for Jenkins', 'controller-backed', 'not a general CI', 'not agents', 'Context7'])

    def test_neighbor_handoffs(self):
        for name in ['github-repo-init-acrazie','repo-modernizer-acrazie']:
            text=(ROOT/'skills'/name/'SKILL.md').read_text()
            self.assertRules(text, ['For substantive CI/CD work beyond minimal bootstrap', 'ci-cd-acrazie', 'project loading boundary', 'not repeat settled interviews'])
        for name in ['audit-repository-acrazie','script-portability-acrazie','feature-builder-acrazie','test-retrofitter-acrazie']:
            self.assertIn('## CI/CD boundary', (ROOT/'skills'/name/'SKILL.md').read_text())

    def test_migration_is_explicit(self):
        text=(ROOT/'README.md').read_text()
        self.assertRules(text, ['not automatically migrated', 'six former', 'ci-cd-acrazie'])
        self.assertFalse(re.search(r'\]\(skills/jenkins-',text))

    def test_fixture_integrity_and_scenarios(self):
        data=json.loads(read('evals/evals.json'))
        self.assertEqual(data['skill_name'],'ci-cd-acrazie')
        self.assertEqual(len(data['evals']),9)
        self.assertEqual(len({x['id'] for x in data['evals']}),9)
        for item in data['evals']:
            self.assertTrue(item['expected_output'])
            for path in item['files']:self.assertTrue((SKILL/path).is_file(),path)

    def test_reference_links(self):
        for p in [SKILL/'SKILL.md',*(SKILL/'references').glob('*.md')]:
            for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
                if '://' not in link and not link.startswith('#'):
                    self.assertTrue((p.parent/link.split('#')[0]).exists(),(p,link))

if __name__ == '__main__':
    unittest.main()
