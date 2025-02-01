---
title: "Logging in Python"
timestamp: 2018-06-12T10:00:01
tags:
  - logging
  - getLogger
  - fileHandler
  - StreamHandler
  - Formatter
published: true
books:
  - python
author: szabgab
archive: true
---


We have already seen how to [get started with simple logging in Python](/simple-logging-in-python).
Now let's see a more comlex, but also more flexible way of [logging](https://docs.python.org/3/library/logging.html)


{% include file="examples/python/log.py" %}

We start by importing the [logging](https://docs.python.org/3/library/logging.html) module.

Then we create a logger object using the `getLogger` method. We could pass any string to it to give it a name,
but it is quite common to use the name of the current file which, in modules is in the `__name__` varible.

Then we can set the minimal level of log messages we would like to handle. This defaults to `WARNING`.
It is important to set this to a low value as later setting won't be able to below this value. So setting this
to `DEBUG` will let the output channels we define later to use anything from DEBUG and up.

Then we can create one or more output channels called `Handlers`. The first one is a handler that will write to a file call
`my.log`. We set the minimum logging level to `INFO`. Remember, there is no point in setting this below the global logging level as that already filters out the low-level logging messages.
Then we create a formatter telling the handler how we would like the log lines to be formatted on this output channel.
Finally we add our output handler to the logger.


Then we create another output channel this time using `StreamHandler` that will print to STDERR. Just as we saw in the
[simple Python logging](/simple-logging-in-python) examples.
Here too we set the minimal logging level and the format.
They could be the same as for the filehandler, but they can be also different as in this example.
Finally we add this handler too to the logger object.

This was the setup. We can do this in our main file.

Then anywhere in the application we can call `getLogger` with the same name that we used earlier.
(Because in our example we are in the same file I used the same `__name__`. The call to `getLogger`
will retuturn the same, already configure logging object.

In order to show this I've assigned it to a different variable name.
Then we could use any of the file logging methods.


The result of running this script is that we see the following on the screen (on STDERR):

```
2018-06-12 09:27:38,749 - DEBUG      - debug
2018-06-12 09:27:38,749 - INFO       - info
2018-06-12 09:27:38,749 - WARNING    - warning
2018-06-12 09:27:38,749 - ERROR      - error
2018-06-12 09:27:38,750 - CRITICAL   - critical
```

The content of "my.log" will look like this:

```
2018-06-12 09:27:38,749 - __main__ - INFO       - info
2018-06-12 09:27:38,749 - __main__ - WARNING    - warning
2018-06-12 09:27:38,749 - __main__ - ERROR      - error
2018-06-12 09:27:38,750 - __main__ - CRITICAL   - critical
```


