import requests
import os
import json
import logging as logger

from requests import Response

from src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1

from src.utilities.credentials_utils import CredentialsUtils


class RequestUtil(object):
    def __init__(self):
        self.r_json = None
        self.url = None
        self.status_code = None
        self.env = os.environ.get(
            "ENV_URL", "test"
        )  # environ.get is dict() and when you call it with get
        # you can specify default value in this case 'test'. In hosts_config.py all environments are specs.
        # ENV_URL is env var that should be exported and possible values are: test, dev, prod ->
        # will be used as keys to retrieve value from API_HOSTS dict()!
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(
            client_key=CredentialsUtils.get_credentials()["wc_key"],
            client_secret=CredentialsUtils.get_credentials()["wc_secret"],
        )

    def assert_status_code(self, expected_status_code):
        assert self.status_code == expected_status_code, (
            f"Bad status code! "
            f"Expected {expected_status_code}, Actual {self.status_code}. "
            f"URL {self.url}, Response Json {self.r_json}"
        )

    def post(
        self, endpoint, payload=None, headers=None, expected_status_code=200
    ) -> Response:
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        logger.debug(
            f"############################# SENDING API REQUEST VIA ENV: {self.base_url} ######################"
        )
        r = requests.post(
            url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth
        )
        self.r_json = r.json()
        self.status_code = r.status_code
        self.assert_status_code(expected_status_code)
        logger.debug(f"API POST response is: {self.r_json}")
        return r

    def get(
        self, endpoint, payload=None, headers=None, expected_status_code=200
    ) -> Response:
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = self.base_url + endpoint
        logger.debug(
            f"############################# SENDING API REQUEST VIA ENV: {self.base_url} ######################"
        )
        r = requests.get(
            url=self.url, data=json.dumps(payload), headers=headers, auth=self.auth
        )
        self.r_json = r.json()
        self.status_code = r.status_code
        self.assert_status_code(expected_status_code)
        logger.debug(f"API GET response is: {self.r_json}")
        return r

    def put(self):
        pass

    def delete(self):
        pass
