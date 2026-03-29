import handle_500
import pytest

@pytest.fixture()
def web():
    return handle_500.app.test_client()

def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<a href="/bad">bad</a>' in rv.data

def test_bad(web):
    rv = web.get('/bad')
    assert rv.status == '500 INTERNAL SERVER ERROR'
    assert b'Our Page crashed' in rv.data
    assert b'<b>500 Internal Server Error: The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</b>' in rv.data

