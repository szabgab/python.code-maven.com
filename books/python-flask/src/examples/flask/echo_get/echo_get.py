from flask import Flask, request
app = Flask(__name__)

@app.get("/")
def main_page():
    return '''
     <form action="/echo" method="GET">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''

@app.get("/echo")
def echo():
    user_text = request.args.get('text', '')
    if user_text:
        return "You said: " + user_text
    return "Nothing to say?"
