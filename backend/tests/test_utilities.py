from mocks.translations import MOCK_TRANSLATIONS
from unbabel.models import Translation, TranslationSchema
from unbabel.utilities import (recently_updated_translations,
                               update_translations)


def test_update_translations(app, api, mocker):
    mocker.patch.object(api, "get_translation", return_value={"status": "new"})
    update_translations()

    translation_schema = TranslationSchema()
    translations = [translation_schema.dump(
        translation) for translation in Translation.query.all()]

    # Statuses should be updated to completed!
    for translation_a, translation_b in zip(
            sorted(translations, key=lambda x: list(x.keys())),
            sorted(MOCK_TRANSLATIONS, key=lambda x: list(x.keys()))):
        assert ((translation_a["uid"] == translation_b["uid"]) and
                translation_a["status"] == "completed" and
                translation_b["status"] == "new")


def test_recently_updated_translations(app):
    # Translations updated in last second should equal the inserted mock
    # translations
    recently_updated = recently_updated_translations(1)
    assert isinstance(recently_updated, list)
    assert len(recently_updated) == len(MOCK_TRANSLATIONS)


def test_recently_updated_translations_zero_seconds(app):
    # Nothing was updated in last 0 seconds
    recently_updated = recently_updated_translations(0)
    assert isinstance(recently_updated, list)
    assert len(recently_updated) == 0
