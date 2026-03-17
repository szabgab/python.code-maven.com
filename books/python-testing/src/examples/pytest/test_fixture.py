import tempfile
import time

def setup_module():
    global db_server
    db_server = tempfile.TemporaryDirectory()
    print(f"setup_module:         {db_server.name}")

def teardown_module():
    print(f"teardown_module       {db_server.name}")


def setup_function():
    global db
    db = time.time()
    print(f"  setup_function                                              {db}")

def teardown_function():
    print(f"  teardown_function                                          {db}")


def test_one():
    print(f"    test_one          {db_server.name} {db}")
    assert True
    print("    test_one after")

def test_two():
    print(f"    test_two          {db_server.name} {db}")
    assert False
    print("    test_two after")

def test_three():
    print(f"    test_three        {db_server.name} {db}")
    assert True
    print("    test_three after")
