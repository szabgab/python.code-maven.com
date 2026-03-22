from flask import Flask, redirect

app = Flask(__name__)

@app.get('/')
def main_page():
    return '<a href="/cm">Go to Code Maven</a>'

@app.get('/cm')
def cm():
    return redirect('https://code-maven.com/')
