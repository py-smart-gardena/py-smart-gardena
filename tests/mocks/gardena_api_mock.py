import requests_mock

from tests.gardena_api_return.authentication_return import authentication_return
from tests.gardena_api_return.locations_return import location_return
from tests.gardena_api_return.devices_return import (
    device_water_control_return,
    device_gateway_return,
    device_mower_return,
    device_sensor_return,
)


class GardenaApiMock:
    adapter = requests_mock.Adapter()

    def mount(self, smart_system):
        smart_system.request_session.mount("https://smart.gardena.com/", self.adapter)

    def register_sessions(self):
        return self.adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/sessions",
            json=authentication_return,
            status_code=200,
        )

    def register_locations(self):
        return self.adapter.register_uri(
            "GET",
            "https://smart.gardena.com/sg-1/locations/?user_id=196ab891-a521-872c-ab1d-1685d1e77afc",
            json={"locations": [location_return]},
            status_code=200,
        )

    def register_devices(self):
        return self.adapter.register_uri(
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

    def register_device_sensor_ambient_temperature_refresh_command(
        self, device_id, location_id
    ):
        return self.adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/devices/"
            + device_id
            + "/abilities/ambient_temperature/command?locationId="
            + location_id,
            json={},
            status_code=204,
        )

    def register_device_sensor_light_refresh_command(self, device_id, location_id):
        return self.adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/devices/"
            + device_id
            + "/abilities/light/command"
            "?locationId=" + location_id,
            json={},
            status_code=204,
        )

    def register_device_sensor_humidity_refresh_command(self, device_id, location_id):
        return self.adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/devices/"
            + device_id
            + "/abilities/humidity"
            "/command?locationId=" + location_id,
            json={},
            status_code=204,
        )

    def register_device_water_control_open__close_valve_command(
        self, device_id, location_id
    ):
        return self.adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/devices/"
            + device_id
            + "/abilities/outlet/command?locationId="
            + location_id,
            json={},
            status_code=204,
        )

    def register_mower_command(self, device_id, location_id):
        return self.adapter.register_uri(
            "POST",
            "https://smart.gardena.com/sg-1/devices/"
            + device_id
            + "/abilities/mower/command?locationId="
            + location_id,
            json={},
            status_code=204,
        )


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
