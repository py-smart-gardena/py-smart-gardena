import json

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session


class GardenaApiClient:
    def __init__(self, email: str, password: str, client_id: str):
        self.connected = False
        self.AUTHENTICATION_HOST = "https://api.authentication.husqvarnagroup.dev"
        self.SMART_HOST = "https://api.smart.gardena.dev"
        self.email = email
        self.password = password
        self.client_id = client_id
        self.oauth_session = None
        self.token = None

    def authenticate(self):
        """
        Authenticate and get tokens.
        This function needs to be called first.
        """
        if not self.connected:
            url = self.AUTHENTICATION_HOST + "/v1/oauth2/token"
            extra = {"client_id": self.client_id}
            self.oauth_session = OAuth2Session(
                client=LegacyApplicationClient(client_id=self.client_id),
                auto_refresh_url=url,
                auto_refresh_kwargs=extra,
                token_updater=self.__token_saver,
            )
            self.token = self.oauth_session.fetch_token(
                token_url=url,
                username=self.email,
                password=self.password,
                client_id=self.client_id,
            )
            self.connected = True

    def call_command(self, service_id, data):
        args = {"data": data}
        headers = self.__create_header(True)

        r = self.oauth_session.put(
            f"{self.SMART_HOST}/v1/command/{service_id}",
            headers=headers,
            data=json.dumps(args, ensure_ascii=False),
        )
        if r.status_code != 202:
            response = r.json()
            raise Exception(f"{r.status_code} : {response['errors'][0]['title']}")

    def call_smart_system_get(self, url):
        response = self.oauth_session.get(
            f"{self.SMART_HOST}{url}", headers=self.__create_header()
        )
        if self.__response_has_errors(response):
            return None
        return json.loads(response.content.decode("utf-8"))

    def disconnect(self):
        # if self.client:
        #     self.client.should_stop = True
        # if self.ws:
        #     self.ws.close()
        if self.oauth_session:
            self.oauth_session.delete(
                f'{self.AUTHENTICATION_HOST}/v1/token/{self.token["refresh_token"]}',
                headers={"X-Api-Key": self.client_id},
            )
            self.oauth_session.delete(
                f'{self.AUTHENTICATION_HOST}/v1/token/{self.token["access_token"]}',
                headers={"X-Api-Key": self.client_id},
            )
        self.connected = False

    def __token_saver(self, token):
        self.token = token

    def __create_header(self, include_json=False):
        headers = {"Authorization-Provider": "husqvarna", "X-Api-Key": self.client_id}
        if include_json:
            headers["Content-Type"] = "application/vnd.api+json"
        return headers

    def __response_has_errors(self, response):
        if response.status_code not in (200, 202):
            r = response.json()
            if "errors" in r:
                msg = "{r['errors'][0]['title']} - {r['errors'][0]['detail']}"
            elif "message" in r:
                msg = f"{r['message']}"

                if response.status_code == 403:
                    msg = f"{msg} (hint: did you 'Connect an API' in your Application?)"
            else:
                msg = f"{r}"

            self.logger.error(f"{response.status_code} : {msg}")

            if response.status_code in (401, 403):
                raise Exception(msg)

            return True
        return False
