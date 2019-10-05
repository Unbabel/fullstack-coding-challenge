import json

from flask import Blueprint, Response, jsonify, request
from unbabel.api import Unbabel
from unbabel.models import Translation, TranslationSchema, db
from unbabel.utilities import recently_updated_translations

bp = Blueprint("translations", __name__, url_prefix="/translations")
unbabel = Unbabel()


@bp.route("/", methods=("POST", ))
def add_translation():
    """Route for adding a translation to the database.

    Raises:
        Exception: required text, source_language and target_language were not
                   provided.

    Returns:
        JSON: The translation that was added to the database.
    """
    try:
        text = request.json["text"].strip()
        source_language = request.json["source_language"]
        target_language = request.json["target_language"]
    except TypeError:
        raise Exception(
            "You must provide text, its source language and a target language!"
        )

    # Get translation from API and insert into database
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

    return jsonify(translation)


@bp.route("/", methods=("GET", ))
def get_translations():
    """Retrieves all translations currently in the database.

    Returns:
        JSON: A list of all translations currently in the database.
    """
    translation_schema = TranslationSchema()
    translations = [translation_schema.dump(
        translation) for translation in Translation.query.all()]

    return jsonify(translations)


@bp.route("/delete/<translation_uid>", methods=("DELETE",))
def delete_translation(translation_uid):
    """Deletes a translation with the given UID from the database and Unbabel's
    API.

    Args:
        translation_uid (int or str): A translation's UID.

    Raises:
        Exception: translation with given UID does not exist in the database.

    Returns:
        JSON: A success message if translation was deleted, or an error message
              if the message could not be deleted via the Unbabel API.
    """
    translation = Translation.query.filter_by(uid=translation_uid).first()

    if not translation:
        raise Exception(
            f"Could not find translation with uid {translation_uid} in "
            "database!")

    response = unbabel.delete_translation(translation_uid)
    db.session.delete(translation)
    db.session.commit()

    return jsonify(response)


@bp.route("/stream", methods=("GET",))
def stream_translations():
    """Streams all recently updated translations. The EventSource interface
    can be used to receive these client-side.

    Returns:
        Response: A server-sent event containing the recently updated
                  translations.
    """
    translation_schema = TranslationSchema()

    def event_stream():
        while True:
            recently_updated = [
                translation_schema.dump(translation)
                for translation in recently_updated_translations()]
            if recently_updated:
                yield f"data: {json.dumps(recently_updated)}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")
