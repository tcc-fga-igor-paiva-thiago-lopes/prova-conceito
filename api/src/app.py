from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

app.config.from_object("src.config.Config")

db = SQLAlchemy(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

from src.model.truck_driver import TruckDriver

@app.route('/truck_driver', methods=['POST'])
def register_new_driver():
    request_data = request.get_json(force=True)
    
    truck_driver = TruckDriver(name=request_data.get("name"))
    truck_driver.save()

    return truck_driver.to_json(), requests.codes.created

with app.app_context():
    db.create_all()
    db.session.commit()
