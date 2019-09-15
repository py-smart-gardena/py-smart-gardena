from .base_service import BaseService


class Valve(BaseService):
    def update_service(self, message):
        self.update_attribute_in_map(message["attributes"]["activity"], "activity")
        self.update_attribute_in_map(message["attributes"]["name"], "name")
        self.update_attribute_in_map(message["attributes"]["state"], "state")
