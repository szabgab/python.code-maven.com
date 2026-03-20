import basic

def test_app():
    web = basic.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'Hello World!'


# TODO: add tests to the other apps and check the output of the logs
