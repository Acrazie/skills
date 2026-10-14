# Migration des mises à jour de Dependabot vers Renovate

## Contrat et approbation

Le 14 octobre 2026, l’utilisateur a approuvé la préparation des fichiers et des
validations locales pour le seul dépôt `Acrazie/skills`. L’objectif est de réduire
le bruit des PR avec l’application GitHub Renovate hébergée par Mend, dont l’accès
sera limité à ce dépôt. Cette approbation ne couvre ni installation de
l’application, ni changement des paramètres de sécurité GitHub, ni publication,
fusion ou déploiement.

## Politique retenue

- Maintenir les trois périmètres existants : dépendances Bun du site, GitHub
  Actions et images Docker, y compris les digests déjà présents.
- Regrouper les mises à jour mineures, patch et digest en trois groupes distincts.
  Les versions majeures restent individuelles et nécessitent une approbation de
  création dans le Dependency Dashboard ; cette approbation n’autorise pas la fusion.
- Créer les branches ordinaires les 1er et 15 de chaque mois, pendant toute la
  journée dans le fuseau `Europe/Paris`. Cette approximation acceptée représente
  des intervalles de 14 à 17 jours, pas un intervalle strict de quatorze jours.
  Le calendrier autorise une exécution mais ne déclenche pas l’application Mend.
- Autoriser les actualisations et rebases des branches existantes hors créneau.
- Limiter à cinq PR ordinaires Renovate ouvertes au total. Les PR Dependabot
  temporaires ne sont pas comptées ; les correctifs de sécurité ne sont pas
  soumis à cette limite ni au créneau ordinaire.
- Conserver les titres et commits Conventional Commits `chore(deps)` et les labels
  existants. Ne jamais activer l’automerge : une fusion sur `main` peut entraîner
  un déploiement Dokploy.
- Ne pas ajouter de maintenance indépendante du lockfile. Chaque mise à jour
  Bun doit néanmoins régénérer le lockfile si nécessaire.

## Périmètre de préparation et exclusions

Ajouter `renovate.json` et ce contrat dans le worktree Codex isolé existant, base
`ff6c26cc948478c0c1f8a48b90ea56506ca9e6d8`. Garder
`.github/dependabot.yml` inchangé pendant la préparation et la transition.
Ne modifier aucun skill, workflow, dépendance applicative, image ou paramètre
distant. Aucun nouveau terme métier ne justifie une extension du glossaire ;
aucun compromis suffisamment durable ne nécessite un ADR.

La configuration utilise des règles explicites, sans preset de regroupement
susceptible de regrouper également les versions majeures. Les managers activés
sont `bun`, `github-actions` et `dockerfile`.

## Critères et preuves attendues

1. Le validateur officiel Renovate accepte le fichier sans erreur ni migration.
2. Les assertions locales vérifient les trois groupes, l’approbation des majors,
   le calendrier, la limite, l’absence d’automerge et les exceptions de sécurité.
3. Le diff reste limité à la configuration et au contrat ; Dependabot reste intact.
4. Avant bascule, une véritable PR Renovate mettant à jour le site démontre la
   cohérence de `site/package.json` et `site/bun.lock`, sans erreur de génération
   d’artefacts. `bun install --frozen-lockfile` et tous les checks CI doivent passer
   pour son snapshot exact. Cette preuve distante ne peut pas être remplacée par
   la seule validation locale du fichier.
5. Le transfert des correctifs de sécurité nécessite une preuve distincte :
   Dependency graph et Dependabot alerts actifs, accès en lecture aux alertes
   pour l’application et traitement réussi d’une alerte éligible réelle. En
   l’absence de cette preuve, Dependabot security updates reste actif.

## Procédure de bascule — non exécutée

1. Après autorisation distincte de publication puis de fusion, intégrer cette
   configuration tout en conservant Dependabot.
