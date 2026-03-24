from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.get('/')
def main_page():
    return '''<form action="/goto" method="POST">
            <input name="username">
            <input type="submit" value="Go">
        </form>'''

@app.post('/goto')
def login_post():
    username = request.form.get('username')
    if username is None or username == '':
        return redirect(url_for('user_page_central'))
    return redirect(url_for('user_page', name = username))

@app.get('/user/')
def user_page_central():
    return 'List of users'

@app.get('/user/<name>')
def user_page(name):
    return f'Page of {name}'
