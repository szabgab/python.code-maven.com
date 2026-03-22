from flask import Flask
app = Flask(__name__)

@app.get("/")
def main_page():
    return '''
Main<br>
<a href="/user/23">23</a><br>
<a href="/user/42">42</a><br>
<a href="/user/Joe">Joe</a><br>
'''

@app.get("/user/", defaults={ 'uid': 'zero' })
@app.get("/user/<uid>")
def user_by_uid(uid):
    if uid == 'zero':
        return "List users"
    return uid

