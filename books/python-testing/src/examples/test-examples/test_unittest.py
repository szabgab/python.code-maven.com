import pytest
import os
import subprocess

@pytest.fixture()
def root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def capture(command):
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode


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

