import pytest
import unittest
from gardena.smart_system import SmartSystem

location_message = '{"id":"753aecac-4c46-440e-aa96-d92436a11e77","type":"LOCATION","relationships":{"devices":{"data":[{"id":"28c26146-94c1-42d7-986a-89f5237550ce","type":"DEVICE"},{"id":"78594cad-b26e-4abf-b5c6-62c1453fc34c","type":"DEVICE"},{"id":"8529a062-4005-4055-b35e-03658ff04662","type":"DEVICE"},{"id":"a130596e-6627-4020-aea5-b6d2f24d0e03","type":"DEVICE"},{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf","type":"DEVICE"}]}},"attributes":{"name":"My Garden"}}'

"""{'attributes': {'name': 'My Garden'},
 'id': '753aecac-4c46-440e-aa96-d92436a11e77',
 'relationships': {'devices': {'data': [{'id': '28c26146-94c1-42d7-986a-89f5237550ce',
                                         'type': 'DEVICE'},
                                        {'id': '78594cad-b26e-4abf-b5c6-62c1453fc34c',
                                         'type': 'DEVICE'},
                                        {'id': '8529a062-4005-4055-b35e-03658ff04662',
                                         'type': 'DEVICE'},
                                        {'id': 'a130596e-6627-4020-aea5-b6d2f24d0e03',
                                         'type': 'DEVICE'},
                                        {'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf',
                                         'type': 'DEVICE'}]}},
 'type': 'LOCATION'}"""

device_message = '{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf","type":"DEVICE","relationships":{"location":{"data":{"id":"753aecac-4c46-440e-aa96-d92436a11e77","type":"LOCATION"}},"services":{"data":[{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf:wc","type":"VALVE_SET"},{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf","type":"VALVE"},{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf","type":"COMMON"}]}}}'

"""{'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf',
 'relationships': {'location': {'data': {'id': '753aecac-4c46-440e-aa96-d92436a11e77',
                                         'type': 'LOCATION'}},
                   'services': {'data': [{'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf:wc',
                                          'type': 'VALVE_SET'},
                                         {'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf',
                                          'type': 'VALVE'},
                                         {'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf',
                                          'type': 'COMMON'}]}},
 'type': 'DEVICE'}"""


service_message = """{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf","type":"COMMON","relationships":{"device":{"data":{"id":"d6259669-8471-488c-a88e-bcf3a07a58bf","type":"DEVICE"}}},"attributes":{"name":{"value":"Water Control"},"batteryLevel":{"value":87,"timestamp":"2019-02-04T08:34:36.658+0000"},"batteryState":{"value":"OK","timestamp":"2019-02-04T08:34:36.546+0000"},"rfLinkLevel":{"value":70,"timestamp":"2019-02-04T08:34:36.728+0000"},"serial":{"value":"00019796"},"modelType":{"value":"GARDENA smart Water Control"},"rfLinkState":{"value":"OFFLINE"}}}"""

"""{'attributes': {'batteryLevel': {'timestamp': '2019-02-04T08:34:36.658+0000',
                                 'value': 87},
                'batteryState': {'timestamp': '2019-02-04T08:34:36.546+0000',
                                 'value': 'OK'},
                'modelType': {'value': 'GARDENA smart Water Control'},
                'name': {'value': 'Water Control'},
                'rfLinkLevel': {'timestamp': '2019-02-04T08:34:36.728+0000',
                                'value': 70},
                'rfLinkState': {'value': 'OFFLINE'},
                'serial': {'value': '00019796'}},
 'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf',
 'relationships': {'device': {'data': {'id': 'd6259669-8471-488c-a88e-bcf3a07a58bf',
                                       'type': 'DEVICE'}}},
 'type': 'COMMON'}"""


class SmartSystemTest(unittest.TestCase):
    def setup_method(self, method):
        self.sm = SmartSystem(email="login", password="password", client_id="client_id")

    def test_smart_system(self):
        self.sm.on_message(location_message)
        assert len(self.sm.locations) == 1

    def test_location(self):
        self.sm.on_message(location_message)
        self.sm.on_message(device_message)

        location = self.sm.locations["753aecac-4c46-440e-aa96-d92436a11e77"]
        assert location.data["id"] == "753aecac-4c46-440e-aa96-d92436a11e77"
        assert location.data["name"] == "My Garden"
        assert len(location.devices) == 1

    def test_device(self):
        self.sm.on_message(location_message)
        self.sm.on_message(device_message)
        self.sm.on_message(service_message)

        device = self.sm.locations["753aecac-4c46-440e-aa96-d92436a11e77"].devices[
            "d6259669-8471-488c-a88e-bcf3a07a58bf"
        ]
        assert device.data["id"] == "d6259669-8471-488c-a88e-bcf3a07a58bf"
        assert len(device.services) == 1

    def test_service(self):
        self.sm.on_message(location_message)
        self.sm.on_message(device_message)
        self.sm.on_message(service_message)

        service = (
            self.sm.locations["753aecac-4c46-440e-aa96-d92436a11e77"]
            .devices["d6259669-8471-488c-a88e-bcf3a07a58bf"]
            .services["COMMON"]["d6259669-8471-488c-a88e-bcf3a07a58bf"]
        )
        assert service.data["batteryLevel"] == 87
        assert service.data["batteryState"] == "OK"
        assert service.data["modelType"] == "GARDENA smart Water Control"
        assert service.data["name"] == "Water Control"
        assert service.data["rfLinkLevel"] == 70
        assert service.data["rfLinkState"] == "OFFLINE"
        assert service.data["serial"] == "00019796"
