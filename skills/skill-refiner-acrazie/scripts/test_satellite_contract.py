#!/usr/bin/env python3
"""Static instruction/eval consistency; no campaign or visual runtime execution."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[3]
CANVAS = 'canvas-banner-designer-acrazie'
HERO = 'immersive-hero-designer-acrazie'
SVG = 'svg-designer-acrazie'
VISUALS = [CANVAS, HERO, SVG]
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
        for id in (CANVAS, HERO):
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
        self.rules(CANVAS, 'SKILL.md', 'one animation loop per scene', 'reduced motion')
        self.rules(HERO, 'SKILL.md', 'Never autoplay audio', 'unmount/remount')
        self.rules(SVG, 'SKILL.md', 'Do not generate any SVG before', 'ASCII as evidence')

    def test_canvas_handoff_graph_evidence(self):
        source = text(HERO)
        graph = (ROOT / 'site/src/lib/skill-graph.ts').read_text()
        match = re.search(r"source: 'immersive-hero-designer-acrazie'.*?quote: '((?:\\.|[^'])*)'", graph, re.S)
        self.assertIsNotNone(match)
        quote = match.group(1).replace("\\'", "'").replace('\\n', '\n')
        self.assertIn(quote, source)
        self.rules(HERO, 'SKILL.md', 'apply its dependency loading gate',
                   'Missing activation blocks only that dependency')

    def test_draft_reference_format(self):
        for id, path in [(CANVAS, 'canvas-draft.md'), (SVG, 'banner-draft.md'),
                         (SVG, 'icon-draft.md')]:
            self.rules(id, 'references/' + path,
                       'not execution or export approval')
            if id != 'svg-designer-acrazie':
                self.rules(id, 'references/' + path, 'numbered decision options')

    def test_export_install_gate(self):
        for id in (SVG,):
            self.rules(id, 'references/exports.md', 'approved', 'installed',
                       'npx', 'permission', 'external resources')
        self.assertNotIn('npx @resvg', text(SVG, 'references/exports.md'))

    def test_svg_single_owner_and_conditional_domains(self):
        svg = 'svg-designer-acrazie'
        body = flat(svg)
        for retired in ('svg-icon-designer-acrazie', 'svg-banner-designer-acrazie'):
            self.assertFalse((ROOT / 'skills' / retired).exists())
        self.rules(svg, 'SKILL.md', 'one static-vector workflow', 'conditional domain',
                   'actual smallest target size', 'crop and avatar occlusion',
                   'currentColor', 'no fixed question fields', 'not a quota',
                   'not create a package logo', 'real encoding', 'not a renamed PNG')
        for source in ('icon-draft.md', 'banner-draft.md', 'presets.md'):
            self.assertIn('references/' + source, text(svg))
        self.rules(svg, 'references/exports.md', 'An ICO must be encoded as ICO',
                   'requested embedded sizes', 'Do not install a renderer',
                   'actual pixel dimensions', 'export permission does not authorize integration')
        self.assertNotIn('50% to 65%', body)
        self.assertNotIn('3–5 directions', flat(svg, 'references/inspiration-library.md'))
        self.assertNotIn("entrypoint's four", flat(svg, 'references/icon-draft.md'))
        self.assertNotIn('Every direction in a multi-choice concept batch needs',
                         flat(svg, 'references/icon-draft.md'))
        cases = json.loads(text(svg, 'evals/evals.json'))['evals']
        self.assertEqual(len(cases), 8)
        self.assertEqual({c['name'] for c in cases if c['id'] > 4}, {
            'svg-icon-color-small-size', 'svg-real-favicon',
            'svg-banner-contextual-crop', 'svg-combined-targets'})
        self.assertTrue(all(c['prompt'].startswith('Simulation only') for c in cases))

    def test_svg_catalogue_and_package_logo_retirement(self):
        self.assertFalse(list((ROOT / 'skills').glob('*/assets/*logo*.svg')))
        self.assertTrue((ROOT / 'site/public/logo.svg').exists())
        readme = (ROOT / 'README.md').read_text()
        translations = (ROOT / 'site/src/i18n/skills.ts').read_text()
        canvas = text('canvas-banner-designer-acrazie')
        for source in (readme, translations, canvas):
            self.assertIn('svg-designer-acrazie', source)
            self.assertNotIn('svg-icon-designer-acrazie', source)
            self.assertNotIn('svg-banner-designer-acrazie', source)
        self.assertIn('Do not create package logos automatically',
                      (ROOT / 'AGENTS.md').read_text())

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
