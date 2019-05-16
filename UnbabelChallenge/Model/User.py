from flask_sqlalchemy import SQLAlchemy
from UnbabelChallenge.Services.db_connection import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    translations = db.relationship('Translation', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"