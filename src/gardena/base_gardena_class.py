class BaseGardenaClass:
    """Base class for information retrieved by gardena"""

    def _update_field_if_exists(self, array, field_name, value):
        if value is not None:
            self.data[field_name] = value
