# Contrat — Pilote de skills vérifiables et reproductibles

## Objectif et périmètre approuvé

Formaliser un standard commun, puis l'appliquer uniquement à `interview-acrazie`
et `repo-modernizer-acrazie`, y compris leurs références nécessaires. Les règles
essentielles doivent accompagner chaque skill installé séparément, sans dépendre
du fichier `AGENTS.md` de ce dépôt ni d'un harnais particulier.

## Décisions et critères observables

1. Conserver les spécialisations utiles. Ne plus présenter les connaissances
   techniques changeantes comme des vérités fixes : syntaxe, API, commandes,
   compatibilité, versions et maintenance sont vérifiées à chaque exécution quand
   utilisées pour une décision ou une action. La documentation doit correspondre
   à la version du projet ou à la cible envisagée, et non automatiquement à la
   dernière version. L'état local reste vérifié dans le dépôt.
2. Tracer les sources, la version concernée et les limites des faits utilisés.
   Si une documentation est inaccessible ou contradictoire, marquer le fait non
   vérifié et suspendre uniquement la décision ou l'action qui en dépend. Ne pas
   substituer la mémoire du modèle à une preuve ; poursuivre le travail indépendant.
3. Reproductibilité signifie étapes obligatoires, décisions tracées, critères
   vérifiables et structure de sortie commune ; elle ne garantit pas des textes
   ou résultats identiques entre modèles ou harnais.
4. Réutiliser le format Markdown existant des questions : état actuel, options
   numérotées, exactement une recommandation motivée, réponse attendue. Traduire
   dans la langue de l'utilisateur, ne pas préremplir le consentement. Les sorties
   finales explicitent décisions, preuves et limites, sans supprimer les sections
   métier ni les autorisations existantes.
5. Le standard est documenté dans le dépôt et embarqué dans les deux skills.
   Les références du pilote ne doivent pas contredire les règles d'entrée par des
   prescriptions périssables ou des commandes tenues pour autoritatives sans preuve.
6. Effectuer les validations de structure/métadonnées pertinentes, des contrôles
   statiques ciblés et des scénarios représentatifs : version ancienne,
   documentation inaccessible, documentation contradictoire, choix numérotés et
   recommandation unique. Distinguer contrôles statiques, simulation dans le harnais
   courant et essais réels multi-modèles/multi-harnais ; aucune preuve universelle.

## Exclusions et exécution

- Pas de généralisation aux autres skills, changement d'installations globales,
  refonte des périmètres métier ou création d'un nouveau skill.
- Pas de nouvelle suppression Jenkins : remplacement déjà présent dans la base
  `origin/main` actualisée (`bf72bf9`) utilisée par ce worktree.
- Aucun commit, push, PR ou déploiement sans accord distinct.
- Worktree isolé : `.worktrees/codex/portable-skill-pilot`, branche
  `codex/portable-skill-pilot`, depuis `main` actualisé.
- Un agent implémenteur réalise le pilote ; un vérificateur indépendant examine
  le contrat et un instantané figé, sans hériter du raisonnement de l'auteur.
  L'implémenteur corrige les défauts, puis les changements sont revérifiés.

## Approbation

L'utilisateur a choisi le pilote `interview-acrazie` + `repo-modernizer-acrazie`,
puis répondu `1` à la demande distincte d'approbation du contrat : standard commun,
adaptation du pilote, tests, implémenteur puis vérificateur indépendant, worktree
isolé depuis `main` actualisé, sans généralisation ni publication (11 octobre 2026).

## Preuves de livraison

### Décisions et réalisation

Le standard mainteneur est dans `docs/portable-skill-standard.md`. Chaque skill
pilote charge ses règles embarquées dans `references/portable-practice.md` ; les
deux copies sont identiques et leur cohérence est testée. Les références du
Modernizer remplacent les cibles de versions fixes, recettes autoritatives et
ratios de performance non prouvés par une démarche de découverte et de preuve.
Les périmètres métier et frontières d'autorisation sont conservés. Les trois
termes du pilote sont définis dans `CONTEXT.md`.

### Contrôles effectivement exécutés le 11 octobre 2026

- Critères 1, 2 et 5 : lecture des entrées/références, vérification des liens
  locaux, identité des copies et six tests du pilote intégrés à `test:invocation`.
- Critères 3 et 4 : contrôles des questions à quatre champs, options numérotées,
  recommandation unique et bilans structurés ; conservation des contrats métier.
- Critère 6 : validation des deux entrées et de la structure, `git diff --check`,
  14 tests engineering-core, 9 tests commit-contract, 13 tests invocation/pilote,
  15 tests du graphe source et 4 tests des pages générées : **55 tests réussis**.
- Build local du site : **72 pages générées**, succès. Les quatre tests de sortie
  nécessitaient ce build ; leur premier échec `ENOENT` avant génération ne constitue
  ni une validation réussie ni une régression, et leur relance a réussi.
- Huit simulations limitées, quatre par skill, issues des prompts versionnés de
  leurs `evals/evals.json` : version adéquate, documentation inaccessible,
  contradiction documentaire et question localisée/autonomie simulée. **8/8 probes,
  24/24 attentes satisfaites** dans le contexte du vérificateur.
- Revue indépendante : **ACCEPT**, aucun défaut introduit démontré dans les six
  critères et les invariants examinés. Instantané examiné : base
  `bf72bf94fe035835da50845e4555412c8bfa12a1`, digest
  `81f437dab3ba007ff19838e43b3236cdd26292a373ea987cf2f6f8f7db1261cb`
  (18 fichiers). Cette section de livraison est ajoutée après ce verdict ; elle
  ne modifie pas les instructions, tests ou critères approuvés.

### Limites et conservation des preuves

Le rapport, manifest, diff, logs et réponses des probes de cette session sont sous
`/tmp/portable-skill-pilot-review-1/`. Ces artefacts sont temporaires ; les prompts,
attentes et tests reproductibles restent dans le dépôt.

Les simulations ont été produites et évaluées par le vérificateur dans un contexte
commun du harnais Codex, avec identifiant exact du modèle non exposé. Elles ne sont
pas des exécutions autonomes d'un runner ni huit contextes isolés. Les sources
`docs://` sont synthétiques : aucun service documentaire amont n'a été interrogé
par ces scénarios. L'autonomie d'installation est contrôlée statiquement et
simulée, pas démontrée par une installation réelle dans un autre hôte. Aucune
garantie multi-modèles/multi-harnais, de sélection native, de compatibilité réelle
d'outils tiers ou de comportement identique n'est revendiquée.

Les dépendances existantes du site ont été installées localement avec lockfile
figé pour les contrôles ; aucune dépendance ou lockfile modifié, aucune installation
globale. Aucun staging, commit, push, PR ou déploiement effectué. La généralisation
reste exclue et requiert une nouvelle approbation.
