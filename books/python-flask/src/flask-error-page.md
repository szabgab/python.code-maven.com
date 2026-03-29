# Flask 500 Internal Server Error page

{% embed include file="src/examples/flask/500/default_500.py" %}

{% embed include file="src/examples/flask/500/test_default_500.py" %}

Will not trigger in debug mode!

```
$ flask --app default_500 run
```

```
curl -I http://localhost:5000/not

HTTP/1.0 500 INTERNAL SERVER ERROR
```

{% embed include file="src/examples/flask/500/handle_500.py" %}

{% embed include file="src/examples/flask/500/test_handle_500.py" %}

```
$ flask --app handle_500 run
```
