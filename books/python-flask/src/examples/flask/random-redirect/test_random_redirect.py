import random_redirect
import pytest

@pytest.fixture()
def web():
    return random_redirect.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/random">Random</a>'

def test_random(web):
    rv = web.get('/random')
    assert rv.status == '302 FOUND'
    assert 'https://' in rv.headers['Location']
    print(rv.headers['Location'])
    assert rv.headers['Location'] in random_redirect.urls
