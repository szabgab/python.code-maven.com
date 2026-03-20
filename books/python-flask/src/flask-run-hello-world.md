# Flask: Run Hello World

In order to run the [Hello World application](./flask-hello-world.md) we execute the `flask` command and provide the name of the file as the value of the `--app` parameter. (We don't need to include the `.py` extension.) We can optionally provide the `--debug` flag as well.

```
flask --app hello --debug run
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


