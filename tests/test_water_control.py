import pytest
import unittest
from gardena.water_control import WaterControl
from tests.base_test_device import BaseTestDevice


class WaterControlTestCase(unittest.TestCase, BaseTestDevice):

    water_control_test_info = {
        "id": "d6259669-3241-488c-a88e-bcf3a07a58bf",
        "name": "Water Control",
        "category": "watering_computer",
        "configuration_synchronized": False,
        "abilities": [
            {
                "id": "43126f82-d6eb-3e5f-9213-dec302f8ffe1",
                "name": "device_info",
                "properties": [
                    {
                        "id": "47310b2d-6fd6-39b7-8523-a2b7da1d74ce",
                        "name": "manufacturer",
                        "value": "Gardena",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "d1ea4945-af97-3bd6-8104-7c68f62e5c13",
                        "name": "product",
                        "value": "1-DEVICE",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "49c80029-bc7c-3bfa-8e81-985e7692596f",
                        "name": "serial_number",
                        "value": "12345678",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "37508766-c341-345b-afac-19b09dc91f8e",
                        "name": "version",
                        "value": "0.3.5-2.5.2-1.2.5-ICD1.17_1.0.20",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "f640069c-9c51-37b8-ab57-509a1036210d",
                        "name": "category",
                        "value": "watering_computer",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "e51218c9-0701-3a0d-9429-9be9f3218de2",
                        "name": "last_time_online",
                        "value": "2019-01-03T23:25:56.050Z",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "262c8bec-3094-3aa5-abf5-771b883e1936",
                        "name": "sgtin",
                        "value": "3034F8EE90126D4000004D54",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "23d5d42d-7b00-3a7e-9bb2-bec9a1c90190",
                        "name": "connection_status",
                        "value": "online",
                        "writeable": False,
                        "supported_values": [],
                    },
                ],
                "type": "device_info",
            },
            {
                "id": "b6cf692a-f58d-3eb1-b4dc-d397d4cd98ef",
                "name": "battery",
                "properties": [
                    {
                        "id": "795285f8-7a81-38f7-9c45-7f54088580e1",
                        "name": "level",
                        "timestamp": "2019-01-03T23:25:56.085Z",
                        "unit": "%",
                        "value": 97,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "c3e84d63-c8e1-3735-8e59-a04c55b7e6ce",
                        "name": "disposable_battery_status",
                        "timestamp": "2019-01-03T23:25:56.050Z",
                        "value": "ok",
                        "writeable": False,
                        "supported_values": [
                            "out_of_operation",
                            "replace_now",
                            "low",
                            "ok",
                            "undefined",
                        ],
                    },
                ],
                "type": "battery_power",
            },
            {
                "id": "ece39d87-c0cd-30d5-8321-4999dab007f0",
                "name": "radio",
                "properties": [
                    {
                        "id": "84e90e01-f893-3b18-af9d-83d33b2beeca",
                        "name": "quality",
                        "timestamp": "2019-01-03T23:25:56.108Z",
                        "unit": "%",
                        "value": 100,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "397b71cf-243d-3fff-ad26-24fac8e912d3",
                        "name": "connection_status",
                        "timestamp": "2019-01-04T00:19:13.892Z",
                        "value": "unknown",
                        "writeable": False,
                        "supported_values": [
                            "unknown",
                            "status_device_unreachable",
                            "status_device_alive",
                        ],
                    },
                    {
                        "id": "33aee19d-3014-3f48-9a85-8f6eb7a1d495",
                        "name": "state",
                        "timestamp": "2019-01-03T23:25:56.140Z",
                        "value": "good",
                        "writeable": False,
                        "supported_values": ["bad", "poor", "good", "undefined"],
                    },
                ],
                "type": "radio_link",
            },
            {
                "id": "9b2c5f65-5d6e-3ec4-8bef-a899ae48d18c",
                "name": "outlet",
                "properties": [
                    {
                        "id": "decc061d-21de-3764-b4aa-9567c35a0747",
                        "name": "valve_open",
                        "timestamp": "2019-01-03T20:25:30.588Z",
                        "value": False,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "cb92ff5d-136d-333c-8612-d66cc03f7c2b",
                        "name": "manual_override",
                        "timestamp": "2019-01-03T20:25:30.603Z",
                        "value": "inactive",
                        "writeable": True,
                        "supported_values": ["inactive", "open", "undefined"],
                    },
                    {
                        "id": "4b213b6b-03fb-395a-bfe9-511e01b10cad",
                        "name": "button_manual_override_time",
                        "timestamp": "2019-01-03T20:25:30.632Z",
                        "unit": "minutes",
                        "value": 30,
                        "writeable": True,
                        "supported_values": [],
                    },
                    {
                        "id": "82d195db-1bd8-30aa-ab7c-e5c68db453ed",
                        "name": "last_manual_override_time",
                        "timestamp": "2019-01-03T20:25:30.617Z",
                        "unit": "minutes",
                        "value": 30,
                        "writeable": False,
                        "supported_values": [],
                    },
                ],
                "type": "watering_outlet",
            },
            {
                "id": "023e07e4-5a67-3a4f-be11-80093e3690a8",
                "name": "ambient_temperature",
                "properties": [
                    {
                        "id": "a99fff90-8f75-38c3-a6ac-7608373c8ba4",
                        "name": "temperature",
                        "timestamp": "2019-01-03T23:25:56.167Z",
                        "unit": "C",
                        "value": 22,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "bf080d5d-2f4f-3fe4-ba3e-ebbd87af0bf1",
                        "name": "frost_warning",
                        "timestamp": "2019-01-03T23:25:56.193Z",
                        "value": "no_frost",
                        "writeable": False,
                        "supported_values": ["no_frost", "frost", "undefined"],
                    },
                ],
                "type": "ambient_temperature_sensor",
            },
            {
                "id": "1a8f5816-afc8-30b5-8e00-f18fc72d1d12",
                "name": "identification",
                "properties": [],
                "type": "identification",
            },
            {
                "id": "1869491d-ddcf-3076-b508-fe1b9bc5ddc2",
                "name": "scheduling",
                "properties": [
                    {
                        "id": "5e387793-c43d-363e-83dd-64ba1cec2dfa",
                        "name": "scheduled_watering_next_start",
                        "timestamp": "2019-01-04T00:19:13.892Z",
                        "value": None,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "6a286ada-24cb-36ee-8ce0-11f2be397202",
                        "name": "scheduled_watering_end",
                        "timestamp": "2019-01-04T00:19:13.892Z",
                        "value": None,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "5fd7e3cc-dbeb-3e33-a2fe-01f1fa3caf6e",
                        "name": "adaptive_scheduling_last_decision",
                        "timestamp": "2019-01-04T00:19:13.892Z",
                        "value": "undefined",
                        "writeable": False,
                        "supported_values": [
                            "undefined",
                            "watered_sensor_timeout",
                            "skipped",
                            "watered",
                        ],
                    },
                ],
                "type": "scheduling",
            },
            {
                "id": "177ce23e-adb6-3bca-af1f-b0f66891c8fb",
                "name": "firmware",
                "properties": [
                    {
                        "id": "f71b4480-7501-3ed1-b50f-51559a888ce6",
                        "name": "firmware_status",
                        "value": "up_to_date",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "d294efe8-deaf-39fb-85dd-2ad627ed6f2f",
                        "name": "firmware_upload_progress",
                        "value": 0,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "eea94260-8ca9-3cfb-bbda-70ef5c6e10bf",
                        "name": "firmware_available_version",
                        "value": "",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "e9e4ca8e-ed98-37dc-bba3-bb59db7b239d",
                        "name": "inclusion_status",
                        "value": "included",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "722180d1-2dc6-3c3f-a400-b3e0b6b15999",
                        "name": "firmware_update_start",
                        "value": True,
                        "writeable": True,
                        "supported_values": [],
                    },
                    {
                        "id": "df3b6d30-00f5-3520-aab7-cb4b528861e8",
                        "name": "firmware_command",
                        "value": "idle",
                        "writeable": True,
                        "supported_values": [
                            "idle",
                            "firmware_cancel",
                            "firmware_flash",
                            "firmware_upload",
                            "unsupported",
                        ],
                    },
                ],
                "type": "firmware",
            },
        ],
        "configuration_synchronized_v2": {
            "value": False,
            "timestamp": "2019-01-03T20:25:59.172Z",
        },
        "configuration_update": {
            "status": "failed",
            "timestamp": "2019-01-03T20:25:59.172Z",
        },
        "constraints": [
            {
                "resource_name": "scheduled_events",
                "values": [
                    {"name": "is_supported", "unit": "", "value": True},
                    {"name": "events_week_max", "unit": "", "value": 18},
                    {"name": "duration_max", "unit": "minutes", "value": 600},
                    {"name": "is_pausable", "unit": "", "value": True},
                ],
            },
            {
                "resource_name": "scheduling_wizard_watering",
                "values": [
                    {"name": "is_supported", "unit": "", "value": True},
                    {"name": "is_suntimings_supported", "unit": "", "value": True},
                ],
            },
        ],
        "device_state": "ok",
        "property_constraints": [
            {
                "name": "outlet",
                "values": [
                    {
                        "name": "manual_override",
                        "values": [
                            {
                                "name": "manual_watering_range",
                                "unit": "minutes",
                                "value": {"min": 0, "max": 59},
                            }
                        ],
                    },
                    {
                        "name": "button_manual_override_time",
                        "values": [
                            {
                                "name": "manual_watering_range",
                                "unit": "minutes",
                                "value": {"min": 0, "max": 59},
                            }
                        ],
                    },
                ],
            }
        ],
        "scheduled_events": [],
        "scheduling_wizard_mowing": None,
        "settings": [
            {
                "name": "schedules_paused_until",
                "id": "903bc550-e6fc-4ced-8d6b-c60f2ab5cc88",
                "value": "",
            }
        ],
        "status_report_history": [
            {
                "level": "important",
                "message": "ok",
                "raw_message": "code ID: 0",
                "source": "device",
                "timestamp": "2019-01-03T23:25:55.846Z",
            },
            {
                "level": "important",
                "message": "ok",
                "raw_message": "code ID: 0",
                "source": "device",
                "timestamp": "2019-01-03T22:25:54.604Z",
            },
            {
                "level": "important",
                "message": "ok",
                "raw_message": "code ID: 0",
                "source": "device",
                "timestamp": "2019-01-03T21:25:53.840Z",
            },
        ],
        "zones": [],
    }

    def test_init(self):
        water_control = WaterControl(smart_system=self.smart_system_test_info)
        assert water_control.smart_system == self.smart_system_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            WaterControl()

    def test_water_control_information(self):
        water_control = WaterControl(smart_system=self.smart_system_test_info)
        water_control.update_information(information=self.water_control_test_info)
        assert water_control.id == self.water_control_test_info["id"]
        assert water_control.name == self.water_control_test_info["name"]
        # XXX : no description for water_control ?
        # assert water_control.description == self.water_control_test_info["description"]
        assert water_control.category == self.water_control_test_info["category"]
        assert (
            water_control.is_configuration_synchronized
            == self.water_control_test_info["configuration_synchronized"]
        )
        assert water_control.serial_number == "12345678"
        assert water_control.version == "0.3.5-2.5.2-1.2.5-ICD1.17_1.0.20"
        assert water_control.last_time_online == "2019-01-03T23:25:56.050Z"
        assert water_control.device_state == "ok"
        assert water_control.battery_level == 97
        assert water_control.battery_status == "ok"
        assert water_control.radio_quality == 100
        assert water_control.radio_connection_status == "unknown"
        assert water_control.radio_state == "good"
        assert water_control.ambient_temperature == 22
        assert water_control.frost_warning == "no_frost"
        assert water_control.firmware_status == "up_to_date"
        assert not water_control.watering_valve_open
        assert water_control.watering_manual_override == "inactive"
