import os


class GardenaPersistenceConfiguration:
    def __init__(self, email: str = None, password: str = None, client_id: str = None):
        self.email = email or os.getenv("GARDENA_EMAIL")
        self.password = password or os.getenv("GARDENA_PASSWORD")
        self.client_id = client_id or os.getenv("GARDENA_CLIENT_ID")
