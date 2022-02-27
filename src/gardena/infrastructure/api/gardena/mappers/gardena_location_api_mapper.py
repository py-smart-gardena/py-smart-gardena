from gardena.domain.entities.location import Location


class GardenaLocationApiMapper:
    @staticmethod
    def to_location(data) -> Location:
        return Location(id=data["id"], name=data["attributes"]["name"])
