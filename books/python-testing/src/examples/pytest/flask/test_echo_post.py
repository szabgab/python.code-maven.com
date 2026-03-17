import echo_post

class TestEcho:
    def setup_method(self):
        self.flapp = echo_post.app.test_client()
        print("setup")

    def test_main_page(self):
        rv = self.flapp.get('/')
        assert rv.status == '200 OK'
        assert '<form action="/echo" method="POST">' in rv.data.decode('utf-8')

    def test_echo_get(self):
        rv = self.flapp.get('/echo')
        assert rv.status == '405 METHOD NOT ALLOWED'
        assert '<title>405 Method Not Allowed</title>' in rv.data.decode('utf-8')

    def test_echo_post_empty(self):
        rv = self.flapp.post('/echo')
        assert rv.status == '200 OK'
        assert b"Nothing to say?" == rv.data

    def test_echo_post_with_data(self):
        rv = self.flapp.post('/echo', data={ "text": "foo bar" })
        assert rv.status == '200 OK'
        assert b"You said: foo bar" == rv.data

    def test_echo_404(self):
        rv = self.flapp.get('/qqrq')
        assert rv.status == '404 NOT FOUND'
        assert b'The requested URL was not found on the server.' in rv.data

