from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Translation(db.Model):
    """
    """
    __tablename__ = "translations"

    created_at = db.Column(db.DateTime(), nullable=False)
    source_language = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    target_language = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)
    text_format = db.Column(db.String(), nullable=False)
    translated_text = db.Column(db.Text(), default=None)
    uid = db.Column(db.String(), nullable=False, primary_key=True, unique=True)
    updated_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f"<Translation {self.uid}>"
