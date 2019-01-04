from gardena.base_gardena_device_class import BaseGardenaDeviceClass


class WaterControl(BaseGardenaDeviceClass):
    """Class to communicate with a sensor"""

    watering_valve_open = None
    watering_manual_override = None

    """Used to map data between 'mower' ability fields and class fields"""
    watering_outlet_ability_fields = {
        "valve_open": "watering_valve_open",
        "manual_override": "watering_manual_override",
    }

    def update_information(self, information):
        super(WaterControl, self).update_information(information)
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def update_specific_device_info(self, device_specific_information):
        if device_specific_information["type"] == "watering_outlet":
            self.set_ability_field(
                device_specific_information, self.watering_outlet_ability_fields
            )
