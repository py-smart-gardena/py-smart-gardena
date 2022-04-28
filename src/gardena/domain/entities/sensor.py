from .base_device import BaseDevice
from .device_type import DeviceType


class Sensor(BaseDevice):
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
        ambient_temperature: str = "N/A",
        light_intensity: str = "N/A",
        soil_humidity: str = "N/A",
        soil_temperature: str = "N/A",
    ):
        """Constructor for the sensor device."""
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
        self.type: DeviceType = DeviceType.SENSOR
        self.ambient_temperature: str = ambient_temperature
        self.light_intensity: str = light_intensity
        self.soil_humidity: str = soil_humidity
        self.soil_temperature: str = soil_temperature
        self.battery_level: str = battery_level
        self.battery_state: str = battery_state
