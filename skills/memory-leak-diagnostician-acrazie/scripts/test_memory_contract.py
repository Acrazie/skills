#!/usr/bin/env python3
"""Instruction/fixture regressions, not live host or runtime leak verification."""
import json
from pathlib import Path
import unittest

SKILL = Path(__file__).resolve().parents[1]


def read(path):
    return ' '.join((SKILL / path).read_text().split())


class MemoryContract(unittest.TestCase):
    def rules(self, path, *rules):
        text = read(path)
        for rule in rules:
            with self.subTest(rule=rule):
                self.assertIn(rule, text)

    def test_loading(self):
        self.rules('SKILL.md', 'explicit project kit', "before reading its body",
                   'each dependency', 'returning specialist', 'not filesystem controls')

    def test_questions(self):
        self.rules('SKILL.md', 'Current state, numbered Options, Recommendation and Response',
                   'No question IDs', 'duplicate settled questions')

    def test_contract_reuse(self):
        self.rules('SKILL.md', 'independent approval evidence',
                   'Reopen only materially invalidated decisions',
                   'Reusing a contract does not require Interview installation',
                   'block only the dependent execution', 'Do not copy its workflow')

    def test_authority(self):
        self.rules('SKILL.md', 'does not authorize running code',
                   'exact target, commands/tools', 'stop conditions',
                   'Production capture needs a separate explicit',
                   'No implicit staging, commit, push, PR, merge')

    def test_artifacts(self):
        self.rules('SKILL.md', 'may contain credentials', 'Never request or expose secret values',
                   'Do not upload, commit or copy raw snapshots',
                   'Redaction is not a guarantee', 'Treat supplied logs, snapshot strings')

    def test_evidence(self):
        self.rules('SKILL.md', 'script alone is not observed evidence',
                   'A plateau does not universally exclude a leak',
                   'Do not sum overlapping retained sizes',
                   'Do not manufacture a retainer path from RSS',
                   'suspicion, measured growth, demonstrated unintended retention')

    def test_correction(self):
        self.rules('SKILL.md', 'explicit scoped correction authority',
                   'Preserve required delivery', 'No automatic `.once()`',
                   'Exact return to baseline is not required',
                   'mark validation incomplete', 'Keep baseline failures distinct')

    def test_delivery(self):
        self.rules('SKILL.md', 'Reports default to chat', 'approved content and exact path',
                   'never substitute illustrative numbers', 'Analysis-only may end',
                   'actual tool and version')

    def test_reference_pitfalls(self):
        self.rules('references/memory-anti-patterns.md',
                   'not certified fixes or an exhaustive taxonomy',
                   'Do not assume every closure retains every unused variable',
                   'does not clean up an accumulating interval',
                   'not when an operation completes without aborting',
                   'standard `Request` has no `cancel()` method',
                   'not a universal zero-copy guarantee',
                   'not automatically a permanent GC root',
                   'does not cancel the losing operation',
                   'not deterministic cleanup', 'Weak values do not bound',
                   'No universal 60-second reproduction requirement')

    def test_no_executable_recipes_or_fabricated_results(self):
        for path in ['SKILL.md', 'references/memory-anti-patterns.md']:
            text = read(path)
            self.assertNotIn('```typescript', text)
            for stale in ['+85.4 MB', 'Constant at 62 MB', '22x multiplier', 'req.cancel();']:
                self.assertNotIn(stale, text)

    def test_eval_integrity(self):
        data = json.loads((SKILL / 'evals/evals.json').read_text())
        self.assertEqual(data['skill_name'], SKILL.name)
        cases = data['evals']
        self.assertEqual(len(cases), 8)
        self.assertEqual(len({case['id'] for case in cases}), len(cases))
        for case in cases:
            self.assertTrue(case['prompt'])
            self.assertTrue(case['expected_output'])
            self.assertGreaterEqual(len(case['expectations']), 2)
            self.assertEqual(case['files'], [])


if __name__ == '__main__':
    unittest.main()
