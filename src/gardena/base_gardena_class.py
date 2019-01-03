class BaseGardenaClass:
    """Base class for information retrieved by gardena"""

    def __init__(self, smart_system=None, api_information=None):
        """Constructor, create instance of a gardena device"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        if api_information is None:
            raise ValueError("Argument 'api_information' is missing")
        self.smart_system = smart_system
        self.api_information = api_information

    def get_id(self):
        return self.api_information["id"]

    def get_name(self):
        return self.api_information["name"]
