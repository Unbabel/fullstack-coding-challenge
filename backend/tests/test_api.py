import pytest

from mocks.translations import MOCK_TRANSLATION


def test_init(api):
    assert api.base_url == "https://sandbox.unbabel.com/tapi/v2/"
    assert "Authorization" in api.headers
    assert "Content-Type" in api.headers


def test_post_translation(api, mocker):
    # POST requests returns nothing, so raise an Exception
    mocker.patch("requests.post", return_value=False)
    with pytest.raises(Exception):
        response = api.post_translation(MOCK_TRANSLATION["uid"])

    # Using the same text, source_language and target_language should result in
    # the same response as the POST request's response
    mocker.patch.object(api, "post_translation",
                        return_value=MOCK_TRANSLATION)

    response = api.post_translation(MOCK_TRANSLATION["text"],
                                    MOCK_TRANSLATION["source_language"],
                                    MOCK_TRANSLATION["target_language"])

    assert response == MOCK_TRANSLATION


def test_get_translation(api, mocker):
    # GET requests returns nothing, so raise an Exception
    mocker.patch("requests.get", return_value=False)
    with pytest.raises(Exception):
        response = api.get_translation(MOCK_TRANSLATION["uid"])

    # Using the same UID should result in the same response as the GET request's
    # response
    mocker.patch.object(api, "get_translation",
                        return_value=MOCK_TRANSLATION)

    response = api.get_translation(MOCK_TRANSLATION["uid"])

    assert response == MOCK_TRANSLATION


def test_delete_translation(api, mocker):
    # DELETE request for translation with UID that does not exist in database
    mocker.patch("requests.delete", return_value=False)
    response = api.delete_translation(123)
    assert response == {"message": "error"}

    # DELETE request for translation with UID that *does* exist in database
    mocker.patch("requests.delete", return_value=True)
    response = api.delete_translation(123)
    assert response == {"message": "success"}
