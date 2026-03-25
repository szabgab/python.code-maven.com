from flask import Flask, render_template, url_for, redirect, request, session
app = Flask(__name__)
app.secret_key = 'loginner'

users = {
    'admin' : 'secret',
    'foo'   : 'myfoo',
}

@app.get("/")
def main():
    return render_template('main.html')

@app.get('/login')
def login_form():
    return render_template('login.html')

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password and username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('account'))

    return render_template('login.html', error_message="Invalid login")

@app.get("/account")
def account():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    return render_template('account.html', username=username)

@app.get('/logout')
def logout():
    if not session.get('username'):
        return render_template('message.html', message="Not logged in")
    else:
        del session['username']
    return render_template('logout.html')


