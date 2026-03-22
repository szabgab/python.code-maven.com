import pytest
import flask_app

@pytest.fixture()
def web():
    return flask_app.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Hello World!' == rv.data

def test_main_page(web):
    rv = web.get('/login')
    assert rv.status == '200 OK'
    assert b'Showing the login page ...' == rv.data

