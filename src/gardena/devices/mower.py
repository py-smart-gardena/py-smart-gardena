from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class Mower(BaseGardenaDeviceClass):
    """Class to communicate with a mower"""

    internal_temperature = None
    mower_manual_operation = None
    mower_status = None
    mower_timestamp_next_start = None

    """Used to map data between 'mower' ability fields and class fields"""
    mower_ability_fields = {
        "manual_operation": "mower_manual_operation",
        "status": "mower_status",
        "timestamp_next_start": "mower_timestamp_next_start",
    }

    temperature_ability_fields = {"temperature": "internal_temperature"}

    mower_ability_type_maps = {
        "robotic_mower": mower_ability_fields,
        "internal_temperature_sensor": temperature_ability_fields,
    }

    def get_device_specific_ability_type_maps(self):
        return self.mower_ability_type_maps

    def park_until_next_timer(self):
        self.call_command("mower", {"name": "park_until_next_timer"})

    def park_until_further_notice(self):
        self.call_command("mower", {"name": "park_until_further_notice"})

    def start_resume_schedule(self):
        self.call_command("mower", {"name": "start_resume_schedule"})

    def start_override_timer(self, duration=240):
        self.call_command(
            "mower",
            {"name": "start_override_timer", "parameters": {"duration": duration}},
        )
