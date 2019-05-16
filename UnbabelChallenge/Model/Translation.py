from flask_sqlalchemy import SQLAlchemy
from UnbabelChallenge.Services.db_connection import db
from datetime import datetime


class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    target_language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    callback_url = db.Column(db.String(200), nullable=True)
    text = db.Column(db.Text, nullable=False)
    request_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)
    translated_text = db.Column(db.Text, nullable = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Translation('{self.id}', '{self.request_date}')"