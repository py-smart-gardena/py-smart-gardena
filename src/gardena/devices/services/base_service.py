class BaseService:
    id = None
    data = {}

    def __init__(self, id):
        self.id = id

    def update_service(self, message):
        print("BaseService update_service called ... no implementation found")

    def update_attribute_in_map(self, value, field_name):
        if value is not None:
            self.data[field_name] = value["value"]

    def __str__(self):
        str = "{"
        for key, value in self.data.items():
            str += f"{key} : {value}, "
        str += "}"
        return str
