---
title: "Create images with Python PIL and Pillow and write text on them"
timestamp: 2017-12-27T11:30:01
tags:
  - PIL
  - Pillow
  - Image
  - ImageDraw
  - ImageFont
published: true
books:
  - python
author: szabgab
archive: true
---


Pillow is a fork of PIL. You should use Pillow these days.

## Install Pillow

Before you can use it you need to install the Pillow library.
Read the [documentation of Pillow](https://pillow.readthedocs.io/) on how to install it on your operating system.

## Draw a simple image with one color

```python
from PIL import Image, ImageDraw
img = Image.new(mode, size, color)
img.save(filename)
```

There are various values for <b>mode</b> listed in the documentation of Pillow. For example RGB and RGBA can be modes.
The <b>size</b> is a tuple in the form of (width, height) in pixels.
The <b>color</b> can be a word such as 'red', or a triplet for RGB colors of 3 values between 0-255.

This script:

{% include file="examples/python/pil_new_red_image.py" %}

will create this image:

<img src="/img/pil_red.png" alt="red rectangular" />

We can also use the individual RGB values in their decimal form taken from some color wheel or other color selector application.

{% include file="examples/python/pil_new_color_image.py" %}

The result is this:

<img src="/img/pil_color.png" alt="red rectangular" />


## Writing text on image

For this we also need to import `ImageDraw`. We pass the location of the top-left corner of the text,
the text itself, and the color of the text. There are number of other parameters you can pass to this method.

{% include file="examples/python/pil_write_text_on_image.py" %}

The result is this:

<img src="/img/pil_text.png" alt="" />


## Selecting the font

There are a number of ways to select the font used for writing on the image. We need to import and use the `ImageFont`
to load a TrueType font. Mac OSX supplies a bunch of fonts that are located in the `/Library/Fonts/`.
On other platforms you'll need to locate the files yourself and then pass the full path to the function.
Alternatively you could include the font-file in your application and then you can know where is the font-file relative to your code.

In this example we load the font using the `truetype` method of the `ImageFont` passing to it the path to
the fonts and the size of the fonts to be loaded.

{% include file="examples/python/pil_write_text_on_image_select_font.py" %}

The result is this:

<img src="/img/pil_text_font.png" alt="" />

