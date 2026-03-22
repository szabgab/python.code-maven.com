import app

def test_app():
    web = app.myapp.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == 'Main'

