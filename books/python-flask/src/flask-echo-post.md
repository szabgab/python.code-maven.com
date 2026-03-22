# Flask: Echo POST - The `request` object of Flask and the `form`


* [request](https://flask.palletsprojects.com/en/stable/api/#flask.Request)
* [request.form](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form)

There is also a dictionary called "request.form" that is get filled by data submitted using a POST request. This too is a plain Python dictionary.
In this case too we can use either the "request.form.get('field', '')" call we can use the "in" operator to check if the key is in the dictionary and then the regular dicstionary look-up.

{% embed include file="src/examples/flask/echo_post/echo_post.py" %}

```
flask --app echo_post run
```

