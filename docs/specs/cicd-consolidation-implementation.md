# Réalisation du propriétaire CI/CD unique

## Autorisation et isolation

Le 2026-10-11, après architecture approuvée, l'utilisateur a demandé « go implementer »
puis choisi « 1 » au contrat de réalisation complète bornée. Celui-ci autorise
création de ci-cd-acrazie, remplacement des six packages Jenkins sans redirections,
références internes, handoffs de six voisins, surfaces actives de documentation/
instructions/site/tests, trois documents de cadrage, ce contrat et installation
verrouillée du site dans ce seul worktree. Pas d'autorisation d'opération CI/CD réelle
ou de livraison Git.

Worktree réutilisé : `.worktrees/codex/cicd-consolidation-architecture`, branche dédiée
`codex/cicd-consolidation-architecture`, base
`2aa64de467698f16ad91ddb50491908a1edb23e3`. Les trois documents de cadrage étaient
non indexés ; aucun travail tiers ou changement d'index n'a été absorbé.

[Architecture](cicd-consolidation-architecture.md),
[ADR 0010](../adr/0010-consolidate-repository-cicd-ownership.md),
[propriétaire](../../skills/ci-cd-acrazie/SKILL.md).

## Réalisation et invariants

- Un package ci-cd-acrazie remplace les six anciens ; 21 packages courant au lieu de 26.
  Aucun plugin/runtime/CLI, aucune redirection, aucun nouveau logo.
- Entrée commune courte ; références ciblées stack, Jenkins, décisions, validation,
  opérations et six interfaces de déploiement existantes. Pas de chargement global
  de références ou de nouveau spécialiste par fournisseur/langage.
- Savoirs candidats conservés/réexaminés, pas certification de recettes. Context7
  Jenkins consulté pour linter, libraries fiables et fuite via scripts de forks.
  Outils non listés demandent documentation/capacités actuelles avant génération.
- Kits explicites, reprise de contrat indépendant, quatre champs localisés, gates
  d'edits/checks/installations/réseau/spawning/Git/opérations distantes conservés.
  Linter, run, publication et déploiement sont preuves distinctes ; read-back avant
  annonce/retry et autorisation des effets de rollback, pas données implicitement.
- Repo Init garde bootstrap minimal défini par template établi/décisions existantes ;
  Modernizer garde inspection/plan global. Leurs handoffs substantiels passent au
  propriétaire unique sans réinterview ni activation implicite. Quatre autres voisins
  conservent tâches propres et exclusions CI/CD.
- Cinq arêtes vers spécialistes retirées ; deux handoffs conditionnels réels vers
  CI/CD ajoutés avec citations source exactes. Graphe : quatre relations au total,
  pas d'arêtes pour références internes ni hub Jenkins artificiel.
- Catalogue trois langues, catégorie, README, SECURITY et exemples AGENTS/invocation
  actualisés. Archives de sources Jenkins dans architecture remplacées par liens
  immuables à la base observée ; preuves historiques non réinventées. ADR reste
  l'approbation de conception, pas la preuve de réalisation ou de publication.
- Trois fixtures synthétiques Jenkins déplacées sans exécution ; log renommé .txt.
  Neuf scénarios documentés : trois existants adaptés, six nouveaux couvrant provider
  inconnu/CI-only, confiance, réponse distante ambiguë, rollback data, reprise et kit
  pinné. Aucun scénario exécuté par modèle/hôte.

## Périmètre et exclusions

Inclus : package ci-cd-acrazie et retrait des six packages, six SKILL voisins,
deux références Repo Init et protocole Modernizer, README/CONTEXT/SECURITY/AGENTS/
invocation, architecture active, trois documents de cadrage/contrat, trois modules
site et trois tests site. Fixtures/assets anciens supprimés seulement dans ce
worktree et objets Git historiques préservés.

Exclus : migration de kits/installations/symlinks globaux, nouveaux logos, opérations
CI/CD réelles, administration plateformes/cloud/runners, tests modèles/hôtes, revue
indépendante, Docker smoke, staging/commit/push/PR/merge/déploiement. Les liens/versions
consommateurs sont inchangés ; aucune mise à jour transparente prétendue.

## Critères et preuves

C1 : un propriétaire, aucune ancienne entrée/package actif, scopes/handoffs cohérents.
C2 : gates et provenance explicites ; référence interne non assimilée à skill/plugin.
C3 : catalogue/graphe/support de kits générique, metadata/frontmatter/JSON/liens valides.
C4 : suites statiques et site plus build ; limites runtime et erreurs réelles rapportées.
C5 : allowlist, historique/versions/outillage/index/installations externes préservés.

Preuves finales à compléter après contrôles. Première passe Python : nouveaux
19 tests et régressions réussis. Premier build réussi ; trois tests sortie graphe
échouaient sur ancien compteur codé 7. Régression ajustée à la comparaison des
relations source réelles (quatre), pas désactivée. Une commande de test lancée
au cwd racine au lieu de site a échoué « Script not found » sans modification ;
relancée ensuite dans site. Aucune recette fixture exécutée pour contourner un gate.


## Preuves finales

- C1/C2 : **19 nouveaux tests statiques réussis**, unité unique/gates/provenance,
  CI-only, confiance, artefacts/runners, scope administratif, enveloppe distante,
  rollback data, niveaux de preuve, revue, stacks/Jenkins, handoffs et migration.
- C3 : trois nouveaux tests site couvrent catégorie/catalogues trois langues et
  handoffs exacts. Parsing YAML du catalogue, JSON/AST, **108 liens locaux** des
  surfaces concernées et **26 liens README** vérifiés. Versions/lockfile, linker
  global et scripts d'installation de kits inchangés.
- C4 : **138 tests Python réussis** (119 existants + 19 nouveaux), **34 tests site**
  (7 invocation/catalogue, 8 sélection modèle, 19 graphe/sortie), total **172 tests**.
  Build **72 pages**, correspondant à retrait de cinq packages nets, sans anciennes
  routes Jenkins. Installation frozen-lockfile autorisée, manifest/lockfile inchangés.
- C5 : allowlist bornée contrôlée ; 21 packages, aucun package Jenkins résiduel,
  structure/frontmatter/whitespace validés, index vide. Pas de fichier interne,
  campagne, preview ou installation externe ajouté dans le périmètre.

Ces preuves sont statiques/locales. Neuf scénarios non exécutés ; aucun test
modèle/hôte, run fournisseur, publication/déploiement/rollback, certification
recettes runtime ou revue indépendante. Worktree conservé sans livraison Git.
