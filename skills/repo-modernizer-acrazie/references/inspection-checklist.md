# Checklist d'Inspection Passive en Lecture Seule

Ce document détaille les points de contrôle et commandes d'investigation en lecture seule utilisés lors de la phase de scan initial.

---

## 1. Inventaire des Fichiers Clés à Détecter

Avant toute interaction, exécuter les recherches de présence de fichiers :

| Domaine | Fichiers Cibles | Indice Détecté |
| :--- | :--- | :--- |
| **Package Managers & Lockfiles** | `pnpm-lock.yaml`, `package-lock.json`, `yarn.lock`, `bun.lockb` | Gestionnaire JS/TS actif |
| | `uv.lock`, `poetry.lock`, `Pipfile.lock`, `requirements.txt` | Gestionnaire Python actif |
| | `Cargo.lock`, `go.mod`, `composer.lock` | Rust, Go, PHP |
| **Runtime & Engines** | `.nvmrc`, `.node-version`, `.python-version`, `mise.toml`, `.tool-versions` | Version déclarée du runtime |
| **Linters & Formatters** | `biome.json`, `biome.jsonc`, `eslint.config.*`, `.eslintrc*`, `.prettierrc*` | Stack de qualité JS/TS |
| | `ruff.toml`, `.flake8`, `.isort.cfg`, `pyproject.toml` | Stack de qualité Python |
| | `.golangci.yml`, `phpstan.neon`, `.php-cs-fixer.*` | Go / PHP |
| **Build & Bundler** | `vite.config.*`, `webpack.config.*`, `rollup.config.*`, `tsup.config.*` | Compilateur / Bundler |
| **Tests & QA** | `vitest.config.*`, `jest.config.*`, `playwright.config.*`, `cypress.config.*` | Frameworks de tests |
| **CI/CD & Hooks** | `.github/workflows/*.yml`, `lefthook.yml`, `.husky/`, `.pre-commit-config.yaml` | Automatisation CI/CD |
| **Gouvernance** | `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `.github/ISSUE_TEMPLATE/` | Briques de gouvernance |

---

## 2. Commandes d'Inspection Non-Destructives

### A. Détection des Dépendances Obsolètes
- **Node.js (pnpm / npm) :**
  ```bash
  pnpm outdated || npm outdated
  ```
  *Analyse :* repérer les écarts de versions majeures (colonne `Current` vs `Latest`).
- **Python (uv / pip) :**
  ```bash
  uv pip list --outdated || pip list --outdated
  ```
- **Go :**
  ```bash
  go list -u -m all
  ```
- **Rust :**
  ```bash
  cargo outdated || true
  ```
- **PHP :**
  ```bash
  composer outdated --direct
  ```

---

### B. Détection des Actions GitHub Obsolètes
Scanner les workflows pour relever les versions des actions officielles :
```bash
grep -E 'uses: actions/[a-zA-Z0-9_-]+@(v1|v2|v3)' .github/workflows/*.yml || true
```
*Alerte :* Les versions `@v2` et `@v3` reposent souvent sur des environnements Node 12/16 dépréciés.

---

### C. Détection des Configurations de Linters Dépréciées
Vérifier si le projet utilise les formats legacy :
- En JS/TS : présence de fichiers `.eslintrc*` (format déprécié depuis ESLint v9).
- En Python : présence conjointe de `.flake8`, `.isort.cfg` et `black` (remplaçables par `ruff`).

---

### D. Détection des Gaps de Gouvernance & Hygiène
Vérifier les fichiers absents par rapport aux standards Acrazie (`github-repo-init-acrazie`) :
- Hook manager moderne (**Lefthook**) absent ?
- Workflow de release automatisée (**Release Please**) absent ?
- Fichier `.editorconfig` manquant ?
- `.gitignore` incomplet (manque `.worktrees/`, `.env*`) ?
- Documentation de sécurité (`SECURITY.md`) ou contribution (`CONTRIBUTING.md`) absente ?
