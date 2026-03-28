# Flask Jinja template with conditional

* `if`
* `else`
* `endif`

In order to show the correct message, we use an if-else-endif construct.

This works fine on the `/echo` page, but unfortunately the message also shows up on the main page.

How could we avoid that? We could create a new template for the main page where we don't have this
message, but then we will need to duplicate the form. Or we can separate it into another template
and include it in both templates.

{% embed include file="src/examples/flask/jinja-conditional/jinja_conditional.py" %}
{% embed include file="src/examples/flask/jinja-conditional/templates/echo.html" %}
{% embed include file="src/examples/flask/jinja-conditional/test_jinja_conditional.py" %}


