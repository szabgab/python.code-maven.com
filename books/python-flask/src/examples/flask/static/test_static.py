import static
import pytest

@pytest.fixture()
def web():
    return static.app.test_client()


def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert '<h1>Main page</h1>' in rv.data.decode('utf-8')
    assert '<img src="/static/img/python.png">'  in rv.data.decode('utf-8')
    assert '<a href="/other">other</a>'  in rv.data.decode('utf-8')

def test_other_page(web):
    rv = web.get('/other')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'text/html; charset=utf-8'
    assert '<h2>Other page</h2>' in rv.data.decode('utf-8')
    assert '<img src="/static/img/python.png">' in rv.data.decode('utf-8')

def test_image(web):
    rv = web.get('/static/img/python.png')
    assert rv.status == '200 OK'
    assert rv.headers['Content-Type'] == 'image/png'
    with open("static/img/python.png", "rb") as fh:
        image = fh.read()
    assert image == rv.data

