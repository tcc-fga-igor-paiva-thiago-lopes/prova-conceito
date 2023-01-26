from flask import Flask
from flask_restful import Api
from src.resources.trips import Trips
from flask_cors import CORS


def create_app():
    """
    Create the Flask app
    """
    app = Flask(__name__)

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    api = Api(app)

    api.add_resource(Trips, "/trips")


    return app, api, None
