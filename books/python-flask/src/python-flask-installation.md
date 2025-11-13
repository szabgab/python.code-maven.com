# Python Flask installation

There is nothing special. You install flask as you'd install any other Python package. Using some kind of virtual envrionment is recommended here too.

```bash
virtualenv venv -p python3
source venv/bin/activate

pip install flask
```

## Install using uv

[uv](https://docs.astral.sh/uv/) is avery fast package and project manager. After installing uv you can do the following.

```
$ uv init flask-demo
$ cd flask-demo
$ uv add flask
```

Rename the `main.py` file to `app.py` to make it easier to follow along.


```
$ uv run flask run
```

