"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)

default_img = 'https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=default_img)

    def serialize(self):
        """Returns a dict representation of cupcake which we can into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
    
    def __repr__(self):
        return f"< Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating} image_url={self.image} >"