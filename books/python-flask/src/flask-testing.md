# Flask Testing with `unittest`

Throughout this book we used `pytest` for writing tests and I think it is the better choice, but some people might want to stick to the `unittest` library so for their sake I prepared an example using `unittest`:

{% embed include file="src/examples/flask/with-unittest/with_unittest.py" %}

{% embed include file="src/examples/flask/with-unittest/test_with_unittest.py" %}

Run with

```
python -m unittes test_app.py
```

Actually you could also use `pytest` to run these tests.

```
pytest
```

