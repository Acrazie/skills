# Taxonomie Thématique & Matrice de Modernisation

Ce document définit les 6 piliers d'analyse du setup technique d'un dépôt, ainsi que les critères de classification en 3 paliers d'ambition (Tiers).

---

## 1. Les 6 Piliers d'Analyse du Setup

Lors du scan d'un dépôt existant, l'évaluation structure les éléments techniques selon six dimensions fondamentales, complétées par un volet transverse de gouvernance.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        REPO SETUP TAXONOMY                             │
├──────────────────┬──────────────────┬──────────────────────────────────┤
│ 1. Runtime & Lang│ 2. Qualité & Lint│ 3. Build & Bundlers              │
│    Versions,     │    Linters,      │    Vite, Rspack, tsup vs         │
│    engines, mise │    formatters,   │    Webpack, CRA, Babel           │
│    python-version│    typecheckers  │                                  │
├──────────────────┼──────────────────┼──────────────────────────────────┤
│ 4. Tests & QA    │ 5. CI/CD DevOps  │ 6. Dépendances & Package Mgr     │
│    Vitest, Jest, │    Actions v4+,  │    pnpm, bun, uv vs npm, yarn v1 │
│    Playwright,   │    Lefthook,     │    Montée libs core &            │
│    Pytest, mocks │    Release Please│    secondaires                   │
├──────────────────┴──────────────────┴──────────────────────────────────┤
│ Transverse: Gouvernance & Hygiène (README, CI checks, security, etc.)  │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Pilier 1 : Runtime & Langage
- **Composants :** Version du langage d'exécution (Node.js, Python, Go, Rust, PHP), spécifications de version dans les manifests (`engines` dans `package.json`, `requires-python` dans `pyproject.toml`, version dans `go.mod`, etc.).
- **Fichiers pivots :** `.nvmrc`, `.node-version`, `.python-version`, `mise.toml`, `.tool-versions`, `Dockerfile`.
- **Signaux d'obsolescence :** Version en End-of-Life (EOL) ou hors support LTS (ex: Node < 20, Python < 3.10, PHP < 8.2). Absence de déclaration explicite de version entraînant des divergences entre machines de dev et CI.

---

### Pilier 2 : Qualité de Code, Linters & Formatters
- **Composants :** Outils de formatage de code, linters de syntaxe et de style, analyse statique de types.
- **Fichiers pivots :** `.eslintrc*`, `eslint.config.*`, `biome.json`, `.prettierrc*`, `ruff.toml`, `pyproject.toml` (sections ruff/black/flake8), `tsconfig.json`, `phpstan.neon`, `.golangci.yml`.
- **Signaux d'obsolescence :**
  - Configuration legacy ESLint (`.eslintrc.js` ou `.eslintrc.json`) dépréciée au profit de la Flat Config ESLint 9 ou de **Biome**.
  - Empilement d'outils lents et redondants (ex: ESLint + Prettier + import-sort en JS/TS ; Black + Flake8 + isort en Python au lieu de **Ruff**).
  - Absence de vérification stricte de types (`strict: false` dans `tsconfig.json`, absence de PHPStan / mypy).

---

### Pilier 3 : Build, Compilateurs & Bundlers
- **Composants :** Outils de packaging d'assets, bundling de code, transpilation et compilation frontend / backend.
- **Fichiers pivots :** `webpack.config.js`, `rollup.config.js`, `vite.config.ts`, `rspack.config.js`, `tsup.config.ts`, `babel.config.js`, `.swcrc`.
- **Signaux d'obsolescence :**
  - Utilisation de `create-react-app` (CRA), Webpack 4 ou Webpack 5 non optimisé avec des temps de build élevés (> 30s) au lieu de **Vite** ou **Rspack**.
  - Transpilation Babel lente non cachée sans tirets SWC/esbuild.
  - Scripts de build custom complexes remplaçables par des bundlers modernes zéro-config (ex: `tsup`).

---

### Pilier 4 : Tests & Assurance Qualité
- **Composants :** Frameworks de tests unitaires, tests d'intégration, runners de tests end-to-end (E2E), outils de couverture.
- **Fichiers pivots :** `jest.config.*`, `vitest.config.*`, `cypress.config.*`, `playwright.config.*`, `pytest.ini`, `setup.cfg`, `phpunit.xml`.
- **Signaux d'obsolescence :**
  - Jest configuré avec `ts-jest` ou `babel-jest` avec des démarrages lents et une incompatibilité ESM native, là où **Vitest** réutilise la config Vite directement et offre une vitesse x10.
  - Cypress sur des suites lourdes au lieu de **Playwright** (parallélisation native, isolation par contexte de navigateur, auto-waiting).
  - Framework de test déprécié (ex: Mocha/Chai non maintenu, `unittest` historique en Python sans fixtures pytest).

---

