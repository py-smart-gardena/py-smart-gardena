class Location:
    def __init__(self, smart_system=None, location_info=None):
        """Constructor, create instance of a gardena device"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        if location_info is None:
            raise ValueError("Argument 'location_info' is missing")
        self.smart_system = smart_system
        self.location_info = location_info

    def get_id(self):
        return self.location_info["id"]

    def get_name(self):
        return self.location_info["name"]
