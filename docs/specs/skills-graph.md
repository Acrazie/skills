# Carte interactive des skills

## Objectif
Permettre de découvrir tous les skills du catalogue et leurs invocations documentées dans une carte 2D expressive, puis de lire leurs instructions sans quitter la carte.

## Périmètre
- Inclus : routes `/graph/`, `/fr/graph/`, `/zh/graph/`, navigation, recherche, zoom, déplacement, recentrage, sélection et lecteur du SKILL.md complet.
- Exclus : backend, modification des skills, redesign du reste du site, relations de simple mention/recommandation, commit, push, PR et déploiement.

## Critères et preuves prévues
- C1 : tous les skills, même isolés, apparaissent ; tests du modèle et pages générées dans trois langues.
- C2 : chaque invocation directionnelle possède des extraits sources vérifiés ; aucun lien tiré d'une simple mention ; tests des sources, extrémités, cycles et cas invalides.
- C3 : recherche, sélection par carte/liste, voisins entrants/sortants, lecture complète et lien de fiche fonctionnent ; tests ciblés et vérification navigateur.
- C4 : carte originale 2D, familles visuelles, connexions et impulsions ciblées ; inspection desktop/mobile.
- C5 : clavier, alternative HTML sans JavaScript, absence de débordement à 320px, mouvement réduit, arrêt hors écran et pause manuelle ; vérifications navigateur.
- C6 : bibliothèque uniquement sur cette page, placement stabilisé et animations bornées ; build, poids compressé et contrôle au repos.
- C7 : catalogue et fiches existantes préservés ; build et revue du diff.

## Décisions et contexte
Astro statique, données réelles issues de `skills/`, lecteur Markdown et langues en/fr/zh existants. Direction : constellation de circuits 2D, force-graph, lecteur neutre, couleurs limitées à la visualisation. Les liens montrent des instructions documentées, éventuellement conditionnelles, jamais une trace d'exécution ni une autorisation de contourner les règles d'invocation. Les invocations sont sélectionnées explicitement et leurs passages sources contrôlés au build, pas inférées par recherche de noms.

## Approbation
Status: approved
Le 1 octobre 2026, dans cette conversation Codex, l'utilisateur a choisi « carte 2d expressive », accepté le périmètre et les invocations explicites, puis répondu « ok et ok pour l'installation » au contrat complet et à la demande séparée d'installation de force-graph. Destination approuvée : ce fichier dans `.worktrees/codex/skills-graph`. Aucune autorisation de livraison Git ou de production n'est inférée.

## Preuves de livraison
Validation locale terminée le 1 octobre 2026.

- C1–C2 : `bun run test:graph` après build, 17 tests et 181 assertions réussis. 19 skills, 7 appels conditionnels sourcés, nœuds isolés, cycles, doublons, extrémités inconnues, sources périmées et chemins invalides couverts. Le build vérifie chaque extrait ; les liens sont revus et maintenus explicitement dans `site/src/lib/skill-graph.ts`, sans inférence automatique de mentions.
- C3 : navigateur local, recherche « jenkins » (7 correspondances, car une description mentionne aussi Jenkins), recherche sans résultat, remise à zéro, sélection clavier par Entrée, clic réel sur le nœud feature-builder, lecture et passage source vérifiés. Jenkins expose ses 5 appels ; son spécialiste Go expose l'appel entrant. Le SKILL.md intégral de chaque skill est comparé au HTML généré dans les trois langues.
- C4 : captures viewport desktop 1440×1000, mobile 390×844 et lecteur 320×844 inspectées. Familles, modules carrés, connexions directionnelles, sélection et lecteur indépendant présents. Captures temporaires sous `.impeccable/review/`, ignorées par Git.
- C5 : aucun débordement horizontal constaté à 320, 390 et 1440px. Focus placé sur le titre du skill après activation clavier ; preuve source développable et lien GitHub vérifiés. Pause manuelle et état `paused` au repos observés. Préférence de mouvement réduit et arrière-plan couverts par tests de politique, câblage `matchMedia`/`visibilitychange` inspecté ; pas d'émulation de la préférence système ni de test avec lecteur d'écran. Sans JavaScript, instructions et relations sont des éléments details HTML natifs ; carte et recherche non fonctionnelles masquées par noscript. Sur mobile, défilement vertical de la page reste permis sur le Canvas.
- C6 : placement fixe, rafraîchissement de 120ms ou signaux de 1800ms, arrêt explicite du RAF au repos/hors écran. Import dynamique de force-graph uniquement sur la carte. Tailles des fichiers : renderer 172 473 octets (56 738 gzip), contrôleur 8 488 octets (3 549 gzip), page FR 216 951 octets (58 826 gzip). Ce sont des tailles compressées mesurées, pas une mesure réseau ou un benchmark. Le test d'une arborescence de sources sans .git a reproduit puis éliminé une dépendance incompatible avec le Dockerfile existant ; aucun Docker réel exécuté.
- C7 : `bun run build` réussit, 66 pages. Catalogue et fiches n'importent pas le contrôleur de carte ; comportement du helper Markdown sans baseUrl préservé par test. `git diff --check` et les 29 liens README passent. Aucun fichier de skill modifié. Détecteur Impeccable exécuté une fois : aucune observation.

Revue visuelle et vérification du système menées dans ce workflow séquentiel, sans sous-agent. Système existant conservé : surfaces neutres et typographies de DESIGN.md ; couleurs du nouveau graphe confinées à cette page, conformément à la direction approuvée. Aucun changement de PRODUCT.md ou DESIGN.md.

Limites : l'installation dépendance et validation sont locales ; aucun check CI distant, commit, push, PR, merge ou déploiement. Les sources utilisent GITHUB_SHA quand disponible, sinon main (lien mutable), avec extraits vérifiés conservés dans la page. Pas de nouveau checker TypeScript installé ; le build et les interactions réelles sont vérifiés, pas un contrôle de types indépendant.

Investigation du rendu mobile : le callback `onZoom` peut être déclenché synchroniquement pendant `resumeAnimation`, avant l'enregistrement du RAF interne. Cela provoquait une récursion ; un test exécutant la fonction réelle avec un renderer synchrone a échoué, puis passé après protection de réentrance. Les captures précédentes de cette occurrence sont invalidées. Les coordonnées fixes et le cadrage responsive ont été contrôlés par instrumentation temporaire : premier nœud (-90,-248), zoom 1,113, centre (0,31), 38 981 pixels dessinés sur mobile. Les captures pleine page du navigateur peuvent modifier temporairement les dimensions du Canvas et montrer une surface vide ; les confirmations utilisent donc des captures viewport. Instrumentation retirée après diagnostic.
