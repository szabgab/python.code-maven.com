from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Echo(Resource):
    def get(self, text):
        return { "GET response": f"Text: {text}" }

    def post(self, text):
        return { "POST response": f"Text: {text}" }


api.add_resource(Echo, '/echo/<text>')

