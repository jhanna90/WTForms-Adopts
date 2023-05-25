"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://as1.ftcdn.net/jpg/00/87/77/04/220_F_87770408_I24aLBucB1qf7PftDPl5ev2LY7YOBekK.jpg"

db = SQLAlchemy()


class Pet(db.Model):
    """Adoptable pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Returns pet image."""

        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """Connect db to Flask app."""

    db.app = app
    db.init_app(app)
