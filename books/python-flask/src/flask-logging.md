# Flask Logging

[Logging](https://flask.palletsprojects.com/en/stable/logging/) is a very useful tool to avoid the need for manual debugging. It also can provide insight as to what happened in a session on the production server. During development you'll be able to see the messages on the terminal where Flask runs. On the production server it can be saved in a log file for later review.

Flask is using the standard [logging](https://docs.python.org/3/library/logging.html) module.

There are several pre-defined [levels of logging](https://docs.python.org/3/library/logging.html#logging-levels). You can use the specific functions to indicate the importance of each log message.


{% embed include file="src/examples/flask/log/basic.py" %}

First run the applicaton without the `--debug` flag and observe that the minimum log-level is set to WARNING.  By default the logger will only show WARNING and ERROR level log.
```
flask --app basic run
```

Then run the application with the `-debug` flag and observe that the log level is now configure to DEBUG level.

```
flask --app basic --debug run
```

{% embed include file="src/examples/flask/log/test_basic.py" %}

