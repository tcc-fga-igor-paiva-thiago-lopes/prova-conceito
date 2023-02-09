from src.app import db
from sqlalchemy.sql import func
from .application_model import ApplicationModel

class TruckDriver(db.Model, ApplicationModel):
    __tablename__ = "TRUCK_DRIVER"

    id = db.Column(db.Integer, db.Identity(start=1, cycle=True), primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password_digest = db.Column(db.String(512))
    last_sign_in_at = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, email, last_sign_in_at=None):
        self.name = name
        self.email = email
        self.last_sign_in_at = last_sign_in_at

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "last_sign_in_at": self.last_sign_in_at,
            "created_at": self.created_at,
            "updated_at": self.updated_at 
        }