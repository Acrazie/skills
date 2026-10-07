"""Static documentation regression checks, not live agent behavior evaluations."""

from pathlib import Path
import re
import unittest

SKILL = Path(__file__).resolve().parents[1]
ENTRY = (SKILL / "SKILL.md").read_text()
STRATEGY = (SKILL / "references/commit-strategy.md").read_text()
EXECUTION = (SKILL / "references/execution-protocol.md").read_text()
INSPECTION = (SKILL / "references/inspection-checklist.md").read_text()


class CommitContractTests(unittest.TestCase):
    def require(self, document, *fragments):
        for fragment in fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, document)

    def test_discovery_and_non_conventional_repository(self):
        self.require(STRATEGY, "source, portée", "inaccessibilité", "Ne pas imposer Conventional Commits", "Convention existante non Conventional Commits")
        self.require(INSPECTION, "commit-strategy.md", "Une absence de hook n'implique pas une absence de politique")
        self.assertNotIn("Create atomic commits using Conventional Commits", ENTRY)

    def test_policy_without_tooling_or_new_file(self):
        self.require(STRATEGY, "obtenir approbation avant création", "sans nouvel outil", "aucun fichier nouveau n'est obligatoire", "ne confère aucune autorisation")

    def test_strategy_is_binding_even_without_hooks(self):
        self.require(ENTRY, "block non-compliance", "Control compliance even without hooks or CI")
        self.require(STRATEGY, "contrainte obligatoire", "ne pas committer", "--no-verify")

    def test_permission_boundaries(self):
        self.require(STRATEGY, "staging, au commit, au push et à la PR, séparément", "demander avant l'action", "n'accorde pas automatiquement les permissions de livraison")
        self.require(ENTRY, "Commit, push, and PR permissions remain distinct")

    def test_inseparable_migration_units(self):
        self.require(STRATEGY, "regrouper runtime, configuration et adaptations code", "Séparer les intentions indépendantes")
        self.assertNotIn("Chaque couche doit être totalement validée et commitée", EXECUTION)
        self.assertNotIn("Chaque couche ou outil modernisé fait l'objet d'un commit unique", EXECUTION)

    def test_staged_snapshot_and_unrelated_work(self):
        self.require(STRATEGY, "git diff --cached", "Un index déjà contaminé bloque le commit", "Un test vert du working tree ne valide pas un index partiel différent", "sans stash/reset du travail tiers")

    def test_adr_precedes_validation_and_commit(self):
        self.require(ENTRY, "before validation and the corresponding commit")
        self.require(EXECUTION, "avant les validations et l'inclure dans le commit")
        self.assertNotIn("references/adr-template.md", EXECUTION)

    def test_failed_checks_and_safe_checkpoints(self):
        self.require(ENTRY, "obtain separate explicit confirmation before destructive rollback")
        self.require(STRATEGY, "indisponible, rouge ou périmée bloque le commit", "SHA avec les preuves", "trois réparations infructueuses", "Aucun reset ou nettoyage automatique", "HEAD` n'est pas vert par définition")
        for document in (ENTRY, EXECUTION):
            self.assertNotIn("Automatic Rollback", document)
            self.assertNotIn("Rollback Automatique", document)

    def test_local_references_resolve(self):
        for file in [SKILL / "SKILL.md", *sorted((SKILL / "references").glob("*.md"))]:
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", file.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(file=file.name, target=target):
                    self.assertTrue((file.parent / target.split("#")[0]).exists())


if __name__ == "__main__":
    unittest.main()
