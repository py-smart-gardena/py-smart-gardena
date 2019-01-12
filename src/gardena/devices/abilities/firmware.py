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
