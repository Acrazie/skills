---
name: Acrazie Skills
description: Catalogue éditorial sombre avec un hero ASCII photographique distinct.
colors:
  surface: "#151515"
  surface-deep: "#101011"
  surface-raised: "#1d1d1d"
  line: "#38383a"
  ink: "#f3f2f0"
  muted-ink: "#b8b7b5"
  hero-night: "#081525"
  hero-ice: "#d6f1fb"
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

Le hero est un seul moment expressif : photo de nuages, trame de caractères Canvas 2D et lumière froide. Tout le reste du site reste sombre, neutre et calme pour la recherche et la lecture. Les couleurs bleues et la lueur appartiennent exclusivement au hero.

## Colors

Le catalogue et les pages de lecture emploient charbon, graphite et blanc doux. Contraste assuré par la luminosité, sans accents colorés. Le hero seul emploie nuit indigo et bleu glacé.

## Typography

Barlow Condensed porte les grands titres. Inter sert la navigation et le texte courant. JetBrains Mono est réservé aux commandes, données et petits labels techniques.

## Layout

Hero pleine largeur sous la navigation. Catalogue centré sur 1320 px maximum, présenté en lignes éditoriales plutôt qu'en cartes. Fiches et changelog sur une largeur de lecture de 1120 px maximum ; colonne latérale pour la navigation des fiches sur grand écran. À 640 px, les lignes se réorganisent en liste compacte.

## Elevation & Depth

Pages neutres et plates, séparées par des règles fines. La profondeur photographique et le bloom sont réservés au hero. Les contrôles de lecture ne reçoivent pas de halo.

## Shapes

Angles droits et bordures discrètes. Pas de pilules, de cartes flottantes ni de verre décoratif.

## Components

Recherche et filtres restent visibles avant les résultats. Les lignes de skill montrent le nom, la description réelle, la catégorie et la route de détail. Les fiches exposent la commande d'installation et les instructions avant les références.

## Do's and Don'ts

- Préserver les données réelles de `skills/` et du changelog ; ne pas inventer de métriques, d'usage ou de performances.
- Garder tous les textes essentiels et les actions en DOM sémantique ; Canvas est décoratif.
- Maintenir le hero lisible avec photo statique sans JavaScript, et arrêter l'animation hors écran ou en mouvement réduit.
- Ne pas faire déborder les couleurs ou effets du hero sur le catalogue, les fiches et le changelog.
