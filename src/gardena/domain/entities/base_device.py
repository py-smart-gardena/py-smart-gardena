class BaseDevice:
    """Base class informations about gardena devices."""

    def __init__(self):
        """Constructor for the BaseDevice."""
        self.id: str = "None"
        self.type: str = "N/A"
        self.battery_level: str = "N/A"
        self.battery_state: str = "N/A"
        self.name: str = "N/A"
        self.rf_link_level: str = "N/A"
        self.rf_link_state: str = "N/A"
        self.serial: str = "N/A"
        self.model_type: str = "N/A"
        self.callbacks = []
