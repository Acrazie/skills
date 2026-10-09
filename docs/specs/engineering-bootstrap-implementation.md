# Premier lot : amorçage engineering complet

## Contrat approuvé

Date : 2026-10-09. L'utilisateur a choisi amorçage complet, Codex + Claude Code,
configuration et packages suivis dans Git, conservation des personnalisations et
essais uniquement dans dépôts temporaires. Après découverte documentaire, il a
choisi activation explicite de chaque skill, `.acrazie/engineering.json`, copie
canonique et liens relatifs, import/arbitrage des politiques existantes et tests
automatisés uniquement. Il a répondu « ok » au contrat final autorisant ce lot.

Cet accord autorise modification des deux propriétaires existants,
`github-repo-init-acrazie` et `git-ship-acrazie`, avec références, helpers, tests et
documents nécessaires, dans le worktree isolé existant. Aucun staging Git,
commit, push, PR, merge, déploiement ou activation dans un projet réel.

Exclus : CLI Acrazie dédiée, nouveaux skills, site, changement global des
métadonnées d'invocation, configuration globale et essais live Codex/Claude Code.

## Objectif et responsabilités

- Repo Init possède mode activation sans scaffolding forcé, interview au format
  validé, configuration, sélection, installation et préservation des instructions.
- CLI Skills existante possède acquisition/copie initiale dans staging externe.
- Helper Repo Init possède intégration ciblée, preuves de contenu, ownership,
  plan exact, revalidation et readback. Il ne décide pas à la place de l'utilisateur.
- Git Ship possède évaluation des permissions de livraison sous conditions,
  toujours avec récapitulatif et preuve de snapshot. Aucun moteur d'orchestration.

Sources et compromis : [architecture](software-engineering-skill-architecture.md),
[ADR 0008](../adr/0008-explicit-project-kits-and-policy-preauthorization.md),
[mode activation](../../skills/github-repo-init-acrazie/references/engineering-activation.md),
[contrat JSON](../../skills/github-repo-init-acrazie/references/engineering-configuration.md),
[politique de livraison](../../skills/git-ship-acrazie/references/repository-action-policy.md).

## Critères et preuves attendues

- C1 : demande d'activation orientée vers propriétaire existant, distincte de
  scaffolding, sans publication implicite. Preuve : instructions et métadonnées.
- C2 : question à quatre champs ; sélection, hôtes et pins explicites, contrat
  complet avant mutations. Preuve : validation documentaire et request parser.
- C3 : installation projet versionnée ; copie canonique, liens relatifs, flags
  explicit-only adaptés localement et lock des octets réellement installés.
  Preuve : fixtures et intégration bornée de l'installateur.
- C4 : contenu personnalisé conservé, conflits bloqués, réapplication identique,
  update/désélection limitée aux assets inchangés possédés. Preuve : tests temporaires.
- C5 : permissions distinctes, préautorisation uniquement sous preuve indépendante,
  identité et snapshot exacts ; restriction ponctuelle prioritaire. Preuve : tests
  du helper d'éligibilité et contrat d'instructions Git Ship.
- C6 : périmètre respecté, aucun faux résultat live ou remote. Preuve : diff,
  état Git, liens locaux et limites explicitement rapportées.

## Validation locale

- C1–C2 : mode et metadata Repo Init mis à jour ; format de questions contrôlé,
  request JSON strict et pins/permissions séparés. YAML des frontmatters modifiés
  et metadata Codex parsé ; parité des 26 packages publiée inchangée.
- C3–C4 : 33 tests offline d'activation réussis : plan sans mutation, installation,
  hashes et flags, liens locaux, réapplication depuis configuration persistée,
  personnalisation, collisions, provenance/hash de staging, locks, politique
  modifiée, plan périmé, update/désélection et arrêt sur échec partiel.
- C5 : 16 tests d'éligibilité des permissions et 11 tests du contrat Git Ship
  réussis. Checks/snapshot, source indépendante d'approbation, restriction actuelle,
  scope exact, action isolée, configuration invalide et absence de policy couverts.
  Total : **60 tests automatisés réussis**. Les définitions d'evals ont été enrichies,
  mais aucun run de modèle, benchmark ni revue indépendante n'a été effectué.
- Intégration réelle bornée : CLI `skills@1.7.2` exécutée dans staging temporaire,
  source `Acrazie/skills#2e624a229405a806fba22e562a3c1bc5bf4e3b59`, sélection
  Interview + Feature Builder. Plan/apply dans un dépôt Git temporaire : 14 paths
  appliqués, policy existante conservée, liens et YAML explicit-only relus,
  hashes du lock adaptés vérifiés, réapplication no-op, aucun commit créé.
  SHA-256 du plan initial :
  `d5adbf2d9bc19662373f7b2417cc7ccf25e8c68545473e825e8b4858a7759f52`.
  Ce test ne lance aucun hôte et ne teste pas toutes les sélections possibles.
- C6 : hooks frontmatter et structure réussis ; `git diff --check`, parsing AST/JSON,
  espaces finaux et 71 liens locaux des fichiers modifiés contrôlés. Exactement
  20 fichiers changés : six documents et 14 fichiers dans les deux packages
  autorisés, incluant la phase documentaire précédente. Index vide ; site et
  instructions actives du checkout inchangés. Aucun commit/push/PR/merge/deploy
  ni activation dans un projet réel.

Empreinte SHA-256 du contenu des 14 fichiers des skills, chemins triés suivis de
NUL puis octets de chaque fichier :
`fff652ca09c6202d1760426e8d0eb4f726d6ffe6abf85678342f03c58717b135`.
Ce n'est ni un SHA Git ni la preuve d'un commit/staging. Validation exécutée avec
Python 3.14.3 et Node 26.8.1 ; metadata vérifiée avec Ruby/Psych.

Les observations simulées d'approbation des fixtures ne constituent pas autorisation
dans un vrai dépôt. Tests et flags ne prouvent pas comportement live d'un hôte.
La suite du site et son build n'ont pas été lancés : site exclu, dépendance locale
`gray-matter` absente. Le garde textuel existant du récapitulatif Git Ship a été
contrôlé séparément, sans revendiquer réussite de toute cette suite.

## Risques et limitations acceptés

- Les hôtes n'ont pas été lancés. Métadonnées explicit-only et instructions ne
  sont pas un contrôle d'accès filesystem. Homonymes/global plugins ou hôte
  non inventorié empêchent de promettre un gate exclusif ; ne pas les modifier ici.
- Un grant persistant nécessite preuve indépendante d'approbation humaine.
  Les helpers ne découvrent ni consentement, ni conflits sémantiques dans une prose,
  ni protections distantes. Le caller doit produire des observations vérifiées.
- Plan/apply n'est pas transaction multi-fichiers ; interruption ou concurrence
  externe nécessite inspection et récupération approuvée, pas rollback automatique.
- Metadata adapter borné au layout Acrazie ; formats inattendus bloqués.
- Installer pin ne gèle pas dépendances npm transitives. Télémétrie désactivée
  désactive aussi audit API Skills ; aucun audit externe n'est revendiqué.
- Merge/déploiement : politique configurable, mais aucun exécuteur nouveau livré.
