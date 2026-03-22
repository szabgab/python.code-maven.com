# Flask: Run Hello World

In order to run the [Hello World application](./flask-hello-world.md) we execute the `flask` command and provide the name of the file as the value of the `--app` parameter. (We don't need to include the `.py` extension.) We can optionally provide the `--debug` flag as well.

```
flask --app hello --debug run
```

If you are using `uv` then you might want to run

```
uv run flask --app hello --debug run
```

