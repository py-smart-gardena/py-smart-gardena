from gardena.domain.entities.base_device import BaseDevice
from gardena.domain.entities.device_type import DeviceType


class Mower(BaseDevice):
    def __init__(
        self,
        id: str = None,
        battery_level: str = "N/A",
        battery_state: str = "N/A",
        name: str = "N/A",
        rf_link_level: str = "N/A",
        rf_link_state: str = "N/A",
        serial: str = "N/A",
        model_type: str = "N/A",
        callbacks=[],
        activity: str = "N/A",
        operating_hours: str = "N/A",
        state: str = "N/A",
        last_error_code: str = "N/A",
    ):
        """Constructor for the mower device."""
        BaseDevice.__init__(
            self,
            id=id,
            name=name,
            rf_link_level=rf_link_level,
            rf_link_state=rf_link_state,
            serial=serial,
            model_type=model_type,
            callbacks=callbacks,
        )
        self.type: DeviceType = DeviceType.MOWER
        self.activity: str = activity
        self.operating_hours: str = operating_hours
        self.state: str = state
        self.last_error_code: str = last_error_code
        self.battery_level = battery_level
        self.battery_state = battery_state
