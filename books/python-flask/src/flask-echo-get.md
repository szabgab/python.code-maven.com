# Flask: Echo GET

The next step in our adventure to learn Flask is to be able to accept input from the user and return a page based on that input.

There are several ways a client (a browser) can send data to a (web) server. One of them is the `GET` method.
This is when you can see the names of the parameters and the values in the address-bar.

request.args is a dictionary. We could write request.args['name'] but then it would raise and excpetion and the whole application would crash
if the user did not send in a value for the "name" field. We could check if the key exists before trying to access the value using the "in" operator,
but that seems like a bit of a waste of work here. Instead we call the "get" method that every dictionary in Python has. It will return None, if the key "name"
did not exists. We could even provide a default value to the "get" method".


{% embed include file="src/examples/flask/echo_get/app.py" %}

---

* request
* request.args