### Pilier 5 : CI/CD, Hooks & Automatisation DevOps
- **Composants :** Workflows GitHub Actions, gestionnaires de git hooks, pipelines de release et publication, conteneurs de dev.
- **Fichiers pivots :** `.github/workflows/*.yml`, `lefthook.yml`, `.husky/`, `.pre-commit-config.yaml`, `release-please-config.json`, `.devcontainer/`.
- **Signaux d'obsolescence :**
  - Actions GitHub obsolètes utilisant Node 12 ou Node 16 (ex: `actions/checkout@v2` ou `@v3`, avertissements de dépréciation dans la console GitHub).
  - Absence de cache de dépendances dans les actions CI (`cache: 'pnpm'` ou `actions/cache`).
  - Git hooks basés sur Husky verbeux ou scripts shell non parallélisés au lieu de **Lefthook** (binaire Go ultra-rapide et parallèle).
  - Absence d'automatisation des versions et changelogs (**Release Please** manquant).

---

### Pilier 6 : Gestionnaire de Paquets & Dépendances Applicatives
- **Composants :** Gestionnaire de dépendances, format des lockfiles, dépendances directes et devDependencies.
- **Fichiers pivots :** `package.json` + lockfile (`pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`), `pyproject.toml` + (`uv.lock`, `poetry.lock`), `go.mod` + `go.sum`, `Cargo.toml` + `Cargo.lock`, `composer.json` + `composer.lock`.
- **Signaux d'obsolescence :**
  - Utilisation de gestionnaires obsolètes ou sous-performants (npm standard ou yarn v1 au lieu de **pnpm** ou **bun** ; pip/pipenv au lieu de **uv**).
  - Écarts de versions majeures sur les bibliothèques centrales (ex: React 17/18 ➔ React 19, Next.js Pages Router ➔ App Router, Vue 2 ➔ Vue 3, Symfony 5 ➔ Symfony 6/7).
  - Présence de dépendances abandonnées (non mises à jour depuis > 2 ans ou marquées deprecate sur npm/pypi).

---

### Volet Transverse : Gouvernance & Hygiène
- **Composants :** Documentation de contribution, sécurité, licences, templates d'issues et de PR.
- **Fichiers pivots :** `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `.github/ISSUE_TEMPLATE/`, `CODEOWNERS`.
- **Signaux d'absence :** Manque de fichiers standards garantissant la maintenabilité collective (standards issus de `github-repo-init-acrazie`).

---

## 2. La Matrice d'Ambition à 3 Paliers (Tiers)

Pour chaque recommandation d'amélioration ou de mise à niveau, le skill positionne l'intervention selon 3 paliers d'ambition bien distincts :

```text
┌────────────────────────────────────────────────────────────────────────────┐
│                    MODERNIZATION TIERS (PALIERS)                           │
├───────────────────┬─────────────────────────┬──────────────────────────────┤
│ TIER 1            │ TIER 2                  │ TIER 3                       │
│ Conservateur      │ Majeur                  │ Remplacement Moderne         │
│ (Drop-in / Minor) │ (Breaking Version Bump) │ (Paradigm Shift)             │
├───────────────────┼─────────────────────────┼──────────────────────────────┤
│ - Patch & minor   │ - Montée majeure du     │ - Remplacement d'outil par   │
│ - Zéro rupture    │   même outil (React 19, │   l'alternative Next-Gen     │
│ - GH Actions v4   │   ESLint 9, PHP 8.3)    │   (Webpack->Vite,            │
│ - Lockfile update │ - Breaking changes      │    Jest->Vitest,             │
│ - Risque : Minimal│   refactorisés par IA   │    ESLint->Biome,            │
│ - Effort : Immédiat│ - Risque : Modéré       │    Poetry->uv,               │
│                   │ - Effort : Moyen        │    Husky->Lefthook)          │
│                   │                         │ - Risque : Géré par l'IA     │
│                   │                         │ - Gain DX & Perf : Maximal   │
└───────────────────┴─────────────────────────┴──────────────────────────────┘
```

### Critères de Choix entre Tiers :

1. **Quand privilégier le Tier 1 :**
   - Mise à niveau rapide de maintenance sans risque de déstabiliser une release imminente.
   - Nettoyage des alertes de sécurité mineures (Dependabot).
   - Actualisation des runners de CI sans altération des scripts de test.

2. **Quand privilégier le Tier 2 :**
   - L'outil existant est satisfaisant mais sa version actuelle accumule du retard ou bloque de nouvelles fonctionnalités.
   - Les breaking changes sont bien délimités et disposent d'un guide officiel de migration.
   - L'équipe souhaite conserver les conventions existantes sans changer d'écosystème.

3. **Quand privilégier le Tier 3 (Modernisation & Remplacement) :**
   - L'outil existant engendre une friction quotidienne notable (temps de démarrage lents, configurations tentaculaires, plugins conflictuels).
   - Un remplaçant moderne s'est imposé comme standard de l'industrie avec des gains de vitesse spectaculaires (x10 à x100 grâce à Rust/Go/esbuild).
   - La migration, autrefois pénible et chronophage, est rendue triviale et sûre grâce à l'assistance de l'IA et aux codemods officiels.
