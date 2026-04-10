import os
from conftest import capture

def test_stdout_stderr(root):
    os.chdir(f"{root}/pytest/")

    command = ["pytest", "-s", "-q", "test_stdout_stderr.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert b'stdout during testing' in out
    assert b'Adding 2 to 3' in out
    assert b'2 passed in' in out
    assert b'stderr during testing' in err


