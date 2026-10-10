# Harmonisation des spécialistes de décision engineering

## Objectif et approbation

Harmoniser Audit Repository et Repo Modernizer avec les frontières des kits projet
et le format des questions, sans remplacer leurs entretiens spécialisés.

Le 2026-10-11, dans cette conversation, l'utilisateur a choisi « 1 » pour cadrer
ce lot, puis « 1 » à l'option « Approuver ce contrat et autoriser réalisation ».
Le contrat présenté incluait modifications ciblées, tests statiques, scénarios
documentés et installation verrouillée du site uniquement dans le nouveau worktree.
Cette preuve autorise le lot ci-dessous, pas une adoption dans un projet réel ni
la livraison Git. Aucun nouveau terme ni compromis durable ne nécessite d'ADR.

## Périmètre et isolation

Base actualisée : `874c315b36df0c7f9683a4db3b67022542d204b6`, branche dédiée
`codex/engineering-decision-harmonization`, worktree
`.worktrees/codex/engineering-decision-harmonization`.
PR #96 était ouverte lors du cadrage ; ce lot indépendant part de `main` sans
absorber ses modifications ni dépendre de sa fusion.

Inclus : les deux `SKILL.md`, références Audit interview-tree/audit-record,
Modernizer commit-strategy/execution-protocol, scénarios des deux spécialistes,
nouveau test statique et ce contrat. Dix fichiers exactement.

Exclus : nouveaux skills, refonte des recommandations/version exemples des
catalogues techniques, nouveaux appels obligatoires à Interview ou Git Ship,
metadata publiée, instructions actives, changements du site, activation dans
projet réel, installation globale, essais hôtes/modèles, revue indépendante,
staging, commit, push, PR, merge et déploiement. Les seules dépendances installées
sont celles déjà verrouillées du site pour ses validations locales approuvées.

## Décisions et invariants

- Kits explicites/instructions plus strictes : activation avant lecture ou
  délégation pour chaque skill/dépendance ; ne pas déduire permission d'action de
  son chargement. Defaults publiés conservés.
- Questions utilisateur : état actuel, options numérotées, recommandation et réponse,
  localisés, sans IDs ni réponse présumée. Rapports et scorecard restent distincts.
- Audit conserve son entretien adaptatif. Réutiliser contrat spécialisé courant
  avec preuve indépendante d'accord et validations autorisées, même si l'accord
  existe dans la conversation plutôt que dans un nouveau Task Contract persistant.
  Réouvrir seulement les décisions invalidées ; record historique non assimilé
  à consentement actuel. Contenu/destination doivent être approuvés immédiatement
  avant écriture ; aucune implémentation sous autorité d'audit.
- Modernizer conserve plan/pilier/tier/stratégie indépendamment approuvés et actuels,
  sans répéter les décisions. Révalidation des faits et checks toujours nécessaire :
  plan approuvé et HEAD ne sont pas preuves de checkpoint vert.
- Repo Init possède scaffolding et activation engineering brownfield, sans migration
  de stack. Sa référence conceptuelle n'est pas une dépendance ni activation.
- Migration, installation, gouvernance, staging/commit/push/PR et récupération
  restent séparés. Un fichier de politique n'est pas une preuve de consentement.
- Préserver stratégie de commits, unités cohérentes, preuve de l'index exact, hooks,
  ADR Tier 2/3, baseline validée et arrêt après trois réparations infructueuses.
  Récupération destructive requiert confirmation séparée ; aucun reset automatique.

Sources : [architecture](software-engineering-skill-architecture.md),
[noyau](engineering-core-harmonization.md),
[discipline Modernizer](modernizer-commit-strategy.md),
[politique d'invocation](../../.agents/invocation.md).

## Critères et preuves

- C1, frontières/format/reprise : **10 tests statiques nouveaux réussis** ; avant
  changements, huit échecs attendus sur dix. Ils contrôlent contenu d'instructions,
  metadata, références et définitions de scénarios, pas décisions d'agents réels.
- C2, invariants spécialisés : neuf tests existants de stratégie Modernizer réussis,
  sans modification ni relaxation de leurs assertions.
- C3, régressions : 14 tests noyau, 33 activation, 16 permissions et 11 contrat
  Git Ship réussis. Avec C1/C2 : **93 tests Python réussis**.
- C4, site : `bun install --frozen-lockfile`, cinq tests invocation, build **87 pages**
  et 18 tests graphe réussis. Total : **116 tests automatisés réussis**.
  Manifest/lockfile et metadata publiée identiques à la base. Aucune déclaration
  du graphe ne cite les deux skills changés ; aucune nouvelle arête ajoutée.
- C5, périmètre/hygiène : frontmatter/structure, parsing YAML du catalogue,
  liens README et locaux, AST du nouveau test, JSON des scénarios, whitespace,
  allowlist de dix fichiers et index vide contrôlés ; `git diff --check` réussi.
- Sept nouveaux scénarios documentés : trois Audit, quatre Modernizer. Scénarios
  définis seulement, aucune exécution par modèle ou hôte, aucun benchmark comparatif.

Ces preuves sont locales. Aucun Docker build/smoke, revue indépendante, installation
réelle du kit ni test d'hôte. Les instructions ne sont pas des contrôles d'accès
filesystem ; les homonymes globaux restent une limite pour un gate strict.
Worktree conservé, sans staging/commit/push/PR, merge ou déploiement pour ce lot.

Commande ciblée, depuis le worktree :

```bash
python3 -B skills/audit-repository-acrazie/scripts/test_engineering_decision_contract.py
```
