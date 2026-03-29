# Flask JSON API

If instead of a string we return a dictionary, Flask will assume it is an API endpoint
and will return a serialized version of the data structure.

* jsonify

{% embed include file="src/examples/flask/return-json/return_json.py" %}

```
$ curl -I http://localhost:5000/api/info
HTTP/1.0 200 OK
Content-Type: application/json
```
{% embed include file="src/examples/flask/return-json/test_return_json.py" %}


