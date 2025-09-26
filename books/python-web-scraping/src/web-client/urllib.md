# get HTML page using urllib

[urllib](https://docs.python.org/library/urllib.html) is a rather low level library. It comes standard with Python and thus it might be useful for simple tasks.

{% embed include file="src/examples/urllib/with_urllib.py" %}


This code will print the content of the HTML page download from the given web site.

If there is an error the request will raise an exception.

For example if ask for a page that does not exist on the server we'll get a urllib.error.HTTPError  with the text **HTTP Error 404: Not Found**.

If we ask for a URL that does not even resolve we'll get a urllib.error.URLError exception the text **Name or service not known**.

We should probably wrap the code in a `try` - `except` expression.


