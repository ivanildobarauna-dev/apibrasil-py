from api_brasil.api_client.client_builder import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature


class WhatsAppApi(APIBrasilFeature):
    def __init__(self, api_brasil_client: APIBrasilClient): 
        self.api_brasil_client = api_brasil_client

    def execute(self, message: str, phone_number: str):
        print('Executing WhatsAppApi')
        print(f"Received creds: {self.api_brasil_client.get_credentials()}")
        print('VehiclesApi WhatsAppApi')