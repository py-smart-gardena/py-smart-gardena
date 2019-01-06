from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class FirmwareAbility(BaseGardenaDeviceClass):

    firmware_status = None
    firmware_upload_progress = 0
    firmware_update_start = False

    def __init__(self, smart_system=None, location=None):
        super(FirmwareAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(
            {
                "firmware": {
                    "firmware_status": "firmware_status",
                    "firmware_upload_progress": "firmware_upload_progress",
                    "firmware_update_start": "firmware_update_start",
                }
            }
        )
