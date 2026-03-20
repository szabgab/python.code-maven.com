# Address already in use

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

