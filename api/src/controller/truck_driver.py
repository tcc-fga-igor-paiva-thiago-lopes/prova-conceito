from flask import request, Blueprint
from src.app import app
from src.model import TruckDriver
import requests

@app.route('/truck_driver', methods=['POST'])
def register_new_driver():
    request_data = request.get_json(force=True)
    
    truck_driver = TruckDriver(name=request_data.get("name"))
    truck_driver.save()

    return truck_driver.to_json(), requests.codes.created

