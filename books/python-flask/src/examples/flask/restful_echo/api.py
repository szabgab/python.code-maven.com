from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class Echo(Resource):
    def get(self):
        user_text = request.args.get('text', '')
        return { "echo": user_text, "method": "GET" }
    def post(self):
        user_text = request.form.get('text', '')
        return { "echo": user_text, "method": "POST" }

api.add_resource(Echo, '/echo')

