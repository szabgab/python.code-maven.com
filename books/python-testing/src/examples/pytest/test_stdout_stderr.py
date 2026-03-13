import sys
import appprint

def test_hello():
    print("hello testing")
    print("stderr during testing", file=sys.stderr)

def test_add():
    assert appprint.add(2, 3) == 5
