# Un propriétaire SVG statique, sans logos de package

Décision acceptée le 2026-10-12. L'utilisateur a choisi `svg-designer-acrazie`, le
retrait des deux anciens packages sans redirections, puis le retrait des logos de
tous les skills en conservant identité du portail, favicons et images de référence.
Le contrat du lot 3 autorise sa réalisation locale, pas sa publication.

## Contexte et alternatives

Icônes et bannières suivent la même démarche : brief, concepts utiles, production
SVG, validation et exports demandés. Leurs différences portent sur les critères
applicables : topologie et petites tailles d'un côté, typographie et recadrage de
l'autre. Deux packages répètent permissions, métadonnées et protocole d'export.

Alternatives examinées : garder deux propriétaires, élargir un ancien identifiant,
ou créer un propriétaire neutre avec références conditionnelles. Le propriétaire
neutre évite un nom trompeur sans ajouter une responsabilité métier. Des packages
transitoires de redirection auraient conservé trois points d'entrée ; ils sont écartés.

## Décision

Un seul package couvre les assets SVG statiques auparavant traités par les deux
skills. Les références icône/bannière restent conditionnelles ; exports et autorité
sont communs. Les améliorations SVG approuvées du lot 1 sont reprises. Ni quotas
créatifs, ni charset obligatoire, ni format de présentation unique ne sont imposés.
Originalité, sélection, approbations distinctes, sécurité des sources, petites tailles,
recadrage et preuve réelle des exports restent exigés selon le contexte.

Les huit logos de package inventoriés sont retirés sans remplacement. Le catalogue
n'en a pas besoin. Le portail, ses favicons et les images d'inspiration restent
inchangés ; ils n'ont pas le même rôle qu'une décoration de package.

## Conséquences et limites

Aux nouvelles révisions distribuées, les anciens identifiants de package et leurs
pages ne sont plus proposés. Aucune redirection n'est ajoutée. Le nom neutre accepte
un coût de migration explicite : installations globales, copies projet, liens et
kits pinnés ne sont pas réécrits automatiquement. Une ancienne révision reste
ancienne ; la publication et les effets sur le site distant ne sont pas prouvés
par une modification locale.

Historique, changelog et contrats anciens restent intacts. Les consommateurs actifs,
le catalogue multilingue et les tests évoluent ensemble. La fusion n'autorise ni
retouche raster, animation, refonte UI, diagrammes génériques, nouvelle dépendance,
installation, livraison Git ou déploiement.

Périmètre, migration et preuves : [contrat de consolidation](../specs/svg-consolidation.md).
