---
title: "Write text on existing image using Python PIL - Pillow"
timestamp: 2019-04-22T12:40:01
tags:
  - PIL
  - Pillow
published: true
books:
  - python
author: szabgab
archive: true
---


This could be used for any image, but for the example we use this <a href="/create-images-with-python-pil-pillow">image
that was created using Python</a>:

![](/img/pil_color.png)

A slightly generic script to write text in the top left corner: (Coordintates (0, 0))

{% include file="examples/python/pil_write_on_image.py" %}

The result looks like this:

![](/img/pil_text_hello.png)

