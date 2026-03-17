# Pytest testing key-value store - environment variable

* We need to be able to set the name of the data file externally. e.g. Using an environment variable.
* This requires some change to the application to make it more testable.
* Luckily this application already had a function called `_get_filename`.

{% embed include file="src/examples/pytest/key-value-store-testable/store.py" %}

{% embed include file="src/examples/pytest/key-value-store-testable/test_store.py" %}

