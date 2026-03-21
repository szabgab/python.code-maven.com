# Troubleshooting: Address already in use

When you try to run your application you might encounter this error

```
$ flask run
 * Serving Flask app 'app'
 * Debug mode: on
Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
```

This means that there is another application running on the same port. It might be that you have already tried flask in a different window and you have not shut it down.

On Linux or Mac it might be that you used `Ctrl-Z` to stop the program. Which actually only suspends it, but keeps the port used.

The solution is to either find the other instance and close it using `Ctrl-C` or to launch this instance on a different port.

You can do the latter by provideing the `--port` parameter. e.g.

```
$ flask run --app app --debug --port 8080
```


If you have run a flask application in another window, or maybe you moved it to the background, or if there is another application already using port 5000, then you'll see an error indicating that when you try to start Flask.


You can supply `--port 5001` to the command line to use a different port or you can try to locate the other program and shut it down.


Tools to locate the program running on port 5000

## Linux

```
netstat -nlp | grep 5000
```

## Linux and macOS

```
lsof -P -i :5000
```

## Windows

```
netstat -ano | findstr 5000
```

[see also](https://flask.palletsprojects.com/en/stable/server/)



