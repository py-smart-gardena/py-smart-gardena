import asyncio
import json
import logging
import ssl
import functools

import backoff
from httpx import HTTPStatusError
from websockets.asyncio.client import connect
from websockets.exceptions import ConnectionClosed
from authlib.integrations.httpx_client import AsyncOAuth2Client
from json.decoder import JSONDecodeError
from authlib.integrations.base_client.errors import (
    OAuthError,
    InvalidTokenError
)
from gardena.devices.device_factory import DeviceFactory
from gardena.exceptions.authentication_exception import AuthenticationException
from gardena.location import Location
from gardena.token_manager import TokenManager

MAX_BACKOFF_VALUE = 900

class RateLimitException(Exception):
    pass

@functools.lru_cache(maxsize=1)
def get_ssl_context():
    context = ssl.create_default_context()
    return context

class SmartSystem:

    def __init__(self, client_id=None, client_secret=None, level=logging.INFO, ssl_context=None):
        if client_id is None or client_secret is None:
            raise ValueError("Arguments 'client_id' and 'client_secret' are required")

        logging.basicConfig(level=level, format="%(asctime)s %(levelname)-8s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)

        self.AUTHENTICATION_HOST = "https://api.authentication.husqvarnagroup.dev"
        self.SMART_HOST = "https://api.smart.gardena.dev"
        self.client_id = client_id
        self.client_secret = client_secret
        self.locations = {}
        self.client: AsyncOAuth2Client = None
        self.token_manager = TokenManager(logger=self.logger)
        self.should_stop = False
        self.is_ws_connected = False
        self.ws_status_callback = None

        self.connection_attempts = 0
        self.max_backoff = MAX_BACKOFF_VALUE
        self.base_delay = 5

        self.supported_services = ["COMMON", "VALVE", "VALVE_SET", "SENSOR", "MOWER", "POWER_SOCKET", "DEVICE"]
        self._ssl_context = ssl_context or get_ssl_context()

    def create_header(self, include_json=False):
        headers = {"Authorization-Provider": "husqvarna", "X-Api-Key": self.client_id}
        if include_json:
            headers["Content-Type"] = "application/vnd.api+json"
        return headers

    async def authenticate(self):
        url = self.AUTHENTICATION_HOST + "/v1/oauth2/token"
        extra = {"client_id": self.client_id}
        self.client = AsyncOAuth2Client(self.client_id, self.client_secret, update_token=self.token_saver, grant_type="client_credentials", token_endpoint=url, verify=self._ssl_context)
        self.token_manager.load_from_oauth2_token(await self.client.fetch_token(url, grant_type="client_credentials"))

    async def quit(self):
        self.should_stop = True
        if self.client and self.token_manager.access_token:
            await self.client.post(f"{self.AUTHENTICATION_HOST}/v1/oauth2/revoke", headers={"Authorization": "Bearer " + self.token_manager.access_token}, data={"token": self.token_manager.access_token})

    async def token_saver(self, token, refresh_token=None, access_token=None):
        self.token_manager.load_from_oauth2_token(token)

    async def call_smart_system_service(self, service_id, data):
        args = {"data": data}
        headers = self.create_header(True)
        r = await self.client.put(f"{self.SMART_HOST}/v2/command/{service_id}", headers=headers, data=json.dumps(args, ensure_ascii=False))
        if r.status_code != 202:
            response = r.json()
            raise Exception(f"{r.status_code} : {response['errors'][0]['title']}")

    @backoff.on_exception(backoff.expo, HTTPStatusError, max_value=MAX_BACKOFF_VALUE, logger=logging.getLogger(__name__))
    async def __call_smart_system_get(self, url):
        response = await self.client.get(url, headers=self.create_header())
        if self.__response_has_errors(response):
            return None
        return json.loads(response.content.decode("utf-8"))

    def __response_has_errors(self, response):
        if response.status_code not in (200, 202):
            try:
                r = response.json()
                msg = r['errors'][0]['title'] if 'errors' in r else r.get('message', str(r))
            except JSONDecodeError:
                msg = response.content
            self.logger.error(f"{response.status_code} : {msg}")
            if response.status_code == 401:
                raise AuthenticationException(msg)
            response.raise_for_status()
            return True
        return False

    async def update_locations(self):
        response_data = await self.__call_smart_system_get(f"{self.SMART_HOST}/v2/locations")
        if response_data and "data" in response_data:
            self.locations = {loc['id']: Location(self, loc) for loc in response_data["data"]}
            for loc in self.locations.values():
                loc.update_location_data(loc)
        else:
            self.logger.error("No locations found.")

    async def __get_ws_url(self, location):
        args = {"data": {"type": "WEBSOCKET", "attributes": {"locationId": location.id}, "id": "does-not-matter"}}
        r = await self.client.post(f"{self.SMART_HOST}/v2/websocket", headers=self.create_header(True), data=json.dumps(args, ensure_ascii=False))
        if r.status_code == 429:
            raise RateLimitException("API rate limit reached when retrieving WebSocket URL")
        r.raise_for_status()
        return r.json()["data"]["attributes"]["url"]

    def calculate_backoff_delay(self):
        return min(self.max_backoff, self.base_delay * (2 ** self.connection_attempts))

    async def start_ws(self, location):
        self.connection_attempts = 0

        while not self.should_stop:
            websocket = None

            try:
                self.logger.info(f"Attempting WebSocket connection (Attempt {self.connection_attempts + 1})")
                ws_url = await self.__get_ws_url(location)
                websocket = await self.__launch_websocket_loop(ws_url)
                self.connection_attempts = 0

            except RateLimitException as error:
                self.connection_attempts += 1
                delay = self.calculate_backoff_delay()
                self.logger.warning(f"Rate limit reached: {error}. Backing off for {delay} seconds.")

            except (ConnectionClosed, InvalidTokenError, OAuthError) as error:
                self.connection_attempts += 1
                delay = self.calculate_backoff_delay()
                self.logger.warning(f"WebSocket connection error: {error}. Backing off for {delay} seconds.")

            except Exception as error:
                self.connection_attempts += 1
                delay = self.calculate_backoff_delay()
                self.logger.error(f"Unexpected error: {type(error).__name__}: {error}. Backing off for {delay} seconds.")

            finally:
                self.set_ws_status(False)
                if websocket and websocket.open:
                    try:
                        await websocket.close()
                        self.logger.info("WebSocket connection closed cleanly.")
                    except Exception as close_error:
                        self.logger.warning(f"Error closing WebSocket: {close_error}")

            if not self.should_stop:
                self.logger.info(f"Waiting {delay} seconds before next connection attempt...")
                try:
                    await asyncio.wait_for(self._wait_with_cancel(delay), timeout=delay + 5)
                except asyncio.TimeoutError:
                    pass

    async def _wait_with_cancel(self, delay):
        for _ in range(delay):
            if self.should_stop:
                break
            await asyncio.sleep(1)

    async def __launch_websocket_loop(self, url):
        websocket = await connect(url, ping_interval=150, ping_timeout=60, close_timeout=10, ssl=self._ssl_context, max_size=2 ** 20, compression=None)
        self.set_ws_status(True)
        self.logger.info("WebSocket connected successfully!")

        try:
            while not self.should_stop:
                try:
                    message = await asyncio.wait_for(websocket.recv(), timeout=5.0)
                    self.on_message(message)

                except asyncio.TimeoutError:
                    if not websocket.open:
                        self.logger.warning("WebSocket connection closed unexpectedly.")
                        break

                except ConnectionClosed:
                    self.logger.warning("WebSocket connection closed by server.")
                    break

        except Exception as ex:
            self.logger.error(f"Error in WebSocket message loop: {type(ex).__name__}: {ex}")
            raise

        finally:
            if websocket.open:
                await websocket.close()

        return websocket

    def on_message(self, message):
        data = json.loads(message)
        self.logger.debug(f'Received {data["type"]} message: {message}')

    def add_ws_status_callback(self, callback):
        self.ws_status_callback = callback

    def set_ws_status(self, status):
        self.is_ws_connected = status
        if self.ws_status_callback:
            self.ws_status_callback(status)
