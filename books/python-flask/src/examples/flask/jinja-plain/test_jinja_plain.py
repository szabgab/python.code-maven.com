import jinja_plain
import pytest

@pytest.fixture()
def web():
    return jinja_plain.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data

def test_echo_data(web):
    rv = web.post('/echo', data={'text': 'Hello'})
    assert rv.status == '200 OK'
    assert b'You said: Hello' == rv.data

def test_echo(web):
    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b'You said: ' == rv.data
