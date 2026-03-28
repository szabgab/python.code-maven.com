from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Hello(Resource):
    def get(self):
        return { "message": "GET - Restful Flask" }
    def post(self):
        return { "message": "POST - Restful Flask" }

api.add_resource(Hello, '/api/hello')

