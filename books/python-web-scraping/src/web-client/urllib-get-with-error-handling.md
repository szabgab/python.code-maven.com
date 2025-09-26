# urllib GET with error handling


The [urllib](https://docs.python.org/3/library/urllib.html) module is split into several submodules. One of them is the [urllib.error](https://docs.python.org/3/library/urllib.error.html)
that defines the exceptions raised by [urllib.request](https://docs.python.org/3/library/urllib.request.html)


{% embed include file="src/examples/urllib/urllib_error_handling.py" %}

We are using the [httpbin](https://httpbin.org/) service locally.

Asking for the main page we get a proper response with content:

```
$ python3 urllib_error_handling.py http://localhost/
Success: Downloaded 9593 characters.
```

## no name resolution

If we try to access a site, but there is no DNS name resolution we get a `URLError` and we can check `reason` field to see what was the problem.

```
$ python3 urllib_error_handling.py http://notlocalhost
URLError: <urlopen error [Errno -3] Temporary failure in name resolution>
[Errno -3] Temporary failure in name resolution
```

## Connection refused

If the name resolution works, but the web server does not work (in our case we don't run any service on port 8081 locally) then again we get an `URLError`
but with a different `reason`.

```
$ python3 urllib_error_handling.py http://localhost:8081
URLError: <urlopen error [Errno 111] Connection refused>
[Errno 111] Connection refused
```

## 404 NOT FOUND

We can ask the httpbin service to return specific status codes. That's a very nice way to test how our code behaves when it receives am "unexpected" status code.

```
$ python3 urllib_error_handling.py http://localhost/status/404
not found
HTTPError: HTTP Error 404: NOT FOUND
```

So we received an `HTTPError` and we could even find out what was the exact status code.

## 500 INTERNAL SERVER ERROR

We can even ask the httpbin service to return a 500 error.

```
$ python3 urllib_error_handling.py http://localhost/status/500
internal error
HTTPError: HTTP Error 500: INTERNAL SERVER ERROR
```


## 401 UNAUTHORIZED

We can ask httpbin to return a 401 status code. Our example does not have any special treatment for that so we just print "Unhandled error".

```
$ python3 urllib_error_handling.py http://localhost/status/401
Unhandled error: 401
HTTPError: HTTP Error 401: UNAUTHORIZED
```


## 301 redirection

However, redirections, such as the 301 status code, does not trigger an exception. So if we will want to handle these as well, we'll have to use another approach.

```
$ python3 urllib_error_handling.py http://localhost/status/301
Success: Downloaded 228 characters.
```


