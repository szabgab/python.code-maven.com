import os
from conftest import capture

def test_mymath_with_pytest(root):
    os.chdir(f"{root}/testing/good/")

    command = ["pytest", "test_mymath_with_pytest.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 1 item' in out
    assert b'test_mymath_with_pytest.py .' in out
    assert b'1 passed in' in out
    assert err == b''

def test_mymath_with_pytest_class(root):
    os.chdir(f"{root}/testing/good/")

    command = ["pytest", "test_mymath_with_pytest_class.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 1 item' in out
    assert b'test_mymath_with_pytest_class.py .' in out
    assert b'1 passed in' in out
    assert err == b''

