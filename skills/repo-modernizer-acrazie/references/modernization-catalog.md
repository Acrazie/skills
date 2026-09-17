# Catalogue des Outils Modernes & Chemins de Migration

Ce document recense les meilleures alternatives modernes par écosystème, les commandes d'installation, les codemods officiels et les points d'attention lors de la refactorisation.

---

## 1. Écosystème JavaScript & TypeScript

### A. Qualité de Code & Formatage

| Existant (Legacy) | Cible Tier 2 | Cible Tier 3 (Recommandée) | Gain / Justification |
| :--- | :--- | :--- | :--- |
| ESLint legacy (`.eslintrc*`) + Prettier | ESLint 9 Flat Config (`eslint.config.js`) | **Biome** (`biome.json`) | Vitesse x25 (moteur Rust), remplace linter + formatter en un seul binaire, zéro configuration complexe de plugins. |

#### Recette de Migration vers Biome (Tier 3) :
```bash
# 1. Installation de Biome
pnpm add -D --save-exact @biomejs/biome

# 2. Initialisation ou migration automatique depuis ESLint/Prettier
pnpm biome init
pnpm biome migrate eslint --write
pnpm biome migrate prettier --write

# 3. Nettoyage des anciennes dépendances
pnpm remove eslint prettier @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint-config-prettier eslint-plugin-react
rm -f .eslintrc* .prettierrc* .eslintignore .prettierignore
```

---

### B. Build, Compilateurs & Bundlers

| Existant (Legacy) | Cible Tier 2 | Cible Tier 3 (Recommandée) | Gain / Justification |
| :--- | :--- | :--- | :--- |
| `create-react-app` (CRA) / Webpack 4/5 | Webpack 5 moderne avec SWC | **Vite** (`vite.config.ts`) ou **Rspack** | HMR quasi-instantané (< 50ms), démarrage dev instantané sans pré-bundling lourd, support TypeScript natif. |
| Scripts Babel / Rollup pour bibliothèques | Rollup 4 | **tsup** (`tsup.config.ts`) | Bundler zéro-config propulsé par esbuild, génère ESM + CJS + `.d.ts` automatiquement. |

#### Recette de Migration Webpack/CRA vers Vite (Tier 3) :
```bash
# 1. Installer Vite et le plugin framework
pnpm add -D vite @vitejs/plugin-react

# 2. Déplacer index.html à la racine du projet et ajouter le script module
# <script type="module" src="/src/main.tsx"></script>

# 3. Remplacer les variables REACT_APP_* par VITE_* (et process.env par import.meta.env)
# 4. Remplacer les scripts dans package.json ("dev": "vite", "build": "tsc && vite build")
```

---

### C. Frameworks de Test

| Existant (Legacy) | Cible Tier 2 | Cible Tier 3 (Recommandée) | Gain / Justification |
| :--- | :--- | :--- | :--- |
| Jest (`ts-jest` / `babel-jest`) | Jest 29 + `@swc/jest` | **Vitest** (`vitest.config.ts`) | Partage la configuration et les plugins de Vite, support ESM natif, exécution multithread ultra-rapide. |
| Cypress (E2E) | Cypress 13 | **Playwright** (`playwright.config.ts`) | Parallélisation native gratuite, installation d'un seul clic de tous les navigateurs, vitesse x3, auto-wait fiable. |

#### Recette de Migration Jest vers Vitest (Tier 3) :
```bash
# 1. Installer Vitest
pnpm add -D vitest @vitest/coverage-v8

# 2. Lancer le codemod automatique si pertinent
npx vitest-codemod ./src

# 3. Remplacement des mocks : jest.fn() -> vi.fn(), jest.spyOn() -> vi.spyOn(), jest.mock() -> vi.mock()
# 4. Supprimer ts-jest, babel-jest et jest.config.*
```

---

### D. Gestionnaire de Paquets

| Existant (Legacy) | Cible Tier 2 | Cible Tier 3 (Recommandée) | Gain / Justification |
| :--- | :--- | :--- | :--- |
| npm standard ou Yarn v1 (classic) | npm 10+ avec lockfile v3 | **pnpm** ou **bun** | Économie massive d'espace disque (hard links centralisés), installation x3 plus rapide, isolation stricte des dépendances fantômes. |

---

## 2. Écosystème Python

### A. Packaging & Gestion des Environnements

| Existant (Legacy) | Cible Tier 2 | Cible Tier 3 (Recommandée) | Gain / Justification |
| :--- | :--- | :--- | :--- |
| `pip` + `requirements.txt`, `pipenv`, `poetry` | Poetry 1.8+ avec lockfile | **uv** (`pyproject.toml` + `uv.lock`) | Résolution et installation 10x à 100x plus rapide (moteur Rust), gestion unifiée des versions Python (`uv python install`), remplace pip, pip-tools, virtualenv, poetry. |

