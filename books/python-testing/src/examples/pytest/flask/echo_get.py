from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
<form action="/echo" method="GET">
<input name="text">
<input type="submit" value="Echo">
</form>
'''

@app.route("/echo")
def echo():
    answer = request.args.get('text')
    if answer:
        return "You said: " + answer
    else:
        return "Nothing to say?"

