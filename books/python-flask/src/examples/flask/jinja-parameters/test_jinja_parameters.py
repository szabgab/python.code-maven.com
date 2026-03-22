import jinja_parameters
import pytest

@pytest.fixture()
def web():
    return jinja_parameters.app.test_client()


def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data

def test_echo_data(web):
    rv = web.post('/echo', data={ 'text': 'foo bar' })
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said: <b>foo bar</b>' in rv.data

def test_echo(web):
    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said: <b></b>' in rv.data

