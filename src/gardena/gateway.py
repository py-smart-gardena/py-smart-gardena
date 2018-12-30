class Gateway:
    """Class to communicate with smart gateway and handle network calls"""

    def __init__(self, smart_system):
        """Constructor, create instance of gateway"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        self.smart_system = smart_system
