class Location:
    """Keep informations about gardena locations (gardens, ..) and devices"""

    def __init__(self, id: str = "N/A", name: str = "N/A", devices={}):
        self.id = id
        self.name = name
        self.devices = devices
