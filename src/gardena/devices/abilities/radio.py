from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class RadioAbility(BaseGardenaAbilityClass):

    # Radio fields
    radio_abilities = {
        "radio_link": {
            "quality": "radio_quality",
            "connection_status": "radio_connection_status",
            "state": "radio_state",
        }
    }

    def __init__(self, smart_system=None, location=None):
        super(RadioAbility, self).__init__(smart_system=smart_system, location=location)
        self.register_abilities(self.radio_abilities)
        self.radio_quality = None
        self.radio_connection_status = None
        self.radio_state = None
        self.device_state = None

    def get_all_info(self):
        values = {
            "radio_quality": self.radio_quality,
            "radio_connection_status": self.radio_connection_status,
            "radio_state": self.radio_state,
        }
        return {**super(RadioAbility, self).get_all_info(), **values}
