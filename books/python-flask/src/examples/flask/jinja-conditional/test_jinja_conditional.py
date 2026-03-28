import jinja_conditional

def test_main_page():
    web = jinja_conditional.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data

def test_echo_post_params():
    web = jinja_conditional.app.test_client()

    rv = web.post('/echo', data={ 'text': 'foo bar' })
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said: <b>foo bar</b>' in rv.data

def test_echo_post_no_params():
    web = jinja_conditional.app.test_client()

    rv = web.post('/echo')
    assert rv.status == '200 OK'
    assert b'<form action="/echo" method="POST">' in rv.data
    assert b'You said' not in rv.data
    assert b'You did not say anything.' in rv.data

