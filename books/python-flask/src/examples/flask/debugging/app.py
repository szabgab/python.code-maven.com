from flask import Flask, request
import mymath

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <form action="/area" method="GET">
         Width: <input name="width">
         Height: <input name="height">
         <input type="submit" value="Area">
     </form>
'''

@app.get("/area")
def area():
    width = request.args.get('width')
    height = request.args.get('height')
    if width is None:
        return 'Missing width'
    if height is None:
        return 'Missing height'
    return "The area is {}".format(mymath.area(int(width), int(height)))

