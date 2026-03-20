from flask import Flask, request
import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

app.logger.info('Start application')

@app.get("/")
def main():
    app.logger.info("Start main route")
    return """
    <form method="POST" action="/reverse">
    <input name="text">
    <input type="submit" value="Send">
    </form>
    <a href="/other">missing page</a>
    <a href="/divide">Page with exception</a>
    """

@app.get("/divide")
def divide():
    x = 23
    y = 0
    z = x / y
    return "done"

@app.post("/reverse")
def reverse():
    app.logger.info("Start reverse route")
    text = request.form.get('text')
    if text is None:
        return "No data was provided"
    text = text[::-1]
    return text

@app.teardown_appcontext
def end(err):
    # The request object is not available here.
    # err is the exception object, if there was an unhandled exception in one of the routes.
    app.logger.info(f"End {err}")

# This will run at the end of every request. You can add some cleaup code to it.
#app.teardown_appcontext(end)

