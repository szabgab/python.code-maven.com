import os
import subprocess
import pytest

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


