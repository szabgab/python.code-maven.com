import echo_get
import pytest


@pytest.fixture()
def app():
    print("setup")
    return echo_get.app.test_client()

def test_main(app):
    rv = app.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="GET">' in rv.data

def test_echo(app):
    rv = app.get('/echo?text=Hello')
    assert rv.status == '200 OK'
    assert b'You said: Hello' in rv.data

def test_empty_echo(app):
    rv = app.get('/echo')
    assert rv.status == '200 OK'
    assert b'Nothing to say?' in rv.data

def test_missing_page(app):
    rv = app.get('/qqrq')
    assert rv.status == '404 NOT FOUND'
    assert b'The requested URL was not found on the server.' in rv.data
