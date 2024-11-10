from api_brasil import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature


class VehiclesApi(APIBrasilFeature):
    def __init__(self, api_brasil_client: APIBrasilClient):
        self.api_brasil_client = api_brasil_client

    def execute(self):
        print('Executing VehiclesApi')
        print(f"Received creds: {self.api_brasil_client.get_credentials()}")
        print('VehiclesApi executed')