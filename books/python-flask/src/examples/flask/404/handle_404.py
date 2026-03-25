from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return 'Main <a href="/not">404 page</a>'

@app.errorhandler(404)
def not_found(err):
    return f"Design your own 'Not found' page! {err}", 404
