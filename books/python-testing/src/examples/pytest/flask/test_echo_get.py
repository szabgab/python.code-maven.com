import echo_get

class TestEcho:
    def setup_method(self):
        self.flapp = echo_get.app.test_client()
        print("setup")

    def test_main(self):
        rv = self.flapp.get('/')
        assert rv.status == '200 OK'
        assert b'<form action="/echo" method="GET">' in rv.data

    def test_echo(self):
        rv = self.flapp.get('/echo?text=Hello')
        assert rv.status == '200 OK'
        assert b'You said: Hello' in rv.data

    def test_empty_echo(self):
        rv = self.flapp.get('/echo')
        assert rv.status == '200 OK'
        assert b'Nothing to say?' in rv.data
