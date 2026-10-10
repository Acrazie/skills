# Harmonisation des compléments engineering

## Objectif et approbation

Raccorder Product Critic et Adversarial Reviewer aux frontières du noyau engineering
livré par PR #94, sans créer de nouveaux propriétaires ni modifier les defaults
publiés. L'architecture et le glossaire existants suffisent ; aucun nouveau terme
ou compromis architectural durable ne nécessite de nouvel ADR.

Le 2026-10-10, dans cette conversation, l'utilisateur a choisi « 1 » pour ce lot,
puis « 1 » pour tests statiques et scénarios documentés sans modèle ni hôte. Après
présentation du contrat final et de ses exclusions, il a répondu « 1 » à
« Approuver contrat et autoriser réalisation bornée ». Cette preuve autorise les
modifications ci-dessous, pas une activation dans un autre dépôt ni la livraison Git.

## Périmètre

Base actualisée : `874c315b36df0c7f9683a4db3b67022542d204b6`, contenant PR #94 et
PR #95. Travail dans le worktree isolé
`.worktrees/codex/engineering-complements-harmonization`, branche
`codex/engineering-complements-harmonization`.

Inclus : les deux `SKILL.md`, leurs références et scénarios directement concernés,
une suite statique ciblée et ce contrat. Vérification des régressions existantes,
de la structure, des liens et du graphe du site. Aucun changement du catalogue,
des déclarations du graphe ou des metadata n'est nécessaire : aucune citation du
graphe actuel ne pointe vers les deux skills modifiés.

Exclus : nouveaux skills, modifications globales, nouveaux outils/dépendances ou
versions sans approbation distincte, activation dans un projet réel, essais hôtes,
évaluations par modèle, revue indépendante, staging, commit, push, création/mise
à jour de PR, merge et déploiement.

## Décisions et invariants

- Dans un kit explicite ou sous instruction plus stricte, chaque skill, dépendance
  et retour au spécialiste requiert activation avant lecture ou délégation du corps.
  Les defaults de la bibliothèque publiée restent model-invocable.
- Product Critic réutilise un contrat applicable et des preuves d'approbation
  indépendantes ; un statut seul ne suffit pas. Réouvrir uniquement les décisions
  matériellement invalidées. Aucune installation/lecture cérémonielle d'Interview.
- Quand clarification est nécessaire, Interview possède l'entretien. Absence ou
  activation manquante bloque seulement l'étape dépendante ; ne pas dupliquer son
  entretien. Dans un kit géré, installation via mise à jour approuvée de Repo Init
  et sélection épinglée, pas installation directe non épinglée.
- Interview persiste et s'arrête ; retour à Critic distinct de l'approbation du
  contrat. Critic n'implémente jamais et distingue rapport, option, contrat,
  activation et autorisation de réalisation dans le passage à Builder.
- Reviewer reste indépendant, sans contexte auteur hérité, sans correction ni
  self-review de l'implémenteur. Activation, spawning et choix du modèle restent
  séparés ; aucun nouveau mécanisme de délégation n'est introduit.
- Objectif et scope explicites suffisent à l'intake d'une revue lecture seule.
  Des exigences autoritatives et un diff complet stable restent nécessaires pour
  un verdict ; aucun Interview ou Task Contract cérémoniel n'est imposé.
- Verdict limité au snapshot ; nouvelle activation pour re-review dans kit explicite.
  Une revue bloquée ne dispense pas d'une revue exigée par politique du dépôt.
- Questions utilisateur : seulement état actuel, options numérotées, recommandation
  et réponse, localisés, sans IDs ni choix recommandé traité comme consentement.

Sources : [architecture](software-engineering-skill-architecture.md),
[noyau](engineering-core-harmonization.md),
[politique d'invocation](../../.agents/invocation.md),
[contrat partagé](../../skills/interview-acrazie/references/task-contract.md).

## Critères et preuves attendues

- C1 : frontières de chargement et metadata inchangée ; tests statiques, comparaison
  des metadata avec base et parsing YAML.
- C2 : Critic réutilise contrat, respecte gates Interview/retour/Builder et limites
  de rapport/implémentation ; assertions et quatre scénarios documentés.
- C3 : Reviewer conserve isolation, intake lecture seule, snapshot et permissions ;
  assertions et quatre scénarios documentés.
- C4 : quatre champs localisés, dépendances absentes bloquant seulement leur étape ;
  assertions d'instructions et scénarios.
- C5 : régressions, structure, liens, graphe et diff ; aucune mutation hors lot.

## Preuves de livraison

Validation locale terminée. L'utilisateur a séparément autorisé l'installation
verrouillée du site dans ce worktree, sans changement de versions ni de lockfile :

- C1–C4 : **12 tests statiques ciblés réussis**. Avant modification des instructions
  et scénarios : neuf échecs et une erreur attendue de recherche d'instruction absente
  sur 12 tests. Après modification : 12/12. Ce sont des tests de contenu, non des
  simulations d'un moteur d'exécution ou des décisions réelles d'un agent.
- Régressions : 14 tests noyau, 33 activation, 16 permissions et 11 contrat Git Ship
  réussis. Avec le lot ciblé : **86 tests automatisés réussis**.
- Huit nouveaux scénarios documentés, quatre par skill, sans exécution par modèle
  ou hôte ; anciens scénarios conservés.
- C1/C5 : tous frontmatters et metadata du catalogue parsés avec Ruby/Psych ;
  frontmatters et metadata des deux skills identiques à la base. Structure et
  validation frontmatter réussies ; six liens locaux, AST du test, whitespace,
  allowlist de huit fichiers et index vide contrôlés ; `git diff --check` réussi.
- C5, site : après `bun install --frozen-lockfile`, cinq tests invocation réussis.
  Première exécution graphe : 14 tests réussis et quatre échecs faute de pages
  générées, non une citation périmée. Après `bun run build` : **87 pages générées**
  et **18 tests graphe réussis**. Total avec les suites précédentes : **109 tests
  automatisés réussis**. `site/package.json` et `site/bun.lock` identiques à la base.
  Aucun fichier versionné du site modifié ; aucune citation de graphe ne pointe
  vers les skills modifiés. Documentation Context7 de Bun 1.4.2 consultée pour
  confirmer la sémantique frozen-lockfile. Aucun Docker build/smoke exécuté.
- Aucun staging, commit, push, PR, merge, déploiement ou changement global.
  Worktree conservé pour validation et éventuelle livraison séparément autorisée.

Les scénarios `engineering-complements-*` dans les deux
`evals/evals.json` sont définis, non exécutés. Les tests statiques contrôlent les
instructions ; ils ne prouvent ni décisions réelles d'un modèle ni chargement par
Codex/Claude Code. Les gates ne sont pas des contrôles d'accès filesystem ; les
homonymes globaux et le comportement live des hôtes restent des limites connues.

Commande ciblée, depuis le worktree :

```bash
python3 -B skills/product-critic-acrazie/scripts/test_engineering_complements_contract.py
```
