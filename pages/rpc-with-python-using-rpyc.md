---
title: "RPC with Python using RPyC"
timestamp: 2018-12-15T20:40:01
tags:
  - rpyc
published: true
books:
  - python
author: szabgab
archive: true
---


[RPyC](https://rpyc.readthedocs.io/) provides remote procedure call, or more precisely,
<b>Remote Python Call</b> between two computers.

On both machines we need to have Python and the RPyC package installed and on the server we need to launch a process
before we can talk to it. The nice thing is that it runs on all the 3 major Operating systems: Linux, Mac OSX, and MS Windows,
and you can make RPyC between machines running different OS-es.



## Install RPyC

It is simple just type

```
pip install rpyc
```

## Run the RPyC server

Nothing special needed. just run the `rpyc_classic.py` script that came with the `RPyC` installation:

```
rpyc_classic.py
```

It will print something like this to the console, and then it will wait for a client to connect.
As the client access the server we will see further output appearing on the console.

```
INFO:SLAVE/18812:server started on [0.0.0.0]:18812
```


## Simple module use

{% include file="examples/python/rpyc_modules.py" %}

This example, as all the other examples here require the name or IP address of remote server on the command line.
So you'd run

```
python rpyc_modules.py remote_machine
```

If you wanted to run this on `remote_machine`

or you'd run

```
python rpyc_modules.py localhost
```

if you had only one computer and wanted to see how you can talk to yourself.

In this simple script we connect to a remote server using the following call:

```python
conn = rpyc.classic.connect(server)
```

Then we can use the connection object stored in `conn` to execute commands on the remote server.

We can attache a local name to a remote Python object. For example this line connects the `rsys`
name on our client to the `sys` object on the server. (It automatically imports the `sys` module
on the server.)

```python
rsys = conn.modules.sys
```

Once we have made that call we can use the `rsys` on the client just as we would use `sys`
on the server. For example we can access its attributes and print them on the console of the client:

```python
print(rsys.version)
```

The same with the `os` module in the above code.

## Persistent variables on the server

On the next example we use the `execute` and `eval` methods of the connection object.
The `execute` method will, execute arbitrary code on the server. In our example first we
create a variable with a new value. Then we change the content of the variable.

Finally we use the `eval` method to evaluate an expression and return the results.

{% include file="examples/python/rpyc_variables.py" %}

The super nice thing is that it will take any data structure we have on the server and replicate it locally.
So in the second set of calls we create a dictionary on the server, we modify it, and then we copy it back to the client
using the `eval` method.

On the client we get a copy of the remote object.

Better yet, we can use the `namespace` attribute of the connection object
which is a dictionary where the keys are the object in on the remote server. For example the
variables we created there. Thus `conn.namespace["scores"]` refers to the object called
`scores` on the remote machine. We can access and even change the object and its attributes
with regular Python code like this:

```python
conn.namespace["scores"]["Bar"] += 58
```


## Remote exception handling

{% include file="examples/python/rpyc_exception.py" %}

If an exception occurs on the server, it is printed to the console of the server
and the exception itself is propagated to the client.

Meaning that the last print-statement will not be executed.

You can catch the remote exception locally the same way you'd catch
local exceptions.


```
Traceback (most recent call last):
  File "rpyc_exception.py", line 12, in <module>
    conn.execute('z = x/y')
  File "/Users/gabor/venv3/lib/python3.6/site-packages/rpyc/core/netref.py", line 199, in __call__
    return syncreq(_self, consts.HANDLE_CALL, args, kwargs)
  File "/Users/gabor/venv3/lib/python3.6/site-packages/rpyc/core/netref.py", line 72, in syncreq
    return conn.sync_request(handler, oid, *args)
  File "/Users/gabor/venv3/lib/python3.6/site-packages/rpyc/core/protocol.py", line 523, in sync_request
    raise obj
ZeroDivisionError: division by zero

========= Remote Traceback (1) =========
Traceback (most recent call last):
  File "/home/gabor/venv3/lib/python3.6/site-packages/rpyc/core/protocol.py", line 347, in _dispatch_request
    res = self._HANDLERS[handler](self, *args)
  File "/home/gabor/venv3/lib/python3.6/site-packages/rpyc/core/protocol.py", line 624, in _handle_call
    return self._local_objects[oid](*args, **dict(kwargs))
  File "/home/gabor/venv3/lib/python3.6/site-packages/rpyc/core/service.py", line 154, in exposed_execute
    execute(text, self.exposed_namespace)
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
```

## Upload code - run function

Based on the above example we could upload and `execute</h> any Python code.
If that was a function definition then we would effectively create a new function on
the remote server which can be later executed.

For clarity I've moved the code that should be executed remotely to a separate file.
It is a simple implementation of the Fibonacci function:

{% include file="examples/python/remote_code.py" %}

Then there is code that will load this file in the client as a plain text, then
call `execute` on the connection object to execute the function definition
on the remote machine.

After we executed the code, we can use the `namespace` attribute of the connection
to access the function and call it with any parameter.

{% include file="examples/python/rpyc_exception.py" %}

{% include file="examples/python/rpyc_timeout.py" %}

{% include file="examples/python/rpyc_reconnect_objects.py" %}

{% include file="examples/python/rpyc_ping.py" %}


{% include file="examples/python/rpyc_with_reconnect.py" %}


Modules problem, might be solved with [properties](/slides/python/property-fixing-bad-api-with-decorators)
[L109](https://github.com/tomerfiliba/rpyc/blob/c362ebc9969b4385bbebf3043ecd97ef2a374e96/rpyc/core/service.py#L109)

