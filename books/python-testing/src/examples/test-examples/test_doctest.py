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


def test_doctest_good_module(root):
    #print(root)

    command = ["python", "-m", "doctest", f"{root}/testing/good/mymath.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert err == b''

def test_doctest_bad_module(root):
    #print(root)

    command = ["python", "-m", "doctest", f"{root}/testing/bad/fibonacci.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b''
    assert err == b''

def test_doctest_bad_module_with_failure(root):
    #print(root)

    command = ["python", "-m", "doctest", f"{root}/testing/failure/fibonacci.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert b'1 item had failures' in out
    assert err == b''


