import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '2'

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '3'

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '4'

def test_app_separate():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '5'
    # The counter is global!


