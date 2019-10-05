import pytest

from mocks.translations import MOCK_TRANSLATIONS
from unbabel import create_app
from unbabel.api import Unbabel
from unbabel.models import Translation, db


@pytest.fixture
def app():
    app = create_app(True)

    with app.app_context():
        db.create_all()

        # Insert mock translations into database
        for translation in MOCK_TRANSLATIONS:
            db.session.add(Translation(**translation))
        db.session.commit()

        app.db = db
        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def api():
    return Unbabel()
