---
title: "Python: avoid importing everything using a star: *"
timestamp: 2020-03-23T13:30:01
tags:
  - import
  - '*'
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


When I teach Python I keep telling my students to avoid importing using <b>*</b>,
but it isn't always easy as there are many examples
on the Internet, some even in official documentation, using code like:

```
from tkinter import *
```

Instead of that it would be better to write:

```
import tkinter as tk
```

But why?


## Automatic function overwriting

Let's say you have this code:

```
from Amodule import *
from Bmodule import *
```

and you use the function <b>calc</b> from Amodule.

Then you upgrade Bmodule (an external module) and it starts to also provide a function called <b>calc</b>.
Maybe it is a helper function of Bmodule so it is not even documented.

Suddenly your code starts to use the function <b>calc</b> provided by Bmodule.

Python does not even complain, but this is not what you wanted.

So in general it is better to avoid this feature of Python.

In general it is better to be explicit about what you are importing than implicit.

Oh, and in case you say "but I only use * for one module" here is the same example for you:

```
from Amodule import calc
from Bmodule import *
```

In this example your code will still break if <b>Bmodule</b> starts to have a function called <b>calc</b>.
Which, by the way can happen even if <b>Bmodule</b> only imports a function called <b>calc</b>.


## Tk - tkinter

Back to the tkinter example you might have some code like this:

```python
from tkinter import *
```

and then your code uses keywords such as <b>Tk, Menu, Frame, Label, Button</b>.

It is better to explicitly import whatever you need:

```
from tkinter import Tk, Menu, Frame, Label, Button
</code<

Even better (as in easier to read) is to import the <b>tkinter</b> module (with or without an alias):

```
import tkinter as tk
```

and then use the objects of tkinter with their full names:

```python
tk.Tk   instead of Tk
tk.Menu instead of Menu
```

