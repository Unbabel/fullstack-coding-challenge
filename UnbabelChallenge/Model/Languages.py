from flask_sqlalchemy import SQLAlchemy
from UnbabelChallenge.Services.db_connection import db
from datetime import datetime


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String(5), nullable=False)
    full_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Language('{self.id}', '{self.short_name}', '{self.full_name}')"

