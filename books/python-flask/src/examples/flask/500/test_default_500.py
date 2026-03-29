import default_500
import pytest

@pytest.fixture()
def web():
    return default_500.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/bad">bad</a>' in rv.data

def test_bad(web):
    rv = web.get('/bad')
    assert rv.status == '500 INTERNAL SERVER ERROR'
    assert b'<h1>Internal Server Error</h1>' in rv.data

