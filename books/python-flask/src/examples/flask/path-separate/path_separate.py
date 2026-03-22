from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def main_page():
    return '''
Main<br>
<a href="/user/23">23</a><br>
<a href="/user/42">42</a><br>
<a href="/user/Joe">Joe</a><br>
'''

@app.get("/user/<uid>")
def api_info(uid):
    return uid

@app.get("/user/")
def user():
    return 'User List'
