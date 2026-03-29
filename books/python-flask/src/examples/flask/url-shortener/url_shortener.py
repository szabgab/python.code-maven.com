from flask import Flask, request, render_template, redirect
import json
import os
import random

app = Flask(__name__)

# We might want this to be configurable
LENGTH = 8
FILENAME = "short.json"

@app.get("/")
def main_page():
    return render_template("main.html")

@app.post("/add")
def add_url():
    url = request.form.get('url', '')
    if not url:
        return render_template("main.html", error = "No URL provided")

    short = get_unique_short_string()
    save(url, short)
    short_url = f"{request.url_root}r/{short}"
    return render_template("success.html", short=short, short_url=short_url)

@app.get("/r/<short>")
def handle_short_url(short):
    data = load_data()
    url = data.get(short)
    if url:
        return redirect(url)
    return render_template("missing.html", short=short)


def get_unique_short_string():
    # TODO: handle the extreme case when there are no more unique strings
    # TODO: handle when we start to have too many strings and we start to
    # have too many hits.
    while True:
        short = random_short_string(LENGTH)
        if not get_url(short):
            return short

def random_short_string(length):
    # TODO: instead of random we could take time.time() and represent it in base 62
    character = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return "".join(random.sample(character, length))

def load_data():
    data = {}
    if os.path.exists(FILENAME):
        with open(FILENAME) as fh:
            data = json.load(fh)
    return data

def save(url, short):
    data = load_data()
    data[short] = url
    with open(FILENAME, "w") as fh:
        json.dump(data, fh)

def get_url(short):
    data = load_data()
    return data.get(short)

