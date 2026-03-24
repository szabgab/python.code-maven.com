from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.get('/')
def main_page():
    return '<a href="/goto">Go to</a>'

@app.get('/goto')
def goto():
    return redirect(url_for('user_page'))

@app.get('/user')
def user_page():
    return 'User page'
