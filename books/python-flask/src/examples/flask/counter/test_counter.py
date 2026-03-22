import counter
import pytest

@pytest.fixture()
def web():
    return counter.app.test_client()


def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '2'

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '3'

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '4'

def test_app_separate(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data.decode('utf-8') == '5'
    # The counter is global!


