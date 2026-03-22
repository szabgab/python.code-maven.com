import echo_get

def test_main_page():
    web = echo_get.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<form action="/echo" method="GET">' in rv.data.decode('utf-8')

def test_echo_no_params():
    web = echo_get.app.test_client()
    rv = web.get('/echo')
    assert rv.status == '200 OK'
    assert b"Nothing to say?" == rv.data

def test_echo_no_text():
    web = echo_get.app.test_client()
    rv = web.get('/echo?text=')
    assert rv.status == '200 OK'
    assert b"Nothing to say?" == rv.data

def test_echo_text():
    web = echo_get.app.test_client()
    rv = web.get('/echo?text=foo+bar')
    assert rv.status == '200 OK'
    assert b"You said: foo bar" == rv.data
