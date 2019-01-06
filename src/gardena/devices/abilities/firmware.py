from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class FirmwareAbility(BaseGardenaAbilityClass):

    firmware_status = None
    firmware_upload_progress = 0
    firmware_update_start = False
    firmware_abilities = {
        "firmware": {
            "firmware_status": "firmware_status",
            "firmware_upload_progress": "firmware_upload_progress",
            "firmware_update_start": "firmware_update_start",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(FirmwareAbility, self).__init__(
            smart_system=smart_system, location=location
        )
        self.register_abilities(self.firmware_abilities)
