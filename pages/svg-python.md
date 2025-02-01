---
title: "SVG with Python"
timestamp: 2018-01-01T07:30:03
tags:
  - CodeMaven
published: false
books:
  - python
author: szabgab
archive: true
---


A number of examples creating [SVG](/svg) images using [Python](/python).

More specifically using the [svgwrite](https://svgwrite.readthedocs.io/) module.


These scripts all create SVG files that can be embedded in an HTML document usng a simple `img` tag.

Coordinates are in tuples of (x, y) where (0, 0) is in the top left corner.

## Rectangular

<img src="/img/rect.svg" />

{% include file="examples/python/svg_rectangle.py" %}

## Arrow

<img src="/img/arrow.svg" />

{% include file="examples/python/svg_arrow.py" %}


```
pip install svgwrite
```