2. Après autorisation distincte d’installation, installer/configurer l’application
   Mend Renovate avec accès au seul dépôt `Acrazie/skills`. Examiner ses permissions
   et son onboarding ; conserver la politique approuvée si une PR d’onboarding
   propose une autre configuration.
3. Vérifier dans le Dashboard les trois périmètres détectés et les digests Docker.
   Attendre le créneau autorisé pour la première PR ordinaire ; toute dérogation
   temporaire nécessite une nouvelle approbation. Vérifier la PR Bun et sa CI
   selon le critère 4, puis les groupes, les majors et les titres/labels.
4. Après ces preuves et autorisation de la bascule, retirer le fichier
   `.github/dependabot.yml` dans une PR distincte. Cela retire les mises à jour
   ordinaires, pas les alertes ni les correctifs de sécurité GitHub.
5. Inventorier les PR Dependabot ouvertes. Ne les fermer qu’après autorisation et
   seulement si elles sont remplacées ou devenues inutiles ; conserver leur preuve
   CI et ne jamais les fusionner automatiquement.
6. Garder Dependency graph, Dependabot alerts et Dependabot security updates
   actifs. Des PR de sécurité en doublon sont acceptées temporairement. Désactiver
   uniquement Dependabot security updates après le critère 5 et autorisation
   distincte du changement de paramètre ; ne jamais désactiver les alertes.

## Retour arrière

Avant retrait de Dependabot, arrêter l’accès Renovate au dépôt après autorisation :
Dependabot est encore configuré. Après retrait, restaurer d’abord le fichier
Dependabot depuis le commit précédant la bascule via une PR et vérifier sa prise
en compte, puis arrêter Renovate. Si les correctifs de sécurité avaient été
transférés, réactiver Dependabot security updates et vérifier les alertes avant
d’arrêter Renovate. Les fermetures de PR et changements d’accès restent autorisés
séparément ; aucun historique ADR n’est réécrit.

## Sources consultées

- [Planification](https://docs.renovatebot.com/key-concepts/scheduling/)
- [Options et alertes de sécurité](https://docs.renovatebot.com/configuration-options/)
- [Manager Bun](https://docs.renovatebot.com/modules/manager/bun/)
- [Validation](https://docs.renovatebot.com/config-validation/)
- [Hébergement Mend](https://docs.renovatebot.com/mend-hosted/overview/)

## Preuves réalisées et limites

Le 14 octobre 2026, le validateur officiel Renovate **44.155.8**, exécuté avec
Node **24.11.0**, a accepté `renovate.json` en mode configuration de dépôt,
avec `--strict --no-global`, sans erreur, avertissement ou migration. Le runtime
temporaire Node 24 respecte les exigences de cette version de Renovate ; aucune
dépendance n’a été ajoutée au dépôt. Commande reproductible :

```sh
npx --yes --package=node@24.11.0 --package=renovate@44.155.8 -- renovate-config-validator --strict --no-global renovate.json
```

Les assertions Python locales ont vérifié les managers, les trois groupes et
leurs types de mises à jour, les labels, les commits, l’approbation des majors,
le calendrier, les rebases hors créneau, la limite, les exceptions de sécurité et
l’absence d’automerge et de maintenance indépendante du lockfile. Elles ont aussi
vérifié l’identité du fichier Dependabot avec `HEAD`, l’allowlist exacte des deux
nouveaux fichiers et l’absence d’espaces de fin de ligne. `git diff --check` passe.
Ce sont des preuves statiques, pas une exécution du bot.

SHA-256 du fichier `renovate.json` validé :
`a38c361fff9cc31772e7a13342e9fe41f4235a0fd3045c8217620d8d154c468f`.

Aucune installation de l’application, lecture des paramètres distants, PR Renovate
réelle, bascule, publication, fusion ou déploiement n’a été exécuté. Aucun build
applicatif n’a été relancé : les dépendances et le code applicatif restent inchangés.
La version exécutée par Mend et son traitement effectif du lockfile Bun restent à
vérifier lors de la phase distante avant tout retrait de Dependabot.
