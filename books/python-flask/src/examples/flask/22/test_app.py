import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<button id="calc">Calc</button>' in rv.data

    # TODO: add more tests
