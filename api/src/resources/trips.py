
# from flask import request
from flask_restful import Resource
from src.resources.utils import simple_error_response

class Trips(Resource):
    def get(self):
        return {
            "list": [
                {
                    "id": 1,
                    "origin": "São Paulo",
                    "destination": "Bahia",
                    "distance": 2455.5,
                    "cargo_type": "grãos",
                    "cargo_weight": 2300,
                    "start_date": "03/12/2022",
                    "end_date": "04/12/2022",
                    "description": "Xablau",
                    "company": "Jefferson Caminhõess"
                }         
            ] 
        }
