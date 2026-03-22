# Flask: Run Hello World Environment variables

Alternativelly we can set the environment variable **FLASK_APP** to the name of the file without the extension.

We can also set the **FLASK_DEBUG** environment variable to 1 tuning on the debug-mode.

Then we execute `flask run`.

It is a bit different how you do this on Linux or Mac vs. on MS Windows.

In either case once Flask is running, you can use your browser to visit your new web application on  the `http://127.0.0.1:5000/` address or the `http://localhost:5000/` address which is the same.
You can also use `curl` on the command line to see the content of the web page.

Once you had enough enjoying the view of your new application, you can hit Ctr-C to stop the program.

## Linux/Mac:

```
$ FLASK_APP=hello FLASK_DEBUG=1 flask run
```

or

```
$ export FLASK_APP=hello
$ export FLASK_DEBUG=1
$ flask run
```

Then visit: `http://127.0.0.1:5000/` or type in

```
curl http://localhost:5000/
```

## MS Windows

On the command line or in the terminal of PyCharm, VS Code or any other IDE:

```
set FLASK_APP=hello
set FLASK_DEBUG=1
flask run
```


