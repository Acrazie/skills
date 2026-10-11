#!/usr/bin/env python3
"""Static instruction/eval consistency; no campaign or visual runtime execution."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
VISUALS = ['canvas-banner-designer-acrazie', 'immersive-hero-designer-acrazie',
           'svg-banner-designer-acrazie', 'svg-icon-designer-acrazie']
REFINER = 'skill-refiner-acrazie'


def text(skill, path='SKILL.md'):
    return (ROOT / 'skills' / skill / path).read_text()


def flat(skill, path='SKILL.md'):
    return ' '.join(text(skill, path).split())


class SatelliteContract(unittest.TestCase):
    def rules(self, skill, path, *rules):
        for rule in rules:
            with self.subTest(skill=skill, rule=rule):
                self.assertIn(rule, flat(skill, path))

    def test_visual_loading(self):
        for id in VISUALS:
            self.rules(id, 'SKILL.md', 'explicit project kit', 'before reading its body',
                       'each dependency', 'returning specialist', 'not filesystem controls')

    def test_contract_reuse(self):
        for id in VISUALS:
            self.rules(id, 'SKILL.md', 'independent approval evidence',
                       'Reopen only materially invalidated decisions',
                       'does not require Interview installation',
                       'block only dependent realization', 'Do not duplicate the foundation interview')

    def test_decisions(self):
        for id in VISUALS:
            self.rules(id, 'SKILL.md', 'Current state, numbered Options, Recommendation and Response',
                       'No question IDs', 'preselected consent', 'Visual drafts may have names')
        self.rules(REFINER, 'SKILL.md', 'numbered Options', 'preselected ratings',
                   'Score/comment collection is evidence')

    def test_permissions_and_reports(self):
        for id in VISUALS:
            self.rules(id, 'SKILL.md', 'Concepts and reports default to chat',
                       'approved content and exact destination',
                       'concept selection alone is not execution approval',
                       'No installs or package-manager downloads by default',
                       'No implicit staging, commit, push, PR, merge, deployment or rollback')

    def test_evidence(self):
        for id in VISUALS:
            self.rules(id, 'SKILL.md', 'disclose unexecuted checks',
                       'do not prove rendered appearance or runtime behavior',
                       'actual evidence', 'assets', 'acceptance criteria')
        self.rules(VISUALS[0], 'SKILL.md', 'one animation loop per scene', 'reduced motion')
        self.rules(VISUALS[1], 'SKILL.md', 'Never autoplay audio', 'unmount/remount')
        self.rules(VISUALS[3], 'SKILL.md', 'Do not generate any SVG before', 'ASCII as evidence')

    def test_canvas_handoff_graph_evidence(self):
        source = text(VISUALS[1])
        graph = (ROOT / 'site/src/lib/skill-graph.ts').read_text()
        match = re.search(r"source: 'immersive-hero-designer-acrazie'.*?quote: '((?:\\.|[^'])*)'", graph, re.S)
        self.assertIsNotNone(match)
        quote = match.group(1).replace("\\'", "'").replace('\\n', '\n')
        self.assertIn(quote, source)
        self.rules(VISUALS[1], 'SKILL.md', 'apply its dependency loading gate',
                   'Missing activation blocks only that dependency')

    def test_draft_reference_format(self):
        for id, path in [(VISUALS[0], 'canvas-draft.md'), (VISUALS[2], 'banner-draft.md'),
                         (VISUALS[3], 'icon-draft.md')]:
            self.rules(id, 'references/' + path, 'numbered decision options',
                       'not execution or export approval')

    def test_export_install_gate(self):
        for id in VISUALS[2:]:
            self.rules(id, 'references/exports.md', 'approved', 'installed',
                       'npx', 'permission' if id == VISUALS[2] else 'bypass', 'external resources')
        self.assertNotIn('npx @resvg', text(VISUALS[2], 'references/exports.md'))

    def test_refiner_explicit_and_operational(self):
        self.rules(REFINER, 'SKILL.md', 'disable-model-invocation: true',
                   'independent approval evidence', 'operational envelope',
                   'not an upfront ideal-behavior specification',
                   'No implicit staging, commit, push, PR', 'does not activate a campaign')
        self.assertIn('allow_implicit_invocation: false', text(REFINER, 'agents/openai.yaml'))
        self.assertIn('behavior record', text(REFINER, 'agents/openai.yaml'))

    def test_refiner_persistence_and_history(self):
        self.rules(REFINER, 'SKILL.md', 'exact approved paths', 'wait for approval',
                   'Reserve a new file exclusively', 'single writer',
                   'No legacy journal/ADR migration', 'terminal status `version_changed`',
                   'Do not patch, rewrite', 'Remind them once per awaiting observation')
        self.rules(REFINER, 'references/journal-schema.md', 'Retain schema version 1.0',
                   'New optional', 'No observations may follow a terminal event',
                   'Unexpected/concurrent change blocks the write')

    def test_refiner_not_forced_adr(self):
        self.rules(REFINER, 'SKILL.md', 'Closure with complete observations does not require an ADR',
                   'durable nontrivial decisions', 'actual approved artifact paths')
        self.rules(REFINER, 'templates/ADR-skill-feedback.md', 'Ordinary preferences',
                   'not this ADR', 'Preserve existing ADR history')

    def test_local_references(self):
        for id in VISUALS + [REFINER]:
            root = ROOT / 'skills' / id
            for path in root.rglob('*.md'):
                for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                    if '://' not in link and not link.startswith('#'):
                        self.assertTrue((path.parent / link.split('#')[0]).exists(), (path, link))

    def test_eval_integrity(self):
        for id in VISUALS + [REFINER]:
            data = json.loads(text(id, 'evals/evals.json'))
            self.assertEqual(data['skill_name'], id)
            cases = data['evals']
            self.assertEqual(len({c['id'] for c in cases}), len(cases))
            batch = [c for c in cases if c.get('name', '').startswith('harmonization-')]
            self.assertEqual(len(batch), 4)
            for c in batch:
                self.assertTrue(c['prompt'])
                self.assertTrue(c['expected_output'])
                self.assertGreaterEqual(len(c['expectations']), 2)
                self.assertEqual(c['files'], [])


if __name__ == '__main__':
    unittest.main()
