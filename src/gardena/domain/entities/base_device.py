class BaseDevice:
    """Base class informations about gardena devices."""

    def __init__(
        self,
        id: str = "None",
        name: str = "N/A",
        rf_link_level: str = "N/A",
        rf_link_state: str = "N/A",
        serial: str = "N/A",
        model_type: str = "N/A",
        callbacks=[],
    ):
        """Constructor for the BaseDevice."""
        self.rf_link_level = rf_link_level
        self.rf_link_state = rf_link_state
        self.serial = serial
        self.model_type = model_type
        self.callbacks = callbacks
        self.id = id
        self.name = name
