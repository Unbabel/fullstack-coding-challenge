import time
from datetime import datetime, timedelta

from unbabel.api import Unbabel
from unbabel.models import Translation, db

unbabel = Unbabel()


def update_translations():
    """Updates all translations in the database whose status has changed."""

    app = db.get_app()

    # Need to use the app's context to access the translations whose status
    # could still change
    with app.app_context():
        incomplete_translations = db.session.query(Translation).filter(
            Translation.status != "completed",
            Translation.status != "failed").all()

    for translation in incomplete_translations:
        updated_translation = unbabel.get_translation(translation.uid)

        # Status was changed, so translation was updated
        if updated_translation.get("status") != translation.status:
            translation.status = updated_translation.get("status")
            translation.translated_text = updated_translation.get(
                "translatedText")
            translation.updated_at = datetime.now()

            db.session.add(translation)

    db.session.commit()


def recently_updated_translations(since_last_checked=10):
    """Returns all translations that were updated in the last
    `since_last_checked` seconds in the database.

    Args:
        since_last_checked (int, optional): The time in seconds to check for
        updated translations in the database. Defaults to 10.

    Returns:
        list: A list of all recently updated translations.
    """
    last_checked = datetime.now() - timedelta(seconds=since_last_checked)
    app = db.get_app()

    with app.app_context():
        recently_updated = db.session.query(Translation).filter(
            Translation.updated_at > last_checked
        ).all()

    time.sleep(since_last_checked)
    return recently_updated
