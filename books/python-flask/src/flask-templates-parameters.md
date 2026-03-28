# Flask Jinja template with parameters

In this example there is a single variable in the the template `{{ text }}`
that will be replaced by the value passed to the `render_template` function.

This happens in the `echo` function, but not in the `main_page` function.
There we don't pass the parameter - as we don't have any value for it.

That's fine with Jinja, it will put an empty string there, however it will still
show the text `You said:`.

We'll fix that next.

{% embed include file="src/examples/flask/jinja-parameters/templates/echo.html" %}

{% embed include file="src/examples/flask/jinja-parameters/jinja_parameters.py" %}

{% embed include file="src/examples/flask/jinja-parameters/test_jinja_parameters.py" %}


