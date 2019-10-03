import time
from datetime import datetime, timedelta

from unbabel.api import Unbabel
from unbabel.models import Translation, db

unbabel = Unbabel()


def update_translations():
    app = db.get_app()

    # Need to use the app's context to access the translations
    with app.app_context():
        incomplete_translations = db.session.query(Translation).filter(
            Translation.status != "completed",
            Translation.status != "failed").all()

    for translation in incomplete_translations:
        updated_translation = unbabel.get_translation(translation.uid)

        if updated_translation.get("status") != translation.status:
            translation.status = updated_translation.get("status")
            translation.translated_text = updated_translation.get(
                "translatedText")
            translation.updated_at = datetime.now()

            db.session.add(translation)

    db.session.commit()


def recently_updated_translations():
    last_checked = datetime.now() - timedelta(seconds=10)
    app = db.get_app()

    with app.app_context():
        recently_updated = db.session.query(Translation).filter(
            Translation.updated_at > last_checked
        ).all()

    time.sleep(10)
    return recently_updated
