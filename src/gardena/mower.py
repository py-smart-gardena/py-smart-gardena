from gardena.base_gardena_device_class import BaseGardenaDeviceClass


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
