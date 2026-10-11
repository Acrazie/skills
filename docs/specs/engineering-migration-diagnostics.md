# Harmonisation Mechanical Port et Diagnostic Queue

## Objectif et approbation

Le 2026-10-11, l'utilisateur a choisi le lot Mechanical Port + Diagnostic Queue,
puis répondu « 1 » à l'option « Approuver contrat et autoriser réalisation bornée,
installation verrouillée comprise ». Cette approbation couvre les huit fichiers,
les gates et validations décrits ici, pas une migration réelle ni une livraison Git.
Aucun nouveau terme ou compromis durable ne nécessite de nouvel ADR.

## Périmètre et isolation

Base : `bb67c5b4f542f40bce86c26ea616cf28fb4f85c0`, depuis `origin/main` actualisé.
Branche `codex/engineering-migration-diagnostics`, worktree dédié
`.worktrees/codex/engineering-migration-diagnostics`. PR #98 reste ouverte lors
du cadrage ; ce lot indépendant n'en absorbe pas les fichiers ou validations.

Huit fichiers : les deux SKILL, leurs références migration-pipeline/queue-guardrails,
leurs deux fichiers evals, un test statique dans Diagnostic Queue et ce contrat.
Metadata publiée, frontmatters et sections de sélection modèle inchangés ; ni
instructions actives, ni graphe/site, ni nouveau package. Le graphe actuel ne
déclare aucun appel de ces deux propriétaires, donc aucune citation à modifier.

Exclus : migration/résolution réelle, installation globale/kit dans projet réel,
tests modèles/hôtes, certification recettes CLI, revue indépendante du lot,
staging, commit, push, PR, merge et déploiement. Installation des seules dépendances
verrouillées du site dans ce worktree pour validation locale approuvée.

## Décisions et invariants

- Kits explicites : activation avant lecture/délégation de chaque dépendance,
  nouvelle activation pour revue d'un nouveau snapshot et retour à l'exécutant.
  Defaults publiés conservés, aucune chaîne automatiquement activée.
- Questions localisées à quatre champs ; accord applicable et indépendant réutilisé,
  seules décisions invalidées rouvertes. Pas d'Interview universel supplémentaire.
- Artefacts : contenu/destinations et écriture approuvés ; préserver existant.
  Exécution, installation/lockfile, réseau, fixtures destructives, spawning/modèle
  et livraison gardent leurs autorisations distinctes. Rapport dans chat par défaut.
- Mechanical : oracle source automatisé indépendant/black-box adéquat et passant
  avant code cible ; mapping et ownership approuvés ; canari et fidélité 1:1 conservés.
  Queue conditionnelle au backlog massif, pas aux petits diagnostics ni à zéro erreur.
  Oracle cible final et validations nécessaires après toutes corrections.
- Revue obligatoire sur chaque unité/fix ; un lot cohérent doit explicitement couvrir
  toutes ses unités. Contexte indépendant, base/candidat exact, ACCEPT requis ;
  REJECT/INCOMPLETE/indisponibilité bloquent acceptation. Correction invalide preuves
  affectées ; syntaxe seule ne démontre pas défaut et ACCEPT ne promet pas zéro bug.
- Queue : ingestion par snapshot/checkpoint, actualisation entre tiers, aucun dispatch
  de diagnostics périmés. Capture brute/non reconnue conservée, parser non universel,
  recettes historiques non certifiées et npx non assimilé à outil sans installation.
- Graphe issu de dépendances réelles, pas manifestes seuls ; composant cyclique bloquant
  suspendu et éventuel cycle-breaking séparément approuvé, sans extraction automatique.
  Un composant indépendant peut continuer sous son accord et ses validations.
- Workers bornés, écritures non chevauchantes, contrôles projet pertinents. Suppression
  staging/commit implicites ; aucun bypass de checks pour réduire compteurs. Fermeture
  requiert diagnostics actuels, revues et checks finaux requis, pas simple burn-down.

Sources : [architecture](software-engineering-skill-architecture.md),
[politique](../../.agents/invocation.md),
[Mechanical](../../skills/mechanical-port-acrazie/SKILL.md),
[Queue](../../skills/diagnostic-queue-runner-acrazie/SKILL.md).

## Critères et preuves attendues

C1 : gates, reprise et permissions cohérents dans entrées/références, tests statiques.
C2 : oracle/revue obligatoires et fraîcheur Queue explicites sans permissions implicites.
C3 : metadata, sections modèle et scope huit fichiers préservés, liens/JSON/YAML valides.
C4 : régressions Python/site et build disponibles ; échecs/limites rapportés exactement.
C5 : huit scénarios documentés, non exécutés par modèle/hôte ; aucune preuve de runtime
CLI, migration réelle, correction de backlog, installation live ou revue indépendante.

Commande ciblée depuis worktree :

```bash
python3 -B skills/diagnostic-queue-runner-acrazie/scripts/test_engineering_migration_contract.py
```

## Preuves de réalisation

Première exécution du nouveau test :
13 réussites et un échec dû à une assertion sensible au saut de ligne dans la phrase
« new reviewer activation ». Assertion normalisée pour les espaces ; pas de
modification de la règle pour faire passer le test.


- C1/C2 : **14 nouveaux tests statiques réussis**, sur chargement/reprise, décisions,
  permissions, oracle, handoff conditionnel, revue indépendante, fraîcheur/parsing,
  cycles/ownership, rapports et références. Ne prouvent pas un comportement d'agent.
- C3 : frontmatters, metadata et sections modèle des deux skills identiques à la base ;
  manifest/lockfile, instructions actives et graphe inchangés. Parsing YAML du catalogue,
  JSON/AST, liens locaux, frontmatter/structure et whitespace contrôlés avec succès.
- C4 : **119 tests Python réussis** (14 nouveaux, 10 décisions, 12 compléments,
  9 stratégie Modernizer, 14 noyau, 33 activation, 16 permissions, 11 Git Ship).
  **31 tests site réussis** (5 invocation, 8 sélection modèle, 18 graphe).
  **150 tests automatisés**, build **87 pages**. Installation frozen-lockfile dans
  ce seul worktree, versions/lockfile inchangés. Deux assertions du site exigent des
  phrases source exactes ; formulations sémantiquement équivalentes rétablies sans
  changer tests ni gates. Une tentative corrective avait mauvais cwd, donc aucun
  fichier modifié par cette tentative ; correction appliquée ensuite au bon worktree.
- C5 : huit scénarios documentés, **non exécutés par modèle/hôte**. Pas de benchmark,
  certification CLI, migration, résolution réelle, Docker build/smoke ou revue
  indépendante du lot. Les gates restent instructions, pas contrôle d'accès filesystem
  ni preuve de support live des hôtes. Homonymes globaux non vérifiés.

Exactement huit fichiers du périmètre modifiés/créés. Index vide ; aucune livraison
Git ni installation réelle de kit. Worktree conservé pour approbation suivante.
