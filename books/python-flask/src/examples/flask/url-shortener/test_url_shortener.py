import url_shortener
import pytest
from bs4 import BeautifulSoup

@pytest.fixture()
def web():
    return url_shortener.app.test_client()

@pytest.fixture(autouse = True, scope = "function")
def mock_database(monkeypatch, tmpdir):
    mocked_data_file = tmpdir.join('data.json')
    monkeypatch.setattr(url_shortener, 'FILENAME', mocked_data_file)

def test_main_page(web):
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.headers["Content-Type"] == "text/html; charset=utf-8"
    assert '<form action="/add" method="POST">' in rv.data.decode('utf-8')

def test_add_nothing(web):
    rv = web.post('/add')
    assert rv.status == '200 OK'
    assert rv.headers["Content-Type"] == "text/html; charset=utf-8"
    assert b'<span style="color: red">No URL provided</span>' in rv.data

def test_add_data(web):
    url = "https://code-maven.com/"
    rv = web.post('/add', data={ "url": url })
    assert rv.status == '200 OK'
    assert rv.headers["Content-Type"] == "text/html; charset=utf-8"
    soup = BeautifulSoup(rv.data, 'html.parser')
    link = soup.find(id="shortened")
    short = str(link.contents[0])
    assert len(short) == url_shortener.LENGTH

    rv = web.get(f'/r/{short}')
    assert rv.status == '302 FOUND'
    assert rv.headers["Content-Type"] == "text/html; charset=utf-8"
    assert rv.headers["Location"] == url

