---
title: "Switch to interactive mode from a Python script"
timestamp: 2016-04-29T09:30:01
tags:
  - code
  - interact
published: true
books:
  - python
author: szabgab
archive: true
---


Instead of stepping through your code with a debugger, you can add some code to your Python script or application
that will instruct it to stop excuting and enter the interactive mode for you to examine what's going on.

This can be especially useful when trying out objects that require complex setup you don't want to type in the
console.


Just add the following lines to your code where you'd like Python to switch to interactive mode:

```python
import code
code.interact(local=locals())
```

The `import` line can be anywhere, but it might be a good idea to put it next to the "code.interact" line
instead of the beginning of your file with all the other `import` statements. This will probably reduce
the chances of forgeting to remove this import statement.

Then run your code as you'd do normally and when it reaches the specific instruction you'll
see the following:

```
Python 2.7.9 (default, Apr  2 2015, 15:34:55)
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>

```

You can then do whatever you do at the console and you even have access to all the variable
Python sees at that point in the code.

Pressing Ctrl-D will get you back to the script.

