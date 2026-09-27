---
name: Acrazie Skills
description: Catalogue éditorial sombre avec un hero pixel art distinct et navigation liquid glass.
colors:
  surface: "#151515"
  surface-deep: "#101011"
  surface-raised: "#1d1d1d"
  line: "#38383a"
  ink: "#f3f2f0"
  muted-ink: "#b8b7b5"
  hero-sky: "#404f90"
  hero-ink: "#18191e"
typography:
  display:
    fontFamily: "Barlow Condensed, sans-serif"
    fontWeight: 700
    lineHeight: 0.95
  body:
    fontFamily: "Inter, sans-serif"
    fontWeight: 400
    lineHeight: 1.6
  code:
    fontFamily: "JetBrains Mono, monospace"
    fontWeight: 500
---

# Design System: Acrazie Skills

## Overview

**Creative North Star: « Signal Atlas »**

Le hero est un seul moment expressif : composition pixel art originale de nuages rose-orangé sur ciel indigo, mouvement lent et navigation translucide. Tout le reste du site reste sombre, neutre et calme pour la recherche et la lecture. Les couleurs du ciel appartiennent exclusivement au hero ; la navigation les laisse voir sans les reprendre sur les pages de lecture.

## Colors

Le catalogue et les pages de lecture emploient charbon, graphite et blanc doux. Contraste assuré par la luminosité, sans accents colorés. Le hero seul emploie indigo, lilas et pêche ; la navigation superposée utilise un verre teinté neutre.

## Typography

Barlow Condensed porte les grands titres. Inter sert la navigation et le texte courant. JetBrains Mono est réservé aux commandes, données et petits labels techniques.

## Layout

Hero pleine largeur derrière un dock liquid glass flottant, centré sur 80 % de la largeur desktop ; le dock suit le défilement, disparaît en descendant et revient en remontant. Sur les pages de lecture, son verre reste neutre. Sur mobile, image au-dessus du texte et dock plus large pour garder les liens lisibles. Catalogue centré sur 1320 px maximum, présenté en lignes éditoriales plutôt qu'en cartes. Fiches et changelog sur une largeur de lecture de 1120 px maximum ; colonne latérale pour la navigation des fiches sur grand écran. À 640 px, les lignes se réorganisent en liste compacte.

## Elevation & Depth

Pages neutres et plates, séparées par des règles fines. La profondeur du pixel art et le léger flou du verre sont réservés au hero et à la navigation. Les contrôles de lecture ne reçoivent pas de halo.

## Shapes

Angles droits et bordures discrètes dans le contenu. Le dock seul reçoit des coins arrondis et flotte au-dessus du contenu ; son verre révèle le hero et laisse deviner les surfaces neutres pendant le défilement.

## Components

Recherche et filtres restent visibles avant les résultats. Les lignes de skill montrent le nom, la description réelle, la catégorie et la route de détail. Les fiches exposent la commande d'installation et les instructions avant les références.

## Do's and Don'ts

- Préserver les données réelles de `skills/` et du changelog ; ne pas inventer de métriques, d'usage ou de performances.
- Garder tous les textes essentiels et les actions en DOM sémantique ; l’image est décorative.
- Maintenir le hero lisible avec photo statique sans JavaScript, et arrêter l'animation hors écran ou en mouvement réduit.
- Ne pas faire déborder les couleurs du hero sur le catalogue, les fiches et le changelog.
