import pytest
import unittest
import requests_mock
import requests
from requests import HTTPError
from gardena.smart_system import SmartSystem


def init_mock(smart_system):
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
        "https://smart.gardena.com/sg-1/locations",
        json={
            "locations": [
                {
                    "id": "1c8b301f-22c8-423d-1b4d-ec25315d1377",
                    "name": "My Garden",
                    "devices": [
                        "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
                        "e3c1b615-7351-25fc-a551-1908254a2b3e",
                    ],
                }
            ]
        },
        status_code=200,
    )
    adapter.register_uri(
        "GET",
        "https://smart.gardena.com/sg-1/devices",
        json={
            "devices": [
                {
                    "id": "75cfc1f8-a20c-51d6-c5ea-1b5ecdde80c1",
                    "name": "Gardena Zentrale",
                    "description": "Gateway device",
                    "category": "gateway",
                    "configuration_synchronized": True,
                    "abilities": [
                        {
                            "id": "f9667bc2-b5e2-11e5-b6a5-32212aec0665",
                            "name": "device_info",
                            "type": "device_info",
                            "properties": [
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000000",
                                    "name": "manufacturer",
                                    "value": "Seluxit",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000001",
                                    "name": "product",
                                    "value": "1-GATEWAY",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000002",
                                    "name": "serial_number",
                                    "value": "N/A",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000003",
                                    "name": "sgtin",
                                    "value": "N/A",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000004",
                                    "name": "version",
                                    "value": "1.2.1",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000005",
                                    "name": "category",
                                    "value": "gateway",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "f9667bc2-b5e2-11e5-b6a5-100000000006",
                                    "name": "last_time_online",
                                    "value": "N/A",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                            ],
                        },
                        {
                            "id": "b74cbb14-b5e4-11e5-86c5-32212aec0665",
                            "name": "gateway",
                            "type": "gateway",
                            "properties": [
                                {
                                    "id": "b74cbb14-b5e4-11e5-86c5-100000000000",
                                    "name": "ip_address",
                                    "value": "192.168.1.217",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "b74cbb14-b5e4-11e5-86c5-100000000001",
                                    "name": "time_zone",
                                    "value": " Europe/Vienna (CEST, +0200)",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                            ],
                        },
                    ],
                    "scheduled_events": [],
                    "status_report_history": [],
                    "constraints": [],
                },
                {
                    "id": "e3c1b615-7351-25fc-a551-1908254a2b3e",
                    "name": "Rosi",
                    "category": "mower",
                    "configuration_synchronized": True,
                    "abilities": [
                        {
                            "id": "8df62358-071c-42e0-b7e2-47ba5bce8e79",
                            "name": "device_info",
                            "type": "device_info",
                            "properties": [
                                {
                                    "id": "7b2af5e2-cd45-4e59-b131-4585cbf7e58a",
                                    "name": "manufacturer",
                                    "value": "Gardena",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "4acce2d8-e395-4ea3-9f6e-fc606fefae31",
                                    "name": "product",
                                    "value": "3-DEVICE",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "83df149b-3509-446a-9f8c-4d1dc71b8a7a",
                                    "name": "serial_number",
                                    "value": "00008438",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "307de2bd-fef1-43d8-b77a-e590a059a5c4",
                                    "name": "version",
                                    "value": "3-2.4.7-1.2.0-4380-MODIFIED-ICD1.16_1.2.0",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "1900a86b-661c-47d2-9f42-f66585f8da82",
                                    "name": "category",
                                    "value": "mower",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "c5693fc4-0cb2-4997-ba51-b32732cd41d0",
                                    "name": "last_time_online",
                                    "value": "2016-07-21T13:28:48Z",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "e1e2e3c2-a424-415a-85bd-212a7ab49fd0",
                                    "name": "sgtin",
                                    "value": "3034F8EE90060080000020F6",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                            ],
                        },
                        {
                            "id": "c9147b85-c3eb-41e7-863c-bb24694e586a",
                            "name": "battery",
                            "type": "battery_power",
                            "properties": [
                                {
                                    "id": "c6f3ad1f-ced9-49f1-8710-268b74b007a8",
                                    "name": "level",
                                    "value": 100,
                                    "timestamp": "2016-07-21T13:28:16Z",
                                    "unit": "%",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "78286acb-3ed1-48c3-bd92-2cacc348f5c1",
                                    "name": "rechargable_battery_status",
                                    "value": "ok",
                                    "timestamp": "2016-07-21T13:28:16Z",
                                    "writeable": False,
                                    "supported_values": ["weak", "ok", "undefined"],
                                },
                                {
                                    "id": "c168f578-a1c6-408a-a132-7124b92ffba5",
                                    "name": "charging",
                                    "value": False,
                                    "timestamp": "2016-07-21T13:28:16Z",
                                    "writeable": False,
                                    "supported_values": ["True", "False"],
                                },
                            ],
                        },
                        {
                            "id": "c924fe09-5a62-4334-a3c2-6c6e8348707c",
                            "name": "radio",
                            "type": "radio_link",
                            "properties": [
                                {
                                    "id": "24bfae0d-a42c-40b3-b19f-a8a704502bbe",
                                    "name": "quality",
                                    "value": 50,
                                    "timestamp": "2016-07-21T13:28:48Z",
                                    "unit": "%",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "a5bc1236-0a55-4cf0-90a4-bbe6cf4aef0d",
                                    "name": "connection_status",
                                    "value": "status_device_unreachable",
                                    "timestamp": "2016-07-21T16:07:13.013366Z",
                                    "writeable": False,
                                    "supported_values": [
                                        "unknown",
                                        "status_device_unreachable",
                                        "status_device_alive",
                                    ],
                                },
                                {
                                    "id": "fec78e5e-6b5a-4e56-b3a2-3b08322878bd",
                                    "name": "state",
                                    "value": "good",
                                    "timestamp": "2016-07-21T13:28:48Z",
                                    "writeable": False,
                                    "supported_values": [
                                        "poor",
                                        "good",
                                        "excellent",
                                        "undefined",
                                    ],
                                },
                            ],
                        },
                        {
                            "id": "1d6a1a0a-aa13-4057-892d-59522d5a719c",
                            "name": "mower",
                            "type": "robotic_mower",
                            "properties": [
                                {
                                    "id": "ecd040e6-f5d4-4517-a2dd-1948616caf3d",
                                    "name": "manual_operation",
                                    "value": False,
                                    "timestamp": "2016-07-21T13:28:14Z",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "c1c48c80-589a-4b2e-a73d-0485f4d2a22f",
                                    "name": "status",
                                    "value": "off_disabled",
                                    "timestamp": "2016-07-21T13:28:17Z",
                                    "writeable": False,
                                    "supported_values": [
                                        "paused",
                                        "ok_cutting",
                                        "ok_searching",
                                        "ok_charging",
                                        "ok_leaving",
                                        "wait_updating",
                                        "wait_power_up",
                                        "parked_timer",
                                        "parked_park_selected",
                                        "off_disabled",
                                        "off_hatch_open",
                                        "unknown",
                                        "error",
                                        "error_at_power_up",
                                        "off_hatch_closed",
                                        "ok_cutting_timer_overridden",
                                        "parked_autotimer",
                                        "parked_daily_limit_reached",
                                        "undefined",
                                    ],
                                },
                                {
                                    "id": "594b6456-57a4-47e4-8736-0a392c87856b",
                                    "name": "source_for_next_start",
                                    "value": "week_timer",
                                    "timestamp": "2016-07-21T13:28:16Z",
                                    "writeable": False,
                                    "supported_values": [
                                        "no_source",
                                        "completed_cutting_daily_limit",
                                        "week_timer",
                                        "countdown_timer",
                                        "mower_charging",
                                        "completed_cutting_autotimer",
                                        "undefined",
                                    ],
                                },
                                {
                                    "id": "dbace91b-b24c-499d-ac69-0fd088af47db",
                                    "name": "timestamp_next_start",
                                    "value": "2016-07-22T08:00:00.000000001Z",
                                    "timestamp": "2016-07-21T13:28:16Z",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                                {
                                    "id": "0e12f167-afb7-4303-914b-e14dfb364026",
                                    "name": "override_end_time",
                                    "value": "1970-01-01T00:00:00.000000001Z",
                                    "timestamp": "2016-07-21T13:28:14Z",
                                    "writeable": False,
                                    "supported_values": [],
                                },
                            ],
                        },
                        {
                            "id": "db40b97e-6ded-43ac-ba53-211acc504404",
                            "name": "internal_temperature",
                            "type": "internal_temperature_sensor",
                            "properties": [
                                {
                                    "id": "ba006658-9762-49c7-ba80-fee5a51600a2",
                                    "name": "temperature",
                                    "value": 32,
                                    "timestamp": "2016-07-21T13:28:48Z",
                                    "unit": "C",
                                    "writeable": False,
                                    "supported_values": [],
                                }
                            ],
                        },
                    ],
                    "scheduled_events": [
                        {
                            "type": "active",
                            "start_at": "08:00",
                            "end_at": "13:00",
                            "weekday": "monday",
                            "recurrence": {"type": "weekly", "weekdays": ["monday"]},
                            "id": "6bb76641-b091-4f9f-9113-0070adbd88db",
                        },
                        {
                            "type": "active",
                            "start_at": "08:00",
                            "end_at": "13:00",
                            "weekday": "wednesday",
                            "recurrence": {"type": "weekly", "weekdays": ["wednesday"]},
                            "id": "96bbfb82-9e7c-4f19-a23f-e109a8cb63e7",
                        },
                        {
                            "type": "active",
                            "start_at": "08:00",
                            "end_at": "13:00",
                            "weekday": "thursday",
                            "recurrence": {"type": "weekly", "weekdays": ["thursday"]},
                            "id": "a891ee16-0454-4a2b-81a0-47ad6b252f2f",
                        },
                        {
                            "type": "active",
                            "start_at": "08:00",
                            "end_at": "13:00",
                            "weekday": "friday",
                            "recurrence": {"type": "weekly", "weekdays": ["friday"]},
                            "id": "c442a34e-263a-431c-8acd-7c5feae0e8b9",
                        },
                        {
                            "type": "active",
                            "start_at": "08:00",
                            "end_at": "13:00",
                            "weekday": "tuesday",
                            "recurrence": {"type": "weekly", "weekdays": ["tuesday"]},
                            "id": "658314ef-6e8b-47f3-8181-5f93a3da3ab2",
                        },
                    ],
                    "status_report_history": [
                        {
                            "level": "warning",
                            "timestamp": "2016-07-21T16:07:13.013366Z",
                            "source": "gateway",
                            "message": "STATUS_DEVICE_UNREACHABLE",
                            "raw_message": "STATUS_DEVICE_UNREACHABLE",
                        },
                        {
                            "level": "info",
                            "timestamp": "2016-07-21T07:30:26.680042Z",
                            "source": "gateway",
                            "message": "STATUS_DEVICE_ALIVE",
                            "raw_message": "STATUS_DEVICE_ALIVE",
                        },
                    ],
                    "constraints": [
                        {
                            "resource_name": "scheduled_events",
                            "values": [
                                {"name": "events_week_max", "value": 14, "unit": ""},
                                {"name": "events_day_max", "value": 2, "unit": ""},
                                {
                                    "name": "recurrence_weekdays_max",
                                    "value": 1,
                                    "unit": "",
                                },
                            ],
                        }
                    ],
                },
            ]
        },
        status_code=200,
    )
    smart_system.request_session.mount("https://smart.gardena.com/", adapter)


def init_failed_mock(smart_system):
    adapter = requests_mock.Adapter()
    adapter.register_uri(
        "POST", "https://smart.gardena.com/sg-1/sessions", json={}, status_code=400
    )
    adapter.register_uri(
        "GET", "https://smart.gardena.com/sg-1/locations", json={}, status_code=400
    )
    adapter.register_uri(
        "GET", "https://smart.gardena.com/sg-1/devices", json={}, status_code=400
    )
    smart_system.request_session.mount("https://smart.gardena.com/", adapter)


class SmartSystemTestCase(unittest.TestCase):
    def test_init(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        assert smart_system.email == "test@test.com"
        assert smart_system.password == "password"

    def test_init_exception_without_email(self):
        with pytest.raises(ValueError):
            SmartSystem(password="password")

    def test_init_exception_without_password(self):
        with pytest.raises(ValueError):
            SmartSystem(email="test@test.com")

    def test_authenticate(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        smart_system.authenticate()
        assert smart_system.token == "7867e26c-05eb-4a60-bf30-7c3a1b4480aa"
        assert smart_system.user_id == "196ab891-a521-872c-ab1d-1685d1e77afc"

    def test_authenticate_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_failed_mock(smart_system)
        with pytest.raises(HTTPError):
            smart_system.authenticate()

    def test_get_locations(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        assert len(smart_system.locations) == 1

    def test_get_locations_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_failed_mock(smart_system)
        with pytest.raises(HTTPError):
            smart_system.authenticate()
        with pytest.raises(HTTPError):
            smart_system.update_locations()

    def test_get_devices(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_devices()
        assert len(smart_system.devices) == 2

    def test_get_devices_failed(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_failed_mock(smart_system)
        with pytest.raises(HTTPError):
            smart_system.authenticate()
        with pytest.raises(HTTPError):
            smart_system.update_devices()

    def test_get_session(self):
        smart_system = SmartSystem(email="test@test.com", password="password")
        init_mock(smart_system)
        assert isinstance(smart_system.get_session(), requests.sessions.Session)
