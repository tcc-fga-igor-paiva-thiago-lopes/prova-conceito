
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
                    "destination": "Salvador",
                    "distance": 2455.5,
                    "cargo_type": "grãos",
                    "cargo_weight": 2300,
                    "start_date": "03/12/2022",
                    "end_date": "04/12/2022",
                    "description": "Soja para Salvador",
                    "company": "Jefferson Caminhões"
                },
                {
                    "id": 2,
                    "origin": "Salvador",
                    "destination": "Goiânia",
                    "distance": 3455.25,
                    "cargo_type": "grãos",
                    "cargo_weight": 1500.75,
                    "start_date": "05/12/2022",
                    "end_date": "07/12/2022",
                    "description": "Volta para Casa",
                    "company": "T&G Transporte"
                }         
            ]
        }
