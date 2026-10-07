# Stratégie de commit des modernisations

Cette stratégie couvre deux responsabilités distinctes : respecter ou formaliser la politique Git du dépôt existant, puis découper et contrôler les commits de la migration approuvée. Elle reprend le modèle adaptable de `github-repo-init-acrazie` pour le brownfield, sans invoquer ce skill ni dépendre de son installation. Elle ne lance pas un chantier de gouvernance hors du périmètre demandé.

## 1. Découvrir avant de choisir

Lire les instructions applicables, `AGENTS.md`, `CONTRIBUTING.md`, `docs/git-workflow.md` s'il existe, les configurations de hooks, CI et releases. Examiner les messages récents comme indice, pas comme permission. Identifier les contraintes pertinentes de branche, signatures, format, granularité et livraison. Inspecter les protections distantes accessibles en lecture seule ; distinguer absence, inaccessibilité et non-vérification. Pour un dépôt local sans distant, les règles distantes ne s'appliquent pas.

Pour chaque règle, conserver source, portée et statut vérifié. Présenter tout conflit entre sources avec ses conséquences ; bloquer l'action concernée jusqu'à résolution autorisée. Une préférence utilisateur ne permet pas de contourner une restriction organisationnelle ou technique. Une instruction de ce skill ne remplace jamais la politique du dépôt.

Ne pas imposer Conventional Commits, un préfixe de branche, un hook, une PR Draft ou une méthode de merge. Préserver une politique existante cohérente. L'historique ou la présence d'un skill de livraison ne confère aucune autorisation.

## 2. Approuver politique et plan de commits

Poser seulement les questions non résolues :
- Quels périmètres indexer, quelles unités cohérentes et quel format de message respecter ?
- Quelles validations sont requises et quelles portes sont véritablement inapplicables, avec justification ?
- Quelles autorisations s'appliquent au staging, au commit, au push et à la PR, séparément ? En l'absence d'autorisation applicable, demander avant l'action.
- Faut-il formaliser une politique absente dans `docs/git-workflow.md` ? Proposer le contenu puis obtenir approbation avant création. Si cette formalisation est refusée, consigner la stratégie de migration approuvée dans le plan existant ; aucun fichier nouveau n'est obligatoire pour l'exécuter.
- Faut-il un outillage d'application ? Hooks, dépendances, CI et réglages GitHub sont des choix distincts. Aucune installation ou mutation distante implicite ; conserver le mode sans nouvel outil comme option valide.

Si `docs/git-workflow.md` existe, préserver son rôle autoritatif sans écrasement. Toute adaptation demande approbation ; maintenir les liens et règles cohérents dans les `AGENTS.md` et `CONTRIBUTING.md` existants, sans créer une nouvelle suite de gouvernance par défaut. Cette politique doit être compréhensible et applicable sans skill de livraison installé.

Inclure dans le plan approuvé, pour chaque commit prévu : intention, périmètre, dépendances, message conforme, validations et ADR requis. L'ordre des couches aide la planification, pas le comptage des commits. Séparer les intentions indépendantes ; regrouper runtime, configuration et adaptations code quand leur séparation produirait un état cassé. Un changement material de frontières ou de règles nécessite une nouvelle approbation avant exécution concernée.

L'approbation de la stratégie en fait une contrainte obligatoire, pas une recommandation. Elle n'accorde pas automatiquement les permissions de livraison. L'absence de hooks ou CI n'allège aucun contrôle.

## 3. Contrôle avant chaque commit

