import requests_mock

from tests.gardena_api_return.authentication_return import authentication_return
from tests.gardena_api_return.locations_return import location_return
from tests.gardena_api_return.devices_return import (
    device_water_control_return,
    device_gateway_return,
    device_mower_return,
    device_sensor_return,
)


def init_mock(smart_system):
    adapter = requests_mock.Adapter()
    adapter.register_uri(
        "POST",
        "https://smart.gardena.com/sg-1/sessions",
        json=authentication_return,
        status_code=200,
    )
    adapter.register_uri(
        "GET",
        "https://smart.gardena.com/sg-1/locations/?user_id=196ab891-a521-872c-ab1d-1685d1e77afc",
        json={"locations": [location_return]},
        status_code=200,
    )
    adapter.register_uri(
        "GET",
        "https://smart.gardena.com/sg-1/devices/?locationId=1c8b301f-22c8-423d-1b4d-ec25315d1377",
        json={
            "devices": [
                device_gateway_return,
                device_mower_return,
                device_sensor_return,
                device_water_control_return,
            ]
        },
        status_code=200,
    )
    smart_system.request_session.mount("https://smart.gardena.com/", adapter)


def init_failed_mock(smart_system):
    adapter = requests_mock.Adapter()
    adapter.register_uri(
        "POST",
        "https://smart.gardena.com/sg-1/sessions",
        json={
            "sessions": {
                "token": "7867e26c-05eb-4a60-bf30-7c3a1b4480aa",
                "user_id": "196ab891-a521-872c-ab1d-1685d1e77afc",
            }
        },
        status_code=200,
    )
    adapter.register_uri(
        "GET",
        "https://smart.gardena.com/sg-1/locations/?user_id=196ab891-a521-872c-ab1d-1685d1e77afc",
        json={},
        status_code=400,
    )
    adapter.register_uri(
        "GET",
        "https://smart.gardena.com/sg-1/devices/?locationId=1c8b301f-22c8-423d-1b4d-ec25315d1377",
        json={},
        status_code=400,
    )
    smart_system.request_session.mount("https://smart.gardena.com/", adapter)
