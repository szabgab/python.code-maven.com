import app

def test_app_1():
    app.data_file = 'test_1.json'    # manually overwrite

    res = app.do_something()       # it is now test_1.json
    ...

def test_app_2():
    res = app.do_something()      # it is still test_1.json
    ...
