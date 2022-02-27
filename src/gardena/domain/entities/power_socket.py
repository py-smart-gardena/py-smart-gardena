from .base_device import BaseDevice
from .device_type import DeviceType


class PowerSocket(BaseDevice):
    def __init__(
        self,
        id: str = "None",
        name: str = "N/A",
        rf_link_level: str = "N/A",
        rf_link_state: str = "N/A",
        serial: str = "N/A",
        model_type: str = "N/A",
        callbacks=[],
        activity: str = "N/A",
        state: str = "N/A",
        last_error_code: str = "N/A",
    ):
        """Constructor for the Power socket device."""
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
        self.type: DeviceType = DeviceType.POWER_SOCKET
        self.activity: str = activity
        self.state: str = state
        self.last_error_code: str = last_error_code
