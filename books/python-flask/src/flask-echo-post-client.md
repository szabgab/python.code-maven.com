# Flask: Echo POST - `curl` and `requests`

```
curl -X POST http://localhost:5000/echo
```

```
curl --data "text=Sancho Panza" http://localhost:5000/echo
```


```
pip install requests
```



{% embed include file="src/examples/flask/echo_post/client.py" %}

