# Flask Path or route parameters - testing

The test here get a bit complex. We have 3 different test-functions. Each one needs the variable returned by the `test_client` function.

While the route with the parameter can handle any value, there is one route that it does not handle. If the visitor reached the page `/user/` page either by mistake or by removing the parameter in the URL, then we'll see a `404 Not Found` page.

{% embed include file="src/examples/flask/path/test_path_params.py" %}

