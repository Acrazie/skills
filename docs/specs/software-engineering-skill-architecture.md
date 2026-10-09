# Architecture des skills software engineering

## Contrat et approbation

Statut : architecture approuvée, implémentation non autorisée par ce document.
Date : 2026-10-09.

Révision après découverte des hôtes : l'utilisateur a ensuite choisi invocation
explicite pour chaque skill et dépendance, configuration
`.acrazie/engineering.json`, copies canoniques avec liens Claude relatifs, et tests
automatisés seulement. [ADR 0008](../adr/0008-explicit-project-kits-and-policy-preauthorization.md)
remplace confirmation unique de chaîne. La réalisation du premier lot possède
son [contrat séparé](engineering-bootstrap-implementation.md) ; les exclusions et
preuves de la première phase documentaire restent historiques.

L'utilisateur a validé les décisions Q1–Q19 de cette conversation, corrigé Q17
pour limiter le format des questions à quatre champs, puis répondu « ok » au
contrat documentaire final. Cette approbation autorise uniquement la rédaction
de l'architecture, du glossaire et des ADR dans le worktree isolé
`.worktrees/codex/software-engineering-architecture`.

L'objectif est de recentrer le catalogue sur le software engineering, en gardant
des propriétaires indépendants pour les tâches indépendantes et des relations
explicites entre les workflows complémentaires. Les compétences visuelles et la
maintenance des agents restent des satellites, sans retrait automatique.

### Périmètre de cette livraison

- Classer les skills existants sans déplacer ni renommer leurs packages.
- Définir sélection, confirmation de chargement, clarification, réalisation,
  vérification, amorçage du dépôt et permissions de livraison.
- Documenter les dépendances, les lacunes et les divergences avec l'état actuel.
- Ne modifier aucun skill, métadonnée d'invocation, script, site ou instruction
  active du dépôt. Ne construire ni CLI ni moteur d'orchestration.
- Ne rien installer, committer, pousser, publier, merger ou déployer.

Le contrat n'autorise pas la mise en œuvre future : celle-ci nécessite son propre
périmètre approuvé. Une architecture approuvée n'est pas une garantie runtime.

## État observé et sources

L'exploration initiale a inspecté 127 refs locales et remote-tracking, 26
identifiants et 60 versions distinctes de `SKILL.md`, sans accès réseau. Après
approbation documentaire, `origin/main` a été actualisé et le worktree créé depuis
`2e624a229405a806fba22e562a3c1bc5bf4e3b59`. Ce snapshot contient 26 skills.
Les autres branches distantes n'ont pas été intégralement réactualisées ; cet
inventaire ne prouve pas l'état actuel de toutes les branches sur GitHub.

