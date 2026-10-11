# Consolidation du propriétaire CI/CD

> Consolidation réalisée dans le lot courant : `ci-cd-acrazie` remplace les six
> packages Jenkins. Les références historiques ci-dessous restent liées à la base
> observée, pas présentées comme packages encore disponibles. Voir
> [contrat et preuves](cicd-consolidation-implementation.md).

## Contrat documentaire et approbation

Le 2026-10-11, l'utilisateur a validé le périmètre CI/CD du dépôt, puis « 1 et 1 et
1 et 1 » pour les opérations distantes séparément autorisées, le support ouvert par
preuves, le retrait des six packages sans redirections et la partition avec Repo
Init/Modernizer. Il a ensuite répondu « 1 » à l'approbation du nom `ci-cd-acrazie`
et d'une rédaction documentaire bornée. Cette dernière autorise trois documents,
pas le remplacement effectif des skills.

Base actualisée : `2aa64de467698f16ad91ddb50491908a1edb23e3`, après PR #99 fusionnée.
Branche `codex/cicd-consolidation-architecture`, worktree dédié
`.worktrees/codex/cicd-consolidation-architecture`.

Inclus : ce contrat, [ADR 0010](../adr/0010-consolidate-repository-cicd-ownership.md)
et termes ciblés du [glossaire](../../CONTEXT.md). Exclus : modification/suppression
ou création de skills/metadata, site, scripts, instructions actives, installations,
opérations CI/CD, staging, commit, push, PR, merge et déploiement. Aucun installateur,
plugin, moteur générique ou CLI n'est conçu ici. Réalisation et livraison auront
leurs périmètres/permissions séparés.

## État observé et prior art

L'inventaire de cadrage en lecture seule a inspecté 141 refs locales/remote-tracking,
74 versions distinctes de SKILL.md et 26 identifiants. Il n'a trouvé aucun propriétaire
CI/CD générique concurrent. Les refs distantes n'étaient pas réactualisées lors de
cet inventaire ; il ne démontre pas l'absence d'un travail non récupéré sur GitHub.
Seul `main` a ensuite été actualisé pour créer ce worktree.

