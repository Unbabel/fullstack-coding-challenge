import pytest

from flask import Response
from mocks.translations import MOCK_TRANSLATION, MOCK_TRANSLATIONS
from unbabel.models import Translation


def test_add_translation(api, client, mocker):
    mocker.patch.object(api, "post_translation", return_value=MOCK_TRANSLATION)
    translation_count = len(Translation.query.all())

    # Should raise an exception when not passing any JSON and translation count
    # should stay the same
    with pytest.raises(Exception):
        response = client.post("/translations/")
    assert translation_count == len(Translation.query.all())

    response = client.post("/translations/", json={
        "text": "Text", "source_language": "en", "target_language": "es"
    })
    new_translation_count = len(Translation.query.all())

    # Response should be OK and translation count should've increased by 1
    assert isinstance(response, Response)
    assert response.status_code == 200
    assert new_translation_count == translation_count + 1


def test_get_translation(client):
    response = client.get("/translations/")

    assert isinstance(response, Response)
    assert response.status_code == 200


def test_delete_translation(api, client, mocker):
    mocker.patch.object(api, "delete_translation", return_value={})
    translation_count = len(Translation.query.all())

    # Should raise an exception when translation with the given uid can't be
    # found and translation count should stay the same
    with pytest.raises(Exception):
        response = client.delete("/translations/delete/123")
    assert translation_count == len(Translation.query.all())

    response = client.delete("/translations/delete/1")
    new_translation_count = len(Translation.query.all())

    # Response should be OK and translation count should've decreased by 1
    assert isinstance(response, Response)
    assert response.status_code == 200
    assert new_translation_count == translation_count - 1


def test_stream(client):
    response = client.get("/translations/stream")

    assert response.status_code == 200
    assert response.mimetype == "text/event-stream"
