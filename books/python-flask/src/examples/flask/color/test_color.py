import color
import pytest

@pytest.fixture()
def web():
    return color.app.test_client()


def test_app(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')

# This does not set the color
def test_get(web):
    rv = web.get('/?color=AAAAAA')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')

def test_post(web):
    rv = web.post('/', data={'color': 'AAAAAA'})
    assert rv.status == '200 OK'
    assert 'background-color: #AAAAAA;' in rv.data.decode('utf-8')

    # It is not persistant
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert 'background-color: #FFFFFF;' in rv.data.decode('utf-8')


