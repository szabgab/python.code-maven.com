from flask import Flask, request
app = Flask(__name__)

@app.get("/")
def main_page():
    return '<a href="/calc">calc</a>'

@app.route("/calc", methods=['GET', 'POST'] )
def calc():
    error = ""
    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        try:
            result = float(a) + float(b)
            return str(result)
        except Exception:
            error = "There was a problem"

    return f'''<form method="POST" action="/calc">
        <input name="a">
        <input name="b">
        <input type="submit" value="Compute">
        </form>
        {error}'''

