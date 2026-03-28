from flask import Flask, request, render_template
app = Flask(__name__)

@app.get("/")
def main_page():
    return render_template('echo.html')

@app.post("/echo")
def echo():
    user_text = request.form.get('text', '')
    return render_template('echo.html', text=user_text)
