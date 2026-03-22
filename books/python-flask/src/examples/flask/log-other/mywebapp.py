from flask import Flask
from flask.logging import default_handler
import logging

import myapp
myapp_logger = logging.getLogger('myapp')

app = Flask(__name__)

#root = logging.getLogger()
#root.addHandler(default_handler)
#root.addHandler(myapp_logger)

app.logger.debug('debug')
app.logger.info('info')
app.logger.warning('warning')

@app.route("/")
def main():
    app.logger.debug("Some debug message")
    app.logger.info("Some info message")
    app.logger.warning("Some warning message")
    app.logger.error("Some error message")
    myapp.myfunc()
    return "Hello World!"


