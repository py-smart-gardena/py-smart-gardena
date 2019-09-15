from .base_service import BaseService


class Common(BaseService):
    def update_service(self, message):
        self.update_attribute_in_map(
            message["attributes"]["batteryState"], "battery_state"
        )
        self.update_attribute_in_map(message["attributes"]["modelType"], "model_type")
        self.update_attribute_in_map(message["attributes"]["name"], "name")
        self.update_attribute_in_map(
            message["attributes"]["rfLinkLevel"], "rfLinkLevel"
        )
        self.update_attribute_in_map(
            message["attributes"]["rfLinkState"], "rfLinkState"
        )
        self.update_attribute_in_map(message["attributes"]["serial"], "serial")
