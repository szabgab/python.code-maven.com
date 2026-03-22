from flask import Flask

app = Flask(__name__)

@app.get("/")
def main():
    return "Hello World!"

@app.get("/login")
def login():
    return "Showing the login page ..."
