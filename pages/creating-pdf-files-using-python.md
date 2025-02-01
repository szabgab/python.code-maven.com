---
title: "Creating PDF files using Python and reportlab"
timestamp: 2019-10-19T07:30:01
tags:
  - PDF
  - reportlab
published: true
books:
  - python
author: szabgab
archive: true
---


Install the reportlab module using:

```
pip install reportlab
```


Use the `canvas.Canvas` to create the skeleton.

Use <b>drawString</b> to add a string.

I admit, I don't know why do I need to call <b>showPage</b> as it seemed to work without that too. I'll updated this
post when I find it out.

`save` will save the pdf file.

{% include file="examples/python/pdf_hello_world.py" %}

[hello_world.pdf](/static/pdf/hello_world.pdf)


## Coordinates, sizes

By default the coordinates of a string are provided in pixels, starting from the lower left corner which is 0, 0.

You can use the <b>reportlab.lib.units</b> module that provides objects such as <b>'cm', 'inch', 'mm', 'pica', 'toLength'</b>
to use more human-friendly units.

{% include file="examples/python/reportlab_lib_units.py" %}

You'd use them like this:

{% include file="examples/python/pdf_hello_world_cm.py" %}


## Fonts (types and sizes)

The <b>getAvailableFonts</b> method will return the list of available fonts.

You can use the <b>setFont</b> method to set the font-type and size. From that point till the next call of
<b>setFont</b>, this will be used.

{% include file="examples/python/pdf_hello_world_fonts.py" %}

[fonts](/static/pdf/hello_world_fonts.pdf)


## Default page size

{% include file="examples/python/pdf_default_pagesize.py" %}

[pagesize](/static/pdf/pagesize.pdf)

For further details and explanation see the [reportlab userguide](https://www.reportlab.com/docs/reportlab-userguide.pdf).

