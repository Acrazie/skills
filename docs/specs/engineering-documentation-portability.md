# Harmonisation README et Script Portability

## Objectif et approbation

Harmoniser README Architect et Script Portability avec les kits projet, les accords
réutilisables et les questions à quatre champs. Rendre les permissions et preuves
Portability honnêtes sans certifier les recettes runtime historiques.

Le 2026-10-11, dans cette conversation, l'utilisateur a choisi « 1 » pour ce lot,
puis « 1 » à « Approuver contrat et autoriser lot borné ». Le contrat incluait
explicitement garde-fous Portability, retrait des garanties non démontrées, tests
statiques et validation du site avec installation verrouillée dans ce worktree.
Cette preuve autorise les modifications ci-dessous, pas une tâche de README ou
portabilité dans un autre dépôt ni une livraison Git. Aucun nouveau terme ou
compromis architectural durable ne nécessite de nouvel ADR.

## Périmètre et isolation

Base actualisée : `bb67c5b4f542f40bce86c26ea616cf28fb4f85c0`, contenant PR #96 et
PR #97 fusionnées. Branche `codex/engineering-documentation-portability`, worktree
`.worktrees/codex/engineering-documentation-portability`.

Neuf fichiers : deux SKILL, trois références directement concernées, deux fichiers
de scénarios, un test statique et ce contrat. Pas de nouveaux skills ou de changement
de metadata publiée, d'instructions actives ou de site.

Exclus : audit/certification/refonte des recettes Node/Bun, migrations réelles,
changements globaux, installation de kits dans projets réels, tests modèles/hôtes,
revue indépendante, staging, commit, push, PR, merge et déploiement. Installation
des dépendances déjà verrouillées du site uniquement pour validations approuvées.

## Décisions et invariants

- Activation avant lecture/délégation dans kit explicite ; chaque dépendance a son
  gate. Defaults publiés inchangés ; aucun nouveau Interview obligatoire.
- Questions : état actuel, options numérotées, recommandation et réponse localisés,
  sans IDs ni consentement présumé. Rapports, candidats et wireframes distincts.
- README : entretien spécialisé, accords et architecture actuels indépendamment
  approuvés réutilisés ; réouvrir seules décisions invalidées. Toujours approbation
  du candidat exact et de la destination immédiatement avant écriture. README seul,
  protection des fichiers générés et gate modèle/délégation préservés.
- Portability : inspection lecture seule puis accord borné avant modification.
  Scripts/callers nécessaires, OS/shells/runners et comportements à préserver
  explicitement sélectionnés ; aucun programme global sous requête ponctuelle.
- Retrait de helper conditionné à adéquation/compatibilité prouvée, pas purge
  axiomatique. Installation/lockfile, réseau, tests destructifs et écriture du rapport
  gardent leurs permissions séparées. Nettoyage seulement sur chemins approuvés,
  jamais recursive-force imposé universellement ; dry-run non présumé inoffensif.
- Compatibilité seulement selon exécutions effectivement observées. Syntaxe et
  émulation ne prouvent pas exécution native d'un autre OS. Gains non mesurés et
  cibles non vérifiées restent explicitement tels quels.
- Guide corrigé aux mêmes frontières : retirer obsolescence universelle, timings et
  zéro-spawn garantis ; distinguer échappement shell et validation d'arguments.
  Recettes conservées comme illustrations historiques non certifiées, à vérifier
  par documentation actuelle et tests avant application réelle.
- Rapport dans chat par défaut ; fichier facultatif après approbation contenu et
  destination. Recommandations non présentées comme changements exécutés.

Sources : [architecture](software-engineering-skill-architecture.md),
[politique](../../.agents/invocation.md),
[README](../../skills/repository-readme-architect-acrazie/SKILL.md),
[Portability](../../skills/script-portability-acrazie/SKILL.md).

## Critères et preuves

- C1, kit/format/reprise : **12 nouveaux tests statiques réussis**. Première
  exécution : neuf échecs et une erreur, dont une assertion de fixture incorrecte
  exigeant metadata `true` explicite alors que l'omission autorise aussi invocation.
  Assertion corrigée sans modification de metadata ; les autres échecs concernent
  instructions/scénarios manquants. Pas preuve d'exécution réelle d'un agent.
- C2, régressions : 10 décisions, 12 compléments, neuf stratégie Modernizer,
  14 noyau, 33 activation, 16 permissions et 11 contrat Git Ship réussis.
  Avec le lot nouveau : **117 tests Python réussis**.
- C3, site : installation frozen-lockfile, cinq tests invocation, huit sélection
  modèle, build **87 pages**, 18 tests graphe réussis. **148 tests automatisés au
  total**. Section de gate modèle README identique à la base et aux autres porteurs.
  Manifest/lockfile et metadata/frontmatters des deux skills identiques à la base.
- C4, périmètre/hygiène : frontmatter/structure, parsing YAML du catalogue,
  30 liens README, liens locaux, AST/JSON, whitespace et allowlist de neuf fichiers
  contrôlés ; `git diff --check` réussi, index vide. Aucune déclaration du graphe
  ne cite ces skills ; aucune arête ajoutée.
- C5, limites : sept scénarios documentés (trois README, quatre Portability),
  non exécutés par modèle/hôte. Aucun benchmark/runtime matrix, Docker build/smoke
  ou revue indépendante. Ne pas transformer tests textuels en certification de
  recettes, d'exécution Windows ou de sécurité shell.

Les gates ne sont pas des contrôles d'accès filesystem ; homonymes globaux et
comportement live des hôtes restent non vérifiés. Worktree conservé sans livraison
Git ni activation réelle.

Commande ciblée, depuis le worktree :

```bash
python3 -B skills/script-portability-acrazie/scripts/test_engineering_documentation_contract.py
```
