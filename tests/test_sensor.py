import pytest
import unittest
from gardena.sensor import Sensor
from tests.base_test_device import BaseTestDevice


class SensorTestCase(unittest.TestCase, BaseTestDevice):

    sensor_test_info = {
        "id": "a130596e-6627-4030-aea5-b6d2f24d0e03",
        "name": "Sensor",
        "category": "sensor",
        "configuration_synchronized": False,
        "abilities": [
            {
                "id": "8d416f3e-ba1f-36b9-a834-ff1c0ec12303",
                "name": "device_info",
                "properties": [
                    {
                        "id": "0f533890-24a4-3e4f-b081-6daa44661755",
                        "name": "manufacturer",
                        "value": "Gardena",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "8678bf08-c361-3889-b625-12db90685c53",
                        "name": "product",
                        "value": "2-DEVICE",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "bc40765a-fc7a-3db9-a282-ddad079b5f3a",
                        "name": "serial_number",
                        "value": "12345678",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "6617fc68-2a31-3b29-b4a3-69c2a45b7516",
                        "name": "version",
                        "value": "1.0.3-2.5.2-1.2.5-ICD1.17_1.0.18",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "37f464b1-9266-3b42-a287-23bc7093e3e8",
                        "name": "category",
                        "value": "sensor",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "bb3ee73a-ad9b-31da-a5e8-2bb9f71ab12e",
                        "name": "last_time_online",
                        "value": "2019-01-03T23:57:34.549Z",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "3e3624ea-57d0-356f-be5f-bbfc18ceb002",
                        "name": "sgtin",
                        "value": "3034F8EE9012674000006F2E",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "285fbc74-18eb-3658-aeb5-f7575c254945",
                        "name": "connection_status",
                        "value": "online",
                        "writeable": False,
                        "supported_values": [],
                    },
                ],
                "type": "device_info",
            },
            {
                "id": "dd950bf3-6ca1-38e9-b34a-d99c5ff3ac05",
                "name": "battery",
                "properties": [
                    {
                        "id": "337274a1-deab-3f86-9a07-b206071c5a14",
                        "name": "level",
                        "timestamp": "2019-01-03T20:52:55.847Z",
                        "unit": "%",
                        "value": 97,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "2df67171-bf65-3798-92b0-b9f1ae782f6c",
                        "name": "disposable_battery_status",
                        "timestamp": "2019-01-03T19:37:43.753Z",
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
                "id": "16ffe9d2-2a45-3a36-85b6-57db7cbe304b",
                "name": "radio",
                "properties": [
                    {
                        "id": "6406f3cd-2359-3125-93bc-45bcdcca5b61",
                        "name": "quality",
                        "timestamp": "2019-01-03T23:38:09.673Z",
                        "unit": "%",
                        "value": 90,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "c7333be1-86c1-3b81-aaf6-506aa2ccb537",
                        "name": "connection_status",
                        "timestamp": "2019-01-04T00:19:13.888Z",
                        "value": "unknown",
                        "writeable": False,
                        "supported_values": [
                            "unknown",
                            "status_device_unreachable",
                            "status_device_alive",
                        ],
                    },
                    {
                        "id": "ac704b41-21a7-3276-b0fa-e31a07294334",
                        "name": "state",
                        "timestamp": "2019-01-03T23:38:09.700Z",
                        "value": "good",
                        "writeable": False,
                        "supported_values": ["bad", "poor", "good", "undefined"],
                    },
                ],
                "type": "radio_link",
            },
            {
                "id": "afe50b39-235e-364d-a7d6-06247cb1da35",
                "name": "ambient_temperature",
                "properties": [
                    {
                        "id": "63b43cac-f3cc-3b4d-8e8a-9c5461b34139",
                        "name": "temperature",
                        "timestamp": "2019-01-03T23:38:09.603Z",
                        "unit": "C",
                        "value": 22,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "398c00c1-8f05-37db-afc9-30bb9af4cca6",
                        "name": "frost_warning",
                        "timestamp": "2019-01-03T23:38:09.626Z",
                        "value": "no_frost",
                        "writeable": False,
                        "supported_values": ["no_frost", "frost", "undefined"],
                    },
                ],
                "type": "ambient_temperature_sensor",
            },
            {
                "id": "b41772b6-c0eb-3622-80ba-72a037409bd2",
                "name": "soil_temperature",
                "properties": [
                    {
                        "id": "d54a6fb7-6673-3494-bba0-a8f57d8acdd4",
                        "name": "temperature",
                        "timestamp": "2019-01-03T23:56:22.851Z",
                        "unit": "C",
                        "value": 22,
                        "writeable": False,
                        "supported_values": [],
                    }
                ],
                "type": "soil_temperature_sensor",
            },
            {
                "id": "cafe4489-5d79-3ecb-9c93-4b9ad95ca474",
                "name": "humidity",
                "properties": [
                    {
                        "id": "bd5c371d-f134-32d8-b85b-5e14a5ba3ca8",
                        "name": "humidity",
                        "timestamp": "2019-01-03T23:57:34.549Z",
                        "unit": "%",
                        "value": 0,
                        "writeable": False,
                        "supported_values": [],
                    }
                ],
                "type": "soil_humidity_sensor",
            },
            {
                "id": "18001d46-83e2-3681-a2f3-c419d9469212",
                "name": "light",
                "properties": [
                    {
                        "id": "bc71616b-5a28-375c-9cbd-7ef0ba8d0e5b",
                        "name": "light",
                        "timestamp": "2019-01-03T23:38:09.648Z",
                        "unit": "lx",
                        "value": 0,
                        "writeable": False,
                        "supported_values": [],
                    }
                ],
                "type": "light_sensor",
            },
            {
                "id": "ac47ed7b-f888-36dc-97fb-b810d824bb52",
                "name": "identification",
                "properties": [],
                "type": "identification",
            },
            {
                "id": "99021742-fed7-3f19-8386-dd04f8e72073",
                "name": "firmware",
                "properties": [
                    {
                        "id": "b314aaa8-eb32-3403-a82e-c015b2ce9ae1",
                        "name": "firmware_status",
                        "value": "up_to_date",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "1eb44f83-ac63-3fb1-8099-ddf48889a4a1",
                        "name": "firmware_upload_progress",
                        "value": 0,
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "3bb7bf53-185d-3fed-9526-fa10f77da355",
                        "name": "firmware_available_version",
                        "value": "",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "5e37c0ac-a9ff-3366-bd62-98214a2a477f",
                        "name": "inclusion_status",
                        "value": "included",
                        "writeable": False,
                        "supported_values": [],
                    },
                    {
                        "id": "6afbae36-1ff6-3c89-a693-98ddc03e3fa2",
                        "name": "firmware_update_start",
                        "value": True,
                        "writeable": True,
                        "supported_values": [],
                    },
                    {
                        "id": "0b957be4-71e6-39b3-ae1d-21ea7ebe7500",
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
            "timestamp": "2019-01-03T19:37:50.971Z",
        },
        "configuration_update": {
            "status": "failed",
            "timestamp": "2019-01-03T19:37:50.971Z",
        },
        "constraints": [
            {
                "resource_name": "scheduled_events",
                "values": [{"name": "is_supported", "unit": "", "value": False}],
            }
        ],
        "device_state": "ok",
        "property_constraints": [],
        "scheduled_events": [],
        "scheduling_wizard_mowing": None,
        "settings": [],
        "status_report_history": [
            {
                "level": "important",
                "message": "ok",
                "raw_message": "code ID: 0",
                "source": "device",
                "timestamp": "2019-01-03T23:38:09.398Z",
            },
            {
                "level": "important",
                "message": "ok",
                "raw_message": "code ID: 0",
                "source": "device",
                "timestamp": "2019-01-03T22:38:08.560Z",
            },
            {
                "level": "important",
                "message": "ok",
                "raw_message": "code ID: 0",
                "source": "device",
                "timestamp": "2019-01-03T21:38:07.260Z",
            },
        ],
        "zones": [],
    }

    def test_init(self):
        sensor = Sensor(smart_system=self.smart_system_test_info)
        assert sensor.smart_system == self.smart_system_test_info

    def test_init_exception_without_smart_system(self):
        with pytest.raises(ValueError):
            Sensor()

    def test_sensor_information(self):
        sensor = Sensor(smart_system=self.smart_system_test_info)
        sensor.update_information(information=self.sensor_test_info)
        assert sensor.id == self.sensor_test_info["id"]
        assert sensor.name == self.sensor_test_info["name"]
        # XXX : no description for sensor ?
        # assert sensor.description == self.sensor_test_info["description"]
        assert sensor.category == self.sensor_test_info["category"]
        assert (
            sensor.is_configuration_synchronized
            == self.sensor_test_info["configuration_synchronized"]
        )
        assert sensor.serial_number == "12345678"
        assert sensor.version == "1.0.3-2.5.2-1.2.5-ICD1.17_1.0.18"
        assert sensor.last_time_online == "2019-01-03T23:57:34.549Z"
        assert sensor.device_state == "ok"
        assert sensor.battery_level == 97
        assert sensor.battery_status == "ok"
        assert sensor.radio_quality == 90
        assert sensor.radio_connection_status == "unknown"
        assert sensor.radio_state == "good"
        assert sensor.ambient_temperature == 22
        assert sensor.frost_warning == "no_frost"
        assert sensor.sensor_soil_temperature == 22
        assert sensor.sensor_soil_humidity == 0
        assert sensor.sensor_light == 0
        assert sensor.firmware_status == "up_to_date"
