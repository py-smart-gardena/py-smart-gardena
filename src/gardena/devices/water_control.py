from gardena.devices.base_gardena_device_class import BaseGardenaDeviceClass


class WaterControl(BaseGardenaDeviceClass):
    """Class to communicate with a water control device"""

    watering_valve_open = None
    watering_manual_override = None

    """Used to map data between 'watering' ability fields and class fields"""
    watering_outlet_ability_fields = {
        "valve_open": "watering_valve_open",
        "manual_override": "watering_manual_override",
    }

    water_control_ability_type_maps = {
        "watering_outlet": watering_outlet_ability_fields
    }

    def get_device_specific_ability_type_maps(self):
        return self.water_control_ability_type_maps

    def open_valve(self, duration=30):
        data = {
            "name": "manual_override",
            "parameters": {"manual_override": "open", "duration": duration},
        }
        self.smart_system.call_smart_system(
            url=self.get_ability_command_url("outlet"), request_type="post", data=data
        )

    def close_valve(self):
        data = {"name": "cancel_override", "parameters": {}}
        self.smart_system.call_smart_system(
            url=self.get_ability_command_url("outlet"), request_type="post", data=data
        )