Le [parent Jenkins](https://github.com/Acrazie/skills/blob/2aa64de467698f16ad91ddb50491908a1edb23e3/skills/jenkins-devops-acrazie/SKILL.md) possède déjà
inspection, décision, approbation, réalisation, diagnostic et validation. Il permet
explicitement de continuer sans spécialistes. Les interprètes
[Go](https://github.com/Acrazie/skills/blob/2aa64de467698f16ad91ddb50491908a1edb23e3/skills/jenkins-go-acrazie/SKILL.md),
[JS/TS](https://github.com/Acrazie/skills/blob/2aa64de467698f16ad91ddb50491908a1edb23e3/skills/jenkins-js-ts-acrazie/SKILL.md),
[Python](https://github.com/Acrazie/skills/blob/2aa64de467698f16ad91ddb50491908a1edb23e3/skills/jenkins-python-acrazie/SKILL.md),
[Rust](https://github.com/Acrazie/skills/blob/2aa64de467698f16ad91ddb50491908a1edb23e3/skills/jenkins-rust-acrazie/SKILL.md) et
[Symfony/PHP](https://github.com/Acrazie/skills/blob/2aa64de467698f16ad91ddb50491908a1edb23e3/skills/jenkins-symfony-php-acrazie/SKILL.md) apportent contraintes
et provenance des commandes, pas cinq workflows indépendants d'implémentation.
Tous ces packages existent encore et conservent leurs gates actuels.

Le [graphe](../../site/src/lib/skill-graph.ts) contient cinq appels Jenkins vers
spécialistes avec citations source exactes ; retirer les packages sans modifier
les déclarations casse leur résolution. La consolidation est donc plus qu'un
renommage. Ce document remplace la cible de la famille Jenkins dans
[l'architecture engineering initiale](software-engineering-skill-architecture.md),
sans réécrire ses preuves historiques ni modifier ses autres propriétaires.

## Propriétaire cible et frontières

`ci-cd-acrazie` possède une tâche complète sur un seul dépôt : concevoir, réparer,
moderniser et valider son pipeline, ainsi que conduire les opérations CI/CD
explicitement demandées et autorisées. CI seule, publication, livraison contrôlée
et déploiement sont des capacités distinctes ; non demandée signifie non applicable,
pas une obligation de construire une chaîne production.

Hors périmètre : administration de contrôleurs/plateformes, installation de plugins,
configuration de runners globaux, provisioning ou administration cloud et infrastructure.
Des références cloud/VM/Compose/Kubernetes peuvent décrire une interface existante
de déploiement sans autoriser la création de cette infrastructure. Si une opération
nécessite une capacité absente, bloquer cette étape et proposer le travail séparé,
pas transformer silencieusement le pipeline en programme DevOps.

## Support ouvert, connaissances ciblées

Le noyau porte inspection, clarification adaptée, contrat applicable, provenance,
frontières de confiance, artefacts immuables, gates et preuves. Les particularités
Jenkins, autres fournisseurs CI et stacks vivent dans des références internes
chargées seulement si pertinentes. Aucun package par langage/outil, dépendance
inter-skill artificielle, résolveur ou interface exécutable universelle n'est requis.

Un outil non répertorié n'est pas automatiquement exclu : découvrir configuration,
version, interface et documentation actuelle avant de proposer commandes ou edits.
Un fournisseur connu n'est pas automatiquement vérifié. Recettes existantes sont
savoirs candidats à réexaminer, pas commandes certifiées ; ne pas inventer build,
test, publication, déploiement ou rollback par convention de langage. Vérifier
les sources projet et documenter ce qui reste inconnu. Une preuve indisponible
bloque l'étape dépendante, sans bloquer toute découverte sûre.

## Autorisation et vérification

Appliquer la [politique d'invocation](../../.agents/invocation.md) : dans un kit
explicite, activation séparée de chaque skill avant lecture/délégation et retour
au propriétaire après un handoff. Les références internes font partie du skill
activé ; leur lecture pertinente n'est ni activation d'un autre skill ni permission
de télécharger/installer/exécuter leurs exemples.

Réutiliser l'accord actuel indépendamment approuvé et les décisions compatibles ;
clarifier seulement les éléments non résolus/invalidés. Questions à quatre champs
localisés : état actuel, options numérotées, recommandation, réponse. Une proposition
ou étiquette de statut n'est pas consentement. Un ADR n'est nécessaire que pour
un choix durable justifiant ses compromis, pas pour chaque réparation.

Séparer edits locaux, checks à effets, réseau/lectures distantes, installation,
spawning/modèles, staging/commit/push/PR et opérations CI/CD. Respecter permissions
ponctuelles et éventuelles préautorisations indépendamment prouvées, avec leurs
conditions et protections ; le skill ou une configuration proposée ne s'octroie
aucun droit. Une permission de déploiement n'autorise pas toutes opérations annexes.

Pour déclenchement, publication, promotion, déploiement, abort ou rollback : établir
cible exacte, révision/artefact immuable, données transmises, effets, prérequis,
checks, limites et conditions de validité de l'enveloppe autorisée. Les opérations
production et leurs effets destructifs/data restent distinctement autorisés ;
rollback n'est pas permission implicite de supprimer ou restaurer des données.
Après mutation distante, lire l'état cible et vérifier avant annonce ou retry d'une
requête ambiguë non idempotente. Une interface indisponible donne un résultat bloqué
ou un modèle de commande non secret pour l'utilisateur, pas un succès inventé.

Préserver séparation source fiable/contribution non fiable et ne pas exposer
credentials de publication/signature/production aux builds non fiables. Ne jamais
demander, afficher ou persister valeurs secrètes. Planifier identité immuable,
provenance, promotion sans rebuild, comportement d'échec et rollback vérifiable.
Checks statiques/linter, exécution CI, publication et déploiement live sont preuves
différentes ; rapporter snapshot, commande, environnement, résultats et limites.

## Partition avec les autres propriétaires

| Propriétaire | Conserve | Transfert au propriétaire CI/CD |
| --- | --- | --- |
| Repo Init | Configuration et bootstrap minimal du dépôt, sélection/activation du kit et politique d'actions | Pipeline substantiel, intégrations, promotion ou diagnostic complexe ; pas workflow parallèle concurrent |
| Repo Modernizer | Audit et plan global de modernisation, identification des unités et gates | Réalisation des changements CI/CD substantiels, avec son accord applicable |
| Audit Repository | Évaluation technique bornée, recommandation | Réalisation CI/CD après décision et autorisation ; jamais implémentation sous audit |
| Script Portability | Scripts multiplateformes sélectionnés | Orchestration pipeline et interfaces CI/CD ; pas propriétaire implicite de Jenkinsfile/workflows |
| Feature Builder / Test Retrofitter | Comportement applicatif/tests dans leurs frontières | Création, migration et réparation substantielles du pipeline |
| Git Ship | Actions Git/PR séparément demandées | Ne devient pas exécuteur CI/CD du seul fait qu'une PR est prête |

Un handoff transmet scope, contrat, décisions, preuves et permissions applicables,
pas une nouvelle autorisation ou activation. Le seuil bootstrap minimal versus
travail substantiel devra être rendu concret dans le contrat de réalisation : un
gabarit établi sans nouvelles décisions de pipeline n'autorise pas une intégration
spécifique, une architecture de promotion ou une opération distante.

## Retrait et migration des consommateurs

La réalisation future devra créer le propriétaire puis retirer les six packages
Jenkins du catalogue courant dans un changement cohérent. Pas de redirections
transitoires ni migration automatique de kits ou installations existantes.
Révisions pinnées et historique restent consultables ; un ancien kit peut continuer
à utiliser sa révision jusqu'à sa mise à jour explicitement approuvée.

Publier une correspondance des six identifiants vers le propriétaire unique ;
expliquer déplacement des références, choix/permissions à préserver, destinations
et validation avant toute mise à jour de kit. L'installateur actuel est générique,
mais une sélection enregistrée n'est pas réécrite par simple renommage de package.
Le script de liens globaux ne retire pas les anciens liens : ne pas l'exécuter
pour nettoyer cette transition ; toute suppression/réparation globale a son accord.
Les URLs existantes peuvent cesser d'exister ; ne pas prétendre compatibilité
transparente sans dispositif approuvé. Ne pas altérer des commits historiques.

## Surfaces à traiter lors de la réalisation

- Packages, metadata, assets et références : préserver seulement savoirs pertinents
  et provenances, réexaminer recettes ; ne pas copier en bloc promesses obsolètes.
- README/catalogues localisés et catégorie CI/CD du site ; graphe et ses cinq appels,
  hub Jenkins, preuves source et tests d'invocation ciblant anciens spécialistes.
- Handoffs/exclusions et références actives des propriétaires voisins ; instructions
  actives et lien illustratif SECURITY si touchés doivent être explicitement inclus.
- Glossaires/architecture actifs versus contrats historiques : corriger cible et
  liens actifs sans fabriquer rétrospectivement preuves de la nouvelle réalisation.
- Sélections/versions de kits consommateurs et liens globaux : hors remplacement
  bibliothèque par défaut, toujours migration séparément autorisée.

Ce relevé définit impacts, pas autorisation d'éditer ces surfaces. Pas de preuve
que tous fournisseurs/langages fonctionnent. Scénarios futurs : CI-only sans
production, fournisseur inconnu/documentation insuffisante, contribution non fiable,
commande sans provenance, publication/déploiement non autorisés, réponse distante
ambiguë, rollback à effet data, reprise de contrat, handoff explicite, package retiré
et kit pinné inchangé. Définir validations et preuves dans contrat d'implémentation.

## Critères et preuves documentaires

C1 : trois fichiers autorisés seulement ; aucun skill/site/instruction active modifié.
C2 : quatre choix et nom approuvés fidèlement décrits ; actuel et cible distingués.
C3 : ADR explique compromis et migration, glossaire uniquement termes/rôles.
C4 : liens locaux/whitespace et structure existante vérifiés ; index vide.
Aucun build/runtime, opération CI/CD ou scénario modèle/hôte n'est requis ou prouvé
par cette livraison documentaire.


## Preuves de cette phase

- C1 : allowlist exacte de trois fichiers contrôlée ; 26 packages toujours présents,
  aucun `skills/ci-cd-acrazie` créé, skills/site/instructions actives inchangés.
- C2 : quatre réponses et nom validés confrontés au cadrage ; retrait et opérations
  décrits comme cible future, pas résultats déjà effectués.
- C3 : ADR 0010 motive propriétaire unique versus famille/plugin, retrait sans
  redirections et coût de migration ; glossaire conserve termes existants comme
  vocabulaire de transition et distingue propriétaire cible/références/enveloppe.
- C4 : **12 liens locaux vérifiés**, structure des skills existants valide,
  whitespace/diff check réussis, index vide. HEAD/base inchangé.

Aucun test modèle/hôte, build/site/runtime, installation, déclenchement pipeline,
publication ou déploiement exécuté. Aucun staging/commit/push/PR/merge. Worktree
conservé ; les preuves sont documentaires locales, sans revue indépendante.
