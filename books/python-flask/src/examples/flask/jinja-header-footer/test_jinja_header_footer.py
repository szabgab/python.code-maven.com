import jinja_header_footer

def test_main_page():
    web = jinja_header_footer.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert b'<!DOCTYPE html>' in rv.data
    assert b'<title>Code Maven Jinja include example</title>' in rv.data
    assert b'<h1>Code Maven Jinja include example</h1>' in rv.data
    assert b'<h2>Languages</h2>' in rv.data
    assert b'Timeless' in rv.data
    assert b'</html>' in rv.data
