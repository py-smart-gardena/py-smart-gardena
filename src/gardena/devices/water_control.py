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
        self.call_command(
            "outlet",
            {
                "name": "manual_override",
                "parameters": {"manual_override": "open", "duration": duration},
            },
        )

    def close_valve(self):
        self.call_command("outlet", {"name": "cancel_override", "parameters": {}})
