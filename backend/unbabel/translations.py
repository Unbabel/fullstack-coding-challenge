import json

from flask import Blueprint, request
from unbabel.api import Unbabel
from unbabel.models import Translation, TranslationSchema, db

bp = Blueprint("translations", __name__, url_prefix="/translations")
unbabel = Unbabel()


def json_response(payload, status=200):
    return json.dumps(payload), status, {"Content-Type": "application/json"}


@bp.route("/", methods=("POST", ))
def add_translation():
    text = request.json["text"]
    source_language = request.json["source_language"]
    target_language = request.json["target_language"]

    translation = unbabel.post_translation(
        text, source_language, target_language)

    database_translation = Translation(
        source_language=translation["source_language"],
        status=translation["status"],
        target_language=translation["target_language"],
        text=translation["text"],
        text_format=translation["text_format"],
        uid=translation["uid"]
    )

    db.session.add(database_translation)
    db.session.commit()

    return json_response(translation)


@bp.route("/", methods=("GET", ))
def get_translations():
    translation_schema = TranslationSchema()
    translations = [translation_schema.dump(
        translation) for translation in Translation.query.all()]
    return json_response(translations)
