---
title: "ANSI command line colors with Python"
timestamp: 2022-09-04T09:30:01
tags:
  - ANSI
  - cat
  - color
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


If you use the command line a lot (as you should on a Linux or Unix machine, such as the Mac) then you have surely noticed that the text
is sometimes printed in color.

How can this be done in Python and how can one create a file that will display part of its content using colors even if you just "cat"-it?


All you have to know for this is that there is something called [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)
that allows you to give instructions to the screen of a command-line window. Some of these instructions are related to color.

Here is an example script:

{% include file="examples/python/color.py" %}

Here I picked some of the colors from ANSI escape code table and put them in variables. Then I only need to print the code to the screeen.

Running this script:

```
python color.py
```

resulted in the following output on my computer:

<img src="/img/ansi-colors.png" alt="ansi colored output text">


## Color file content without programming language

If I run the same script, but redirect the output to a file

```
python color.py > color.txt
```

I'll get a "regular" text file that looks like this:

{% include file="examples/python/color.txt" %}


```
cat color.txt
```

<img src="/img/ansi-colors.png" alt="ansi colored output text">


