import json
import os

import requests

dirname = os.path.dirname(os.path.realpath(__file__))


class Unbabel():
    def __init__(self):
        config = json.loads(open(f"{dirname}/../../config.json").read())
        username = config["UNBABEL_USERNAME"]
        api_key = config["UNBABEL_API_KEY"]

        self.headers = {
            "Authorization": f"ApiKey {username}:{api_key}",
            "Content-Type": "application/json"
        }
        self.base_url = "https://sandbox.unbabel.com/tapi/v2/"

    def post_translation(self, text, source_language, target_language):
        body = {
            "text": text,
            "source_language": source_language,
            "target_language": target_language,
            "text_format": "text"
        }
        response = requests.post(
            f"{self.base_url}translation/", json=body, headers=self.headers)

        return response.json()

    def get_translation(self, uid):
        response = requests.get(
            f"{self.base_url}translation/{uid}", headers=self.headers)
        return response.json()
