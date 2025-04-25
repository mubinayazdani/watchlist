from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    watched = db.Column(db.Boolean, default=False)