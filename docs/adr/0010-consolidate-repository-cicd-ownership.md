# Un seul propriétaire CI/CD du dépôt

Décision acceptée le 2026-10-11 ; réalisation non autorisée par cet ADR. Remplacer
la famille de six packages Jenkins par `ci-cd-acrazie`, propriétaire du workflow
CI/CD d'un dépôt indépendamment du langage et de l'outil. Les cinq interprètes de
stack ne possèdent pas de tâches d'implémentation indépendantes : leurs connaissances
et celles propres à Jenkins deviennent des références internes ciblées, pas des
skills complémentaires ni un plugin ou moteur d'orchestration.

Cette consolidation privilégie une responsabilité complète et des gates cohérents
plutôt que des packages par technologie. Le support est ouvert, mais toute action
reste fondée sur le dépôt, les versions/capacités réellement disponibles et une
documentation actuelle ; aucune compatibilité universellement testée n'est promise.
Le propriétaire peut conduire les opérations distantes demandées sous autorisations
distinctes et vérification, sans administrer plateformes, runners globaux ou cloud.
Repo Init garde le bootstrap minimal et Modernizer l'audit/plan global ; les travaux
CI/CD substantiels passent au propriétaire unique sans répéter les décisions valides.

## Conséquences

Les anciens packages seront retirés du catalogue courant sans redirections
transitoires lors d'une réalisation séparément approuvée. Le coût assumé est une
migration explicite des consommateurs : ni kits pinnés ni installations/liens
globaux ne sont réécrits automatiquement. Historique et anciennes révisions restent
préservés ; le catalogue, graphe, tests et handoffs actifs devront évoluer ensemble.
Garder six redirections affaiblirait l'objectif « un seul skill » sans nécessité
actuellement démontrée. Une famille plugin et un périmètre DevOps administratif
étendu ont été écartés pour absence de besoin de runtime propre et responsabilités
excessives.

Contrat, état actuel et migration :
[architecture de consolidation](../specs/cicd-consolidation-architecture.md).