1. **Autorisation et destination** : vérifier branche autorisée, isolation approuvée et permissions applicables au staging et au commit. Si elles manquent, présenter périmètre, message et preuves et demander accord. Ne pas déduire permission de commit de l'accord de migration.
2. **Périmètre exact** : inspecter index, modifications et fichiers non suivis. Indexer uniquement les chemins ou hunks approuvés, puis examiner `git diff --cached` et les chemins indexés. Aucun travail tiers, secret ou artefact temporaire. Un index déjà contaminé bloque le commit ; demander arbitrage sans désindexer implicitement le travail tiers. Ne jamais utiliser un commit global pour absorber des fichiers hors périmètre.
3. **Cohérence et documentation** : vérifier intention et frontières approuvées, inclusion des fichiers nécessaires (manifest, lockfile, configurations, code, tests), et ADR Tier 2/3 préparé avant validation et inclus dans la migration concernée. Ne pas livrer un commit cassé pour satisfaire « un outil = un commit ».
4. **Message** : appliquer la convention choisie, y compris les contraintes de signatures ou releases existantes. Conventional Commits seulement si imposés ou choisis. Ne jamais ajouter `Co-authored-by:`.
5. **Preuve du contenu à committer** : exécuter les validations applicables approuvées sur le contenu exact destiné au commit. Un test vert du working tree ne valide pas un index partiel différent. Si des changements non indexés contribuent au résultat, bloquer et obtenir un snapshot isolé de l'index selon les moyens autorisés du dépôt, sans stash/reset du travail tiers. Relancer les checks affectés après toute modification du contenu validé, y compris par formatteur ou hook. Une vérification requise absente, indisponible, rouge ou périmée bloque le commit ; ne pas contourner les hooks avec `--no-verify` ni assouplir silencieusement les critères.

Si un contrôle échoue, ne pas committer. Montrer l'écart et proposer correction conforme ou révision explicite du plan, sans contourner une règle supérieure. Si le commit lui-même échoue, conserver les modifications et ne pas enregistrer de nouveau point de contrôle.

## 4. Points de contrôle et récupération

Avant la première migration, valider la base et enregistrer son SHA avec les commandes, résultats et périmètre validé. Ne pas annoncer de point de contrôle vert si des checks requis échouent. Sans point de contrôle vérifié, demander arbitrage avant migration.

Après chaque commit réussi, vérifier que le contenu committé correspond au snapshot validé ; enregistrer son SHA avec les preuves dans le suivi du plan. Si un hook a modifié des fichiers, recontrôler le contenu et les checks affectés avant de le déclarer vert. Un SHA sans preuve associée n'est pas un point de contrôle validé ; `HEAD` n'est pas vert par définition.

Après trois réparations infructueuses, arrêter et préserver index, fichiers modifiés et non suivis. Fournir commande en échec, trace représentative, réparations tentées et dernier SHA vérifié (ou son absence). Proposer les options de récupération sans les exécuter. Toute récupération destructive nécessite confirmation séparée précisant cible, chemins et conséquences, et préservation du travail tiers. Aucun reset ou nettoyage automatique.

Push et PR restent soumis à leurs propres autorisations et contrôles distants. Dans le bilan, distinguer commits validés localement, CI en attente, PR ouverte/mergée et déploiement ; ne pas annoncer une livraison distante sur la seule preuve locale.

## 5. Scénarios de conformité

| Situation | Comportement attendu |
|---|---|
| Convention existante non Conventional Commits, compatible avec règles supérieures | Préserver ce format ; ne pas installer Commitlint. |
| Politique absente, formalisation approuvée, hooks refusés | Créer la politique approuvée ; appliquer tous les contrôles sans nouvel outil. |
| Politique absente, fichier refusé, stratégie de migration approuvée | Suivre le plan existant sans générer `docs/git-workflow.md`. |
| Accord de migration, aucune permission de commit | Demander autorisation avant staging/commit selon les règles applicables ; aucun push ou PR implicite. |
| Runtime, configuration et code interdépendants | Une unité cohérente annoncée, validée et commitée ensemble. |
| Fichier tiers déjà indexé ou tests verts grâce à modifications non indexées | Bloquer le commit ; préserver le travail tiers et obtenir preuve du snapshot exact. |
| Check requis absent ou échoué, hook contourné proposé | Bloquer ; aucun faux succès ou `--no-verify`. |
| ADR Tier 2/3 requis | Préparer avant validation et inclure dans le commit concerné. |
| Trois réparations échouées, `HEAD` non prouvé vert | Préserver état, citer checkpoint enregistré ou absence, demander arbitrage. |

Ces scénarios et les tests structurels vérifient le contrat documentaire ; ils ne constituent pas une preuve du comportement réel d'un agent sur un dépôt cible.

Documentation Git consultée pour le contrôle de l'index : [git diff](https://git-scm.com/docs/git-diff) (`--cached` compare l'index au commit de référence, `HEAD` par défaut).
