import unittest

from gardena.devices.sensor import Sensor
from tests.gardena_api_return.devices_return import device_sensor_return
from tests.fixtures import SmartSystemFixture, LocationFixture
from tests.devices.base_device_test_class import BaseDeviceTestClass


class SensorTestCase(unittest.TestCase, BaseDeviceTestClass):
    def test_sensor_information(self):
        sensor = Sensor(
            smart_system=SmartSystemFixture.get_smart_system_fixture(),
            location=LocationFixture.get_location_fixture(),
        )
        sensor.update_information(device_sensor_return)
        assert sensor.id == device_sensor_return["id"]
        assert sensor.name == device_sensor_return["name"]
        # XXX : no description for sensor ?
        # assert sensor.description == device_sensor_return["description"]
        assert sensor.category == device_sensor_return["category"]
        assert (
            sensor.is_configuration_synchronized
            == device_sensor_return["configuration_synchronized"]
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
        assert sensor.firmware_upload_progress == 0
        assert sensor.firmware_update_start

    def test_refresh_ambient_temperature(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_device_sensor_ambient_temperature_refresh_command(
            "a130596e-6627-4030-aea5-b6d2f24d0e03",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        sensor = Sensor(smart_system=smart_system, location=location)
        sensor.update_information(device_sensor_return)
        sensor.refresh_ambient_temperature()
        assert m_result.call_count == 1

    def test_refresh_light_intensity(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_device_sensor_light_refresh_command(
            "a130596e-6627-4030-aea5-b6d2f24d0e03",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        sensor = Sensor(smart_system=smart_system, location=location)
        sensor.update_information(device_sensor_return)
        sensor.refresh_light_intensity()
        assert m_result.call_count == 1

    def test_refresh_soil_moisture(self):
        smart_system = SmartSystemFixture.get_smart_system_fixture()
        mock = self.create_mock(smart_system)
        smart_system.authenticate()
        smart_system.update_locations()
        location = smart_system.locations["1c8b301f-22c8-423d-1b4d-ec25315d1377"]
        m_result = mock.register_device_sensor_humidity_refresh_command(
            "a130596e-6627-4030-aea5-b6d2f24d0e03",
            "1c8b301f-22c8-423d-1b4d-ec25315d1377",
        )
        sensor = Sensor(smart_system=smart_system, location=location)
        sensor.update_information(device_sensor_return)
        sensor.refresh_soil_moisture()
        assert m_result.call_count == 1
