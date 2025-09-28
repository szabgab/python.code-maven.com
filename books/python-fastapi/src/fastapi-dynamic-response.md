# FastAPI - Dynamic response


* A small step ahead generating part of the content of the response dynamically.

We also start using `uv` to manage packages. So you'll need to [install uv](https://docs.astral.sh/uv/getting-started/installation/) before you try this.


## Dependencies

{% embed include file="src/examples/fastapi/dynamic-response/pyproject.toml" %}

You don't need to do any separate step of installing the dependencies, you can go ahead and run the code:

```
uv run fastapi dev main.py
```

the visit `http://localhost:8000`


In this example we use the [datetime](https://docs.python.org/3/library/datetime.html) module to generate the current time. And return it as the value of the 'date' field.

{% embed include file="src/examples/fastapi/dynamic-response/main.py" %}

## Testing

The testing is  going to be a bit trickier. After all we don't know what will be the exact time when someone runs the tests and thus we cannot compare the returned data to some
exact expectation. In a more advanced example we might mock the time, but for now we'll just make our test a bit more forgiving. We'll only check if the returned data looks like a
date and if can be converted to a `datetime` object.

We check if the JSON returns exactly the fields we are expecting. We need to sort the fields as we don't want to assume the exact order of the fields in the JSON.

* We use an exact match for the text field.
* For the `date` field first we use a rather simple regex to verify that the returned string looks like a timestamp.
* Then we try to load it using the [fromisoformat](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat) method.

{% embed include file="src/examples/fastapi/dynamic-response/test_main.py" %}

In order to run the tests we only need to execute:

```
uv run pytest
```


---

* datetime
* re
* pytest

