---
title: "Create your own interactive shell with cmd in Python"
timestamp: 2018-02-15T22:30:01
tags:
  - cmd
  - CLI
published: true
books:
  - python
author: szabgab
archive: true
---


When writing an Command Line Interface for an application it could be nice to have an interactive shell
with command completition and history. The [cmd](https://docs.python.org/3/library/cmd.html)
library of Python provides a framework for that.

We will build an application step-by-step. Scroll down to the [end of the page](#full) to see a full example
with all the bells and whistles.


## Skeleton of the Interactive shell

The recommendation is to subclass the Cmd class, so that's what we do here, though as being a skeleton
we don't do anything else with it.

{% include file="examples/python/cli/skeleton.py" %}

We create an instance object of the `MyPrompt` class and immediately call the `cmdloop` method.
We could have used a temporary variable there if we wanted to be a bit more verbose like this:

```
p = MyPrompt()
p.cmdloop()
```

but the result is the same.

When we run this script it will display a default prompt:

```
(Cmd)
```

You can't do much with it. You can type in `?` and press ENTER to get the following help:

```
Documented commands (type help <topic>):
========================================
help
```

help
# (Cmd) Ctrl-C

You can ask for help on `help` by typing in:

```
help help
```

And it will print:

```
List available commands with "help" or detailed help with "help cmd".
```

If you would like to exit the application you need to press `Ctlr-C` and get a `KeyboardInterrupt`.

## First commands

You can add commands to the system by implementing the corresponding `do_*` methods.

{% include file="examples/python/cli/commands.py" %}

We implemented to commands: `exit` and `add`.

When we run the script it will show use the standard prompt:

```
(Cmd)
```

If at this point we press `TAB` twice we get the list of all the available command. In our case that is

```
add   exit  help
```

If we type in `help` we get the following output:

```
(Cmd) help

Documented commands (type help <topic>):
========================================
help

Undocumented commands:
======================
add  exit
```

If we type in `help add` as the help window suggests for the documented commands we get:

```
(Cmd) help add
*** No help on add
```

If we type in `add` followed by some text and press ENTER the system will run the `do_add` method and
pass the text to the method. In our case we get:

```
(Cmd) add Hello World
Adding 'Hello World'
```

If we type in `exit` it will call the `do_exit` method, print "Bye" and exit the `cmdloop`.
In our case it means it will go on and print the string "after".

```
(Cmd) exit
Bye
after
```


## Help - documenting commands

As you could see above, the built-in `help` command had some documentation, but the two command we added did not
have any. There are two ways to add documentation to a command. Either by adding a method with the `help_*` prefix
or by adding docstring to the appropriate `do_*` method.

{% include file="examples/python/cli/help.py" %}

Entering `?` not all the commands are listed under the "Documented commands":

```
(Cmd) ?

Documented commands (type help <topic>):
========================================
add  exit  help
```


We can get help by typing in `help` and the name of the command:

```
(Cmd) help add
Add a new entry to the system.
```

```
(Cmd) help exit
exit the application.
```

We can still exit the application:

```
(Cmd) exit
Bye
```


## Prompt and banner

The default prompt is `(Cmd)` but we can override it using the `prompt` attribute of the class.

In addition we can set a text to be the banner, that is the text shown when we launch the application, before the first prompt
is shown. We only need to assign the text to the `intro` attribute.

{% include file="examples/python/cli/prompt.py" %}

If we run this application we'll see:

```
Welcome! Type ? to list commands
pb>
```


## Default actions

Sometime you might want to be able to freely parse the input. For example if you'd like to implement short, one-letter alternatives
of longer commands. If you implement a method called `default` that method will be called every time a command is
entered that does not correspond to any of the `do_*` methods.

{% include file="examples/python/cli/default.py" %}

In this example we catch stand-alone `x` and `q` characters and call the `do_exit` method for them.


## Ctrl-d EOF

You might have noticed thet if you press `Ctrl-d`, the standard way to exit most command line application, our examples print <b>*** Unknown syntax: EOF</b>. That's because Ctrl-d send an EOF (End Of File) signal and by default Cmd does not know what to do with it.

The solution is to implement the `do_EOF` method that will be called when the user presses `Ctl-d`. As we already have a `do_exit` method, we can just assign that to the `do_EOF` and have both do the same. In order to provide help for the EOF, we can include a function
called `help_EOF` that is assigned the `help_exit` function.

<h2 id="full">Full example</h2>

This examples includes all of the above techniques.

{% include file="examples/python/cli/full.py" %}


See also the [Cmd wiki page](https://wiki.python.org/moin/CmdModule).

