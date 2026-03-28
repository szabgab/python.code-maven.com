# Flask REST API - Hello World

{% embed include file="src/examples/flask/restful_hello/api.py" %}
{% embed include file="src/examples/flask/restful_hello/test_api.py" %}

```
flask --app api run
```

## GET request

```
$ curl -i http://localhost:5000/api/hello
HTTP/1.1 200 OK
Server: Werkzeug/3.1.6 Python/3.13.7
Date: Sat, 28 Mar 2026 19:42:26 GMT
Content-Type: application/json
Content-Length: 35
Connection: close

{"message": "GET - Restful Flask"}
```

## POST request

```
$ curl -i -X POST http://localhost:5000/api/hello
HTTP/1.1 200 OK
Server: Werkzeug/3.1.6 Python/3.13.7
Date: Sat, 28 Mar 2026 19:43:19 GMT
Content-Type: application/json
Content-Length: 36
Connection: close

{"message": "POST - Restful Flask"}
```

