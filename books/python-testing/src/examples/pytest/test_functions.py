import tempfile
import time

def test_one():
    db_server = setup_db_server()
    db = setup_db()
    print(f"    test_one         {db}")
    assert True
    print("    test_one after")
    teardown_db(db)
    # teardown_db_server(db_server)

def test_two():
    db_server = setup_db_server()
    db = setup_db()
    print(f"    test_two         {db}")
    assert False
    print("    test_two after")
    teardown_db(db)
    # teardown_db_server(db_server)

def test_three():
    db_server = setup_db_server()
    db = setup_db()
    print(f"    test_three       {db}")
    assert True
    print("    test_three after")
    teardown_db(db)
    # teardown_db_server(db_server)

def setup_db():
    db = str(time.time()).replace(".", "_")
    print(f"setup_db             {db}")
    return db

def teardown_db(db):
    print(f"teardown_db          {db}")


def setup_db_server():
    print("setup db_server")
    if 'db_server' not in setup_db_server.__dict__:
        setup_db_server.db_server = tempfile.TemporaryDirectory()
        setup_db_server.time = time.time()
        print(f"new   db_server environment {setup_db_server.db_server.name}")
    return setup_db_server.db_server

def teardown_db_server(db_server):
    print("teardown_db_server {setup_db_server.db_server.name}")

