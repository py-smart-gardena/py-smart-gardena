import pprint
import traceback

import sys

from dependency_injector.wiring import Provide, inject
from gardena.application.container import Container
from gardena.infrastructure.api.gardena.gardena_api_client import GardenaApiClient
from gardena.use_cases.list_devices import ListDevice
from gardena.use_cases.list_locations import ListLocations


@inject
def main(
        list_locations: ListLocations = Provide[Container.list_locations],
        list_devices: ListDevice = Provide[Container.list_devices],
        start_mowing = Provide[Container.start_mowing],
        gardena_api: GardenaApiClient = Provide[Container.gardena_api],
) -> None:
    try:
        locations = list_locations.execute()
        pprint.pprint(locations[0].__dict__)
        devices = list_devices.execute(locations[0])
        pprint.pprint(devices.mowers[0].__dict__)
        start_mowing.execute(devices.mowers[0], 3600)
        pprint.pprint(devices.power_sockets[0].__dict__)
        pprint.pprint(devices.sensors[0].__dict__)
        pprint.pprint(devices.smart_irrigation_controls[0].__dict__)
    except Exception:
        traceback.print_exc()

    gardena_api.disconnect()


if __name__ == "__main__":
    container: Container = Container()
    container.config.email.from_env("GARDENA_EMAIL")
    container.config.password.from_env("GARDENA_PASSWORD")
    container.config.client_id.from_env("GARDENA_CLIENT_ID")
    container.init_resources()
    container.wire(modules=[__name__])

    main(*sys.argv[1:])
