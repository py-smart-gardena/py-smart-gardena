from gardena.domain.entities.base_device import BaseDevice


class Mower(BaseDevice):
    def __init__(self):
        """Constructor for the mower device."""
        BaseDevice.__init__(self)
        self.type = "MOWER"
        self.activity: str = "N/A"
        self.operating_hours: str = "N/A"
        self.state: str = "N/A"
        self.last_error_code: str = "N/A"
