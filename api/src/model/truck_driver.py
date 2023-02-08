from src.app import db

class TruckDriver(db.Model):
    __tablename__ = "truck_driver"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
