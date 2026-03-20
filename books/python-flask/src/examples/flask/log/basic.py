from flask import Flask
app = Flask(__name__)

# This is logged when the server starts
app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')

@app.route("/")
def main():
    app.logger.debug("Some debug message")
    app.logger.info("Some info message")
    app.logger.warning("Some warning message")
    app.logger.error("Some error message")
    return "Hello World!"


