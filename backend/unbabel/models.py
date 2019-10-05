from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema

db = SQLAlchemy()


class Translation(db.Model):
    """Model for a translation."""

    __tablename__ = "translations"

    source_language = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(), nullable=False, default="new")
    target_language = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)
    text_format = db.Column(db.String(), nullable=False)
    translated_text = db.Column(db.Text(), default=None)
    uid = db.Column(db.String(), nullable=False, primary_key=True, unique=True)

    # Set for streaming updated translations to client
    created_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), nullable=False,
                           default=db.func.current_timestamp())

    def __repr__(self):
        return (f'<Translation uid="{self.uid}"'
                f' status="{self.status}"'
                f' text="{self.text}"'
                f' translated_text="{self.translated_text}">')


class TranslationSchema(ModelSchema):
    class Meta:
        model = Translation
