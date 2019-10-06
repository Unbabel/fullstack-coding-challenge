import json
import os

import requests


class Unbabel():
    def __init__(self):
        username = os.getenv("UNBABEL_USERNAME")
        api_key = os.getenv("UNBABEL_API_KEY")

        self.headers = {
            "Authorization": f"ApiKey {username}:{api_key}",
            "Content-Type": "application/json"
        }
        self.base_url = "https://sandbox.unbabel.com/tapi/v2/"

    def post_translation(self, text, source_language, target_language):
        """Posts a translation to the Unbabel API.

        Args:
            text (str): The text that will be translated to the target language.
            source_language (str): The language the text is written in.
            target_language (str): The language the text will be translated to.

        Raises:
            Exception: POST request could not be sent.

        Returns:
            JSON: A translation from the Unbabel API.
        """
        body = {
            "text": text,
            "source_language": source_language,
            "target_language": target_language,
            "text_format": "text"
        }
        response = requests.post(
            f"{self.base_url}translation/", json=body, headers=self.headers)

        if not response:
            raise Exception("POST request could not be sent.")

        return response.json()

    def get_translation(self, uid):
        """Gets a translation from the Unbabel API.

        Args:
            uid (str or int): The UID of the requested translation.

        Raises:
            Exception: GET request could not be sent.

        Returns:
            JSON: A translation from the Unbabel API.
        """
        response = requests.get(
            f"{self.base_url}translation/{uid}", headers=self.headers)

        if not response:
            raise Exception("GET request could not be sent.")

        return response.json()

    def delete_translation(self, uid):
        """Deletes a translation via the Unbabel API.

        Args:
            uid (str or int): The UID of the requested translation.

        Returns:
            dict: A dictionary with a success message on success, or a
                  dictionary with an error message on failure.
        """
        response = requests.delete(
            f"{self.base_url}translation/{uid}", headers=self.headers)

        if not response:
            return {"message": "error"}
        return {"message": "success"}
