
# from flask import request
from flask_restful import Resource
from src.resources.utils import simple_error_response

class Trips(Resource):
    def get(self):
        return {
            "list": [
                {
                    "id": 1,
                    "text": "Xablau"
                }
            ] 
        }
