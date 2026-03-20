import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form method="POST" action="/reverse">'in rv.data

def test_reverse():
    web = app.app.test_client()

    rv = web.post('/reverse', data={ "text": "foo bar" })
    assert rv.status == '200 OK'
    assert b'rab oof' == rv.data

def test_divide():
    web = app.app.test_client()

    rv = web.get('/divide')
    assert rv.status == '500 INTERNAL SERVER ERROR'
    assert b'<title>500 Internal Server Error</title>' in rv.data
    #assert b'ZeroDivisionError: division by zero' in rv.data


