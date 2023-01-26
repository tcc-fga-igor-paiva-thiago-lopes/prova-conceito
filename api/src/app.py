from flask import Flask
from flask_restful import Api
from src.resources.expenses import Expenses


def create_app():
    """
    Create the Flask app
    """
    app = Flask(__name__)

    api = Api(app)

    api.add_resource(Expenses, "/expenses")


    return app, api, None
