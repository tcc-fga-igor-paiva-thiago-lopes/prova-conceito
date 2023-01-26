
# from flask import request
from flask_restful import Resource
from src.resources.utils import simple_error_response

class Expenses(Resource):
    def get(self):
        return { "list": [] }
