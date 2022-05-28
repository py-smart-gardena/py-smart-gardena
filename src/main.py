import os

from gardena.smart_system import SmartSystem
import pprint

smart_system = SmartSystem(email=os.environ.get('GARDENA_EMAIL'), password=os.environ.get('GARDENA_PASSWORD'), client_id=os.environ.get('GARDENA_CLIENT_ID'))
smart_system.authenticate()
smart_system.update_locations()
for location in smart_system.locations.values():
    smart_system.update_devices(location)
    pprint.pprint(location)
    for device in location.devices.values():
        pprint.pprint(device)

smart_system.start_ws(smart_system.locations['LOCATION_ID'])
