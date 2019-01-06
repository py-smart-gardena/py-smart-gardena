from tests.mocks.gardena_api_mock import GardenaApiMock


class BaseDeviceTestClass:
    def create_mock(self, smart_system):
        api_mock = GardenaApiMock()
        api_mock.register_sessions()
        api_mock.register_locations()
        api_mock.register_devices()
        api_mock.mount(smart_system)
        return api_mock
