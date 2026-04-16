import app
import pytest

@pytest.fixture()
def web():
    return app.app.test_client()


def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'Post JSON to /api/calc' == rv.data

def test_calc(web):
    rv = web.post('/api/calc', json={ 'a' : '10', 'b': '2' })
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'application/json'
    resp = rv.json
    assert resp == {
        "a"        :  10,
        "b"        :  2,
        "add"      :  12,
        "multiply" :  20,
        "subtract" :  8,
        "divide"   :  5,
    }

def test_bad_request(web):
    rv = web.post('/api/calc')
    assert rv.status == '415 UNSUPPORTED MEDIA TYPE'

