import mywebapp

def test_app():
    web = mywebapp.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == 'Hello World!'

