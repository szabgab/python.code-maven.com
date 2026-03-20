# Configure logging level

You can set the level of logging inside the code or in an external configuration file.

{% embed include file="src/examples/flask/log/set_level.py" %}

```
flask --app set_level --debug run
```

This will show INFO, WARN, ERROR level log messasges.

