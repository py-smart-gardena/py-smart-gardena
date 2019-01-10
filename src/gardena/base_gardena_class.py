class BaseGardenaClass:
    """Base class for information retrieved by gardena"""

    def __init__(self, smart_system=None):
        """Constructor, create instance of a gardena object"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        self.smart_system = smart_system
        self.id = None
        self.name = None

    def set_field_if_exists(self, hashmap, hashmap_key, field_name):
        if hashmap_key in hashmap and hasattr(self, field_name):
            setattr(self, field_name, hashmap[hashmap_key])

    def update_information(self, information):
        self.set_field_if_exists(information, "id", "id")
        self.set_field_if_exists(information, "name", "name")

    def get_all_info(self):
        values = {"id": self.id, "name": self.name}
        return values
