from flask import Flask
from flask_restful import Api
from src.resources.trips import Trips
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("src.config.Config")

db = SQLAlchemy(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

api.add_resource(Trips, "/trips")

from src.model.truck_driver import TruckDriver

with app.app_context():
    db.create_all()
    db.session.commit()
