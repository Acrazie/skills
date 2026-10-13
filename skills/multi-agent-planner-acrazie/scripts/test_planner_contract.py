#!/usr/bin/env python3
"""Static planning contract checks, not agent/runtime execution evidence."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / 'skills/multi-agent-planner-acrazie'


def read(path='SKILL.md'):
    return ' '.join((SKILL / path).read_text().split())


class PlannerContract(unittest.TestCase):
    def rules(self, path, *rules):
        for rule in rules:
            with self.subTest(rule=rule):
                self.assertIn(rule, read(path))

    def test_planning_only(self):
        self.rules('SKILL.md', 'never spawns workers itself',
                   'No implicit staging, commit, push, PR, merge',
                   'no automatic executor, reviewer or shipping chain')

    def test_loading(self):
        self.rules('SKILL.md', 'before reading its body', 'each dependency',
                   'returning specialist', 'not filesystem controls')

    def test_contract(self):
        self.rules('SKILL.md', 'independent approval evidence',
                   'Reopen only materially invalidated decisions',
                   'Contract reuse does not require Interview installation',
                   'block only dependent planning', 'do not duplicate its interview')

    def test_decisions_and_fast_path(self):
        self.rules('SKILL.md', 'Current state, numbered Options, Recommendation and Response',
                   'No question IDs', 'preselected consent',
                   'fast path does not waive model validation',
                   'blocked or pending instead of silently choosing')

    def test_count_and_retry(self):
        self.rules('SKILL.md', 'Bound concurrent workers by verified runtime capacity',
                   'approved lot count', 'agreed resource budget',
                   'approved bounded retry budget', 'no new causal hypothesis',
                   'not repeated retries under renamed workers',
                   'no last-writer-wins', 'After retry exhaustion')

    def test_no_universal_count_or_retry_quota(self):
        for path in ('SKILL.md', 'references/patterns.md', 'references/examples.md'):
            text = read(path)
            self.assertNotIn('at most five concurrent workers', text.lower())
            self.assertNotIn('one bounded retry per slice', text.lower())
        self.rules('references/patterns.md', 'Unknown retry budgets remain pending',
                   'Renaming the worker does not reset that budget', 'new causal hypothesis')
        self.rules('SKILL.md', 'If capacity is unknown', 'No hierarchical supervisors',
                   'No implicit staging, commit, push, PR, merge')

    def test_scope_collision(self):
        self.rules('SKILL.md', 'non-overlapping write sets',
                   'cannot share an index', 'isolated worktrees',
                   'integration owner', 'lockfiles belong to one owner',
                   'Discovered overlap stops the affected slice')

    def test_proof(self):
        self.rules('SKILL.md', 'Handles are evidence pointers, not proof',
                   'integrated final snapshot', 'baseline failures, unexecuted checks',
                   'Fresh-context review remains isolated')

    def test_delivery(self):
        self.rules('SKILL.md', 'Reports default to chat', 'approved content and exact path',
                   'one bounded fenced prompt', 'single-agent path',
                   'pending pre-spawn gate', 'Plan approval is not delegation')

    def test_model_gate_unchanged(self):
        def section(id):
            text = (ROOT / 'skills' / id / 'SKILL.md').read_text()
            return text.split('## Subagent model selection\n')[1].split('\n## ')[0].strip()
        self.assertEqual(section(SKILL.name), section('repository-readme-architect-acrazie'))

    def test_references(self):
        self.rules('references/platforms.md', 'revalidate available models and override support',
                   'Do not assume an alias or model identifier transfers',
                   'does not call these mechanisms itself', 'not proof that the host enforces')
        self.rules('references/examples.md', 'repository count alone does not justify delegation',
                   'approved bounded slice budget')
        self.rules('references/patterns.md', 'Renaming the worker does not reset that budget',
                   'One bounded agent owns the task', 'immutable/verifiable handles')
        self.rules('references/interview-tree.md', 'Unknown technical facts',
                   'No lettered options', 'not a parallelism rule')

    def test_eval_integrity(self):
        data = json.loads((SKILL / 'evals/evals.json').read_text())
        self.assertEqual(data['skill_name'], SKILL.name)
        self.assertEqual(len(data['evals']), 8)
        self.assertEqual(len({c['id'] for c in data['evals']}), 8)
        for c in data['evals']:
            self.assertTrue(c['prompt'])
            self.assertTrue(c['expected_output'])
            self.assertGreaterEqual(len(c['expectations']), 2)
            self.assertEqual(c['files'], [])


if __name__ == '__main__':
    unittest.main()
