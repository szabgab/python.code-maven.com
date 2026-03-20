import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/bad">bad</a>' in rv.data

def test_bad():
    web = app.app.test_client()

    rv = web.get('/bad')
    assert rv.status == '500 INTERNAL SERVER ERROR'
    assert b'<h1>Internal Server Error</h1>' in rv.data

    # TODO: test the other file as well
    # TODO: check the exception text
