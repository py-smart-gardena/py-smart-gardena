from gardena.devices.abilities.base_gardena_ability_class import BaseGardenaAbilityClass


class RadioAbility(BaseGardenaAbilityClass):

    # Radio fields
    radio_quality = None
    radio_connection_status = None
    radio_state = None
    device_state = None
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
