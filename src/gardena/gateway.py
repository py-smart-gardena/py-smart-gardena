class Gateway:
    """Class to communicate with smart gateway and handle network calls"""

    def __init__(self, smart_system=None):
        """Constructor, create instance of gateway"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        self.smart_system = smart_system
