# Flask: Echo GET - using `curl` and `requests`

We can test the application externally as well.

For this we first have to make sure the application runs. Then we can use either `curl` the command line too or the `requests` library of Python.

[curl](https://curl.se/)

```
curl http://localhost:5000/
curl http://localhost:5000/echo?text=Sanch+Panza
```

Python [requests](https://docs.python-requests.org/)

```
pip install requests
```

{% embed include file="src/examples/flask/echo_get/client.py" %}

