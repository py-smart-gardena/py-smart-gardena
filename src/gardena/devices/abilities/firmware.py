from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class FirmwareAbility(BaseGardenaAbilityClass):

    firmware_abilities = {
        "firmware": {
            "firmware_status": "firmware_status",
            "firmware_upload_progress": "firmware_upload_progress",
            "firmware_update_start": "firmware_update_start",
            "firmware_available_version": "firmware_available_version",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(FirmwareAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.firmware_abilities)
        self.firmware_status = None
        self.firmware_upload_progress = 0
        self.firmware_update_start = False
        self.firmware_available_version = None

    def get_all_info(self):
        values = {
            "firmware_status": self.firmware_status,
            "firmware_upload_progress": self.firmware_upload_progress,
            "firmware_update_start": self.firmware_update_start,
            "firmware_available_version": self.firmware_available_version,
        }
        return {**super(FirmwareAbility, self).get_all_info(), **values}

    def firmware_command(self, method):
        self.call_property_command(
            "firmware",
            "firmware_command",
            {
                "properties": {
                    "name": "firmware_command",
                    "value": method,
                    "timestamp": None,
                    "at_bound": None,
                    "unit": None,
                    "writeable": True,
                    "supported_values": [
                        "idle",
                        "firmware_cancel",
                        "firmware_flash",
                        "firmware_upload",
                        "unsupported",
                    ],
                    "ability": "ca1e3797-9bfc-3f26-972a-cfaafad82507",
                }
            },
        )

    def upload_firmware(self):
        self.firmware_command("firmware_upload")

    def firmware_cancel(self):
        self.firmware_command("firmware_cancel")

    def firmware_flash(self):
        self.firmware_command("firmware_flash")


# https://sg-api.dss.husqvarnagroup.net/sg-1/devices/282555da-2b13-4f51-8b59-d9097e74e248/abilities/firmware/properties/firmware_command?locationId=753aecac-4c46-440e-aa96-d92436a11e77
# {"properties":{"name":"firmware_command","value":"firmware_upload","timestamp":null,"at_bound":null,"unit":null,"writeable":true,"supported_values":["idle","firmware_cancel","firmware_flash","firmware_upload","unsupported"],"ability":"ca1e3797-9bfc-3f26-972a-cfaafad82507"}}
