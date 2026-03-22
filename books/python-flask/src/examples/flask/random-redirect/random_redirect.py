from flask import Flask, redirect
import random

app = Flask(__name__)

urls = [
    'https://code-maven.com/',
    'https://perlmaven.com/',
    'https://hostlocal.com/',
    'https://pydigger.com/',
    'https://szabgab.com/',
]

@app.get('/')
def main_page():
    return '<a href="/random">Random</a>'

@app.get('/random')
def random_redirect():
    return redirect(random.choice(urls))
