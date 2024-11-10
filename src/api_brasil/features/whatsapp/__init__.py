from api_brasil.api_client.client_builder import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature
import requests

class WhatsAppApi(APIBrasilFeature):
    def __init__(self, 
                 api_brasil_client: APIBrasilClient,
                 time_typing: int =1):
         
        self.api_brasil_client = api_brasil_client
        self.time_typing = time_typing 

    def set_phone_number(self,phone_number: str):
        self.phone_number  = phone_number

    def send_text(message: str):
        pass  

    def send_file():
        pass
