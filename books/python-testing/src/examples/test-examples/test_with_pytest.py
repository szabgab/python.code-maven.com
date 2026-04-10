import os
from conftest import capture

def test_mymath_with_pytest(root):
    os.chdir(f"{root}/testing/good/")

    command = ["pytest", "test_mymath_with_pytest.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 1 item' in out
    assert b'test_mymath_with_pytest.py .' in out
    assert b'= 1 passed in' in out
    assert err == b''

def test_mymath_with_pytest_class(root):
    os.chdir(f"{root}/testing/good/")

    command = ["pytest", "test_mymath_with_pytest_class.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 1 item' in out
    assert b'test_mymath_with_pytest_class.py .' in out
    assert b'= 1 passed in' in out
    assert err == b''

def test_fibonacci_with_pytest(root):
    os.chdir(f"{root}/testing/bad/")

    command = ["pytest", "test_fibonacci_with_pytest.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 1 item' in out
    assert b'test_fibonacci_with_pytest.py .' in out
    assert b'= 1 passed in' in out
    assert err == b''

def test_fibonacci_with_pytest_failing(root):
    os.chdir(f"{root}/testing/bad/")

    command = ["pytest", "test_fibonacci_with_pytest_failing.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert b'collected 1 item' in out
    assert b'test_fibonacci_with_pytest_failing.py F' in out
    assert b'= 1 failed in' in out
    assert err == b''

def test_fibonacci_with_pytest_failing_separated(root):
    os.chdir(f"{root}/testing/bad/")

    command = ["pytest", "test_fibonacci_with_pytest_failing_separated.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert b'collected 4 items' in out
    assert b'test_fibonacci_with_pytest_failing_separated.py F...' in out
    assert b'= 1 failed, 3 passed in' in out
    assert err == b''

def test_run_all_the_good_tests(root):
    os.chdir(f"{root}/testing/good/")

    command = ["pytest"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 7 items' in out
    assert b'= 7 passed in' in out
    assert err == b''

def test_run_all_the_bad_tests(root):
    os.chdir(f"{root}/testing/bad/")

    command = ["pytest"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert b'collected 19 items' in out
    assert b'= 6 failed, 13 passed in' in out
    assert err == b''

def test_exercise(root):
    os.chdir(f"{root}/testing/")

    command = ["pytest", "test_math.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'collected 3 items' in out
    assert b'= 3 passed in' in out
    assert err == b''


