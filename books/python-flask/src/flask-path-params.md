# Flask Path or route parameters

In addition to having routes for fixed pathes, Flask can also handle routes where one or more parts of the path can have any value.

It can be especially useful if the response is then looked up in some sort of a database.

{% embed include file="src/examples/flask/path/path_params.py" %}

* The route `/user/42` works.
* The route `/user/Joe` also works. (Do we want this?)
* The route `/user/` returns 404 not found
* The route `/user` returns 404 not found

```
flask --app path_params run
```


