class BaseGardenaDevice:
    def __init__(self, smart_system=None, device_info=None):
        """Constructor, create instance of a gardena device"""
        if smart_system is None:
            raise ValueError("Argument 'smart_system' is missing")
        if device_info is None:
            raise ValueError("Argument 'device_info' is missing")
        self.smart_system = smart_system
        self.device_info = device_info
