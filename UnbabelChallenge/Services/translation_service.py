import requests

# Requires Python3
import json
import urllib3
from flask import request
from base64 import encode
from UnbabelChallenge.Exceptions import UnExc


API_USERNAME = 'fullstack-challenge'
API_KEY = '9db71b322d43a6ac0f681784ebdcc6409bb83359'
WEB_HOST = 'https://unbabel-fs-challenge.herokuapp.com/'


def language_pair(source_language, target_language):
    headers = {
        'Authorization': "ApiKey {}:{}".format(API_USERNAME, API_KEY),
        'Content-Type': "application/json"
    }

    body = {
        'source_language': source_language,
        'target_language': target_language,
        'text_format': "text"
    }

    url = "https://sandbox.unbabel.com/tapi/v2/language-pair/"

    try:
        r = requests.get(url, headers=headers, json=body)
        if r.ok:
            return r.json()
        else:
            return UnExc.API_ERROR

    except:
        return UnExc.API_ERROR



def request_translation(source_language, target_language, text, identifier):
        
    callback_url = WEB_HOST + "/translation/" + identifier #request.host
        
    headers = {
        'Authorization': "ApiKey {}:{}".format(API_USERNAME, API_KEY),
        'Content-Type': "application/json"
    }

    body = {
        'text': text,
        'source_language': source_language,
        'target_language': target_language,
        'callback_url': callback_url,
        'text_format': "text"
    }

    url = 'https://sandbox.unbabel.com/tapi/v2/translation/'

    try:
        r = requests.post(url, headers=headers, json=body)
        if r.ok:
            return r.json()
        else:
            return UnExc.API_ERROR

    except Exception as e:
        print(e)
        return UnExc.API_ERROR