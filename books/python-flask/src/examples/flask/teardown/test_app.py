import app
import pytest

@pytest.fixture()
def web():
    return app.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form method="POST" action="/reverse">'in rv.data

def test_reverse(web):
    rv = web.post('/reverse', data={ "text": "foo bar" })
    assert rv.status == '200 OK'
    assert b'rab oof' == rv.data

def test_divide(web):
    rv = web.get('/divide')
    assert rv.status == '500 INTERNAL SERVER ERROR'
    assert b'<title>500 Internal Server Error</title>' in rv.data
    #assert b'ZeroDivisionError: division by zero' in rv.data


