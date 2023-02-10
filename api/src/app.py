from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
from src.controller.utils import simple_error_response

app = Flask(__name__)

app.config.from_object("src.config.Config")

db = SQLAlchemy(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

api = Api(app)

from src.model.truck_driver import TruckDriver

@app.route('/truck_driver', methods=['POST'])
def register_new_driver():
    request_data = request.get_json(force=True)
    
    REQUIRED_FIELDS = ["name", "email", "password", "password_confirmation"]

    missing_fields = []

    for field in REQUIRED_FIELDS:
        if request_data.get(field, None) is None:
            missing_fields.append(field)

    if len(missing_fields) > 0:
        return simple_error_response(
            f"Os seguintes campos são obrigatórios: {missing_fields.join(', ')}.",
            requests.codes.unprocessable_entity
        )

    try:
        truck_driver = TruckDriver(
            name=request_data.get("name"),
            email=request_data.get("email"),
            password=request_data.get("password"),
            password_confirmation=request_data.get("password_confirmation")
        )

        truck_driver.save()
    except Exception as error:
        return simple_error_response(
            f"Falha ao salvar usuário: {error}",
            requests.codes.unprocessable_entity
        )

    return truck_driver.to_json(), requests.codes.created


with app.app_context():
    db.create_all()
    db.session.commit()
