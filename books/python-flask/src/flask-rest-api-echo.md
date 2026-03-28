# Flask REST API - Echo


{% embed include file="src/examples/flask/restful_echo/api.py" %}
{% embed include file="src/examples/flask/restful_echo/test_api.py" %}

```
flask --app api run
```

## GET request

```
$ curl -i http://localhost:5000/echo?text=Hello+World!
HTTP/1.1 200 OK
Server: Werkzeug/3.1.6 Python/3.13.7
Date: Sat, 28 Mar 2026 19:50:13 GMT
Content-Type: application/json
Content-Length: 42
Connection: close

{"echo": "Hello World!", "method": "GET"}
```

## POST request

```
$ curl -i -X POST -d 'text=Dear+Flask' http://localhost:5000/echo
HTTP/1.1 200 OK
Server: Werkzeug/3.1.6 Python/3.13.7
Date: Sat, 28 Mar 2026 19:51:40 GMT
Content-Type: application/json
Content-Length: 41
Connection: close

{"echo": "Dear Flask", "method": "POST"}
```

