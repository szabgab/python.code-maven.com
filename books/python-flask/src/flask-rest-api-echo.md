# Flask REST API - Echo


{% embed include file="src/examples/flask/restful_echo/api.py" %}
{% embed include file="src/examples/flask/restful_echo/test_api.py" %}

```
flask --app api run
```

## GET request

```
$ curl -i http://localhost:5000/echo
HTTP/1.1 200 OK
Server: Werkzeug/3.1.6 Python/3.13.7
Date: Sat, 28 Mar 2026 19:30:43 GMT
Content-Type: application/json
Content-Length: 32
Connection: close

{"prompt": "Type in something"}
```

## POST request

```
$ curl -X POST -i http://localhost:5000/echo
HTTP/1.1 200 OK
Server: Werkzeug/3.1.6 Python/3.13.7
Date: Sat, 28 Mar 2026 19:31:20 GMT
Content-Type: application/json
Content-Length: 17
Connection: close

{"echo": "This"}
```
