from gardena.domain.entities.location import Location


class GardenaLocationApi:
    def __init__(self):
        self.id = "N/A"
        self.name = "N/A"
        self.devices = {}

    def to_location(self) -> Location:
        location: Location = Location()
        location.id = self.id
        location.name = self.name
        location.devices = self.devices
        return location
