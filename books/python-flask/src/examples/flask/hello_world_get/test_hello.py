import hello

def test_app():
    web = hello.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == 'Hello World!'

    # You can also test it this way:
    assert rv.data == b'Hello World!'
