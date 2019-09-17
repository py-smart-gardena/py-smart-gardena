class Service:
    data = {}
    type = None

    def update_service(self, message):
        for field in message["attributes"]:
            self.update_attribute_in_map(message, field)

    def update_attribute_in_map(self, message, field_name, data_field_name=None):
        if field_name in message["attributes"]:
            target_field_name = field_name
            if data_field_name is not None:
                target_field_name = data_field_name
            self.data[target_field_name] = message["attributes"][field_name]["value"]

    def __str__(self):
        str = "{"
        str += f'"type": {self.type}, '
        for key, value in self.data.items():
            str += f'"{key}" : {value}, '
        str += "}"
        return str