#### Recette de Migration vers uv (Tier 3) :
```bash
# 1. Initialiser uv dans le projet existant
uv init --bare

# 2. Importer les dépendances existantes
uv add $(cat requirements.txt | grep -v '^#')
# Ou convertir depuis pyproject.toml / poetry :
uv pip compile pyproject.toml -o requirements.txt

# 3. Synchroniser l'environnement virtuel local
uv sync
```

---

### B. Linters & Formatters Python

| Existant (Legacy) | Cible Tier 2 | Cible Tier 3 (Recommandée) | Gain / Justification |
| :--- | :--- | :--- | :--- |
| Flake8 + Black + isort + pylint | Versions récentes des 3 outils | **Ruff** (`ruff.toml` ou section `[tool.ruff]`) | Remplace Black, Flake8, isort, pyupgrade et pydocstyle en un seul binaire Rust ultra-rapide (x50). |

#### Recette de Migration vers Ruff (Tier 3) :
```bash
# 1. Installer ruff via uv
uv add --dev ruff

# 2. Linter et formater le projet
uv run ruff check --fix .
uv run ruff format .

# 3. Supprimer .flake8, .isort.cfg et les dépendances black/flake8/isort
```

---

## 3. Écosystème Go

| Composant | Existant (Legacy) | Cible Recommandée | Action de Modernisation |
| :--- | :--- | :--- | :--- |
| **Toolchain & Version** | Go 1.18 - 1.21 sans directive | Go 1.22+ avec directive `toolchain` | Mise à jour de `go.mod` : ajout de `toolchain go1.23.X`, utilisation du nouveau `math/rand/v2`, boucles for-range améliorées. |
| **Linters** | `go vet` basique ou `golint` déprécié | **golangci-lint** v1.60+ | Configuration de `.golangci.yml` avec lintersets modernes (`gofmt`, `govet`, `staticcheck`, `errcheck`). |
| **Multi-modules** | Scripts bash custom | **Go Workspaces** (`go.work`) | Gestion fluide des dépendances inter-modules en local. |

---

## 4. Écosystème Rust

| Composant | Existant (Legacy) | Cible Recommandée | Action de Modernisation |
| :--- | :--- | :--- | :--- |
| **Édition Rust** | Édition 2018 | **Édition 2021** (ou 2024 preview) | Exécution de `cargo fix --edition` puis mise à jour de `edition = "2021"` dans `Cargo.toml`. |
| **Linter** | Configuration Clippy par défaut | **Clippy all-targets avec règles pédantiques choisies** | Ajout de `[lints.clippy]` dans `Cargo.toml` ou passage de `cargo clippy --all-targets -- -D warnings`. |
| **Tests Runner** | `cargo test` standard | **cargo-nextest** | Exécution des tests en parallèle avec rapport propre et isolation des tests lents. |

---

## 5. Écosystème PHP & Symfony

| Composant | Existant (Legacy) | Cible Recommandée | Action de Modernisation |
| :--- | :--- | :--- | :--- |
| **Gestionnaire & PHP** | Composer 1 / PHP 7.4 - 8.0 | Composer 2.7+ / **PHP 8.2 - 8.3** | Typage strict (`declare(strict_types=1);`), attributs natifs, readonly classes, `composer audit`. |
| **Refactorisation Automatique** | Migration manuelle | **Rector** (`rector.php`) | Automatisation des breaking changes via `vendor/bin/rector process` (SetList PHP_82, SYMFONY_64). |
| **Analyse Statique** | Pas d'analyse ou niveau bas | **PHPStan niveau 8+** | Détection anticipée des erreurs de types et null-safety. |
| **Tests** | PHPUnit 8/9 avec annotations | **PHPUnit 10/11 avec attributs** | Remplacement des annotations docblock `@test` par les attributs PHP 8 `#[Test]`. |

---

## 6. CI/CD & DevOps (Transverse)

### A. GitHub Actions
- **Bump d'actions obsolètes :**
  - `actions/checkout@v2` ou `@v3` ➔ `actions/checkout@v4` (compatibilité Node 20 runner).
  - `actions/setup-node@v2/v3` ➔ `actions/setup-node@v4` avec `cache: 'pnpm'`.
  - `actions/setup-python@v3/v4` ➔ `actions/setup-python@v5`.
- **Ajout de la gestion de concurrence :**
  ```yaml
  concurrency:
    group: ${{ github.workflow }}-${{ github.ref }}
    cancel-in-progress: true
  ```

### B. Git Hooks & Automatisation de Commit
- **Remplacement de Husky / pre-commit par Lefthook :**
  - Ultra-rapide (écrit en Go), exécute les linters et formatters en parallèle.
  - Configuration unique et claire dans `lefthook.yml`.
  - Intégration native des Conventional Commits via hook `commit-msg`.

### C. Automatisation des Releases & Changelogs
- **Mise en place de Release Please :**
  - Crée automatiquement les PRs de release à partir des Conventional Commits.
  - Met à jour le `CHANGELOG.md` et incrémente le numéro de version selon SemVer.
