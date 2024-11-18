""" Application feature to send messages to WhatsApp using the API Brasil. """
from api_brasil.api_client.client_builder import APIBrasilClient
from api_brasil.features.interfaces import APIBrasilFeature


class WhatsAppApi(APIBrasilFeature):
    """ The class is responsible for send messages to WhatsApp using the API Brasil. """
    def __init__(self,
                  api_brasil_client: APIBrasilClient,
                  device_token: str,
                  time_typing: int =1):
        super().__init__(api_brasil_client)
        self.api_brasil_client = api_brasil_client
        self.device_token = device_token
        self.time_typing = time_typing
        self.phone_number = None


    def to_number(self,phone_number: str):
        """ Set the phone number to send the message. """
        self.phone_number  = phone_number

    def send_message(self, message: str) -> dict:
        """ Send a message to the phone number set. """
        endpoint = "/whatsapp/sendText"

        response = self.api_brasil_client.post_request(
            endpoint=endpoint,
            device_token=self.device_token,
            body={
                "text": message,
                "number": self.phone_number,
                "time_typing": self.time_typing
            }
        )

        return response
    
    def send_file(self):
        """ Send a file to the phone number set. """
