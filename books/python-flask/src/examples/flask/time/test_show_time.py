import show_time
import re

def test_home():
    web = show_time.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert rv.data == b'<a href="/time">show time</a>'

def test_time():
    web = show_time.app.test_client()

    rv = web.get('/time')
    assert rv.status == '200 OK'
    assert re.search(r'\d+\.\d+$', rv.data.decode('utf-8'))
