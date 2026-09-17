# ADR Template : Décision de Modernisation du Setup

Utiliser ce modèle pour documenter chaque migration majeure (Tier 2) ou remplacement d'outil (Tier 3) validé dans le dépôt. Le fichier doit être enregistré sous `docs/adr/YYYY-MM-DD-<titre-kebab-case>.md`.

---

```markdown
# ADR: [Numéro séquentiel ou Date] - [Titre de la Modernisation]

- **Date :** YYYY-MM-DD
- **Statut :** Accepté
- **Palier d'intervention :** [Tier 2 : Majeur | Tier 3 : Remplacement Moderne]
- **Pilier concerné :** [Runtime | Qualité & Linters | Build & Bundler | Tests & QA | CI/CD | Dépendances]
- **Auteur(s) :** [Équipe de développement]

---

## 1. Contexte & Problématique

[Décrire l'état initial de la configuration et les difficultés rencontrées : lenteur de compilation, incompatibilité de versions, format de configuration déprécié, friction pour les nouveaux développeurs, etc.]

---

## 2. Décision & Changement Opéré

Nous avons décidé de migrer de **[Ancien outil/version]** vers **[Nouvel outil/version]**.

### Alternatives Évaluées :
- **Option 1 (Maintien / Mise à jour mineure Tier 1) :** [Pourquoi cette option a été écartée]
- **Option 2 (Montée de version Tier 2) :** [Pourquoi cette option a été retenue ou écartée]
- **Option 3 (Remplacement moderne Tier 3) :** [Pourquoi cette option a été retenue]

---

## 3. Conséquences & Bénéfices

### Bénéfices (Conséquences Positives) :
- [Gain de temps de build ou de tests (ex: tests Jest passés de 45s à 3s avec Vitest)]
- [Simplification de la maintenance (ex: configuration unique biome.json remplaçant 4 fichiers)]
- [Support natif des technologies modernes (ESM, TypeScript, dernières versions de runtime)]

### Compromis & Points de Vigilance (Conséquences Négatives) :
- [Éventuels plugins non encore portés]
- [Changement d'habitudes ou de commandes CLI pour l'équipe]

---

## 4. Validation & Conformité

- **Outils / Codemods utilisés :** [ex: npx @biomejs/biome migrate eslint]
- **Résultats des vérifications :**
  - Lint / Format : ✅ Passé
  - Typage : ✅ Passé
  - Suite de tests : ✅ Passé ([X] tests exécutés avec succès)
  - Build : ✅ Passé
```