Sources responsables : [politique d'invocation](../../.agents/invocation.md),
[contrat initial](software-development-skill-tree.md),
[Interview](../../skills/interview-acrazie/SKILL.md),
[Repo Init](../../skills/github-repo-init-acrazie/SKILL.md),
[Git Ship](../../skills/git-ship-acrazie/SKILL.md) et
[glossaire](../../CONTEXT.md).

Le socle Interview/Feature Builder et plusieurs dépendances existent déjà. Le
[graphe du site](../../site/src/lib/skill-graph.ts) représente certaines relations,
mais n'est ni exhaustif ni un exécuteur. Aucun installateur CLI Acrazie ou registre
projet des skills installés n'a été identifié. Le
[script de liaison contributeur](../../scripts/link-skills.sh) lie tous les skills
globalement ; il ne répond pas à l'installation sélective dans un projet.

Correction après actualisation : l'ancien snapshot de Git Ship imposait certaines
conventions fixes. Le snapshot actualisé possède une livraison adaptable et une
validation du contenu exact. Il exige toutefois encore une approbation explicite
du récapitulatif ; la reconnaissance d'une préautorisation persistante reste à
concevoir. Merge automatique et déploiement restent exclus de son périmètre.

## Catalogue et responsabilités

Ce classement est conceptuel. Les 26 identifiants et chemins restent inchangés.

| Famille | Propriétaires existants | Responsabilité et frontière |
| --- | --- | --- |
| Cadrage | [interview-acrazie](../../skills/interview-acrazie/SKILL.md) | Décisions manquantes et contrat approuvé ; aucune implémentation. |
| Décisions techniques | [audit-repository-acrazie](../../skills/audit-repository-acrazie/SKILL.md) | Évaluation technique bornée dans un dépôt ; pas revue de diff ni implémentation. |
| Décisions produit | [product-critic-acrazie](../../skills/product-critic-acrazie/SKILL.md) | Valeur, usage et coût des fonctionnalités ; recommandations, pas modifications. |
| Réalisation | [feature-builder-acrazie](../../skills/feature-builder-acrazie/SKILL.md) | Nouveau comportement applicatif et ses tests ; pas bug-fix ni refactor. |
| Tests existants | [test-retrofitter-acrazie](../../skills/test-retrofitter-acrazie/SKILL.md) | Tests sur comportement existant insuffisamment couvert ; pas correction fonctionnelle implicite. |
| Vérification | [adversarial-reviewer-acrazie](../../skills/adversarial-reviewer-acrazie/SKILL.md) | Revue indépendante de changements ; aucune implémentation de correction. |
| Configuration et amorçage | [github-repo-init-acrazie](../../skills/github-repo-init-acrazie/SKILL.md) | Configuration du dépôt ; futur mode d'activation engineering sans scaffolding imposé. |
| Livraison | [git-ship-acrazie](../../skills/git-ship-acrazie/SKILL.md) | Actions Git/PR demandées et prouvées ; pas réalisation, merge automatique ou déploiement actuels. |
| Documentation du dépôt | [repository-readme-architect-acrazie](../../skills/repository-readme-architect-acrazie/SKILL.md) | README principal ; pas toute documentation générique. |
| Modernisation | [repo-modernizer-acrazie](../../skills/repo-modernizer-acrazie/SKILL.md) | Modernisation demandée ; pas mises à niveau opportunistes. |
| Automatisation portable | [script-portability-acrazie](../../skills/script-portability-acrazie/SKILL.md) | Scripts multiplateformes et frontières shell ; pas migration globale ou Jenkins. |
| Migration de langage | [mechanical-port-acrazie](../../skills/mechanical-port-acrazie/SKILL.md) | Port mécanique avec oracle ; pas réécriture ou refactor dans un même langage. |
| Diagnostics massifs | [diagnostic-queue-runner-acrazie](../../skills/diagnostic-queue-runner-acrazie/SKILL.md) | Files massives de diagnostics ; pas débogage ponctuel. |
| Mémoire runtime | [memory-leak-diagnostician-acrazie](../../skills/memory-leak-diagnostician-acrazie/SKILL.md) | Fuites runtime démontrées ; pas audit statique ou bug-fix général. |
| CI/CD Jenkins | [jenkins-devops-acrazie](../../skills/jenkins-devops-acrazie/SKILL.md) | Pipelines du dépôt ; pas administration du contrôleur. |
| Interprétation Jenkins | [jenkins-go-acrazie](../../skills/jenkins-go-acrazie/SKILL.md), [jenkins-js-ts-acrazie](../../skills/jenkins-js-ts-acrazie/SKILL.md), [jenkins-python-acrazie](../../skills/jenkins-python-acrazie/SKILL.md), [jenkins-rust-acrazie](../../skills/jenkins-rust-acrazie/SKILL.md), [jenkins-symfony-php-acrazie](../../skills/jenkins-symfony-php-acrazie/SKILL.md) | Spécialistes de stack pour Jenkins ; pas exécuteurs génériques ni propriétaires du déploiement. |
| Satellites web | [immersive-hero-designer-acrazie](../../skills/immersive-hero-designer-acrazie/SKILL.md), [canvas-banner-designer-acrazie](../../skills/canvas-banner-designer-acrazie/SKILL.md) | Workflows visuels spécialisés ; pas propriétaire générique de toute interface. |
| Satellites vectoriels | [svg-banner-designer-acrazie](../../skills/svg-banner-designer-acrazie/SKILL.md), [svg-icon-designer-acrazie](../../skills/svg-icon-designer-acrazie/SKILL.md) | Bannières, icônes et marques ; pas génération raster ou refonte de site. |
| Planification des agents | [multi-agent-planner-acrazie](../../skills/multi-agent-planner-acrazie/SKILL.md) | Planification demandée ; pas délégation ou exécution automatique. |
| Maintenance des skills | [skill-refiner-acrazie](../../skills/skill-refiner-acrazie/SKILL.md) | Campagne explicitement activée ; pas correction implicite d'un skill. |

Lacunes confirmées : correction générale de bugs et refactor à comportement
constant. Leurs futurs workflows devront respectivement posséder reproduction,
cause racine et tests de régression, ou invariants et preuves de conservation.
Aucun identifiant, package ou développement de ces capacités n'est autorisé ici.
La disponibilité de propriétaires pour merge/déploiement doit être établie avant
de rendre ces actions exécutables ; une permission n'est pas un workflow.

## Sélection, chargement et réalisation

1. À partir de la demande, proposer le spécialiste pertinent, pas une interview
   universelle. Sa sélection peut utiliser les métadonnées disponibles, sans lire
   ses instructions complètes avant confirmation.
2. Dans un kit projet activé, désactiver invocation automatique des copies locales.
   Proposer le skill et ses dépendances sans charger leur corps.
3. Attendre commande explicite utilisateur pour chaque skill : `$skill-name` dans
   Codex, `/skill-name` dans Claude Code. Une activation ne couvre pas les
   dépendances ; chaque passage requiert une nouvelle activation explicite.
4. Réutiliser un contrat explicitement approuvé, actuel et exactement applicable.
   Proposer activation d'Interview si des décisions utilisateur manquent ; ne pas répéter les
   décisions déjà établies ni remplacer l'interview métier d'un spécialiste.
5. Exiger un contrat pour les modifications non triviales. Pour audit ou revue en
   lecture seule, un objectif et un périmètre explicites suffisent. L'absence de
   contrat pour une petite tâche ne dispense jamais des permissions applicables.
6. L'approbation finale du contrat peut autoriser explicitement la réalisation
   prévue par le spécialiste. Interview persiste le contrat puis s'arrête ; il
   n'implémente pas. Le spécialiste reprend uniquement sous cette autorisation.
7. L'exécutant possède tests et validations de ses modifications, en réutilisant
   l'outillage adapté. Test Retrofitter n'est pas une dépendance pour chaque test.
8. Proposer une revue indépendante pour changements ordinaires ; l'exiger lorsque
   workflow ou politique du dépôt l'impose. Une revue acceptée devient un gate
   dont les conditions de réussite doivent être vérifiables.
9. Terminer avec les preuves et limites, puis appliquer les permissions de livraison.

Les instructions de proposition doivent vivre dans le contexte chargé en amont,
notamment `AGENTS.md`, pas uniquement dans un `SKILL.md` déjà lu. Si un hôte charge
automatiquement les instructions avant intervention de l'agent, la promesse
« confirmation avant chargement » n'est pas satisfaite : une configuration hôte
compatible est nécessaire avant activation. Les copies installées adoptent les
réglages explicit-only vérifiés dans la documentation des deux hôtes ; les defaults
de la bibliothèque et les installations globales ne sont pas modifiés. Les homonymes
globalement invocables doivent être résolus avant de prétendre à un gate strict.
Fonctionnement live des hôtes non vérifié. Skill Refiner reste explicit-only.

### Exemple : search bar

Proposer Feature Builder puis attendre son activation explicite. Découvrir le
contexte ; si nécessaire, proposer Interview puis attendre sa propre activation.
Clarifier les décisions manquantes et approuver le contrat, puis demander activation
explicite du spécialiste pour reprendre réalisation. Feature Builder réalise logique et interface dans le
périmètre prévu, produit les tests et propose ou réalise la revue applicable.
Un spécialiste visuel non annoncé nécessite une confirmation supplémentaire.
La livraison suit ensuite les permissions configurées, sans bundle Git implicite.

## Complémentarité et dépendances

Une simple référence recommande un complément ; elle ne constitue pas une
obligation. Une dépendance obligatoire définit son déclencheur, le propriétaire
attendu, le résultat requis, le critère de réussite et l'étape bloquée sans preuve.
Une dépendance conditionnelle est obligatoire lorsque sa condition est vraie.
Ces distinctions doivent rester visibles dans les instructions et validations,
sans nouveau résolveur ou moteur d'exécution dans cette phase.

| Relation observée | Nature actuelle | Résultat ou limite |
| --- | --- | --- |
| Feature Builder / Interview | Obligatoire sans contrat actuel approuvé | Contrat approuvé ; absence d'Interview bloque réalisation. |
| Test Retrofitter / Interview | Systématique, avec réutilisation possible | Contrat pour tests existants ; harmonisation future avec règle générale de réutilisation, sans changer le skill ici. |
| Product Critic / Interview | Conditionnelle | Résolution des décisions utilisateur manquantes. |
| Feature Builder / Adversarial Reviewer | Facultative à proposer, puis gate si acceptée | Résultat indépendant sur snapshot final ; politique peut rendre revue obligatoire. |
| Mechanical Port et Diagnostic Queue Runner / Adversarial Reviewer | Obligatoire | Vérification indépendante exigée par ces workflows. |
| Jenkins DevOps / spécialistes de stack | Facultative | Contraintes de stack ; absence ne bloque pas automatiquement Jenkins. |
| Immersive Hero / contrat Canvas | Conditionnelle au médium | Réutilisation des contraintes Canvas, pas sélection implicite sans confirmation. |

Dépendance obligatoire indisponible : bloquer uniquement l'étape concernée,
expliquer le manque et proposer installation. Ne jamais installer silencieusement
ni imiter le skill manquant. Complément facultatif absent : poursuivre si sûr,
en signalant la limitation. Les confirmations de chargement ne valent pas
autorisation de déléguer à des agents ou d'installer des outils.

## Amorçage engineering du dépôt

Repo Init reste le propriétaire de la configuration, avec un futur mode
« activation engineering sur dépôt existant ». Ce mode n'impose ni nouvelle stack,
ni migration, ni scaffolding, ni GitHub distant. Une CLI Acrazie dédiée est différée.
Un mécanisme d'installation existant sera réutilisé seulement si ses capacités
réelles répondent au contrat, après vérification de sa documentation actuelle.

### Parcours cible

1. Utiliser un Repo Init déjà accessible et explicitement choisi ou confirmé ;
   ne pas dépendre circulairement d'un kit pas encore installé. Son accès initial
   reste un prérequis d'implémentation à documenter, pas une installation autorisée ici.
2. Inspecter dépôt, instructions, skills présents et configurations existantes.
3. Proposer une sélection adaptée, modifiable : Interview + Feature Builder comme
   socle ; tests, revue et livraison selon besoins ; spécialistes selon projet.
   Rendre visibles les dépendances et les capacités non disponibles.
4. Présenter configuration, permissions, destinations d'installation, versions et
   modifications exactes des instructions ; obtenir une validation consolidée.
5. Installer seulement la sélection approuvée dans le projet, sans lien vers un
   checkout personnel. Identifier versions ou révisions ; aucune mise à jour silencieuse.
6. Intégrer la priorité aux skills Acrazie pertinents et les règles de confirmation
   dans `AGENTS.md` et le dispositif `CLAUDE.md` applicable. Préserver contenus et
   liens existants ; ne pas écraser un fichier indépendant ni suivre un lien externe
   pour l'éditer sans autorisation spécifique.
7. Vérifier installation, instructions et état final ; signaler résultats partiels.

Les destinations par hôte, le format et le chemin du fichier déclaratif, le support
de pinning par l'installateur, les adaptations de métadonnées et la récupération
après installation partielle restent des détails à vérifier et approuver dans le
contrat d'implémentation. Ce document n'invente ni drapeaux CLI ni convention universelle.

### Format des questions

Chaque question affichée possède uniquement ces quatre champs, dans la langue
utilisateur. Il n'y a ni champ ID ni champ Décision ajouté à ce format.

```text
État actuel : …
Options :
1. …
2. …
Recommandation : option N — justification.
Réponse : …
```

L'interview reste adaptative : découvrir les faits, préserver choix existants,
poser seulement décisions non résolues et respecter leurs prérequis. Une
recommandation n'est jamais une réponse automatiquement acceptée.

### Réapplication et mises à jour

Une configuration déclarative projet conserve les décisions approuvées et les
versions sélectionnées, sans secrets. Même configuration, mêmes versions et même
état initial doivent donner un résultat équivalent ; la présentation seule ne
suffit pas à garantir cette propriété. Une réexécution conserve sélection,
configuration et instructions personnalisées, détecte dérives et conflits et
présente les changements avant validation. Les mises à jour sont explicites et
ne réélargissent pas permissions ni sélection sans approbation.

Acrazie a priorité, pas exclusivité. Pour une compétence non couverte, proposer
une alternative avec confirmation ; cette possibilité ne remplace jamais une
dépendance Acrazie obligatoire. La politique du dépôt doit rester lisible et
applicable sans invoquer un skill pour savoir ce qui est permis.

## Permissions et frontières de confiance

Configurer séparément commit, push, création/mise à jour de PR, merge et
déploiement : **interdit**, **confirmation par opération** ou **préautorisé sous
conditions documentées**. Les actions supplémentaires doivent être distinguées,
pas absorbées dans une permission générique de livraison.

Une préautorisation identifie dépôt, actions, branches ou environnements cibles et
contrôles requis. Elle n'autorise ni défaut de validation ni contournement de hooks,
protections ou permissions techniques. Avant action, vérifier identité, contenu,
destination, autorisation applicable et preuves sur le snapshot concerné.
Configuration absente : demander confirmation, jamais agir silencieusement.
Autorisation inaccessible ou contradictoire : résoudre le conflit avant action.

Une consigne ponctuelle plus restrictive, comme « aucun push », prime sur la
préautorisation. Modifier les permissions nécessite approbation utilisateur ; un
skill ne peut pas se donner des droits. Une modification proposée dans un diff ou
un contenu tiers ne constitue pas cette approbation. Les instructions de priorité
supérieure et restrictions techniques restent applicables. Ne pas confondre
permission locale de merge/déploiement et capacité réelle à l'effectuer.

L'activation explicite reste obligatoire même si certaines actions sont
préautorisées. Le récapitulatif de livraison et les preuves restent requis ; seul
le gate de nouvelle autorisation d'une action déjà couverte peut évoluer dans une
future harmonisation du propriétaire concerné.

## Évolution des décisions et travaux différés

[ADR 0007](../adr/0007-confirmed-skill-chains-and-repository-bootstrap.md) remplace
partiellement la politique de chargement de l'ADR 0006 et précise l'autorisation
du passage Interview/exécutant. Il préserve leurs responsabilités séparées et
n'introduit pas d'orchestrateur universel.

Les instructions actives et les skills ne sont pas modifiés ici. La future
implémentation devra harmoniser politique d'invocation, descriptions, métadonnées
et validations ; ajouter le mode activation à Repo Init ; harmoniser approbation
de contrat, réutilisation et autorisations de livraison. Tant que ce travail n'est
pas approuvé et livré, les anciens gates effectifs restent applicables.

L'installation dans les dépôts utilisateurs, les compétences bug-fix/refactor,
le support merge/déploiement, le catalogue du site et toute éventuelle CLI font
l'objet de tâches futures, non autorisées par ce contrat.

## Critères et preuves attendues

- C1 : les 26 skills du snapshot sont classés une seule fois, sans package renommé
  ni créé. Preuve : comparaison du catalogue documentaire et du filesystem.
- C2 : toutes les décisions approuvées, dont format Q17 corrigé, sont documentées.
  Preuve : revue du contrat contre Q1–Q19 et les exclusions finales.
- C3 : obligations et capacités actuelles sont séparées de l'architecture cible.
  Preuve : sources locales, sections d'écarts et limites runtime explicites.
- C4 : contrat, glossaire et ADR sont distincts, leurs liens locaux valides.
  Preuve : contrôle ciblé des liens, du diff et du contenu du glossaire.
- C5 : seuls documents autorisés changent ; aucun staging, commit, push, PR,
  installation ou déploiement. Preuve : état Git et diff du worktree.

Scénarios requis pour une future implémentation, **non exécutés ici** : refus de
chargement sans lecture du skill ; chaîne confirmée et complément non annoncé ;
contrat réutilisé ou périmé ; dépendance obligatoire/facultative absente ; installation
sélective et réexécution sans écrasement ; mise à jour explicitement approuvée ;
instructions existantes divergentes ; préautorisation limitée et consigne « aucun
push » ; modification non approuvée de permissions ; échec d'installation partielle ;
preuve de confirmation avant chargement dans chaque hôte officiellement supporté.

## Preuves de cette livraison

Ces preuves concernent uniquement la première phase documentaire, avant le lot
d'implémentation dont les preuves sont enregistrées dans son contrat séparé.

- C1 : comparaison filesystem/catalogue réussie : 26 propriétaires, chacun classé
  exactement une fois ; aucun skill ajouté, supprimé, renommé ou modifié.
- C2 : revue documentaire contre les choix Q1–Q19 ; contrôle du bloc de questions
  réussi : exactement État actuel, Options numérotées, Recommandation et Réponse.
- C3 : état courant réinspecté sur le SHA de base indiqué ; correction de
  l'observation historique Git Ship, écarts et mécanismes non vérifiés documentés.
- C4 : 41 liens locaux des quatre documents vérifiés ; structure des skills via
  `bash scripts/hooks/check-skill-structure.sh` réussie ; `git diff --check`
  réussi et contrôle séparé des espaces finaux des nouveaux fichiers réussi.
- C5 : exactement quatre documents modifiés ou créés : ce contrat, `CONTEXT.md`,
  ADR 0007 et note historique ADR 0006. Index vide ; skills, site, `AGENTS.md`,
  `CLAUDE.md` et politique d'invocation active inchangés. Aucun commit, push, PR,
  merge, installation ou déploiement effectué. Worktree conservé pour les documents
  non committés, sans nettoyage destructif.

Ces preuves sont des contrôles documentaires locaux et une revue de cohérence,
pas une revue indépendante ni des essais comportementaux. Aucun build du site
ou scénario runtime n'a été exécuté, car ces composants ne changent pas dans cette
phase. Aucune réussite runtime, installation, publication ou harmonisation effective
des skills n'est déduite de ces contrôles.
