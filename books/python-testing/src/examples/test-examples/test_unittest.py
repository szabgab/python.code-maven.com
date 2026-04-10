import os
from conftest import capture

def test_mymath_with_unittest_using_python(root):
    os.chdir(f"{root}/testing/good/")

    command = ["python", "test_mymath_with_unittest.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert b'Ran 1 test in' in err
    assert b'OK' in err

def test_mymath_with_unittest_using_unittest(root):
    os.chdir(f"{root}/testing/good/")

    command = ["python", "-m", "unittest", "test_mymath_with_unittest.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert b'Ran 1 test in' in err
    assert b'OK' in err

def test_mymath_with_unittest_separated(root):
    os.chdir(f"{root}/testing/good/")
    command = ["python", "-m", "unittest", "test_mymath_with_unittest_separated.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert b'Ran 4 tests in' in err
    assert b'OK' in err

def test_fibonacci_with_unittest(root):
    os.chdir(f"{root}/testing/bad/")
    command = ["python", "-m", "unittest", "test_fibonacci_with_unittest.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert b'Ran 1 test in' in err
    assert b'OK' in err

def test_fibonacci_with_unittest_failure(root):
    os.chdir(f"{root}/testing/bad/")
    command = ["python", "-m", "unittest", "test_fibonacci_with_unittest_failure.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert out == b''
    assert b'Ran 1 test in' in err
    assert b'FAILED (failures=1)' in err

def test_fibonacci_with_unittest_separated(root):
    os.chdir(f"{root}/testing/bad/")
    command = ["python", "-m", "unittest", "test_fibonacci_with_unittest_separated.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert b'Ran 3 tests in' in err
    assert b'OK' in err

def test_fibonacci_with_unittest_failure_separated(root):
    os.chdir(f"{root}/testing/bad/")
    command = ["python", "-m", "unittest", "test_fibonacci_with_unittest_failure_separated.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert out == b''
    assert b'Ran 4 tests in' in err
    assert b'FAILED (failures=1)' in err

