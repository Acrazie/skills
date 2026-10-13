# Contrat — consolidation SVG et retrait des logos de package

Date : 2026-10-12. Base : `9e6a6983dac60ebf904cdbc378e0c3419d57c9f0`.
Autorisation : choix Q1 `svg-designer-acrazie`, Q2 retrait sans redirections ; choix
« 1 » pour tous les logos de skills, hors portail/favicons/inspiration ; « ok » au
périmètre final du lot 3. Cette autorisation porte sur la réalisation locale seulement.

## Périmètre et ownership

- Remplacer `svg-icon-designer-acrazie` et `svg-banner-designer-acrazie` par
  `skills/svg-designer-acrazie/` : entrée, métadonnées, références conditionnelles,
  exports communs, scénarios et six images de référence conservées.
- Reprendre les cinq fichiers SVG approuvés du lot 1 depuis son worktree, sans
  recopier ses changements Repo Init. Lot 1 et lot 2 restent intacts et séparés.
- Retirer les huit logos des packages Audit Repository, Repo Init, Planner,
  Modernizer, README Architect, Refiner et des deux anciens SVG, sans nouveau logo.
- Adapter README, catalogue EN/FR/ZH, frontière Canvas, tests satellites, exemple de
  nom dans AGENTS/CONTRIBUTING/formulaire bug et règle de non-création automatique
  de logos de package. Aucun autre comportement de ces consommateurs ne change.
- Documenter vocabulaire dans CONTEXT et décision dans ADR 0011. Préserver les
  contrats historiques et CHANGELOG.

Exclusions : identités/favicons du portail, installations globales, kits pinnés,
autres fusions, nouveaux outils/dépendances, permissions, livraison Git et déploiement.

## Critères et garanties

1. Un seul propriétaire SVG statique, sans deux anciens packages ni redirections.
2. Méthode adaptable, références pertinentes seulement ; aucun rituel de preview ou
   quota de concepts/familles. Préserver les principes d'originalité et la direction élue.
3. Icônes : topologie, petites tailles, color behavior, accessibilité appropriée,
   favicons réellement encodés ; pas de changement HTML/manifest implicite.
4. Bannières : typographie, visibilité, fonts, clipping, recadrage et occlusion vérifiés
   au contexte ; aucune compatibilité courante déduite d'un tableau historique.
5. Exports : source et formats/dimensions/chemins approuvés, outil disponible et
   documenté, transparence, vrai type et dimensions vérifiées. Pas d'installation
   masquée, fetch externe, code SVG non fiable ou faux résultat rendu.
6. Les huit logos de package disparaissent ; branding/favicons du portail et six
   PNG de référence restent identiques.
7. Consommateurs actifs et catalogue cohérents ; uniquement des mentions historiques,
   de migration ou assertions négatives peuvent garder les anciens identifiants.

## Migration des consommateurs

Aucune installation ou mise à jour de kit n'est exécutée par ce lot. Après une
publication séparément autorisée, un utilisateur doit choisir la nouvelle révision
et sélection de skill, puis suivre son mécanisme d'installation/activation approuvé.
Les copies projet, configurations, lockfiles/hashes et liens de harnais doivent être
inventoriés et mis à jour sous leur propre autorisation ; ne pas écraser une copie
modifiée. Un lien vers un répertoire retiré peut devenir cassé. Le script de liaison
contributeur ajoute des liens mais ne retire pas les anciens : ne pas le présenter
comme une migration complète. Les anciennes URLs ne sont pas redirigées.

## Preuves attendues et état

Prévoir hooks frontmatter/structure, liens locaux/README, JSON/scénarios, tests de
contrat satellites, contrôles d'invocation/graphe et build du site avec dépendances
déjà disponibles. Vérifier le périmètre exact et les références/assets conservés.
Les scénarios sont des fixtures : leur définition et les tests statiques ne sont
pas des évaluations comportementales exécutées. Aucun résultat live ou distant
n'est déduit d'un test local. Résultats effectivement exécutés consignés ci-dessous
à la clôture ; une dépendance manquante reste un blocage explicite.

### Première validation — environnement incomplet

- Périmètre vérifié : 55 chemins de migration, 16 fichiers dans le nouveau package,
  huit logos retirés, six PNG conservés byte pour byte ; index inchangé et aucun
  changement portail/CHANGELOG/contrats historiques. Les lots 1 et 2 restent intacts.
- Hooks frontmatter/structure et 25 liens README valides ; liens locaux, JSON et
  fencing Markdown contrôlés. `git diff --check` réussi.
- Tests de contrat satellites : 15 réussis.
- Bun 1.4.2 : 28 tests invocation/portable-pilot/graphe réussis, sans auto-installation.
  Dépendances déjà installées empruntées en lecture ; cache Vite isolé dans le
  worktree. Ce n'est pas une installation exacte du lockfile : notamment Marked
  disponible est 18.0.14, différent de la déclaration du projet.
- Build local tenté avec Astro 7.3.5 : bloqué par import `force-graph` absent des
  dépendances installées disponibles. Aucun paquet installé, aucune externalisation
  ou suppression de fonctionnalité pour masquer l'échec. Tests du graphe sur HTML
  produit non exécutés ; aucun résultat de build complet ni de compatibilité CI
  n'est revendiqué. La vérification requiert un environnement complet séparément
  autorisé.
- Huit scénarios définis (quatre communs, quatre spécifiques icône/favicon/bannière/
  cible combinée), pas d'évaluations comportementales ou de rendu exécutées.
- Aucun commit, push, PR, déploiement ou changement d'installation utilisateur.

### Vérification finale — 2026-10-13

L'utilisateur a autorisé séparément l'installation locale figée des dépendances dans
ce seul worktree. `bun install --frozen-lockfile --ignore-scripts` a installé les
versions déclarées et verrouillées, avec cache local au worktree et scripts lifecycle
désactivés. Manifests/lockfile inchangés ; aucune installation globale ni modification
des installations précédemment empruntées.

- Build Astro local complet : 69 pages générées, dont le nouveau propriétaire SVG
  en EN/FR/ZH ; aucune page des deux anciens identifiants.
- Bun 1.4.2 : 32 tests invocation/portable-pilot/graphe/HTML généré réussis.
- Tests satellites Python : 15 réussis, soit 47 tests locaux réussis au total.
- Hooks, 25 liens README, intégrité des six PNG, retrait des huit logos, périmètre de
  55 chemins et `git diff --check` revalidés. Index, branding du portail, historique
  et lots 1/2 inchangés.
- Le blocage d'environnement de la première validation est levé. Aucune évaluation
  comportementale des huit scénarios, inspection visuelle multi-device, CI distante,
  publication de package ou mise en ligne n'est revendiquée.

Les builds et dépendances sont des artefacts locaux ignorés. Aucune livraison Git ou
mise à jour d'installation utilisateur n'est incluse dans cette vérification.
