"""Static assessment/handoff regressions, not native OS or host certification."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / 'skills/audit-repository-acrazie'


class ScriptPortabilityAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.entry = (SKILL / 'SKILL.md').read_text()
        self.guide = ' '.join((SKILL / 'references/script-portability.md').read_text().split())

    def test_conditional_read_only_owner(self):
        self.assertIn('[references/script-portability.md]', self.entry)
        self.assertIn('Keep this assessment read-only', self.entry)
        self.assertIn('only allowed write path', self.entry)
        for phrase in ('precise portability question', 'selected automation scripts',
                       'not a separate implementation workflow', 'Audit remains read-only',
                       'separate realization authorization', 'not completed refactors'):
            self.assertIn(phrase, self.guide)

    def test_preserved_matrix_and_behavior(self):
        for phrase in ('repository snapshot', 'OS/shell/runtime/runner matrix',
                       'inputs/outputs', 'side effects', 'working directory',
                       'environment precedence', 'success/failure exit codes',
                       'error propagation', 'actual target version'):
            self.assertIn(phrase, self.guide)

    def test_script_trust_and_filesystem_boundaries(self):
        for phrase in ('option-like inputs', 'Distinguish shell injection from option injection',
                       'do not validate executable options', 'Wildcards, spaces, Unicode',
                       'symlink traversal', 'bounded deletion and idempotence',
                       'Preserve unrelated work/data', 'dry-run is non-mutating',
                       'not authority for penetration testing'):
            self.assertIn(phrase, self.guide)

    def test_no_automatic_purge_install_or_runtime_switch(self):
        for phrase in ('Retain a helper unless replacement equivalence is proven',
                       'Do not introduce Bun or upgrade Node', 'No mandatory polyfill purge',
                       'Destructive tests, downloads, network, installation',
                       'manifest/lockfile updates require their separate',
                       'never integrate changes', 'no editing scripts'):
            self.assertIn(phrase, self.guide)
        self.assertNotIn('```', self.guide)
        self.assertNotIn('(Elimination)', self.guide)

    def test_native_proof_and_performance_honesty(self):
        for phrase in ('Syntax inspection or emulation is not native OS execution',
                       'an unexecuted target is not verified', 'Missing required native proof blocks',
                       'not permission to weaken criteria', 'success/error cases and isolated fixtures',
                       'command, snapshot, inputs, exit results', 'baseline/workload/environment',
                       'not measured', 'not proof of no external child process'):
            self.assertIn(phrase, self.guide)

    def test_record_and_pipeline_permissions(self):
        for phrase in ('Report in chat by default', 'approved final Audit Record',
                       'exact content/destination gate', 'selected paths/snapshot',
                       'preserved behavior', 'side effects/permissions and gaps',
                       'Substantive pipeline changes belong to CI/CD'):
            self.assertIn(phrase, self.guide)

    def test_retirement_and_readme_coverage(self):
        for name in ('feature-builder-acrazie', 'script-portability-acrazie'):
            self.assertFalse((ROOT / 'skills' / name).exists())
        migrated = ROOT / 'skills/repository-readme-architect-acrazie/scripts/test_engineering_documentation_contract.py'
        text = migrated.read_text()
        for name in ('test_readme_reuses_current_architecture_not_write_permission',
                     'test_readme_scope_and_generated_boundary_preserved',
                     'test_model_gate_unchanged_against_port'):
            self.assertIn(name, text)

    def test_migrated_scenarios_and_links(self):
        data = json.loads((SKILL / 'evals/evals.json').read_text())
        scenarios = [e for e in data['evals'] if e['name'].startswith('selected-script-assessment-')]
        self.assertEqual(len(scenarios), 4)
        for scenario in scenarios:
            self.assertIn('Simulation only', scenario['prompt'])
            self.assertIn('Audit is read-only', scenario['prompt'])
            self.assertTrue(scenario['expectations'])
        for path in (SKILL / 'SKILL.md', *SKILL.glob('references/*.md')):
            for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', path.read_text()):
                if '://' not in target:
                    self.assertTrue((path.parent / target).exists(), (path, target))


if __name__ == '__main__':
    unittest.main()
