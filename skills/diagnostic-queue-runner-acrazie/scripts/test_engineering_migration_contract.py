#!/usr/bin/env python3
"""Static instruction/link checks only; no host, compiler or model execution."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
IDS = ('mechanical-port-acrazie', 'diagnostic-queue-runner-acrazie')


def read(skill, suffix='SKILL.md'):
    return (ROOT / 'skills' / skill / suffix).read_text()


class MigrationContract(unittest.TestCase):
    def test_loading_boundary(self):
        for skill in IDS:
            body = " ".join(read(skill).split())
            for rule in ("wait for the user's explicit command", 'each dependency before reading',
                         'One invocation does not activate a chain', 'not filesystem access controls',
                         'new reviewer activation', 'implementer requires', 'unpinned substitutes'):
                self.assertIn(rule, body)

    def test_decision_fields_and_contract_reuse(self):
        for skill in IDS:
            body = read(skill)
            for rule in ('Current state, numbered Options', 'Recommendation and Response',
                         'Translate labels/content', 'do not add question IDs',
                         'independently evidenced', 'Reopen only materially invalidated',
                         'explicit scoped realization approval'):
                self.assertIn(rule, body)

    def test_separate_permissions(self):
        for skill in IDS:
            for rule in ('artifact content/destinations', 'preserve existing files',
                         'Installation, lockfile changes', 'No implicit', 'staging, commit, push, PR, merge or deployment'):
                self.assertIn(rule.lower(), read(skill).lower())

    def test_exact_independent_review(self):
        for skill in IDS:
            for rule in ('every', 'exact candidate', 'fresh agent context without inherited author conversation',
                         'separate manual reviewer context', 'Never substitute implementer self-review',
                         '`ACCEPT`', '`REJECT` or `INCOMPLETE`', 'Corrections invalidate', 'not guarantee zero defects'):
                self.assertIn(rule, read(skill))

    def test_port_oracle_and_final_proof(self):
        body = read(IDS[0])
        for rule in ('before any target code is written', 'Compilation alone is not an',
                     'missing, incomplete or compiler-coupled tests block translation',
                     'unchanged behavioral oracle', 'final snapshot', 'not prove target equivalence'):
            self.assertIn(rule, body)

    def test_port_handoff_condition(self):
        body = read(IDS[0])
        for rule in ('small or empty backlog does not require Queue', 'mass compiler/linter backlog',
                     'snapshot, scope, mapping', 'block that dependent resolution'):
            self.assertIn(rule, body)

    def test_preserved_model_gate(self):
        section = lambda text: text.split('## Subagent model selection\n')[1].split('\n## ')[0].strip()
        control = section(read('feature-builder-acrazie'))
        for skill in IDS:
            self.assertEqual(section(read(skill)), control)

    def test_queue_freshness(self):
        for rule in ('once per snapshot/checkpoint', 'never', 'stale diagnostics', 'between tiers',
                     'changed', 'not revalidated', 'No slow root builds in worker inner loops', 'final project checks'):
            self.assertIn(rule, read(IDS[1]))

    def test_queue_parser_and_tool_limits(self):
        for rule in ('not universal', 'unmatched/multiline diagnostics', 'Windows',
                     'parse coverage', 'tool failure', 'silent download', 'not certified commands'):
            self.assertIn(rule, read(IDS[1]))

    def test_queue_cycles_and_ownership(self):
        for rule in ('strongly connected components', 'not assume', 'separately',
                     'Do not automatically extract types', 'Unaffected independent components',
                     'Avoid overlapping writes', 'No implicit', 'not a commit'):
            self.assertIn(rule, read(IDS[1]))

    def test_references_consistent(self):
        port = read(IDS[0], 'references/migration-pipeline.md')
        queue = read(IDS[1], 'references/queue-guardrails.md')
        for text in (port, queue):
            for rule in ('approved', 'snapshot', '`ACCEPT`', '`INCOMPLETE`', 'self-review', 'staging, commit, push, PR, merge or deployment'):
                self.assertIn(rule, text)
        self.assertIn('root is only a proposal', port)
        self.assertIn('not universal', queue)
        self.assertIn('separately\napproved cycle-breaking task', queue)
        self.assertNotIn('### Permitted Operations', queue)
        self.assertNotIn('Automatic `REJECT`', queue)

    def test_reports_do_not_assume_success(self):
        for skill in IDS:
            self.assertIn('Report in chat by default', read(skill))
            self.assertIn('actual', read(skill))
        self.assertNotIn('**Test Oracle Status**: VERIFIED', read(IDS[0]))
        self.assertNotIn('**Total Diagnostics Ingested**: <Initial error count>', read(IDS[1]))

    def test_eval_scenarios(self):
        for skill in IDS:
            data = json.loads(read(skill, 'evals/evals.json'))
            self.assertEqual(data['skill_name'], skill)
            self.assertEqual(len(data['evals']), 4)
            self.assertEqual(len({x['id'] for x in data['evals']}), 4)
            for item in data['evals']:
                self.assertTrue(item['prompt'].startswith('Simulation only'))
                self.assertTrue(item['expected_output'])
                self.assertEqual(item['files'], [])

    def test_local_links(self):
        for skill in IDS:
            folder = ROOT / 'skills' / skill
            for p in [folder / 'SKILL.md', * (folder / 'references').glob('*.md')]:
                for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
                    if '://' not in link and not link.startswith('#'):
                        self.assertTrue((p.parent / link.split('#')[0]).exists(), link)


if __name__ == '__main__':
    unittest.main()
