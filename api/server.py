from src.app import app, db
from flask.cli import FlaskGroup
from src.model.truck_driver import TruckDriver

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(
        TruckDriver(
            name="John",
            email="john@mail.com",
            password="password123",
            password_confirmation="password123"
        )
    )
    db.session.commit()
