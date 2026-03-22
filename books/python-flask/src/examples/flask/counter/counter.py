from flask import Flask
app = Flask(__name__)

counter = 1

@app.get("/")
def main_page():
    global counter
    counter += 1
    return str(counter)

