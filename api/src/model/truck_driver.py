from src.app import db
from .application_model import ApplicationModel

class TruckDriver(db.Model, ApplicationModel):
    __tablename__ = "TRUCK_DRIVER"

    id = db.Column(db.Integer, db.Identity(start=1, cycle=True), primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }