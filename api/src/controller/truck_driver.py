from flask import request, Blueprint
from src.app import app
from src.model import TruckDriver
from .utils import simple_error_response
import requests

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

