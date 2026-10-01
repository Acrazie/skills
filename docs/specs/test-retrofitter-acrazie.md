# Contrat — Test Retrofitter / Acrazie

## Objectif
Créer un skill humain qui ajoute et exécute des tests pertinents sur du code existant non ou insuffisamment testé, sans changement fonctionnel.

## Périmètre
- Inclus : SKILL.md, métadonnées Codex, glossaire spécifique et validation ciblée du workflow.
- Exclusions : nouvelles fonctionnalités, correction des bugs découverts, migrations générales du tooling, création ou migration de pipelines (dont GitHub Actions), installation locale du skill et déploiement.

## Critères et preuves attendues
- C1 : invocation humaine cohérente et structure valide ; preuves : validations du dépôt et métadonnées.
- C2 : appel à interview-acrazie, réutilisation d'un contrat valide et arrêt si fondation absente ; preuves : scénarios représentatifs.
- C3 : oracles distincts, tests choisis selon risques, aucune correction fonctionnelle ou assertion affaiblie ; preuves : scénario de contradiction.
- C4 : runner minimal et refactor soumis à accord, environnement isolé, autorisations sensibles distinctes ; preuves : scénario sans infrastructure et scénario externe.
- C5 : résultats, blocages et validation incomplète distingués ; preuves : scénario avec exécution indisponible.

## Décisions et contexte
Q1–Q11 acceptées dans la conversation : interview fondation obligatoire (réutilisation possible), écriture et exécution ; caractérisation et conformité distinctes ; couverture absente ou insuffisante ; tests seuls par défaut ; sélection motivée des types ; setup minimal approuvé ; test rouge conservé en cas de contradiction ; aucun seuil arbitraire ; environnement isolé ; nom test-retrofitter-acrazie et invocation humaine.

Prior art : 19 skills et 27 versions distinctes inspectés sur branches locales et 55 refs origin après fetch. Aucun workflow équivalent ; frontières explicites avec feature-builder, repo-modernizer, audit et Jenkins. Voir ../../CONTEXT.md pour le vocabulaire. Aucun ADR nécessaire : partition cohérente, sans décision coûteuse à inverser.

## Approbation
Statut : approuvé.
Le 2026-10-01, l'utilisateur a répondu exactement « ok » au contrat complet intitulé « Contrat proposé — test-retrofitter-acrazie », incluant destination docs/specs/test-retrofitter-acrazie.md dans .worktrees/codex/test-retrofitter, création, validation et PR selon règles du dépôt.

## Preuves de livraison
- C1 : validate-skills.sh et check-skill-structure.sh réussis ; YAML parsé avec Ruby/Psych, nom, politiques d'invocation et longueur UI vérifiés ; git diff --check réussi. quick_validate.py non exécuté jusqu'au bout : PyYAML absent des deux runtimes Python disponibles, aucune dépendance installée pour le contourner.
- C2–C5 : deux agents indépendants ont simulé cinq parcours en lecture seule : exigence contredite par code, fondation absente, Python sans runner avec demande GitHub Actions, fixture destructive en production, DB indisponible. Résultats : oracle non affaibli, dépendance obligatoire, contrat avant setup, pipeline exclu, exécution sensible refusée sans autorisation distincte, validation incomplète signalée. Aucun conflit bloquant observé.
- Limite : ces simulations vérifient les décisions du workflow ; aucun benchmark comparatif ni exercice réel de génération/exécution de tests applicatifs effectué.
- check-readme-links.py : 29 liens vérifiés. Aucune installation du skill, fusion ou vérification de production réalisée.

