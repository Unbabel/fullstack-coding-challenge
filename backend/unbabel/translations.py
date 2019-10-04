import json

from flask import Blueprint, Response, request
from unbabel.api import Unbabel
from unbabel.models import Translation, TranslationSchema, db
from unbabel.utilities import recently_updated_translations

bp = Blueprint("translations", __name__, url_prefix="/translations")
unbabel = Unbabel()


def json_response(payload, status=200):
    return json.dumps(payload), status, {"Content-Type": "application/json"}


@bp.route("/", methods=("POST", ))
def add_translation():
    text = request.json["text"].strip()
    source_language = request.json["source_language"]
    target_language = request.json["target_language"]

    translation = unbabel.post_translation(
        text, source_language, target_language)

    database_translation = Translation(
        source_language=translation["source_language"],
        status=translation.get("status", "new"),
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


@bp.route("/delete/<translation_uid>", methods=("DELETE",))
def delete_translation(translation_uid):
    translation = Translation.query.filter_by(uid=translation_uid).first()
    response = unbabel.delete_translation(translation_uid)
    db.session.delete(translation)
    db.session.commit()

    return json_response(response)


@bp.route("/stream", methods=("GET",))
def stream_translations():
    translation_schema = TranslationSchema()

    def event_stream():
        while True:
            recently_updated = [
                translation_schema.dump(translation)
                for translation in recently_updated_translations()]
            if recently_updated:
                yield f"data: {json.dumps(recently_updated)}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")
