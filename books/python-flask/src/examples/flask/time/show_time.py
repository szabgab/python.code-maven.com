from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def main_page():
    return '<a href="/time">show time</a>'

@app.route("/time")
def show_time():
    return str(time.time())
