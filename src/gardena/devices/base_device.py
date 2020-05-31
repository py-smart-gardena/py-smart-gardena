from gardena.base_gardena_class import BaseGardenaClass


class BaseDevice(BaseGardenaClass):
    """Base class informations about gardena devices"""

    id = "N/A"
    type = "N/A"
    battery_level = "N/A"
    battery_state = "N/A"
    name = "N/A"
    rf_link_level = "N/A"
    rf_link_state = "N/A"
    serial = "N/A"
    model_type = "N/A"
    callbacks = []

    def __init__(self, smart_system, device_map):
        self.smart_system = smart_system
        # Only one common field
        self.id = device_map["COMMON"][0]["id"]
        for messages_list in device_map.values():
            for message in messages_list:
                self.update_data(message)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def update_data(self, device_map):
        if device_map["type"] == "COMMON":
            self.update_common_data(device_map)
        self.update_device_specific_data(device_map)
        for callback in self.callbacks:
            callback(self)

    def update_common_data(self, common_map):
        self.set_attribute_value("battery_level", common_map, "batteryLevel")
        self.set_attribute_value("battery_state", common_map, "batteryState")
        self.set_attribute_value("name", common_map, "name")
        self.set_attribute_value("rf_link_level", common_map, "rfLinkLevel")
        self.set_attribute_value("rf_link_state", common_map, "rfLinkState")
        self.set_attribute_value("serial", common_map, "serial")
        self.set_attribute_value("model_type", common_map, "modelType")

    def set_attribute_value(self, field_name, attributes_map, attribute_name):
        if attribute_name in attributes_map["attributes"]:
            setattr(
                self, field_name, attributes_map["attributes"][attribute_name]["value"]
            )
