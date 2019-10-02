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
        print(updated_translation)
        if updated_translation.get("status") != translation.status:
            translation.status = updated_translation.get("status")
            translation.translated_text = updated_translation.get(
                "translatedText")

            db.session.add(translation)

    db.session.commit()
