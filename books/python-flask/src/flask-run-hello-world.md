# Flask: Run Hello World

In order to run the [Hello World application](./flask-hello-world.md) we need to set the environment variable **FLASK_APP** to the name of the file without the extension.

We can also set the **FLASK_DEBUG** environment variable to 1 tuning on the debug-mode, but this is not required for this example.

Then we execute `flask run`.

It is a bit different how you do this on Linux or Mac vs. on MS Windows.

In either case once Flask is running, you can use your browser to visit your new web application on  the `http://127.0.0.1:5000/` address or the `http://localhost:5000/` address which is the same.
You can also use `curl` on the command line to see the content of the web page.

Once you had enough enjoying the view of your new application, you can hit Ctr-C to stop the program.

## Linux/Mac:

```
$ export FLASK_APP=app
$ export FLASK_DEBUG=1
$ flask run
```

or

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

Then visit: `http://127.0.0.1:5000/` or type in

```
curl http://localhost:5000/
```

## MS Windows

On the command line or in the terminal of PyCharm, VS Code or any other IDE:

```
set FLASK_APP=app
set FLASK_DEBUG=1
flask run
```

## Stop the application

To stop the application press `Ctrl-C`,


## Troubleshooting

### Address already in use

When you try to run your application you might encounter this error

```
$ FLASK_APP=app FLASK_DEBUG=1 flask run
 * Serving Flask app 'app'
 * Debug mode: on
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
```

This means that there is another application running on the same port. It might be that you have already tried flask in a different window
and you have not shut it down.

On Linux or Mac it might be that you used `Ctrl-Z` to stop the program. Which actually only suspends it, but keeps the port used.

The solution is to either find the other instance and close it using `Ctrl-C` or to launch this instance on a different port.

You can do the latter by provideing the `--port` parameter. e.g.

```
$ FLASK_APP=app FLASK_DEBUG=1  flask run --port 8080
```

---

* FLASK_DEBUG
* FLASK_APP
* run
* port


