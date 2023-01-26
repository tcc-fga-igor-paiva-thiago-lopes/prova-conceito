import os

POSTGRES_SETTINGS = {
    "url": os.getenv("DB_URL", "postgresql:///truck_drivers"),
    "port": 27017,
    "db": os.getenv("DB_NAME", "truck_drivers"),
    "username": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "example"),
}

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
