class GardenaBaseDeviceApi:
    def __init__(self):
        """Constructor for the BaseDevice."""
        self.id = None
        self.type = "N/A"
        self.name = "N/A"
        self.rf_link_level = "N/A"
        self.rf_link_state = "N/A"
        self.serial = "N/A"
        self.model_type = "N/A"

    def setup_values_from_device_map(self, device_map):
        for messages_list in device_map.values():
            for message in messages_list:
                self.update_data(message)

    def update_data(self, message):
        if message["type"] == "COMMON":
            self.update_common_data(message)
        self.update_device_specific_data(message)

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

    def update_device_specific_data(self, message):
        pass
