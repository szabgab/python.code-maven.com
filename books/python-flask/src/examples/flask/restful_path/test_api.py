import api
import pytest

@pytest.fixture()
def web():
    return api.app.test_client()


def test_get(web):
    rv = web.get('/echo/hello')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json ==  {'GET response': 'Text: hello'}

def test_post(web):
    rv = web.post('/echo/ciao')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    assert rv.json == {'POST response': 'Text: ciao'}
