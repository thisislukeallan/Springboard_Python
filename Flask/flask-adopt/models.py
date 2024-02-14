from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)

default_image = 'https://placedog.net/200'

class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, default=default_image)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pet {self.id} {self.name} {self.species} {self.photo_url} {self.age} {self.notes} {self.available}>"