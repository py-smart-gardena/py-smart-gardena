import asyncio
import logging
import os
import sys
import traceback

from gardena.smart_system import SmartSystem
import pprint


async def main():
    smart_system = SmartSystem(
        client_id=os.environ.get("GARDENA_CLIENT_ID"),
        client_secret=os.environ.get("GARDENA_CLIENT_SECRET"),
        level=logging.DEBUG,
    )
    try:
        print(
            f"Connecting with client_id/client_secret : {os.environ.get('GARDENA_CLIENT_ID')}/{os.environ.get('GARDENA_CLIENT_SECRET')}"
        )
        await smart_system.authenticate()
        await smart_system.update_locations()
        for location in smart_system.locations.values():
            await smart_system.update_devices(location)
            pprint.pprint(location)
            for device in location.devices.values():
                pprint.pprint(device)
                device.add_callback(
                    lambda device: print(f"on a recu un device {device}")
                )
        print(f"------------{next(iter(smart_system.locations))}")
        asyncio.create_task(
            smart_system.start_ws(
                smart_system.locations.get(next(iter(smart_system.locations)))
            )
        )
        while True:
            await asyncio.sleep(5)
    except BaseException as e:
        print("-" * 60)
        print(e)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)
    finally:
        await smart_system.quit()


asyncio.run(main())
