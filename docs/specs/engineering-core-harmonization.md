# Harmonisation du noyau engineering

## Objectif

Consolider Interview, Feature Builder et Test Retrofitter autour du contrat
réutilisable, des dépendances conditionnelles vérifiables et des activations
explicites dans les kits projet, sans inverser les defaults publiés.

## Périmètre et approbation

Le 2026-10-09, dans cette conversation, l'utilisateur a choisi « 1 » pour
l'harmonisation du noyau, puis « 1 » pour tests automatisés et scénarios documentés
sans hôte ni évaluation par modèle. Après présentation du contrat complet et de
sa destination, il a répondu « 1 » à « Approuver contrat et autoriser implémentation
bornée ». Cette réponse approuve ce périmètre ; ce n'est pas une permission Git.

Inclus : trois skills, références directement concernées, politique d'invocation
précisant la priorité projet, tests ciblés et scénarios. Travail uniquement dans
le worktree isolé `codex/engineering-core-harmonization`, depuis
`9dc1c0a1e91d7e992e627d2f385c304de11618fa` (contient PR #93 fusionnée).

Exclus : nouveaux skills, site, configuration globale, activation dans projet réel,
scaffolding, installation d'outils, évaluation par modèle, essais live, staging,
commit, push, PR, merge et déploiement. Aucun nouveau terme de domaine ni compromis
architectural durable n'est décidé : glossaire et ADR existants suffisent.

## Décisions reprises

- Chaque question possède uniquement état actuel, options numérotées,
  recommandation et réponse, dans la langue utilisateur.
- Contrat réutilisable : approbation indépendante démontrée, tâche couverte et
  contexte matériel actuel. Un statut `approved` seul ne suffit pas.
- Dépendance Interview obligatoire seulement sans contrat applicable. Un résultat
  valable satisfait le gate sans installation ni chargement cérémoniel.
- Dans kit explicite, chaque dépendance et retour au spécialiste nécessite commande
  utilisateur propre. Acceptation du contrat/review et choix du modèle ne remplacent
  pas cette activation. Defaults publiés et metadata restent inchangés.
- Interview documente puis s'arrête ; autorisation explicite de réalisation peut
  figurer dans approbation finale, sans exécution ni activation par Interview.
- Absence/activation manquante bloque seulement étape dépendante ; pas d'installation,
  copie de substitution ni entretien parallèle improvisé.
- Exécutant possède tests ; Test Retrofitter conserve oracles et exclusions métier.
- Revue facultative acceptée devient gate ; revue exigée par politique ne peut être
  levée par simple refus. Activation, délégation et modèle restent séparés.

Sources : [architecture](software-engineering-skill-architecture.md),
[ADR 0008](../adr/0008-explicit-project-kits-and-policy-preauthorization.md),
[contrat partagé](../../skills/interview-acrazie/references/task-contract.md),
[politique d'invocation](../../.agents/invocation.md).

## Critères et preuves attendues

- C1 : format des questions exact, adaptatif et localisé ; preuve statique du
  template et scénario de frontier documenté.
- C2 : réutilisation avant Interview, branches invalidées seulement, oracles requis
  préservés ; assertions d'instructions et scénarios contrat actuel/périmé.
- C3 : gate de chargement précède lecture/délégation, retour explicite sans nouvelle
  interview ; assertions d'instructions et scénarios de dépendance non activée.
- C4 : permissions, review obligatoire et defaults publiés préservés ; tests statiques,
  YAML et comparaison metadata avec base, scénarios de refus et installation.
- C5 : aucune mutation hors lot ; liens, hooks frontmatter/structure, diff et état Git.

## Preuves de livraison

- C1–C4 : 14 tests statiques du noyau réussis. Première exécution avant changements
  d'instructions : neuf échecs attendus sur 12 tests ; puis ajouts de contrôles
  d'autorisation et format des questions des exécutants. Ils contrôlent instructions,
  template, réutilisation, gates, oracles, revue, metadata et définitions de scénarios,
  sans simuler un moteur d'exécution pour prétendre valider les agents.
- Régressions amorçage/livraison : 33 tests activation, 16 tests permissions et
  11 tests contrat Git Ship réussis. Total : **74 tests automatisés réussis**.
- Huit scénarios supplémentaires documentés : deux Interview, trois Feature Builder,
  trois Test Retrofitter. Aucun scénario exécuté par modèle ni hôte.
- C4–C5 : YAML de tous frontmatters et metadata parsé avec Ruby/Psych ; metadata
  des trois packages identique à la base. Garde textuel pertinent du site contrôlé
  séparément ; suite/build du site non exécutés (site exclu), sans en revendiquer succès.
- C5 : frontmatter et structure réussis ; AST/JSON, sept liens locaux des documents
  changés, whitespace et `git diff --check` réussis. Dix fichiers changés exactement,
  index vide, aucun commit/push/PR ni activation globale/réelle. Worktree conservé.

Commande noyau, depuis le worktree :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 skills/interview-acrazie/scripts/test_engineering_core_contract.py
```

Les scénarios dans `evals/evals.json` sont définis, pas exécutés ; tests textuels
ne prouvent ni décisions d'un modèle ni chargement réel des hôtes. Aucun contrôle inside skill ne peut garantir son non-chargement
préalable : les instructions amont et adapters livrés au lot précédent restent
nécessaires, et les homonymes globaux demeurent limite à résoudre séparément.
