from flask import Flask
import logging
app = Flask(__name__)
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['gabor@localhost'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))
if not app.debug:
    app.logger.addHandler(mail_handler)

@app.route("/")
def main():
    app.logger.debug("Some debug message")
    app.logger.info("Some info message")
    app.logger.warning("Some warning message")
    app.logger.error("Some error message")

    return "Hello World"

