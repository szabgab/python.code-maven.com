import echo_post
import pytest

@pytest.fixture()
def web():
    return echo_post.app.test_client()

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action="/echo" method="POST">' in rv.data.decode('utf-8')

def test_echo_get(web):
    rv = web.get('/echo')
    assert rv.status == '405 METHOD NOT ALLOWED'
    assert '<title>405 Method Not Allowed</title>' in rv.data.decode('utf-8')

def test_echo_post_nothing(web):
    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b"Nothing to say?" == rv.data

def test_echo_post_data(web):
    rv = web.post('/echo', data={ "text": "foo bar" })
    assert rv.status == '200 OK'
    assert b"You said: foo bar" == rv.data
