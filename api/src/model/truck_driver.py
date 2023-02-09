from src.app import db

class TruckDriver(db.Model):
    __tablename__ = "TRUCK_DRIVER"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
