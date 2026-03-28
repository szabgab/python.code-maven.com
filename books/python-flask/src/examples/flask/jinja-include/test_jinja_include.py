import jinja_include
import pytest

@pytest.fixture()
def web():
    return jinja_include.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data

    assert b'You did not say anything.' not in rv.data
    assert b'You said: <b>foo bar</b>' not in rv.data

def test_echo_post_param(web):
    rv = web.post('/echo', data={ 'text': 'foo bar' })
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said: <b>foo bar</b>' in rv.data

def test_echo_post_empty_param(web):
    rv = web.post('/echo', data={ 'text': '' })
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said' not in rv.data
    assert b'You did not say anything.' in rv.data

def test_echo_post_no_param(web):
    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said' not in rv.data
    assert b'You did not say anything.' in rv.data

