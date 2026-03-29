from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class Echo(Resource):
    #def get(self):
    #    parser = reqparse.RequestParser()
    #    parser.add_argument('text', type=str, help='Type in some text')
    #    args = parser.parse_args()
    #    text = args.get('text', '')
    #    return { "res": f"Text: {text}" }

    def post(self):
        print("in post")
        parser = reqparse.RequestParser()
        # curl -H "Content-Type: application/json" -d '{"text": 23}' -i http://localhost:5000/echo
        #parser.add_argument('text', type=int, help='Type in some text')

        # curl -H "Content-Type: application/json" -d '{"text": "hello world"}' -i http://localhost:5000/echo
        parser.add_argument('text', help='Type in some text')
        args = parser.parse_args()
        print("parsed")
        return { "Answer": f"You said: {args['text']}" }

class Area(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        # $ curl -H "Content-Type: application/json" -d '{"width": 3, "height": 4}' -i http://localhost:5000/area
        parser.add_argument('width', type=int, help='integer')
        parser.add_argument('height', type=int, help='integer')
        args = parser.parse_args()
        width = args.get('width', 0)
        height = args.get('height', 0)
        area = width * height
        return { "area": area }


api.add_resource(Echo, '/echo')
api.add_resource(Area, '/area')

