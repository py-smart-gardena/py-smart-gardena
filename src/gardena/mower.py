class Mower:
    """Class to communicate with a mower"""

    def __init__(self, smart_system=None):
        """Constructor, create instance of gateway"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        self.smart_system = smart_system
