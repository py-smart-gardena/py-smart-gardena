from dependency_injector import containers, providers
from dependency_injector.providers import Configuration
from gardena.infrastructure.api.gardena.gardena_api_client import GardenaApiClient
from gardena.infrastructure.api.gardena.gardena_devices_persistence import (
    GardenaDevicesPersistence,
)
from gardena.infrastructure.api.gardena.gardena_location_persistence import (
    GardenaLocationsPersistence,
)
from gardena.infrastructure.api.gardena.gardena_mower_persistence import (
    GardenaMowersPersistence,
)
from gardena.use_cases.list_devices import ListDevice
from gardena.use_cases.list_locations import ListLocations
from gardena.use_cases.persistence.devices_persistence import DevicesPersistence
from gardena.use_cases.persistence.locations_persistence import LocationsPersistence
from gardena.use_cases.persistence.mowers_persistence import MowersPersistence
from gardena.use_cases.start_mowing import StartMowing
from gardena.use_cases.start_schedule import StartSchedule
from gardena.use_cases.stop_mowing import StopMowing
from gardena.use_cases.stop_schedule import StopSchedule


class Container(containers.DeclarativeContainer):
    config: Configuration = providers.Configuration()

    # logging = providers.Resource(
    #     logging.config.fileConfig,
    #     fname="logging.ini",
    # )

    # Persistence
    gardena_api: GardenaApiClient = providers.Singleton(
        GardenaApiClient,
        email=config.email,
        password=config.password,
        client_id=config.client_id,
    )

    location_persistence: LocationsPersistence = providers.Factory(
        GardenaLocationsPersistence, gardena_api
    )

    devices_persistence: DevicesPersistence = providers.Factory(
        GardenaDevicesPersistence, gardena_api
    )

    mowers_persistence: MowersPersistence = providers.Factory(
        GardenaMowersPersistence, gardena_api
    )

    # Use cases
    list_locations: ListLocations = providers.Factory(
        ListLocations, location_persistence=location_persistence
    )
    list_devices: ListDevice = providers.Factory(
        ListDevice, devices_persistence=devices_persistence
    )
    start_mowing = providers.Factory(StartMowing, mowers_persistence=mowers_persistence)
    stop_mowing = providers.Factory(StopMowing, mowers_persistence=mowers_persistence)
    start_schedule = providers.Factory(
        StartSchedule, mowers_persistence=mowers_persistence
    )
    stop_schedule = providers.Factory(
        StopSchedule, mowers_persistence=mowers_persistence
    )
