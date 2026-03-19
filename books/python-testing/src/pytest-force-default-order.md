# PyTest: Force default order

If for some reason we would like to make sure the order remains the same in a given file
even when using the `--random-order` flag, we can add the following two lines of code.

```python
import pytest
pytestmark = pytest.mark.random_order(disabled=True)
```

{% embed include file="src/examples/pytest/order/test_default_order.py" %}


```
$ pytest -v --random-order

test_order.py::test_three PASSED
test_order.py::test_one PASSED
test_order.py::test_two PASSED
test_default_order.py::test_one PASSED
test_default_order.py::test_two PASSED
test_default_order.py::test_three PASSED
```
